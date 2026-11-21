# 🎨 Designer — Developer에게 전달할 최종 '애니메이션 명세서' 초안을 작성해주세요. 이 명세서에는 (1) Defect ID 진단 과정에서 발생하는 모든 시각적 변화(Transition), (2) 글리치 효과의 타이밍과 변주, 그리고 (3) 시스템 경고 메시지 오버레이가 화면에 나타날 때의 정확한 애니메이션 로직(CSS/JS 레벨)을 상세히 포함해야 합니다. 이는 코딩 작업의 기준점이 됩니다.

🎨 Designer: 작업 시작합니다. CEO의 지시에 따라 개발자가 즉시 코딩에 사용할 수 있도록 '애니메이션 명세서(Animation Specification)'를 작성하겠습니다. 이 문서는 단순한 디자인 가이드가 아닌, **로직과 타이밍을 포함하는 기술 사양서**여야 합니다.

이 명세서는 현재 작업 중인 MiniFunnel 구조의 핵심적인 사용자 경험(UX) 요소들—위기감 조성 및 정보 전달—에 대한 애니메이션 로직을 정의합니다. 파일명은 개발자들이 가장 쉽게 접근할 수 있도록 `mini_funnel_design_specs/` 폴더 내부에 생성하겠습니다.

<create_file path="c:\Data\Project\connect-ai\mini_funnel_design_specs\Animation_Specification_v1.0.md"># ⚙️ MiniFunnel 인터랙션 애니메이션 명세서 (v1.0)
## 📄 개요 및 목표
이 명세서는 '온현'의 콘텐츠 흐름 중, 사용자가 일반 정보 탐색 단계에서 **공학적 위기감(Engineered Urgency)**을 느끼고 최종적으로 MiniFunnel 진단 페이지로 전환되는 과정에 필요한 모든 애니메이션 로직을 정의합니다.

