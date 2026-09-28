# 💻 코다리 — Mini-App Funnel의 최종 통합 작업에 착수합니다. Designer가 정의한 Deep Crimson Red 플래싱 효과와 HOMA-IR/MMIV 리스크 스코어 계산 로직을 결합하여, 사용자가 데이터를 입력하고 '시스템 과부하' 경고를 경험하며 CTA로 강제 유도되는 완전하게 작동하는(Functional) MVP 컴포넌트(`MiniAppFunnel.tsx`)를 완성해주세요. 테스트 코드를 포함하여 개발 결과물을 산출합니다.

💻 코다리: 작업 시작합니다.

CEO 지시 사항 확인했습니다. Mini-App Funnel의 최종 통합 단계군요. 단순히 UI를 만드는 게 아니라, '공학적 불안감'을 유발하는 시스템 장치로 설계되어야 한다는 점을 명확히 인지하고 있습니다. ⚙️

이건 단순 컴포넌트 작성이 아니라, **사용자 심리 기반의 트랜잭션 플로우(Funnel)**를 구현하는 작업입니다. 따라서 기존 코드를 읽어보고, 리스크 스코어 계산 로직과 Deep Crimson Red 경고 시스템을 통합한 후, 반드시 테스트를 통해 안정성을 검증해야 합니다.

먼저, 현재 존재하는 `MiniAppFunnel.tsx` 파일의 내용을 파악하겠습니다.

