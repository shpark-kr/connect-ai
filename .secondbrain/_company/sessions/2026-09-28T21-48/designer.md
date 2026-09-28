# 🎨 Designer — Mini-App Funnel의 '위기 $	o$ 해결' 전환 프로토콜 인터랙티브 스펙 시트(Interactive Spec Sheet)를 최종 확정하고, 이를 개발자가 코딩할 수 있도록 CSS Keyframes 레벨까지 상세한 코드 기반 지침을 완성하여 developer에게 전달하세요.

🎨 Designer: 작업 시작합니다. Mini-App Funnel의 핵심 전환 프로토콜을 개발자가 바로 코딩할 수 있는 레벨로 최종 스펙화하겠습니다. 이 스펙은 단순히 '애니메이션'을 나열하는 것이 아니라, CSS Keyframes와 DOM 요소 간의 상호작용(Interactivity)과 시각적 계층 구조(Visual Hierarchy) 변경까지 포함해야 합니다.

가장 중요한 것은 **Deep Crimson Red (위기감)**에서 **Soft Gold (해결책 수용)**으로 전환될 때 발생하는 '정보 처리 과정'을 애니메이션으로 구현하는 것입니다. 이 과정을 통해 사용자에게 시스템이 위기를 인식하고, 전문가의 개입(Solution)을 통해 안정화되는 공학적 신뢰를 심어줘야 합니다.

저는 지난 작업을 기반으로 `FunnelTransitionModule_SpecSheet_V2.0.md` 파일을 최종 코딩 지침서로 덮어씁니다. 이 파일은 개발팀에게 전달할 단일 진실 공급원(Single Source of Truth)이 될 것입니다.

<create_file path="c:\Data\Project\connect-ai\assets\mini-app\FunnelTransitionModule_SpecSheet_V3.0.md"># 🚨 Mini-App Funnel 전환 프로토콜: 인터랙티브 스펙 시트 (Interactive Spec Sheet) V3.0 #

**문서 목적:** Deep Crimson Red 경고 상태에서 Soft Gold 해결책 제안 단계로의 부드럽지만 명확한 시스템 전환을 위한 최종 코드 기반 지침 제공.
**대상:** 프론트엔드 개발팀 (React/Vue + CSS Keyframes 담당)
**필수 아셋:**
1.  `DeepCrimsonRed_Overlay`: 배경 오버레이 및 경고 메시지 컴포넌트.
2.  `SoftGold_Panel`: 해결책 제안 카드 컴포넌트.
3.  `SystemPulseAnimation`: 전환 과정에서 사용될 미묘한 애니메이션 효과 (예: 펄스, 스캔라인).

---

## 🔴 단계 1: Deep Crimson Red 경고 상태 (Crisis State)

**상태:** 시스템이 공학적 위기(HOMA-IR, hs-CRP 등 전문 지표 기반)를 인지하고 사용자에게 강력한 주의를 환기시키는 상태.
**시각 목표:** 긴급성, 심각성, 즉각적인 행동 필요성을 극대화합니다.

### 1.1. 레이아웃 및 스타일 스펙
*   **배경 오버레이:** 전체 Viewport에 `opacity: 0.8`의 Deep Crimson Red 계열 필터 적용. (CSS Filter: hue-rotate(345deg) / brightness(0.9)).
*   **핵심 요소 배치:** 중앙에 '위기 진단 결과' 컴포넌트를 배치하고, 주변부에 깜빡이는 경고 메시지(`blink`)를 배치합니다.
*   **Deep Crimson Red Keyframe (경고):**
    ```css
    @keyframes warning-pulse {
        0%, 100% { box-shadow: 0 0 15px rgba(220, 38, 38, 0.7); } /* Deep Crimson */
        50% { box-shadow: 0 0 30px rgba(220, 38, 38, 1), inset 0 0 10px rgba(255, 0, 0, 0.5); }
    }
    /* 적용: 경고 진단 패널에 반복 적용 (animation: warning-pulse 1s infinite alternate;) */
    ```

### 1.2. 상호작용 로직 (Interaction Logic)
*   **트리거:** 전문 지표 수치(e.g., HOMA-IR > 3.0)가 임계치를 초과하는 순간, 즉시 Deep Crimson Red 오버레이가 전체 화면을 뒤덮으며 전환 시작.
*   **CTA 비활성화:** 이 상태에서는 모든 하위 CTA 버튼이 `pointer-events: none;` 처리되어 클릭 불가 상태를 유지합니다.

---

## 🔄 단계 2: 전환 프로토콜 (The Transition) - [Critical]

**목표:** 위기 인식(Danger) $\to$ 해결책 탐색(Hope/Trust). 이 과정은 '시스템의 재부팅' 또는 '데이터 필터링'처럼 보이게 해야 합니다.
**지속 시간:** 총 1.0초 ~ 1.5초 (타이밍 매우 중요)

