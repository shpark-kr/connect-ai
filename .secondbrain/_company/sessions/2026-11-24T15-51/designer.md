# 🎨 Designer — 개발자에게 전달할 최종 컴포넌트 API 명세서를 작성해 주세요. 특히 'Gap Score' 표시 위젯과 '#D82B3A' Critical Alert 팝업이 어떤 상태(State)에서, 어느 정도의 애니메이션(Motion/Timing Spec), 그리고 어떤 데이터 입력을 받아야 하는지 (Prop 정의)를 상세하게 정리해야 합니다. 이 명세서는 순수한 디자인 가이드가 아닌 '개발 지침서' 형태로 구체화되어야 합니다.

🎨 Designer: 작업 시작합니다.

사용자의 지시와 모든 시스템 컨텍스트(개인 목표, 공동 목표, 최근 의사결정 로그)를 종합했을 때, 현재 프로젝트의 가장 핵심적인 병목 구간은 **'디자인 명세서 $\rightarrow$ 개발 구현'**으로 넘어가는 단계입니다. 이전 세션에서 `funnel_qa_v3.md`와 `Interaction_Flow_Spec_v1.md`라는 훌륭한 초안을 만들었지만, 이는 '기획자 관점의 상세 지침서'에 가깝습니다.

개발자가 코드를 작성할 수 있도록 **"컴포넌트 API 명세(Component API Specification)"** 형태로 전환하는 것이 현재 가장 시급하고 높은 가치를 가지는 단일 작업입니다. 이 문서는 앞으로 Funnel 개발 과정에서 발생하는 모든 디자인/UX 논쟁의 최종 결정권자 역할을 수행할 것입니다.

따라서, 저는 **개발팀을 위한 최종 컴포넌트 API 명세서**를 작성하겠습니다.

---

## ⚙️ Component API Specification: 핵심 위젯 정의
(대상: Developer)

본 문서는 Funnel Flow에서 사용되는 두 가지 핵심 상호작용 요소에 대한 기술적 사양(Technical Spec)을 정의합니다. 디자인 가이드가 아닌, 개발자가 바로 구현할 수 있는 컴포넌트 Props 및 Behavior 명세입니다.

### 1. `GapScoreDisplay` 위젯 (핵심 위험 지표 시각화)

사용자의 '미조치 손실 공포'를 가장 강력하게 자극하는 핵심 요소입니다. 단순한 숫자가 아닌, **시간 경과에 따른 변화와 위험 레벨**을 전달해야 합니다.

| 속성 | 타입 | 설명 | 필수 여부 |
| :--- | :--- | :--- | :--- |
| `score` | Number (Integer) | 현재의 Gap Score 값입니다. (-100 ~ 0). | O |
| `initialScore` | Number (Integer) | 사용자가 진단 Funnel에 처음 진입했을 때 측정된 기준 점수. (손실 비교용). | O |
| `isTrackingActive` | Boolean | 현재 스크롤/페이지 이동 등 사용자 액션이 일어나고 있는지 여부. (애니메이션 제어용) | O |
| `title` | String | 위젯 상단에 표시되는 설명 제목 (예: '미조치 위험 지표'). | O |

**[State & Behavior Spec]**

| State/Trigger | Condition (조건) | Visual Change (시각 변화) | Animation Spec (개발 지침) |
| :--- | :--- | :--- | :--- |
| **Normal** | `score > -20` | 배경색: `#FFFFFF`. 폰트 색상: `#333333`. 점수 그래프: 완만하게 하락 추세. | 기본 라인 애니메이션 (Smooth Line Interpolation). 업데이트 시 지연 시간(Easing)을 50ms 적용하여 부드럽게 수치 변화. |
| **Warning** | `-20 >= score > -60` | 배경색: `#FFF8E1` (은은한 노란빛). 점수 그래프: 가파른 하락세 시작. 경고 아이콘(⚠️) 활성화. | `score`가 임계값(-20)을 넘어설 때, 2초 동안 Background Color Transition (Fade-in/Out) 발생. |
| **Critical** | `score <= -60` | 배경색: `#FADBD8` (옅은 빨간빛). 점수 그래프: 급격한 하락(Cliff Edge) 표현. 위험 아이콘(🚨) 최대 강조. | **[핵심]**: `score`가 임계값(-60)에 도달하는 순간, 1초 동안 Background Flicker Effect (빠른 깜빡임 애니메이션) 적용 필수. 수치 변화 시 *Pop* 효과와 함께 점프 애니메이션을 사용한다. |

