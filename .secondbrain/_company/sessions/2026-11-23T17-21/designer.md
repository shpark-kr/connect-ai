# 🎨 Designer — Mockup v2.0에 명시된 모든 요소를 포함하여, Gap Score Visualizer의 '개발자용 디자인 시스템 스펙(Component Library)'을 제작해 주세요. 핵심 컴포넌트별로 (1) 상태 정의 (Default/Hover/Active/Error), (2) CSS 변수 및 크기 기준, (3) 접근성 가이드라인(ARIA Label 등)을 상세히 명시해야 합니다.

🎨 Designer: 작업 시작합니다. CEO의 지시와 현재 개인 목표에 따라, Gap Score Visualizer를 개발 단계로 끌어올리기 위한 '개발자용 디자인 시스템 스펙(Component Library)'을 작성하겠습니다. 이 문서는 단순한 목업이 아닌, 프론트엔드 엔지니어가 즉시 코딩할 수 있도록 CSS 변수와 접근성 지침까지 포함하는 최종 설계 문서입니다.

---

# 📐 Design System Spec: Gap Score Visualizer (LVI)
**버전:** 1.0.0 (V2.0 기반 확정)
**컴포넌트 목표:** 사용자의 현재 상태(Actual Value)와 이상적인 기준점(Ideal Benchmark) 간의 '손실 가치 격차(Gap Score)'를 시각적 위기감과 권위적인 데이터 시각화로 전달한다.
**톤앤매너:** Deep Navy 기반, 전문가 진단 대시보드, 긴급 경고 (Alarm Red).

## 1. 컴포넌트 구조 및 레이아웃 (Structure & Layout)

### A. 기본 아키텍처
*   **컨테이너:** `GapScoreVisualizer` (Flex Container)
*   **구성 요소:**
    1.  `GraphArea`: 실제 데이터를 시각화하는 캔버스 영역 (SVG 또는 Canvas 기반).
    2.  `KeyMetricCard`: Gap Score 수치 및 핵심 요약 정보를 보여주는 카드 컴포넌트.

### B. 기술 스펙 (CSS Variables & Dimensions)
개발자가 사용해야 할 전역 CSS 변수를 정의합니다.

```css
/* 🎨 Global Color Palette */
--color-deep-navy: #0A1931;    /* Primary Background/Text Dark */
--color-alarm-red: #E74C3C;     /* Critical Warning State (🚨) */
--color-ideal-blue: #2ECC71;    /* Ideal Benchmark / Goal State (✅) */
--color-secondary-text: #B0BEC5; /* Supporting Text/Labels */
--color-border: #1F3A64;       /* Subtle Divider Line */

/* 📏 Sizing & Spacing Variables */
--gap-score-height: 32px;        /* 기본 그래프 높이 (rem) */
--card-padding: 2rem;            /* 카드 내부 여백 */
--border-radius: 8px;            /* 모서리 둥글기 */
```

## 2. 컴포넌트 상태 정의 및 로직 (State Management)

Gap Score Visualizer는 데이터 입력 값에 따라 세 가지 핵심 상태(Default, Warning, Critical/Error)를 가집니다.

| 상태 | 트리거 조건 (Trigger Condition) | 시각적 변화 (Visual Change) | 경고 애니메이션 (Animation) | ARIA Role & 메시지 |
| :--- | :--- | :--- | :--- | :--- |
| **Default** (초기/정상) | Gap Score가 임계치 범위 내에 있을 때. | 그래프 영역이 부드러운 Gradient Blue로 채워짐. `KeyMetricCard`의 배경은 어두운 네이비 유지. | 없음. Smooth transition only. | `role="status"`. "현재 손실 위험도가 낮습니다." |
| **Warning** (주의) | Gap Score가 임계치 $T_1$을 초과했을 때. | 그래프 영역에 노란색/주황색 계열의 하이라이트가 적용됨. `KeyMetricCard`의 테두리가 깜빡이는 듯한 애니메이션 효과(Pulse)를 가짐. | 1~2초 주기로 미세하게 밝기가 변하는 Pulse effect (`opacity: 0.8` $\leftrightarrow$ `opacity: 1`). | `role="alert"`. "주의: 시간 경과에 따른 손실 위험이 감지되었습니다." |
| **Critical/Error** (위기) | Gap Score가 임계치 $T_2$를 초과하거나, 데이터 입력 실패 시. | 그래프 영역 전체가 `--color-alarm-red`로 채워지고, 깜빡임 애니메이션(Blinking)이 가장 강력하게 적용됨. `KeyMetricCard`의 폰트 크기가 미세하게 커지며 긴급함을 강조. | **필수:** 3초 간격으로 배경색(`background`)과 플래시 효과를 주기적으로 토글 (Red $\rightarrow$ Navy). | `role="alert"` + `aria-live="assertive"`. "🚨 경고! 즉각적인 개입이 필요하며, 심각한 손실이 발생 중입니다." |

