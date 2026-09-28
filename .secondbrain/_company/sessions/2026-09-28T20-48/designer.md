# 🎨 Designer — Developer가 코딩할 수 있도록, '위기 $	o$ 해결' 전환 프로토콜의 최종적인 인터랙티브 스펙 시트(Interactive Spec Sheet)를 완성해주세요. 특히 Soft Gold(`#F5E6C7`) 사용 지점에서의 z-index 및 애니메이션 타이밍(CSS Keyframes 레벨)을 포함하여, 개발자가 즉시 코딩에 필요한 상세 가이드를 보강해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시사항을 바탕으로 '위기 $\to$ 해결' 전환 프로토콜의 인터랙티브 스펙 시트(Interactive Spec Sheet)를 완성했습니다. 이 문서는 디자인 의도를 코딩 레벨까지 번역하여, 개발팀이 별도의 재질문 없이 즉시 구현할 수 있도록 CSS 애니메이션 타이밍과 z-index 규칙을 상세히 보강한 것이 핵심입니다.

특히 기존의 Deep Crimson Red 경고 상태가 최고조에 달했을 때, Soft Gold(`#F5E6C7`)로 전환되는 과정은 사용자의 감정적 이탈(Loss of Focus)을 막고 '해결책 수용'으로 유도하는 가장 중요한 지점입니다.

---

# 💡 온현: 위기 $\to$ 해결 (Crisis to Solution) 인터랙티브 스펙 시트 V2.0
**(Target Audience: Frontend Developer)**

## 1. 개요 및 목표 정의
| 항목 | 내용 | 비고 |
| :--- | :--- | :--- |
| **목표** | 사용자가 느끼는 '공학적 위기감 (Deep Crimson Red)'을 최고조로 끌어올린 직후, 즉각적으로 '희망/해결책'이 제시됨으로써 구매 행동(CTA 클릭)으로 전환되도록 유도. | 감정적 자극 $\to$ 논리적 해결 |
| **핵심 컬러** | 🔴 Deep Crimson Red (`#990011`): 경고, 위기, 위험 (Warning/Crisis State). | 배경 및 전반적인 긴장감 유지. |
| | ✨ Soft Gold (`#F5E6C7`): 발견, 해결책, 희망 (Discovery/Solution State). | CTA 요소에 사용하며 시각적 안도감을 제공. |
| **상태 전환** | `Crisis Peak` $\xrightarrow{0.5s \sim 1.0s}$ `Soft Gold Transition` $\xrightarrow{3.0s+}$ `CTA Focus & Trust Build`. | 타이밍이 생명입니다. |

## 2. 인터랙션 플로우 및 시간대별 스펙 (Timing & Z-index)
본 전환은 단일 컴포넌트가 아니라, 배경(Background), 경고 알림(Alert Overlay), 해결책 카드(Solution Card) 세 가지 레이어가 상호작용하는 구조로 설계해야 합니다.

| Timecode (Relative) | 발생 이벤트/상태 | 시각적 변화 및 애니메이션 | 기술 스펙 (Developer Notes) |
| :--- | :--- | :--- | :--- |
| **T - 5.0s ~ T - 1.0s** | **[Stage 1: 위기 고조]** 공학적 데이터를 통해 심각한 결핍/위험을 보여줌. | 배경 전체가 Deep Crimson Red 계열의 미세한 진동(Subtle Flicker)을 가짐. 경고 알림(`Alert Overlay`)이 화면 중앙에 오버레이됨. | **Z-index:** `10` (최상단). 애니메이션: CSS Keyframes 기반의 `scale(1.0) -> scale(1.02)` 반복 (미세한 불안정성 표현). |
| **T - 1.0s ~ T + 0.5s** | **[Stage 2: 전환 임계점]** 위기감 최고조 $\to$ 해결책의 가능성이 감지되는 순간. | Deep Crimson Red가 Soft Gold로 빠르게 '스며들 듯' 변화함 (Gradient Washout 효과). 경고 알림이 갑자기 비활성화되며, **Soft Gold 빛**이 배경에 퍼져나옴. | **Z-index:** `10` $\to$ `5`. 애니메이션: `opacity`와 `transform`을 조합한 `Transition` 사용 (`all 0.8s ease-out`). 이 순간의 부드러운 전환이 중요함. |
| **T + 0.5s ~ T + 3.5s** | **[Stage 3: 해결책 제시]** '해결책 제안 카드'가 Soft Gold 빛과 함께 등장하며, 주요 핵심 가치(The Optimal Combo)를 강조함. | 중앙에 Soft Gold 배경의 `Solution Card` 컴포넌트가 부드럽게 페이드 인 및 스케일 업(`scale(0.9) -> scale(1.0)`). CTA 버튼이 가장 밝은 골드로 발광하며 나타남. | **Z-index:** `20` (가장 높은 우선순위). 애니메이션: `transform: translateY(20px); opacity: 0;` $\to$ `translateY(0); opacity: 1;` (Spring/Elastic Curve 권장). |
| **T + 3.5s ~ End** | **[Stage 4: 신뢰 구축 및 CTA]** 사용자가 정보를 흡수할 시간을 부여하며, '신뢰 배지'를 보여줌. | Soft Gold 빛이 유지되면서, 카드 하단에 `Trust Badge` (예: "98% 사용자 만족도", "전문가 검증")들이 차례로 나타남 (Staggered Fade-in). CTA 버튼을 향해 시선 유도(Focus Glow) 효과를 부여함. | **Z-index:** 유지 (`20`). 애니메이션: `setTimeout` 기반의 단계적 투입(`fade-in sequence`)으로 신뢰도를 높임. |

