# 💻 코다리 — Designer가 완성할 MiniFunnel Mockup의 최종 가이드라인을 바탕으로, 실제로 작동 가능한 '최소 기능 단위(MVP) 프로토타입'의 초기 코드를 작성해주세요. 특히, Defect ID 입력/제시 → 시스템 오류 페이지 진입 → 초기 상품 추천 CTA가 연결되는 3단계 흐름만이라도 구현하여 개발 환경에 테스트 가능하도록 설정해야 합니다. (Landing Kit 구조 참고)

💻 코다리: 작업 시작합니다.

CEO 지시사항과 Designer의 상세 가이드라인을 보니, 이제는 개념적인 Mockup 단계를 넘어 실제 사용자 흐름(User Flow)에 맞는 *상태 기반 프로토타입*이 필요한 시점이네요. ⚙️ 단순히 컴포넌트를 나열하는 건 안 됩니다. 이 Funnel은 사용자의 심리적 동선과 공학적 위기감이 핵심인데, 이를 코드로 구현하려면 상태 관리(State Machine)가 필수입니다.

제공된 로컬 파일 구조(`mini-funnel-proto`)를 보니 이미 3단계에 필요한 컴포넌트들이 준비되어 있습니다. 이제 이들을 `App.tsx`라는 메인 컨테이너에서 State Transition을 통해 연결하는 작업을 진행하겠습니다.

우선, 현재 핵심 파일인 `src/App.tsx`의 구조와 내용을 파악해야 합니다.

<read_file path="c:\Data\Project\FreqTrade\mini-funnel-proto\src\App.tsx"/>


---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\FreqTrade\mini-funnel-proto\src\App.tsx (77줄, 3.9KB)
```
 1	import React, { useState } from 'react';
 2	import DefectIdCard from './components/DefectIdCard';
 3	import SymptomInputForm from './components/SymptomInputForm';
 4	import ReportOutputArea from './components/ReportOutputArea';
 5	
 6	// Mock Data Definitions (Dummy data for the prototype)
 7	const MOCK_DEFECT = {
 8	    id: 'E-C403',
 9	    description: '만성적 염증 수치 상승 및 대사 효율 저하. 신체 활동과 영양소 흡수 경로에 심각한 병목 현상이 감지되었습니다.',
10	};
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\FreqTrade\mini-funnel-proto\src\App.tsx (77줄)
```
 1	import React, { useState } from 'react';
 2	import DefectIdCard from './components/DefectIdCard';
 3	import SymptomInputForm from './components/SymptomInputForm';
 4	import ReportOutputArea from './components/ReportOutputArea';
 5	
 6	// Mock Data Definitions (Dummy data for the prototype)
 7	const MOCK_DEFECT = {
 8	    id: 'E-C403',
 9	    description: '만성적 염증 수치 상승 및 대사 효율 저하. 신체 활동과 영양소 흡수 경로에 심각한 병목 현상이 감지되었습니다.',
10	};
11	
12	const INITIAL_REPORT_DATA = {
13	    defectId: MOCK_DEFECT.id,
14	    summary: "현재 패턴 분석 결과, 신체의 에너지 대사 효율성이 임계점 이하로 떨어져 있습니다. 이는 단순 피로가 아닌, 시스템적인 '만성적 염증'에 기인한 구조적 문제입니다. 즉각적인 개입이 필요합니다.",
15	    severity: "CRITICAL",
16	    rootCause: "주요 영양소 흡수 경로의 미세 균열 및 운동 부족으로 인한 대사 불균형 가속화.",
17	    protocol: "최적의 결과를 위해서는 '개인 맞춤형 3단계 프로토콜 번들'을 통한 전문 지식과 관리 시스템이 필수적으로 요구됩니다. 이 보고서만으로는 근본적인 해결책 제시가 어렵습니다.",
18	};
19	
20	const App: React.FC = () => {
21	    // State to manage the report data after form submission
22	    const [reportData, setReportData] = useState<typeof INITIAL_REPORT_DATA>(INITIAL_REPORT_DATA);
23	    const [loading, setLoading] = useState(false);
24	
25	    /**
26	     * 시뮬레이션: 증상 데이터를 받아 최종 보고서를 생성하는 함수 (API 호출 시뮬)
27	     */
28	    const handleAnalyzeSymptoms = async (symptoms: any) => {
29	        setLoading(true);
30	        // API Latency Simulation
31	        await new Promise(resolve => setTimeout(resolve, 1500));
32	
33	        // Simulate successful data processing and report generation
34	        const newReportData = {
35	            defectId: MOCK_DEFECT.id, // Keep the ID consistent for the prototype
36	            summary: "입력된 데이터를 바탕으로 재분석한 결과, 초기 예측이 맞습니다. '대사 효율성 저하'가 핵심 문제이며, 특히 수면 패턴과 미세 영양소 결핍 간의 상관관계가 높게 감지되었습니다.",
37	            severity: Math.random() > 0.7 ? "CRITICAL" : "HIGH",
38	            rootCause: `BPI ${symptoms.bodyPainLevel}와 Sleep Score ${symptoms.sleepQualityScore}%의 불일치 패턴이 주요 원인으로 추정됩니다.`,
39	            protocol: "가장 효과적인 개입은 수면 주기 최적화(Circadian Rhythm Optimization)와 미세 영양소 보강을 결합한 '통합 관리 시스템'입니다. 이는 오직 유료 프로토콜 번들을 통해서만 접근 가능합니다.",
40	        };
41	
42	        setReportData(newReportData);
43	        setLoading(false);
44	    };
45	
46	
47	  return (
48	    <div className="min-h-screen p-8 bg-[#0A1931] text-gray-200 font-sans">
49	      <header className="mb-12 border-b border-red-700/50 pb-4">
50	        <h1 className="text-4xl font-mono uppercase tracking-widest flex items-center">
51	            <span className="text-[#C5222D] mr-3 animate-pulse">[SYSTEM ALERT]</span> 
52	            Health Protocol Validator <span className='ml-4 text-sm font-normal text-gray-400'>(Beta v1.0)</span>
53	        </h1>
54	        <p className="mt-2 text-lg text-[#C5222D]/70">
55	            공학적 위기감 기반의 신체 진단 및 문제 해결 프로세스 시뮬레이터 💻
56	        </p>
57	      </header>
58	
59	      {/* 1. 핵심 Defect ID 표시 */}
60	      <div className="mb-16 max-w-3xl mx-auto">
61	        <DefectIdCard defectId={MOCK_DEFECT.id} description={MOCK_DEFECT.description} />
62	      </div>
63	
64	      {/* 2. 증상 입력 및 분석 */}
65	      <div className="max-w-4xl mx-auto mb-16">
66	        <SymptomInputForm onAnalyze={handleAnalyzeSymptoms} />
67	      </div>
68	
69	      {/* 3. 최종 보고서 출력 영역 */}
70	      <div className="max-w-5xl mx-auto">
71	        <ReportOutputArea reportData={reportData} />
72	      </div>
73	    </div>
74	  );
75	};
76	
77	export default App;
```
