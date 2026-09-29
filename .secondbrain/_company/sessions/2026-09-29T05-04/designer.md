# 🎨 Designer — MiniFunnel Funnel의 'Deep Crimson Red $	o$ Soft Gold' 상태 전환 애니메이션과 UI/UX 인터랙션에 대한 최종 고화질 프로토타입(Figma 또는 유사 툴)을 제작해 주세요. 이 프로토타입은 단순히 시각적 구현을 넘어, 사용자의 마우스 오버(Hover), 클릭(Click) 등 모든 상호작용 지점에서 발생하는 미세한 애니메이션 변화와 트랜지션 효과를 포함해야 합니다. 개발자가 즉시 코드로 변환할 수 있도록 컴포넌트 단위로 분리하여 정의해 주세요.

🎨 Designer: 작업 시작합니다.
제시된 지시는 MiniFunnel Funnel의 가장 핵심적인 상업 논리 전환점(Error $\to$ Solution)을 담고 있으므로, 이 부분을 단순히 애니메이션으로 처리해서는 안 됩니다. **'위기감 해소 과정 자체가 곧 제품/솔루션에 대한 신뢰 구축'**이라는 관점에서 접근해야 합니다.

개발팀이 즉시 활용할 수 있도록 Figma 프로토타입의 구조적 명세와 컴포넌트 레벨의 인터랙티브 가이드를 작성하겠습니다. 실제 파일 형태로 제공하는 대신, 개발자 핸드오프(Hand-off)에 최적화된 '디자인 시스템 스펙 시트'를 완성합니다.

---

## 📁 MiniFunnel Funnel: State Transition Component Guide (v1.0)

### 🎯 목표 및 사용 목적
**목표:** Deep Crimson Red (위기/오류) 상태에서 Soft Gold (해결책/솔루션) 상태로의 전환을 유도하는 고밀도, 컴포넌트 기반 UI/UX 가이드를 제공한다.
**핵심 논리:** 단순한 색상 변경이 아닌, **'문제 인식 $\to$ 시스템 오류 감지 $\to$ 해결 프로세스 개시 $\to$ 신뢰 회복 및 CTA 활성화'**의 4단계 서사적 흐름을 애니메이션으로 구현해야 한다.

### 🎨 브랜드 가이드라인 재확인
| 요소 | 상태 (State) | 색상 코드 (HEX/CSS Var) | 의미론적 역할 |
| :--- | :--- | :--- | :--- |
| **Error** | Deep Crimson Red | `var(--color-danger, #B71C2D)` | 위기 경고, 시스템 오류, 즉각적인 주의 필요. |
| **Recovery** | Soft Gold | `var(--color-success, #FFC107)` | 해결책 제시, 가능성 발견, 행동 유도 (Actionable). |
| **Background** | Neutral/Dark Navy | `var(--bg-primary, #1A2333)` | 전문성과 신뢰성을 유지하는 기반. |

### 🛠️ 컴포넌트 분리 및 기술 사양 (Developer Handoff Ready)

#### 1. Component: `ErrorStateIndicator` (위기 경고 모듈)
*   **역할:** 사용자가 임계치를 초과했을 때, 시스템이 오류 코드를 제시하는 영역.
*   **시각 요소:** 공학적 느낌의 글꼴(Monospace/Geometric Sans), 붉은색 하이라이트 박스.
*   **상호작용 (Interaction):**
    *   **Default:** Deep Crimson Red 배경 + 깜빡임 효과(Pulsing Animation, `animation: pulse 1s infinite;`).
    *   **Hover:** 경고 메시지 주변의 테두리가 미세하게 커지면서 내부 깊이감(Shadow Depth)을 증가시키고, 글자가 잠깐 더 진해짐 (Focus Effect).
    *   **Click:** 없음. 이 컴포넌트는 시스템 상태에 의해 주입되는 정보 표시 영역임.

