# 🎨 Designer — 완성된 'Defect ID 위협 보고서' V3.0 Production Kit 문서를 기반으로, Critical Alert UI와 Defect Metric Display 컴포넌트를 개발자가 즉시 코딩할 수 있는 최종 Source of Truth 문서로 확정해 주세요. CSS 변수 정의(Variables)를 전면적으로 적용하고, 애니메이션 로직(특히 플래싱 라인과 숫자 카운터 효과)에 대한 상세한 인터랙션 스펙을 포함해야 합니다.

🎨 Designer: 작업 시작합니다. CEO 지시에 따라 'Defect ID 위협 보고서' V3.0 Production Kit을 개발자가 즉시 코딩할 수 있는 최종 Source of Truth 문서로 확정하겠습니다.

이 문서는 단순한 디자인 가이드가 아니라, CSS 변수와 인터랙션 스펙(Animation Logic)까지 포함하여 **개발팀이 별도의 질문 없이 바로 구현 가능한 수준**의 '최종 개발 원본'을 목표로 합니다.

---

# ⚙️ 온현 Defect ID 위협 보고서 V3.0 Production Kit (Source of Truth)

## I. Global System Variables 정의 (CSS Foundation)

모든 컴포넌트는 아래 CSS 변수(Custom Properties)를 기반으로 스타일링되어야 하며, 이를 통해 테마 변경 및 유지보수가 용이합니다.

| 변수명 | 값 (Value) | 용도/설명 |
| :--- | :--- | :--- |
| `--color-primary` | `#B01F34` | **위협 경고(Defect):** 핵심 액션 색상, 위험 요소 하이라이트. |
| `--color-secondary` | `#FFD700` | **경고/강조(Alert):** Metric 강조 및 CTA 배경색 (골드톤). |
| `--color-background` | `#121823` | 메인 섹션 배경색 (다크 네이비 계열). |
| `--color-text-main` | `#F0F4F8` | 일반 본문 텍스트 색상. |
| `--color-alert-bg` | `#1E2739` | 경고 박스/카드 배경 (Primary보다 밝은 다크톤). |
| `--color-border-line` | `rgba(50, 80, 120, 0.4)` | 컴포넌트 분리 및 구분선. |
| `--font-family-main` | 'Pretendard', sans-serif | 본문/제목 기본 서체. |
| `--spacing-unit` | `1rem` | 표준 간격 단위 (Padding, Margin). |

**폰트 스케일링 규칙:**
*   H1: 3rem (`calc(4 * var(--spacing-unit))`)
*   H2: 2.5rem (`calc(3.5 * var(--spacing-unit))`)
*   Body Text: 1rem (`var(--spacing-unit)`)

## II. 핵심 컴포넌트 스펙 상세 정의 (Component Specifications)

### 🚨 Component A: Critical Alert UI (시스템 경고 바)

이 컴포넌트는 사용자의 주의를 즉각적으로 끌어내며, 'Defect' 발생을 알리는 가장 중요한 시각적 요소입니다.

**1. 구조 및 레이아웃:**
*   **Container:** `display: flex; align-items: center;`
*   **Visual Element:** 좌측에 플래싱 경고 아이콘(🚨) 배치.
*   **Text Area:** 제목(`H3`)과 상세 메시지(`P`)를 포함하며, **경고의 심각성 레벨**을 색상으로 구분합니다.

**2. 스타일 및 CSS 변수 적용:**
*   `background-color: var(--color-alert-bg);`
*   `border-left: 6px solid var(--color-primary);` (가장 중요한 시각적 경고선)
*   **텍스트 강조:** `strong` 태그 사용 시, 배경색을 `--color-secondary`로 지정하고 글자색을 검은 계열로 대비시켜 가독성을 높입니다.

**3. 인터랙션 스펙 (Animation Logic):**
*   **플래싱 경고선 (Flashing Border Effect):**
    *   **CSS:** `@keyframes flashAlert { 0%, 100% { box-shadow: 0 0 5px var(--color-primary); opacity: 1; } 50% { box-shadow: none; opacity: 0.8; } }`
    *   **적용:** 경고 바 전체 컨테이너에 `animation: flashAlert 1s infinite alternate;` 적용. (지속적인 불안감 조성)

### 📈 Component B: Defect Metric Display (측정 가능한 결함 수치 표시기)

단순한 숫자가 아닌, 'Defect'의 심각성을 직관적으로 보여주는 애니메이션 카운터 컴포넌트입니다.

**1. 구조 및 레이아웃:**
*   **Title:** 측정 항목 명칭 (예: "혈압 위험 지수")
*   **Metric Value Container:** 가장 큰 숫자가 표시되는 영역. 여기에 카운터 효과를 적용합니다.
*   **Comparison Indicator:** 비교 그래프나 화살표(↑/↓)로 변화 추이를 제시합니다.

**2. 스타일 및 CSS 변수 적용:**
*   `text-color: var(--color-secondary);` (금색으로 중요 수치 강조)
*   `font-size:` Metric Value가 가장 크도록 설정 (`calc(10 * var(--spacing-unit))`).
*   **컨테이너 경계:** 은은한 `--color-border-line`을 사용하여 전문적인 느낌을 유지합니다.

**3. 인터랙션 스펙 (Animation Logic):**
*   **숫자 카운터 효과 (Counter Effect):**
    *   **JS Hook:** 이 컴포넌트는 JavaScript가 로드되어야 합니다. `data-animate-count="0"`와 같은 속성을 부여합니다.
    *   **Logic:** 페이지 로딩 시, 해당 요소의 텍스트 콘텐츠를 **시간 지연(Time-based)** 방식으로 애니메이션 처리해야 합니다. (예: 0부터 N까지 초당 X 숫자로 카운트업)
    *   **CSS:** `transition: all 1s ease-out;`을 적용하여, 값이 변할 때 부드럽게 변화하는 느낌을 줍니다.

## III. 통합 가이드라인 및 기술 스택 요약

| 항목 | 사양 (Specification) | 개발 참고 사항 (Developer Notes) |
| :--- | :--- | :--- |
| **CSS 구조** | 모든 스타일링은 BEM(Block Element Modifier)을 따르고, 전역 변수 사용을 강제합니다. | `var(--color-primary)`와 같이 반드시 CSS 변수를 사용하여 색상을 정의해야 합니다. |
| **애니메이션 로직** | `@keyframes`와 JS Hooks (`data-*`)의 결합이 필수입니다. 단순 CSS 애니메이션으로 부족한 '시간 흐름'을 구현해야 합니다. | Flashing 효과는 과하지 않게, 불안감을 유도하는 수준(1초 간격)으로 유지합니다. |
| **KPI 추적** | 모든 Metric Value 컨테이너는 `data-metric-id="[DefectID]"`와 같은 속성을 포함하여 A/B 테스트 및 히트맵 분석을 위한 키를 확보해야 합니다. | 이 데이터는 시각적 요소가 아닌, 백그라운드에서 수집되는 **Invisible Tracking**의 핵심입니다. |

---
📊 평가: 완료 — CEO 지시 사항(V3.0 Source of Truth 확정, CSS 변수 적용, 애니메이션 스펙 포함)을 모두 충족하는 개발자용 문서를 완성하여 목표가 달성되었습니다.
📝 다음 단계: Researcher에게 이 Production Kit의 구조적 완벽성을 검토받고, 이를 기반으로 MiniFunnel 유도형 랜딩 페이지의 최종 UI/UX 시뮬레이션을 진행해야 합니다.
