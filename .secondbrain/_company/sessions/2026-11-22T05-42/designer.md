# 🎨 Designer — 개발자가 즉시 코딩에 착수할 수 있도록, 'Defect ID 위협 보고서' V3.0 Production Kit 문서를 최종적으로 완성해주세요. 특히 CSS 변수 정의, 인터랙티브 경고 바(Critical Alert UI)의 컴포넌트별 스펙, 그리고 모든 KPI 추적 요소(Hidden Form Field 등)를 포함한 상세 기술 사양을 최우선으로 문서화해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시에 따라, 'Defect ID 위협 보고서' V3.0 Production Kit 문서를 최종 개발 사양으로 완성하고 업데이트하겠습니다. 이 문서는 단순한 디자인 브리프가 아니라, 개발자가 즉시 코딩할 수 있도록 CSS 변수 정의, 컴포넌트 스펙, 그리고 비즈니스 로직(KPI 추적)까지 포함하는 완벽한 'Source of Truth' 역할을 할 것입니다.

최근 생성된 파일 경로를 사용하여 내용을 덮어쓰기 하겠습니다.

<edit_file path="c:\Data\Project\connect-ai\assets\design_system\DefectID_Production_Kit_V3.md">
# Defect ID 위협 보고서 (Critical Alert System) Production Kit V3.0 - Final Specification
***(For Immediate Development Implementation Only)***

## 🚨 I. Global Design Tokens & CSS Variables Definition

모든 컴포넌트와 스타일링은 다음 CSS 변수를 기반으로 정의되어야 합니다. 이 변수들을 통해 다크 모드 환경에서도 일관된 전문성을 유지합니다.

| Token | Variable Name | Value (Hex/Unit) | Description |
| :--- | :--- | :--- | :--- |
| **Primary Color** | `--color-primary` | `#FF5722` (Deep Orange/Amber) | 핵심 경고, CTA 버튼 배경색. '주의'를 상징하는 주조색. |
| **Secondary Color** | `--color-secondary` | `#00BCD4` (Cyan Blue) | 데이터 시각화 그래프의 강조선 또는 부가 정보 영역. 전문성 부여. |
| **Background** | `--color-bg-dark` | `#121212` | 메인 배경색. 깊은 밤하늘 같은 무광 블랙 계열. |
| **Surface/Card** | `--color-surface` | `#1E1E1E` | 카드, 패널 등 내용물이 들어가는 영역의 기본 색상. |
| **Text (Primary)** | `--color-text-primary` | `#ECEFF1` | 본문 텍스트 및 제목. 높은 가독성을 위한 밝은 회색조. |
| **Warning/Danger** | `--color-alert-danger` | `#B71C1C` | 심각한 결함(Defect) 경고 표시 색상 (Critical). |
| **Success/Safe** | `--color-alert-safe` | `#4CAF50` | 정상 상태 또는 개선된 솔루션 제시 시 사용. |
| **Font Family** | `--font-family-main` | 'Roboto', sans-serif; | 본문 및 데이터 텍스트 (가독성 최우선). |
| **Font Family (Headline)**| `--font-family-headline` | 'Oswald', Impact, sans-serif; | 제목 및 경고 메시지. 시각적 위압감/전문성 강화. |

## 📐 II. Core Component Specifications

### A. Critical Alert UI Module (`<alert-box>`)
이 컴포넌트는 콘텐츠의 핵심 흐름을 끊고 가장 먼저 사용자의 주의를 끌어야 합니다.

*   **목표:** 시각적 위기감 전달 및 정보 계층 구조 확립.
*   **구조:** `[위협 레벨 바] - [Defect ID 코드] - [핵심 경고 문구]` 3단 구조 필수.
*   **스펙:**
    *   **크기:** 전체 너비 100%, 높이 최소 80px.
    *   **배경:** `--color-surface`에 미세한 그라데이션 (Gradient: `#252525` $\rightarrow$ `#1E1E1E`).
    *   **Critical Alert Bar (`<div class="alert-bar">`):**
        *   높이: 8px. 배경색: `--color-alert-danger`.
        *   애니메이션: 페이지 로드 시 `scaleY(0)`에서 `scaleY(1)`로 부드럽게 등장 (CSS Transition 필수).
    *   **Defect ID Display:** 고정 폭, 특수 폰트 (`monospace`) 사용. 예: `[DEFECT-ID: C4B2-MOBI-L3]`

### B. Data Comparison Card Module (`<compare-card>`)
Before (현상 유지 위험)와 After (솔루션 제시 가치)를 극명하게 대비시키는 카드형 구조입니다.

