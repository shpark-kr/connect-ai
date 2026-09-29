# 💻 코다리 — MiniFunnel V2.0을 위한 '데이터 로딩 실패(DATA_LOAD_FAIL)' 시나리오의 프로토타입 코드 구조를 작성해주세요. 이 코드는 이전 세션에서 정의된 Deep Crimson Red 테마와 공학적 위기감 UI 컴포넌트 팩을 사용해야 하며, 데이터가 정상적으로 로드되지 않았을 때 사용자에게 보여줄 'SYSTEM ALERT' 모달창의 상태 전이(State Transition) 및 API 호출 실패 로직(Mock Error Handling)을 포함하여 E2E 테스트 가능한 형태로 구현합니다.

💻 코다리: 작업 시작합니다.

CEO의 지시를 확인했습니다. MiniFunnel V2.0에 필요한 `DATA_LOAD_FAIL` 시나리오 프로토타입을 설계하는 것은 매우 중요한 안정성 강화 작업입니다. 단순히 UI만 만드는 게 아니라, **State Transition**과 **Mock Error Handling**, 그리고 기존의 **공학적 위기감(Deep Crimson Red)** 테마를 통합해야 하므로, E2E 테스트가 가능한 구조로 접근하겠습니다.

이 로직은 React/TypeScript 환경을 가정하고 컴포넌트 기반으로 설계하며, 실패 시나리오에서 핵심인 `try...catch`와 상태 관리를 명확히 분리하는 것이 중요합니다.

### ⚙️ 작업 계획 및 검증 절차

1.  **API Mocking:** 데이터 로딩의 성공/실패를 제어할 수 있는 가짜 API 함수를 먼저 정의하여, 테스트 환경을 만듭니다.
2.  **State Container 구현:** 데이터를 요청하고 그 상태(Loading $\to$ Success / Loading $\to$ Error)에 따라 다음 뷰로 전환하는 메인 로직 컴포넌트를 작성합니다.
3.  **UI Component 작성:** Deep Crimson Red 테마의 'SYSTEM ALERT' 모달을 완성하고, 실패 시나리오에서 보여지는 구체적인 오류 메시지 구조를 정의합니다.

### 🏗️ 구현 (파일 생성)

MiniFunnel 로직이 들어갈 폴더 구조와 핵심 컴포넌트들을 생성하겠습니다.

<create_file path="./src/hooks/useDataLoadingState.ts">
```typescript
// src/hooks/useDataLoadingState.ts
/**
 * 데이터 로딩 상태를 관리하는 커스텀 훅 (Custom Hook)
 * 에러 핸들링과 상태 전이를 중앙 집중화하여 테스트 가능하게 합니다.
 */
import { useState, useCallback } from 'react';

type LoadingState = 'IDLE' | 'LOADING' | 'SUCCESS' | 'ERROR';

interface DataResult<T> {
    data: T | null;
    state: LoadingState;
    error: Error | null;
}

/**
 * 가상의 데이터 로딩 API 호출 함수입니다. (Mock Service)
 * 이 함수는 실제 네트워크 지연 및 실패 시뮬레이션을 담당합니다.
 */
const mockFetchMiniFunnelData = async (): Promise<any> => {
    console.log("[API Mock]: MiniFunnel 핵심 진단 데이터를 요청합니다...");
    
    // 2초 지연을 통해 실제 네트워크 호출 시간 시뮬레이션
    await new Promise(resolve => setTimeout(resolve, 2000));

    // === FAILURE INJECTION POINT (실패 주입점) ===
    // 테스트를 위해 특정 조건에서 실패하도록 구현합니다.
    if (Math.random() < 0.3 || localStorage.getItem('simulateFail') === 'true') {
        console.error("[API Mock]: 데이터 로딩에 치명적인 오류 발생.");
        throw new Error("DATA_LOAD_FAIL: 필수 진단 데이터를 가져오는 데 실패했습니다. 네트워크 연결 또는 서버 측 문제일 수 있습니다. (HTTP 503)");
    }
    // ===========================================

    const mockData = {
        status: "SYSTEM_OK",
        diagnosisScore: Math.floor(Math.random() * 100) + 1,
        requiredActionCode: "A-922-C", // 예시 오류 코드
        nextStepUrl: "/diagnostics/success"
    };

    console.log("[API Mock]: 데이터 로딩 성공.");
    return mockData;
};


/**
 * 데이터를 불러오는 비즈니스 로직을 캡슐화하고 상태를 관리합니다.
 * @returns {DataResult<any>} 현재 로딩 결과와 상태
 */
export const useMiniFunnelDataLoader = () => {
    const [result, setResult] = useState<DataResult<any>>({
        data: null,
        state: 'IDLE',
        error: null
    });

    // 데이터 로딩 함수를 useCallback으로 감싸 재사용성을 높입니다.
    const loadData = useCallback(async () => {
        setResult({ data: null, state: 'LOADING', error: null });
        try {
            // 1. API 호출 실행 및 Mock Error Handling 적용
            const data = await mockFetchMiniFunnelData();
            
            // 2. 성공 시 상태 전이 (Success State Transition)
            setResult({ data: data, state: 'SUCCESS', error: null });

        } catch (e) {
            // 3. 실패 시 상태 전이 및 에러 객체 저장 (Error State Transition)
            const errorMessage = e instanceof Error ? e.message : "알 수 없는 오류가 발생했습니다.";
            setResult({ data: null, state: 'ERROR', error: new Error(errorMessage) });
        }
    }, []);

    // 초기 로드 시 자동 호출되는 패턴을 고려하여 loadData를 노출합니다.
    return { result, loadData };
};
```

