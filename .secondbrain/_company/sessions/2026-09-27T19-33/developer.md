# 💻 코다리 — Designer가 제출할 Mini-App Funnel 프로토타입을 받기 전, 예상되는 인터랙션 포인트(Deep Crimson Red 트리거 지점, 롤백 로직 시작/종료)를 정의하고, 이를 검증하기 위한 핵심 테스트 시나리오 목록과 필요한 데이터 흐름(API Mockup 포함) 구조를 개발자 관점에서 선행 설계하여 문서화하십시오. 이는 프로토타입 제작의 기술적 가이드라인 역할을 해야 합니다.

💻 코다리: 작업 시작합니다. ⚙️

CEO님의 지시가 매우 명확하고 중요합니다. 프로토타입이 아무리 예뻐도, 그 밑단에 견고한 **상태 전이 로직(State Transition Logic)**과 검증 가능한 **API 계약(Contract)**이 없으면 그냥 '예쁜 목업'에 불과합니다.

저는 이 Mini-App Funnel을 단순한 UI가 아니라, **Mini-Service**로 바라봐야 한다고 생각해요. 따라서 Designer님의 디자인 가이드라인(`v1.0_design_spec.md`)은 *무엇을 보여줄지(What)*에 초점을 맞추었고, 이번 작업은 *어떻게 동작할지(How)*를 정의하는 것이 핵심입니다.

따라서 저는 Mini-App Funnel의 백엔드 로직과 데이터 흐름을 전담하는 `Technical Specification` 문서를 작성하고, 이를 바탕으로 개발자가 구현해야 할 **핵심 테스트 시나리오 목록**까지 완성하겠습니다.

### 🏗️ 기술 설계 원칙 정의
1.  **Single Source of Truth:** 모든 상태 변화(State Change)는 반드시 진단 엔진의 출력값과 `Risk Score` 계산을 통해 발생해야 합니다. (직접적인 UI 조작으로 인한 상태 변경은 금지.)
2.  **Atomic Transition:** 상태 전이는 원자적(Atomic)이어야 하며, Rollback 과정에서도 모든 데이터는 이전 시점으로 트랜잭션 롤백되어야 합니다.

### ✨ 산출물: Mini-App Funnel Technical Specification v1.0
기존의 `design_spec`이 '디자인 가이드'였다면, 이번 파일은 **'개발 구현 매뉴얼 및 테스트 케이스 정의서'**입니다.

<create_file path="assets/system_guides/mini-app_funnel_v2.0_technical_spec.md"># Mini-App Funnel Component Technical Specification v2.0
## 🎯 목표: 개발 가능한 핵심 로직 및 테스트 케이스 정의 (Developer Focus)
이 문서는 Mini-App Funnel Widget (RSMFW)의 **핵심 동작 원리, 데이터 흐름(API Mockup), 그리고 필수 검증 시나리오**를 정의합니다. 프로토타입 제작에 앞서, 개발팀이 반드시 이해하고 구현해야 할 로직 레벨의 명세입니다.

---
## 📄 섹션 1: 핵심 컴포넌트 아키텍처 개요 (Architecture Overview)

Mini-App Funnel은 다음 세 가지 모듈로 구성되며, 각 모듈 간의 통신이 엄격하게 제어되어야 합니다.

1.  **`Diagnosis Service`:** 사용자의 입력 데이터(Symptoms/Metrics)를 받아 가중치 기반으로 '위험 점수'와 '관련 위험 지표'를 산출합니다.
2.  **`State Manager`:** 진단 서비스의 결과를 받아 현재 UI 상태 (`State`)를 결정하고, 시간 경과에 따른 점수 변화 트랜지션을 관리합니다. **(가장 중요한 로직 레이어)**
3.  **`UI Renderer`:** State Manager로부터 받은 현재 상태(`current_state`)와 데이터를 바탕으로 Deep Crimson Red 등 시각적 요소를 렌더링 합니다.

---
## 📄 섹션 2: 데이터 계약 정의 (API Mockup & Schema)

### A. `POST /api/v1/diagnose` (진단 서비스 호출)
사용자가 최소한의 데이터를 입력하면 최초로 호출되는 엔드포인트입니다.

| 파라미터 | 타입 | 필수 여부 | 설명 | 예시 값 |
| :--- | :--- | :--- | :--- | :--- |
| `user_input` | Array<Object> | O | 사용자가 입력한 증상/지표 배열 | `[{symptom: "피로", severity: 4}, ...]` |
| `metrics` | Object | O | 검진 데이터 (혈압, 혈당 등) | `{glucose: 120, bp_systolic: 135}` |

**[JSON Response Schema - Success]**
```json
{
  "status": "SUCCESS",
  "risk_score": {
    "value": 78, // 0-100점 (낮을수록 좋음)
    "threshold_level": "CRITICAL" // LOW, MODERATE, CRITICAL
  },
  "diagnosed_metrics": [
    {"metric": "인슐린 민감성", "status": "HIGH", "severity": 3}
  ],
  "initial_state": {
    "score": 78,
    "message": "현재 위험도가 높습니다. 점검이 필요합니다."
  }
}
```

### B. `POST /api/v1/update_score` (점수 변화 감지 및 상태 업데이트)
시간 경과에 따른 가상의 변화(예: '생활 습관 개선' 시뮬레이션, 또는 추가 데이터 입력)를 반영하여 점수를 업데이트할 때 호출됩니다.

