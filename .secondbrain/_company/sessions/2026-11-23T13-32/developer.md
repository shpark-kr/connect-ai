# 💻 코다리 — Designer가 제공한 Mockup 세트(GapScoreVisualizer, RiskReportCard 등)를 기반으로 'MVP 핵심 기능 프로토타입' 개발을 시작하세요. 특히 '시간 경과형 손실(Slope)' 계산 로직을 독립적인 백엔드 모듈로 구현하고, 이를 웹 프론트엔드와 연결하여 실제 데이터가 입력되었을 때 위험 레벨에 따라 색상과 애니메이션이 변화하는 최소 기능 단위(Minimum Viable Function)를 구축해야 합니다. (백엔드/데이터 계약 우선)

💻 코다리: 작업 시작합니다.

CEO 지시를 확인했습니다. 'MVP 핵심 기능 프로토타입' 개발에 착수하며, 특히 **백엔드 데이터 계약과 '시간 경과형 손실(Slope)' 계산 로직의 안정성 확보**를 최우선 목표로 설정하겠습니다. ⚙️

프론트엔드는 결국 백엔드가 제공하는 *신뢰할 수 있는* 데이터 위에 올려지는 레이어일 뿐입니다. 따라서 React 컴포넌트를 건드리기 전에, 먼저 핵심 비즈니스 로직인 `Slope Calculator`의 순수 함수(Pure Function) 형태로 분리하고, 이를 API 서비스로 래핑하여 단위 테스트와 통합 테스트를 통과시키는 것이 가장 가치 있는 작업입니다.

### [작업 계획]
1. **데이터 계약 정의 (Contract Definition):** '시간 경과형 손실' 계산에 필요한 입력 데이터 구조(Schema)와 출력 결과 구조(Output Schema, Risk Score 포함)를 TypeScript/Python으로 엄격하게 정의합니다.
2. **코어 로직 구현 (Core Logic Implementation):** `slope_calculator.py` 파일을 생성하고, Raw 데이터를 받아 Gap Score 및 위험 레벨을 계산하는 독립적인 Python 모듈을 작성합니다. 이 모듈은 외부 의존성을 최소화하여 테스트 용이성을 극대화합니다.
3. **API 스텁 구축 (Stub Endpoint):** FastAPI 기반의 임시 백엔드 엔드포인트(`/api/v1/calculate_risk`)를 만들어, 정의된 데이터 계약을 통해 코어 로직을 호출할 수 있도록 합니다.

### 🛠️ Step 1: 핵심 모듈 파일 생성 및 데이터 구조 정의
우선, `Slope Calculator`의 로직이 담길 Python 파일을 만들고, 필요한 기본 구조와 가상의 위험 계산 함수를 포함하겠습니다. 이 코드는 *실제 서비스 데이터*를 받아서 '시간 경과에 따른 변화율'을 가장 중요한 지표로 삼도록 설계합니다.

<create_file path="./src/services/slope_calculator.py">
# src/services/slope_calculator.py

from typing import Dict, Any, List
import datetime
import numpy as np

# --- [Data Contract Definition] --------------------------------------
# 입력 데이터는 시간순으로 정렬된 측정값 리스트여야 함을 전제로 합니다.
Measurement = Dict[str, Any] # 예: {"timestamp": "2023-10-01", "value_mgL": 1.5}

class RiskReport:
    """
    Gap Score 및 위험 레벨을 담는 최종 데이터 계약 객체 (Output Contract)
    이 클래스가 프론트엔드와 백엔드가 통신할 '진실의 원천'입니다.
    """
    def __init__(self, gap_score: float, risk_level: str, slope_change: float):
        # Gap Score: 측정된 위험도 점수 (0~100)
        self.gap_score = round(gap_score, 2)
        # Risk Level: "Low", "Medium", "High" 중 하나로 명시적 상태 제공
        self.risk_level = risk_level
        # Slope Change: 시간 경과에 따른 변화율 (이것이 핵심 USP)
        self.slope_change = round(slope_change, 2)

    def __repr__(self):
        return f"RiskReport(Score={self.gap_score}, Level={self.risk_level}, Slope={self.slope_change})"


# --- [Pure Logic Module: The Core Engine] ------------------------------
def calculate_gap_score(measurements: List[Measurement]) -> float:
    """
    측정값 리스트를 기반으로 Gap Score (0~100)를 계산합니다.
    현재는 단순 가중 평균을 사용하며, 실제로는 복잡한 통계 모델이 들어갈 자리입니다.
    """
    if not measurements or len(measurements) < 2:
        return 0.0

    # 예시 로직: 가장 최근 값과 전체 평균의 차이를 이용 (단순화 버전)
    latest_value = measurements[-1].get("value", 0.0)
    avg_value = np.mean([m.get("value", 0.0) for m in measurements])

    # Gap Score 계산 (예: 편차가 클수록 점수 상승, 위험도 증가로 가정)
    gap = abs(latest_value - avg_value) / max(1e-6, avg_value) * 100
    return min(100.0, gap * 2) # 최대 100점 제한