<create_file path="./src/components/SystemAlertModal.tsx">
```tsx
// src/components/SystemAlertModal.tsx
import React from 'react';

interface SystemAlertProps {
    error: Error;
    onRetry: () => void; // 재시도 핸들러를 받습니다.
}

/**
 * [Deep Crimson Red] 테마의 시스템 경고(SYSTEM ALERT) 모달 컴포넌트입니다.
 * 공학적 권위감과 위기감을 조성하는 것이 핵심 목표입니다.
 */
const SystemAlertModal: React.FC<SystemAlertProps> = ({ error, onRetry }) => {
    // Deep Crimson Red 톤을 위한 스타일링 상수 정의 (CSS Placeholder)
    const deepRedBg = "bg-[#8B0000]"; // Deep Crimson Red
    const warningText = "text-red-400";

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 p-4">
            {/* 모달 컨테이너 */}
            <div className={`w-full max-w-lg ${deepRedBg} border-4 border-red-700 shadow-2xl p-8 rounded-xl transform transition duration-500 scale-100`}>
                
                {/* 헤더: 공학적 오류 코드 시각화 */}
                <div className="text-center mb-6">
                    <h2 className={`text-3xl font-mono tracking-widest ${warningText}`}>
                        SYSTEM ALERT [CODE: PENS-503]
                    </h2>
                    <p className="mt-2 text-xl font-semibold">진단 시스템 오류 발생</p>
                </div>

                {/* 본문: 실패 상세 내용 */}
                <div className="mb-8 bg-red-900/5 p-4 rounded-lg border-l-4 border-red-500">
                    <p className="text-sm font-mono mb-2 text-red-300">
                        ERROR CODE: {error.message.split(':')[1]?.trim() || 'UNKNOWN'}
                    </p>
                    <p className="text-lg text-white font-medium">
                        {/* 사용자에게 보여줄 요약 메시지 */}
                        진단 데이터를 불러오는 데 실패했습니다. 시스템에 일시적인 장애가 발생한 것으로 보입니다. 
                    </p>
                </div>

                {/* 액션 버튼 (상태 전이 유도) */}
                <div className="flex justify-center space-x-4">
                    <button 
                        onClick={onRetry} 
                        className={`px-6 py-3 text-white font-bold rounded-lg transition duration-150 hover:bg-red-700 bg-red-800`}
                        // 재시도는 즉각적인 액션(CTA)을 유도하여 사용자 참여를 높임
                    >
                        🔄 다시 시도 (Retry Check)
                    </button>
                    <button 
                        onClick={() => alert("진단가에게 문의하기")} 
                        className="px-6 py-3 text-red-200 font-bold rounded-lg transition duration-150 hover:bg-red-900/70 border border-red-600"
                    >
                        전문가 상담 요청
                    </button>
                </div>
            </div>
        </div>
    );
};

export default SystemAlertModal;
```

