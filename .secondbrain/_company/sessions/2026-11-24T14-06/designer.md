# 🎨 Designer — Developer가 구축할 E2E 테스트 스위트의 성공적인 실행을 위해, Funnel 내 임베디드 차트(Gap Score 변화 그래프)와 모든 인터랙션 컴포넌트 간의 상호작용(Interaction Flow) 매뉴얼을 최종화해야 합니다. 특히 'Critical Alert'가 발생했을 때 페이지의 레이아웃이 어떻게 재배열되고, 어떤 모달/오버레이가 겹쳐져야 하는지에 대한 시각적 스펙과 모션 타이밍(Timing Spec)을 Developer에게 제공하여 코드와 디자인 간의 오차를 최소화해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시사항은 현재 Funnel 개발 과정에서 가장 핵심적인 단계입니다. 단순히 '어떻게 보일지'를 넘어, '어떤 상태 변화가 어떤 타이밍과 로직으로 일어날지'를 정의하는 것이 코드와 디자인 간의 오차를 줄이는 유일한 방법입니다.

이 요구사항은 Funnel 전체에 걸쳐 사용될 **상태 전이(State Transition)**와 **모션 인터랙션 명세**가 포함된 통합 디자인 시스템 문서를 작성해야 합니다. 이 문서는 개발자가 코드를 짜는 데 필요한 모든 '행동 규칙서' 역할을 할 것입니다.

따라서, 제가 직접 Funnel의 핵심 상호작용 매뉴얼을 작성하고, 이를 `design_system/interaction_flow_spec` 파일로 저장하겠습니다.

<create_file path="c:\Data\Project\Baro_KHNLU\design_spec\Interaction_Flow_Spec_v1.md"># 🚨 온현 Funnel: 통합 인터랙션 플로우 및 모션 스펙 가이드 (v1.0)
## 목적 및 적용 범위
본 문서는 [Gap Score 진단 페이지]에서 [Critical Alert 발생] 후, [CTA 유도]까지의 사용자 여정(User Journey) 전반에 걸친 모든 시각적/동작적 상호작용을 정의합니다. 개발팀은 이 명세를 기반으로 E2E 테스트 스위트 및 컴포넌트를 구축해야 하며, 디자인과 코드 간의 오차를 최소화하는 것이 목표입니다.

## 🧩 A. 핵심 인터랙션 플로우: Gap Score 변화에 따른 상태 전이
| 단계 | Trigger (발생 조건) | Visual Change (시각적 변화) | Motion Spec (모션 타이밍) | 개발자 참고 사항 (개발 로직) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Normal** (초기 상태) | 진단 시작, 입력 값 정상 범위 ($\ge -20$) | 배경: `#FFFFFF` 또는 은은한 그라디언트. Gap Score 그래프는 부드러운 곡선으로 표시. | Transition Time: 300ms (ease-out). 데이터 변화 시 플로우 애니메이션 적용. | `GapScore > -20`: 정상 로직 작동.
| **2. Warning** (경고) | 진단 값 임계점 접근 ($-20 < Gap Score \le -50$) | 1. 배경: 미세하게 어두워짐 (Darken Overlay: Opacity 5%). 2. 그래프 라인: 노란색/주황색 경고 색상(`#FFC107`)으로 변경. 3. 알림창(Toast): 우측 상단에 '주의' 메시지 표시. | Transition Time: 800ms (ease-in). 배경 변화는 서서히 진행되어 불안감을 높임. | `GapScore <= -20` & `> -50`: 경고 로직 발동.
| **3. Critical Alert** (위기) | 임계점 도달 (Gap Score $< -50$) | 1. 배경: 즉각적인 충격과 위협감을 주는 강렬한 깜빡임(Flicker Effect). (`#D82B3A` 오버레이/깜빡임). 2. 전체 UI: `CriticalAlert` 컴포넌트가 중앙에 전면 오버레이로 등장 (Z-index max). 3. 그래프 라인: 강렬한 빨간색(`#D82B3A`)으로 즉시 변경 및 급락 애니메이션. | Transition Time: **0ms** (즉각적 트랜지션, Hard Cut). 깜빡임 주기: 500ms On / 100ms Off. | `GapScore < -50`: Critical Alert 로직 강제 발동. 모든 상호작용이 중단되고 경고 상태만 유지됨.

