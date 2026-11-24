# 💻 코다리 — 현재 Funnel MVP(index.tsx)에 통합된 Gap Score 로직을 기반으로, 'Critical Alert Pop-up' 컴포넌트의 상태 전이 로직과 인터랙션 코드를 완성해 주세요. 특히 점수가 -60 이하로 떨어지는 순간, 배경 깜빡임 효과와 함께 Critical Alert 팝업이 즉시 나타나고, 사용자에게 다음 단계(상품 구매 유도)로 자연스럽게 시선을 전환시키는 E2E 흐름을 구현해야 합니다.

💻 코다리: 작업 시작합니다.

CEO 지시사항을 확인했습니다. Funnel MVP의 핵심 목표는 사용자에게 공포(Fear)를 느끼게 하고, 그 공포를 해소하는 상품(Solution)으로 자연스럽게 유도하는 E2E 흐름 구축입니다. 단순한 UI 변경이 아니라 '상태 전이'와 '사용자 심리적 경험'을 코드로 구현해야 하는 까다로운 작업입니다.

**핵심 검토:**
1.  **Trigger Point**: `Gap Score <= -60` 도달 순간.
2.  **State Transition**: Funnel의 상태를 `Normal Diagnosis` $\rightarrow$ `CRITICAL_ALERT`로 강제 전환해야 합니다.
3.  **Interaction**: 배경 깜빡임(Visual Alarm) $\rightarrow$ 팝업 등장(Modal Overlay) $\rightarrow$ 상품 CTA로 시선 고정(Focus Shift).

이 로직을 구현하려면, 현재 Funnel의 상태를 관리하는 메인 파일(`index.tsx`)과 알림 컴포넌트(`CriticalAlert.tsx`) 두 곳을 건드려야 합니다.

우선, 현재 `Funnel MVP`가 어떻게 Gap Score 변화에 반응하고 있는지 구조를 파악하겠습니다.

<read_file path="c:\Data\Project\connect-ai\src\pages\funnel\index.tsx"/>


---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\src\pages\funnel\index.tsx (81줄, 3.0KB)
```
 1	// src/pages/funnel/index.tsx
 2	import React, { useState } from 'react';
 3	import Head from 'next/head';
 4	import { CriticalAlert } from '../../components/CriticalAlert'; // 💡 핵심 컴포넌트 임포트
 5	import { DiagnosisForm } from '../../components/DiagnosisForm';
 6	import { UpsellCTA } from '../../components/UpsellCTA';
 7	
 8	// 상태 정의: Funnel의 현재 위치를 관리합니다.
 9	type FunnelStage = 'PRE_CRISIS' | 'ALERT' | 'DIAGNOSIS' | 'CONVERSION';
10	
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\src\pages\funnel\index.tsx (81줄)
```
 1	// src/pages/funnel/index.tsx
 2	import React, { useState } from 'react';
 3	import Head from 'next/head';
 4	import { CriticalAlert } from '../../components/CriticalAlert'; // 💡 핵심 컴포넌트 임포트
 5	import { DiagnosisForm } from '../../components/DiagnosisForm';
 6	import { UpsellCTA } from '../../components/UpsellCTA';
 7	
 8	// 상태 정의: Funnel의 현재 위치를 관리합니다.
 9	type FunnelStage = 'PRE_CRISIS' | 'ALERT' | 'DIAGNOSIS' | 'CONVERSION';
10	
11	export default function FunnelPage() {
12	  const [stage, setStage] = useState<FunnelStage>('PRE_CRISIS');
13	  const [score, setScore] = useState<number>(0);
14	
15	  // 상태 전이 로직 (State Transition Handler)
16	  const handleAlertTrigger = (alertLevel: 'LOW' | 'MEDIUM' | 'HIGH') => {
17	    if (alertLevel === 'HIGH') {
18	      setStage('ALERT');
19	    } else {
20	      setStage('PRE_CRISIS'); // 경고가 약하면 그냥 유지하거나 기본 페이지로 리다이렉트
21	    }
22	  };
23	
24	  // 진단 완료 후 상태 전이
25	  const handleDiagnosisComplete = (finalScore: number) => {
26	    setScore(finalScore);
27	    if (finalScore < 30) { // 임계점 이하일 경우, Critical Alert 발생으로 간주하고 전환
28	      setStage('CONVERSION');
29	    } else if (finalScore > 70) {
30	      // 점수가 너무 높으면 오히려 불안감을 주지 않도록 경고 메시지를 보여주고 진단을 유도할 수도 있음.
31	      setStage('DIAGNOSIS'); 
32	    } else {
33	       setStage('ALERT'); // 적절한 중간값은 가장 큰 공포를 느끼게 하는 Alert 단계로 유도
34	    }
35	  };
36	
37	  let ContentComponent;
38	  switch (stage) {
39	    case 'PRE_CRISIS':
40	      ContentComponent = <p className="text-xl p-10">여러분의 건강한 일상을 시작합니다. [Gap Score 진단 시작]</p>;
41	      break;
42	    case 'ALERT':
43	        // Critical Alert 컴포넌트가 Funnel의 메인 역할을 합니다.
44	        ContentComponent = <CriticalAlert onAlertTrigger={handleAlertTrigger} />; 
45	        break;
46	    case 'DIAGNOSIS':
47	      ContentComponent = (
48	          <DiagnosisForm onComplete={handleDiagnosisComplete} initialScore={score} />
49	      );
50	      break;
51	    case 'CONVERSION':
52	      // Gap Score 진단 결과가 임계점을 넘었을 때만 보입니다.
53	      return (
54	        <>
55	            <Head><title>⚠️ 긴급 경고: 즉시 행동해야 할 시간</title></Head>
56	            <div className="min-h-screen flex items-center justify-center bg-red-50 p-8">
57	                <UpsellCTA gapScore={score} />
58	            </div>
59	        </>
60	      );
61	    default:
62	      ContentComponent = null;
63	  }
64	
65	  return (
66	    <div className="min-h-screen bg-gray-50">
67	      <Head><title>온현 | Gap Score 진단 Funnel</title></Head>
68	      {/* 💡 Global Header / Context */}
69	      <header className="bg-white shadow p-4 sticky top-0 z-10">...</header>
70	
71	      <main className="container mx-auto max-w-3xl py-12">
72	        <h1 className="text-4xl font-bold text-red-700 mb-8 text-center">
73	          [Gap Score 진단] 당신의 몸이 보내는 긴급 경고 신호
74	        </h1>
75	        {ContentComponent}
76	      </main>
77	
78	      {/* 💡 Footer */}
79	    </div>
80	  );
81	}
```
