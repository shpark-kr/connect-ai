# 💻 코다리 — Business가 정의한 A/B 테스트 가설들을 개발에 반영하기 위해, Funnel 프로토타입에 '플래그 기반 로직 시스템'을 추가해야 합니다. 이 시스템은 트래픽의 일정 비율(예: 20%)을 여러 변수 그룹으로 분배하고, 각 변수 그룹별 성과 데이터를 실시간으로 수집 및 비교할 수 있도록 구조화되어야 합니다. 필요한 데이터 추적 지점(Tracking Pixels) 명세와 API 연동 포인트를 설계해 주세요.

💻 코다리: 작업 시작합니다.

CEO님의 지시사항을 보니, 단순히 기능을 추가하는 수준이 아니라 **데이터 측정 체계 자체를 업그레이드**해야 하는 구조적 변화네요. 👍 A/B 테스트 가설(현빈님이 수립)을 개발에 녹여내려면, 트래픽 분배부터 데이터 추적이 일관되게 이루어지는 시스템 아키텍처가 필요합니다.

단순히 로직을 넣는 건 가장 낮은 레벨의 작업이고요. 코드는 깨지기 쉽고, 나중에 디버깅할 때 *왜 이 변수가 다른 값을 가질까?* 라는 근본적인 질문에 답하기 어렵게 됩니다. ⚙️

따라서 저는 다음 단계를 거쳐 접근하겠습니다:
1.  **코드 탐색**: Funnel의 핵심 흐름을 담당하는 메인 페이지 (`src/pages/funnel/index.tsx`)를 먼저 파악하여, 시스템 로직이 어디에 주입되어야 할지 위치를 잡겠습니다.
2.  **시스템 설계 (Flagging)**: A/B 테스트 그룹을 결정하고 전역적으로 관리할 `ABTestContext`와 관련 훅을 만듭니다.
3.  **추적 계층 분리**: 모든 측정(Pixel, Event) 로직은 컴포넌트에서 분리하여 재사용 가능한 `AnalyticsService`를 구현합니다. (이게 가장 중요해요. 코드가 지저분해지는 걸 막아야 하거든요.)

먼저 Funnel의 메인 페이지 구조부터 파악하겠습니다.

<read_file path="c:\Data\Project\connect-ai\src\pages\funnel\index.tsx"/>

📊 평가: 진행중 — 현재 Funnel 메인 로직을 읽어 시스템에 필요한 Flagging 및 추적 계층(Layer)을 설계하는 중입니다.
📝 다음 단계: `ABTestContext`와 `AnalyticsService`를 구현할 유틸리티 파일을 생성하고, 이들을 `src/pages/funnel/index.tsx`에 통합하겠습니다.

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
