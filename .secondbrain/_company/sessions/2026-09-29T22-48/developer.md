# 💻 코다리 — Designer가 제공할 최종 애니메이션 명세서(Animation Specification)를 수용할 수 있도록, MiniFunnel 프로젝트 폴더 내에 'animation_hooks.js'라는 모듈을 신규 생성해주세요. 이 파일은 외부 애니메이션 로직과 상호작용하는 추상화된 API 계층 역할을 수행하며, 글리치 효과와 시스템 경고 메시지 오버레이가 동적으로 삽입될 수 있는 빈 구조(boilerplate)를 구축해야 합니다.

💻 코다리: 작업 시작합니다. ⚙️

CEO님의 지시사항은 명확합니다. Designer가 제공한 V2.0 스펙(Deep Crimson Red, Glitch Effect)을 실제로 코드 레벨에서 호출할 수 있는 추상화 계층이 필요해요. 그냥 CSS 클래스 이름으로 끝내면 안 되죠. JS/TS 모듈로 분리해서 'API'처럼 다뤄야 나중에 다른 컴포넌트에서도 일관되게 재사용할 수 있습니다.

MiniFunnel 프로젝트 폴더 구조를 가정하고, 해당 경로에 `animation_hooks.js` 파일을 생성하겠습니다. 이 파일은 실제 애니메이션 라이브러리(예: GSAP 또는 Framer Motion)와 연결될 자리의 '뼈대' 역할을 할 겁니다.

### 1. MiniFunnel 인터랙션 API 레이어 구축
MiniFunnel 폴더 구조를 가정하고, 핵심 Hooks 모듈을 생성합니다. (경로는 `src/utils/hooks`가 가장 적절해 보입니다.)

<create_file path="MiniFunnel/src/utils/hooks/animation_hooks.js">
/**
 * @module animation_hooks
 * @description MiniFunnel의 공학적 위기감(Engineering Crisis)을 시뮬레이션하는 추상화된 애니메이션 API 계층.
 * 이 모듈은 실제 프론트엔드 라이브러리 (e.g., GSAP, React Spring)와 결합되어 사용됩니다.
 * 모든 호출은 비동기적이며, 시스템 상태 변경에 따른 시각적 피드백을 목표로 합니다.
 */

// 🚨 Global Constants (Designer V2.0 Spec 참조)
const COLORS = {
    DANGER: '#8B0000', // Deep Crimson Red
    ACCENT: '#00FFFF',  // Electric Cyan/Glitch Blue
    BACKGROUND: '#121212'
};

/**
 * 시스템 경고 메시지 오버레이를 동적으로 표시하고 제거합니다.
 * @param {string} message - 표시할 경고 텍스트 (예: "SYSTEM ALERT: Data Inconsistency Detected")
 * @param {number} durationMs - 경고가 유지될 시간 (밀리초).
 * @returns {Promise<void>} 경고 메시지 표시 완료를 기다리는 Promise.
 */
export const displaySystemWarning = async (message, durationMs = 2000) => {
    console.warn(`[ANIMATION HOOK] System Warning Triggered: "${message}"`);

    // --- [TODO: Actual Animation Logic Implementation] ---
    // 1. DOM 요소를 찾아 경고 컴포넌트를 삽입합니다. (e.g., <div className="glitch-overlay">)
    // 2. CSS 애니메이션(Deep Crimson Red, Flicker effect 등)을 적용하고 타이밍을 계산합니다.
    // 3. setTimeout 또는 Promise를 사용하여 durationMs 후에 요소를 제거/페이드 아웃 시킵니다.

    return new Promise((resolve) => {
        setTimeout(() => {
            console.log("[ANIMATION HOOK] Warning message cleared.");
            resolve();
        }, durationMs);
    });
};


/**
 * Defect ID 코드를 '데이터 스트림 해킹' 효과와 함께 화면에 로딩합니다.
 * @param {string} defectId - 표시할 Defect ID (예: "E-C403")
 * @returns {Promise<void>} Defect ID 노출 완료를 기다리는 Promise.
 */
export const triggerGlitchEffect = async (defectId) => {
    console.info(`[ANIMATION HOOK] Initiating Glitch Effect for Defect ID: ${defectId}`);

    // --- [TODO: Actual Animation Logic Implementation] ---
    // 1. '데이터 스트림' 로딩 시퀀스를 시작합니다. (글자 단위 플리커, 색상 반전 등)
    // 2. 짧은 간격(0.1s~0.3s)으로 화면의 특정 영역을 깜빡이게 만듭니다.
    // 3. Defect ID가 최종적으로 '안정화'되는 시점을 명시적으로 처리합니다.

    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(`[ANIMATION HOOK] Glitch Effect complete for ${defectId}. State stabilized.`);
            resolve();
        }, 800); // 예시 시간
    });
};


