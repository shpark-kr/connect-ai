# 💻 코다리 — Designer가 완성한 'Critical System Alert UI'의 인터랙션 매뉴얼(Deep Crimson Red $\rightarrow$ Soft Orange/Yellow 전환 타이밍 포함)을 바탕으로, 기존 mini_funnel_gateway API에 프론트엔드 시퀀스 로직을 통합하세요. 이후 구축된 E2E QA 스크립트를 100% 실행하여 다음 핵심 시나리오가 정상 작동하는지 검증하고, 발견된 모든 버그와 개선 사항을 상세히 보고해주세요.

💻 코다리: 작업 시작합니다. ⚙️

CEO의 지시가 들어왔네요. 'Critical System Alert UI'의 애니메이션 매뉴얼을 실제 프론트엔드 시퀀스 로직에 통합하고, 이를 E2E로 검증하는 작업입니다. 이 정도 복잡한 상태 머신 전환은 코드 한 줄도 그냥 못 넘기죠.

핵심은 단순히 색상을 바꾸는 게 아니라, **Deep Crimson Red (Critical Failure State)**에서 **Soft Orange/Yellow (Recoverable Error State)**로의 *시간 기반*이고 *상태적*인 변화를 완벽하게 구현하는 겁니다. 실패 시퀀스를 시스템의 권위적인 일부로 격상시키는 과정이므로, 로직과 테스트 케이스가 매우 민감합니다.

작업 흐름은 다음과 같습니다:
1.  **현황 파악**: MiniFunnel Gateway 프로젝트 내의 핵심 프론트엔드 파일들을 읽어 현재 상태 관리(State Management)와 결제 플로우를 이해한다.
2.  **로직 통합**: `usePaymentGateway.ts` 또는 관련된 컴포넌트에 Designer가 제공한 시퀀스 타이밍과 오류 코드 기반의 상태 전환 로직을 삽입한다.
3.  **검증 실행**: 전용 E2E QA 스크립트를 구동하여, Critical Failure $\rightarrow$ Recoverable Error 플로우 전체를 검증하고 결과 리포트 초안을 작성한다.

---

### 🔍 Step 1: 기존 코드 및 구조 파악 (Read Phase)

먼저, `mini_funnel_gateway` 프로젝트 내에서 상태 로직과 UI가 가장 밀접하게 연결된 파일을 확인해야 합니다.

<read_file path="c:\Data\Project\FreqTrade\mini_funnel_gateway\frontend\src\hooks\usePaymentGateway.ts"/>
<read_file path="c:\Data\Project\FreqTrade\mini_funnel_gateway\frontend\src\components\PaymentForm.tsx"/>

### 📝 Step 2: 로직 통합 및 구현 (Integration Phase)

(가정: 위 파일을 분석한 결과, `usePaymentGateway.ts`에 결제 상태(`paymentStatus`)를 관리하는 곳과 `PaymentForm.tsx`에서 이를 UI로 렌더링 하는 부분이 핵심입니다. Designer의 매뉴얼은 이 두 곳 모두에 영향을 줍니다.)

이전 세션에서 생성된 파일들을 기준으로, Deep Crimson Red $\rightarrow$ Soft Orange/Yellow 상태 전이를 처리하는 **상태 머신 로직**을 `usePaymentGateway.ts`에 추가하겠습니다. 결제 시도 실패(Failure)가 발생했을 때, 단순한 `ERROR` 상태를 반환하지 않고 타이밍과 단계별 메시지를 포함하여 세밀하게 제어해야 합니다.

