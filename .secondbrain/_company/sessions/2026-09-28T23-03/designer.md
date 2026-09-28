# 🎨 Designer — Mini-App Funnel의 '위기 $\to$ 해결' 전환 프로토콜 기반 최종 UI 목업(Mockup)을 제작해 주세요. 특히 Instagram 로드맵에 사용된 모든 CTA 지점에 대한 시각적/인터랙티브 UX 검토가 필요하며, Deep Crimson Red 경고와 Soft Gold 신뢰 증진 애니메이션의 세부적인 타이밍과 배치를 반드시 포함해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시에 따라 Mini-App Funnel의 '위기 $\to$ 해결' 프로토콜 기반 최종 UI Mockup을 완성하는 것을 넘어, **개발자가 즉시 코딩에 착수할 수 있는 수준의 상호작용(Interaction) 중심의 컴포넌트 명세서와 플로우 차트를 제작**하겠습니다.

단순한 시각적 목업은 이미 진행된 단계이므로, 이번 작업은 **'사용자 경험 흐름을 정의하는 기술 사양서 (Technical Specification)'**를 만드는 데 집중합니다. 특히 Instagram 로드맵에 사용되는 모든 CTA 지점의 심리적 연결 고리(Deep Crimson Red 경고 $\rightarrow$ Soft Gold 신뢰)가 완벽히 구현되도록 설계하겠습니다.

---

### 🛠️ 산출물: Funnel Mini-App 최종 상호작용 컴포넌트 명세서 (V3.0)

이 문서는 개발자에게 전달될 핵심 가이드라인이며, 모든 애니메이션 타이밍과 상태 변화 로직을 정의합니다.

#### 1. 기본 컬러 및 타입 시스템 재확인
| 요소 | 이름 | HEX 코드 | 용도/의미 | 적용 범위 |
| :--- | :--- | :--- | :--- | :--- |
| **Crisis** | Deep Crimson Red (DCR) | `#9E001A` | 경고, 위협, 위험 감지. '지금 당장 문제 발생' 시각화. | HOMA-IR 수치 초과, 핵심 지표 이상 감지 등 모든 Warning UI 배경/텍스트. |
| **Solution** | Soft Gold (SG) | `#C5A347` | 신뢰, 해결책 제시, 전문성. '해결 가능함' 시각화. | Funnel Mini-App의 메인 버튼, 성공 메시지, 전문가 의견 강조. |
| **Base** | Dark Navy (DN) | `#0A192F` | 배경색. 높은 대비를 통한 집중 유도. | 전체 페이지/섹션 배경. |
| **Accent** | Pure White / Light Gray | `#E6EDF3` / `#FFFFFF` | 가독성 최우선. 텍스트 및 카드 내용물. | 본문 컨텐츠, 그래프 라벨 등. |

#### 2. 핵심 컴포넌트 명세 (The Three Pillars)

**A. 경고 배너 컴포넌트 (`[Component: WarningBanner]`)**
*   **표시 조건:** 사용자가 임상 지표(HOMA-IR, hs-CRP 등)를 입력하거나 Funnel 진입 시, 기준치 이탈이 감지될 때 (예: HOMA-IR > 2.5).
*   **디자인/애니메이션:**
    1.  **초기 상태 (Initial):** `Deep Crimson Red` 배경의 점진적 깜빡임(`Animation: flash(0s, 0.5s)`) 효과를 적용하여 시각적 긴급성을 최고조로 끌어올립니다.
    2.  **텍스트:** "🚨 **경고**: 귀하의 지표는 위험 수준입니다. 즉각적인 확인이 필요합니다." (HOMA-IR 수치를 붉은색으로 강조)
    3.  **UX 로직:** 이 배너가 화면 최상단에 고정(Sticky)되어야 하며, 사용자가 스크롤해도 사라지지 않아야 합니다.

**B. 신뢰 증진 패널 컴포넌트 (`[Component: SolutionPanel]`)**
*   **표시 조건:** 경고 배너 노출 직후 (Deep Crimson Red $\rightarrow$ Soft Gold 전환 시점).
*   **디자인/애니메이션:**
    1.  **전환 애니메이션:** DCR 배경이 부드럽게(Ease-in-out, 500ms) `Soft Gold` 색상으로 변색되는 과정이 핵심입니다. (시각적 안도감 유발).
    2.  **콘텐츠 구조:** 전문 용어와 데이터 기반의 해결책을 제시하는 카드 UI가 배치됩니다. (예: "✅ **해결책**: 이 문제를 개선하기 위해, \[Mini-App]에서 맞춤 진단이 필요합니다.")
    3.  **CTA 버튼 (`[Button: CTA_Primary]`):** 가장 눈에 띄게 `Soft Gold` 색상을 사용하며, 마우스를 올리면(Hover) 은은하게 밝아지면서 클릭 가능한 상태임을 직관적으로 알립니다.

