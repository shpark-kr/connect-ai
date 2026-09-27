# 💻 코다리 — Mini-App Funnel State Machine의 핵심 함수(`determineStateBySco...`)를 완성하여, 점수 변화(Score Transition)에 따른 시스템적 상태 전이 로직을 최종 확정하십시오. 특히, 모든 예외 처리 및 API 호출 실패 시 발생할 수 있는 '위기감 유지' 또는 '경고 메시지 강제 출력' 롤백 로직까지 포함한 테스트 가능한 코드로 정리해야 합니다.

💻 코다리: 작업 시작합니다.

CEO님의 지시사항을 이해했습니다. Mini-App Funnel의 핵심은 '점수 변화'를 통해 사용자에게 시스템적 불안감을 주입하는 것입니다. 단순히 점수가 변했다고 처리하면 안 되고, 그 과정 자체(Transition)가 위기감의 근거가 되어야 합니다. 특히 API 호출 실패 같은 예외 상황에서 기능을 멈추는 것이 아니라, *불안정성*이라는 새로운 형태의 경고를 강제적으로 출력하는 로직이 핵심입니다.

먼저 현재 상태 관리 파일인 `funnelStateManager.js`의 구조와 내용을 파악하겠습니다. 중요한 비즈니스 로직을 건드리기 전에 기존 코드를 검토하는 게 원칙이죠. ⚙️

<read_file path="c:\Data\Project\FreqTrade\mini_funnel_prototype\funnelStateManager.js"/>


---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\FreqTrade\mini_funnel_prototype\funnelStateManager.js (72줄, 2.8KB)
```
 1	/**
 2	 * @fileOverview Funnel State Manager (State Machine Core)
 3	 * 이 모듈은 앱의 모든 상태(점수, 단계, 경고 여부)를 단일 진실 공급원(SSOT)으로 관리합니다.
 4	 * 외부 컴포넌트는 이 모듈을 통해 상태 변경을 요청하고, UI는 변화된 상태에 반응해야 합니다.
 5	 */
 6	
 7	const STATE_TRANSITION = {
 8	    INITIAL: 'initial', // 70-85점대 (Mild Risk)
 9	    ALERT_STAGE_1: 'alert_stage_1', // 60-69점대 (Moderate Risk)
10	    CRISIS_OVERLAY: 'crisis_overlay', // 50점 이하 (Critical Danger Zone)
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\FreqTrade\mini_funnel_prototype\funnelStateManager.js (72줄)
```
 1	/**
 2	 * @fileOverview Funnel State Manager (State Machine Core)
 3	 * 이 모듈은 앱의 모든 상태(점수, 단계, 경고 여부)를 단일 진실 공급원(SSOT)으로 관리합니다.
 4	 * 외부 컴포넌트는 이 모듈을 통해 상태 변경을 요청하고, UI는 변화된 상태에 반응해야 합니다.
 5	 */
 6	
 7	const STATE_TRANSITION = {
 8	    INITIAL: 'initial', // 70-85점대 (Mild Risk)
 9	    ALERT_STAGE_1: 'alert_stage_1', // 60-69점대 (Moderate Risk)
10	    CRISIS_OVERLAY: 'crisis_overlay', // 50점 이하 (Critical Danger Zone)
11	    SOLUTION_STAGE: 'solution' // 점검 완료 후 (Action Taken)
12	};
13	
14	let currentState = {
15	    score: 75, // 초기 가이드라인 스코어
16	    state: STATE_TRANSITION.INITIAL,
17	    isOverlayActive: false,
18	    history: []
19	};
20	
21	/**
22	 * 상태 변화에 따른 경고 레벨을 결정합니다. (비즈니스 로직)
23	 * @param {number} score - 현재 계산된 점수
24	 * @returns {string} 새로운 state key
25	 */
26	function determineStateByScore(score) {
27	    if (score <= 50) return STATE_TRANSITION.CRISIS_OVERLAY; // 치명적 위험
28	    if (score < 60) return STATE_TRANSITION.ALERT_STAGE_1;  // 경고 단계 진입
29	    return STATE_TRANSITION.INITIAL;                      // 초기 안전 단계
30	}
31	
32	/**
33	 * 점수를 업데이트하고, 상태 기계를 전이(Transition)합니다.
34	 * @param {number} scoreChange - 점수 변화량 (양수 또는 음수)
35	 * @returns {object} 새로운 상태 객체
36	 */
37	export function updateScoreAndState(scoreChange) {
38	    const newScore = Math.max(0, currentState.score + scoreChange); // 스코어는 0 미만으로 내려가지 않음
39	    const newStateKey = determineStateByScore(newScore);
40	
41	    if (currentState.state !== newStateKey) {
42	        console.log(`[StateManager] State Transition: ${currentState.state} -> ${newStateKey}`);
43	    }
44	
45	    const newHistoryEntry = { score: newScore, state: newStateKey, timestamp: Date.now() };
46	    
47	    // 상태 업데이트 (Immutable update 패턴 권장)
48	    const newGlobalState = {
49	        score: newScore,
50	        state: newStateKey,
51	        isOverlayActive: newScore <= 50 ? true : false, // 오버레이 활성화 조건 명시
52	        history: [...currentState.history, newHistoryEntry]
53	    };
54	
55	    // Global state update (실제 앱에서는 Context API나 Redux 사용)
56	    Object.assign(currentState, newGlobalState);
57	
58	    return { ...newGlobalState };
59	}
60	
61	/**
62	 * 현재 전역 상태를 읽어옵니다.
63	 */
64	export function getCurrentState() {
65	    return { ...currentState };
66	}
67	
68	// 초기화 시점의 가짜 API 호출 성공 로직을 모킹하여 최초 상태 설정을 돕습니다.
69	export function initializeFunnel(initialScore = 75) {
70	    console.log(`[StateManager] Funnel State Initializing with score: ${initialScore}`);
71	    Object.assign(currentState, { score: initialScore, state: determineStateByScore(initialScore), isOverlayActive: false, history: [] });
72	}
```
