# 🔴 Mini-App Funnel V1.0 (Code Fix & Enhancement Spec)

## 📌 목적
개발 로직 안정화 검토 결과, Deep Crimson Red 경고 및 Glitch Effect의 **‘발생 시점(Timing)’**과 **‘위기감 레벨 분할(Tension Leveling)’**에 대한 디자인 의도 보강이 필요합니다. 단순한 버그 수정이 아닌, 위기감을 극대화하는 사용자 경험 흐름을 명시합니다.

## 🛠️ 주요 변경 지침 (MUST FIX & ENHANCE)

### 1. Glitch Effect 트리거 조건 강화 (Technical/Visual Sync)
*   **현상:** 글리치 효과가 특정 임계값 도달 시에만 발생하도록 로직이 명확하지 않음.
*   **문제점:** 경고의 강도가 불규칙하여 사용자에게 혼란을 줌. '시스템 오류'는 예측 가능한 패턴을 가져야 합니다.
*   **수정 지침 (코드 기반):** Glitch Effect는 **단순히 값이 임계치를 넘는 순간(Threshold Breach)**이 아니라, 해당 값의 변화율(`|Delta Value|`)과 현재 시스템 상태가 복합적으로 작용할 때 발생해야 합니다.
    *   `IF HOMA_IR < [THRESHOLD] AND (Current_Value - Previous_Value) < MINUS_DELTA:`
        *   **액션:** Glitch Effect (CSS `animation-glitch: 0.5s`)를 발동합니다.
        *   **디자인 강화:** 글리치와 동시에 배경 네이비 색상에 미세한 노이즈(Noise Overlay) 필터를 적용하여 '시스템 불안정'을 시각적으로 증폭시킵니다.

### 2. Deep Crimson Red 경고 UI 계층 구조화 (Hierarchy & Priority)
*   **현상:** 모든 중요한 메시지가 동일한 크기/강도의 빨간색으로 표시되어 중요도 구분이 어려움.
*   **문제점:** 사용자 피로도 증가 및 핵심 정보(CTA 유도)의 희석.
*   **수정 지침 (컴포넌트 기반):** 경고를 3단계 레벨로 분리하고, 각 단계에 맞는 시각적 컴포넌트를 사용해야 합니다.

| Level | 상태/경고 유형 | 색상 코드 (HEX) | 시각 효과 및 애니메이션 | 적합한 UI 컴포넌트 |
| :---: | :--- | :--- | :--- | :--- |
| **Level 1** | **주의 (Warning)** (e.g., '미흡') | `#CC3333` (Deep Crimson) | 미세 깜빡임 (`Pulse Effect`) + 작은 경고 아이콘 🔺 | `[Component: Warning Callout Box]` |
| **Level 2** | **위기 (Critical)** (e.g., '심각한 누수') | `#990000` (Deep Crimson Red) | 주기적인 진동 효과 (`Vibration Animation`) + 경고 타이머 시퀀스 | `[Component: System Alert Banner]` |
| **Level 3** | **시스템 오류 (Fatal)** (e.g., '진단 불가능') | `#FF0000` (Pure Red) | 강렬한 글리치 효과 + 화면 전체 깜빡임 (`Screen Flicker`) | `[Component: Emergency Override Overlay]` |

### 3. CTA 유도 구간의 미묘한 연출 지침 (UX Flow Enhancement)
*   **목표:** Funnel 진입 직전, 사용자가 가장 취약하고 위기감을 느낄 때 전환을 유도해야 합니다.
*   **수정 지침 (시간/시퀀스):**
    1.  HOMA-IR 수치가 Level 2에 도달합니다. (`[T+0s]`)
    2.  `System Alert Banner`가 활성화되며 경고 메시지가 표시됩니다. (`[T+1s]`)
    3.  진단 결과 데이터가 로딩되는 **빈 화면(Placeholder State)**에서, 갑자기 시스템 오류 팝업이 뜨며 Glitch Effect (Level 3)를 한번 짧게 강하게 발동시킵니다. (`[T+2.5s]`)
    4.  **최종 메시지:** "현재 시스템은 정확한 진단 모듈을 필요로 합니다."라는 문구와 함께 Mini-App Funnel의 CTA 버튼만 중앙에 남고, 주변의 모든 정보는 흐릿하게 처리(Depth Blur)됩니다. (`[T+3s]`)
*   **개발자 액션 요청:** 이 시퀀스 (Level 2 $\rightarrow$ Glitch/Level 3 $\rightarrow$ Blur + CTA Focus)를 위한 타이밍 제어 로직을 반드시 검증하고, 애니메이션 전환 지점의 부드러움을 최우선으로 테스트해야 합니다.

---
## ✅ 체크리스트 요약 (Developer QA Checklist)
1. [ ] Glitch Effect 발생 조건이 단순 임계값(Threshold)이 아닌, 변화율(Delta Rate) 기반인지 확인.
2. [ ] Level 1~3 경고 UI 컴포넌트가 적절한 HEX 코드로 분리되어 사용되는지 검토.
3. [ ] CTA 유도 직전의 'Deep Blur' 및 'Glitch/Level 3' 시퀀스가 명시된 시간표(T+0s ~ T+3s)에 맞춰 작동하는지 E2E 테스트 수행.