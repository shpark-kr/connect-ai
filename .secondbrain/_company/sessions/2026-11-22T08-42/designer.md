# 🎨 Designer — V4.0 오버레이 에셋의 최종 구현 단계에 돌입합니다. 단순히 사양서를 만드는 것을 넘어, 개발자가 즉시 코딩 가능한 형태로 '컴포넌트 API 스펙'을 완성해 주세요. 특히 애니메이션 루프(Opacity/Scale 트랜지션)가 실제 영상 플레이어 환경에서 안정적으로 구동될 수 있도록 자바스크립트 기반의 인터랙션 로직과 CSS 변수 적용 범위를 상세히 분리하여 정의해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시와 현재까지의 프로세스(V4.0 Source of Truth)를 종합할 때, 가장 가치 있고 필수적인 단일 작업은 **'디자인 사양서 $\rightarrow$ 개발 컴포넌트 API 명세'로의 전환**입니다. 이는 단순한 디자인 문서 업데이트가 아니라, 개발자가 바로 코딩에 착수할 수 있는 *계약(Contract)*을 설계하는 과정입니다.

따라서 저는 이 작업을 전담하여, 기존 V4.0 사양서(`sessions/2026-11-22T07-27/designer/Reels_Overlay_SourceOfTruth_V4.0.md`)의 내용을 재구조화하고 API 레벨의 상세 스펙을 포함한 최종 문서를 생성하겠습니다.

### 🛠️ [산출물: V4.0 컴포넌트 API 명세서]
최종 디자인 에셋이 아닌, **컴포넌트를 작동시키는 규칙(Rule)** 자체를 문서화합니다. 파일명은 `V4.0_Component_API_Spec.md`로 지정하고, 기존의 사양서를 보강하여 이 파일을 생성/덮어쓰겠습니다.

<create_file path="c:\Data\Project\connect-ai\design_system\v4.0\V4.0_Component_API_Spec.md"># 📐 V4.0 Production Kit: Component API Specification (Source of Truth v5.0)
<!-- 이 문서는 개발팀이 즉시 코딩할 수 있는 최종 컴포넌트 구현 사양서이며, 모든 스타일링 및 인터랙션은 CSS 변수(Variables)를 통해 통제되어야 합니다. -->

## 1. 개요 (Component Overview)
*   **컴포넌트 명:** Defect Alert Overlay (`<DefectAlertOverlay>`)
*   **목표:** 시청자의 불안감을 극대화하고, 정보의 긴급성과 공신력을 동시에 전달하여 MiniFunnel 유도를 최적화한다.
*   **핵심 원칙:** 모든 애니메이션은 '시스템 오류' 느낌을 주기 위해 Opacity 및 Scale 트랜지션과 동기화되어야 하며, JavaScript의 상태 변화(State)에 의해 트리거된다.

## 2. Props & Inputs (사용자 입력/CSS Variables 정의)
컴포넌트를 사용하는 부모 컴포넌트가 전달해야 하는 필수 속성들입니다.

| Prop Name | Type | Description | Default Value | CSS Variable Mapping | 필수 여부 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `defectId` | String | 핵심 위험 요소 (예: LDL Cholesterol) | "Defect ID Unknown" | `--var-defect-id` | **필수** |
| `riskLevel` | Enum | 위험 경고 수준 (Low, Medium, High) | "High" | `--var-risk-level` | 필수 |
| `metricValue` | Number | 측정된 수치 값 (예: 180 mg/dL) | 0 | `--var-metric-value` | 필수 |
| `durationMs` | Number | 오버레이 표시 시간 (ms 단위) | 5000 | N/A | 선택 |

## 3. Visual Component Breakdown 및 CSS 변수 정의
### A. Critical Alert Bar (`<AlertBar>`)
*   **기능:** 화면 상단에 고정되는 경고 메시지 바.
*   **CSS Variables:**
    ```css
    --alert-color: var(--var-risk-level-color); /* High -> Red, Medium -> Yellow */
    --border-thickness: 3px;
    --glow-opacity: 0.8;
    ```