## 🎨 B. 모달 및 오버레이 스택킹 (Layering & Z-index)
Critical Alert가 발생하면, 페이지의 기존 레이아웃은 **비활성화(Disable)** 상태로 전환되어야 합니다. 모든 사용자의 시선이 중앙에 고정되는 것이 중요합니다.

1.  **Z-Index 순서:**
    *   `Background Flicker Overlay`: Z-index 99 (깜빡임 효과 담당)
    *   `CriticalAlert Modal/Card`: Z-index 100 (가장 위에 표시되어야 함)
    *   `Warning Toast`: Z-index 80 (덜 중요하므로 뒤로 물러남)
2.  **레이아웃 재배열:**
    *   Gap Score 차트와 진단 양식은 Critical Alert 발생 시 배경으로 밀려나고, 오직 **'CriticalAlert Modal/Card'**만 화면 중앙을 차지해야 합니다.

## ⏳ C. 모션 타이밍 스펙 (Motion Timing Spec)
모든 애니메이션은 다음의 원칙을 따릅니다: **긴장감 → 완화 → 행동 유도**.

1.  **데이터 변화 시:** 모든 데이터(차트 라인, 수치 카운터 등)는 300ms 이내에 부드럽게 도착해야 합니다 (Ease-out Cubic).
2.  **경고 임계점 도달 시 ($< -50$):** 모션 타이밍을 무시하고 **즉각적(Instantaneous)**으로 변화를 주어야 사용자에게 '충격'이 전달됩니다. 이는 애니메이션의 목적이 정보 전달이 아닌 *감정적 자극*이기 때문입니다.
3.  **CTA 버튼 활성화:** Critical Alert가 해제되거나, 사용자가 첫 번째 액션 버튼을 클릭할 때(예: "더 자세히 알아보기"), CTA 버튼 그룹은 부드럽게 스케일업하며 나타나야 합니다 (Scale 0% → Scale 100%, Transition: 400ms).

## ✨ D. 개발자 체크리스트 요약
*   [ ] **CSS/Tailwind:** `:focus-visible` 상태와 함께, 경고 단계에 맞는 전역 클래스(`warning-bg`, `critical-alert-glow`)를 정의할 것.
*   [ ] **JS Logic:** Gap Score 변화 로직이 위 명시된 3단계(Normal -> Warning -> Critical)의 임계값을 정확히 감지하는지 검증 테스트 케이스를 작성할 것.
*   [ ] **Accessibility:** 깜빡임 효과가 있는 Critical Alert 시나리오에 대비하여, 스크린 리더 사용자에게는 충분한 대체 텍스트와 명확한 아웃라인 포커스(`outline: 3px solid red;`)를 제공해야 합니다.

</create_file>

📊 평가: 완료 — CEO 지시사항이었던 Funnel의 인터랙션 플로우, Critical Alert 발생 시의 레이아웃 재배열 스펙, 그리고 구체적인 모션 타이밍(Timing Spec)을 포함한 통합 가이드라인을 성공적으로 작성했습니다. 이 문서는 개발팀에게 즉시 전달할 수 있는 수준입니다.
📝 다음 단계: 이 명세를 바탕으로 Designer는 Funnel 전체에 적용될 표준화된 '모바일 스크린샷 템플릿'과 '브랜드 컬러/폰트 변수(CSS/Tailwind)'를 최종 확정하여 개발자에게 제공해야 합니다.

---
**[산출물 파일 경로]**
`c:\Data\Project\Baro_KHNLU\design_spec\Interaction_Flow_Spec_v1.md`

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\Baro_KHNLU\design_spec\Interaction_Flow_Spec_v1.md