#### 2. Component: `SolutionPathwayCTA` (솔루션 제시 모듈)
*   **역할:** 오류 감지 후, 해결책(온현의 솔루션/워크북)으로 시선을 전환시키는 버튼 및 설명 블록.
*   **시각 요소:** 부드럽고 따뜻한 골드톤 사용. '개선 가능성'을 강조하는 텍스트 구조.
*   **상호작용 (Interaction):**
    *   **Default:** Soft Gold 배경의 주 CTA 버튼이 화면 하단 중앙에 배치되며, 가장 명확하게 보이는 요소여야 함.
    *   **Hover:** 버튼 색상이 미세하게 밝아지며(Luminosity increase), 입체적인 '눌리는' 느낌(Depth/Shadow change)을 즉시 제공해야 함.
    *   **Click:** 클릭 애니메이션과 함께, Funnel의 다음 페이지(혹은 워크북 다운로드 팝업)로 부드럽게 전환됨 (Transition: Ease-out Quad).

#### 3. Module: `State_Switch_Transition` (핵심 애니메이션 로직)
이 모듈은 Error State와 Solution CTA가 공존하는 영역 전체를 아우르며, 가장 중요한 부분입니다.

| 단계 | 시간 (Duration) | 애니메이션 설명 (Animation Curve/Easing) | 개발 지침 (Technical Directive) |
| :--- | :--- | :--- | :--- |
| **[Start]** | 0ms | `ErrorStateIndicator`가 최대 강도(Deep Crimson Red, Pulse ON)로 활성화됨. | CSS: `opacity: 1; transform: scale(1);` |
| **[Trigger]** | T+500ms (자동 발생) | 시스템이 '개선 가능성' 데이터를 로드하는 가상의 지연 시간/로딩 애니메이션을 삽입. | UI: "데이터 분석 중..." 등의 텍스트와 함께, Error State가 점진적으로 흐려지기 시작해야 함. |
| **[Transition]** | T+500ms $\to$ T+1200ms | **Deep Crimson Red의 색상이 Soft Gold로 서서히 변이(Color Interpolation)하며 밝아짐.** 경고 문구가 추상화되면서 '해결책 탐색'을 의미하는 모호한 기하학적 패턴으로 대체됨. | CSS: `transition: all 700ms cubic-bezier(0.2, 1.5, 0.3, 1);` (Overshoot 효과를 통해 전환의 드라마 강조) |
| **[End]** | T+1200ms | `ErrorStateIndicator`가 완전히 사라지고, 그 자리에 `SolutionPathwayCTA`가 부드럽게 나타남(Fade-in). CTA 버튼이 중심 포커스를 잡음. | CSS: `opacity: 0; transform: translateY(-20px);` (사라짐) $\to$ `opacity: 1; transform: translateY(0);` (나타남) |

### ✅ 최종 요약 및 구현 가이드라인
1.  **레이아웃:** Funnel의 위기감 고조 구간은 **좌측에 Error State를, 우측/하단에 Solution CTA**를 배치하여 시선이 자연스럽게 흐르도록 유도합니다 (F 패턴).
2.  **애니메이션 타이밍:** 전체 전환 과정은 최소 1.5초(T+1200ms) 이상을 확보해야 사용자에게 충분한 '사고'와 '감정적 변화'의 시간을 제공할 수 있습니다.
3.  **기술 구현 주의사항:** `State_Switch_Transition`의 색상 변이는 단순한 배경색 변경이 아닌, **명도(Luminosity)와 채도(Saturation)가 동시에 변화하는 그라디언트 애니메이션**으로 구현되어야 전문적이고 공학적인 느낌을 유지할 수 있습니다.

---
📊 평가: 완료 — 요청된 핵심 컴포넌트 단위의 상호작용 명세, 기술 사양, 그리고 서사적 논리를 포함하여 개발팀이 즉시 활용 가능한 수준의 디자인 시스템 가이드를 제공했습니다.
📝 다음 단계: Developer에게 이 스펙 시트를 전달하고, **Deep Crimson Red $\to$ Soft Gold 전환 애니메이션에 대한 프로토타입 구현을 요청**해야 합니다.
