# 💻 코다리 — Designer가 완성한 'Mini-App Funnel의 최종 기술 명세서'를 바탕으로, 점수(Score) 기반의 동적 색상 변경 및 애니메이션 로직을 통합하여 개발 환경에 구현하십시오. 특히, Deep Crimson Red 계열의 위험도 측정 바(SVG 구조 포함)와 A/B 테스트용 CTA 버튼 3종의 상태 변화(클릭, 마우스 오버)를 완벽하게 코딩하고 디버깅해야 합니다. 모든 변경 사항은 커밋 메시지와 함께 Git에 기록하며, Mini-App이 실제 운영 환경에 배포될 수 있는 수준까지 완성하는 것을 목표로 합니다.

💻 코다리: 작업 시작합니다. ⚙️

CEO 지시사항 확인했습니다. Mini-App Funnel의 핵심인 점수 기반 동적 로직과 A/B 테스트 CTA 구현은 이 프로젝트의 성공을 좌우하는 가장 중요한 단계입니다. 코드 한 줄도 그냥 넘어갈 수 없죠. 특히 위험도가 시각적으로 체감되어야 사용자 행동이 유발되는데, 이건 단순히 스타일링 문제가 아니라 **상태(State) 관리와 로직** 문제니까요.

현재 `FunnelDiagnosticForm.tsx`가 메인 컴포넌트 역할을 하고 있으므로, 여기에 새로운 위험도 측정 바 (`RiskMeter`) 컴포넌트와 A/B 테스트 CTA 그룹을 통합하는 것이 가장 효율적입니다. 구조를 깨지 않으면서 기능을 확장해야 합니다.

**계획:**
1.  기존 `FunnelDiagnosticForm.tsx`의 현재 상태(특히 렌더링 로직)를 파악하여, 위험도 측정 바와 CTA가 삽입될 정확한 위치와 Prop 타입을 결정합니다.
2.  점수 기반 동적 애니메이션과 색상 매핑을 처리할 새로운 컴포넌트 `RiskMeterDisplay.tsx`를 생성합니다. (SVG 구조 포함).
3.  A/B 테스트용 3종 CTA 버튼을 관리하고, `:hover`, `:active` 상태 변화 로직 및 트래킹 플라세홀더가 완벽히 구현된 `ABTestCtaGroup.tsx`를 생성합니다.
4.  최종적으로 이 두 컴포넌트를 `FunnelDiagnosticForm.tsx`에 통합하고, E2E 테스트를 진행하여 안정성을 검증하겠습니다.

일단 첫 단계로, 메인 컨테이너 역할을 하는 `FunnelDiagnosticForm.tsx`의 내용을 먼저 읽겠습니다. 기존 로직을 파악해야 정확한 삽입 위치와 Prop Drilling 최소화가 가능합니다.

<read_file path="c:\Data\Project\FreqTrade\mini-app-funnel\src\components\FunnelDiagnosticForm.tsx"/>

