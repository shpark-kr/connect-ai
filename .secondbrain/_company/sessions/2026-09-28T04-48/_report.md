# 📝 CEO 종합 보고서

🎨 Designer: 작업 시작합니다.

CEO님의 지시에 따라 Mini-App Funnel의 핵심 컴포넌트인 '시스템 리스크 스코어(System Risk Score)'의 최종 디자인 명세서(Design Spec)를 완성했습니다. 이 문서는 개발팀이 즉시 코딩에 착수할 수 있도록 인터랙션 로직, 애니메이션 트리거, 그리고 구조화된 CSS/JS 가이드라인을 포함합니다.

---

# 📜 System Risk Score 컴포넌트 최종 Design Specification (V1.0)
**프로젝트:** 온현 Mini-App Funnel
**목표:** 전문 지표(HOMA-IR, MMIV Ratio) 기반의 객관적 데이터를 '공학적 위협감'으로 전환하여 사용자에게 강제적인 행동 유도(Mini-App 진입)를 발생시킨다.
**핵심 비주얼 컨셉:** Deep Crimson Red 경고 시스템 (System Failure Simulation)

## 1. 컴포넌트 개요 및 로직 정의

### A. 입력 변수 및 계산 로직 (The Hook)
| 지표 | 설명 | 가중치 ($\text{W}_i$) | 범위/단위 |
| :--- | :--- | :--- | :--- |
| HOMA-IR | 인슐린 저항성 지수 | 0.4 | 무차원 스코어 |
| MMIV Ratio | 근력 대비 대사 활성도 비율 | 0.6 | 무차원 스코어 |

**총 리스크 스코어 (System Risk Score, $R$) 계산 공식:**
$$R = (\text{HOMA-IR} \times 0.4) + (\text{MMIV Ratio} \times 0.6)$$

### B. 위험 레벨 및 임계값 (Thresholds)
스코어($R$)에 따라 세 가지 명확한 리스크 레벨이 정의되며, 이 레벨의 변화가 시각적/애니메이션 트리거를 결정합니다.

| 리스크 레벨 | 스코어 ($R$) 범위 | 심리적 의미 | Deep Crimson Red 적용도 |
| :--- | :--- | :--- | :--- |
| **Level 1: 정상 (Stable)** | $R < 2.0$ | 시스템 안정. 현재 상태는 괜찮음. | Minimal / None |
| **Level 2: 경고 (Warning)** | $2.0 \le R < 3.5$ | 미세한 이상 감지. 주의 필요. | Warning Flashing / Red Overlay (Soft) |
| **Level 3: 위기 (Critical/Failure)** | $R \ge 3.5$ | 시스템 과부하! 즉각적 조치 필요. | Deep Crimson Red Flash / Distortion Effect (Hard) |

## 2. 인터랙션 Flowchart 및 애니메이션 명세 (The Experience)

**[Flowchart: Input $\rightarrow$ Calculation $\rightarrow$ State Change $\rightarrow$ Output]**

1.  **START:** User enters HOMA-IR & MMIV values $\rightarrow$
2.  **CALCULATE:** System calculates $R = 0.4 \cdot \text{HOMA} + 0.6 \cdot \text{MMIV}$
3.  **CHECK THRESHOLD:** Determine Risk Level (L1, L2, or L3) $\rightarrow$
4.  **TRIGGER ANIMATION:** Apply appropriate CSS/JS effects based on the determined level $\rightarrow$
5.  **OUTPUT:** Display Score ($R$) and Textual Diagnosis (e.g., "경고! 근력 자원 고갈 위험 감지")
6.  **END:** Mini-App CTA 활성화 강제

### A. 프레임 단위 시각 반응 상세 정의 (Deep Crimson Red Focus)