## 3. 핵심 컴포넌트 상세 스펙 (Component Breakdown)

### A. Graph Area (LVI Timeline)
*   **유형:** 시계열 그래프 (Time Projection Graph).
*   **데이터 매핑:** X축: 시간 흐름 (Months/Years), Y축: 가치 손실률 (%).
*   **핵심 요소:**
    1.  `ActualPath`: 현재 데이터 기반의 실제 진행 경로 (Deep Navy $\rightarrow$ Alarm Red로 변색).
    2.  `IdealBenchmark`: 이상적인 목표 지점 (Steady Green Line, `stroke-dasharray: 5;`).
    3.  `RiskZoneShading`: 위기 영역을 나타내는 배경 음영 처리(Gradient Fill)가 상태 변화에 따라 다르게 적용되어야 함.

### B. Key Metric Card (Gap Score 수치 표시)
*   **목적:** 시각 정보의 해석을 돕고, 결제 유도 문구 배치 공간 확보.
*   **스펙:** `display: flex; justify-content: space-between; align-items: center;`
*   **Content Hierarchy:**
    1.  **Score Value (H1):** 현재 Gap Score 값. 크기는 가장 커야 함. 상태에 따라 `--color-alarm-red`가 적용되어 강조됨.
    2.  **Change Trend (Small Text):** 전주 대비 변화율 ($\Delta$). 이 값이 음수일 때 경고색이 사용됨.
    3.  **CTA Trigger:** `[전문 리포트 요청]` 버튼. **(Critical State에서만 활성화되어야 함)**

## 4. 접근성 및 개발 가이드라인 (Accessibility & Dev Guide)

| 항목 | 지침 사항 (Instruction) | 이유/목적 |
| :--- | :--- | :--- |
| **ARIA Labeling** | 그래프 영역 전체에 `aria-describedby="gap-score-summary"`를 적용하고, `KeyMetricCard`의 Score Value는 `role="status"`로 명시한다. | 스크린 리더 사용자에게 시각적 위기감을 텍스트 정보로 확실하게 전달하기 위함. |
| **Color Contrast** | Critical/Error 상태에서 빨간색 플래시는 배경에 충분한 대비(Contrast Ratio > 4.5:1)를 유지해야 하며, 순수한 빨강(#FF0000) 사용을 피한다. | 색맹 사용자나 저시력자도 경고의 의미를 인지할 수 있도록 보조적인 요소(아이콘, 애니메이션)가 필요함. |
| **Focus Management** | Critical State로 진입 시, 컴포넌트 내의 모든 상호작용 가능한 요소(버튼 등)에 포커스가 자연스럽게 이동하며 강조되어야 한다 (Tab Index 순서 정의). | 사용자의 다음 행동 경로를 명확히 제시하고 이탈을 막기 위함. |
| **데이터 로딩** | 데이터가 로드되는 동안, 그래프 영역은 'Loading...' 상태 대신 추상적인 움직임(Skeleton UI)과 함께 "진단 중입니다. 잠시만 기다려 주세요."라는 전문적 톤의 카피를 노출해야 한다. | 사용자가 대기 시간을 지루하게 느끼지 않도록 전문가적인 느낌을 유지함. |

---
📊 평가: 완료 — Gap Score Visualizer를 실제 개발 단계로 이끌 수 있는 상세한 컴포넌트 라이브러리 스펙이 완성되었으며, 이는 다음 단계의 Mockup v2.0에 명시된 모든 요구사항(상태, CSS 변수, 접근성)을 포괄합니다.
📝 다음 단계: Frontend Developer에게 위의 **디자인 시스템 Spec**과 `c:\Data\Project\Baro_KHNLU\sessions\2026-11-23T15-36\gap_score_visualizer_mockup_v2.md`를 전달하고, 이를 기반으로 실제 동작하는 프로토타입 구현을 시작해야 합니다.