📊 평가: 진행중 — 핵심 컴포넌트의 현재 구조 파악이 선행되어야 코딩을 시작할 수 있습니다.
📝 다음 단계: `FunnelDiagnosticForm.tsx`를 기반으로, 위험도 측정 바와 CTA 그룹 컴포넌트를 생성하고 통합하겠습니다.

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\FreqTrade\mini-app-funnel\src\components\FunnelDiagnosticForm.tsx (100줄, 5.3KB)
```
 1	// 주요 상태와 로직을 관리하는 뼈대 컴포넌트입니다. (React 환경 가정)
 2	import React, { useState, useMemo } from 'react';
 3	import { calculateRiskScore } from '../utils/scoreCalculator';
 4	import { DiagnosticInputs, DiagnosticResult } from '../types';
 5	
 6	/**
 7	 * FunnelDiagnosticForm: 사용자의 입력과 점수 계산을 통합하는 메인 폼 컴포넌트.
 8	 * 이 구조가 Mini-App의 핵심 상태 관리 레이어가 됩니다.
 9	 */
10	const initialInputs: DiagnosticInputs = {
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\FreqTrade\mini-app-funnel\src\components\FunnelDiagnosticForm.tsx (100줄)
```
  1	// 주요 상태와 로직을 관리하는 뼈대 컴포넌트입니다. (React 환경 가정)
  2	import React, { useState, useMemo } from 'react';
  3	import { calculateRiskScore } from '../utils/scoreCalculator';
  4	import { DiagnosticInputs, DiagnosticResult } from '../types';
  5	
  6	/**
  7	 * FunnelDiagnosticForm: 사용자의 입력과 점수 계산을 통합하는 메인 폼 컴포넌트.
  8	 * 이 구조가 Mini-App의 핵심 상태 관리 레이어가 됩니다.
  9	 */
 10	const initialInputs: DiagnosticInputs = {
 11	    age: 45,
 12	    systolicBp: 120,
 13	    diastolicBp: 80,
 14	    sleepHours: 7,
 15	    activityLevelScore: 60,
 16	};
 17	
 18	export const FunnelDiagnosticForm: React.FC = () => {
 19	    const [inputs, setInputs] = useState<DiagnosticInputs>(initialInputs);
 20	
 21	    // UseMemo를 사용하여 inputs가 변경될 때만 점수 계산을 수행하도록 최적화합니다.
 22	    const diagnosticResult: DiagnosticResult = useMemo(() => {
 23	        return calculateRiskScore(inputs);
 24	    }, [inputs]);
 25	
 26	    // 실제 폼 입력 핸들러 (이벤트 처리를 위한 기본 구조)
 27	    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
 28	        const { name, value, type } = e.target;
 29	        let newValue: any = value;
 30	
 31	        if (type === 'number') {
 32	            newValue = parseFloat(value) || 0;
 33	        }
 34	
 35	        setInputs(prev => ({ ...prev, [name]: newValue }));
 36	    };
 37	
 38	    return (
 39	        <div className="p-8 max-w-xl mx-auto bg-white shadow-2xl rounded-lg">
 40	            <h1 className="text-3xl font-bold mb-6 text-[#B30000]">🧬 Mini-App 진단 도구</h1>
 41	            
 42	            {/* 폼 섹션: 사용자가 직접 데이터를 입력하는 부분 */}
 43	            <div className="space-y-4 border p-6 rounded-md bg-gray-50">
 44	                {/* Age Input */}
 45	                <div>
 46	                    <label htmlFor="age" className="block text-sm font-medium text-gray-700">나이 (Age)</label>
 47	                    <input type="number" name="age" id="age" value={inputs.age} onChange={handleInputChange} 
 48	                           className="mt-1 block w-full p-2 border rounded-md focus:ring-[#B30000] focus:border-[#B30000]" />
 49	                </div>
 50	                 {/* BP Input (간소화) */}
 51	                <div className="flex space-x-4">
 52	                    <div>
 53	                        <label htmlFor="systolicBp" className="block text-sm font-medium text-gray-700">수축기 혈압 (Systolic)</label>
 54	                        <input type="number" name="systolicBp" id="systolicBp" value={inputs.systolicBp} onChange={handleInputChange} 
 55	                               className="mt-1 block w-1/2 p-2 border rounded-md focus:ring-[#B30000] focus:border-[#B30000]" />
 56	                    </div>
 57	                     <div>
 58	                        <label htmlFor="diastolicBp" className="block text-sm font-medium text-gray-700">이완기 혈압 (Diastolic)</label>
 59	                        <input type="number" name="diastolicBp" id="diastolicBp" value={inputs.diastolicBp} onChange={handleInputChange} 
 60	                               className="mt-1 block w-1/2 p-2 border rounded-md focus:ring-[#B30000] focus:border-[#B30000]" />
 61	                    </div>
 62	                </div>
 63	                 {/* ... 나머지 입력 필드 (수면 시간, 활동량 등) 생략 ... */}
 64	            </div>
 65	
 66	            <button 
 67	                onClick={() => console.log('Diagnosis Triggered')}
 68	                className="w-full py-3 mt-6 bg-[#B30000] text-white font-bold rounded-lg hover:bg-[#8a0000] transition duration-150"
 69	            >
 70	                진단 점수 확인하기 (Calculate Score)
 71	            </button>
 72	
 73	            {/* 결과 표시 영역 */}
 74	            <div className="mt-10 p-6 border-t pt-6">
 75	                <h2 className="text-xl font-bold mb-4">🔍 진단 결과</h2>
 76	                
 77	                {/* 🚨 위험도 측정 바 (여기에 동기화될 핵심 UI 요소) */}
 78	                <div className={`w-full h-8 rounded-full ${diagnosticResult.riskLevel === "Low Risk (양호)" ? 'bg-green-500' : diagnosticResult.riskLevel === "Moderate Risk (주의 필요)" ? 'bg-yellow-500' : 'bg-[#B30000]'}`}>
 79	                    <div 
 80	                        className="h-full w-[calc(100%-0%)] transition-all duration-700 ease-out" 
 81	                        style={`width: ${diagnosticResult.score}%`}
 82	                    ></div>
 83	                </div>
 84	
 85	                <p className="mt-4 text-2xl font-bold">최종 점수: <span className={/* 동적 색상 적용 */}> {`${diagnosticResult.score}`}</span> / 100점</p>
 86	                <p className={`text-lg mt-2 p-3 rounded ${diagnosticResult.riskLevel === "High Risk (위험 경고)" ? 'bg-red-100 text-red-800' : diagnosticResult.riskLevel === "Low Risk (양호)" ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'}`}>
 87	                    📌 위험 레벨: {diagnosticResult.riskLevel}
 88	                </p>
 89	
 90	                {/* CTA 섹션 (여기서 Funnel이 시작됨) */}
 91	                <div className="mt-6 p-4 border-l-4 border-[#B30000] bg-red-50">
 92	                    <h3 className="font-bold text-[#B30000]">⚠️ 코다리 검증: 위험도가 높습니다!</h3>
 93	                    <p>당신의 현재 점수를 바탕으로, 추가적인 전문 진단이 필요합니다. 지금 바로 Mini-App에서 상세 분석을 받아보세요.</p>
 94	                </div>
 95	            </div>
 96	        </div>
 97	    );
 98	};
 99	
100	export default FunnelDiagnosticForm;
```
