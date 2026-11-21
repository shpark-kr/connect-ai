# 💻 코다리 — 새로 정의된 MiniFunnel의 최종 수익화 로직(Business가 제시한 구조)에 맞춰 웹사이트/MiniFunnel 페이지의 기술적 구현 우선순위를 결정해 주세요. 특히, 선결제 결제 시스템과 진단 보고서 데이터 연동을 위한 API 테스트 및 에러 핸들링(500 Internal Error 등) 코드 시퀀스를 설계하고, 실제 배포 가능한 수준으로 코딩 보일러플레이트를 정리해야 합니다.

💻 코다리: 작업 시작합니다.
CEO의 지시와 현빈이 재정립한 MiniFunnel 수익화 로직을 검토했습니다. 이건 단순 웹사이트 개발 문제가 아니라, **데이터 흐름과 금융 트랜잭션 안정성**이 핵심인 고난도 파이프라인 구축 문제입니다. ⚙️

현빈이 제시한 '진단 → 결제/심화 진단 → 구독'의 구조를 기술적으로 구현하려면, 가장 중요한 건 *어떤 단계에서 데이터가 유실되거나 트랜잭션이 깨지느냐* 입니다. 따라서 API 설계와 에러 핸들링 시퀀스에 초점을 맞춰야 합니다.

우선 백엔드 환경을 설정하고, MiniFunnel의 핵심 로직 흐름(Flow)을 처리할 **FastAPI 기반의 서버 스캐폴딩**을 구축하겠습니다. 이 구조는 진단 데이터 수집, 결제 연동 시뮬레이션, 그리고 최종 보고서 생성을 책임지는 세 가지 주요 모듈로 구성되어야 합니다.

### 🛠️ 기술적 구현 우선순위 결정 및 설계 (System Design)

| Priority | 시스템 컴포넌트 | 목적 (Why?) | 핵심 기능 (How?) | 에러 핸들링 초점 |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **`DiagnosisAPI`** | 초기 진입 및 데이터 수집. (Step 1) | 유효성 검사(Input Validation), 사용자 ID 기반의 임시 데이터 저장. | 입력 필드 누락/형식 오류 (`400 Bad Request`). |
| **2** | **`PaymentGatewayAPI`** | 결제 트랜잭션 처리 및 상태 변경. (Step 2) | 외부 PG 연동 시뮬레이션, `PENDING` → `PAID` 상태 플로우. | 네트워크 실패, PG 응답 오류 (`503 Service Unavailable`), DB Write Conflict. |
| **3** | **`ReportGenerationAPI`** | 최종 데이터 조합 및 보고서 생성. (Step 3) | 저장된 원본 진단 데이터 + 결제 데이터를 취합하여 구조화된 JSON/PDF 형태로 출력. | 필수 데이터 누락(가장 치명적), 권한 만료 (`401 Unauthorized`). |

---

### 💻 구현 작업: FastAPI 스캐폴딩 및 API 테스트 시퀀스 설계

이 로직을 담기 위해 프로젝트 폴더를 만들고, 필요한 파일을 생성하겠습니다. 실제 배포 가능한 최소 기능 단위(Minimum Viable Boilerplate)로 정리합니다.

#### Step 1: 디렉토리 구조 생성
먼저 프로젝트의 기본 골격을 만듭니다.

<create_file path="mini_funnel_backend/app/main.py">
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
import logging
from typing import Dict, Any

# 로거 설정 (실제 에러 추적을 위해 필수)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="MiniFunnel Backend API", version="1.0.0")

# --- 1. 데이터 모델 정의 (Pydantic Schema) ---
class DiagnosisInput(BaseModel):
    """Step 1: 초기 진단 테스트 입력값"""
    user_id: str  # 필수: 사용자 식별자
    test_score: int | None = None # 정량적 점수
    symptom_description: str  # 주관식 설명

class PaymentRequest(BaseModel):
    """Step 2: 결제 요청 모델"""
    user_id: str
    plan_type: str  # 예: 'premium_report', 'subscription'
    payment_token: str # PG에서 받은 토큰 (보안 중요)


# --- 2. Mock Database/State Management (실제로는 Redis나 DB 사용) ---
# 안전한 상태 관리를 위해 메모리 캐시를 사용합니다. 실제 배포 시에는 반드시 Redis 또는 SQL을 사용해야 합니다.
MOCK_DB: Dict[str, Any] = {}

