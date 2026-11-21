# 💻 코다리 — MiniFunnel의 핵심 트래픽 유입처인 'Defect ID 시스템 진단 보고서 페이지'를 최종적으로 구현해주세요. 이 페이지는 Designer가 확정한 '오류 코드 기반 전문 진단 UI/UX'와 현빈이 설계한 제휴 마케팅(쿠팡 파트너스 등) 수익화 로직을 완벽하게 통합해야 합니다. 반드시 상태 전이(State Transition)에 따른 에러 핸들링과 AOV 최적화 플로우를 포함하여 E2E 테스트가 가능한 형태로 코드를 작성하고, git 브랜치로 관리해주세요.

💻 코다리: 작업 시작합니다.

CEO 지시사항은 이 MiniFunnel의 핵심 수익화 경로를 완성하는 가장 중요한 작업입니다. 'Defect ID 시스템 진단 보고서 페이지'는 단순히 UI를 보여주는 곳이 아니라, 사용자의 위기감을 극대화하고 상태 전이를 통해 자연스럽게 고가 제품(AOV 최적화)으로 유도해야 하는 **핵심 비즈니스 로직의 집합체**입니다.

코드 한 줄이라도 그냥 넘길 수 없습니다. 요구하신 대로, Designer님이 확정한 UI/UX와 Hyunbin님의 수익화 로직을 통합하고, 상태 전이 기반의 E2E 테스트가 가능한 구조로 코드를 설계하겠습니다. ⚙️

우선, 현재 작업 대상 파일인 `DefectReportPage.tsx`의 기존 내용을 파악하여 어떤 구조 위에서 작업을 시작해야 할지 확인하는 것이 필수입니다.

<read_file path="c:\Data\Project\connect-ai\src\components\DefectReportPage.tsx"/>


