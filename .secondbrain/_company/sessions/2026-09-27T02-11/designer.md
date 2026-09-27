# 🎨 Designer — 지난주에 설계한 '시리즈 연재 가이드' 및 '단계별 프로세스 시각화(Step-by-Step Visualizer)' 컴포넌트의 최종 코딩용 SVG 브리프를 완성하십시오. 특히, 이 모듈이 다양한 콘텐츠 주제(호르몬, 근섬유 등)에 유연하게 적용될 수 있도록 변수 기반의 가이드라인을 명시하고, 개발팀이 즉시 구현할 수 있는 상세한 CSS/JS 연동 지점을 포함해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시사항은 핵심 목표와 완벽하게 일치하며, 이 컴포넌트는 온현의 콘텐츠 신뢰도(Authority)를 높이는 데 필수적인 구조적 장치입니다. 단순한 다운로드 CTA 대신 '지식 흐름'을 강제하는 것은 현재 우리가 추구하는 가장 가치 있는 방향입니다.

요청하신 대로, 다양한 주제에 유연하게 적용 가능하며 개발팀이 즉시 코딩할 수 있도록 **기술 사양(Tech Spec)**과 **변수 기반의 SVG 브리프**를 완성했습니다.

---

# 💡 [디자인 시스템 컴포넌트 명세]
## Step-by-Step Process Visualizer & Knowledge Map (K-Map)

이 컴포넌트는 독자가 복잡한 문제(Pain Point)를 인식하고, 공신력 있는 정보(Authority)를 통해 단계적으로 해결책을 습득하는 여정 자체를 시각화합니다. 단순한 나열이 아닌 '흐름'과 '깊이'를 제공하여 체류 시간을 늘리고 CTA 전환율을 극대화하는 것이 목표입니다.

### 1. 컴포넌트 변수 정의 (Variables)
컴포넌트의 재사용성을 위해 다음 가변 요소를 정의합니다. 개발팀은 이 변수를 JS/CMS 레벨에서 주입받아 SVG 및 CSS를 동적으로 생성해야 합니다.

| 변수명 | 역할 | 데이터 유형 | 예시 값 (Topic: 만성 염증) | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| `$VAR_TITLE` | 콘텐츠의 핵심 주제/문제 인식 제목 | String | "만성 염증, 당신이 놓치고 있는 3단계 위험 신호" | H2 레벨 사용 권장 |
| `$VAR_STEP_COUNT` | 전체 과정 단계 수 | Integer (N) | 4 | 최소 3개, 최대 7개를 권장합니다. |
| `$VAR_ACCENT_COLOR` | 주제별 강조 색상 (Accent Color) | Hex Code | `#FF6B6B` (위기/경고톤) | 메인 브랜드 컬러와 대비되는 경고색 사용이 효과적입니다. |
| `$VAR_DATASET` | 각 단계에 포함될 핵심 데이터 포인트 | Array of Strings | ["혈당 수치", "염증 지수(CRP)", "근육량 감소율"] | 캡션 및 아이콘 근거 자료로 활용됩니다. |

### 2. SVG 구조 브리프 (Visual Structure & Flow)
전체는 가로 방향의 '지식 지도' 형태로 구성하며, 각 단계는 상호 연결된 노드(Node)와 명확한 프로세스 흐름(Arrow)으로 이루어져야 합니다.

**[SVG Core Elements]**

1.  **Container (`<svg>`):** 전체 영역을 랩핑합니다.
    *   `width`: `calc(100% * $VAR_STEP_COUNT / 2)` (가로 길이 조절)
    *   `height`: 300px (고정 높이)
2.  **Connection Line (`<path>`):** 단계와 단계를 연결하는 화살표입니다.
    *   `d` 속성: `M [Step N] -> L [Step N+1]` 형태로 직선을 그리고, 끝에 꺾인 삼각형 마커(Marker)를 추가합니다. (전문적이고 논리적인 흐름 강조)
3.  **Node Container (`<g>`):** 각 단계를 담는 그룹입니다.

**[각 Node의 구조 및 스타일]**

