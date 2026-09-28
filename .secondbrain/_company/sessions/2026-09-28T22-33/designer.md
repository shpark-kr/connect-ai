# 🎨 Designer — Developer가 코딩에 즉시 사용할 수 있도록, Mini-App Funnel의 '위기 $\to$ 해결' 전환 프로토콜 인터랙티브 스펙 시트(CSS Keyframes 레벨)를 기반으로 최종 UI 컴포넌트 명세서와 필요한 CSS 변수 목록을 재확인하여 개발자에게 전달해 주세요. (개발자가 코딩에만 집중할 수 있도록, 비주얼 자산 관점의 모든 디테일을 정리해야 합니다.)

🎨 Designer: 작업 시작합니다. Mini-App Funnel의 '위기 $\to$ 해결' 전환 프로토콜에 대한 최종 개발 스펙 시트를 완성하여, 코딩 단계에서 발생할 수 있는 모든 비주얼 오해를 제거하겠습니다.

개발자가 이 명세서를 기반으로 `MiniFunnel.tsx` 내부에 스타일과 로직을 구현하면 됩니다. 단순한 디자인 가이드가 아니라, **상태 변화(State Change)에 따른 CSS Keyframes와 변수 정의**에 초점을 맞추었습니다.

---

## 📄 [최종] Mini-App Funnel 인터랙티브 스펙 시트 V3.0 (개발자 전용)
**목표:** 네트워크 불안정성 기반의 '위기 $\to$ 해결' 감정 아크를 완벽히 구현한다.
**배포 대상:** 개발 에이전트 (코다리)
**주요 변경 사항:** Transition State에 대한 Keyframe 정의 및 모든 색상/시간 변수화.

### I. 🎨 시스템 CSS 변수 목록 (Variables Definition)

개발자가 하드코딩 대신 변수를 사용하도록 강제합니다. 이는 유지보수와 디버깅의 핵심입니다.

| 변수 이름 | 값 (Hex Code) | 설명 | 적용 영역 |
| :--- | :--- | :--- | :--- |
| `--color-primary` | `#4A1E5A` | 브랜드 메인 컬러 (딥 퍼플 계열) | 일반 UI 요소, 헤더 등 |
| `--color-soft-gold` | `#F5E6C7` | 기본 배경/휴식 상태 색상 | 초기 로딩 및 해결 단계 배경 |
| `--color-crisis-red` | `#B3001F` | **위기 경고** 메인 컬러 (Deep Crimson Red) | 오류 메시지, 플래싱 UI 요소의 주색 |
| `--color-text-dark` | `#1A1A1A` | 기본 텍스트 색상 (높은 가독성) | 일반 텍스트 |
| `--color-bg-default` | `rgb(255, 255, 255)` | 기본적인 배경색 (Pure White 대비) | 컴포넌트 내부 배경 |
| `--transition-duration` | `0.6s` | 모든 상태 변화의 부드러운 전환 시간 | `:hover`, State Transition 전반 |
| `--crisis-pulse-speed` | `1.2s` | 위기 경고 효과 (Pulse)의 반복 속도 | `@keyframes pulse` |

### II. 🚨 핵심 컴포넌트 명세: 상태별 시각적 변화 로직

Funnel은 다음 세 가지 명확한 **상태(State)**를 가집니다. 각 상태는 완전히 다른 CSS 클래스(`status-normal`, `status-crisis`, `status-solution`)를 통해 제어되어야 합니다.

#### 1. State: Normal (평온/대기)
*   **목적:** 사용자에게 안정감과 신뢰감을 제공하는 초기 진단 단계.
*   **배경색:** `--color-soft-gold`
*   **주요 요소 스타일:** 부드러운 그림자(Soft Shadow), 미니멀리즘 카드 디자인.
*   **애니메이션:** 없음 (또는 매우 느리고 잔잔한 배경 광원 효과).

