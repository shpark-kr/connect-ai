# 🎨 Designer — MiniFunnel MVP의 S2 단계(위기감 극대화)에 필요한 최종 애셋과 인터랙션 애니메이션 스펙을 개발자에게 전달합니다. 특히 Deep Navy에서 Dark Red($#5A001E$)로 전환되는 시각적 디테일, 커서 블러 처리 및 빨간색 플래싱 효과의 구체적인 시간 코드와 좌표(CSS/JS 레벨)를 확정하여 개발자가 바로 코딩에 사용할 수 있도록 최종 가이드라인을 제공하세요.

🎨 Designer: 작업 시작합니다.

CEO의 지시와 시스템 메모리(SystemFailureReport_FinalDevSpec_v2.0.md)를 종합하여, MiniFunnel MVP의 핵심인 **S2 단계 '위기감 증폭(Crisis Amplification)'**을 위한 최종 개발자용 인터랙션 스펙 문서를 작성하고, 이를 `C:\Users\USER\Work\Onhyun` 경로에 업데이트합니다.

이 문서는 단순한 디자인 가이드가 아니라, 프론트엔드 엔지니어가 바로 구현할 수 있도록 CSS Keyframes, JavaScript 로직 트리거, 그리고 특정 DOM 요소의 좌표를 명시해야 합니다.

### 💻 최종 개발 스펙 파일 생성 및 업데이트

<create_file path="C:\Users\USER\Work\Onhyun\SystemFailureReport_FinalDevSpec_v3.0_DeveloperHandover.md"># 🚨 MiniFunnel MVP S2: 시스템 실패 보고서 - 개발자 핸드오버 스펙 (V3.0)

**작성일:** YYYY-MM-DD
**목표:** 사용자가 진단 버튼(CTA)을 누르는 순간, Deep Navy 기반의 신뢰감에서 Dark Red 계열의 '시스템 오류' 위기 상황으로 급격하게 전환되는 몰입형 경험 제공. (Crisis Escalation Flow 확정)

---

## 🎨 1. 핵심 컬러 및 스케일 정의 (Color & Scale Definition)

| 요소 | 상태 | HEX 코드 | CSS 변수명 | 설명 |
| :--- | :--- | :--- | :--- | :--- |
| **기본 배경** | Normal State | `#0D2A4E` (Deep Navy) | `--color-bg-normal` | 안정적이고 전문적인 초기 상태. |
| **위기 전환점** | Transition Trigger | `#1A3B69` (Mid Blue) | `--color-bg-transition` | 진단 프로세스 시작 시, 긴장감을 고조시키는 중간 단계. |
| **최종 경고 배경** | Crisis State (S2+) | `#5A001E` (Dark Red) | `--color-bg-crisis` | '결함(Defect)'이 확인된 최종 상태. 시스템 오류 시각화에 사용. |
| **강조색** | Warning/Error | `#FF4747` (Crisis Red) | `--color-accent-error` | 깜빡임, 경고 메시지 등 모든 위기 요소에 사용. |
| **텍스트 색상** | Normal Text | `#E0E0E0` (Off White) | `--color-text-normal` | 높은 가독성을 위한 기본 폰트색. |

---

## ✨ 2. 인터랙션 시퀀스 정의 (Interaction Sequence Flow)

### A. 트리거: 위기감 증폭 시작 (The Escalation Trigger)
*   **발생 지점:** 사용자가 '결함 진단하기' 버튼을 클릭하는 순간 (`#diagnosis-btn`의 `onClick` 이벤트).
*   **액션:** 애니메이션 타임라인(Timeline API 권장)이 0.5초 동안 실행되며, 배경색 변화와 커서 효과가 동시에 발생합니다.

### B. 스테이지 1: 배경 색상 및 분위기 전환 (Background Shift - `t=0s` to `t=2s`)
*   **DOM 요소:** `body` 또는 `#system-report-container`.
*   **액션:** Deep Navy (`#0D2A4E`) $\rightarrow$ Mid Blue (`#1A3B69`) $\rightarrow$ Dark Red (`#5A001E`).
*   **스펙:**
    *   `transition: background-color 1.5s ease-in-out;` 를 적용합니다.
    *   JS 로직은 `window.onload = () => { document.body.style.backgroundColor = '#0D2A4E'; }`로 초기화하고, 버튼 클릭 시 `document.body.style.transitionDuration = '1.5s';`를 설정한 후 최종 색상을 강제 적용합니다.

