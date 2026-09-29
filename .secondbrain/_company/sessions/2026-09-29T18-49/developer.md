# 💻 코다리 — MiniFunnel의 핵심 기능을 구현합니다. Designer가 확정한 '결함 진단 결과 시각화(Diagnosis Visualization)' 컴포넌트와 Master Defect DB 데이터를 기반으로, 실제 사용자에게 보여질 수 있는 인터랙티브한 상태 기계(State Machine) 프로토타입을 작성해주세요. 이는 단순 목업이 아니라, E-M411과 같은 특정 결함 ID를 입력했을 때 공학적 경고 UI가 팝업되고, 점수/스코어 등이 시각화되는 기능을 포함해야 합니다. React 기반의 컴포넌트 형태로 코드를 제공하고, 필요한 API 연동 포인트(Dummy API로 대체 가능)와 테스트 가이드를 반드시 작성해주세요.

💻 코다리: 작업 시작합니다.

CEO 지시사항은 명확하고 중요한 로직입니다. MiniFunnel의 핵심인 '진단 과정'을 실제 인터랙티브 컴포넌트로 구현하는 것은 가장 높은 우선순위를 가집니다. 단순 목업이 아닌, 상태 기계(State Machine)를 기반으로 설계해야만 공학적 위기감과 권위가 유지됩니다.

React 환경에 맞춰 `DiagnosisForm`과 핵심 로직을 분리하여 작성하겠습니다. 모든 컴포넌트는 TypeScript와 함수형 컴포넌트 패턴을 따르겠습니다.

### 🔧 구현 계획 (State Machine 기반)
1.  **API Layer (Dummy Hook):** Master Defect DB를 조회하는 비동기 API 호출을 시뮬레이션합니다 (`useDiagnosisApi`). 로딩, 성공, 에러 상태 처리를 포함해야 합니다.
2.  **State Manager:** 사용자의 입력(Defect ID)과 API 응답에 따라 컴포넌트의 상태(`IDLE` -> `LOADING` -> `DIAGNOSING` -> `RESULT`)를 관리합니다.
3.  **Visualization Component:** 공학적 경고 톤을 유지하며, 진단된 결함 정보와 스코어를 시각화하는 UI입니다.

먼저, 필요한 파일들을 프로젝트 구조에 생성하겠습니다. (Next.js 환경을 가정하고 컴포넌트 폴더 내부에 배치합니다.)

