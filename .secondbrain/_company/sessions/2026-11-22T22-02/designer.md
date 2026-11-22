# 🎨 Designer — Researcher가 정의한 '20년 전 vs 현재 인슐린 저항성 곡선' 등 핵심 비교 데이터를 기반으로, A/B 테스트 및 변수 기반 구현이 가능한 시각화 컴포넌트(그래프)를 최종 디자인 명세서로 작성해 주세요. 이 그래프는 '시스템 오류'의 구체적인 Gap을 가장 강력하게 보여줄 수 있도록 전문적이고 긴급한 톤앤매너를 유지해야 합니다.

🎨 Designer: 작업 시작합니다.

## 🚀 최우선 작업 결정 및 실행 보고

**[가장 가치 있는 단일 작업]**: Researcher가 제공하는 'Defect ID 기반 생체 지표(예: 인슐린 저항성 곡선)' 데이터를 가장 강력하게 시각화하고, A/B 테스트를 염두에 둔 **변수 기반 그래프 컴포넌트 최종 디자인 명세서** 작성.

*   **이유**: 회사 목표가 수익 극대화이며, 이는 곧 '정보 제공'을 넘어 '위험 인식(Gap) $\rightarrow$ 해결책 제시(CTA)'의 흐름으로 이어져야 합니다. 이 그래프는 모든 콘텐츠에서 사용할 수 있는 핵심 시각적 근거물(Visual Proof Point)이 되며, 이를 표준 컴포넌트화하는 것이 가장 큰 레버리지를 창출합니다.
*   **에이전트 분배**: 🎨 Designer (Lead Designer).

---

## 📊 디자인 명세서: Defect ID 추적 시각화 그래프 컴포넌트 V1.0

다음은 '20년 전 vs 현재 인슐린 저항성 곡선' 등의 생체 지표 비교 데이터를 담을 수 있는, React 기반의 **변수(Variable-based) 인터랙티브 차트 컴포넌트** 명세서입니다. 이 컴포넌트는 단순한 그래프가 아니라, 사용자에게 '위험 신호(Defect)'를 경고하는 기능을 수행합니다.

### 1. 목적 및 기능 정의 (Goal & Function)

| 항목 | 내용 | 비고 |
| :--- | :--- | :--- |
| **핵심 목표** | 시각적 공포감(Fear of Loss) 극대화 및 전문성 확보. '나이가 들어서' 문제가 아니라, '시스템 오류가 발생했다'는 과학적 인식을 주입. | **Defect ID 프레임워크 적용.** |
| **주요 기능** | 1. 과거 정상 상태(Baseline). 2. 현재 측정된 위험 상태(Defect Zone). 3. 최적의 관리/개선 시점(Solution Curve)을 시간 축에 걸쳐 명확하게 대비하여 보여줌. | 인터랙티브 요소 필수 (Hover, Zoom). |
| **A/B 테스트 변수** | 그래프 색상 팔레트 (컬러 A vs B), 비교 기준 데이터 포인트를 강조하는 방식 (라인 강조 vs 영역 음영). | CSS Variable 기반 제어. |

### 2. 디자인 및 UX 명세 (Design Specification)

#### A. 컬러 시스템 (Color Palette - Defect Focus)
*   **배경색 (`--color-bg`):** `#0A1931` (짙은 네이비/블랙 계열, 전문적이고 차분함 유지)
*   **정상 상태 (Baseline / 과거):** `--color-normal`: `#4CAF50` (진한 녹색. 안정성 상징. 희망의 톤).
*   **위험 상태 (Defect Zone / 현재):** `--color-defect`: `#D32F2F` (강렬한 적색. 경고/긴급성을 즉각적으로 전달).
*   **솔루션 강조 (Solution Curve):** `--color-solution`: `#FFC107` (골드 톤. '기회'와 '해결책'을 상징하며, 시선 집중 유도).
*   **텍스트/축:** `#E0E0E0` (밝은 회색).

#### B. 타이포그래피 및 레이아웃
*   **폰트:** Pretendard 또는 Noto Sans KR (가독성 최우선).
*   **레이아웃:** 16:9 비율의 와이드 컴포넌트 형태. 그래프 자체를 중앙에 배치하고, 좌측과 우측에 핵심 요약 박스(Callout Box)를 배치하여 **데이터 해석 가이드**를 제공해야 합니다.

#### C. 인터랙션 및 변수 기반 구현 (Technical Requirement)
1.  **Tooltip/Hover:** 사용자가 특정 시간대나 지표 포인트를 마우스 오버하면, 해당 포인트의 *정량적 수치*와 그 의미(예: "이 시점의 인슐린 저항성은 정상 범위보다 25% 높으며, 이는 [Defect ID]를 의미합니다.")가 **팝업**으로 표시되어야 합니다.
2.  **Area Shading:** '위험 구간'은 단순히 선으로 그리는 것이 아니라, 배경색과 대비되는 `--color-defect`로 **점진적인 음영(Gradient Area)**을 깔아 공포감을 극대화합니다. (이 부분이 가장 중요한 시각적 연출입니다.)
3.  **State Management Props:** 컴포넌트는 다음 3가지 주요 `props`를 받아야 합니다.
    *   `dataPoints: {year: number, normalValue: number, defectValue: number}` (핵심 데이터 배열)
    *   `comparisonGoal: string` (예: "인슐린 저항성 감소")
    *   `solutionStrategy: string` (CTA와 연결되는 해결책 설명 텍스트)

### 3. 구현 코드 스펙 예시 (Conceptual Implementation Snippet)

```css
/* -- Design System Variables for Graph Component */
:root {
  --color-bg: #0A1931; /* Base Background */
  --color-normal: #4CAF50; /* Baseline Green */
  --color-defect: #D32F2F; /* Danger Red - Key Highlight */
  --color-solution: #FFC107; /* Gold/Yellow - Opportunity */
}

/* -- Component Structure (Conceptual React State) */
<GraphComponent 
    dataPoints={researcherDataArray} 
    comparisonGoal="인슐린 저항성 개선" 
    solutionStrategy="식이요법 및 근력 운동 병행"
/>

/* -- CSS for Defect Area Highlighting */
.defect-area {
  /* 이 영역은 절대적인 음영을 가져야 함 */
  background: linear-gradient(to right, rgba(211, 47, 47, 0.3), transparent); 
  opacity: var(--defect-intensity, 0.8); /* 강도 조절 가능하도록 변수화 */
}
```

---

📊 평가: 완료 — 핵심 비교 데이터를 구조적이고 기술적으로 구현 가능한 컴포넌트 명세로 완성하여 콘텐츠 제작의 표준을 확립함.
📝 다음 단계: 이 디자인 스펙을 기반으로, 실제로 '인슐린 저항성' 데이터를 넣어 **테스트용 와이어프레임(Figma/Sketch)** 초안을 작성하고 개발자에게 전달할 최종 에셋 세트를 준비해야 합니다.