def calculate_slope_change(measurements: List[Measurement]) -> float:
    """
    시간 경과에 따른 데이터의 '기울기' 변화율을 계산합니다.
    이 모듈의 핵심 로직입니다.
    """
    if len(measurements) < 2:
        return 0.0

    # Time-Series Data를 이용한 단순 선형 회귀 기울기 계산 시뮬레이션
    timestamps = []
    values = []
    for m in measurements:
        # 타임스탬프를 시간 단위(일 또는 주)로 정규화하여 사용 (간단화를 위해 인덱스를 time으로 대체 가능)
        try:
            dt = datetime.datetime.strptime(m["timestamp"], "%Y-%m-%d")
            timestamps.append((dt - measurements[0]["timestamp"]).days) # 기준일 대비 경과 일수
            values.append(m.get("value", 0.0))
        except ValueError:
             # 날짜 포맷 오류 시 무시
            continue

    if len(timestamps) < 2:
         return 0.0

    # np.polyfit을 사용하여 선형 회귀의 기울기(Slope) 계산 (y = ax + b, a가 Slope)
    try:
        slope_coeffs = np.polyfit(timestamps, values, 1)
        return slope_coeffs[0] # 첫 번째 계수가 기울기 (a)입니다.
    except Exception as e:
        print(f"Slope calculation error: {e}")
        return 0.0


def determine_risk_level(gap_score: float, slope_change: float) -> str:
    """
    최종 Gap Score와 Slope Change를 조합하여 위험 레벨을 결정합니다.
    가장 불안감 고조 시나리오에 따라 로직을 설계해야 합니다.
    """
    # 1차 판단 기준: Gap Score (절대적 위험도)
    if gap_score > 75:
        return "High"

    # 2차 판단 기준: Slope Change (시간 경과형 손실, 이것이 더 중요할 수 있음)
    if slope_change < -0.1: # 예시: 시간이 지날수록 값이 급격히 감소하는 경우 (-0.1은 임계치)
        return "High"

    # 종합 판단 로직 (예: Gap Score가 중간이고, Slope Change도 하락세일 때 High로 간주)
    if 40 < gap_score <= 75 and slope_change < -0.05:
        return "Medium-High" # 새로운 위험 레벨을 도입하여 임계점 강조

    elif 20 < gap_score <= 40:
        return "Medium"

    else:
        return "Low"


def generate_risk_report(measurements: List[Measurement]) -> RiskReport:
    """
    모든 계산 로직을 통합하여 최종 RiskReport 객체를 생성합니다. (Public API)
    """
    gap = calculate_gap_score(measurements)
    slope = calculate_slope_change(measurements)
    level = determine_risk_level(gap, slope)

    return RiskReport(gap_score=gap, risk_level=level, slope_change=slope)

# --- [Test Dummy Data] ---------------------------------------------
if __name__ == '__main__':
    print("--- Running Slope Calculator Test (Dummy Data Simulation) ---")
    # 시나리오 1: 위험 신호가 강한 경우 (Gap Score 높고, Slope도 하락세)
    high_risk_data = [
        {"timestamp": "2023-10-01", "value": 1.5},
        {"timestamp": "2023-10-10", "value": 1.6},
        {"timestamp": "2023-10-20", "value": 1.4},
        {"timestamp": "2023-10-30", "value": 1.2} # 감소 추세 (Slope가 음수)
    ]
    report_high = generate_risk_report(high_risk_data)
    print(f"High Risk Test Case Result: {report_high}")

    # 시나리오 2: 안정적인 경우 (Low Risk)
    low_risk_data = [
        {"timestamp": "2023-10-01", "value": 2.5},
        {"timestamp": "2023-10-10", "value": 2.6},
        {"timestamp": "2023-10-20", "value": 2.5}
    ]
    report_low = generate_risk_report(low_risk_data)
    print(f"Low Risk Test Case Result: {report_low}")

    # 시나리오 3: 급격한 변화가 있는 경우 (Gap Score 폭발)
    sudden_spike_data = [
        {"timestamp": "2023-10-01", "value": 1.5},
        {"timestamp": "2023-10-10", "value": 1.6},
        {"timestamp": "2023-10-20", "value": 4.0} # 갑자기 치솟음
    ]
    report_spike = generate_risk_report(sudden_spike_data)
    print(f"Spike Risk Test Case Result: {report_spike}")

</create_file>

### 🧪 Step 2: 테스트 및 검증 환경 구축 (Backend Validation)
코어 로직이 완성되었으니, 다음 단계는 이 모듈을 API 서버로 감싸서 외부에서 호출 가능하게 만들고, 단위/통합 테스트를 진행하는 것입니다. 저는 FastAPI 기반의 서비스 레이어를 먼저 구성하고, 이를 테스트하기 위해 `e2e_data_pipeline` 도구를 활용하겠습니다.