<create_file path="./src/pages/MiniFunnelDiagnostic.tsx">
```tsx
// src/pages/MiniFunnelDiagnostic.tsx
import React, { useState, useCallback } from 'react';
import { useMiniFunnelDataLoader } from '../hooks/useDataLoadingState';
import SystemAlertModal from '../components/SystemAlertModal';

/**
 * MiniFunnel V2.0 진단 페이지의 메인 컴포넌트입니다.
 * 데이터 로딩 상태 변화(LOADING -> SUCCESS / ERROR)에 따른 UI를 제어합니다.
 */
const MiniFunnelDiagnostic: React.FC = () => {
    // 훅을 사용하여 상태 관리와 로직 분리 (Clean Separation of Concerns)
    const { result, loadData } = useMiniFunnelDataLoader();
    
    const [isManuallyLoading, setIsManuallyLoading] = useState(false);

    /**
     * 데이터 로딩 핸들러: 버튼 클릭 시 호출됩니다.
     */
    const handleLoadData = useCallback(() => {
        if (result.state === 'LOADING') return; // 이미 로딩 중이면 무시
        setIsManuallyLoading(true);
        loadData().finally(() => {
            setIsManuallyLoading(false);
        });
    }, [result.state, loadData]);

    // ------------------------------------------
    // 1. LOADING 상태 렌더링
    if (result.state === 'LOADING') {
        return (
            <div className="p-8 text-center">
                {/* 공학적 로딩 스피너 */}
                <div className="animate-spin inline-block w-12 h-12 border-4 border-red-500 rounded-full mb-4" role="status"></div>
                <p className="text-xl text-gray-700">시스템 진단 중... 데이터를 가져오고 있습니다. 잠시만 기다려 주세요.</p>
                {/* T+Nms 로직을 위한 주석 (미래 기능) */}
                <p className="mt-2 text-sm font-mono">[STATUS: INITIALIZING MODULES...]</p>
            </div>
        );
    }

    // ------------------------------------------
    // 2. ERROR 상태 렌더링 (SYSTEM ALERT 모달 활성화)
    if (result.state === 'ERROR') {
        return (
            <>
                {/* 배경 콘텐츠는 비활성화된 느낌을 주고, 모달만 전면 노출 */}
                <div className="p-8">
                    <h2 className="text-3xl font-bold text-gray-500/70 mb-4">진단 불가 (Diagnosis Unavailable)</h2>
                    <p className="text-lg text-gray-600">현재 데이터를 불러오는 데 문제가 발생했습니다. 아래 경고창을 확인해 주세요.</p>
                </div>
                {/* SystemAlertModal 컴포넌트를 통해 오류를 시각화하고 재시도 유도 */}
                <SystemAlertModal 
                    error={result.error!} 
                    onRetry={handleLoadData} // 모달 내부에서 re-trigger
                />
            </>
        );
    }

    // ------------------------------------------
    // 3. SUCCESS 상태 렌더링 (최종 목표)
    if (result.state === 'SUCCESS' && result.data) {
        const data = result.data;
        return (
            <div className="p-8 bg-white rounded-xl shadow-lg border-t-4 border-[#8B0000]">
                <h2 className="text-3xl font-bold mb-6 text-[#8B0000]">✅ 진단 완료: 시스템 안정화 프로토콜 실행</h2>
                
                {/* 핵심 데이터 표시 */}
                <div className="space-y-4">
                    <div>
                        <p className="text-gray-500 font-semibold">현재 상태:</p>
                        <span className={`inline-block py-2 px-6 text-lg rounded-full ${data.status === 'SYSTEM_OK' ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'}`}>
                            {data.status}
                        </span>
                    </div>

                    <div className="flex justify-between items-center p-4 bg-gray-50 rounded-lg border">
                        <div>
                            <p className="text-sm font-semibold text-gray-600">진단 점수:</p>
                            <p className="text-3xl font-extrabold text-[#8B0000]">{data.diagnosisScore}/100</p>
                        </div>
                        <button 
                            onClick={() => console.log("다음 단계로 이동 시뮬레이션")}
                            className="px-6 py-2 bg-red-700 text-white rounded hover:bg-red-800 transition"
                        >
                            {data.requiredActionCode} 기반 다음 조치 확인하기 ➡️
                        </button>
                    </div>

                    <div className="p-4 border-t pt-6">
                        <p className="text-sm text-gray-500">다음 단계 URL (API Endpoint): {data.nextStepUrl}</p>
                        {/* CTA는 항상 시스템 안정화 과정을 강조 */}
                    </div>
                </div>
            </div>
        );
    }

    // ------------------------------------------
    // 초기/기본 렌더링 (IDLE)
    return (
        <div className="p-8 text-center max-w-xl mx-auto">
            <h2 className="text-3xl font-bold mb-6 text-[#8B0000]">MiniFunnel 진단 시스템</h2>
            <p className="mb-8 text-gray-700">
                사용자의 건강 데이터를 공학적으로 분석하여 현재 상태의 위험도와 필요한 해결책을 제시합니다.
            </p>

            {/* 로딩 버튼 (초기 액션 유도) */}
            <button 
                onClick={handleLoadData} 
                disabled={isManuallyLoading}
                className={`px-12 py-4 text-xl font-bold rounded-full transition duration-300 ${isManuallyLoading ? 'bg-gray-400 cursor-not-allowed' : 'bg-[#8B0000] hover:bg-red-900'} text-white`}
            >
                {isManuallyLoading ? '진단 중...' : '시스템 진단 시작 (Start Diagnosis)'}
            </button>

            <p className="mt-6 text-sm text-gray-500">
                💡 Tip: 이 버튼을 눌러 데이터 로딩 실패(DATA_LOAD_FAIL) 시나리오를 테스트해 보세요.
            </p>
        </div>
    );
};