#### 2. State: Crisis (위기 발생) - 🔥 Critical Focus Area
*   **발동 조건:** API 호출 실패, 데이터 전송 오류 등 '시스템적 불안정성' 감지 시.
*   **시각 목표:** **공학적 경고(Engineered Alert)** 느낌 부여. 시스템이 멈추거나 오작동하는 듯한 긴급함 연출.
*   **CSS Keyframes: `@keyframes flash-warning`**
    ```css
    @keyframes flash-warning {
      0%, 100% { box-shadow: 0 0 5px rgba(179, 0, 31, 0.8); border-color: #B3001F; background-color: rgba(179, 0, 31, 0.1); }
      50% { box-shadow: 0 0 20px rgba(179, 0, 31, 1), inset 0 0 10px rgba(179, 0, 31, 0.8); background-color: rgba(179, 0, 31, 0.2); }
    }

    /* 적용 클래스 */
    .status-crisis {
      background-color: var(--color-soft-gold); /* 배경은 유지하되 */
      border: 4px solid var(--color-crisis-red); /* 경고 테두리 추가 */
      animation: flash-warning var(--crisis-pulse-speed) infinite alternate;
      /* 레이아웃 요소가 깜빡이는 듯한 효과를 주어 불안감을 증폭 */
    }
    ```

#### 3. State: Solution (해결/행동 유도)
*   **발동 조건:** Funnel Mini-App의 데이터 분석 완료 및 해결책 제시 시점.
*   **시각 목표:** 경고의 긴장감 해소 $\to$ **확신과 명료함(Clarity)**으로 전환.
*   **CSS Keyframes: `@keyframes stabilize`**
    ```css
    @keyframes stabilize {
      0% { opacity: 0; transform: translateY(20px); }
      100% { opacity: 1; transform: translateY(0); }
    }

    /* 적용 클래스 */
    .status-solution {
      background-color: var(--color-soft-gold); /* 안정적인 배경 유지 */
      border: none; /* 경고 테두리 제거 */
      box-shadow: 0 15px 30px rgba(74, 30, 90, 0.1); /* Soft Shadow로 신뢰감 부여 */
      animation: stabilize var(--transition-duration) ease-out;
    }
    ```

### III. 📐 컴포넌트별 레이아웃 및 애니메이션 좌표 (Layout & Timing Blueprint)

| 섹션 | 상태 변화 시점 | 주요 연출 요소 | 시간 흐름 (Timing) | 디테일 지침 |
| :--- | :--- | :--- | :--- | :--- |
| **A. 진단 영역** | Normal $\to$ Crisis Transition Start | 로딩 스피너가 갑자기 빨간색 플래시로 변함. | 0s ~ 1.5s (급격한 변화) | `MiniFunnel`의 메인 컨테이너에 `status-crisis` 클래스를 강제 적용하며, **브랜드 컬러에서 경고 색으로의 급변**이 느껴지도록 해야 합니다. |
| **B. 위기 메시지** | Crisis State 유지 중 (최고조) | "WARNING: Data Integrity Failure." 텍스트가 깜빡이며, 주변 컴포넌트 테두리 전체에 `flash-warning` 적용. | 1.5s ~ 4.0s (긴장감 최고조) | **Deep Crimson Red**을 사용한 경고 UI를 중앙에 배치하고, 모든 정보 전달이 *불가능*하다는 메시지를 주는 것이 중요합니다. |
| **C. 해결책 제시** | Crisis $\to$ Solution Transition Start | 화면 전체가 잠깐 어두워지거나(Fade Out), `Deep Crimson Red` 플래시가 멈추고 `Soft Gold`로 부드럽게 복귀함. | 4.0s ~ 5.0s (이완 및 전환) | **Transition Keyframe:** 이 지점에서 반드시 `status-solution` 클래스로의 변경을 Trigger 해야 합니다. 애니메이션은 `ease-out`으로 가장 부드러워야 합니다. |
| **D. CTA 유도** | Solution State 유지 중 | 해결책(CTA 버튼)이 중앙에 나타나며, 마치 '정상화된 시스템'처럼 확실하게 고정됨. | 5.0s ~ End (안정적 정보 제공) | CTA 버튼은 `Deep Crimson Red`가 아닌 `--color-primary`를 사용하여 신뢰성을 높이고, 배경의 Soft Gold와 대비되게 해야 합니다. |

---
📊 평가: 완료 — 개발자가 코딩에 바로 사용할 수 있는 CSS 변수 및 Keyframes 레벨의 구체적인 지침을 제공하여 명세서 작성이 목표로 달성되었습니다.
📝 다음 단계: 개발 에이전트(코다리)가 위 스펙 시트를 기반으로 `MiniFunnel.tsx` 컴포넌트에 스타일과 상태 관리 로직을 적용하고, E2E 검증 테스트를 실행해야 합니다.
