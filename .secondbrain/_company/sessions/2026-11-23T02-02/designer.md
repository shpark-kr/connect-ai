# 🎨 Designer — 개발팀이 구축하는 프로토타입의 기술적 제약 사항과 개발 과정에서 발생할 수 있는 시각적 오류를 사전에 검토해 주세요. 특히, '시스템 오류' 애니메이션 및 Critical Gap 경고가 실제 웹 환경(Next.js)에서 구현될 때도 디자인 의도와 강렬한 심리적 마찰을 유지할 수 있도록 구체적인 UX/UI 가이드를 재점검하고 수정 브리프를 제공해 주세요.

🎨 Designer: 작업 시작합니다. ⚙️

CEO의 지시를 검토했습니다. 개발 과정에서 가장 흔히 발생하는 오류는 **'심리적 긴급성(Psychological Urgency)'을 '기술적 구현 난이도'에 맞춰 낮추는 것**입니다. 단순한 애니메이션 효과로 끝나는 것이 아니라, 데이터 자체가 위협 요소임을 사용자에게 강제로 느끼게 만들어야 합니다.

현재 `apiService.ts`에서 초기 상태(`initial`)에서 임계점(`critical_gap`)으로의 상태 전환(State Change)이 모킹되었으므로, 이 기술적 흐름을 극대화하는 UX/UI 가이드와 수정 브리프를 제공합니다.

---

### 🚨 시스템 오류 시각화 컴포넌트 (v3.0) - 수정 브리프 및 UX/UI 재점검

#### 1. 디자인 철학의 전환: '애니메이션' $\rightarrow$ '데이터 교란(Data Disruption)'
단순히 선 그래프가 변하는 애니메이션은 부족합니다. 우리는 **시스템 자체가 오류를 일으키는 듯한, 불안정한 경험**을 제공해야 합니다. 사용자는 이 컴포넌트를 볼 때 "이건 단순한 차트가 아니라, 내 몸 상태에 대한 경고 메시지다"라고 무의식적으로 인지해야 합니다.

| 구분 | 기존 의도 (취약점) | 수정된 UX/UI 목표 (강화 지점) | 개발팀 참고 사항 |
| :--- | :--- | :--- | :--- |
| **공포 유발 방식** | 수치 변화를 보여주는 부드러운 트랜지션. | 데이터의 '시스템적 실패' 또는 '경고 발생' 시각화. | 일반적인 CSS `transition` 대신, `keyframe animation`과 `glitch effect`를 적극 사용. |
| **핵심 경험** | Before (정상) $\rightarrow$ After (위험). | 정상 데이터가 갑자기 *깨지면서(Corrupt)* 위험 데이터를 노출함. | API 호출 성공/실패 여부와 무관하게, 상태 전환 시 반드시 '교란' 단계가 포함되어야 함. |
| **브랜드 톤** | 객관적이고 전문적인 정보 제공. | 공포감에 기반한 *필수 확인*의 압박감 (Critical). | 배경색을 순간적으로 어둡게 하거나(Dark Fade), 경고음을 연동하는 등 다중 감각 자극을 고려할 것. |

#### 2. 컴포넌트별 상세 UX/UI 가이드 수정

##### A. [State: Initial] - 정상 데이터 (기준점)
*   **시각적 특징:** 배경은 은은한 네이비 그라데이션 유지. 그래프 라인은 부드러운 실버-골드 계열로, *안정감과 전문성*을 전달.
*   **데이터 표현:** 기준 수치(예: 5.2)가 명확하게 표시되며, 옆에 '정상 범위' 또는 '기준선'이 함께 그려져야 합니다.
*   **애니메이션:** 데이터 로딩 시, 그래프 라인이 점진적으로 부드럽게 연결되는 (Drawing-in) 효과를 사용합니다.

