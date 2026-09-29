# 🎨 Designer — MiniFunnel의 'Critical System Alert UI (CSA-UI)' 컴포넌트 스펙을 기반으로, 실제 결제 직전 단계에 적용할 Deep Crimson Red 경고 메시지 및 애니메이션 타이밍의 최종 구현 가이드라인(Implementation Guide)를 작성해주세요. 특히, 오류 발생 시 사용자가 취해야 할 행동 유도 지점(CTA)과 그에 맞는 미니 로딩 스피너 디자인까지 포함하고, 이 모든 것이 '시스템 실패 과정'이라는 권위적 톤을 유지하도록 상세히 명시해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO 지시에 따라 MiniFunnel의 핵심 결제 게이트웨이 단계에 적용될 'Critical System Alert UI (CSA-UI)'의 최종 구현 가이드라인을 작성했습니다. 이 가이드는 단순한 디자인 사양을 넘어, **시스템 실패 과정을 사용자 경험(UX)의 권위적인 일부**로 격상시키고, 다음 행동으로 강제 유도하는 개발자 레벨의 상세 매뉴얼입니다.

---

## 🛠️ MiniFunnel CSA-UI (Critical System Alert UI) 최종 구현 가이드라인 v1.0

### 🎯 목표
MiniFunnel 결제 직전 단계(Payment Gateway Transition Point)에서 발생하는 모든 시스템 오류를 '사용자의 문제'가 아닌, **'시스템의 구조적 경고 신호'**로 포지셔닝하여 사용자에게 높은 위기감과 전문성을 동시에 전달합니다.

### 🎨 디자인 및 컬러 팔레트
| 요소 | 색상 코드 (HEX) | 역할 / 의도 |
| :--- | :--- | :--- |
| **Deep Crimson Red** | `#8B0000` | *Critical Alert*: 시스템의 치명적 실패, 즉각적인 주의 환기. 공포와 긴급성 극대화. |
| **Soft Orange/Yellow** | `#FFBF00` | *Recovery State*: 위기감 완화(De-escalation). 다음 행동 지점을 제시하며 심리적 안정감을 유도하는 전환점 색상. |
| **Background/Text** | `#1A1A2E` / `White` | 공식 다크 네이비 배경 유지. 전문성 및 권위 강조. |

### 🧱 컴포넌트 상세 스펙 및 인터랙션 시퀀스 (Interaction Sequence)

#### A. 트리거 조건 (Trigger Condition)
*   **발동 지점:** 결제 버튼 클릭 $\rightarrow$ 백엔드 게이트웨이 API 호출 성공 전, **어떤 종류의 시스템 오류가 발생했을 때 무조건 발동**합니다. (예: 카드사 통신 오류, 서버 타임아웃, 세션 만료 등)
*   **기술 스펙:** `[System.ErrorState]` 상태 머신 진입 시 강제 호출되어야 합니다.

#### B. [Phase 1] Critical Alert State (T=0ms ~ T+500ms)
이 단계는 사용자가 '무엇인가 잘못되었다'고 인식하는 시간입니다. **모든 입력 필드는 비활성화**됩니다.

1.  **시각적 효과:** 전체 화면에 Deep Crimson Red 색상의 오버레이(Overlay)가 급격히 덮어씌워집니다 (Fade-in).
2.  **핵심 메시지:** 중앙에 크고 권위적인 시스템 경고창이 나타납니다.
    *   **제목:** `[CRITICAL SYSTEM ALERT: PAYMENT FAILURE]` (글자 크기 최대화, Deep Crimson Red)
    *   **본문:** "시스템 게이트웨이 통신 오류가 감지되었습니다. 현재 결제 과정의 무결성이 확보되지 않았습니다."
3.  **전문성 강화 요소:** 필수적으로 **오류 코드를 명시**하여 기술적 권위를 부여합니다.
    *   `[ERROR CODE: GATEWAY_TIMEOUT_408]` (좌측에 고정 배치)
4.  **애니메이션:** 경고 메시지 배경이 2초 동안 미세하게 깜빡이는(Pulse) 애니메이션을 주어 시각적 위기감을 유지합니다.