---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\src\components\DefectReportPage.tsx (212줄, 8.2KB)
```
 1	import React, { useState, useReducer, useCallback } from 'react';
 2	import './DefectReportPage.css'; // CSS 파일 분리 (가정)
 3	
 4	// --- 1. 타입 정의 및 상수 설정 ---
 5	
 6	/** Defect ID 상태 코드 */
 7	type DefectCode = 'E-C403' | 'M-S7D' | 'P-T2A';
 8	
 9	/** 페이지의 전체 상태 머신 (State Machine) */
10	interface PageState {
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\src\components\DefectReportPage.tsx (212줄)
```
  1	import React, { useState, useReducer, useCallback } from 'react';
  2	import './DefectReportPage.css'; // CSS 파일 분리 (가정)
  3	
  4	// --- 1. 타입 정의 및 상수 설정 ---
  5	
  6	/** Defect ID 상태 코드 */
  7	type DefectCode = 'E-C403' | 'M-S7D' | 'P-T2A';
  8	
  9	/** 페이지의 전체 상태 머신 (State Machine) */
 10	interface PageState {
 11	  currentStep: number; // 1, 2, or 3
 12	  diagnosisCompleted: boolean;
 13	  paymentStatus: 'idle' | 'processing' | 'success' | 'failed';
 14	  retryAttempt: number;
 15	  isLocked: boolean; // MiniFunnel CTA가 활성화되는지 여부
 16	}
 17	
 18	/** 상태 전이 액션 타입 */
 19	type Action = 
 20	  | { type: 'DIAGNOSE_SUCCESS'; code: DefectCode } 
 21	  | { type: 'ATTEMPT_PAYMENT' } 
 22	  | { type: 'SET_STATUS'; status: typeof PageState['paymentStatus'] }
 23	  | { type: 'RESET_PAGE' };
 24	
 25	// --- 2. 상태 리듀서 (Business Logic Core) ---
 26	
 27	/** 
 28	 * DefectReportPage의 핵심 상태 로직을 관리합니다. 
 29	 * UI와 비즈니스 규칙(상태 전이, 결제 실패 처리)을 분리하는 것이 핵심입니다.
 30	 */
 31	const initialState: PageState = {
 32	  currentStep: 1, // S1: Diagnosis & Alert
 33	  diagnosisCompleted: false,
 34	  paymentStatus: 'idle',
 35	  retryAttempt: 0,
 36	  isLocked: false,
 37	};
 38	
 39	function reportReducer(state: PageState, action: Action): PageState {
 40	  switch (action.type) {
 41	    case 'DIAGNOSE_SUCCESS':
 42	      // S1 -> S2로의 상태 전이 로직
 43	      return { 
 44	        ...state, 
 45	        currentStep: 2, 
 46	        diagnosisCompleted: true, 
 47	        isLocked: false // 결제는 아직 시도 안 했으므로 잠금 해제
 48	      };
 49	
 50	    case 'ATTEMPT_PAYMENT':
 51	      // 결제 시도 시작 -> 상태만 업데이트하고 실제 처리는 외부 API 호출 함수에서 진행
 52	      return { 
 53	        ...state, 
 54	        paymentStatus: 'processing', 
 55	        retryAttempt: state.retryAttempt + 1,
 56	        isLocked: true // 결제 중에는 인터랙션 잠금
 57	      };
 58	
 59	    case 'SET_STATUS':
 60	      // API 결과에 따라 상태 업데이트 (성공 또는 실패)
 61	      return { ...state, paymentStatus: action.status };
 62	
 63	    case 'RESET_PAGE':
 64	      // 페이지 초기화
 65	      return initialState;
 66	
 67	    default:
 68	      return state;
 69	  }
 70	}
 71	
 72	// --- 3. API 시뮬레이션 및 복원력 로직 (Resilience Module) ---
 73	
 74	/**
 75	 * 가짜 결제 API 호출을 시뮬레이션합니다.
 76	 * 실제 환경에서는 Axios/Fetch와 함께 try...catch 블록으로 감싸야 합니다.
 77	 * 이 함수는 '복구 프로토콜'의 핵심이며, 실패 시 재시도 로직을 포함해야 합니다.
 78	 */
 79	const simulatePaymentApiCall = async (amount: number): Promise<boolean> => {
 80	  let attemptCount = 0;
 81	  const MAX_RETRIES = 3;
 82	
 83	  while (attemptCount < MAX_RETRIES) {
 84	    attemptCount++;
 85	    console.log(`[API Call] Payment Attempt #${attemptCount} for ${amount} KRW.`);
 86	
 87	    // 실제 API 호출이 실패할 확률 시뮬레이션 (예: 네트워크 오류, 서버 과부하 등)
 88	    // 1회차(Attempt #1)와 2회차(Attempt #2)는 강제 실패하도록 설정하여 백오프 테스트 유도.
 89	    if (attemptCount <= 2 && Math.random() < 0.8) { // 높은 확률로 실패 가정
 90	      console.error(`[API Error] Connection failed or transaction rejected on attempt ${attemptCount}.`);
 91	      
 92	      // --- BACKOFF 로직 구현 (핵심!) ---
 93	      const delayTime = Math.pow(2, attemptCount - 1) * 1000; // 2초, 4초, 8초... 백오프
 94	      console.log(`[Recovery Protocol] Retrying in ${delayTime / 1000} seconds...`);
 95	      await new Promise(resolve => setTimeout(resolve, delayTime));
 96	      
 97	      continue; // 실패했으니 재시도
 98	    } else {
 99	      // 성공 시뮬레이션 (3번째 이후 또는 초기 조건 충족 시)
100	      console.log(`[API Success] Transaction successful on attempt ${attemptCount}!`);
101	      return true; 
102	    }
103	  }
104	  // 모든 재시도가 실패했을 경우 최종적으로 false 반환
105	  return false;
106	};
107	
108	// --- 4. 메인 컴포넌트 ---
109	
110	interface DefectReportPageProps {
111	  initialDefectCode: DefectCode;
112	}
113	
114	const DefectReportPage: React.FC<DefectReportPageProps> = ({ initialDefectCode }) => {
115	  const [state, dispatch] = useReducer(reportReducer, initialState);
116	  const handleDiagnosisSuccess = useCallback(() => {
117	    dispatch({ type: 'DIAGNOSE_SUCCESS', code: initialDefectCode });
118	  }, [initialDefectCode]);
119	
120	  // 결제 처리 핸들러 (가장 복잡한 부분)
121	  const handlePurchaseAttempt = async () => {
122	    if (state.paymentStatus === 'processing') return; // 이미 처리 중이면 무시
123	    
124	    dispatch({ type: 'ATTEMPT_PAYMENT' });
125	
126	    try {
127	      // 1. API 호출 시뮬레이션 실행 (백오프 로직 포함)
128	      const success = await simulatePaymentApiCall(99000); // 예시 금액
129	      
130	      // 2. 최종 결과에 따른 상태 전이 처리
131	      if (success) {
132	        dispatch({ type: 'SET_STATUS', status: 'success' });
133	        alert("✅ 복구 프로토콜 활성화! 결제가 성공적으로 완료되었습니다.");
134	      } else {
135	        dispatch({ type: 'SET_STATUS', status: 'failed' });
136	        alert("🚨 치명적 오류 발생. 모든 재시도에 실패했습니다. 고객센터를 이용해주세요.");
137	      }
138	    } catch (error) {
139	      console.error("Critical failure during payment process:", error);
140	      dispatch({ type: 'SET_STATUS', status: 'failed' });
141	    }
142	  };
143	
144	  // --- 5. UI 렌더링 로직 분리 (가독성 및 SRP 준수) ---
145	
146	  const renderStepOne = () => (
147	    <div className="system-alert">
148	      <h2>⚠️ 시스템 오류 경고: Defect Code {initialDefectCode} 감지</h2>
149	      <p>현재의 상태는 일반적인 피로도가 아닙니다. 이는 전문 진단이 필요한 **시스템 레벨의 치명적 결함**입니다.</p>
150	      {/* ... 추가 위기감 조성 콘텐츠 (Writer/Designer 브리프 활용) ... */}
151	      <button onClick={handleDiagnosisSuccess} className="btn-primary">진단 보고서 열람 및 다음 단계로 이동 ⚙️</button>
152	    </div>
153	  );
154	
155	  const renderStepTwo = () => (
156	    <div className="necessity-proof-section">
157	      <h2>🔬 진단 결과: 전문적인 개입이 필수적입니다.</h2>
158	      <p>자가진단만으로는 근본 원인을 파악할 수 없습니다. 저희 MiniFunnel의 **'패치 프로토콜'**을 통해 정확한 복구 경로를 설정해야 합니다.</p>
159	      {/* ... 데이터 기반 증명 콘텐츠 (Defect ID와 관련된 통계 자료) ... */}
160	    </div>
161	  );
162	
163	  const renderStepThree = () => {
164	    let statusMessage = '';
165	    if (state.paymentStatus === 'processing') {
166	      statusMessage = `처리 중입니다... (${state.retryAttempt}/3 시도). 안정성을 위해 잠시만 기다려주세요.`;
167	    } else if (state.paymentStatus === 'success') {
168	      statusMessage = '🎉 복구 프로토콜 활성화 완료! 고객님의 시스템은 정상화 단계에 진입했습니다.';
169	    } else if (state.paymentStatus === 'failed') {
170	      statusMessage = '❌ 결제 처리 실패. 저희가 2차 지원을 요청드립니다. 담당자에게 문의하세요.';
171	    } else {
172	      statusMessage = '구매를 진행하여 시스템 복구 프로토콜을 활성화해주세요.';
173	    }
174	
175	    return (
176	      <div className="purchase-protocol-section">
177	        <h3>✅ MiniFunnel 패치 프로토콜 실행</h3>
178	        <p>{statusMessage}</p>
179	        {/* 결제 버튼은 상태에 따라 비활성화/활성화 */}
180	        <button 
181	          onClick={handlePurchaseAttempt} 
182	          disabled={state.paymentStatus === 'processing' || state.isLocked}
183	          className={`btn-cta ${state.paymentStatus === 'success' ? 'active' : ''}`}
184	        >
185	          {state.paymentStatus === 'processing' ? '🔄 복구 중...' : (
186	            `[필수 패치 실행] ${99000.toLocaleString()}원 결제 시도`
187	          )}
188	        </button>
189	      </div>
190	    );
191	  };
192	
193	  // --- 6. 최종 JSX 반환 ---
194	  return (
195	    <div className="defect-report-container">
196	      <h1>[온현] 시스템 진단 보고서</h1>
197	      <div className="step-indicator">
198	        Step {state.currentStep} / 3 ({['진단', '필요성 증명', '패치 프로토콜'][state.currentStep - 1]})
199	      </div>
200	
201	      <section className="content-area">
202	        {/* State Machine에 따라 다른 컴포넌트 렌더링 */}
203	        {state.currentStep === 1 && renderStepOne()}
204	        {state.currentStep === 2 && renderStepTwo()}
205	        {state.currentStep >= 3 && renderStepThree()}
206	      </section>
207	
208	    </div>
209	  );
210	};
211	
212	export default DefectReportPage;
```
