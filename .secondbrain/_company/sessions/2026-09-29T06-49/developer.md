# 💻 코다리 — Designer가 확정한 '공학적 경고 컴포넌트(Deep Crimson Red)'를 적용하여, MiniFunnel 진단 과정 중 가장 핵심적인 '위기감 조성' 상태 변화 로직을 구현해 주세요. 특히 사용자가 자신의 데이터를 입력하거나 특정 오류 코드를 발견할 때, 단순한 텍스트 출력을 넘어 시각적/기술적으로 불안감을 극대화하는 State Machine(예: 로딩 스피너 $	o$ 에러 코드 폭발 $	o$ 경고 메시지)을 포함하여 인터랙티브 프로토타입으로 완성해야 합니다. (HTML/JS 기반)

💻 코다리: 작업 시작합니다.
요청하신 내용은 Funnel의 핵심 로직, 즉 '위기감 조성(Crisis Generation)' 상태 변화를 구현하는 것입니다. 단순히 UI 컴포넌트를 나열하는 것이 아니라, 시간이 흐름에 따라 사용자의 불안감을 극대화하는 **State Machine**을 구축해야 합니다.

이건 단순한 프론트엔드 코드가 아닙니다. 공학적 트라우마(Engineering Trauma)를 사용자에게 주입하는 로직입니다. 따라서 `MiniFunnelCore.tsx`가 이 모든 상태 전이를 담당하도록 구조를 변경하고, Designer님이 정의하신 'Deep Crimson Red' 경고 컴포넌트를 핵심 전환점(`State.ERROR_DETECTED`)에 강제 삽입하겠습니다.

우선 현재 코어 로직의 상태를 확인하겠습니다.

<read_file path="c:\Data\Project\connect-ai\src\components\MiniFunnelCore.tsx"/>


---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\src\components\MiniFunnelCore.tsx (41줄, 1.4KB)
```
 1	import React from 'react';
 2	import { useMiniFunnel } from '../context/MiniFunnelContext';
 3	import ProblemView from './ProblemView';
 4	import ErrorWarningView from './ErrorWarningView';
 5	import SolutionCTA from './SolutionCTA';
 6	
 7	const MiniFunnelCore: React.FC = () => {
 8	  // Context를 이용해 현재 Funnel의 상태를 읽어옵니다.
 9	  const { currentState } = useMiniFunnel();
10	
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\src\components\MiniFunnelCore.tsx (41줄)
```
 1	import React from 'react';
 2	import { useMiniFunnel } from '../context/MiniFunnelContext';
 3	import ProblemView from './ProblemView';
 4	import ErrorWarningView from './ErrorWarningView';
 5	import SolutionCTA from './SolutionCTA';
 6	
 7	const MiniFunnelCore: React.FC = () => {
 8	  // Context를 이용해 현재 Funnel의 상태를 읽어옵니다.
 9	  const { currentState } = useMiniFunnel();
10	
11	  let ContentComponent;
12	
13	  switch (currentState) {
14	    case 'PROBLEM':
15	      ContentComponent = <ProblemView />;
16	      break;
17	    case 'ERROR_TRIGGERED':
18	    case 'WARNING_ACTIVE':
19	      // 오류 감지 및 경고 단계에서는 ErrorWarningView를 보여줍니다. 
20	      // 실제로는 이 상태에서 짧은 애니메이션 로딩 화면을 추가할 수 있습니다.
21	      ContentComponent = <ErrorWarningView />;
22	      break;
23	    case 'SOLUTION_CTA':
24	      // Funnel의 마지막 단계, 해결책 제시 및 CTA 노출
25	      ContentComponent = <SolutionCTA />;
26	      break;
27	    default:
28	      ContentComponent = <div>시스템 오류: Unknown State.</div>;
29	  }
30	
31	  return (
32	    <div className="w-full max-w-4xl mx-auto p-6 bg-white shadow-2xl rounded-lg border-t-8 border-red-700/50">
33	      <h1 className="text-3xl font-bold text-gray-900 mb-8 border-b pb-2">
34	        🧬 온현 MiniFunnel: 건강 시스템 진단 모듈
35	      </h1>
36	      {ContentComponent}
37	    </div>
38	  );
39	};
40	
41	export default MiniFunnelCore;
```
