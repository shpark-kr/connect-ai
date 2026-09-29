# 💻 코다리 — Designer가 확정한 MiniFunnel의 최종 UI/UX 스펙(특히 애니메이션 및 Deep Crimson Red 경고 로직)을 기반으로, 실제 구현에 필요한 기술 아키텍처(컴포넌트 분리, 상태 변화 관리 등)를 설계하세요. 모바일 트래픽 부하 상황에서도 오류 메시지가 완벽하게 작동하는 E2E QA 테스트 시나리오와 코딩 가이드라인을 포함하여 보고서를 작성해주세요.

💻 코다리: 작업 시작합니다.

MiniFunnel 결제 퍼널의 기술 아키텍처 설계는 정말 중요한 단계입니다. ⚙️ UI/UX가 아무리 완벽해도, 그 뒤에 흐르는 상태 관리와 에러 처리가 허술하면 모바일 트래픽 부하 상황에서 쉽게 깨집니다. 특히 '시스템 오류'라는 공학적 위기감을 조성하려면, 단순히 화면을 바꾸는 게 아니라 *프로세스 자체가 실패하는 듯한* 느낌을 줘야 합니다.

Designer가 확정한 V4.0 스펙(`Deep Crimson Red`, `Shake Effect`)을 기반으로, 저는 이 퍼널이 **견고하고(Resilient)**, **확장 가능하며(Scalable)**, **테스트 가능한(Testable)** 아키텍처를 갖도록 설계하겠습니다.

아래에 기술 아키텍처 블루프린트와 E2E QA 테스트 시나리오를 보고합니다.

---

## 🏗️ MiniFunnel Payment Flow: Technical Architecture Blueprint (v1.0)

이 퍼널은 React/Next.js 기반의 TypeScript 환경을 가정하고 설계합니다. 핵심 원칙은 **State-Driven Development**와 **Component Isolation**입니다.

### 1. 컴포넌트 분리 전략 (Component Isolation)
전체 결제 흐름을 단일 거대한 컴포넌트로 만들지 않고, 각 단계별로 역할을 명확히 분리하여 유지보수성을 극대화합니다.

| 컴포넌트명 | 역할 (Responsibility) | 기술 요구사항 | 재사용성 |
| :--- | :--- | :--- | :--- |
| **`PaymentButtonContainer`** | 결제 버튼의 상태(State)를 관리하고, 클릭 이벤트 발생 시 전체 퍼널 로직을 시작하는 최상위 제어기. | `useState`, `useCallback` (React Hooks), State Machine 연동. | 높음 (다른 Funnel에서도 재사용 가능). |
| **`SystemAlertOverlay`** | Deep Crimson Red 기반의 오버레이 컴포넌트. 배경 흔들림(Jitter Effect) 및 애니메이션 로직을 전담. | CSS Animation (`keyframes`), Tailwind/Styled-Components를 이용한 스타일링, Z-index 제어. | 매우 높음 (다른 '오류 상태' UI에 활용). |
| **`LoadingSpinnerComponent`** | API 호출 중 발생하는 일반적인 로딩 스피너 및 텍스트 표시. | 순수 함수(Pure Component)로 구현하여 테스트 용이성 확보. | 높음. |
| **`MiniFunnelForm`** | 실제 유저 정보 입력 및 결제 수단 선택 UI. (데이터 바인딩 담당). | TypeScript Type Safety 필수, Formik/React Hook Form 같은 폼 라이브러리 사용 권장. | 보통. |

### 2. 상태 관리 설계 (State Machine)
가장 중요한 것은 **전환(Transition)** 로직입니다. 단순한 `isLoading: boolean`으로는 부족하며, 명시적인 State를 정의해야 합니다.

**A. 핵심 상태 정의:**

```typescript
type PaymentState = 'IDLE' | 'LOADING_NORMAL' | 'PROCESSING_ERROR' | 'SUCCESS' | 'FAILURE';
```

**B. 흐름도 (Flowchart & Guarding):**

1.  **`[Initial] IDLE`**: 사용자가 버튼 클릭 전 상태. (`PaymentButtonContainer`가 초기화)
2.  **$\rightarrow$ `LOADING_NORMAL`**: 사용자가 버튼 클릭 시, API 호출 시작. 로딩 스피너 표시 (애니메이션: 푸른색/녹색 계열). *이 단계는 일반적인 성공 경로처럼 보이게 하는 것이 목표.*
3.  **(API Latency 발생)** $\rightarrow$ **Guard Check:** 백엔드로부터 유효성 검증 실패 응답(4xx) 또는 타임아웃(504)이 감지될 경우, 상태가 `PROCESSING_ERROR`로 강제 전환된다. (핵심!)
4.  **$\rightarrow$ `PROCESSING_ERROR`**: **Critical Moment.** `SystemAlertOverlay`가 활성화되며 Deep Crimson Red 필터와 Shake Effect를 적용한다. 이 컴포넌트 내부에서 "시스템 자원 고갈 경고" 텍스트 및 타이머 로직이 실행된다.
5.  **$\rightarrow$ `SUCCESS`/`FAILURE`**: 에러 메시지 처리 후, 최종 성공/실패 페이지로 리다이렉션 또는 상태 업데이트.

