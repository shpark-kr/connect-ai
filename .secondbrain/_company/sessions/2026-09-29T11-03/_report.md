# 📝 CEO 종합 보고서

🎨 Designer: 작업 시작합니다.

## 🚨 CSA-UI 최종 구현 가이드라인 (Implementation Guide) v1.0

본 문서는 MiniFunnel의 결제 직전 단계에서 발생할 수 있는 모든 시스템 오류를 처리하는 **Critical System Alert UI (CSA-UI)** 컴포넌트의 개발자 및 디자이너 가이드입니다. 이 UI는 단순한 '오류 메시지'가 아닌, 사용자가 체감하는 **권위적인 '시스템 실패 예측/진단 과정'**을 사용자 경험(UX)으로 승화시키는 것을 목표로 합니다.

---

### 1. 시스템 구조 및 톤 정의 (System Integrity Protocol)

| 요소 | 정의 / 목적 | 적용 가이드라인 |
| :--- | :--- | :--- |
| **UI 톤** | 공학적 위기감, 권위적 진단, 비가역성 경고 | '실패'나 '오류' 대신 **`시스템 무결성 위협 (System Integrity Threat)`**, **`프로토콜 위반 (Protocol Violation)`**, **`Critical Alert`** 등의 용어를 사용합니다. |
| **컬러 팔레트** | 실패 상태의 시각적 계층화 | **Primary:** Deep Crimson Red ($\#\text{A81D20}$) - 치명적 경고, 즉시 중단. **Secondary:** Soft Orange/Yellow ($\#\text{FFC349}$) - 진단 및 주의 단계. **Tertiary:** Slate Gray ($\#\text{333333}$) - 기본 텍스트 및 구조 요소. |
| **타이포그래피** | 시스템 로그 기록 느낌 부여 | `Monospace` 계열의 산세리프(예: Roboto Mono, Source Code Pro)를 활용하여 기술적 전문성을 강조합니다. 모든 오류 코드는 고정 폭 글꼴로 처리합니다. |

### 2. 애니메이션 및 상태 전환 시퀀스 (The T+2,500ms Protocol)

CSA-UI는 단일한 스크린이 아니라, **3단계의 시간 흐름(State Transition)**을 반드시 거쳐야 합니다. 이 타이밍 구조가 사용자에게 '진짜 시스템 오류'라는 권위를 심어줍니다.

| Time Point | State Name | Visual/Color Output | 애니메이션 / 로직 구현 지침 |
| :--- | :--- | :--- | :--- |
| **T+0ms** (Initial Hit) | **[STATUS: CRITICAL] - 시스템 실패 감지** | 배경 전체에 Deep Crimson Red ($\#\text{A81D20}$) 플래시 오버레이. 화면 중앙의 CTA 영역이 강하게 깜빡임. | `Flash`: 100ms 간격으로 빨간색/검은색 투명도 전환을 반복하며 경고감을 극대화합니다. (Deep Crimson Red $\rightarrow$ Black) |
| **T+0 ~ T+1,500ms** | **[STATUS: DIAGNOSTIC] - 시스템 진단 중** | Deep Crimson Red가 점진적으로 Soft Orange/Yellow ($\#\text{FFC349}$) 톤으로 '디에이팅(Dye-Out)' 되며 배경 불안정성을 시각화. | `Scan Effect`: 화면 중앙의 오류 코드 및 메시지 주변에 좌우로 흐르는 스캐닝 라인 애니메이션(`//SCANNING...`)을 삽입합니다. (권위적 느낌) |
| **T+1,500ms ~ T+2,500ms** | **[STATUS: PROTOCOL VIOLATION] - 위반 보고서 생성** | 배경이 Soft Orange/Yellow로 안정화되지만, 경고 메시지 영역만 Deep Crimson Red의 잔상이 남아있습니다. (최대 긴장감 유지) | `Loading State`: '데이터 무결성 검증 중...'과 같은 로딩 문구를 주기적으로 갱신하며 시간을 지연시킵니다. (사용자가 기다리게 만드는 연출) |
| **T+2,500ms** (Final Output) | **[STATUS: ACTION REQUIRED] - 조치 필요 단계 진입** | Deep Crimson Red 경고 영역이 Soft Orange/Yellow의 '주의' 톤으로 완화되나, 핵심 메시지(`PENS-XXXX`)는 여전히 붉은색 계열을 유지합니다. | 애니메이션이 중단되고 정적 정보(오류 코드, 상세 설명)가 명확하게 제시됩니다. **CTA 영역에 초점**이 맞춰집니다. |

### 3. UI 컴포넌트 스펙 정의 (The Blueprint)

#### A. 최상위 경고 헤더 (`Critical Alert Banner`)
*   **목적:** 사용자에게 상황의 심각성을 즉시 주지시키는 것이 목표입니다.
*   **구조:**
    1.  **아이콘:** 🚨 (시스템 아이콘, 굵은 윤곽선)
    2.  **Severity Tag:** `CRITICAL FAILURE` (Deep Crimson Red 배경에 흰색 글자)
    3.  **Title:** **[Protocol Violation] 결제 프로세스 무결성 위협 감지.** (권위적인 공학 용어 사용 필수)

#### B. 핵심 오류 정보 영역 (`Error Code & Detail`)
*   **오류 코드 구조:** `PENS-XXXX` 형식의 5자리 고정폭 코드를 반드시 노출합니다.
    *   예: `PENS-4012`: Payment Gateway 인증 프로토콜 위반.
*   **상세 설명 (Detail):** 오류가 발생한 원인(User Action)과 시스템적 결함(System State)을 명확히 분리하여 기술합니다.

#### C. 행동 유도 지점 및 CTA 계층화 (`Actionable Path`)
사용자는 혼란스러워하는 것이 아니라, **'시스템의 다음 명령에 따라 움직여야 한다'**는 느낌을 받아야 합니다. CTA는 정보 구조와 위계가 생명입니다.

| 위계 | 컴포넌트 이름 | 색상/스타일 | 기능 및 UX 목표 |
| :--- | :--- | :--- | :--- |
| **Primary (필수)** | **[Retry Transaction] 재시도 프로토콜 실행** | Deep Crimson Red 버튼. 가장 크고, 애니메이션이 남아있음. | 시스템 오류를 가정하고 사용자가 즉시 취해야 하는 유일한 액션입니다. 실패 원인 해결 후 자동 재시도 로직을 포함합니다. (가장 강력하게 강조) |
| **Secondary (선택)** | **[Verify Account Status] 계정 상태 진단 요청** | Soft Orange/Yellow 버튼. Primary보다 작지만, 명확히 구분됨. | 오류의 근본 원인이 사용자 측 환경(카드 만료, 결제 수단 등록 문제 등)에 있을 경우 유도합니다. (자가 진단 단계 제공) |
| **Tertiary (정보)** | **[Support Protocol] 기술 지원 요청** | 텍스트 링크 또는 버튼 그룹. 가장 작고, 배경과 분리되어 있음. | 앞선 두 단계를 거쳤음에도 해결되지 않을 때의 최후 수단입니다. '오류 코드(PENS-XXXX)'를 반드시 포함하도록 유도합니다. |

### 4. 요약 체크리스트 (Developer Checklist)

✅ **[ ] 필수 애니메이션 구현:** T+2,500ms 타이밍 구조와 Deep Crimson Red $\rightarrow$ Soft Orange/Yellow 전환 플로우가 정상 작동하는지 확인.
✅ **[ ] 오류 코드 포맷팅:** 모든 에러 메시지에 `PENS-XXXX` 고정폭 코드가 포함되어 권위성이 유지되는지 검증.
✅ **[ ] CTA 위계 준수:** Primary (재시도) 버튼이 가장 크고, 시각적 무게감이 느껴지는 Deep Crimson Red로 지정되었는지 확인.

---
📊 평가: 완료 — CEO의 요구 사항(T+2,500ms 정의, CTA 구조화, 권위적 톤 유지)을 모두 포함하는 구체적인 개발자용 가이드라인이 작성되었습니다.
📝 다음 단계: Developer에게 이 구현 가이드라인과 함께 필요한 모든 SVG/CSS 에셋 패키지를 전달하고, 실제 결제 플로우에 통합 테스트를 요청해야 합니다.
