# 💻 코다리 — MiniFunnel MVP의 핵심 로직(위험 점수 계산 및 상태 변화)을 기반으로 단위 테스트(Unit Test) 코드를 작성하고, 전역 스타일 분리 및 데이터 바인딩이 적용된 최종 통합 버전의 `App.tsx` 프로토타입을 완성해주세요. 특히 '위기감 증폭' 시퀀스(Deep Navy $\rightarrow$ Dark Red)에 따른 상태 머신 로직과 입력값 유효성 검사까지 완벽하게 구현해야 합니다.

💻 코다리: 작업 시작합니다.

CEO 지시사항 잘 받았습니다. MiniFunnel MVP의 핵심은 단순히 UI를 구현하는 게 아니라, **불안감을 자극하여 전문적 권위를 확보하고 구매로 유도하는 '시스템 오류'라는 컨셉을 기술적으로 완벽하게 구현**하는 데 있습니다. 이 로직이 흔들리면 모든 마케팅 퍼널 자체가 무너집니다.

요구하신 작업은 단순히 `App.tsx`를 완성하는 것을 넘어, 핵심 비즈니스 로직(위험 점수 계산 및 상태 전이)을 분리하고 단위 테스트까지 완료해야 하는 고난도의 통합 프로젝트입니다. 특히 '위기감 증폭' 시퀀스(`Deep Navy` $\rightarrow$ `Dark Red`)는 단순한 스타일 변경이 아니라, **상태 머신(State Machine)**의 핵심 로직으로 작동해야 합니다.

저는 다음 3단계로 진행하겠습니다.
1.  **탐색 및 이해**: 현재 `App.tsx`의 구조를 파악합니다. (필수)
2.  **핵심 로직 분리 및 테스트**: 위험 점수 계산, 유효성 검사, 상태 전이 로직을 별도의 유틸리티 파일로 추출하고 단위 테스트 코드를 작성하여 안정성을 확보합니다.
3.  **통합 및 완성**: `App.tsx`를 리팩토링하여 분리된 로직과 전역 스타일링/데이터 바인딩을 적용한 최종 프로토타입을 완성합니다.

우선, 현재 작업 대상 파일의 내부 구조를 먼저 파악하겠습니다. 절대 추측으로 코드를 수정할 순 없으니까요.

<read_file path="C:\Users\USER\OnhyunProject\App.tsx"/>

📊 평가: 진행중 — 기존 코드 분석 후 핵심 로직을 분리하고 단위 테스트부터 시작해야 안전합니다.
📝 다음 단계: `App.tsx` 내용을 기반으로 위험 점수 계산 및 상태 전이 로직(State Machine)을 위한 별도의 유틸리티 파일(`src/utils/riskCalculator.ts`)을 생성하겠습니다.

---
## 📁 파일 액션 결과

📖 읽기: ~\OnhyunProject\App.tsx (163줄, 7.5KB)
```
 1	import React, { useState, useCallback } from 'react';
 2	import DefectInputForm from './components/DefectInputForm';
 3	import SystemRiskGauge from './components/SystemRiskGauge';
 4	// MiniFunnelPage는 최종 CTA 단계에서 사용될 것이므로 여기서는 제외합니다.
 5	
 6	/**
 7	 * @typedef {Object} DiagnosisInputs
 8	 * @property {string} symptom1 - 첫 번째 주요 증상 (예: 만성 피로)
 9	 * @property {number} yearsDiagnosed - 진단 기간 (연도)
10	 */
...
```

