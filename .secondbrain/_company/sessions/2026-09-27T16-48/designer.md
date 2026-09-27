# 🎨 Designer — 개발팀 핸드오프에 필요한 최종 애니메이션 컴포넌트 세트를 완성합니다. Mini-App의 '위험도 변화'가 발생할 때마다 나타나는 핵심 요소(Deep Crimson Overlay, 점수 게이지 등)에 대한 인터랙티브 루프와 트랜지션을 구체적인 프레임별/시간대별 디자인 스펙으로 정리하고, 코다리가 테스트할 수 있는 형태로 자산 목록을 분류하여 개발팀에게 전달하십시오.

🎨 Designer: 작업 시작합니다.

CEO 지시에 따라 Mini-App Funnel의 핵심 인터랙티브 자산 세트를 개발팀에 전달하기 위한 최종 디자인 명세서(Design Specification Handover Package)를 완성합니다. 이 문서는 단순한 이미지가 아닌, **시간 기반의 상호작용 규칙**을 정의하여 코다리 에이전트가 검증하고 개발팀이 구현할 수 있는 형태로 구조화되었습니다.

---

## 📁 Mini-App Funnel: 핵심 애니메이션 컴포넌트 핸드오버 스펙 (V1.0)

### 💡 목표 및 원칙
*   **목표:** 사용자의 '위험도 변화'를 감정적으로 증폭시키고, 즉각적인 행동(Mini-App 진단)을 유도한다.
*   **원칙:** 모든 애니메이션은 **깊이감(Depth)**과 **긴급성(Urgency)**에 초점을 맞춘다. 단순한 색상 변화가 아닌, 시스템 경고음이나 물리적 충격 같은 느낌을 시각적으로 구현해야 한다.

### 🧩 컴포넌트별 상세 스펙 및 인터랙션 루프

#### 1. [Gauge] 점수 게이지 애니메이션 (The Score Degradation)
| 상태 | 설명 | 시간/Duration | 키프레임 & 이징(Easing) | 개발 지시사항 |
| :--- | :--- | :--- | :--- | :--- |
| **Normal → Warning** | (예: 75점 $\to$ 50점) 점수가 급격히 하락하며 경고색이 번져나가는 느낌. | 1.2초 | Start(Green/Yellow) $\to$ Easing Out Quad $\to$ Midpoint(Amber/Red Gradient). 게이지 바가 마치 '찢어지는' 듯한 시각적 불안정성 필요. | **[Asset]** `gauge_degrade_75_to_50.lottie` (SVG 기반) |
| **Warning → Critical** | (예: 50점 $\to$ 30점) 경고 상태가 임계점을 넘어 치명적 위기감으로 변하는 순간. | 0.8초 | Start(Amber) $\to$ Rapid Fall ($\text{Ease In Out Cubic}$) $\to$ End(Deep Crimson Red). 게이지 바 전체에 미세한 **글리치(Glitch)** 효과와 진동 애니메이션을 적용. | **[Asset]** `gauge_critical_alert.lottie` (진동/글리치 포함) |
| **Stabilization** | 점수가 일시적으로 정체되거나 안정화될 때. | 0.5초 | 부드럽게(Ease Out Sine) 떨림이 잦아들며, 주변으로 Deep Crimson Red의 잔상(Afterglow)이 은은하게 퍼짐. | 개발팀 참고용: 과도한 애니메이션 방지 루프. |

#### 2. [Overlay] 심층 위기 경고 오버레이 (The Deep Crimson Overlay)
| 발생 조건 | 목적 및 효과 | 애니메이션 스펙 | 트리거/제어 |
| :--- | :--- | :--- | :--- |
| **Critical 진입** | 사용자에게 즉각적인 '공포'와 '개입 필요성'을 각인. | 1.5초 동안 화면 전체를 Deep Crimson Red 계열의 필터가 덮음. 시작 시 `Opacity: 0%` $\to$ `Opacity: 100%`. 전환 직후 **미세한 쉐이크(Shake)** 효과와 함께, 중앙에 경고 메시지(`🚨 CRITICAL ALERT`)가 강하게 깜빡임(Blink). | 스코어 점수가 Critical Threshold(30점 이하)를 돌파하는 순간. (최우선 이벤트) |
| **CTA 유도 시** | Funnel의 핵심 목표인 Mini-App 진단을 강조. | 오버레이는 배경 전체가 아닌, *메시지와 CTA 영역만* 선택적으로 붉은색으로 하이라이트됨. 경고 메시지 뒤에 Deep Crimson Red의 빛 번짐(Bloom) 효과를 적용하여 '중요함'을 극대화. | Mini-App 진단 도구 유입 직전 (Problem $\to$ Solution 전환점). |

#### 3. [Transition] 시퀀스 간 연결 애니메이션
*   **섹션 이동:** 일반적인 슬라이드 전환 대신, 배경의 Deep Crimson Red 필터가 점차 강해지면서 마치 '깊은 데이터 분석 터널'을 통과하는 듯한 느낌으로 부드럽게 오버레이됨. (Transition: Dissolve + Color Shift).
*   **핵심 정보 노출:** 중요한 그래프나 수치(예: 30점)가 등장할 때, 주변부가 Deep Crimson Red의 스파크 효과와 함께 **'강제적으로 나타나는'** 시각적 충격을 주어야 함.

### 🛠️ 개발팀 핸드오버 자산 목록 (Asset Manifest for Dev Team)
다음은 애니메이션 구현을 위해 반드시 준비되어야 할 에셋들입니다. 모든 파일은 Lottie JSON 또는 SVG 형태로 전달합니다.

1.  **Gauge Assets:**
    *   `gauge_initial.svg`: 초기 상태 게이지 배경 및 마커.
    *   `gauge_degrade_75_to_50.lottie`: 경고 레벨 하락 애니메이션 루프.
    *   `gauge_critical_alert.lottie`: 임계점 돌파 시 글리치+진동 효과가 적용된 최종 자산 (핵심).
2.  **Overlay Assets:**
    *   `overlay_full_screen_critical.lottie`: 전체 화면 오버레이 경고 루프.
    *   `overlay_cta_highlight.svg`: CTA 버튼 및 주변 영역을 강조하는 선택적 하이라이트 마스크 (Deep Crimson Red).
3.  **Transition Assets:**
    *   `transition_tunnel_dissolve.lottie`: 섹션 전환에 사용되는 붉은색 필터 디졸브 효과.

---

📊 평가: 완료 — CEO 지시가 요구한 '개발팀 핸드오프를 위한 구체적인 애니메이션 컴포넌트 세트와 시간 기반의 스펙'을 완성했으므로 목표가 달성되었습니다.
📝 다음 단계: 이 자산들을 실제 개발 환경에 적용하고, 코다리 에이전트를 통해 해당 애니메이션 변화 로직(점수 $\to$ 위험도)과 연동된 **End-to-End 테스트 시나리오**를 작성해야 합니다.