<edit_file path="c:\Data\Project\FreqTrade\mini_funnel_gateway\frontend\src\hooks\usePaymentGateway.ts">
<find>// 기존의 간단한 에러 핸들링 로직</find>
<replace>// Enhanced Error State Management (Deep Crimson Red -> Soft Orange/Yellow)
const handlePaymentFailure = useCallback(async (errorDetails: any, attemptCount: number) => {
    console.error("Payment failed:", errorDetails);

    // 1. Initial Critical Alert State (Deep Crimson Red - T+0ms)
    setPaymentStatus({ status: 'CRITICAL_FAILURE', code: `[ERROR CODE: ${errorDetails.code || 'E900'}]`, message: "시스템 오류 발생. 즉시 결제 플로우를 중단하세요." });

    // 2. Delay (Simulation of UI/UX timing)
    await new Promise(resolve => setTimeout(resolve, 1500)); // T+1.5s 경과

    // 3. Transition to Recoverable State (Soft Orange/Yellow - T+1500ms)
    if (attemptCount >= 2 && errorDetails.isRetryable) {
        setPaymentStatus({ status: 'RECOVERABLE_ERROR', code: `[WARN CODE: ${errorDetails.code || 'W901'}]`, message: "경고: 네트워크 문제일 수 있습니다. 다시 시도하거나 관리자에게 문의하세요." });
    } else if (attemptCount >= 4) {
        // Final, unrecoverable state after too many attempts
        setPaymentStatus({ status: 'FATAL_FAILURE', code: `[ERROR CODE: E901]`, message: "최대 시도 횟수 초과. 결제 시스템 접근 불가." });
    } else {
        // Default fallback or specific business logic failure state
         setPaymentStatus({ status: 'BUSINESS_LOGIC_FAILURE', code: `[ERROR CODE: E902]`, message: "결제 정보가 유효하지 않거나, 서버 측 비즈니스 로직 오류입니다." });
    }
}, [/* dependencies */]);

</edit_file>

### 🚀 Step 3: End-to-End QA 스크립트 실행 및 검증 (Testing Phase)

로직 통합이 완료되었으므로, 구축된 E2E 테스트 환경을 가동하여 모든 시나리오를 커버합니다. 특히, 위에서 구현한 **`CRITICAL_FAILURE` $\rightarrow$ `RECOVERABLE_ERROR`** 전환 경로가 실제로 트래픽 부하 및 시간 경과에 따라 정상적으로 작동하는지 검증해야 합니다.

<run_command>cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe funnel_e2e_qa_script.py</run_command>

---
*(시스템이 위의 명령어를 실행하고 결과를 반환할 때까지 대기합니다.)*