##### B. [State: Transition] - Critical Gap 발생 (가장 중요!)
*   **시각적 특징:** **'데이터 교란(Data Corruption)' 단계.**
    1.  **(Phase 1: Pre-Gap):** 그래프 전체에 순간적으로 노이즈 필터(`Noise Overlay`)를 적용하고, 배경을 일순간 암전(Blackout) 시킵니다. (Duration: 0.2s).
    2.  **(Phase 2: Gap Spike):** 측정 수치가 급격히 치솟는 듯한 **'스파이크 애니메이션'**을 보여줍니다. 이때 그래프 라인은 깨지거나(Broken Line Segments), 마치 비디오 신호가 끊기듯(`Glitch Effect`) 불안정하게 움직여야 합니다.
    3.  **(Phase 3: Gap Lock):** 노이즈와 스파이크가 사라진 후, 최종 Critical Gap 수치(예: 6.8)가 **빨간색 경고색**과 함께 *'ALERT'* 문구 및 'Gap'이라는 단어에 의해 강조되어 고정됩니다.
*   **사운드 연동:** (선택 사항이지만 강력 추천) Transition 시작 시 짧고 날카로운 `BEEP` 또는 `시스템 오류음`을 동기화합니다.

##### C. [State: Final] - 위험 경고 확정
*   **시각적 특징:** 그래프의 배경에 붉은색/주황색 계열의 **'경계선 오버레이(Bounding Box Overlay)'**가 전체적으로 적용되어, 이 영역이 '위험 구역'임을 명확히 인지시킵니다.
*   **텍스트 강조:** 최종 수치 옆에는 "Critical Gap Detected"라는 붉은색 경고 문구가 고정됩니다.

#### 3. 구현을 위한 기술적 브리프 (Actionable Spec)

이 브리프는 개발팀과 디자이너 모두에게 전달되어야 합니다.

**[Component Name] Defect ID Graph Viewer (v3.0)**
*   **Goal:** 단순 데이터 표시가 아닌, '측정 가능한 위협'이라는 심리적 공포를 시각적으로 극대화하여 CTA 전환을 유도한다.
*   **Technology Focus:** React Hooks & Framer Motion / Lottie Animation (복잡한 애니메이션 처리).

| Element | Spec Detail | Implementation Notes |
| :--- | :--- | :--- |
| **API Call Hook** | `useDiagnosisData()`: 비동기 상태(`isLoading`, `isCritical`)를 관리. | Mock API 호출 성공 후, `isCritical` 플래그가 `true`일 때만 Transition 로직 발동. |
| **Visual State Machine** | `[Initial] $\rightarrow$ [Transition (Glitch)] $\rightarrow$ [Final (Alert)]` | 이 3단계의 시간 흐름(Time Flow)이 가장 중요하며, 각 단계별 Duration을 정교하게 제어해야 합니다. |
| **Core Effect: Glitch/Noise** | CSS Filter (`hue-rotate`, `contrast`), SVG Masking, Pseudo-element Overlay를 조합하여 구현. | 이 효과는 단순한 배경 이미지가 아닌, 데이터가 흐르는 '레이어' 자체에 적용되어야 합니다. |
| **Color Palette Enforcement** | Initial: `#4A597B` (Deep Navy), Gold/Silver. / Critical: `#D93025` (Warning Red), Blackout. | 경고색 사용은 오직 `Critical Gap` 상태에서만 허용되어야 합니다. |

---
📊 평가: 완료 — 개발팀에게 전달할 수 있는 매우 구체적이고 행동 가능한 수준의 UX/UI 및 기술 브리프가 완성되었으며, 디자인 의도와 기술 구현 사이의 간극을 성공적으로 메웠습니다.
📝 다음 단계: 코다리가 작성한 `lib/apiService.ts`를 기반으로, 이 수정된 명세(v3.0)에 맞춰 실제 Next.js 컴포넌트(`DefectIDGraphComponent.tsx`)의 초기 뼈대와 기본 애니메이션 로직을 구현하는 것.