**C. 데이터 비교 차트 컴포넌트 (`[Component: DataComparisonChart]`)**
*   **활용처:** 콘텐츠 본문 및 Funnel 진입 전의 흥미 유발 단계.
*   **디자인 원칙:** 항상 A/B 대비 형식 (Before $\leftrightarrow$ After).
    *   **Before (위험):** 어둡고 불안정한 톤 (Dark Gray/Deep Crimson Red)으로 표현된 통계적 결손이나 위험 지점 강조.
    *   **After (기회):** 밝고 명확한 톤 (Soft Gold Gradient / Light Blue Accent)으로 표현된 개선 효과나 얻게 될 이득을 시각화합니다.

#### 3. 핵심 상호작용 플로우 정의 (Developer Guide)

| 단계 (State) | 사용자 행동/트리거 | 애니메이션/UX 변화 (Timing) | 목적 및 역할 |
| :--- | :--- | :--- | :--- |
| **Step 1: 공포 유발** | 콘텐츠 읽기 $\rightarrow$ 지표 확인 | `Deep Crimson Red` 경고 배너가 깜빡임(Flash). (0.0s - 2.5s) | 전문적 위기감 조성 및 주의력 극대화.
| **Step 2: 전환 임계점** | Mini-App Funnel 진입 시도 | DCR 배경 $\rightarrow$ SG 배경으로의 부드러운 색상 변화 (Fade). (2.5s - 4.0s) | 심리적 안도감 및 기대감 조성. **(가장 중요)**
| **Step 3: 해결책 제시** | Funnel 내부 콘텐츠 읽기 | `Soft Gold` 강조 박스가 나타나며, 핵심 솔루션을 구조적으로 전달함. (4.0s - 7.0s) | 문제 인식 $\rightarrow$ 신뢰 구축(Solution).
| **Step 4: 최종 CTA 유도** | 마지막 정보 습득 완료 시점 | `CTA_Primary` 버튼이 은은한 광원 효과와 함께 포커스를 받으며, 클릭을 강력하게 요청함. (7.0s - 9.0s) | 행동 촉발(Conversion).

#### 4. Instagram 로드맵 기반 CTA 매핑 및 검토
Instagram 로드맵에서 사용된 모든 CTA는 결국 **'위험 지표 확인 $\rightarrow$ 전문가 솔루션 탐색 $\rightarrow$ Mini-App 진입'**이라는 동일한 흐름을 가집니다. 따라서 Funnel의 UI/UX는 단일화되어야 합니다.

| Instagram 콘텐츠 주제 | 유도하는 감정적 Pain Point | Funnel Funnel에서의 역할 (CTA 배치) | UX 강조 포인트 |
| :--- | :--- | :--- | :--- |
| **A. HOMA-IR 과부하** | '내 몸의 시스템이 망가지고 있다'는 공학적 위기감. | **Step 1 $\rightarrow$ Step 2 전환 지점 (최우선)**: Funnel 진입 직후 DCR 경고 배너를 통해 직접 노출. | Deep Crimson Red를 가장 강하게 사용하고, 수치 기반의 즉각적인 위험을 강조해야 함.
| **B. 장기요양 사각지대** | '노후 준비가 안 되어 있다'는 재정적 위협감. | **Step 3 (SolutionPanel):** Mini-App에서 필요한 체크리스트/진단 결과를 제시하며, Funnel 진입을 통해 부족한 부분을 보완해야 함을 강조. | Soft Gold 배경의 전문적인 '체크리스트' 이미지를 활용하여 신뢰도를 높여야 함.
| **C. 근력 및 대사 저하** | '나이가 들면서 스스로 통제할 수 없다'는 기능적 위기감. | **Step 4 (Final CTA):** Funnel의 마지막 섹션에서, "생활 습관만으로는 부족하며, 데이터 기반 관리가 필요하다"고 결론지으며 Mini-App을 최종 출구로 제시. | 직접적인 질문("혹시 이러진 않으신가요?")과 함께 강한 동기 부여를 제공해야 함.

---
📊 평가: 완료 — 모든 CTA 지점의 공통 분모인 Funnel 진입 경험을 기술 사양서 형태로 통합하여, 개발에 필요한 구체적 상호작용 로직(Timing, Color State)까지 정의했기 때문에 목표 달성이 가능합니다.
📝 다음 단계: Developer에게 이 명세서를 전달하고, 실제 인터랙티브 프로토타입 구현 및 E2E 테스트를 요청해야 합니다.