---

### 2. Critical Alert Pop-up 컴포넌트 (`<CriticalAlert />`)

시스템 오류나 위험 임계점에 도달했을 때 발생하는, Funnel의 감정적 클라이맥스(Climax)를 담당하는 컴포넌트입니다. **이 컴포넌트는 디자인 가이드가 아닌 '강제적인 시스템 경고'로 인식되어야 합니다.**

| 속성 | 타입 | 설명 | 필수 여부 |
| :--- | :--- | :--- | :--- |
| `isVisible` | Boolean | 팝업 활성화/비활성화 상태. (Funnel 로직에 의해 제어됨) | O |
| `severityLevel` | Enum (`LOW`, `MEDIUM`, `HIGH`) | 경고의 심각도 레벨. (High: `#D82B3A` 사용). | O |
| `messageBody` | String | 사용자에게 전달할 구체적이고 공포감을 유발하는 문구. | O |
| `actionPrompt` | React Component/String | 경고를 해결하거나 다음 단계로 나아가게 하는 CTA (예: '전문가 진단 받기'). | O |

**[State & Behavior Spec]**

| State/Trigger | Condition (조건) | Visual Change (시각 변화) | Animation Spec (개발 지침) |
| :--- | :--- | :--- | :--- |
| **Hidden** | `isVisible === false` | 컴포넌트가 DOM에서 완전히 숨겨져야 합니다. | 없음. |
| **Triggering** | `isVisible`이 `false` $\rightarrow$ `true`로 변경될 때 (즉, 위험 임계점 도달 시) | 팝업 전체가 화면 중앙에 강력하게 나타남. 배경을 가리고 모든 요소를 압도해야 함. | **[필수]**: `0ms`의 즉각적인 등장 애니메이션 (Instant Appearance). 동시에 전체 페이지 배경이 `#D82B3A` 색상으로 미세하게 깜빡이는(Flash) 효과를 1초간 적용하여 긴급성을 극대화합니다. |
| **Active** | 활성화 상태 유지 중일 때 | `severityLevel`에 따라 경고색이 유지되며, 주변 UI 요소는 흐릿해지거나 어둡게 처리되어야 함 (Depth/Focus Effect). | 팝업 자체는 고정(Fixed Position)되고, 미세한 진동 애니메이션(Subtle Pulse Animation)을 지속적으로 주어 주의를 분산시키지 않도록 합니다. |

---
**[총평 및 다음 단계]**

이 명세서가 완료됨으로써, Funnel의 핵심 인터랙션 요소에 대한 디자인적 논쟁은 종료되며 개발 착수 준비가 끝납니다. 이제 남은 것은 이 API 사양을 기반으로 **실제 프로토타입을 구축하고 A/B 테스트를 실행할 데이터 아키텍처**를 완성하는 것입니다.

📊 평가: 완료 — Funnel의 핵심 컴포넌트 사용법에 대한 '개발 지침서' 작성이 목표로 제시된 모든 요구사항(State, Motion Spec, Prop 정의)을 포함하여 성공적으로 마무리되었습니다.
📝 다음 단계: Developer에게 이 API 명세서를 전달하고, **`funnel_qa_v3.md`**의 데이터 로직과 연결되는 플래그 기반 추적 시스템(Tracking Layer) 구축에 착수하도록 지시해야 합니다.
