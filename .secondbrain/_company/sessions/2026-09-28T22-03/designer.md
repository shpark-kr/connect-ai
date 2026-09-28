# 🎨 Designer — Developer가 제공할 E2E 테스트 결과(버그, 성공 지점 등)를 전제로 하여, Deep Crimson Red $ightarrow$ Soft Gold 전환 애니메이션을 적용한 Funnel의 최종 UI 목업을 제작합니다. 특히 사용자 흐름상 가장 중요한 3개의 CTA 포인트에 대한 시각적/인터랙티브 UX 검토가 필요합니다.

🎨 Designer: 작업 시작합니다. 📐

CEO님의 지시와 개발팀의 최신 테스트 결과(`NameResolutionError`)를 모두 고려했습니다. 현재 Funnel 자체에 네트워크 레벨의 치명적인 에러가 발생했기 때문에, 실시간 Mockup 제작은 불가능합니다. 이 문제를 해결하기 위해서는 먼저 Developer에게 DNS/네트워크 환경 개선이 필요하며, 제가 디자인적으로 완성할 수 있는 것은 '최종 인터랙티브 UX 시퀀스 블루프린트'입니다.

따라서 Funnel의 3가지 핵심 CTA 포인트를 중심으로, 현재까지의 모든 스펙(Deep Crimson Red $\to$ Soft Gold)을 종합하여, 개발자가 바로 Figma 컴포넌트로 구현할 수 있는 **최종 UI/UX 상세 디자인 명세서**를 제작하겠습니다. 이 문서는 단순히 이미지를 나열하는 것이 아니라, 상태 변화(State Change), 애니메이션 로직(Keyframe Logic), 그리고 사용자의 인지 흐름(User Flow)을 좌표 및 코드 레벨로 지정해야 합니다.

---

### 🚨 Critical Dependency Alert: Funnel 접근성 문제
Developer가 실행한 테스트 결과(`NameResolutionError`)는 현재 **온현 사이트의 도메인 이름 해석 자체에 문제가 있다**는 것을 의미합니다 (DNS Failure). 이 에러가 해결되지 않으면, 어떤 UI Mockup도 실제 환경에서 검증될 수 없습니다.

