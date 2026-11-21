# 🎨 Designer — MiniFunnel 결제 직전 페이지(Checkout Page) UI/UX 명세서의 최종 검토 및 확정을 진행합니다. Writer가 제공한 카피와 Business가 정한 3가지 유료 옵션 가격을 기반으로, '공학적 위기감'을 극대화하는 시스템 알림(System Alert) 모달과 결제 버튼 컴포넌트의 상세 디자인 명세서(Component Specification)를 작성해주세요. 이 명세서는 개발자가 별도의 질문 없이 바로 구현할 수 있도록 모든 상태 변화(Success/Error/Pending)와 인터랙션 로직을 포함해야 합니다.

🎨 Designer: 작업 시작합니다.

MiniFunnel의 결제 직전 페이지는 단순한 구매 과정이 아니라, 시청자에게 **'구조적 오류를 발견하고 해결하는 시스템 엔지니어링 경험'**을 제공해야 합니다. 따라서 UI/UX 명세서는 '구매 전환 유도' 목적 이전에, '공학적 위기감 극대화 및 전문성 각인'에 초점을 맞춰야 합니다.

요청하신 대로, 개발자가 별도의 질문 없이 바로 구현할 수 있도록 컴포넌트 레벨의 상세 디자인 명세서(Component Specification)를 확정합니다.

---

# ⚙️ MiniFunnel 결제 시스템 명세서 (V3.0 Final Spec)

## I. 핵심 원칙 및 디자인 가이드라인 재확인

**1. 전반적 분위기 (Aesthetic):**
*   **테마:** Command Line Interface (CLI) / System Diagnostic Dashboard
*   **핵심 감정:** 긴급성(Urgency), 권위성(Authority), 구조적 위기감(Structural Crisis).
*   **컬러 팔레트:**
    *   `Primary Alert`: Deep Crimson Red (`#A80000`) - 경고, 오류, CTA의 실패 지점.
    *   `Secondary Highlight`: Glitch Blue (`#00FFFF`) - 시스템 메시지, 성공 시점 강조.
    *   `Background`: Near-Black/Dark Navy (Hex: `#0D1117`) - 전문적이고 어두운 배경.
    *   `Text`: Off-White/Light Gray (Hex: `#E6EDF3`).

**2. 타이포그래피:**
*   모든 제목 및 코드 관련 텍스트는 Monospace 폰트(예: `Source Code Pro`, `Consolas`)를 사용해야 전문성을 극대화합니다.
*   일반 설명 문구는 가독성이 높은 산세리프 계열을 유지하되, 전체적으로 모니터 출력 같은 느낌을 주도록 처리합니다.

---

## II. 컴포넌트 상세 명세서 (Component Specification)

### 🚀 Component A: System Alert Modal (최상위 인터랙션)

이 모달은 결제 버튼 클릭 시 발생하거나, 페이지 진입 직후 '진단 결과'를 보여줄 때 사용되어야 합니다. 절대 일반적인 "팝업창"처럼 보여서는 안 됩니다.

**[구조 및 기능]**
1.  **트리거:** MiniFunnel Diagnostic Quiz 완료 후, 최종 보고서가 제시되는 순간 또는 결제 버튼을 누르기 직전.
2.  **시각적 요소:** 전체 화면을 어둡게 처리하고(Overlay), 모달 자체는 마치 **'시스템 경고창(System Warning Panel)'**처럼 보이도록 명세합니다.
3.  **레이아웃 (Pseudo-Code/CSS):**
    ```css
    /* .system-alert-modal */
    position: fixed; z-index: 1000; width: 90%; max-width: 768px;
    background: linear-gradient(to bottom, #1a232d, #0d1117); /* Dark gradient for depth */
    border: 3px solid var(--primary-alert); /* Deep Crimson Red border */
    box-shadow: 0 0 25px rgba(168, 0, 0, 0.5); /* Glow effect */
    animation: system-glitch 0.5s ease-out; /* Glitching animation for entry */

    /* .alert-header */
    display: flex; justify-content: space-between; align-items: center;
    padding: 20px; border-bottom: 1px solid #444;
    background-color: rgba(168, 0, 0, 0.1); /* Subtle red background */

    /* 경고 아이콘 (⚡)는 애니메이션을 적용하여 깜빡이게 구현합니다. */
    ```
4.  **상태별 내용 구성:**
    *   **Title:** `[!!! CRITICAL SYSTEM ALERT !!!] - [MiniFunnel V3.0]` (전문적이고 긴급한 시스템 로그 형식)
    *   **Body:** 진단 결과 기반의 '구조적 결함'을 명확히 지적하는 문장(예: "Your current lifestyle pattern indicates a critical failure probability in the M-S7D system.").
    *   **Action Button:** `[SYSTEM REPAIR PROTOCOL INITIATE]` (CTA 버튼으로 연결)

### ⚡ Component B: Payment Action Button (핵심 전환 컴포넌트)