<read_file path="c:\Data\Project\FreqTrade\src\components\MiniAppFunnel.tsx"/>

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\FreqTrade\src\components\MiniAppFunnel.tsx (210줄, 9.3KB)
```
 1	import React, { useState, useCallback, useMemo } from 'react';
 2	// Deep Crimson Red와 시스템 과부하 경고를 위한 커스텀 CSS 클래스를 사용합니다. 
 3	// 실제 프로젝트의 global.css에 이 스타일이 정의되어 있다고 가정합니다.
 4	
 5	/**
 6	 * @typedef {Object} RiskInputs
 7	 * @property {number} homaIr - Homeostatic Model Assessment of Insulin Resistance (HOMA-IR) 값.
 8	 * @property {number} mmiv - Modified Mini Vascular Index (MMIV) 값.
 9	 */
10	
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\FreqTrade\src\components\MiniAppFunnel.tsx (210줄)
```
  1	import React, { useState, useCallback, useMemo } from 'react';
  2	// Deep Crimson Red와 시스템 과부하 경고를 위한 커스텀 CSS 클래스를 사용합니다. 
  3	// 실제 프로젝트의 global.css에 이 스타일이 정의되어 있다고 가정합니다.
  4	
  5	/**
  6	 * @typedef {Object} RiskInputs
  7	 * @property {number} homaIr - Homeostatic Model Assessment of Insulin Resistance (HOMA-IR) 값.
  8	 * @property {number} mmiv - Modified Mini Vascular Index (MMIV) 값.
  9	 */
 10	
 11	// --- 가상의 로직 상수 및 함수 정의 (⚠️ 명세서 검토 후 업데이트 필요 ⚠️) ---
 12	
 13	/**
 14	 * 리스크 스코어 계산 로직을 담는 순수 함수.
 15	 * 실제 가중치와 임계값은 funnel_design_spec_v2.md에 따라 확정되어야 합니다.
 16	 * @param {RiskInputs} inputs - 사용자 입력 지표 값들.
 17	 * @returns {{ score: number, riskLevel: 'Stable' | 'Warning' | 'Critical', message: string }} 계산 결과 객체.
 18	 */
 19	const calculateRiskScore = (inputs) => {
 20	    // 임시 가중치 적용: HOMA-IR(0.4), MMIV(0.6) 가정
 21	    const score = (inputs.homaIr * 0.4 + inputs.mmiv * 0.6).toFixed(2);
 22	    let riskLevel;
 23	    let message;
 24	
 25	    // 임시 경고 로직: 스코어 기반 레벨링
 26	    if (parseFloat(score) >= 3.5) {
 27	        riskLevel = 'Critical'; // 위기 (Red)
 28	        message = "시스템 과부하 감지! 즉각적인 생활 습관 시스템 복구가 필요합니다.";
 29	    } else if (parseFloat(score) >= 2.0) {
 30	        riskLevel = 'Warning'; // 경고 (Yellow)
 31	        message = "경고: 일부 지표의 임계점 초과가 관찰됩니다. 면밀한 점검이 필요합니다.";
 32	    } else {
 33	        riskLevel = 'Stable'; // 안정 (Green)
 34	        message = "현재 시스템은 비교적 안정적인 상태를 유지하고 있습니다. 지속적인 관리 바랍니다.";
 35	    }
 36	
 37	    return { score: parseFloat(score), riskLevel, message };
 38	};
 39	
 40	
 41	// --- 컴포넌트 정의 ---
 42	
 43	const FunnelInputForm = ({ onCalculate }) => {
 44	    const [homaIr, setHomaIr] = useState('');
 45	    const [mmiv, setMmiv] = useState('');
 46	
 47	    const handleSubmit = (e) => {
 48	        e.preventDefault();
 49	        const inputs = {
 50	            homaIr: parseFloat(homaIr) || 0,
 51	            mmiv: parseFloat(mmiv) || 0,
 52	        };
 53	        onCalculate(inputs);
 54	    };
 55	
 56	    return (
 57	        <form onSubmit={handleSubmit} className="space-y-6 p-8 bg-gray-800/50 rounded-xl border border-red-900 shadow-2xl">
 58	            <h2 className="text-3xl font-extrabold text-white flex items-center">
 59	                <span className="mr-3 text-deep-crimson-red">//</span> 시스템 데이터 입력 (V1.0)
 60	            </h2>
 61	            <p className="text-gray-400">정확한 리스크 스코어 계산을 위해 전문 지표를 입력해 주세요.</p>
 62	
 63	            {/* HOMA-IR Input */}
 64	            <div>
 65	                <label htmlFor="homaIr" className="block text-sm font-medium text-red-300 mb-1">
 66	                    HOMA-IR (인슐린 저항성 지표) <span className="text-yellow-400">*</span>
 67	                </label>
 68	                <input
 69	                    type="number"
 70	                    id="homaIr"
 71	                    value={homaIr}
 72	                    onChange={(e) => setHomaIr(e.target.value)}
 73	                    placeholder="예: 2.5"
 74	                    className="w-full p-3 border border-gray-600 rounded-lg bg-gray-700 text-white focus:ring-red-500 focus:border-red-500 transition duration-150"
 75	                    required
 76	                />
 77	            </div>
 78	
 79	            {/* MMIV Input */}
 80	            <div>
 81	                <label htmlFor="mmiv" className="block text-sm font-medium text-red-300 mb-1">
 82	                    MMIV (미세혈관 지수) <span className="text-yellow-400">*</span>
 83	                </label>
 84	                <input
 85	                    type="number"
 86	                    id="mmiv"
 87	                    value={mmiv}
 88	                    onChange={(e) => setMmiv(e.target.value)}
 89	                    placeholder="예: 1.8"
 90	                    className="w-full p-3 border border-gray-600 rounded-lg bg-gray-700 text-white focus:ring-red-500 focus:border-red-500 transition duration-150"
 91	                    required
 92	                />
 93	            </div>
 94	
 95	            <button 
 96	                type="submit" 
 97	                className="w-full py-3 px-6 bg-[#8B0000] hover:bg-[#A00000] text-white font-bold rounded-lg transition duration-200 shadow-lg active:scale-[0.99]"
 98	            >
 99	                리스크 스코어 계산 실행 <span className="ml-2">⚙️</span>
100	            </button>
101	        </form>
102	    );
103	}
104	
105	const FunnelResultDisplay = ({ result }) => {
106	    if (!result) return null;
107	
108	    // Tailwind 클래스 기반의 동적 스타일링 로직 구현
109	    const getStyleClasses = (level) => {
110	        switch (level) {
111	            case 'Critical':
112	                return "bg-[#8B0000] ring-4 ring-red-500/70 animate-pulse shadow-[0_0_30px_rgba(139,0,0,0.8)]"; // Deep Crimson Red & Flashing
113	            case 'Warning':
114	                return "bg-yellow-600/70 ring-2 ring-yellow-500 animate-pulse/slow shadow-[0_0_20px_rgba(255,193,7,0.8)]"; // Yellow Warning
115	            case 'Stable':
116	                return "bg-green-600/70 ring-2 ring-green-500 shadow-[0_0_20px_rgba(76,175,80,0.8)]"; // Stable Green
117	            default:
118	                return "bg-gray-700";
119	        }
120	    };
121	
122	    // 경고 메시지 부분에 공학적 오류 시뮬레이션 스타일 적용
123	    const ErrorOverlay = ({ children }) => (
124	        <div className="p-4 border-l-4 border-red-500 bg-[#1a0808] shadow-[inset_0_0_15px_rgba(139,0,0,0.7)]">
125	            <p className="text-lg font-mono text-red-400 tracking-widest animate-blink">{children}</p>
126	        </div>
127	    );
128	
129	    return (
130	        <div className={`mt-12 p-8 rounded-xl shadow-2xl ${getStyleClasses(result.riskLevel)} transition duration-500 transform scale-[1.02]`}>
131	            <h2 className="text-4xl font-extrabold text-white mb-4">🚨 [SYSTEM ALERT] 리스크 스코어 측정 결과</h2>
132	            
133	            {/* 시스템 오류 경고 오버레이 영역 */}
134	            <ErrorOverlay>
135	                시스템 과부하 상태: {result.riskLevel} | 최종 위험 지수 (R Score): <span className="text-3xl font-mono ml-2">{result.score}</span>
136	            </ErrorOverlay>
137	
138	            <div className="mt-6 space-y-4">
139	                {/* 결과 메시지 */}
140	                <div>
141	                    <h3 className="text-2xl font-semibold text-white mb-2">시스템 분석 요약</h3>
142	                    <p className="text-xl italic text-white/90">{result.message}</p>
143	                </div>
144	
145	                {/* CTA 섹션 (Mini-App Funnel 유도) */}
146	                <div className="mt-8 p-6 bg-[#110505] border-t-4 border-[#FFD700] shadow-inner">
147	                    <h3 className="text-2xl font-extrabold text-[#FFD700] mb-3 flex items-center">
148	                        <span className="mr-2">⚠️</span> 시스템 복구 모듈 실행 필요 (필수)
149	                    </h3>
150	                    <p className="mb-4 text-gray-300">측정된 위험도에 기반하여, 개인 맞춤형 '시스템 임계점 복구 솔루션'을 확인하십시오.</p>
151	                    
152	                    {/* 실제 CTA 버튼으로 대체될 부분 */}
153	                    <button 
154	                        className="w-full py-4 text-xl font-extrabold bg-[#8B0000] hover:bg-[#A00000] text-white rounded-lg transition duration-200 tracking-wider shadow-md"
155	                        onClick={() => alert("Funnel Link Redirecting...")} // 실제 Funnel 링크로 대체 필요
156	                    >
157	                        👉 [Mini-App Funnel] 나에게 맞는 복구 솔루션 확인하기 (클릭)
158	                    </button>
159	                </div>
160	            </div>
161	        </div>
162	    );
163	};
164	
165	
166	const MiniAppFunnel: React.FC = () => {
167	    // 상태 관리: 계산 결과 저장
168	    const [result, setResult] = useState(null);
169	
170	    /**
171	     * 리스크 스코어를 계산하고 결과를 상태에 저장하는 핸들러.
172	     * @param {RiskInputs} inputs - HOMA-IR 및 MMIV 값
173	     */
174	    const handleCalculateRiskScore = useCallback((inputs) => {
175	        try {
176	            // 1. 로직 실행 (순수 함수 사용)
177	            const calculatedResult = calculateRiskScore(inputs);
178	            
179	            // 2. 결과 상태 업데이트
180	            setResult(calculatedResult);
181	
182	        } catch (error) {
183	            console.error("Funnel 스코어 계산 중 오류 발생:", error);
184	            setResult({ score: NaN, riskLevel: 'Stable', message: "시스템 로직 처리 중 알 수 없는 에러가 발생했습니다." });
185	        }
186	    }, []);
187	
188	    return (
189	        <div className="container mx-auto py-12 px-4 max-w-3xl">
190	            <h1 className="text-5xl font-black text-white mb-8 text-center tracking-tighter">
191	                🧬 Mini-App Funnel: 생체 시스템 리스크 스코어 측정
192	            </h1>
193	
194	            {/* 폼과 결과는 구조적으로 분리하여 사용자가 흐름을 이해하도록 함 */}
195	            <div className="grid md:grid-cols-2 gap-10 items-start">
196	                {/* 입력 영역 (왼쪽) */}
197	                <div>
198	                    <FunnelInputForm onCalculate={handleCalculateRiskScore} />
199	                </div>
200	
201	                {/* 결과 출력 영역 (오른쪽) */}
202	                <div className="min-h-[400px]">
203	                    <FunnelResultDisplay result={result} />
204	                </div>
205	            </div>
206	        </div>
207	    );
208	};
209	
210	export default MiniAppFunnel;
```