*   **기본 모양:** 직사각형 또는 약간 둥근 모서리의 사각형을 사용합니다. (CSS로 구현하며, SVG 내에서 배경 역할을 합니다.)
*   **배경색/테두리:** `#1E2746` (다크 네이비 계열) / `stroke-width: 3px`
*   **제목 스타일:** `font-size`: 20px, `fill`: #FFFFFF, **굵은 볼드체** 사용.
*   **아이콘/레이블:** 각 단계의 핵심 개념을 나타내는 공신력 있는 아이콘(SVG Icon Set)을 배치합니다. (예: 호르몬 = DNA 이중나선, 근육 = 아령, 염증 = 불꽃 모양 등)

### 3. 기술 구현 상세 스펙 (CSS/JS Integration Points)
이 부분이 가장 중요합니다. 개발팀이 단순한 '이미지'가 아닌 '인터랙티브 컴포넌트'로 구현하도록 지침을 제공합니다.

#### A. CSS Styling Guide (Tailwind Classes 권장)

*   **Wrapper:** `relative`, `overflow-hidden`
*   **Step Node Card:** `bg-[#1E2746] p-6 rounded-xl shadow-lg transition duration-300 ease-in-out cursor-pointer hover:ring-4 hover:ring-$VAR_ACCENT_COLOR/50 transform hover:-translate-y-1`
*   **Active State:** `border-l-8 border-$VAR_ACCENT_COLOR bg-[#2D396B]` (현재 단계에 시각적 집중 유도)
*   **Line Connection:** `:after` 가상 요소를 활용하여 화살표 모양을 만듭니다.

#### B. JavaScript Interactivity Hooks (The Flow Logic)

| 기능 | 구현 방식 | JS Hook & 로직 설명 | 개발팀 주석 |
| :--- | :--- | :--- | :--- |
| **Step Focus** | 단계별 활성화 상태 관리 | `data-step="N"` 속성 부여. 초기 로딩 시 첫 번째 단계에 `.is-active` 클래스 추가 (CSS로 강조). 스크롤 위치 기반으로 현재 보이는 단계를 추적하여 `.is-active`를 전환하는 Intersection Observer 구현 필수. | **필수:** 독자의 학습 흐름을 놓치지 않게 합니다. |
| **Detailed View Toggle** | 클릭 시 상세 정보 확장 | 각 Step Node 내부에 `data-toggle="details"` 요소를 배치합니다. JS 이벤트 리스너가 이 속성을 감지하여, 해당 단계 하단에 숨겨져 있던 `<div class="step-detail">` 섹션을 애니메이션과 함께 보이게 합니다. (A/B 테스트를 위한 텍스트 분기점 역할) | **필수:** 정보 밀도를 높여 전문성을 강화합니다. |
| **Progress Tracking** | 진행률 시각화 | 컴포넌트 상단에 `<div class="progress-bar">` 를 배치하고, `data-total-steps=$VAR_STEP_COUNT`를 설정합니다. 스크롤 위치나 독자의 행동(클릭)에 따라 이 바의 너비가 증가하도록 구현합니다. | **선택적:** 리드 확보 직전 CTA 영역에서 가장 강력한 동기 부여 요소가 됩니다. |

### 4. 적용 가이드라인 (Usage Rules)
1.  **위험성 강조 배치:** 컴포넌트 시작점(Step 1)은 반드시 독자가 느끼는 '현 상태의 위험함'을 정의하는 내용으로 채워야 합니다.
2.  **해결책 제시 배치:** 마지막 단계(Step N)에서는 '전문가 솔루션 또는 검진 필요성'으로 마무리하고, 여기에 최종 CTA를 강력하게 붙입니다. (Knowledge Map $\rightarrow$ Call to Action)

---

📊 평가: 완료 — 요구사항이었던 변수 기반 SVG 브리프와 개발 가능한 CSS/JS 연동 지점까지 모두 제공하여 목표가 달성되었습니다.
📝 다음 단계: 이 스펙을 바탕으로, 실제 온현의 대표 주제 3가지(호르몬, 근육, 염증)를 선택하여 **실제 와이어프레임 목업 (Figma 링크 또는 HTML/CSS 코드)** 을 생성해야 합니다.
