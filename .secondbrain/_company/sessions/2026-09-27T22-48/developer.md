# 💻 코다리 — Mini-App Funnel의 E2E(End-to-End) 시뮬레이션 로직 구축을 최우선 과제로 진행합니다. '만성 염증' 사례를 기반으로, 표준 위험 점수 그래픽 자산과 연동되어 사용자가 특정 임계점(Deep Crimson Red)에 도달했을 때 다음 단계(유료 진단 요구 CTA)로 강제 상태 전이가 이루어지는 프로토타입 코드를 완성하고 테스트 케이스를 준비해 주세요.

💻 코다리: 작업 시작합니다.

CEO 지시가 매우 명확하고 핵심적입니다. Mini-App Funnel의 E2E 시뮬레이션 로직 구축은 온현사의 수익 구조를 결정하는 가장 중요한 부분입니다. 단순히 UI를 보여주는 걸 넘어, **'위험 인지 $\rightarrow$ 상태 전이 $\rightarrow$ 유료 CTA 강제'**라는 논리적 흐름을 코드로 구현하고 검증해야 합니다.

이 작업은 프론트엔드(React/TSX) 로직과 백엔드 API 호출, 그리고 비즈니스 규칙(위험 점수 계산 및 임계점 체크)의 세 가지 레이어가 완벽하게 결합되어야 합니다. 한 군데라도 틈이 있으면 Funnel 자체가 무너집니다.

먼저 현재 프로토타입 코드를 파악하고, 핵심 로직인 '진단 엔진'을 테스트하여 비즈니스 규칙에 따라 상태 전이가 제대로 되는지 검증하는 것이 순서입니다.

### ⚙️ 작업 계획 및 실행 (3단계)
1.  **[검증] 진단 엔진 테스트:** Mini-App Funnel의 핵심 로직인 '위험 점수 계산 및 임계점 도달 여부'를 전용 테스트 스위트를 통해 검증합니다. 이 단계가 성공해야 프론트엔드에 녹일 근거가 생깁니다.
2.  **[구현] 프로토타입 컴포넌트 수정:** 현재 작업 중인 `page.tsx`에 상태 관리 로직과 위험 점수 게이지 UI를 통합하고, 진단 엔진의 결과를 받아 State Transition을 실행하는 메인 코드를 작성합니다.
3.  **[최종 검증] E2E Funnel 테스트:** 전체 사용자 흐름(시뮬레이션)을 최종적으로 돌려보며, CTA가 정확히 발동되는지 확인하고 시스템 안정성을 확보합니다.

---

### 🛠️ Step 1: 진단 엔진 로직의 비즈니스 규칙 검증
Mini-App Funnel의 핵심은 '위험 점수'입니다. 이 점수를 기반으로 상태 전이를 처리하는 `test_diagnosis_engine`을 먼저 실행하여, 우리가 정의한 임계치(Deep Crimson Red) 도달 시 유료 CTA가 발동되는지 로직 레벨에서 검증하겠습니다.

<run_command>cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe test_diagnosis_engine.py</run_command>

### 🛠️ Step 2: `page.tsx`에 E2E 상태 전이 로직 통합
진단 엔진 테스트가 성공적으로 완료된다는 가정 하에, 이제 실제 사용자 화면인 `c:\Data\Project\connect-ai\prototype\app\page.tsx` 파일에 이 복잡한 상태 전이(State Transition) 및 위험 점수 게이지 컴포넌트를 통합해야 합니다.

먼저 현재 `page.tsx`의 내용을 읽어보고, 어떤 구조로 로직을 삽입할지 판단하겠습니다.

<read_file path="c:\Data\Project\connect-ai\prototype\app\page.tsx"/>

(만약 파일 내용이 너무 길거나 복잡하다면, 핵심적인 `useState`와 API 호출 부분을 중점적으로 확인해야 합니다.)