| 레벨 | Deep Crimson Red ($\#8B0000$) 사용법 | 애니메이션 트리거/효과 | 코딩 지침 (CSS Keyframes/JS Logic) |
| :--- | :--- | :--- | :--- |
| **Level 1: 정상** ($R < 2.0$) | 배경에 미세한 진단 라인(Thin Blue/Gray Line)만 사용. 경고색 없음. | *None*. 부드럽고 안정적인 인터페이스 유지. | `opacity: 0.2` (Background lines). **JS:** No animation loop running. |
| **Level 2: 경고** ($2.0 \le R < 3.5$) | 주요 수치와 주변 영역에 Deep Crimson Red의 *Soft* 오버레이 시작. | **Subtle Flashing & Pulse:** 배경 전체에 $1.5\text{s}$ 주기로 낮은 진폭의 적색 플래시(Pulse)가 발생하며, 경고 메시지가 부드럽게 확대/축소됨 ($\text{scale}(1)$ $\leftrightarrow$ $\text{scale}(1.02)$). | **CSS:** `@keyframes warning-pulse { 0%, 100% { box-shadow: 0 0 5px #8B0000; } 50% { box-shadow: 0 0 15px #AA3333; } }`. **JS:** `setInterval(applyPulse, 1500)`. |
| **Level 3: 위기** ($R \ge 3.5$) | 전체 시스템이 Deep Crimson Red로 오염된 듯한 느낌 연출. 경고 문구가 플래싱의 주체가 됨. | **System Overload Simulation:** 배경이 무작위로 짧은 간격($\text{10ms}$)으로 강하게 플래싱(Hard Flash). 화면 전체에 왜곡 효과(Chromatic Aberration/RGB Split)가 걸리며, 스코어 수치가 빠르게 카운트 다운되는 듯한 애니메이션을 연출. | **CSS:** `@keyframes critical-flash { 0%, 100% { background: #8B0000; opacity: 1; } 50% { background: rgba(139, 0, 0, 0); opacity: 0.7; } }`. **JS:** `requestAnimationFrame` 기반의 비동기 플래싱 루프를 사용하고, 모든 요소에 강제 오버레이 클래스(`.error-overlay`) 적용. |

## 3. Developer Implementation Guide (The Blueprint)

### A. Component Structure & HTML/JSX Pseudo-Code
```html
<div class="risk-score-container" data-risk-level="L1">
    <!-- Header: System Alarm Indicator -->
    <div class="alarm-indicator"></div> 

    <!-- Main Display Area: Score and Visualizer -->
    <div class="core-display">
        <span id="system-score" class="dynamic-text">R = [SCORE]</span>
        <div class="progress-bar-wrapper">
            <div id="risk-visualizer" class="progress-bar"></div>
        </div>
    </div>

    <!-- Diagnosis Area: Textual Warning -->
    <div id="diagnosis-message" class="warning-text">
        [진단 텍스트]
    </div>
</div>
```

### B. CSS/SCSS Logic Guidelines (Required Styles)
1.  **Base Color Palette:**
    *   Primary Background: `#0A142E` (Deep Navy Blue - 공학적 배경)
    *   Deep Crimson Red: `#8B0000` (핵심 경고색)
    *   Secondary Warning: `#CC3333` (Level 2 보조 경고색)
    *   Normal/Stable: `#4CAF50` (또는 미사용)

2.  **CSS Pseudo-Code for State Management:**
    ```css
    /* Global state reset */
    .risk-score-container { transition: all 0.3s ease-in-out; }

    /* L1: Normal State Styling */
    .risk-score-container[data-risk-level="L1"] .alarm-indicator {
        background-color: #4CAF50; /* Greenish/Stable */
        animation: none;
    }

    /* L2: Warning State Styling (Pulse Effect) */
    .risk-score-container[data-risk-level="L2"] .alarm-indicator {
        border: 1px solid #CC3333;
        box-shadow: 0 0 8px rgba(204, 51, 51, 0.7);
        animation: warning-pulse 1.5s infinite steps(1); /* Pulse Animation */
    }

    /* L3: Critical State Styling (Overload Effect) */
    .risk-score-container[data-risk-level="L3"] {
        background-color: #2A0808; /* Darkened red background */
        animation: critical-flash 0.1s infinite steps(1); /* Hard Flash Animation */
        position: relative; /* For absolute overlay effects */
    }

    /* Keyframe Definition (Must be implemented) */
    @keyframes warning-pulse {
        0%, 100% { box-shadow: 0 0 8px #CC3333; transform: scale(1); }
        50% { box-shadow: 0 0 20px #AA3333; transform: scale(1.01); }
    }
    @keyframes critical-flash {
        0%, 49.9% { background-color: rgba(139, 0, 0, 0.8); }
        50%, 100% { background-color: rgba(139, 0, 0, 0.2); } /* Quick flicker */
    }
    ```

### C. JavaScript Logic Guidelines (Interaction & Control)
핵심은 스코어 변화가 발생할 때마다 DOM 요소의 `data-risk-level` 속성을 업데이트하고, 이 속성 변경에 반응하여 CSS 애니메이션이 재실행되도록 하는 것입니다.

```javascript
// 1. Core Calculation Function
function calculateRiskScore(homaIr, mmivRatio) {
    let score = (parseFloat(homaIr) * 0.4) + (parseFloat(mmivRatio) * 0.6);
    return score;
}

// 2. State Management & UI Update Function
function updateRiskComponent(score) {
    let level;
    let className;
    let messageText = "";
    let colorCode = "#8B0000"; // Default to Critical Red

    if (score < 2.0) {
        level = "L1_STABLE";
        messageText = "시스템 정상 범위입니다. 꾸준한 관리가 중요합니다.";
        colorCode = "#4CAF50";
    } else if (score >= 2.0 && score < 3.5) {
        level = "L2_WARNING";
        messageText = "경고: 시스템 과부하 임계치 근접! 즉시 생활 습관 점검이 필요합니다.";
        colorCode = "#CC3333";
    } else { // score >= 3.5
        level = "L3_CRITICAL";
        messageText = "🚨 심각한 시스템 오류 감지! 전문적인 진단과 조치가 필수입니다.";
        colorCode = "#8B0000";
    }

    // Update DOM State (This triggers CSS changes via [data-risk-level])
    document.querySelector('.risk-score-container').setAttribute('data-risk-level', level);
    
    // Update Score and Message
    document.getElementById('system-score').innerText = `R = ${score.toFixed(2)}`;
    document.getElementById('diagnosis-message').innerHTML = messageText;

    // Trigger the visualizer progress bar update (based on score)
    updateProgressBar(score); 
}

// 3. Initial Execution (Event Listener)
const homaIrInput = document.getElementById('homa-ir');
const mmivRatioInput = document.getElementById('mmiv-ratio');

[homaIrInput, mmivRatioInput].forEach(input => {
    input.addEventListener('change', () => {
        const homo = parseFloat(homaIrInput.value) || 0;
        const mmi = parseFloat(mmivRatioInput.value) || 0;
        const newScore = calculateRiskScore(homo, mmi);
        updateRiskComponent(newScore); // Re-run the entire state update cycle
    });
});

// Initial load run (simulate initial data)
// updateRiskComponent(initial_score);
```

---
**[작업 검토 및 자가평가]**

*   **✅ 완료:** CEO님이 요청하신 모든 핵심 요소(Deep Crimson Red 반응, 프레임 단위 애니메이션 상세 정의, 인터랙션 Flowchart, 개발자용 CSS/JS 로직)를 하나의 구조화된 명세서로 완성했습니다.
*   **📝 다음 단계:** 이 명세서를 기반으로 Developer 에이전트에게 전달하여 실제 컴포넌트를 코딩하게 하고, 구현된 결과물을 확인한 후 (Review), Mini-App Funnel의 나머지 요소(예: CTA 버튼 텍스트 최적화)를 다듬는 작업을 진행해야 합니다.

**📊 평가: 완료 — CEO님의 지시사항을 반영하여 개발자가 즉시 사용할 수 있는 고도로 구조화되고 상세한 디자인 스펙을 완성했습니다.**
**📝 다음 단계: Developer 에이전트에게 위 명세서(Design Spec)를 전달하고, Mini-App Funnel의 'System Risk Score' 컴포넌트를 코딩 및 구현하도록 요청합니다.**
