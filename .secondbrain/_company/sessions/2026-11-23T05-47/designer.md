# 🎨 Designer — 개발팀과의 협업을 위해, Funnel E2E 테스트가 성공적으로 안정화되었을 때를 가정한 'Critical Gap' 컴포넌트의 최종 UI/UX 스펙을 준비하세요. 개발자가 제시하는 실제 데이터 로딩 흐름과 기술적 제약을 고려하여, 심리적 강렬함과 시스템 구현 가능성을 모두 갖춘 디자인 브리프를 작성해야 합니다.

🎨 Designer: 작업 시작합니다.

현재 Funnel E2E 테스트가 실패한 상황(에러 로그 확인됨)이므로, 최종 UI/UX 스펙은 '기술적 안정화 가정' 하에 **모듈식 디자인 시스템 브리프** 형태로 작성하는 것이 가장 가치 높습니다. 단순히 이미지를 만드는 것을 넘어, 개발팀이 상태 변화에 따라 컴포넌트를 구현할 수 있도록 구조와 로직을 명시해야 합니다.

다음은 Funnel E2E 테스트가 성공적으로 안정화되었고, 데이터 로딩 흐름이 확정되었다고 가정하고 작성한 **'Critical Gap 시각화 모듈 (v1.0)'** 디자인 브리프입니다.

---

# 🚨 Critical Gap Visualizer Component Spec (D-System v1.0)

**목표:** 사용자가 자신의 건강 데이터가 '시스템 오류' 상태에 빠졌음을 직관적이고 심리적으로 강렬하게 인지하도록 유도한다. 단순한 경고창이 아닌, **데이터 시스템 자체의 붕괴 위협**처럼 느껴져야 한다.
**대상 영역:** 모든 핵심 수치 지표(Vital Metric)가 표시되는 대시보드 섹션 (특히 Funnel CTA 주변).

## 1. 시스템 상태 정의 및 반응 로직 (State Machine Logic)

컴포넌트는 데이터의 임계점(Threshold)에 따라 세 가지 명확한 상태를 가져야 하며, 각 상태는 단순 색상 변화가 아닌 **시각적 교란(Visual Disruption)**을 동반해야 합니다.

| 상태 (State) | 데이터 기준 | 시각적 목표 (Psychological Goal) | 개발 트리거 (Trigger) |
| :--- | :--- | :--- | :--- |
| **🟢 Normal (Baseline)** | Gap Score < 10% | 무난함, 관찰 가능. | 초기 로딩 또는 안정 데이터 수신. |
| **🟠 Warning (Pre-Failure)** | 10% $\le$ Gap Score < 30% | 주의 환기, '무언가 잘못되고 있다'는 막연한 불안감 유발. | 데이터 값의 급격한 변화(Slope) 감지. |
| **🔴 Critical Failure** | Gap Score $\ge$ 30% | 위협, 즉각적인 조치 필요 (Panic). 시스템 오류 경고. | 임계점 초과 + 특정 지표 결측/오류 발생 시. |

## 2. 디자인 브리프: 컴포넌트별 상세 스펙

### A. Normal State (기본값)
*   **배경:** 다크 네이비 계열 (#1A233B). 미묘한 노이즈 오버레이(Noise Overlay, Opacity 5%) 유지.
*   **지표 표시:** 일반적인 글래스모피즘 카드 안에 배치. 데이터 값은 골드 포인트 컬러(#FFC107)를 사용하되, 간결하게 표현.

### B. Warning State (🟠 주의 단계) - `data-warning` 클래스 적용
이 상태는 '데이터가 불안하다'는 느낌을 주어야 합니다.
*   **배경 변화:** 배경 노이즈 오버레이의 **강도(Intensity)**를 5% $\rightarrow$ 15%로 증가시킵니다. (미세한 지직거림 효과).
*   **테두리/애니메이션:** 컴포넌트 전체에 가늘고 깜빡이는(Pulsing) 주황색(`#FF9800`) 테두리를 추가합니다. `animation: pulse 1s infinite alternate;` 적용.
*   **텍스트 효과 (Data Drift):** 수치 데이터 값 주변에 아주 작은 글리치(Glitch) 효과를 주기적으로 발생시켜, 숫자가 '흔들리는' 듯한 착시를 유도합니다.

### C. Critical Failure State (🔴 심각 오류 단계) - `data-critical` 클래스 적용
최고의 위협감을 주는 상태입니다. 시스템이 멈춘 듯한 느낌을 주어야 합니다.
*   **배경 변화:** 배경색 전체가 어두운 빨간색(Deep Crimson, `#A82323`)으로 미세하게 오버레이 됩니다. (완전히 바뀌지 않도록 주의).
*   **시각적 교란 (The Core Effect):**
    1.  **글리치 효과:** 모든 텍스트 컴포넌트(`h1`, `p` 등)에 **강력한 글리치 애니메이션**을 적용합니다. (좌우로 짧게 이동하며 색상이 번쩍이는 효과).
    2.  **Noise/Static:** 노이즈 오버레이의 강도를 30%까지 최대화하고, 가끔씩 화면 전체가 순간적으로 '노이즈 스파이크(Noise Spike)'를 일으키는 애니메이션을 추가합니다. (CSS Filter: `hue-rotate()` 및 Opacity 급변 활용).
    3.  **경고 메시지:** 컴포넌트 하단에 "CRITICAL DATA DISRUPTION DETECTED"와 같은 시스템 경고 문구를 빨간색으로 고정 배치하고, 텍스트가 마치 **전송되는 데이터 패킷**처럼 깜빡이게 합니다.

## 3. 기술 구현 가이드라인 (Developer Blueprint)

개발팀은 다음의 자바스크립트 기반 상태 관리 로직을 따라야 합니다.

```javascript
// Pseudocode for Component Logic
function updateCriticalGap(newScore, oldScore) {
    let currentState = getComponentState(); // 현재 상태 가져오기

    if (newScore >= 30) {
        applyCSSClass('data-critical');
        triggerAnimation('Glitch', 'Noise Spike');
        displayAlertMessage("시스템 전력 부족: 즉각적인 개입 필요");
    } else if (newScore >= 10 && oldScore < 10) { // 경계점 감지
        applyCSSClass('data-warning');
        triggerAnimation('Pulse', 'Data Drift');
        displayAlertMessage("주의: 데이터 변동성 증가 감지");
    } else if (newScore < 10 && currentState !== 'normal') {
        applyCSSClass('normal');
        clearAnimations();
        displayAlertMessage(""); // 메시지 제거
    } else {
        // 상태 변화 없음
    }
}
```

---
📊 평가: 완료 — E2E 테스트의 성공 가정을 전제로, 개발팀이 요구하는 기술적 깊이(State Machine, 애니메이션 로직)를 포함한 모듈화된 최종 스펙을 제시하여 목표 달성이 가능합니다.
📝 다음 단계: 코다리 에이전트가 Funnel E2E 테스트 환경 안정화를 완료하고 실제 데이터 흐름/기술 제약 사항을 공유해야 합니다.

---
**[핵심 기대 효과]**
*   단순히 '빨간색'으로 경고하는 것이 아니라, **시스템 자체가 고장나고 있다는 위협감**을 주어 사용자의 행동(CTA 클릭)을 유도합니다.
*   모든 시각적 요소에 애니메이션/상태 변화를 부여하여 지루할 틈이 없는 몰입도를 유지합니다.