### 3. 모바일 트래픽 부하 대응 설계 (Resilience Focus)
모바일 환경에서의 불안정성을 해결하기 위해 다음 두 가지 로직을 강제합니다.

1.  **Client-Side Retry Logic:** `LOADING_NORMAL` 상태에서 네트워크 오류(Connection Lost)가 감지되면, 즉시 에러를 띄우기보다 **3회까지 지연 재시도(Exponential Backoff)**하는 로직을 먼저 시도해야 합니다.
2.  **Optimistic UI Update + Fallback:** 결제 버튼 클릭과 동시에 임시로 성공 상태 UI(예: "잠시만 기다려 주세요...")를 보여주되, 백엔드 응답이 1초 이상 지연되거나 에러가 발생하면 즉시 `SystemAlertOverlay`를 통해 **'시스템 오류'** 경고로 강제 전환되어야 합니다.

---

## 🧪 E2E QA 테스트 시나리오 및 코딩 가이드라인

아키텍처의 견고함을 검증하기 위해 다음 세 가지 핵심 실패 경로에 대한 E2E(End-to-End) 테스트를 설계합니다. (Jest/Enzyme 또는 Cypress 사용 권장)

### 1. Critical Failure Path Test: Processing Error
*   **목표:** 네트워크 지연 및 서버 측 오류가 발생했을 때, Deep Crimson Red 경고가 정확한 타이밍에 노출되는지 검증한다.
*   **테스트 시나리오:**
    1.  사용자가 결제 버튼 클릭 (`Action`).
    2.  `PaymentButtonContainer`의 내부 상태를 모킹(Mocking)하여, API 호출이 3초 이상 지연되도록 설정하고(`Network Latency Mock`), 응답은 `HTTP 503 Service Unavailable`로 강제한다.
    3.  **검증:** 화면에 Deep Crimson Red 오버레이가 나타나고, 'Critical System Alert' 문구가 표시되며, 페이지 전체가 Shake Effect를 일으키는지 확인한다. (UI Assertion)

### 2. Resilience Test: Low Bandwidth Simulation
*   **목표:** 모바일 환경에서 간헐적으로 발생하는 연결 끊김(Drop Packet) 상황을 시뮬레이션하고 앱이 크래시되지 않는지 검증한다.
*   **테스트 시나리오:**
    1.  사용자가 결제 버튼 클릭 (`Action`).
    2.  Mocking 레이어를 사용하여, API 호출 중간에 `Network Error (Connection Reset)`를 3회 발생시킨다.
    3.  **검증:** 시스템이 즉시 에러로 빠지는 대신, 재시도 카운터를 표시하며 지정된 쿨다운 시간(예: 2초) 동안 대기하는지 확인한다.

### 3. Edge Case Test: Input Validation Bypass
*   **목표:** 클라이언트 측 유효성 검증을 우회하려는 시도를 막고, 서버 응답에 따라 적절한 에러 메시지를 보여주는지 테스트한다.
*   **테스트 시나리오:**
    1.  사용자가 필드를 비워두거나 잘못된 포맷으로 입력하고 결제 버튼 클릭 (`Action`).
    2.  백엔드 모킹을 통해 `HTTP 400 Bad Request`와 함께 "이메일 형식이 유효하지 않습니다"라는 구체적인 에러 메시지를 반환하도록 설정한다.
    3.  **검증:** Deep Crimson Red 경고가 아닌, *특정 필드를 강조하는* 일반적인 Validation Error UI가 표시되며, 사용자에게 해당 필드만 수정할 기회를 제공하는지 확인한다.

---

📊 평가: 완료 — 요청된 모든 기술 아키텍처 요소(컴포넌트 분리, 상태 관리, E2E QA 시나리오)를 구조화하여 제시했습니다.
📝 다음 단계: 프론트엔드 코드 구현을 시작하고, 특히 `SystemAlertOverlay` 컴포넌트에 Deep Crimson Red 색상 및 Shake/Jitter Effect CSS 애니메이션을 실제로 적용해야 합니다.