***
*(사용자에게는 이어서 Step 2의 코드를 작성하고 테스트하는 과정이 이어집니다)*
---
*Self-Correction/Refinement:* The user will provide the read result here. I must wait for that output before writing any code for `page.tsx`. If the file is large, I'll focus my `<edit_file>` on a new component or hook rather than rewriting the whole thing to maintain clean architecture.

---
📊 평가: 진행중 — 진단 엔진의 비즈니스 로직 검증과 실제 프론트엔드 구현 사이의 연결고리 작업이 필요하며, 다음 스텝에서 프로토타입 코드 수정 및 E2E 테스트를 할 예정입니다.
📝 다음 단계: Step 1 실행 결과(진단 엔진 테스트)를 분석하고, 그 결과를 바탕으로 `c:\Data\Project\connect-ai\prototype\app\page.tsx` 파일을 에디팅하여 상태 전이 로직을 구현할 것입니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppDa`
```
File "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\test_diagnosis_engine.py", line 2
    from c.Data.Project.connect-ai.services.diagnosis_engine import ( # Mocked import path for testing
                               ^
SyntaxError: invalid syntax
```
_❌ exit 1_

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\prototype\app\page.tsx (194줄, 8.5KB)
```
 1	// prototype/app/page.tsx
 2	"use client";
 3	
 4	import React, { useState, useEffect } from 'react';
 5	
 6	// --- TYPES & ENUMS ---
 7	type RiskLevel = 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
 8	type FunnelStage = 'RECOGNITION' | 'AMPLIFICATION' | 'DIAGNOSIS_CTA';
 9	
10	interface DiagnosisData {
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\prototype\app\page.tsx (194줄)
```
  1	// prototype/app/page.tsx
  2	"use client";
  3	
  4	import React, { useState, useEffect } from 'react';
  5	
  6	// --- TYPES & ENUMS ---
  7	type RiskLevel = 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  8	type FunnelStage = 'RECOGNITION' | 'AMPLIFICATION' | 'DIAGNOSIS_CTA';
  9	
 10	interface DiagnosisData {
 11	  score: number; // 0~100
 12	  riskLevel: RiskLevel;
 13	}
 14	
 15	// --- CORE COMPONENT LOGIC (Simulation) ---
 16	
 17	const calculateRiskLevel = (score: number): RiskLevel => {
 18	    if (score >= 90) return 'CRITICAL';
 19	    if (score >= 70) return 'HIGH';
 20	    if (score >= 40) return 'MEDIUM';
 21	    return 'LOW';
 22	};
 23	
 24	// Helper function to simulate API calls and tracking
 25	const trackEvent = (event: string, data: Record<string, any>) => {
 26	    console.log(`[Tracking Log] ${new Date().toISOString()} | Event: ${event} | Data:`, data);
 27	    // In a real environment, this would be an axios/fetch call to the tracking API endpoint.
 28	};
 29	
 30	// --- STAGE COMPONENTS ---
 31	
 32	const RiskGaugeDisplay = ({ score, level }: { score: number; level: RiskLevel }) => {
 33	    let colorClass = '';
 34	    switch (level) {
 35	        case 'CRITICAL':
 36	            colorClass = 'bg-red-800 animate-pulse'; // Deep Crimson Red! 🚨
 37	            break;
 38	        case 'HIGH':
 39	            colorClass = 'bg-yellow-600';
 40	            break;
 41	        case 'MEDIUM':
 42	            colorClass = 'bg-orange-400';
 43	            break;
 44	        default:
 45	            colorClass = 'bg-green-500';
 46	    }
 47	
 48	    return (
 49	        <div className="w-full mt-8 p-6 bg-gray-900 rounded-xl shadow-2xl">
 50	            <h3 className="text-2xl font-bold text-white mb-4">🚨 시스템 위험 점수 게이지</h3>
 51	            <div className="relative h-10 w-full border-x-4 border-gray-700 rounded-none overflow-hidden">
 52	                {/* The actual gauge fill */}
 53	                <div 
 54	                    className={`absolute top-0 left-0 h-full transition-all duration-1000 ease-out ${colorClass}`}
 55	                    style={{ width: `${score}%` }}
 56	                ></div>
 57	                {/* Gauge border line */}
 58	                <div className="absolute top-0 right-0 w-2 h-full bg-gray-700"></div>
 59	            </div>
 60	            <div className="flex justify-between text-white mt-3 text-sm font-mono">
 61	                <span>점수: {score}%</span>
 62	                <span>위험도: <span className="uppercase">{level}</span></span>
 63	            </div>
 64	        </div>
 65	    );
 66	};
 67	
 68	// STAGE 1: Danger Recognition (Initial Shock)
 69	const StageRecognition = ({ onProceed }: { onProceed: () => void }) => {
 70	    return (
 71	        <div className="p-8 bg-red-900/20 border border-red-700 rounded-lg shadow-inner">
 72	            <h2 className="text-4xl font-extrabold text-red-500 mb-4 tracking-wide">경고: 시스템적 고장 감지</h2>
 73	            <p className="text-xl text-gray-800 mb-6">
 74	                혹시 느껴지는 '피로함'이나 '만성 통증'이 단순한 증상이라고 생각하셨나요?
 75	            </p>
 76	            <div className="mb-6 p-4 bg-red-900/50 border border-red-700 rounded-md">
 77	                <p className="text-lg text-red-300 font-semibold">⚠️ 경고: 이는 단순 증상 수준이 아닙니다. 측정 가능한 '시스템 고장'의 신호일 수 있습니다.</p>
 78	            </div>
 79	            <button 
 80	                onClick={onProceed}
 81	                className="px-8 py-3 bg-red-600 text-white font-bold rounded-lg hover:bg-red-700 transition duration-200"
 82	            >
 83	                다음 단계로 위험 점수 측정하기 $\rightarrow$ (문제 증폭)
 84	            </button>
 85	        </div>
 86	    );
 87	};
 88	
 89	// STAGE 2: Problem Amplification (The Deep Dive)
 90	const StageAmplification = ({ score, onProceed }: { score: number; onProceed: () => void }) => {
 91	    return (
 92	        <div className="p-8 bg-gray-100 border-l-4 border-yellow-500 rounded-lg shadow-xl">
 93	            <h2 className="text-3xl font-bold text-gray-800 mb-6">🔍 [자가 진단 분석] 당신의 시스템은 얼마나 고장 났나요?</h2>
 94	            
 95	            {/* The Risk Gauge */}
 96	            <RiskGaugeDisplay score={score} level={calculateRiskLevel(score)} />
 97	
 98	            <div className="mt-10 space-y-4">
 99	                <h4 className="text-xl font-semibold text-gray-700">발견된 위험 지표 (예시)</h4>
100	                <ul className="list-disc pl-5 text-gray-600">
101	                    <li>[혈관 탄력성] 임계치 초과: 3년 평균 대비 25% 감소.</li>
102	                    <li>[근육 대사 효율] 저하: 활동 에너지 소모가 급격히 떨어지는 패턴 감지.</li>
103	                    <li>[장-뇌 축 민감도] 과부하 상태: 만성 염증 지표(hs-CRP) 수치 모니터링 필요.</li>
104	                </ul>
105	            </div>
106	
107	            <div className="mt-10 text-center">
108	                 {/* CTA 2 */}
109	                <button 
110	                    onClick={onProceed}
111	                    className="px-8 py-3 bg-yellow-600 text-white font-bold rounded-lg hover:bg-yellow-700 transition duration-200"
112	                >
113	                    심화 분석 및 구체적 해결책 확인하기 $\rightarrow$ (진단 요구)
114	                </button>
115	            </div>
116	        </div>
117	    );
118	};
119	
120	// STAGE 3: Diagnostic Requirement & CTA (The Conversion Point)
121	const StageDiagnosisCTA = () => {
122	    return (
123	        <div className="p-10 bg-red-900/80 border-4 border-deep-crimson rounded-xl shadow-[0_0_20px_rgba(220,39,59,0.8)] text-center">
124	            <h2 className="text-4xl font-extrabold text-white mb-4 animate-pulse">🚨 위험 임계치 도달! 즉각적인 진단이 필요합니다.</h2>
125	            <p className="text-2xl text-red-200 mb-8">
126	                지금까지의 데이터는 '위험'을 알렸을 뿐, 당신에게 필요한 것은 **정확한 수치적 자가진단**입니다.
127	            </p>
128	
129	            {/* The Mandatory CTA */}
130	            <button 
131	                onClick={() => {
132	                    trackEvent('MiniApp_Funnel_Click', { status: 'Success' });
133	                    alert("➡️ Mini-App Funnel로 이동합니다! (실제로는 링크 클릭)");
134	                }}
135	                className="text-2xl px-12 py-5 bg-gradient-to-r from-red-600 to-black text-white font-extrabold rounded-full shadow-[0_0_15px_rgba(220,39,59,0.9)] hover:scale-105 transition duration-300 cursor-pointer"
136	            >
137	                ✨ 무료 위험 점수 자가 진단 시작하기 (Mini-App Funnel) ✨
138	            </button>
139	
140	             <p className="text-sm text-red-400 mt-6">
141	                * 모든 유입은 데이터 기반으로 추적됩니다.
142	            </p>
143	        </div>
144	    );
145	};
146	
147	
148	// --- MAIN PAGE COMPONENT ---
149	
150	export default function Home() {
151	    const [stage, setStage] = useState<FunnelStage>('RECOGNITION');
152	    const [simulatedScore, setSimulatedScore] = useState(55); // 1차 진단 점수 시뮬레이션 값
153	
154	    // State transition handler (The core logic)
155	    const handleProceedToNextStage = () => {
156	        if (stage === 'RECOGNITION') {
157	            setStage('AMPLIFICATION');
158	            // 1단계 완료 후, 2단계 진입을 위해 점수 데이터를 업데이트하는 로직 시뮬레이션.
159	            // 실제로는 여기서 API 호출이 발생하여 점수가 재산출됨.
160	            setSimulatedScore(Math.min(85, Math.max(60, simulatedScore + 15))); // 점수를 높여서 위기감 조성
161	        } else if (stage === 'AMPLIFICATION') {
162	            setStage('DIAGNOSIS_CTA');
163	            // 2단계 완료 후, 최종 CTA를 노출하며 점수 변화가 거의 없거나 미묘하게 높아지는 효과 유지.
164	        }
165	    };
166	
167	    const renderStage = () => {
168	        switch (stage) {
169	            case 'RECOGNITION':
170	                return <StageRecognition onProceed={handleProceedToNextStage} />;
171	            case 'AMPLIFICATION':
172	                return <StageAmplification score={simulatedScore} onProceed={handleProceedToNextStage} />;
173	            case 'DIAGNOSIS_CTA':
174	                return <StageDiagnosisCTA />;
175	            default:
176	                return null;
177	        }
178	    };
179	
180	    return (
181	        <div className="min-h-screen bg-gray-50 flex items-center justify-center p-4">
182	            <div className="max-w-4xl w-full space-y-12">
183	                {/* Header / Context */}
184	                <header className="text-center py-6 border-b border-gray-300">
185	                    <h1 className="text-4xl font-extrabold text-red-800">🧬 온현 Mini-App Funnel 프로토타입</h1>
186	                    <p className="text-lg text-gray-500 mt-2">User Flow: 위험 인지 $\rightarrow$ 문제 증폭 $\rightarrow$ 진단 요구</p>
187	                </header>
188	
189	                {/* The Core Prototype */}
190	                {renderStage()}
191	            </div>
192	        </div>
193	    );
194	}
```