### 2.1. 애니메이션 시퀀스 (Sequence Details)
| Time | Action | Visual Change | CSS/DOM Effect | Duration |
| :--- | :--- | :--- | :--- | :--- |
| **T + 0.0s** | **Deep Fade Out** | Deep Crimson Red 오버레이가 강하게 어두워지며 빠르게 사라짐 (블랙 아웃 효과). | `background-color: #000; opacity: 1` $\to$ `opacity: 0` (Transition: 0.2s ease-out) | 0.2s |
| **T + 0.2s** | **System Pulse/Scanline** | 화면 전체에 짧은 '스캔라인' 효과(Scanline animation)가 가로지르며 데이터 로딩을 연출. (기술적 신뢰도 부여). | `::before` pseudo-element 사용. `@keyframes scanline { transform: translateY(-100%) to translateY(100%); }` | 0.3s |
| **T + 0.5s** | **Soft Gold Reveal Trigger** | 화면의 중심부만 부드럽게 밝아지며 Soft Gold(`#F5E6C7`) 계열의 'Solution Panel' 영역이 나타남. | `opacity: 0` $\to$ `opacity: 1`. (Transition: 0.3s ease-in) | 0.3s |
| **T + 0.8s** | **Soft Gold Stabilization** | 배경 색상이 Deep Navy/Gold Tone으로 안정화되며, 해결책 제안 카드가 애니메이션과 함께 나타남. | `background-color: #1a2e45;` (Deep Navy) 유지. Soft Gold 컴포넌트에 미묘한 `scale(1.0)` 진입 효과 적용. | 0.7s |

---

## ✨ 단계 3: Soft Gold 해결책 제안 상태 (Solution State)

**상태:** 시스템이 위기 데이터를 분석하여, 전문가가 검증한 구체적이고 즉각적인 '해결책 조합(The Optimal Combo)'을 제시하는 안정화된 상태.
**시각 목표:** 신뢰감, 전문성, 희망 (하지만 너무 가볍지 않게).

### 3.1. 레이아웃 및 스타일 스펙
*   **배경/전체 분위기:** Deep Navy 계열의 배경 유지. Soft Gold(`F5E6C7`)를 액센트 컬러로 사용하여 신뢰와 고가치 상품을 상징합니다.
*   **해결책 카드 컴포넌트:** 이 카드는 단순한 버튼 그룹이 아닌, **'진단 결과 기반 제안'**처럼 보이게 디자인해야 합니다. (예: "선생님께 맞는 솔루션 조합", "위험도 A를 낮추는 3단계 프로세스").
*   **Soft Gold Keyframe (신뢰):** Soft Gold 배경 요소에 미묘한 '따뜻한 광원 효과'를 주기 위해 `box-shadow` 애니메이션을 사용합니다.
    ```css
    @keyframes warm-glow {
        0%, 100% { box-shadow: 0 2px 8px rgba(245, 230, 199, 0.3); }
        50% { box-shadow: 0 4px 12px rgba(245, 230, 199, 0.6); } /* 미묘한 광원 효과 */
    }
    /* 적용: '해결책 조합' 컨테이너에 주기적 배경 그림자 애니메이션 적용 */
    ```

### 3.2. 최종 CTA 로직 (Conversion Threshold)
*   **CTA 버튼:** `[The Optimal Combo] 자세히 보기` 버튼은 Deep Navy와 대비되는, 가장 눈에 잘 띄는 Soft Gold 배경을 사용합니다.
*   **버튼 인터랙션:** 마우스 오버 시, 단순한 색상 변화가 아닌, '클릭 전 에너지를 응축하는 듯한' 미세한 스케일 업(Scale Up) 애니메이션과 함께 `cursor: pointer;`를 명확히 제공합니다.

---
**개발자 참고 사항:**
*   전환 과정 (T + 0.2s ~ T + 0.8s)의 타이밍은 사용자 체감에 따라 미세 조정이 필요하며, 반드시 **지연 시간(Delay)**을 활용하여 각 단계가 끊어지지 않고 물 흐르듯 연결되는 느낌을 구현해야 합니다.
*   모든 전환 애니메이션은 `will-change: transform, opacity;` 속성을 사용하여 성능 최적화를 고려해 주세요.

</create_file>

📊 평가: 완료 — 요청된 '위기 $\to$ 해결' 프로토콜의 인터랙티브 스펙 시트(V3.0)를 CSS Keyframes 레벨까지 상세화하여 개발자에게 즉시 전달 가능한 형태로 완성했습니다.
📝 다음 단계: Developer 에이전트를 호출하여, 이 `FunnelTransitionModule_SpecSheet_V3.0.md` 파일에 기반한 Mini-App Funnel의 프론트엔드 컴포넌트 코딩을 시작하도록 지시해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\assets\mini-app\FunnelTransitionModule_SpecSheet_V3.0.md
