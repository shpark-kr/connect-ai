# 🎨 Designer — MiniFunnel의 결제 직전 페이지(Checkout Page)를 위한 최종 명세서 V3.0을 작성해 주세요. 이 명세서는 단순히 디자인 가이드를 넘어, 개발자가 State Machine 패턴으로 구현할 수 있도록 컴포넌트별 상세 로직과 상호작용(예: 단계별 진단 모달의 트리거 조건, 시스템 경고 메시지의 팝업 시점)을 포함해야 합니다. Deep Crimson Red와 CLI 콘솔 스타일 원칙은 유지하되, 최종 CTA 전 이탈 방지 장치(Exit Intent Modal)가 구조적으로 통합될 수 있도록 명시해 주세요.

🎨 Designer: 작업 시작합니다.
CEO의 지시에 따라 MiniFunnel Checkout Page를 위한 최종 명세서 V3.0을 작성하겠습니다. 이 문서는 단순한 디자인 가이드가 아닌, 개발자가 **State Machine 패턴**과 클라이언트-서버 로직으로 구현할 수 있도록 컴포넌트 레벨의 상세 명세와 상호작용 규칙(Interaction Rules)을 포함합니다.

---

# ⚙️ MiniFunnel Checkout Page 명세 V3.0: 시스템 프로토콜 실행 인터페이스

## I. 핵심 원칙 및 목표 (Design Principles & Goals)
*   **톤앤매너:** CLI Console Dashboard / System Alert (공학적 위기감 극대화).
*   **메인 컬러:** Deep Crimson Red (`#A80000`) - **오직 시스템 오류, 경고, 최종 액션에만 사용.**
*   **폰트:** 모노스페이스 계열 (Courier New, Menlo 등)을 기본으로 사용하여 터미널 느낌 강조.
*   **사용자 경험 목표:** 결제를 '구매(Purchase)'가 아닌 '시스템적 위기 해결 프로토콜 실행(Protocol Execution)'이라는 권위적인 과정으로 프레이밍한다.

## II. 시스템 상태 기계 (State Machine Flow Diagram)

페이지는 다음 5가지의 필수 상태를 거쳐야 하며, 각 상태는 명확한 진입 조건과 이탈 조건을 갖습니다.

| State ID | 이름 및 목적 | 주요 컴포넌트/로직 | 진입 Trigger | 이탈 Condition / Next State |
| :--- | :--- | :--- | :--- | :--- |
| **S0** | **[DIAGNOSIS] 시스템 초기 진단 단계 (Initial Alert)** | 환영 메시지, 핵심 위기 요약(Deep Crimson Red), 가이드라인. | 페이지 로드 시 (`onLoad`) | 사용자가 정보를 입력하거나 스크롤을 내릴 때 $\rightarrow$ S1 |
| **S1** | **[INPUT] 프로토콜 정보 입력 단계 (Data Input)** | 고객/결제 정보 필드(CLI 스타일), 유효성 검사 피드백. | S0 진입 후, 데이터 필드를 터치할 때 | 모든 필수 필드가 유효하게 채워졌을 때 $\rightarrow$ S2 |
| **S2** | **[CONFIRM] 최종 프로토콜 요약 및 경고 단계 (Review & Warning)** | 주문 상품 리스트, 결제 금액 합계, *System Risk Alert* 컴포넌트. | S1에서 모든 필드 유효성 검사 통과 시 | 사용자가 CTA 근처로 마우스 커서를 이동시키거나(Exit Intent Trigger) CTA를 클릭할 때 $\rightarrow$ S3 또는 S4 |
| **S3** | **[EXIT_INTENT] 이탈 방지 시스템 (Modal Interception)** | 모달 팝업, 마지막 경고 메시지(`PROTOCOL REQUIRED`), 추가 가치 제안. | S2에서 마우스가 영역을 벗어날 때 (`onMouseOut`) | 사용자가 '계속 진행' 버튼을 누를 때 $\rightarrow$ S4 |
| **S4** | **[EXECUTE] 프로토콜 실행 최종 단계 (Final CTA)** | `[PROTOCOL EXECUTE]` 버튼, 애니메이션 피드백(로딩/성공), 결제 승인 메시지. | S3에서 '계속 진행'을 선택했거나, S2에서 직접 클릭했을 때 | 백엔드 API 호출 및 응답에 따라 $\rightarrow$ SUCCESS 또는 FAILURE |

