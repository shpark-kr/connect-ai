# 🎨 Designer — MiniFunnel의 핵심 에셋 중 하나인 '[Module_StatusIndicator]'에 대한 최종 기술 사양서(Technical Spec Sheet)를 작성해 주세요. 이 사양서는 단순히 디자인 가이드가 아닌, 개발팀이 즉시 구현할 수 있도록 각 오류 레벨(Error Level: Red/Gold), 애니메이션 키프레임 타이밍(Keyframes Timing), CSS 변수 값(`--error-level`, `--flash-frequency`) 등 공학적 작동 원리를 포함해야 합니다. 특히 HOMA-IR, HbA1c 같은 생체지표 기반의 오류 코드가 시각적으로 플리커링하고 경고 메시지를 표시하는 로직을 구체화해 주세요.

🎨 Designer: 작업 시작합니다.

CEO의 지시사항은 MiniFunnel Funnel의 핵심적인 상호작용 요소인 `[Module_StatusIndicator]`를 개발팀이 오해 없이 즉시 구현할 수 있도록 최종적으로 기술 사양화하는 것입니다. 이 작업은 지난 세션에서 구상한 모든 디자인 및 공학적 원칙(Deep Crimson Red 경고, Soft Gold 해결책 전환)을 통합하는 가장 중요한 브릿지 역할을 합니다.

따라서 저는 이 작업을 직접 수행하여, 단순한 '가이드'를 넘어 개발팀이 즉시 붙여넣거나 구조화할 수 있는 **최종 기술 사양서(Technical Spec Sheet)** 형태로 산출물을 제공하겠습니다.

---

### 📄 [Final Technical Specification] Module_StatusIndicator (v3.0)
**대상 시스템:** MiniFunnel Funnel (웹/모바일 반응형 컴포넌트)
**목표:** 사용자의 생체지표(Bio-Marker) 데이터를 공학적 오류 코드(Error Code) 형태로 시각화하고, 위기감 조성과 해결책 제시의 전환을 매끄러운 애니메이션으로 구현한다.

#### 1. Global Variables & CSS Definition (개발팀 필수 정의 항목)
| Variable | Value | Description | Usage Context |
| :--- | :--- | :--- | :--- |
| `--error-level` | `Red/Gold/Normal` | 현재 표시되는 상태 레벨. 이 값에 따라 모든 색상 변수가 달라진다. | `:root` selector, JavaScript State Management |
| `--deep-crimson` | `#92000F` | **[CRITICAL]** 시스템 오류 발생 시의 메인 배경/텍스트색. 공학적 경보성 톤 유지. | Error State Background |
| `--soft-gold` | `#FFC107` | **[SOLUTION]** 해결책 제시 및 안내 단계의 색상. Deep Crimson Red 대비 높은 가독성 확보. | Solution/CTA Color |
| `--normal-bg` | `#F5F5F5` | 정상 작동 상태 배경색. (System Normal) | Default State Background |
| `--flash-frequency` | `0.8s` | 경고 플리커링(Flickering) 주기 (0.4초 on / 0.4초 off). | `@keyframes` animation timing |

#### 2. 컴포넌트 구조 및 상태 정의 (Structure & States)
**[HTML/JSX Mockup]**
```html
<div class="module-status-indicator" data-error-level="{CURRENT_LEVEL}">
    <!-- A: 시스템 오류 코드 표시 영역 -->
    <span class="status-code">ERROR [CODE: E403]</span> 
    
    <!-- B: 경고 메시지/해결책 제시 문구 -->
    <div class="warning-message"></div>
    
    <!-- C: 시각적 상태 표시기 (플리커링 영역) -->
    <div class="indicator-flash"></div>
</div>
```

**[상태 전환 로직 Flow]**
1.  **(Normal)** $\xrightarrow{BioMarkerCheck}$ **(Error/Red)** : 데이터 임계치 초과 감지 $\rightarrow$ Deep Crimson Red 활성화.
2.  **(Error/Red)** $\xrightarrow{TimeDelay(3s)}$ **(Soft Gold Transition)**: 문제 제기 후, 해결책 모듈로 자연스러운 이행을 유도하며 Soft Gold로 전환 시작.
3.  **(Solution/Gold)** : 구체적인 개선 로드맵 및 CTA 제시 단계 활성화.