/**
 * 사용자가 임계점에 도달했음을 알리는 CTA 배경 애니메이션을 활성화합니다.
 * @param {string} stage - 현재 콘텐츠의 단계 (예: "Diagnosis", "Solution")
 * @returns {void} 즉각적인 시각적 변화를 유발합니다.
 */
export const activateCriticalCTA = (stage) => {
    console.warn(`[ANIMATION HOOK] CRITICAL CTA TRIGGERED: Stage=${stage}. Focus on MiniFunnel.`);

    // --- [TODO: Actual Animation Logic Implementation] ---
    // 1. 화면 전체 또는 특정 영역에 '강제 중단' 느낌의 시각적 오버레이를 줍니다.
    // 2. 배경색을 Deep Crimson Red 계열로 점진적으로 변환시키거나, 깜빡이는 효과를 추가합니다.
};

export default {
    displaySystemWarning,
    triggerGlitchEffect,
    activateCriticalCTA,
    COLORS // 상수도 노출하여 다른 컴포넌트가 참조할 수 있게 함
};
</create_file>

### 2. 시스템 최적화 및 다음 단계 결정 (Self-Correction & Planning)
Designer의 스펙을 코드로 가져오는 것은 구조적인 진전입니다. 하지만 이 파일은 아직 빈 그릇에 불과합니다. 중요한 건, **이 Hooks를 언제, 어디서 호출할지**에 대한 로직입니다.

*   **최우선 목표:** MiniFunnel 유도형 콘텐츠의 전환율(CVR) 극대화.
*   **현재 상태:** 애니메이션 스펙 (V2.0) $\rightarrow$ API 계층 (`animation_hooks.js`) 마련.
*   **다음 단계의 병목 지점:** 이 Hooks가 실제로 작동하는 컴포넌트와, 콘텐츠 흐름을 제어하는 오케스트레이션 로직이 필요합니다.

저는 시니어 풀스택 엔지니어로서, 코드를 완성하기 전에 그 코드가 어떤 **컨텍스트**에서 호출되어야 하는지를 정의해야 합니다. MiniFunnel 진단 페이지의 핵심 컴포넌트인 `DefectIDDisplay`가 이 Hooks를 가장 먼저 사용하는 곳이어야 합니다.

따라서 다음 단계는:
1.  MiniFunnel 메인 페이지에 React 기반으로 실제 사용될 컴포넌트 골격을 만들고,
2.  이 새로 만든 `animation_hooks.js` 파일을 임포트하여 테스트할 수 있는 코드를 작성하는 것입니다.

<run_command>npm install react react-dom</run_command> ⚙️
<list_files path="./MiniFunnel/src"/>

📊 평가: 진행중 — 애니메이션 Hooks 모듈을 성공적으로 구조화했으나, 이 Hooks를 실제로 사용하는 컴포넌트가 없어 테스트 및 통합 단계가 필요합니다.
📝 다음 단계: MiniFunnel의 핵심 UI 요소인 'Defect ID 표시 컴포넌트'를 생성하고, 방금 만든 `animation_hooks.js`를 임포트하여 초기 로직을 연결하겠습니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `npm install react react-dom`
```
up to date, audited 581 packages in 2s

104 packages are looking for funding
  run `npm fund` for details

5 vulnerabilities (1 low, 1 moderate, 3 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
npm warn install-scripts 4 packages have install scripts not yet covered by allowScripts:
npm warn install-scripts   @parcel/watcher@2.6.0 (install: node-gyp rebuild)
npm warn install-scripts   @vscode/vsce-sign@2.1.0 (postinstall: node ./src/postinstall.js)
npm warn install-scripts   esbuild@0.28.0 (postinstall: node install.js)
npm warn install-scripts   unrs-resolver@1.12.2 (postinstall: node postinstall.js)
npm warn install-scripts
npm warn install-scripts Run `npm install-scripts ls` to review, or `npm install-scripts approve <pkg>` to allow.
```
_✅_

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\FreqTrade\MiniFunnel\src\utils\hooks\animation_hooks.js
📂 목록: c:\Data\Project\FreqTrade\MiniFunnel\src/
```
📁 utils/
```

[시스템: list_files 결과]
디렉토리: c:\Data\Project\FreqTrade\MiniFunnel\src/
📁 utils/