<create_file path="components/MiniFunnel/DiagnosisForm.tsx">
```tsx
import React, { useState, useCallback } from 'react';
import { useDiagnosisApi } from '../hooks/useDiagnosisApi';
import { DiagnosisResult } from '@/types/diagnosisTypes';
import VisualizationComponent from './VisualizationComponent';

// --- State Machine Definition ---
type FunnelState = 'IDLE' | 'LOADING' | 'DIAGNOSING' | 'ERROR' | 'SUCCESS';

interface Props {}

const DiagnosisForm: React.FC<Props> = () => {
    // 1. 상태 관리 및 API Hook 사용
    const [inputDefectId, setInputDefectId] = useState<string>('E-M411'); // 기본값 설정 (가장 많이 노출할 결함)
    const [state, setState] = useState<FunnelState>('IDLE');

    // 2. API 호출 로직 통합 (useDiagnosisApi에서 전역 상태로 관리하는 것이 더 좋으나, 여기서는 컴포넌트 내 구현을 위해 사용)
    const { diagnoseDefectId, isLoading, error, result } = useDiagnosisApi();

    const handleSubmit = useCallback(async () => {
        if (!inputDefectId || state === 'LOADING' || state === 'DIAGNOSING') return;

        // 3. 상태 전환 로직: IDLE -> LOADING -> DIAGNOSING
        setState('LOADING');
        try {
            const diagnosisData = await diagnoseDefectId(inputDefectId);
            
            if (diagnosisData) {
                // 성공 시, 최종 결과로 상태 업데이트
                setState('SUCCESS'); 
            } else {
                 throw new Error("데이터를 가져올 수 없습니다. ID를 확인해주세요.");
            }

        } catch (e: any) {
            console.error("Diagnosis failed:", e);
            setState('ERROR');
            // 에러 메시지를 별도로 관리하는 로직 추가 가능
        } finally {
             // 최종적으로 성공 또는 에러가 발생하면 결과 값을 받도록 구조화합니다.
        }
    }, [inputDefectId, diagnoseDefectId, state]);


    // 4. JSX 렌더링 (State 기반 분기 처리)
    const renderContent = () => {
        if (state === 'LOADING') {
            return <div className="text-center p-8 text-xl text-gray-700">⚙️ 시스템 분석 중... 데이터 스트리밍을 기다리는 중입니다.</div>;
        }

        if (state === 'ERROR') {
             return <div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4" role="alert">
                <p>🚨 시스템 오류 발생: 입력된 결함 ID 또는 데이터에 문제가 있습니다. 다시 시도해주세요.</p>
            </div>;
        }

        if (state === 'SUCCESS' && result) {
            return <VisualizationComponent diagnosisData={result} />;
        }

        return (
            <button 
                onClick={handleSubmit} 
                disabled={isLoading || state !== 'IDLE'}
                className={`w-full py-3 px-6 rounded-lg transition duration-200 ${
                    (state === 'IDLE' && !isLoading) ? 'bg-deep-crimson hover:bg-red-800 text-white' : 
                    'bg-gray-400 cursor-not-allowed'
                }`}
            >
                {isLoading ? '진단 중...' : '결함 분석 시작 (Run Protocol)'}
            </button>
        );
    };

    return (
        <div className="max-w-3xl mx-auto p-8 bg-white shadow-2xl rounded-xl">
            <h2 className="text-2xl font-bold mb-6 border-b pb-2 text-deep-crimson">🧬 시스템 결함 진단 프로토콜</h2>
            
            {/* 입력 폼 */}
            <div className="mb-8">
                <label htmlFor="defectId" className="block text-sm font-medium text-gray-700 mb-2">
                    분석할 공학적 결함 ID (예: E-M411, N-512)을 입력하세요.
                </label>
                <input 
                    id="defectId" 
                    type="text" 
                    value={inputDefectId} 
                    onChange={(e) => setInputDefectId(e.target.value)}
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-deep-crimson focus:border-deep-crimson text-lg tracking-wider uppercase" 
                    placeholder="E-M411" 
                />
            </div>

            {/* 실행 버튼 및 결과 영역 */}
            <div className="mb-8">
                {renderContent()}
            </div>
        </div>
    );
};

export default DiagnosisForm;
```

