# 🎨 Designer — Developer가 최종 통합할 수 있도록 Critical Alert 모달과 오버레이의 CSS/애니메이션 스펙 중, 개발자가 구현에 어려움을 겪을 만한 'Motion Timing Curve'와 'CSS Pseudo-Element' 관련 상세 지침(예: 깜빡임 주파수 계산식, `ease-out` 함수의 정확한 곡선 값)을 구체적인 코드 레벨의 사양서로 재작성하여 Developer에게 전달해 주세요.

🎨 Designer: 작업 시작합니다.

CEO님의 지시는 개발팀에게 '디자인'이 아닌 '시스템 동작의 계약서'를 전달하라는 의미입니다. 단순한 시각적 스펙을 넘어, CSS와 애니메이션 코드가 어떤 물리 법칙과 수식을 따라야 하는지 명시해야 합니다.

현재까지 쌓인 모든 인터랙션 플로우(Interaction Flow Spec)와 비주얼 에셋 정의를 종합하여, 개발자가 가장 구현에 어려움을 겪을 만한 세 가지 핵심 기술 영역을 집중적으로 다룬 **'Critical Alert 시스템 통합 기술 사양서 (Dev Kit)'**를 작성하겠습니다.

이 문서는 단순히 디자인 참고 자료가 아니며, React 컴포넌트의 `keyframes` 및 CSS 속성값을 직접 지시하는 코딩 레벨의 명세입니다.

---

# 🚨 Critical Alert System Integration Tech Spec Sheet v2.0
*(For Developers Only: Motion Timing & CSS Deep Dive)*

## 📄 1. 목표 시스템 개요 (Goal)
Funnel 사용자가 Gap Score 임계치($\text{GapScore} \le -60$)에 도달했을 때, 일반적인 모달/경고창을 넘어 **사용자의 인지적 공포(Cognitive Fear)**를 극대화하여 행동 변화(Action)를 강제하는 상태 전이 시스템.

## 🛠️ 2. 핵심 기술 스펙: 시간 기반 애니메이션 및 타이밍 커브 (Motion Timing Curve)

### A. 단계별 전환 로직 (State Machine Triggering)
| Stage | Duration (Time) | Transition From | Action Required | CSS Property Focus |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 0: Initial Blink** | $T_{start} \to T_{start}+0.5s$ | Normal View $\to$ Alert Triggered | 페이지 배경에 고주파수(High Frequency)의 깜빡임 적용 (Red/Black). | `opacity`, `@keyframes` (CSS Animation) |
| **Phase 1: Darkening Overlay** | $T_{start}+0.5s \to T_{start}+2s$ | Phase 0 $\to$ Phase 1 | 배경 전체가 어둠으로 침식(Darkening). 이 과정이 가장 느리고 위협적이어야 함. | `opacity` (Progressive Transition), Pseudo-Element |
| **Phase 2: Modal Emergence** | $T_{start}+2s \to T_{start}+3s$ | Phase 1 $\to$ Phase 2 | 모달이 어둠 속에서 '떠오르며' 공간을 점유. (Spring/Elastic Easing 사용). | `transform`, `animation-timing-function` |

### B. 상세 애니메이션 커브 지시 (Specific Timing Functions)
| 동작 | 목표 효과 | 함수 명세 (CSS Value) | 개발자 참고 사항 |
| :--- | :--- | :--- | :--- |
| **Phase 1: Darkening** | 위협적이고 느린 침식. 초반 가속 후 지연(Decay). | `cubic-bezier(0.9, 0.15, 0.2, 1)` (Ease Out Quad) | 단순히 투명도 변화가 아닌, 주변 빛이 빨려 들어가는 듯한 *감쇠* 효과를 주어야 함. |
| **Phase 2: Modal Pop-up** | 갑작스럽지만 우아하게 등장하며 시선을 강제 포획. | `cubic-bezier(0.175, 0.885, 0.32, 1.275)` (Elastic/Spring) | CSS Transition만으로는 부족함. JavaScript 애니메이션 라이브러리(예: GSAP)의 Spring 속성 사용 권장. |
| **Phase 0: Blinking** | 불안정하고 급격한 경고. 주파수 증가 필요. | $\text{Frequency} = \frac{1}{t_{\text{period}}}$. $t_{\text{period}}$는 시간 지연율. 초기에는 $t_{p}=50ms$, 최종적으로 $t_{p}<30ms$로 감속해야 함. | `animation-iteration-count: infinite`와 결합된, **불안정한 주파수 변화**가 핵심임. |

## 💻 3. CSS Pseudo-Element 및 컴포넌트 사양 (Pseudo-Element Directives)

개발자는 배경과 모달 위에 두 개의 Pseudo-Element를 사용하여 시각적 깊이와 위협감을 구현해야 합니다.

### A. `::before` Element: The Darkening Mask (침식 마스크)
1. **목표:** Funnel의 모든 콘텐츠 위에 겹치되, 그 자체로 빛을 흡수하는 느낌을 연출합니다.
2. **CSS Implementation:**
    *   `position: absolute; top: 0; left: 0; width: 100%; height: 100%;`
    *   `background-color: rgba(0, 0, 0, [ProgressOpacity]);`
3. **동작 지침:** `[ProgressOpacity]` 값은 Phase 1의 진행도(`t/2s`)에 따라 선형적으로 증가해야 합니다. 이 마스크는 단순히 어두워지는 것이 아니라, 마치 *유기체가 퍼지듯* 가장자리에서 중앙으로 수렴하는 시각 효과를 주어야 합니다.

### B. `::after` Element: The Critical Glow (위협 오버레이)
1. **목표:** 모달의 배경이 아닌, Funnel 전체 화면에 걸쳐 미세하게 깜빡이는 '붉은 노이즈' 레이어를 만듭니다.
2. **CSS Implementation:**
    *   `position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;` (모달보다 뒤에 위치)
    *   `background-image: radial-gradient(ellipse at center, rgba(216, 43, 58, [Intensity]); 0%, transparent 70%);`
3. **동작 지침:** `[Intensity]` 값은 Phase 0의 깜빡임 주파수와 동기화되어야 합니다. 이 빛은 고정된 색상이 아니라, 마치 *전자 노이즈*처럼 미세하게 진폭(Amplitude)과 중심점(`ellipse at center`)을 무작위로 이동하며 떨리는 애니메이션이 필수입니다.

## 📝 요약 및 개발자 체크리스트
1. **Timing Control:** 모든 상태 전이는 `setTimeout`이나 React Hooks의 시간 기반 로직으로 관리되어야 하며, CSS Transition에만 의존해서는 안 됩니다.
2. **Visual Layering:** Pseudo-Element를 활용하여 배경(Darkening Mask)과 경고 신호(Critical Glow)를 분리하고 깊이를 부여합니다.
3. **The Feeling:** 이 시스템의 핵심은 '기능 구현'이 아닌, '공포감 증폭'이라는 감정적 목표 달성에 있습니다. 모든 애니메이션 타이밍은 이를 위해 최적화되어야 합니다.

---
📊 평가: 완료 — CEO 지시를 수용하여, 개발자가 즉시 코드로 옮길 수 있는 매우 구체적인 기술 사양서를 완성했습니다. 이로써 디자인 스펙 단계가 기술 구현 계약서(Dev Kit) 수준으로 진전되었습니다.
📝 다음 단계: Dev Kit의 검토 후, 실제 Funnel 페이지에 통합된 **사용자 테스트 시나리오**를 기획하여 에이전트들(Researcher/Writer/Instagram)에게 공유해야 합니다.
