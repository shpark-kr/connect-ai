# 💻 코다리 — business가 정의한 '온라인 간이 자가 검진 시뮬레이션'의 핵심 로직(Input-Process-Output)을 기반으로, 사용자 경험을 고려한 초기 프론트엔드 와이어프레임 및 데이터 수집 API 엔드포인트 초안을 작성하고, 이 기능 구현에 필요한 최소한의 기술 스펙 문서를 준비하시오.

💻 코다리: 작업 시작합니다.

CEO님의 지시를 받았습니다. 단순히 '화면을 그려주는' 수준이 아니라, 실제로 운영 가능한 서비스를 위한 **최소 기능 제품(MVP) 구현에 필요한 엔지니어링 스펙**을 짜는 것이 핵심입니다. ⚙️

Mini-App은 우리 비즈니스의 가장 중요한 전환점입니다. 여기서 UX나 API 설계가 깨지면 모든 리드 수집 파이프라인이 무너지는 겁니다. 따라서 단순한 UI 제안 대신, **구현 가능성(Feasibility)**과 **확장성(Scalability)**에 초점을 맞춰 다음 세 가지 산출물을 제시합니다.

---

## 📄 [산출물 1] 온라인 간이 자가 검진 시뮬레이션 와이어프레임 (UX/UI Flow)

**목표:** 사용자가 '학습'하는 느낌을 받으면서도, 체계적으로 데이터를 입력하게 유도하고, 마지막에 강력한 정보 격차(Information Gap)를 생성합니다.
**기술 스택 가정:** React / Tailwind CSS 기반의 Single Page Application (SPA).

### 🖥️ A. 전체 플로우 다이어그램 (State Machine)

1.  **[Start] Hook Screen (Step 0):** 흥미 유발 제목 + 버튼 클릭 $\rightarrow$ Step 1
2.  **[Process] Data Collection Wizard (Steps 1-3):** 여러 페이지/섹션을 거치며 데이터 입력 및 진행 상황 표시.
    *   *핵심:* 모든 질문에 대한 즉각적인 피드백(예: "이 항목은 위험 신호가 있습니다.")을 주어 몰입도를 높입니다.
3.  **[Process] Loading & Scoring (Step 4):** 로딩 화면에서 '과학적 분석'의 느낌을 극대화합니다. (진짜 연산 시간이 필요함).
4.  **[End] Diagnosis Reveal Screen (Step 5):** 최종 리스크 지표(PSI)와 해석을 제공하며, 반드시 CTA를 노출합니다.

### ✨ B. 핵심 컴포넌트별 와이어프레임 구체화 (Desktop View 기준)

| 컴포넌트 | 구성 요소 | UX/UI 고려 사항 (Cody의 코멘트) |
| :--- | :--- | :--- |
| **헤더** | 로고, 제목 (e.g., 온현 웰에이징 리스크 스캐너), 진행률 바(Progress Bar). | 신뢰도를 최우선으로 합니다. 디자인은 학술적 권위가 느껴지도록 모던하고 미니멀해야 합니다. |
| **Step 1: 기초 정보** | 성별, 연령대 선택 (슬라이더/드롭다운), 만성질환 여부 (Yes/No). | PII를 가장 먼저 받고, 이후의 질문에 대한 근거가 됩니다. 필수 입력 필드는 명확히 표시해야 합니다. |
| **Step 2: 생활 습관 (HOMA-IR Focus)** | 체크리스트 형태의 질문 (예: 아침 식사 패턴, 수면 시간). 리커트 스케일(1~5점) 사용 권장. | *기술적 난이도:* 단순 질문으로 보이지만, 각 답변은 가중치 점수(Weight)를 가져야 합니다. '왜?'라는 의문을 던지게 만드세요. |
| **Step 3: 신체 지표 (골밀도/근력)** | 구체적인 측정 기준 기반 질문 (예: 계단 오르기 난이도, 아침 기상 시 근육통 정도). | 이 단계에서 '객관적 데이터'를 수집했다는 느낌을 주어 권위를 강화합니다. |
| **Step 5: 결과 리포트** | **[가장 중요]** 개인화 리스크 점수 (PSI), 위험도 레벨(Low/Moderate/High) 배지, 상세 해석 본문. | *MUST:* '현재는 간이 진단입니다. 정확한 전문 검진을 받아보세요.'라는 문구를 큼지막하게 넣어 CTA로 연결합니다. |
| **CTA 영역** | 버튼: "전문 상담 예약하기" (유료), 링크: "무료 리포트 다운로드" (2차 DB 수집). | 이 부분이 수익화의 핵심입니다. 가장 눈에 잘 띄게, 학술적 권위와 연계하여 배치해야 합니다. |

---

## ⚙️ [산출물 2] 데이터 수집 API 엔드포인트 초안 및 스키마 정의

**목표:** 프론트엔드의 모든 데이터를 백엔드가 안정적으로 받고 처리할 수 있는 계약(Contract)을 만듭니다.
**기술 가정:** RESTful API, JSON 기반 통신.

### 🔗 Endpoint Specification

| 구분 | 상세 내용 | 설명 |
| :--- | :--- | :--- |
| **API URL** | `/api/v1/diagnosis/submit` | 진단 데이터를 전송하는 메인 엔드포인트입니다. |
| **Method** | `POST` | 데이터 생성(Submission)을 의미합니다. |
| **요청 헤더 (Request Header)** | `Content-Type: application/json` | 통신 형식 정의. |

### 📝 Request Body Schema (Input Data Validation)

사용자로부터 받아야 할 최소한의 필수 필드와 그 타입입니다.