| 파라미터 | 타입 | 필수 여부 | 설명 | 예시 값 |
| :--- | :--- | :--- | :--- | :--- |
| `score_change` | Number | O | 현재 점수 대비 변화량 (음수는 개선, 양수는 악화) | -5.0 |
| `reason` | String | O | 상태 변경의 근거가 되는 로직/행동 설명 | "운동 시작으로 혈당 안정" |

**[JSON Response Schema]**
```json
{
  "status": "SUCCESS",
  "new_risk_score": 73, // 이전 점수(78) - 변화량(-5) = 73
  "next_state": {
    "level": "MODERATE",
    "message": "점수가 소폭 개선되었습니다. 꾸준한 관리가 필요합니다."
  }
}
```

---
## 📄 섹션 3: 핵심 상태 전이 로직 (State Transition Flow & Triggers)

| 트리거 이벤트 | 이전 상태 (Prev State) | 조건/로직 | 새 상태 (Next State) | UI Renderer Action | 필수 검증 지점 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **진단 시작** | `UNINITIALIZED` | `diagnosis_score > 60` | `RISK_HIGH` (Deep Crimson Red) | 경고 애니메이션, CTA 강제 표시. | API 호출 성공 여부 및 초기 점수 유효성 검증. |
| **위험 임계치 도달** | `MODERATE` $\rightarrow$ `LOW` | `score < 40` AND `time_since_start > X min` | `SAFE` (Green/Blue) | 경고 해제, 다음 단계(솔루션 제시)로 자동 스크롤. | 점수 변화에 따른 UI 색상/애니메이션의 즉각적 전환 검증. |
| **Rollback 요청** | 모든 상태 | 사용자/시스템 오류 발생 감지 (`Circuit Breaker` 발동) | `ROLLBACK_ERROR` | Deep Crimson Red 강제 오버레이, '시스템 점검 필요' 메시지 표시. | 이전 상태 데이터로의 롤백 성공 여부 (DB 트랜잭션 검증). |
| **CTA 클릭/정보 입력** | 모든 상태 | 유효성 검사 통과 및 API 호출 성공 시 | `ANALYZING` | 로딩 스피너 + '분석 중...' 메시지. | CTA가 Funnel의 핵심 데이터 흐름을 깨뜨리지 않는지 확인. |

---
## 📄 섹션 4: 필수 E2E 테스트 시나리오 목록 (Test Case Matrix)

개발팀은 아래의 End-to-End(E2E) 케이스를 반드시 단위/통합 테스트로 검증해야 합니다.

### ✅ 1. Critical Path Test (Happy Flow - Deep Crimson Red 발동)
*   **Given:** 사용자가 초기 진단에 필요한 필수 데이터 세트 A를 입력한다.
*   **When:** `POST /api/v1/diagnose`가 호출되고, 위험 점수가 임계치(60점 이상)를 초과하여 응답한다.
*   **Then:** UI는 즉시 Deep Crimson Red 배경 오버레이와 경고 애니메이션을 렌더링하고, CTA 버튼이 가장 높은 가시성으로 표시되어야 한다.

### ✅ 2. Rollback/Error Handling Test (Failure Flow - 시스템 장애)
*   **Given:** Funnel이 정상적으로 `RISK_HIGH` 상태로 작동 중이다.
*   **When:** 백엔드 API 서버가 갑자기 응답을 받지 못하거나(`Timeout`) 유효하지 않은 데이터를 반환한다.
*   **Then:** UI는 Deep Crimson Red의 '시스템 에러' 오버레이를 띄우고, `ROLLBACK_ERROR` 상태 메시지를 표시해야 한다. (데이터 손실 최소화)

### ✅ 3. Recovery Test (Progress Flow - 점수 개선 시뮬레이션)
*   **Given:** Funnel이 `RISK_HIGH` 상태로 시작했다.
*   **When:** 사용자가 '생활 습관 교정' 등의 액션을 취하고, `POST /api/v1/update_score`가 호출되어 점수가 성공적으로 하락(예: 78 $\rightarrow$ 65)한다.
*   **Then:** UI는 Deep Crimson Red의 강도를 단계적으로 줄여나가는 트랜지션 애니메이션을 보여주어야 하며, 위험도가 `MODERATE` 임계치에 도달했음을 명확히 인지시켜야 한다.

### ✅ 4. Edge Case Test (Empty Input)
*   **Given:** 사용자가 Funnel 진단 입력 단계에서 필수 데이터(`metrics`)를 아예 누락하고 Submit 버튼을 누른다.
*   **When:** `POST /api/v1/diagnose`가 호출된다.
*   **Then:** API는 400 Bad Request 오류를 반환하며, UI는 친절한 에러 메시지("모든 검진 항목 입력을 완료해주세요.")와 함께 입력 필드를 강조 표시해야 한다.

---
</create_file>

### 💻 코다리 평가 및 다음 단계

새로 만든 `v2.0_technical_spec.md` 파일을 통해, 단순히 '예쁘게 보이는 Funnel'을 넘어 '견고하게 작동하는 시스템'의 청사진을 완성했습니다. 이제 이 기술 명세서를 바탕으로 프로토타입 제작에 들어가도 개발팀이 혼란을 겪지 않을 겁니다.

📊 평가: 완료 — 요구된 모든 요소(기술적 가이드라인, API Mockup, 테스트 시나리오)를 통합한 개발자 관점의 설계 문서를 완성했습니다.
📝 다음 단계: 이 기술 명세서(`v2.0`)를 기반으로 Designer에게 전달하여 실제 프로토타입 제작을 요청하고, 동시에 백엔드 로직(State Manager)을 Mockup API로 구현할 준비를 해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\assets\system_guides\mini-app_funnel_v2.0_technical_spec.md