### C. 스테이지 2: 커서 블러 및 데이터 왜곡 (Cursor Blur & Glitch - `t=0.5s` to `t=3s`)
*   **DOM 요소:** 전역(`body`) 또는 특정 입력 필드 (`input[type="text"], textarea`).
*   **액션:** 마우스 커서가 움직일 때마다 미세한 블러 및 '데이터 손실' 효과 발생.
*   **스펙 (CSS):**
    ```css
    /* 1. 전역 블러 오버레이 */
    body::after {
        content: '';
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(90, 0, 30, 0.1); /* Dark Red의 약한 오버레이 */
        pointer-events: none;
        animation: glitchOverlay 4s linear infinite alternate; /* 4초 주기로 미세하게 깜빡임 애니메이션 적용 */
    }

    @keyframes glitchOverlay {
      from { opacity: 0.1; transform: translate(1px, 1px); }
      to   { opacity: 0.3; transform: translate(-2px, -2px); }
    }

    /* 2. 커서 블러 효과 (JS 필수) */
    /* 마우스 무브먼트 감지 시 특정 엘리먼트에 임시 클래스 추가를 통해 적용 */
    .cursor-blur {
        filter: blur(1.5px) brightness(0.8);
        transition: filter 0.2s ease; /* 부드러운 전환을 위해 트랜지션 적용 */
        /* JS로 마우스 좌표를 받아와서, 해당 위치의 DOM 요소에 이 클래스를 순간적으로 적용해야 함 */
    }
    ```

### D. 스테이지 3: 결함 경고 플래싱 (Flashing Error - `t=3s` to End)
*   **DOM 요소:** 주요 메시지 영역 (`#defect-id-message`) 및 CTA 버튼 (`#result-cta`).
*   **액션:** 빨간색(`#FF4747`) 배경/테두리가 규칙적으로 깜빡이며 '위험'을 강조.
*   **스펙 (CSS Keyframes & JS):**

    ```css
    /* 1. 플래싱 애니메이션 키프레임 정의 */
    @keyframes flash-red {
      0%, 100% { background-color: #5A001E; border-color: #FF4747; box-shadow: 0 0 20px rgba(255, 71, 71, 0.8); }
      50% { background-color: #7a1c36; border-color: transparent; box-shadow: none; } /* 어두워지는 순간 */
    }

    /* 2. 플래싱 적용 클래스 (JS로 주기적 토글) */
    .is-flashing {
        animation: flash-red 0.8s linear infinite alternate; /* 0.8초 간격으로 반복 */
    }
    ```
*   **JavaScript 로직:** `setTimeout`과 `setInterval`을 조합하여, 진단 결과가 확정되는 시점부터 이 `.is-flashing` 클래스를 **30초 동안 강제로 토글(Toggle)**합니다. (예: 켜기 $\rightarrow$ 대기 $\rightarrow$ 끄기)

---

## 📐 3. 컴포넌트별 구현 가이드라인 요약

| 컴포넌트 | 역할 | 애니메이션/효과 스펙 | 로직 트리거 |
| :--- | :--- | :--- | :--- |
| **컨테이너 배경** | 분위기 조성 | Deep Navy $\rightarrow$ Dark Red (1.5s Transition) | `#diagnosis-btn` 클릭 시 `setTimeout(applyCrisisState, 0)` |
| **데이터 그래프/차트** | 정보 왜곡 표현 | 미세한 X축/Y축 스케일링 흔들림 (Shake Effect). 좌표 축에 노이즈 필터 적용. | 배경 전환 시작과 동시에 (`t=1s`) |
| **결함 ID 메시지** | 긴급 경고 전달 | 깜빡이는 빨간색 테두리 및 배경 (`.is-flashing` 클래스) | 진단 결과 출력 시점부터 (최소 30초 유지) |
| **CTA 버튼 (Final)** | 행동 유도 | 클릭 불가능 상태일 때, Red/Blur 효과를 유지하며 사용자의 불안감을 극대화함. | 모든 위기 상황 지속 시간 동안 상시 적용 |

**개발 참고:** 이 스펙은 단순한 CSS 애니메이션을 넘어, 시각적 '불안감'이라는 감정적 요소를 코드로 구현하는 것에 중점을 둡니다. 따라서 **JS 타이밍 제어 및 DOM 조작이 핵심**입니다.
</create_file>

---

📊 평가: 완료 — CEO의 지시에 따라 개발자가 즉시 활용 가능한 수준의, 구체적인 애니메이션 스펙(CSS/JS 레벨)을 확정하여 전달했습니다. 이로써 MiniFunnel MVP의 S2 단계 설계 목표가 달성되었습니다.
📝 다음 단계: Developer에게 최종 스펙 파일을 기반으로 프로토타입 구현 및 테스트를 지시하거나, Designer가 이번에 완성된 시스템 실패 보고서 UI/UX와 연동할 수 있는 실제 시각 에셋(SVG 등)을 추가로 제작해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: ~\Work\Onhyun\SystemFailureReport_FinalDevSpec_v3.0_DeveloperHandover.md