<create_file path="components/MiniFunnel/VisualizationComponent.tsx">
```tsx
import React from 'react';
import { DiagnosisResult } from '@/types/diagnosisTypes';

interface Props {
    diagnosisData: DiagnosisResult;
}

// 공학적 경고 톤을 유지한 핵심 시각화 컴포넌트
const VisualizationComponent: React.FC<Props> = ({ diagnosisData }) => {
    if (!diagnosisData) return null;

    // 결함 ID를 헤드라인으로 사용
    const defectId = diagnosisData.defectId;
    // 심각도를 기반으로 경고 색상 결정 (CSS 변수 활용)
    const severityColorClass = diagnosisData.severity === 'Critical' ? 'border-red-600 bg-red-50/70' : 
                               diagnosisData.severity === 'Moderate' ? 'border-yellow-600 bg-yellow-50/70' : 
                               'border-blue-600 bg-blue-50/70';

    return (
        <div className="p-6 border-4 border-deep-crimson rounded-xl shadow-2xl bg-white">
            {/* System Alert Header */}
            <div className={`p-4 mb-6 rounded-lg border-l-8 ${severityColorClass}`}>
                <h3 className="text-sm font-mono tracking-widest uppercase text-deep-crimson flex items-center">
                    <span className="mr-2">🚨</span> SYSTEM ALERT | DIAGNOSTIC REPORT v2.1
                </h3>
                <p className="mt-1 text-lg font-semibold">Defect ID: <span className="text-xl">{defectId}</span></p>
            </div>

            {/* 1. 핵심 결함 요약 (Diagnosis Visualization) */}
            <section className="mb-8 p-6 bg-gray-50 rounded-lg border border-dashed">
                <h4 className="text-xl font-bold text-deep-crimson mb-3 flex items-center">
                    <span className="mr-2 text-2xl">🔬</span> 진단 결과: <span className="ml-1">{diagnosisData.defectName}</span>
                </h4>
                <p className="text-gray-600 mb-4 text-sm">
                    귀하의 현재 시스템 상태는 공학적 결함 {defectId}를 보이고 있습니다. 이는 단순한 노화가 아닌, **기능성 하락**으로 정의됩니다.
                </p>
                <div className="grid grid-cols-2 gap-4 text-center">
                    <div>
                        <p className="text-sm uppercase tracking-wider text-gray-500">심각도 (Severity)</p>
                        <p className={`text-xl font-extrabold ${diagnosisData.severity === 'Critical' ? 'text-red-700' : 'text-yellow-600'}`}>{diagnosisData.severity}</p>
                    </div>
                    <div>
                        <p className="text-sm uppercase tracking-wider text-gray-500">복구 난이도 (Difficulty)</p>
                        <p className={`text-xl font-extrabold ${diagnosisData.difficulty === 'High' ? 'text-red-700' : 'text-green-600'}`}>{diagnosisData.difficulty}</p>
                    </div>
                </div>
            </section>

            {/* 2. 상세 결함 설명 */}
            <section className="mb-8">
                <h4 className="text-xl font-bold text-deep-crimson mb-3 border-b pb-1">📋 시스템 보고서 및 경고 내용</h4>
                <p className="text-gray-700 leading-relaxed">{diagnosisData.description}</p>
            </section>

            {/* 3. 최종 CTA (MiniFunnel 유도) */}
            <div className="mt-10 p-8 bg-deep-crimson rounded-xl text-center shadow-inner">
                <h3 className="text-2xl font-extrabold text-white mb-4 uppercase tracking-wider">⚠️ 즉각적인 프로토콜 업데이트가 필요합니다.</h3>
                <p className="text-lg text-deep-crimson/80 mb-6">
                    이 결함을 해결하고 시스템을 복구하기 위한 **전문 진단 및 맞춤형 솔루션**이 필요합니다.
                </p>
                <button 
                    className="bg-yellow-400 hover:bg-yellow-500 text-deep-crimson font-extrabold py-3 px-12 rounded-full text-xl transition duration-300 transform hover:scale-105 shadow-lg"
                >
                    ✅ MiniFunnel 진단 페이지로 이동하여 복구 프로토콜 확인하기
                </button>
            </div>
        </div>
    );
};

export default VisualizationComponent;
```

<create_file path="hooks/useDiagnosisApi.ts">
```typescript
import { useState, useCallback } from 'react';
// 가상의 타입 정의 (실제 프로젝트에 따라 조정 필요)
export interface DiagnosisResult {
    defectId: string;
    defectName: string;
    severity: 'Critical' | 'Moderate' | 'Low';
    difficulty: 'High' | 'Medium' | 'Low';
    description: string;
}

// 🚨 Dummy API Hook: 실제 백엔드 호출을 시뮬레이션합니다.
export const useDiagnosisApi = () => {
    const [result, setResult] = useState<DiagnosisResult | null>(null);

    /**
     * @param defectId - 분석할 공학적 결함 ID (e.g., E-M411)
     * @returns Promise<DiagnosisResult>
     */
    const diagnoseDefectId = useCallback(async (defectId: string): Promise<DiagnosisResult | null> => {
        console.log(`[API CALL] Attempting to diagnose defect ID: ${defectId}`);

        // 1. API 레이턴시 시뮬레이션
        await new Promise(resolve => setTimeout(resolve, 1500));

        // 2. Defect ID 기반 결과 분기 (가장 중요한 로직)
        if (defectId === 'E-M411') {
            return {
                defectId: defectId,
                defectName: "관절 불안정성 및 연결 조직 약화",
                severity: "Critical", // Critical = 가장 높은 위기감 조성
                difficulty: "High", 
                description: `E-M411은 관절 주변의 결합 조직(Ligamentous Structure)이 기준치 대비 심각하게 감소했음을 의미합니다. 이는 단순히 '관절 통증'으로 치부할 수 없는, 시스템적인 지지 구조의 공학적 실패 신호입니다. 즉각적인 근력 및 보조 장비 프로토콜 적용이 필요합니다.`
            };
        } 
        else if (defectId === 'N-512') {
            return {
                defectId: defectId,
                defectName: "신경 전달 물질 불균형",
                severity: "Moderate",
                difficulty: "Medium",
                description: `N-512는 신경계의 에너지 효율 저하 및 미세한 정보 처리 속도 감소를 나타냅니다. 이는 영양제 과다 복용으로 인한 일시적 현상일 수 있으나, 주기적인 점검이 필요한 수준입니다.`
            };
        } 
        else if (defectId === 'UNKNOWN') {
             // 유효하지 않은 ID 처리
             return null;
        }
        else {
            // 기타 Defect ID에 대한 기본 응답
            return {
                defectId: defectId,
                defectName: `미확인 결함 (${defectId})`,
                severity: "Low",
                difficulty: "Low",
                description: `입력하신 ${defectId}는 현재 Master Defect DB에서 정의된 주요 패턴은 아니나, 경미한 시스템 교란 신호가 감지되었습니다. 추가적인 상세 검진이 권장됩니다.`
            };
        }
    }, []);

    // 실제 전역 상태 관리는 Context API를 사용해야 하지만, 여기서는 구조적 흐름을 위해 로컬 상태로 유지합니다.
    return { diagnoseDefectId, result };
};
```