[시스템: read_file 결과]
파일: ~\OnhyunProject\App.tsx (163줄)
```
  1	import React, { useState, useCallback } from 'react';
  2	import DefectInputForm from './components/DefectInputForm';
  3	import SystemRiskGauge from './components/SystemRiskGauge';
  4	// MiniFunnelPage는 최종 CTA 단계에서 사용될 것이므로 여기서는 제외합니다.
  5	
  6	/**
  7	 * @typedef {Object} DiagnosisInputs
  8	 * @property {string} symptom1 - 첫 번째 주요 증상 (예: 만성 피로)
  9	 * @property {number} yearsDiagnosed - 진단 기간 (연도)
 10	 */
 11	
 12	// ---------------------------------------------------
 13	// CORE LOGIC: 위험 지수 계산 함수 (The Heart of the Funnel)
 14	// ---------------------------------------------------
 15	/**
 16	 * 사용자 입력 데이터를 기반으로 시스템의 위험 점수를 산출합니다.
 17	 * @param {DiagnosisInputs} inputs - 사용자가 입력한 진단 데이터
 18	 * @returns {{score: number, riskLevel: 'Low' | 'Medium' | 'Critical', bgColorClass: string}} 계산된 위험 지수와 스타일 정보
 19	 */
 20	const calculateRiskScore = (inputs) => {
 21	    if (!inputs || !inputs.symptom1) {
 22	        return { score: 0, riskLevel: 'Low', bgColorClass: 'bg-blue-900' }; // 기본값
 23	    }
 24	
 25	    let score = 0;
 26	    const symptomWeighting = {
 27	        "만성 피로": 35,
 28	        "관절 통증": 25,
 29	        "피부 탄력 저하": 15,
 30	        // 여기에 더 많은 증상에 대한 가중치를 추가할 수 있습니다.
 31	    };
 32	
 33	    // 1. 증상 기반 점수 합산 (가장 큰 가중치)
 34	    const symptomScore = symptomWeighting[inputs.symptom1] || 10; // 기본 최소점 부여
 35	    score += symptomScore;
 36	
 37	    // 2. 진단 기간 기반 점수 추가 (시간의 흐름에 따른 누적 위험 강조)
 38	    if (typeof inputs.yearsDiagnosed === 'number' && inputs.yearsDiagnosed >= 5) {
 39	        score += Math.min(10, Math.floor(inputs.yearsDiagnosed / 2)); // 5년 이상이면 최대 10점 추가
 40	    }
 41	
 42	    // 최종 점수 조정 및 클램핑 (최소 5점, 최대 100점)
 43	    const finalScore = Math.min(100, Math.max(5, score + Math.floor(Math.random() * 10))); // 무작위 노이즈 추가로 현실성 부여
 44	
 45	    let riskLevel: 'Low' | 'Medium' | 'Critical';
 46	    let bgColorClass: string;
 47	
 48	    if (finalScore >= 75) {
 49	        riskLevel = 'Critical';
 50	        bgColorClass = 'bg-red-900/80 border-red-700'; // Critical Red!
 51	    } else if (finalScore >= 40) {
 52	        riskLevel = 'Medium';
 53	        bgColorClass = 'bg-yellow-900/80 border-yellow-700'; // 경고 노랑
 54	    } else {
 55	        riskLevel = 'Low';
 56	        bgColorClass = 'bg-blue-900/80 border-blue-700'; // 정상 남색
 57	    }
 58	
 59	    return { score: finalScore, riskLevel, bgColorClass };
 60	};
 61	
 62	
 63	// ---------------------------------------------------
 64	// MAIN COMPONENT
 65	// ---------------------------------------------------
 66	const App = () => {
 67	    /** @type {[DiagnosisInputs | null, React.Dispatch<React.SetStateAction<DiagnosisInputs | null>>]} */
 68	    const [formData, setFormData] = useState(null);
 69	    const [diagnosisResult, setDiagnosisResult] = useState({ score: 0, riskLevel: 'Low', bgColorClass: 'bg-blue-900/80 border-blue-700' });
 70	    const [isLoading, setIsLoading] = useState(false);
 71	
 72	    // 입력값 변경 핸들러
 73	    const handleInputChange = useCallback((key, value) => {
 74	        setFormData(prev => ({ ...prev, [key]: value }));
 75	    }, []);
 76	
 77	
 78	    // 핵심 진단 로직 실행 (Button Click Handler)
 79	    const handleDiagnosisSubmit = () => {
 80	        if (!formData) return;
 81	
 82	        setIsLoading(true);
 83	        
 84	        // 1. 타이밍을 주어 Loading State를 경험하게 함 (UX 강제)
 85	        setTimeout(() => {
 86	            try {
 87	                // 2. 위험 점수 계산 실행
 88	                const result = calculateRiskScore(formData);
 89	                setDiagnosisResult(result);
 90	
 91	                // 3. 로딩 완료 후 상태 업데이트
 92	                setIsLoading(false);
 93	
 94	            } catch (error) {
 95	                console.error("진단 프로세스 중 오류 발생:", error);
 96	                alert("시스템 내부 오류가 감지되었습니다. 잠시 후 다시 시도해 주세요.");
 97	                setIsLoading(false);
 98	            }
 99	        }, 1500); // 1.5초의 로딩 시간 (S1: LOADING_DATA)
100	    };
101	
102	    return (
103	        <div className={`min-h-screen p-8 text-white ${diagnosisResult.bgColorClass}`}>
104	            <header className="mb-12 pt-4">
105	                <h1 className="text-4xl font-extrabold tracking-tight border-b-2 pb-2 border-opacity-50 border-current">
106	                    🩺 온현 시스템 실패 보고서 (MiniFunnel MVP)
107	                </h1>
108	                <p className="mt-2 text-lg opacity-80">사용자님의 현재 건강 상태 데이터를 분석하여 위험도를 진단합니다.</p>
109	            </header>
110	
111	            {/* 1. Diagnosis Form Section */}
112	            <div className={`bg-white/10 p-8 rounded-xl shadow-2xl border-l-4 ${diagnosisResult.bgColorClass.replace('bg-', 'border-')}`}>
113	                <h2 className="text-2xl font-semibold mb-6">STEP 1. 증상 데이터 입력</h2>
114	                <DefectInputForm 
115	                    onInputChange={handleInputChange} 
116	                    currentData={formData || { symptom1: '', yearsDiagnosed: '' }} 
117	                />
118	                
119	                <button 
120	                    onClick={handleDiagnosisSubmit} 
121	                    disabled={isLoading}
122	                    className={`mt-8 w-full py-3 text-xl font-bold rounded-lg transition-all ${
123	                        isLoading ? 'bg-gray-600 cursor-not-allowed' : 'bg-red-600 hover:bg-red-700 shadow-lg'
124	                    }`}
125	                >
126	                    {isLoading ? (
127	                        <div className="flex items-center justify-center">
128	                            <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">...</svg>
129	                            데이터 분석 중... (위기 진단)
130	                        </div>
131	                    ) : '진단 실행: 시스템 실패 보고서 생성'}
132	                </button>
133	            </div>
134	
135	            {/* 2. Result & Gauge Section */}
136	            <div className="mt-16 p-8 bg-white/10 rounded-xl shadow-2xl">
137	                <h2 className="text-2xl font-semibold mb-8 text-center">STEP 2. 진단 결과 및 위험도 분석</h2>
138	
139	                {/* Risk Gauge는 로딩이 끝났을 때만 결과를 보여주어야 합니다. */}
140	                {!isLoading && (
141	                    <SystemRiskGauge result={diagnosisResult} />
142	                )}
143	
144	                {/* MiniFunnel CTA Placeholder - 이 부분이 최종 목표입니다. */}
145	                {!isLoading && (
146	                    <div className="text-center mt-12 p-6 bg-yellow-900/50 border-l-4 border-yellow-500 rounded-lg">
147	                        <h3 className="text-xl font-bold mb-3 text-yellow-300">⚠️ [Critical Action Required]</h3>
148	                        <p className="mb-4 opacity-90">현재 위험도가 감지되었습니다. 단순한 증상으로는 해결할 수 없습니다.</p>
149	                        {/* 최종 목표: MiniFunnelPage로의 CTA */}
150	                        <button 
151	                            onClick={() => alert("MiniFunnel 진입! (다음 단계 구현 필요)")}
152	                            className="px-8 py-3 bg-green-600 hover:bg-green-700 text-lg font-bold rounded transition-transform transform hover:scale-105"
153	                        >
154	                            나만의 맞춤 솔루션 진단 받기 (MiniFunnel)
155	                        </button>
156	                    </div>
157	                )}
158	            </div>
159	        </div>
160	    );
161	};
162	
163	export default App;
```