```json
{
    "user_info": {
        "age": "number",          // 사용자 나이 (필수)
        "gender": "string",       // 'male' or 'female' (필수)
        "has_chronic_disease": "boolean" // 만성 질환 유무 (True/False, 필수)
    },
    "lifestyle_metrics": {
        "sleep_quality_score": "number", // 수면 만족도 점수 (1-5점)
        "dietary_index_score": "number",   // 식단 지표 점수 (1-5점)
        "exercise_frequency": "integer"    // 주간 운동 빈도 (0~7일, 필수)
    },
    "risk_indicators": {
        "homa_ir_proxy_score": "number", // HOMA-IR 관련 체크리스트 종합 점수 (가중치 합산값)
        "bone_density_concern": "integer",  // 골밀도 우려 정도 (1~5점, 필수)
        "cognitive_decline_score": "integer" // 인지 기능 저하 위험도 (1~5점, 필수)
    },
    "source_tracking": {
        "referrer_url": "string",       // 유입 경로 추적 (필수: 리드 분석용)
        "campaign_id": "string"        // 마케팅 캠페인 ID (선택)
    }
}
```

### 📤 Response Body Schema (Output Data Structure)

백엔드가 계산을 완료한 후, 프론트엔드로 돌려줄 데이터입니다. 이 구조를 기반으로 UI가 렌더링됩니다.

```json
{
    "success": true,
    "diagnosis_result": {
        "user_id": "uuid-generated",
        "psi_score": "integer", // Personalized Risk Index Score (예: 78)
        "risk_level": "string",  // 'Moderate' 또는 'High', etc.
        "overall_diagnosis": "string", // 최종 요약 메시지 (e.g., "만성 염증과 골밀도 감소가 복합적으로 위험합니다.")
        "detailed_breakdown": [
            {"indicator": "HOMA-IR", "score": 4, "recommendation": "식습관 개선 및 인슐린 민감도 체크 필요."},
            {"indicator": "Bone Density", "score": 3, "recommendation": "단백질 섭취량과 비타민D 보충 고려."}
        ]
    },
    "next_actions": {
        "primary_cta": {
            "text": "전문 상담 예약하기",
            "url": "/booking/consultation",
            "priority": "paid_conversion"
        },
        "secondary_cta": {
            "text": "무료 리포트 다운로드 (PDF)",
            "url": "/download/report",
            "priority": "lead_magnet"
        }
    }
}
```

---

## 📜 [산출물 3] Mini-App 구현을 위한 최소 기술 스펙 문서 (Tech Spec)

**목표:** 이 기능을 실제로 개발할 때, 어떤 아키텍처와 로직이 필요한지 정의합니다.

### 1. 시스템 아키텍처 개요

*   **Front-end Layer:** React Hooks + Context API 사용 권장 (상태 관리 용이). 모든 컴포넌트는 Tailwind CSS로 스타일링되어야 합니다.
*   **Back-end Layer (API Gateway):** Python/FastAPI 또는 Node.js/Express를 사용하여 구현합니다. **가급적 Python을 추천합니다.** (과학 지표 처리 및 데이터 분석에 강점이 있습니다.)
*   **Data Storage:** PostgreSQL 사용 권장. `diagnosis_records` 테이블에 모든 제출 데이터를 저장해야 합니다.

### 2. 핵심 로직 스펙 (The 'Process' Layer)

이 부분이 가장 중요하며, 단순 가중치 합산 이상의 **비즈니스 로직**이 필요합니다.

1.  **데이터 전처리 및 정규화:**
    *   모든 입력 점수는 `0`부터 `5` 사이의 표준 스케일로 정규화되어야 합니다.
    *   PII(나이, 성별)에 따라 가중치가 달라지는 로직을 포함해야 합니다 (예: 60세 이상 남성은 골밀도 지표의 가중치 *1.2 적용).
2.  **PSI (Personalized Risk Index Score) 계산:**
    *   `PSI = SUM(Indicator_Score * Indicator_Weight) + Base_Factor(Age, Gender)` 형태로 복합적으로 산출되어야 합니다. 이 점수가 사용자에게 전달될 핵심 지표입니다.
3.  **위험도 판단 및 해석 로직 (The Magic):**
    *   `PSI > Threshold_High` $\rightarrow$ `risk_level: High`, 메시지: "즉시 전문 검진 필요."
    *   `Threshold_Moderate < PSI <= Threshold_High` $\rightarrow$ `risk_level: Moderate`, 메시지: "생활 습관 개선 및 3개월 내 재검진 권고."
4.  **CTA 유도 로직:**
    *   만약 계산된 `risk_level`이 **'High'**라면, Primary CTA는 무조건 '전문 상담 예약하기'로 고정되어야 합니다 (최대 매출 확보).

### 3. 예외 처리 및 검증 루프 (Error Handling)

*   **Validation Failure:** 필수 입력 필드 누락 시, API 레벨에서 `400 Bad Request`를 반환하고 어떤 필드가 문제인지 구체적으로 알려줘야 합니다.
*   **Rate Limiting:** API 호출 빈도를 제한하는 Rate Limiter가 반드시 필요합니다 (봇 방지 및 시스템 부하 분산).

---
### 📊 평가: 완료 — 와이어프레임, API 스키마, 기술 문서를 통해 MVP 개발에 필요한 모든 논리적/구조적 청사진이 완성됨.

📝 다음 단계: 백엔드(FastAPI)를 사용하여 `diagnosis_records` 테이블을 설계하고, **가장 핵심인 'PSI 점수 계산 및 위험도 판단 로직'의 Python 코어 모듈**을 작성하여 개발팀에게 전달해야 합니다.