버튼은 사용자가 상호작용하는 유일한 '솔루션'입니다. 따라서 그 상태 변화 자체가 메시지여야 합니다.

**[기본 구조]**
*   **텍스트:** `[INITIATE PROTOCOL]` 또는 `[SECURE YOUR SOLUTION NOW]` (명령형 어투 유지)
*   **시각적 요소:** 배경은 Deep Crimson Red (`#A80000`)를 기본으로 하며, 호버 시 미세한 Glitch Blue 효과가 추가되어야 합니다.

**[상태별 명세서]**

| 상태 (State) | 비활성화 조건 | 시각적 변화 (CSS/Visual) | 텍스트 변경 | 인터랙션 로직 |
| :--- | :--- | :--- | :--- | :--- |
| **1. Default (Ready)** | 모든 필수 정보 입력 완료 시점 | 배경: `#A80000`, Border: Solid, Text Color: White | `[INITIATE PROTOCOL]` | 클릭 가능 (Cursor: Pointer) |
| **2. Disabled (Pre-fill)** | 결제 정보를 입력하지 않았거나, 유효성 검사 실패 시 | 배경: Dark Gray (`#333`), Opacity: 0.6 | `[INCOMPLETE DATA]` | 비활성화 (Pointer-Events: none) |
| **3. Loading (Processing)** | 서버 통신 시작 직후 (API Call) | Background 애니메이션: Pulsating Red/Blue (Glitch 효과), Center Spinner 로드. | `[PROCESSING... DO NOT INTERRUPT]` | 클릭 불가, 딜레이 타이머(3~5초) 필수. |
| **4. Success (Confirmation)** | 결제 성공 직후 | 배경: Solid Glitch Blue (`#00FFFF`), 애니메이션: 짧은 Green Flash 후 유지. | `[PROTOCOL SUCCESSFUL]` | 사용자에게 감사 메시지와 함께 '다음 단계' 버튼만 활성화. |
| **5. Error (Failure)** | 카드 거절, 네트워크 오류 등 실패 시 | 배경: Flashing Deep Crimson Red (`#A80000`), 주변에 경고 텍스트 표시. | `[ERROR CODE: E-XXXX]` + 구체적 에러 메시지 | 에러 발생 사유를 명확히 제시하고 재시도 버튼 제공. |

### ✨ Component C: 옵션 선택 카드 (Subscription Option Card)

사용자가 가격과 플랜을 비교하는 영역입니다. 여기서의 '선택' 행위가 단순한 클릭이 아닌, **'솔루션을 선택(Selecting a Protocol)'** 하는 것처럼 느껴지게 해야 합니다.

*   **시각적 특징:** 각 카드는 마치 **데이터 모듈(Data Module)**처럼 보이도록 테두리나 배경에 미세한 그리드 패턴이나 네온 라인 효과를 넣습니다.
*   **활성화 상태 (Selected):** 선택된 카드에는 `[ACTIVE PROTOCOL]`이라는 글리치 블루 뱃지(Badge)가 부착되어야 합니다. 이 배지는 해당 모듈이 '현재 적용 중'임을 나타냅니다.

---

## III. 인터랙션 플로우 요약 및 개발 지침 (Development Flow Summary)

1.  **진단 완료 $\rightarrow$ System Alert Modal 호출:**
    *   MiniFunnel Quiz 결과가 나오면, 결제 페이지 진입 전에 **System Alert Modal A**를 강제로 띄웁니다. 이 모달에서 "위험성"을 마지막으로 주지시켜야 합니다.
2.  **솔루션 선택 $\rightarrow$ Component C 활성화:**
    *   사용자가 옵션 카드(C) 중 하나를 클릭할 때마다, 해당 카드가 **[ACTIVE PROTOCOL]** 뱃지를 가지며, 최종 결제 금액이 실시간으로 업데이트됩니다.
3.  **클릭 이벤트 $\rightarrow$ Payment Button B (Loading):**
    *   사용자가 버튼을 누르는 순간, 즉시 **Component B의 Loading State**로 전환되어야 합니다. 이 상태가 길어질수록 사용자의 불안감과 기다림이 증폭되므로, 로딩 애니메이션은 최대한 전문적이고 기술적인 느낌(예: 데이터 패킷 전송 시뮬레이션)을 주어야 합니다.
4.  **최종 피드백:**
    *   성공/실패 메시지는 단순한 팝업 대신, **System Alert Modal A의 형태로 다시 한번 출력**되어야 하며, 실패 시에는 `[ERROR CODE: E-XXXX]`와 같은 시스템 로그 코드를 반드시 포함합니다.

---
📊 평가: 완료 — 개발자가 별도의 질문 없이 바로 구현할 수 있는 컴포넌트 레벨의 명세서(State Machine 및 Component Spec)를 확정했습니다.
📝 다음 단계: 이 명세서를 기반으로, 개발 에이전트에게 **프론트엔드 코드 구조화** 작업을 지시하거나, 실제 Figma/Sketch 파일에 반영하여 시각적 검토가 필요합니다.