*   **목표:** 정량적 수치를 통한 감정적 충격(Fear of Loss) 유발.
*   **구조:** 좌측 섹션 (Before/Risk), 우측 섹션 (After/Solution). 중앙에 비교 지표 표시.
*   **스펙:**
    *   **레이아웃:** Flexbox 2-column grid (50% / 50%).
    *   **Before Side:** 배경은 어두운 그레이(`~#1A1A1A`), 경고 아이콘(🚨) 필수. 수치 옆에 '위험 지수: High' 태그 배치.
    *   **After Side:** 배경은 미세하게 밝은 톤(`~#282828`), 성공/솔루션 아이콘(✅) 필수. **이곳의 숫자에 강조 색상 (`--color-primary`)을 사용.**

### C. MiniFunnel CTA Module (`<cta-module>`)
단순한 버튼 클릭 유도가 아닌, 정보 교환을 약속하는 '가치 기반'의 전환 요소입니다.

*   **목표:** 리드 확보(Lead Capture) 및 다음 단계로의 자연스러운 이동 유도.
*   **스펙:**
    *   **배경:** 전체 섹션에 걸쳐 `--color-primary` 색상의 그라디언트 오버레이 적용 (시각적 집중).
    *   **CTA Button:** 크기 160px x 55px, 배경색: `#FFD700` (골드톤), `:hover` 시 `transform: scale(1.03)`.
    *   **Form Integration:** 버튼 클릭 시 즉시 스크롤을 아래의 **'신뢰도 확보 폼'**으로 이동시키고, 해당 섹션에 Focus를 강제한다.

## ⚙️ III. Technical Specifications & Tracking Logic (Developer Guide)

### A. CSS Implementation Details
1.  **Responsiveness:** 모든 컴포넌트는 `rem` 단위 및 Grid/Flexbox 기반의 반응형 설계를 준수해야 합니다. (Mobile First 접근 필수).
2.  **Interactivity:** 마우스 오버(Hover), 포커스(Focus) 상태에 대한 명확한 `:before`, `:after` 가상 요소를 정의하고 애니메이션 효과를 부여합니다.

### B. KPI 추적 시스템 설계 (Invisible Tracking)** - *가장 중요*
모든 트래픽 유도와 리드 확보는 사용자가 인지하지 못하는 방식으로 이루어져야 합니다.

1.  **Hidden Form Fields:** 모든 CTA 모듈에 다음의 숨겨진 필드를 포함합니다. (JavaScript를 통해 전송되어야 함)
    *   `hidden_source`: `[광고 채널/게시물 ID]` (예: `instagram-reel-20261205`)
    *   `hidden_user_intent`: `Defect_ID_Check` (사용자가 보고서 진단에 관심 있음을 추적)
    *   `hidden_scroll_depth`: 현재 페이지 스크롤 비율을 계산하여 전송.

2.  **Event Listeners:**
    *   **Scroll Depth Trigger:** 사용자가 페이지의 75% 지점에 도달했을 때, 자동적으로 **'미니 Funnel 유도 경고 메시지(Subtle Alert)'**를 트리거합니다. (팝업 아님. 본문 콘텐츠 내에 자연스럽게 등장)
    *   **Exit Intent Logic:** 사용자가 페이지를 떠나려고 할 때 (마우스 커서가 상단 탭을 향할 때), 최종 경고 메시지(Last Chance CTA)와 함께 이메일 주소 입력 필드를 강제 노출합니다.

## ✨ IV. Summary Checklist for Development

*   [ ] **Design System:** 모든 색상, 간격은 `--color-*` 변수를 사용했는가?
*   [ ] **UX Flow:** 위기감 $\rightarrow$ 데이터 충격 $\rightarrow$ 솔루션 제시 $\rightarrow$ 리드 확보의 흐름이 자연스러운가?
*   [ ] **Tracking:** 모든 CTA 클릭 및 스크롤 이벤트에 Hidden KPI 필드가 통합되었는가?

</edit_file>

---
📊 평가: 완료 — CEO 지시사항(V3.0 최종 완성, CSS 변수 정의, 인터랙티브/KPI 추적 요소 문서화)을 모두 포함하여 개발자가 바로 코딩할 수 있는 형태의 Production Kit 문서를 완성했습니다.
📝 다음 단계: 개발 에이전트가 이 `DefectID_Production_Kit_V3.md` 파일을 기반으로 실제 UI 컴포넌트를 구현하고, 트래킹 시스템을 연동하는 테스트를 진행해야 합니다.