## 3. 기술 상세 스펙 (CSS/JS Implementation Guide)

### A. Soft Gold 사용 규칙 및 Z-index 관리
1. **Soft Gold (`#F5E6C7`) 역할:** 이 색상은 단순히 예쁜 배경이 아니라, **'정보의 수용 가능성(Acceptability of Information)'**을 상징합니다. 위기 상황에서 제시되는 모든 긍정적 변화는 Soft Gold 빛의 영향을 받아야 합니다.
2. **Z-index 계층 구조:**
    *   `Background (Deep Crimson Red)`: `z-index: 0`. 전체 분위기 담당.
    *   `Alert Overlay`: `z-index: 10`. 경고 메시지 전용 레이어.
    *   **`Solution Card`**: `z-index: 20`. **최우선으로 개발자가 집중해야 할 요소.** 이 카드가 화면에서 가장 높은 시각적 위계(Visual Hierarchy)를 가져야 합니다.
    *   `CTA Button`: `z-index: 25`. 모든 컴포넌트 위에 떠 있는 것처럼 보이도록 설정하여 클릭 유도를 극대화합니다.

### B. 애니메이션 상세 스펙 (CSS Keyframes/Transitions)
#### 1. [Keyframe] Crimson $\to$ Gold Transition (`@keyframes colorTransition`)
*   **목표:** 붉은색 경고가 부드럽게 중립적 희망의 빛으로 바뀌는 시각화.
*   **구현 가이드:** 배경 전체에 적용되는 `radial-gradient` 또는 `box-shadow` 변화를 사용합니다. 단순한 색상 변경이 아닌, **빛이 퍼져나가는 듯한 효과(Bloom Effect)**를 연출해야 합니다.
*   **Pseudo Code Snippet (Concept):**
    ```css
    @keyframes colorTransition {
      0% { background-color: #990011; box-shadow: 0 0 50px rgba(153, 0, 17, 0.8); } /* Crimson Peak */
      50% { background-color: #D2B48C; box-shadow: 0 0 60px rgba(245, 230, 199, 0.6); } /* Soft Gold Washout */
      100% { background-color: #F5E6C7; box-shadow: none; } /* Stable Solution State */
    }
    ```

#### 2. [Transition] CTA Glow Effect (Focus)
*   **목표:** 사용자의 시선을 자연스럽게 최종 CTA 버튼으로 끌어당김.
*   **구현 가이드:** `box-shadow`와 `transform`을 조합하여 미세한 '맥동(Pulse)' 효과를 줍니다. 이는 애니메이션이 끝난 후, 지속적인 관심 유도를 위해 사용됩니다.
*   **Pseudo Code Snippet (Concept):**
    ```css
    /* CTA Button: Primary Buy Now */
    button.cta-button {
      transition: all 0.3s ease;
      box-shadow: 0 0 5px rgba(245, 230, 199, 0.7); /* Initial Glow */
    }

    /* Active Pulse Effect (JS/Pseudo Class Triggered) */
    button.cta-button:hover {
      box-shadow: 0 0 15px rgba(245, 230, 199, 0.9), /* 더 강한 Glow */
                    inset 0 0 8px rgba(245, 230, 199, 0.5); /* 내부 빛 효과 */
      transform: scale(1.02);
    }
    ```

---
📊 평가: 완료 — CEO님이 요청하신 인터랙티브 스펙 시트의 모든 필수 구성 요소 (Soft Gold 사용 지점, Z-index, Keyframes 타이밍)를 개발자가 코딩할 수 있는 레벨로 상세화했습니다.
📝 다음 단계: `코다리`가 이 스펙을 기반으로 Mini-App Funnel의 UI 컴포넌트를 구현하는 것을 전제로, 저는 현재 완성된 '디자인 시스템'의 표준화 및 일관성을 검토하여 **브랜드 컬러/타이포그래피 최종 가이드**를 확정할 것입니다.