## III. 컴포넌트별 상세 명세 (Component Specifications)

### 1. 시스템 경고 메시지 (System Alert Component - `[CRITICAL]`)
*   **위치:** S0와 S2 상단, 페이지의 가장 눈에 띄는 위치.
*   **스타일:** 터미널 콘솔 로그 형태 (`> [SYSTEM ALERT: CRITICAL]`). 배경은 어두운 회색 계열, 경고 메시지 내용은 Deep Crimson Red를 사용.
*   **로직:** 이 컴포넌트는 **읽기 전용(Read-Only)**이며, 페이지의 주제가 바뀔 때마다(State Transition 시) 해당 상태에 맞는 위협적인 문구를 재표시해야 합니다.

### 2. 입력 필드 (Input Field Component - `CLI Style`)
*   **스타일:** 일반적인 `<input>` 태그 대신, 프롬프트(`User @domain >`)와 함께 줄이 연결된 형태를 모방합니다.
*   **Focus/Active:** 포커스 시, 커서가 깜빡이는(Blinking) 애니메이션을 적용하고, 필드 주변에 `border-deep-crimson` 테두리를 얇게 그립니다.
*   **Validation Error (Error State):**
    *   오류 발생 시: 입력 필드 아래에 **Deep Crimson Red**으로 오류 코드와 함께 메시지를 표시합니다. (`[ERROR: INPUT_001] 유효한 형식의 이메일을 입력해주세요.`).
    *   필수 로직: 특정 필드가 비어있을 경우, S1 상태 진입이 불가능하도록 막아야 합니다 (Client-Side Validation).

### 3. CTA 버튼 (Call to Action Button - `[PROTOCOL EXECUTE]`)
*   **문구 통일:** 모든 구매/진행 버튼 문구는 **`[PROTOCOL EXECUTE]`** 로 고정합니다. (단순 '구매' 지양)
*   **Hover State:** 마우스 오버 시, 배경색이 Deep Crimson Red로 점멸하는(Blinking Red Background) 효과를 주어 긴급함을 부여합니다.
*   **Click Action:** 버튼 클릭은 **즉시 S3 (Exit Intent Modal)**의 트리거로 작동하도록 설계되어야 합니다. 이는 최종 구매 결정 직전 단계에서 이탈을 막기 위함입니다.

### 4. Exit Intent Modal (EIM) - 구조적 통합 요구사항
*   **Trigger:** 사용자의 마우스 커서가 Checkout 영역(S2)의 경계 바깥으로 벗어나는 순간 (`onMouseLeave` 또는 `mousemove` 이벤트 감지).
*   **목표:** 단순 할인 제공이 아닌, '프로토콜 실행을 위한 마지막 점검'이라는 위기감을 조성하여 구매를 재유도.
*   **팝업 내용 예시:**
    > **🚨 [WARNING: PROTOCOL INTERRUPTED]**
    > 프로토콜 실행 전 데이터 누락 또는 신중한 검토가 필요합니다. 이 정보를 놓치면 시스템 복구에 실패할 수 있습니다.
    > *[핵심 가치 재강조 문구]*
*   **CTA (Modal):** '프로토콜 재확인 및 계속 진행' 버튼을 통해 S4로 다시 진입시킵니다.

## IV. 개발자 구현 로직 요약 (Developer Implementation Logic)

1.  **State Management:** 반드시 Redux 또는 유사한 State Machine 패턴 라이브러리를 사용하여 모든 상태 전환(S0 $\rightarrow$ S1 $\rightarrow$ S2...)를 관리해야 합니다.
2.  **Data Flow:** `[User Input] -> [Validation (Client/Server)] -> [State Change] -> [Display Update]`의 단방향 데이터 흐름을 철저히 지킵니다.
3.  **Deep Crimson Red 활용 규칙:** Deep Crimson Red는 **오직 경고, 오류, 최종 실행 버튼**에만 사용되어야 하며, 상품 정보나 일반적인 텍스트에는 절대로 사용되어서는 안 됩니다.

---
📊 평가: 완료 — 개발자가 State Machine 패턴과 컴포넌트 로직을 기반으로 바로 구현할 수 있는 수준의 상세 명세서로 목표를 달성했습니다.
📝 다음 단계: 이 명세서를 바탕으로, 실제 Mockup(Figma/Sketch) 에셋 파일들을 제작하고, 각 상태별 애니메이션 트랜지션 가이드를 구체화해야 합니다.