*   **[Action Required]**: 개발팀에게 네트워크 인프라 점검을 최우선으로 요청해야 합니다.
*   **[Designer's Plan]**: 당장 디자인을 멈출 수는 없으므로, Funnel이 정상화되었을 때 바로 적용할 수 있는 **최종 시각적 설계 원본(Source of Truth)**을 만듭니다.

### 🛠️ 산출물: Funnel 최종 인터랙티브 UX 시퀀스 블루프린트 (V1.0)
Funnel의 핵심 CTA 전환 로직과 비주얼 요소를 통합하여, 개발자가 코딩할 수 있는 수준의 상세 컴포넌트 명세서를 작성합니다. 이 문서에는 다음 3가지 필수 요소가 포함됩니다:

1.  **Deep Crimson Red 경고 UI (위기 조성):** 애니메이션 타이밍 및 시각적 강도 정의.
2.  **Soft Gold 전환 배경/카드 (해결책 제시):** z-index, 광원 효과 등 미묘한 상호작용 정의.
3.  **CTA 버튼 3종의 상태 변화:** Idle $\to$ Hover $\to$ Click(Loading) 시의 정확한 색상 코드와 크기 변형 명세.

<create_file path="c:\Data\Project\connect-ai\assets\funnel_ui\Funnel_Final_UX_Blueprint_V1.0.md"># 🎨 Funnel 최종 인터랙티브 UX 시퀀스 블루프린트 (v1.0)
## 🎯 목표: Deep Crimson Red $\to$ Soft Gold 전환 로직을 포함한 최종 UI 컴포넌트 명세

### ⚙️ 1. 전역 스타일 가이드라인 (Global Style Guide)
*   **Primary Color (Danger/Warning):** Deep Crimson Red (`#A82E3C`) - 경고, 위기 상황 사용.
    *   *Usage:* 배경 오버레이, Warning Border, 타이포그래피 강조.
    *   *Animation State:* Keyframe 0% opacity(Normal) $\to$ 100% opacity (Max Alert).
*   **Secondary Color (Solution/Hope):** Soft Gold (`#F5E6C7`) - 해결책, 전환 지점 사용.
    *   *Usage:* 배경 패널, 성공 메시지, CTA 활성화 영역.
    *   *Animation State:* Subtle glow effect (box-shadow: 0 0 20px rgba(245, 230, 199, 0.6)).
*   **Typography:** Noto Sans KR (Pre-defined hierarchy 적용).

### ✨ 2. 인터랙티브 시퀀스 상세 정의 (The Core Flow)
#### A. 위기 조성 단계 (Deep Crimson Red Alert)
| 요소 | 스펙 / 로직 | 애니메이션 타이밍 | 비고 |
| :--- | :--- | :--- | :--- |
| **전환 오버레이** | `#A82E3C` 투명도 70%의 반투명 배경. | `opacity: 0` $\to$ `1` (Duration: 500ms, Ease: Cubic-bezier(0.25, 1, 0.5, 1)). | Deep Crimson Red 경고 UI가 전체 화면을 빠르게 감싸는 느낌. |
| **경고 메시지** | "🚨 [생체 지표] 위험 임계치 도달! 즉각적인 개선이 필요합니다." | Fade-in (Duration: 300ms). | 타이포그래피 크기(H2)와 볼드 처리 강조. |
| **Mini-App Funnel CTA** | Deep Crimson Red 배경의 버튼으로 비활성화 상태 유지. | `transform: scale(1)` $\to$ `scale(0.98)` (Microshake effect). | 사용자에게 '지금은 안 된다'는 긴장감 부여. |

#### B. 해결책 제시 단계 (Soft Gold Transition)
| 요소 | 스펙 / 로직 | 애니메이션 타이밍 | 비고 |
| :--- | :--- | :--- | :--- |
| **전환 배경** | Soft Gold 색상으로의 부드러운 전환. | `opacity: 1` $\to$ `0` (Red) $\to$ `1` (Gold). (Duration: 800ms, Ease: ExpoOut). | 시각적 안정감을 부여하며 '새로운 시작' 느낌 강조. |
| **핵심 솔루션 카드** | Soft Gold 배경의 투명 글래스모피즘 카드(BackdropFilter) 배치. | `translateY(50px)` $\to$ `translateY(0)` (Duration: 600ms, Staggered). | 주요 해결책 정보를 담는 메인 콘텐츠 영역. |
| **Mini-App Funnel CTA** | Soft Gold 배경의 Primary Button으로 활성화. | Fade-in (Duration: 400ms). | '지금 행동할 수 있다'는 희망과 기회를 제시. |

### ✨ 3. 핵심 CTA 컴포넌트 명세 (The Three Pillars)
Funnel 내 사용자 여정에서 가장 중요한 세 가지 액션 버튼에 대한 상세 스펙입니다.

| CTA 목적 | 기본 상태 (Idle) | 호버 상태 (Hover) | 클릭/로딩 상태 (Active) | 비고 / 로직 |
| :--- | :--- | :--- | :--- | :--- |
| **CTA 1: [진단 시작]** | Soft Gold 배경, Deep Crimson Red 텍스트. `padding: 16px`. | 배경 색상 증가 (`#e8d7b2`), 그림자 강화 (Shadow). | 버튼 비활성화 및 로딩 스피너 표시. | *Primary Action.* 가장 크고 눈에 띄게 배치. |
| **CTA 2: [솔루션 상세 보기]** | Soft Gold 배경, Deep Crimson Red 텍스트. `padding: 10px`. | 배경색 변경 없이 미세한 좌우 이동(`translateX(2px)`). | 버튼 비활성화 및 로딩 스피너 표시. | *Secondary Action.* 보조적인 정보 탐색 경로. |
| **CTA 3: [전문가 상담 신청]** | Soft Gold 배경, Deep Crimson Red 텍스트. `padding: 10px`. | 테두리 강조 (Border-solid `#a82e3c`). | 버튼 비활성화 및 로딩 스피너 표시. | *Tertiary Action.* 궁극적인 수익 전환 지점(Lead Gen). |

---
📊 평가: 진행중 — Funnel의 핵심 UI/UX 흐름을 코드 레벨에서 명세화했습니다. 이는 Mockup 제작에 필요한 필수 '설계도' 역할을 합니다. 하지만, 이 설계도를 실제 코드로 옮기거나 최종 비주얼로 검증하기 위해서는 Developer가 네트워크 문제를 반드시 해결해야 다음 단계로 진행할 수 있습니다.
📝 다음 단계: 개발팀에게 Funnel의 DNS/네트워크 환경 점검을 최우선으로 요청하고, 그 결과(Funnel 접속 가능 여부)를 기다립니다. 만약 문제가 지속된다면, 대신 '오프라인 모드'에 대비한 UI 백업 디자인 작업을 진행하겠습니다.