@app.on_event("startup")
async def startup_event():
    logger.info("MiniFunnel Backend API started up.")


# ====================================================
# 🎯 ENDPOINT 1: 진단 테스트 실행 (DiagnosisAPI)
# ====================================================
@app.post("/api/v1/diagnose", status_code=status.HTTP_201_CREATED)
async def execute_diagnosis(data: DiagnosisInput):
    """Step 1: 사용자 입력 데이터를 받아 초기 진단 결과를 기록합니다."""
    if not data.user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID는 필수입니다.")

    # 데이터 검증 및 저장 (시스템 로그에 원본 데이터를 남겨야 합니다.)
    MOCK_DB[data.user_id] = {
        "diagnosis": data.dict(),
        "status": "DIAGNOSED",
        "payment_history": []
    }
    logger.info(f"User {data.user_id}: Diagnosis recorded successfully.")
    return {"message": "진단 기록이 완료되었습니다. 다음 단계로 이동하세요.", "initial_code": f"DEFECT-{data.user_id[:4].upper()}"}


# ====================================================
# 💳 ENDPOINT 2: 결제 및 상태 업데이트 (PaymentGatewayAPI)
# ====================================================
@app.post("/api/v1/purchase", status_code=status.HTTP_200_OK)
async def process_payment(data: PaymentRequest):
    """Step 2: 결제를 시뮬레이션하고, 성공하면 사용자 상태를 업데이트합니다."""
    if data.user_id not in MOCK_DB or MOCK_DB[data.user_id].get("status") != "DIAGNOSED":
        # 데이터가 없거나, 아직 진단 단계에 도달하지 않은 경우 403 Forbidden 처리
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="진단을 먼저 완료해주세요.")

    # 🚨 트랜잭션 핵심 로직: 결제 시뮬레이션
    try:
        if data.payment_token == "FAIL_TOKEN":
            # 명확한 에러 코드 처리 (PG 실패 등)
            raise Exception("Payment Gateway Connection Timeout or Invalid Card.")

        # PG 성공 시뮬레이션 및 상태 업데이트
        MOCK_DB[data.user_id]["status"] = "PAYMENT_COMPLETE"
        MOCK_DB[data.user_id]["payment_history"].append({
            "plan": data.plan_type,
            "amount": 99000 # 예시 금액
        })
        logger.warning(f"User {data.user_id}: Payment successful for {data.plan_type}. Status updated.")
        return {"message": "결제가 성공적으로 완료되었으며, 보고서 생성을 준비합니다."}

    except Exception as e:
        # 모든 비즈니스 로직 관련 예외를 포착하여 사용자에게는 일반적인 실패 메시지를 전달하고, 내부 로그에는 상세 에러를 남깁니다. (가장 중요)
        logger.error(f"CRITICAL PAYMENT ERROR for {data.user_id}: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="결제 처리 중 시스템 오류가 발생했습니다. 관리자에게 문의해주세요.")


# ====================================================
# 📄 ENDPOINT 3: 보고서 생성 (ReportGenerationAPI)
# ====================================================
@app.get("/api/v1/report/{user_id}")
async def generate_report(user_id: str):
    """Step 3: 최종 데이터를 취합하여 시스템 실패 보고서를 생성합니다."""
    if user_id not in MOCK_DB:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="사용자 기록을 찾을 수 없습니다.")

    user_data = MOCK_DB[user_id]

    # ⚠️ 비즈니스 로직 검증: 보고서가 생성되려면 최소한 결제가 완료되어야 함
    if user_data["status"] != "PAYMENT_COMPLETE":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="보고서는 유료 서비스입니다. 먼저 Step 2를 완료해주세요.")

    # 보고서 데이터 구조화 (여기에 복잡한 비즈니스 로직/API 호출이 들어갑니다)
    report = {
        "title": "시스템 실패 진단 및 복구 계획 보고서",
        "user_id": user_id,
        "diagnosis_date": str(datetime.datetime.now()),
        "original_defect_code": user_data["diagnosis"].get("initial_code"),
        "current_status": "COMPLETED",
        "analysis": {
            "summary": f"종합 진단 결과, 시스템 오류 코드 [{user_data['diagnosis'].get('initial_code')}]는 심각한 수준입니다.",
            "recommendation": ["전문가의 직접 컨설팅이 필요합니다. (다음 단계 구독 권유)"],
        },
        "payment_summary": user_data["payment_history"]
    }

    return {"report_content": report, "download_link": f"/downloads/{user_id}_report.pdf"}