export default MiniFunnelDiagnostic;
```

### 🐛 자기 검증 루프 실행 및 테스트 계획

작성한 코드는 컴포넌트와 훅으로 분리되었고, 특히 `useMiniFunnelDataLoader` 내부의 `mockFetchMiniFunnelData` 함수에 **실패 주입점(Failure Injection Point)**을 명확히 만들어 두었습니다. 이는 CEO가 요구하신 'Mock Error Handling'과 'E2E 테스트 가능성'을 보장합니다.

이제 이 로직이 의도대로 동작하는지, 특히 실패 시나리오의 상태 전이가 제대로 발생하는지 확인해야 합니다. `e2e_funnel_cta_test_suite`를 활용하여 MiniFunnel 진단 페이지 전체 흐름을 테스트하겠습니다.

<run_command>cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe e2e_funnel_cta_test_suite.py</run_command>

📊 평가: 진행중 — 핵심 로직 구조는 완성되었으나, 실제로 시스템 전체에 통합된 테스트를 통해 안정성 검증이 필요합니다.
📝 다음 단계: `e2e_funnel_cta_test_suite` 실행 결과를 분석하여, 데이터 실패 시나리오(DATA\_LOAD\_FAIL)가 의도한 대로 Catch되고 'SYSTEM ALERT' 모달이 팝업되는지 최종적으로 확인해야 합니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppDa`
```
=============================================

--- [🌐 Web Test] Funnel 'national_pension' 테스트 시작 ---
[✅ Data Injection]: 데이터 성공적으로 주입됨: 월 평균 150만원 부족
[❌ Web Flow ERROR]: 네트워크/요청 실패: HTTPSConnectionPool(host='www.onhyeon-site.com', port=443): Max retries exceeded with url: /signup/submit (Caused by NameResolutionError("HTTPSConnection(host='www.onhyeon-site.com', port=443): Failed to resolve 'www.onhyeon-site.com' ([Errno 11001] getaddrinfo failed)"))

--- [▶️ YouTube Test] Funnel 'national_pension' 테스트 시작 ---
[✅ Data Injection]: 링크 내부에 위험액 정보가 안전하게 포함됨.
[✅ Tracking Link Structure]: 예상 URL 생성 완료: https://analytics.example.com/track/?utm_source=youtube&funnel=national_pension&campaign=gap_cta&content=gap_cta
[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.


=============================================

--- [🌐 Web Test] Funnel 'health_insurance' 테스트 시작 ---
[⚠️ Data Injection WARN]: 데이터가 누락되었으나, CTA는 대체 텍스트를 안전하게 표시함.
[❌ Web Flow ERROR]: 네트워크/요청 실패: HTTPSConnectionPool(host='www.onhyeon-site.com', port=443): Max retries exceeded with url: /signup/submit (Caused by NameResolutionError("HTTPSConnection(host='www.onhyeon-site.com', port=443): Failed to resolve 'www.onhyeon-site.com' ([Errno 11001] getaddrinfo failed)"))

--- [▶️ YouTube Test] Funnel 'health_insurance' 테스트 시작 ---
[⚠️ Data Injection WARN]: 링크에 데이터 누락 대비 로직이 필요합니다.
[✅ Tracking Link Structure]: 예상 URL 생성 완료: https://analytics.example.com/track/?utm_source=youtube&funnel=health_insurance&campaign=gap_cta&content=gap_cta
[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.


=============================================

--- [🌐 Web Test] Funnel 'inheritance' 테스트 시작 ---
[✅ Data Injection]: 데이터 성공적으로 주입됨: 최소 3천만원 손실 우려
[❌ Web Flow ERROR]: 네트워크/요청 실패: HTTPSConnectionPool(host='www.onhyeon-site.com', port=443): Max retries exceeded with url: /signup/submit (Caused by NameResolutionError("HTTPSConnection(host='www.onhyeon-site.com', port=443): Failed to resolve 'www.onhyeon-site.com' ([Errno 11001] getaddrinfo failed)"))

--- [▶️ YouTube Test] Funnel 'inheritance' 테스트 시작 ---
[✅ Data Injection]: 링크 내부에 위험액 정보가 안전하게 포함됨.
[✅ Tracking Link Structure]: 예상 URL 생성 완료: https://analytics.example.com/track/?utm_source=youtube&funnel=inheritance&campaign=gap_cta&content=gap_cta
[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.

=============================================

[🚨 E2E 테스트 실패] 일부 필수 기능에서 오류가 감지되었습니다. 코드를 수정하고 재검증해야 합니다.
```
_✅_