#### C. [Phase 2] Information & Action State (T+500ms ~ T+1,800ms)
위기를 인지한 사용자에게 '무엇을 할 수 있는지'를 안내하는 단계입니다. **사용자의 행동 유도(CTA)에 집중**합니다.

1.  **시각적 전환:** Deep Crimson Red 오버레이가 점진적으로 투명해지며 (Fade-out), Soft Orange/Yellow 계열의 경고 테두리 또는 배경 그라디언트로 변환됩니다.
2.  **메시지 변경:** 문제 원인에 대한 설명과 함께, **사용자가 취해야 할 명확한 행동 3가지**를 제시합니다. (예: ① 네트워크 재점검, ② 결제 정보 수기 입력 시도, ③ 전문 상담 요청)
3.  **CTA 배치:** 가장 우선순위가 높은 액션(예: '재시도') 버튼을 최전방에 배치하고, 이 버튼은 Soft Orange/Yellow로 강조합니다.
4.  **미니 로딩 스피너 (Mini Loading Spinner):** CTA 주변에 위치하며, 일반적인 회전형이 아닌 **'데이터 재처리 중(Re-processing Data)'이라는 느낌의 공학적 펄스 애니메이션**을 사용해야 합니다. (예: 네 개의 점이 순차적으로 크기가 커지며 사라지는 패턴).

#### D. [Phase 3] Recovery State / Success Redirect (T+1,800ms~)
사용자가 CTA를 누르거나 시스템이 자동으로 다음 단계를 진입시키는 과정입니다.

*   **진행:** Mini Loading Spinner가 활성화된 상태로 페이지 전환을 준비합니다.
*   **애니메이션:** Soft Orange/Yellow에서 매우 차분하고 믿음직한 Light Blue 계열 (예: `#4CAF50`의 톤)로 최종 색상이 전환되며, 사용자가 시스템이 성공적으로 다음 단계로 이동했음을 직관적으로 인지하게 합니다.
*   **결과:** 정상적인 결제 정보 입력 필드 또는 MiniFunnel의 재진입 페이지로 부드럽게 리디렉션됩니다.

### 💻 개발자 구현 가이드 (Pseudo-Code Logic)

```javascript
// Pseudo-code for MiniFunnel Payment Gateway State Management

function handlePaymentGatewayError(errorObject) {
    // 1. System Error Triggered -> Phase 1 Start
    displayCSAUI('Deep Crimson Red', errorObject);

    // T=0ms: Deep Crimson Red Overlay, Alert Message, ERROR CODE Display
    setOverlayColor('#8B0000');
    document.getElementById('error-code').innerText = `[ERROR CODE: ${errorObject.type}]`; 
    
    setTimeout(() => {
        // T=500ms: Transition to Phase 2 (Information & Action)
        setOverlayColor('#FFBF00', 'fade'); // Soft Orange/Yellow fade-in
        displayActionMessage(errorObject);
        startMiniSpinner();
    }, 500);

    setTimeout(() => {
        // T=1800ms: Ready for Recovery / Success Redirect Prep -> Phase 3 Start
        clearInterval(spinnerInterval); // Stop the initial warning spinner
        setOverlayColor('#4CAF50', 'transition'); // Soft Green/Blue transition (Success Hint)
    }, 1800);
}

function startMiniSpinner() {
    // Logic for the controlled, pulsating "Re-processing Data" spinner.
    setInterval(() => {
        updatePulseAnimation();
    }, 300);
}

// Event Listener Hook: This function must be called on every failed API call.
document.getElementById('pay-button').addEventListener('click', (e) => {
    try {
        callPaymentAPI(formData);
    } catch (error) {
        handlePaymentGatewayError(error); 
    }
});
```

---

📊 평가: 완료 — CEO 지시사항의 모든 구성 요소(Deep Crimson Red 경고, 애니메이션 타이밍, CTA, 미니 로딩 스피너, 시스템 실패 권위적 톤)를 포함한 구체적이고 개발 가능한 가이드라인을 제시했습니다.
📝 다음 단계: 이 가이드를 기반으로 디자인 에셋 (PSD/SVG) 및 실제 인터랙션 프로토타입 제작에 착수해야 합니다.