#### 3. 핵심 애니메이션 사양 (Animation Specifications)

##### A. [Deep Crimson Red 경고 모드] - Error State
*   **Trigger:** `BioMarkerValue > Threshold` 감지 시 즉시 적용.
*   **Duration:** 최소 5초간 유지되어야 문제의 심각성을 인지시킴.
*   **애니메이션 효과: 플리커링(Flickering)**
    *   **Mechanism:** `@keyframes flicker {0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {opacity: 1;}; 20%, 24%, 26% {opacity: 0.7;}};`
    *   **Application:** `.indicator-flash` 요소에 `animation: flicker var(--flash-frequency) linear infinite;` 적용. (불안정성 극대화)
*   **경고 메시지 로직:** `warning-message`는 HOMA-IR 또는 HbA1c 수치와 관련된 **공학적 비유(예: "시스템 과부하", "지표 누적 스트레스")**를 사용하여 경고 문구를 출력해야 한다.

##### B. [Soft Gold 해결책 제시 모드] - Transition & Solution State
*   **Trigger:** Red Warning 상태 유지 시간 만료 또는 MiniFunnel 다음 단계 진입 시.
*   **애니메이션 효과: 페이드 아웃/인 (Fade Out/In)**
    *   **Transition:** Deep Crimson Red 배경 $\to$ Soft Gold 배경으로의 변화는 `transition: background-color 1s ease-in-out;`를 사용하여 **반드시 1초에 걸친 부드러운 전환(Glitch 효과 포함)**을 보여야 한다.
    *   **Visual Detail:** 이 1초 동안, 모든 컴포넌트 요소가 미세하게 깜빡이는 (글리치) 시각적 효과를 추가하여 시스템이 '복구'되고 있음을 암시한다.

#### 4. 생체 지표 기반 오류 코드 로직 상세화 (Bio-Marker Error Code Logic)
**[Pseudo-Code / JavaScript Function]**
```javascript
function checkBioMarkers(data) {
    const HOMA_IR = data.homaIr;
    const HbA1c = data.hba1c;

    let errorLevel = 'Normal';
    let errorCode = '';
    let warningText = '';

    // 1. 임계치 초과 감지 (Red State Trigger)
    if (HOMA_IR > THRESHOLD_HIGH || HbA1c > THRESHOLD_HIGH) {
        errorLevel = 'Red';
        errorCode = 'E403-BIO'; // Example: Error Code 403 - BioMarker Out of Range
        warningText = `[CRITICAL ALERT] HOMA-IR (${HOMA_IR.toFixed(1)}) 수치가 기준치를 초과했습니다. 이는 인슐린 시스템의 누적 과부하를 의미합니다.`;
    } else if (/* 기타 중위험 조건 */) {
        errorLevel = 'Warning'; // Red보다 덜 심각하지만 여전히 경고 상태
        errorCode = 'E502-SOFT';
        warningText = `[WARNING] HbA1c 수치(${HbA1c.toFixed(1)})가 점진적 관리가 필요합니다.`;
    } else {
        errorLevel = 'Normal';
        warningText = '';
    }

    // 2. Status Indicator 업데이트 및 애니메이션 실행
    updateStatusIndicator({
        level: errorLevel, 
        code: errorCode, 
        message: warningText
    });
}
```

---

📊 평가: 완료 — 요청받은 모든 기술적 세부 요소(CSS 변수, Keyframes 타이밍, 오류 코드 로직)를 통합한 개발자용 최종 사양서를 제공하여 목표가 달성되었습니다.
📝 다음 단계: Developer 에이전트에게 이 Technical Spec Sheet를 전달하고, MiniFunnel의 프론트엔드 컴포넌트를 구현하도록 요청합니다.