**핵심 원칙:**
1.  **깊이감과 전문성:** 단순한 페이드 인/아웃을 지양하고, 터미널 시스템이나 데이터 스트림 같은 '기계적' 움직임을 사용한다.
2.  **위험 경고의 시각화:** Deep Crimson Red (#B30000)와 Glitch 효과를 통해 시스템 오류가 발생했다는 강력한 인상을 준다.
3.  **로직 기반 동작:** 모든 애니메이션은 CSS Transitions 및 JavaScript Timing API에 의해 제어되어야 한다.

---

## 🔴 1. Defect ID 진단 과정의 시각적 변화 (Diagnosis Transition)

사용자가 일반적인 문제 인식(Pain Point) $\rightarrow$ 시스템 데이터 로딩 $\rightarrow$ 특정 결함 식별 과정을 거칠 때 적용되는 로직입니다.

### A. 단계: Pain Point 입력 및 로드 시작
*   **시작:** 초기 배경은 어두운 다크 네이비 계열 (`#0A192F`).
*   **애니메이션 (JS):** 사용자의 입력 필드가 활성화되면, 주변의 가상 데이터 스트림(점선/미세한 텍스트)이 좌우에서 흐르듯 나타난다.
    *   `animation: stream-flow 8s linear infinite;`
*   **사운드 (UX):** 미세한 기계음 또는 데이터 패킷 전송음을 배경에 깔아준다.

### B. 단계: Defect ID 식별 및 강조 (The Reveal)
*   **트리거:** 백엔드에서 유효한 Defect ID (`E-C403` 등)가 로딩되거나 확정되는 순간.
*   **애니메이션 (CSS/JS):**
    1.  **글리치 효과 적용:** 배경 전체에 0.2초간의 짧고 강력한 Glitch Flash를 적용한다. (`filter: hue-rotate(360deg) saturate(200%) brightness(150%);`)
    2.  **코드 노출 (Typewriter Effect):** Defect ID가 중앙의 전용 코드 블록 컴포넌트에 타이핑되는 효과로 나타난다.
        *   `@keyframes typewrite { 0% { width: 0; } 100% { width: 100%; } }`
        *   CSS `width` 속성을 JS의 `setTimeout`으로 점진적으로 증가시킨다.
    3.  **색상 강조:** 코드가 완성되는 순간, 해당 ID는 Deep Crimson Red (`#B30000`)로 하이라이트되며, 주변에 미세한 펄스(Pulse) 애니메이션을 준다.

---

## 🔥 2. 글리치 효과 (Glitch Effect) 상세 명세

글리치 효과는 '시스템 오류'를 시각적으로 표현하는 가장 중요한 요소입니다. 강도와 타이밍에 따라 변주가 필요합니다.

### A. 기본 Glitch 컴포넌트 (Background Flicker)
*   **목적:** 미묘하게 시스템이 불안정하다는 느낌 부여.
*   **구현 방식:** CSS `filter` 속성 기반의 랜덤 트랜스폼 및 색상 변경을 사용한다.
*   **로직:** 2~3초 주기로, 무작위 선택된 작은 영역(예: 화면의 상단 10%)에 대해 다음 변환이 짧게 적용된다 (Duration: 50ms).

```css
/* CSS Pseudo-code for subtle glitch */
.glitch-background {
  animation: flicker 3s linear infinite;
}
@keyframes flicker {
  0%, 100% { transform: translate(0, 0); opacity: 1; }
  25% { transform: translate(-1px, -2px); opacity: 0.98; }
  75% { transform: translate(2px, 1px); opacity: 0.99; }
}
```

### B. 임계점 Glitch (Critical Failure)
*   **트리거:** MiniFunnel의 최종 CTA 버튼 클릭 직전 또는 경고 메시지 오버레이가 활성화될 때.
*   **강도:** 최상. 화면 전체에 걸쳐 0.3초 동안 빠르게 깜빡이는(Blinking) 효과를 적용한다.
*   **기술:** `box-shadow`와 `filter: contrast()` 속성을 조합하여 색수차(Chromatic Aberration)가 발생한 듯한 오버레이를 구현해야 한다.

---

## 🚨 3. 시스템 경고 메시지 오버레이 (System Alert Overlay) 로직

이 컴포넌트는 콘텐츠의 클라이맥스이자, 사용자가 '문제를 인식'하는 순간에 가장 큰 임팩트를 주어야 합니다.

### A. 활성화 조건 및 트랜지션
*   **트리거:** 콘텐츠 스크립트 상에서 Defect ID와 관련된 위험성이 최고조에 달했을 때 (예: 3분 지점).
*   **애니메이션 로직 (CSS/JS):**
    1.  **Stage 1 (Initiation - 0s):** 화면 전체가 Deep Crimson Red의 반투명 오버레이로 빠르게 어두워진다 (`opacity` from 0 to 0.8 in 150ms).
    2.  **Stage 2 (Alert Display - 0.15s):** 중앙에 `[SYSTEM ALERT: CRITICAL FAILURE]` 메시지가 강렬한 애니메이션과 함께 나타난다.
        *   *메시지:* 크기(Scale)를 0.8에서 1.0으로 급격히 키우면서(`transform: scale()`) 진입하는 느낌을 준다.
    3.  **Stage 3 (Details - 지속):** 경고 메시지 아래에 '진단이 필요합니다'와 같은 서브 카피가 타이핑 효과로 나타나며, 남은 시간(Time Remaining) 카운트다운 컴포넌트가 시작된다.

### B. 필수 애니메이션 로직 요약
| 요소 | Trigger (발동 조건) | Animation Type | Timing/Duration | Key CSS/JS Action |
| :--- | :--- | :--- | :--- | :--- |
| **전체 배경** | 경고 발생 시점 | Fade-to-Red Overlay | 150ms | `background-color` (transparency increase) |
| **메인 메시지** | 시스템 경고 시작 | Scale & Pop-in | 300ms | `transform: scale(0.8)` $\rightarrow$ `scale(1.0)` |
| **Defect ID 코드** | 진단 결과 발표 시 | Typewriter Effect + Pulse | 500ms (Type) + 200ms (Pulse) | JS `setTimeout` & CSS `box-shadow`/`filter` |
| **CTA 유도 영역** | 경고 메시지 하단 | Subtle Glow/Blinking Cursor | 지속적 | CSS `:after` pseudo-element with animation loop. |

---
## 📝 개발자를 위한 요약 및 주의사항 (Handover Brief)

1.  **모든 애니메이션은 `requestAnimationFrame`을 사용하여 부드럽게 구현할 것.** 단순 `setTimeout` 기반의 변화는 피합니다.
2.  **글리치 효과는 사운드와 동기화되어야 합니다.** 시각적 충격이 청각적 경고음과 일치해야 몰입도가 높아집니다.
3.  **Deep Crimson Red (`#B30000`)**은 '위험'의 핵심 색상으로, 이 컬러가 애니메이션의 가장 높은 임팩트 지점에 사용되어야 합니다.

</create_file>

📊 평가: 완료 — 요청된 3가지 항목(Transition, Glitch, Alert Overlay)을 포함한 기술적 명세서 초안 작성이 완료되었습니다.
📝 다음 단계: 코다리에게 이 명세서를 바탕으로 실제 개발 환경(`c:\Data\Project\connect-ai`) 내의 JS/CSS 프로토타입 구현 작업을 시작하도록 지시해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\mini_funnel_design_specs\Animation_Specification_v1.0.md