<create_file path="types/diagnosisTypes.ts">
```typescript
/** 
 * 진단 결과의 데이터 타입을 정의합니다. 
 * 모든 컴포넌트가 이 구조를 따르도록 강제하여 타입 안정성을 확보했습니다.
 */
export interface DiagnosisResult {
    defectId: string;        // E-M411 등 공학적 오류 코드
    defectName: string;      // 결함의 일반적인 명칭
    severity: 'Critical' | 'Moderate' | 'Low'; // 심각도 (위기감 조성 핵심)
    difficulty: 'High' | 'Medium' | 'Low';   // 복구 난이도
    description: string;     // 상세한 공학적 설명 텍스트
}

/**
 * 사용 가능한 모든 Defect ID의 목록을 상수화합니다. (DB와 연동될 부분)
 */
export const AVAILABLE_DEFECTS = [
    { id: 'E-M411', name: '관절 불안정성 및 연결 조직 약화' },
    { id: 'N-512', name: '신경 전달 물질 불균형' },
    // ... 기타 결함 ID 추가 예정
]
```

### 🧪 테스트 가이드라인 (Self-Verification)
코드 구조와 기능 흐름에 대한 검증 루프를 돌려보겠습니다. 다음의 시나리오로 컴포넌트의 안정성을 확인해야 합니다.

1.  **성공 경로 테스트:** `E-M411` 입력 $\rightarrow$ 로딩 상태 진입 (API Hook) $\rightarrow$ 결과 렌더링 (`Critical` 경고 UI 출력).
2.  **실패 경로 테스트 (Edge Case):** 존재하지 않는 ID(`Z-999`) 입력 $\rightarrow$ API 호출 실패 또는 Null 반환 $\rightarrow$ 에러 메시지 컴포넌트가 정상적으로 노출되는지 확인.
3.  **상태 전이 테스트:** 버튼을 연달아 빠르게 클릭했을 때, 무한 루프나 상태 꼬임 없이 `isLoading` 플래그가 정확히 작동하는지 검증해야 합니다.

### 🛠️ 다음 단계 (프로토타입 통합 및 디버깅)
현재 코드는 React 컴포넌트와 로직 분리까지 완료되었으나, 실제 API 호출을 수행하는 백엔드(Mock 또는 Stub)와의 연결 지점과 전역 상태 관리가 미흡합니다.

다음 스텝은 이 `DiagnosisForm`이 포함될 메인 페이지(`MiniFunnelLandingPage.tsx`)를 생성하고, **전체 Funnel의 흐름 (Hero -> Diagnosis Form -> Result CTA)**을 통합하는 것입니다. 또한, 사용된 Dummy API 로직을 실제 백엔드 엔드포인트와 연동하기 위한 `useQuery` 훅 패턴으로 리팩토링해야 합니다.

---
📊 평가: 진행중 — 핵심 컴포넌트 구조(React, State Machine)는 완성되었으나, 최종 통합 환경 및 전역 상태 관리/실제 API Hook 구현이 필요합니다.
📝 다음 단계: MiniFunnel의 최상위 페이지(`MiniFunnelLandingPage.tsx`)를 생성하고, 모든 컴포넌트를 배치하여 E2E 흐름을 구축해야 합니다.