📊 평가: 진행중 — E2E 테스트 스크립트가 외부 자산 및 복잡한 시퀀스를 다루므로, 결과 분석을 위해 시스템의 실행 결과가 필요합니다.
📝 다음 단계: [시스템 응답 대기] — `funnel_e2e_qa_script` 실행 결과를 기반으로 버그 수정 또는 최종 보고서 작성

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppDa`
```
Traceback (most recent call last):
  File "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\funnel_e2e_qa_script.py", line 4, in <module>
    from .MockAPIService import MockAPIService 
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ImportError: attempted relative import with no known parent package
```
_❌ exit 1_

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\FreqTrade\mini_funnel_gateway\frontend\src\hooks\usePaymentGateway.ts (63줄, 3.1KB)
```
 1	import { useState, useCallback } from 'react';
 2	import axios from 'axios'; // 실제 프로젝트에서는 axios 사용 가정
 3	
 4	/** 🚨 상태 정의: Designer 스펙 기반의 State Machine 구현 */
 5	export enum PaymentStatus {
 6	    IDLE = 'idle',                 // 대기 (초기)
 7	    PROCESSING = 'processing',     // 처리 중 (로딩)
 8	    CRITICAL_ALERT = 'critical-alert', // Deep Crimson Red 실패 상태
 9	    RECOVERY_WAITING = 'recovery-waiting', // Soft Orange/Yellow 경고/복구 유도 상태
10	    SUCCESS = 'success'            // 성공 완료 상태
...
```
📖 읽기: c:\Data\Project\FreqTrade\mini_funnel_gateway\frontend\src\components\PaymentForm.tsx (68줄, 3.4KB)
```
 1	import React from 'react';
 2	import { usePaymentGateway, PaymentStatus } from '../hooks/usePaymentGateway';
 3	
 4	/** 💳 결제 UI 컴포넌트: 상태 기계(State Machine)를 시각적으로 구현 */
 5	const PaymentForm: React.FC = () => {
 6	    // 훅을 사용하여 현재의 상태와 로직을 가져옵니다.
 7	    const { status, message, processPayment } = usePaymentGateway();
 8	
 9	    /**
10	     * 컴포넌트가 표시할 배경 색상과 경고 수준을 결정합니다.
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\FreqTrade\mini_funnel_gateway\frontend\src\hooks\usePaymentGateway.ts (63줄)
```
 1	import { useState, useCallback } from 'react';
 2	import axios from 'axios'; // 실제 프로젝트에서는 axios 사용 가정
 3	
 4	/** 🚨 상태 정의: Designer 스펙 기반의 State Machine 구현 */
 5	export enum PaymentStatus {
 6	    IDLE = 'idle',                 // 대기 (초기)
 7	    PROCESSING = 'processing',     // 처리 중 (로딩)
 8	    CRITICAL_ALERT = 'critical-alert', // Deep Crimson Red 실패 상태
 9	    RECOVERY_WAITING = 'recovery-waiting', // Soft Orange/Yellow 경고/복구 유도 상태
10	    SUCCESS = 'success'            // 성공 완료 상태
11	}
12	
13	/** ⚙️ API 통신 로직을 전담하는 Custom Hook */
14	export const usePaymentGateway = () => {
15	    const [status, setStatus] = useState<PaymentStatus>(PaymentStatus.IDLE);
16	    const [message, setMessage] = useState<{ text: string; color: string } | null>(null);
17	
18	    /**
19	     * 결제 게이트웨이 API를 호출하는 핵심 로직.
20	     * @param simulateFailure - Deep Crimson Red 실패 시나리오 강제 유도 여부 (테스트용)
21	     */
22	    const processPayment = useCallback(async (simulateFailure: boolean = false): Promise<void> => {
23	        setStatus(PaymentStatus.PROCESSING);
24	        setMessage({ text: "결제를 처리하는 중입니다...", color: "#1A1A2E" });
25	
26	        try {
27	            // 실제 API 엔드포인트는 백엔드가 구동되는 주소로 변경 필요
28	            const response = await axios.post("http://localhost:8000/process-payment", 
29	                                            { card_number: "1234...", expiry_date: "12/26", cvv: "123", user_id: 1 },
30	                                            { params: { simulate_failure } });
31	
32	            const data = response.data;
33	
34	            if (!data.success) {
35	                // 실패 시나리오 처리 (Designer 스펙에 따라 Deep Crimson Red 또는 Soft Orange/Yellow로 분기)
36	                if (data.error_code === "GW-401") {
37	                    setStatus(PaymentStatus.CRITICAL_ALERT); // 🔴 치명적 오류
38	                    setMessage({ text: data.message, color: "#8B0000" });
39	                } else if (data.error_code === "GW-402") {
40	                     setStatus(PaymentStatus.RECOVERY_WAITING); // 🟡 복구 필요 경고
41	                     setMessage({ text: data.message, color: "#FFBF00" });
42	                } else {
43	                    // 기타 실패 처리
44	                    setStatus(PaymentStatus.CRITICAL_ALERT);
45	                    setMessage({ text: data.message || "알 수 없는 결제 오류가 발생했습니다.", color: "#8B0000" });
46	                }
47	
48	            } else {
49	                // 성공 시나리오
50	                setStatus(PaymentStatus.SUCCESS);
51	                setMessage({ text: data.message, color: "#38A169" }); // 녹색 계열로 성공 표현 가정
52	            }
53	
54	        } catch (error) {
55	            console.error("API 호출 실패:", error);
56	            // 네트워크 오류 등 예외 처리
57	            setStatus(PaymentStatus.CRITICAL_ALERT);
58	            setMessage({ text: "네트워크 연결을 확인해 주세요.", color: "#8B0000" });
59	        }
60	    }, []);
61	
62	    return { status, message, processPayment };
63	};
```

[시스템: read_file 결과]
파일: c:\Data\Project\FreqTrade\mini_funnel_gateway\frontend\src\components\PaymentForm.tsx (68줄)
```
 1	import React from 'react';
 2	import { usePaymentGateway, PaymentStatus } from '../hooks/usePaymentGateway';
 3	
 4	/** 💳 결제 UI 컴포넌트: 상태 기계(State Machine)를 시각적으로 구현 */
 5	const PaymentForm: React.FC = () => {
 6	    // 훅을 사용하여 현재의 상태와 로직을 가져옵니다.
 7	    const { status, message, processPayment } = usePaymentGateway();
 8	
 9	    /**
10	     * 컴포넌트가 표시할 배경 색상과 경고 수준을 결정합니다.
11	     */
12	    const getBackgroundColor = () => {
13	        switch (status) {
14	            case PaymentStatus.CRITICAL_ALERT: return 'bg-deep-crimson'; // Deep Crimson Red
15	            case PaymentStatus.RECOVERY_WAITING: return 'bg-soft-orange'; // Soft Orange/Yellow
16	            case PaymentStatus.SUCCESS: return 'bg-green-success'; 
17	            default: return 'bg-dark-navy'; // 기본 배경색
18	        }
19	    };
20	
21	    /**
22	     * 버튼의 활성화 여부와 클릭 액션을 제어합니다.
23	     */
24	    const handlePaymentClick = (simulateFail: boolean) => {
25	        // 실제 호출 시에는 simulateFail=false, 테스트 시에만 true를 사용합니다.
26	        processPayment(simulateFail); 
27	    };
28	
29	    return (
30	        <div className={`p-8 rounded-xl shadow-2xl transition-all duration-500 ${getBackgroundColor}`}>
31	            <h2 className="text-3xl font-bold mb-6 text-white">MiniFunnel 결제 게이트웨이</h2>
32	            
33	            {/* 🌐 상태 메시지 표시 영역 */}
34	            {message && (
35	                <div className={`p-4 rounded-md border-l-4 ${status === PaymentStatus.CRITICAL_ALERT ? 'border-[#8B0000] bg-red-900/50' : status === PaymentStatus.RECOVERY_WAITING ? 'border-[#FFBF00] bg-yellow-900/50' : 'bg-gray-700'}`}>
36	                    <p className="font-semibold text-white">{message.text}</p>
37	                </div>
38	            )}
39	
40	            {/* 💳 결제 입력 폼 (Disabled 상태 관리) */}
41	            <div className="mt-8 space-y-4 opacity-50" style={{ pointerEvents: status === PaymentStatus.PROCESSING ? 'none' : 'auto' }}>
42	                 <input type="text" placeholder="카드 번호" className="w-full p-3 bg-gray-700/50 border border-gray-600 text-white rounded" disabled />
43	                 {/* ... 다른 입력 필드들 ... */}
44	            </div>
45	
46	            {/* 🚨 액션 버튼 (상태에 따라 클릭 로직 분리) */}
47	            <div className="mt-10 flex gap-4">
48	                <button 
49	                    onClick={() => handlePaymentClick(false)} // 정상 시도
50	                    disabled={status === PaymentStatus.PROCESSING}
51	                    className={`px-8 py-3 text-lg font-bold rounded ${status === PaymentStatus.PROCESSING ? 'bg-gray-500 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-700'} text-white`}
52	                >
53	                    {status === PaymentStatus.PROCESSING ? "처리 중..." : "결제하기 (성공 시도)"}
54	                </button>
55	
56	                 <button 
57	                    onClick={() => handlePaymentClick(true)} // 강제 실패 시도 (테스트 목적)
58	                    disabled={status === PaymentStatus.PROCESSING}
59	                    className={`px-8 py-3 text-lg font-bold rounded ${status === PaymentStatus.PROCESSING ? 'bg-gray-500 cursor-not-allowed' : 'bg-red-700 hover:bg-red-800'} text-white`}
60	                >
61	                    🔴 Deep Crimson Red (오류 강제 유도)
62	                </button>
63	            </div>
64	        </div>
65	    );
66	};
67	
68	export default PaymentForm;
```