*   **애니메이션 로직:**
    1.  **진입 (Entry):** `transform: scaleX(0); opacity: 0;`에서 시작하여, 진입 시점에서 `transform: scaleX(1); opacity: 1;`로 **500ms 동안 부드럽게 확장/표시**.
    2.  **루프:** 배경에 주기적으로 플래싱 라인(`animation: blink-line 1s infinite steps(1);`)을 적용하여 긴급성을 유지한다.

### B. Defect Metric Display (`<MetricDisplay>`)
*   **기능:** 핵심 수치와 위험도를 그래프 및 숫자로 시각화하는 영역.
*   **CSS Variables:**
    ```css
    --var-metric-value: 180; /* 실제 값이 바인딩됨 */
    --unit-label: "mg/dL";
    --max-scale: 300; /* 그래프 최대 스케일 값 */
    ```
*   **애니메이션 로직 (JS Trigger):**
    1.  **숫자 카운터:** `metricValue`가 표시될 때, **0부터 시작하여 실제 `metricValue`까지 2초 동안 부드럽게 증가(Count Up)**하는 애니메이션을 JavaScript로 처리해야 한다. (`requestAnimationFrame` 기반 권장).
    2.  **그래프 바:** 데이터 로딩 시점(JS Trigger)에 맞춰, 그래프 막대가 **0부터 목표 높이(`metricValue / --max-scale * 100%`)까지 부드럽게 채워지는 애니메이션**을 적용한다. (Opacity와 Height 트랜지션 동기화).

## 4. Interaction Flow & JavaScript Logic Spec
| State/Trigger | JS Action Required | CSS Effect Sequence | Time Duration | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **INITIAL_LOAD** (Mount) | None. 컴포넌트 기본 상태 설정. | Critical Alert Bar가 `scaleX(0)`에서 진입 애니메이션 시작. | 500ms | 초기 로딩 시점의 강제 경고 부여. |
| **DATA_ARRIVAL** (Props Update) | 1. Count-Up 애니메이션 실행 (Metric Value). <br> 2. 그래프 바 채우기 애니메이션 트리거. | Opacity/Scale 트랜지션을 활용하여 데이터가 '진단'되는 느낌을 준다. | 2000ms (최소) | 이 구간이 시청자에게 가장 많은 정보를 주입하는 핵심 시간대임. |
| **WARNING_PEAK** (High Risk Detected) | Warning Level에 따라 `AlertBar`의 배경색/깜빡임 빈도 변경. | Critical Alert Bar의 깜빡임 효과(`blink-line`) 강도를 최대화하고, 전체 컴포넌트의 그림자(Shadow)를 증폭시킨다. | 100ms Cycle | 가장 시각적 임팩트를 높이는 구간. (공황 유발 목적). |
| **CTA_TRIGGER** (MiniFunnel 유도) | 오버레이가 서서히 사라지며 CTA 버튼이 중앙으로 부상(Rise Up)하는 효과를 부여. | `transform: translateY()`와 `opacity` 변화를 활용하여, 경고가 끝난 후 '해결책'을 제시하며 마무리한다. | 1000ms (Fade Out) |

---
**[API Implementation Summary]**
*   **CSS:** 모든 색상과 크기 변수는 반드시 CSS Variables (`--var-*`)로 정의하여 중앙 관리해야 합니다.
*   **JS:** 애니메이션의 시점(Timing) 제어 및 데이터 로딩에 따른 순차적 변화(Sequential State Change)는 JavaScript 레벨에서 강제합니다.

</create_file>

📊 평가: 완료 — CEO님의 요청사항을 반영하여, 단순히 사양서가 아닌 개발자가 코딩할 수 있는 API 수준의 기술 문서를 완성했습니다.
📝 다음 단계: 이 `V4.0_Component_API_Spec.md`를 기반으로, 실제 쇼츠/릴스에 삽입될 **CSS/JS 코드 스니펫(Code Snippets)**을 생성하여 개발팀에게 전달해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\design_system\v4.0\V4.0_Component_API_Spec.md