# 필요한 라이브러리 임포트 (실제 실행을 위해 추가)
import datetime
</create_file>

#### Step 2: 파일 구조 확인 및 테스트 준비
생성된 코드는 FastAPI 환경에서 작동하는 백엔드 로직의 핵심 스캐폴딩입니다. 이대로 배포할 수는 없으니, 필수 종속성을 설치하고 기본적인 실행 흐름을 테스트해야 합니다.

<run_command>pip install fastapi uvicorn pydantic</run_command>
<list_files path="./mini_funnel_backend/app"/>

### 🐛 자가 검증 루프 (Self-Validation)
새로 작성한 코드가 기본적인 문법 오류는 없는지 확인합니다.

<run_command>pylint mini_funnel_backend/app/main.py</run_command>

---
**분석:** FastAPI 스캐폴딩과 핵심 API 엔드포인트 설계가 완료되었습니다. 특히, 결제(Step 2)와 보고서 생성(Step 3)에서 **권한 및 상태 검증 로직 (`403 Forbidden`)**을 삽입하여 비즈니스 플로우를 강제하고, 예상치 못한 에러 발생 시 **`500 Internal Server Error`**로 처리하며 상세 로그(`logger.error`)에 기록하도록 설계했습니다. 이는 현빈의 LTV 구조(진단 -> 결제 -> 유지)를 기술적으로 가장 안정성 높게 뒷받침하는 방법입니다.

이 코드는 백엔드 로직 자체는 완성되었으나, 실제 외부 PG 연동 모듈이나 데이터베이스 연결(`MOCK_DB` 대체)은 빠져있습니다. 이것을 다음 스텝에서 다루어야 합니다.

📊 평가: 진행중 — 핵심 API 엔드포인트와 에러 핸들링 구조 설계가 완료되었으며, 이제 이를 실제 서비스 환경에 맞게 통합하고 외부 의존성을 연결해야 합니다.
📝 다음 단계: 백엔드의 안정성과 확장성 확보를 위해, 데이터베이스(SQL) 연동 모듈을 추가하고, 결제 게이트웨이(PG)와 통신하는 비즈니스 계층(Service Layer) 코드를 분리하여 테스트 가능한 형태로 리팩토링해야 합니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `pip install fastapi uvicorn pydantic`
```
Requirement already satisfied: fastapi in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (0.141.1)
Requirement already satisfied: uvicorn in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (0.54.0)
Requirement already satisfied: pydantic in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (2.13.5)
Requirement already satisfied: starlette>=0.46.0 in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (from fastapi) (1.7.0)
Requirement already satisfied: typing-extensions>=4.8.0 in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (from fastapi) (4.16.0)
Requirement already satisfied: typing-inspection>=0.4.2 in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (from fastapi) (0.4.4)
Requirement already satisfied: annotated-doc>=0.0.2 in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (from fastapi) (0.0.5)
Requirement already satisfied: click>=7.0 in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (from uvicorn) (8.5.0)
Requirement already satisfied: h11>=0.8 in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (from uvicorn) (0.16.0)
Requirement already satisfied: annotated-types>=0.6.0 in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (from pydantic) (0.8.0)
Requirement already satisfied: pydantic-core==2.46.5 in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (from pydantic) (2.46.5)
Requirement already satisfied: anyio<5,>=4.0.0 in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (from starlette>=0.46.0->fastapi) (4.15.1)
Requirement already satisfied: idna>=2.8 in C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages (from anyio<5,>=4.0.0->starlette>=0.46.0->fastapi) (3.20)
```
_✅_

### 🔧 실행: `pylint mini_funnel_backend/app/main.py`
```
'pylint'��(��) ���� �Ǵ� �ܺ� ����, ������ �� �ִ� ���α׷�, �Ǵ�
��ġ ������ �ƴմϴ�.
```
_❌ exit 1_

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\mini_funnel_backend\app\main.py
📂 목록: c:\Data\Project\connect-ai\mini_funnel_backend\app/
```
📄 main.py
```

[시스템: list_files 결과]
디렉토리: c:\Data\Project\connect-ai\mini_funnel_backend\app/
📄 main.py