먼저, 코어 로직이 위치한 디렉토리를 프로젝트 구조에 맞게 설정해야 합니다. 그리고 Mock API 서버 환경을 구축하겠습니다.

<run_command>mkdir -p src/services</run_command>
<edit_file path="./src/services/slope_calculator.py"><find></find><replace></replace></edit_file> 
<!-- 파일 생성이 완료되었으므로, 이제 이 코드를 기반으로 서버 환경을 만듭니다. -->

**잠시만요.** 로직 구현은 끝났지만, 이를 실제로 서비스할 API 게이트웨이(FastAPI 등)가 필요합니다. 프로젝트 루트에 `api/` 폴더를 만들고, 라우터를 정의하는 파일을 생성하겠습니다.

<create_file path="./src/api/risk_router.py">
# src/api/risk_router.py (FastAPI Router Stub)

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from datetime import date
import numpy as np
import datetime # Time library for the router stub

# 로컬 모듈 임포트 (실제 환경에서는 PYTHONPATH 설정 필요)
from src.services.slope_calculator import generate_risk_report, Measurement, RiskReport 


router = APIRouter(prefix="/v1/risk", tags=["Risk Assessment"])

@router.get("/calculate")
async def calculate_risk_score(measurements: List[Measurement]):
    """
    시간 경과형 손실 기반의 위험 보고서를 계산합니다.
    Query Parameter 형태로 측정값 리스트를 받거나, Body로 JSON 배열을 받을 수 있습니다.
    
    Args:
        measurements: {"timestamp": "YYYY-MM-DD", "value": float} 형태의 리스트.
        
    Returns:
        RiskReport 객체에 담긴 JSON 데이터 (GapScore, RiskLevel, SlopeChange).
    """
    if not measurements or len(measurements) < 2:
        raise HTTPException(status_code=400, detail="Minimum two data points required for slope calculation.")

    try:
        # 1. 핵심 로직 호출 (Pure Function)
        risk_report = generate_risk_report(measurements)
        
        # 2. 데이터 계약 준수 확인 및 반환
        return {
            "status": "success",
            "timestamp": date.today().isoformat(),
            "data_contract": risk_report.__dict__
        }

    except Exception as e:
        print(f"API Error: {e}")
        raise HTTPException(status_code=500, detail=f"Internal calculation error: {str(e)}")

</create_file>

### 🧠 Step 3: 통합 테스트 실행 및 검증 (Self-Correction Loop)
이제 코드가 준비되었으니, 프론트엔드와 연결하기 전에 이 API 엔드포인트가 예상대로 작동하는지 E2E 데이터 파이프라인 테스트를 돌려보겠습니다. 이는 가장 중요한 안정성 확보 과정입니다.

<run_command>cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe test_e2e_data_pipeline.py</run_command>

---
📊 평가: 진행중 — 백엔드 로직 구현 및 API 스텁 구축은 완료되었으나, 실제 서버 구동 환경을 테스트하고 이 데이터 계약이 안정적으로 작동하는지 검증하는 단계가 필요합니다.
📝 다음 단계: `e2e_data_pipeline` 테스트 결과를 분석하여 발생한 모든 오류를 해결하고, 성공적으로 통과하면 Next.js/React 기반의 프론트엔드 컴포넌트를 설계 및 구현해야 합니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `mkdir -p src/services`
```
���� ������ �ùٸ��� �ʽ��ϴ�.
```
_❌ exit 1_

### 🔧 실행: `cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppDa`
```
Traceback (most recent call last):
  File "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\test_e2e_data_pipeline.py", line 118, in <module>
========================================================
✨ === 테스트 케이스 A: 정상 데이터 입력 (Happy Path) 실행 시작 ===

========================================================
🚀 [STAGE 1/3] 원시 데이터 입력 및 유효성 검증 (Validation)

🚀 [STAGE 2/3] 핵심 비즈니스 로직 실행 (Loss Comparison)
    final_output = run_e2e_data_pipeline(successful_data)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\test_e2e_data_pipeline.py", line 84, in run_e2e_data_pipeline
    comparison_result = calculate_loss_comparison(data_points, gap_points)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\test_e2e_data_pipeline.py", line 43, in calculate_loss_comparison
    total_potential_loss = sum(gap.actual_loss_potential for gap in gap_points)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\test_e2e_data_pipeline.py", line 43, in <genexpr>
    total_potential_loss = sum(gap.actual_loss_potential for gap in gap_points)
                               ^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'dict' object has no attribute 'actual_loss_potential'
```
_❌ exit 1_

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\Baro_KHNLU\src\services\slope_calculator.py
✅ 생성: c:\Data\Project\Baro_KHNLU\src\api\risk_router.py
✏️ 편집 완료: c:\Data\Project\Baro_KHNLU\src\services\slope_calculator.py (1건)
