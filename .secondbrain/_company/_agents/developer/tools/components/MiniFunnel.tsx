import React, { useState, useCallback } from 'react';
import * as ReactDOM from 'react-dom/client';

// --- Constants & Types ---
const DEEP_CRIMSON_RED = '#B3001F'; // Deep Crimson Red Warning Color
const SOFT_GOLD = '#F5E6C7';       // Soft Gold Solution Color

/**
 * Funnel State Enum (시스템 상태 정의)
 */
type FunnelStatus = 'INITIAL' | 'WARNING' | 'LOADING' | 'SUCCESS' | 'ERROR';

/**
 * 가상의 API 호출 시뮬레이션 함수.
 * 이 함수는 네트워크 불안정성을 테스트하기 위해 의도적으로 실패할 수 있습니다.
 * @param attempt 현재 재시도 횟수 (1부터 시작)
 * @returns Promise<string> 성공 시 솔루션 데이터, 실패 시 에러 발생
 */
const callHealthCheckApi = async (attempt: number): Promise<string> => {
    console.log(`[API] Health Check Attempt #${attempt}...`);

    // 1차 시도(Attempt 1)는 항상 실패하게 설정하여 Warning 상태를 유발하고,
    // 2~3차 시도에서 성공하도록 강제합니다. (테스트 목적)
    if (attempt < 3) {
        throw new Error("NameResolutionError: Network connection failed or DNS lookup timed out.");
    }

    await new Promise(resolve => setTimeout(resolve, 800)); // 네트워크 지연 시뮬레이션
    return "{\"status\": \"stable\", \"score\": \"Excellent\", \"advice\": \"Mini-App 구독이 최적의 해결책입니다.\"}";
};


/**
 * MiniFunnel 컴포넌트: '위기 $\to$ 해결' 전환 프로토콜 Mock-up.
 * E2E 테스트가 가능하도록 모든 상태 전이를 명시적으로 관리합니다.
 */
const MiniFunnel: React.FC = () => {
    const [status, setStatus] = useState<FunnelStatus>('INITIAL');
    const [message, setMessage] = useState('');
    const [retryCount, setRetryCount] = useState(0);

    // 🚨 핵심 로직: API 호출 및 재시도/폴백 메커니즘 구현
    const handleTransition = useCallback(async () => {
        setStatus('WARNING'); // 1. 위기 인지 (Deep Crimson Red)
        setMessage("⚠️ 현재 데이터를 기반으로 할 때, 당신의 건강 지표는 '위험' 수준입니다. 근본적인 점검이 필요합니다.");

        setRetryCount(0);

        // 재시도 루프 및 에러 핸들링 구현
        const MAX_RETRIES = 3;
        let success = false;

        for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
            try {
                const resultData = await callHealthCheckApi(attempt); // API 호출 시뮬레이션
                
                // 성공하면 루프 탈출 및 상태 변경
                setRetryCount(attempt);
                setStatus('SUCCESS'); 
                setMessage(`✅ 데이터 점검 완료. (재시도 ${attempt}회). 결과: ${resultData}`);
                success = true;
                break;

            } catch (error) {
                const errorMessage = error instanceof Error ? error.message : "알 수 없는 네트워크 에러";
                console.warn(`[ERROR] Attempt ${attempt} failed: ${errorMessage}`);

                // 실패 시 Deep Crimson Red 경고 메시지 유지 및 재시도 횟수 증가
                setMessage(`🚨 데이터 연결 오류 (${errorMessage}). 잠시 후 자동 재확인합니다...`);
                setRetryCount(attempt);

                if (attempt === MAX_RETRIES) {
                    setStatus('ERROR'); // 최대 시도 실패 -> 최종 에러 상태
                    setMessage("❌ 모든 점검 경로가 불안정합니다. 전문가의 도움이 필요합니다.");
                    break; 
                }
            }
        }
    }, []);

    // 초기 로드 시 Funnel 실행 (자동 검증)
    React.useEffect(() => {
        handleTransition();
    }, [handleTransition]);


    // --- UI 렌더링 로직 ---
    const renderStatusCard = () => {
        let title = '';
        let description = '';
        let colorClass = 'bg-gray-100';

        switch (status) {
            case 'INITIAL':
                title = "Mini-App Funnel 시작";
                description = "데이터 점검을 위해 핵심 지표 분석을 시작합니다.";
                colorClass = 'bg-blue-50';
                break;
            case 'WARNING':
                title = "🔴 [경고] 데이터 불안정 감지";
                description = `현재 상태: ${message}. 근본적인 원인을 파악해야 합니다.`;
                colorClass = `bg-${DEEP_CRIMSON_RED}`; // Deep Crimson Red (강한 경고)
                break;
            case 'LOADING':
                title = "⏳ 데이터 분석 중...";
                description = "네트워크 연결을 확인하며 최적의 솔루션을 탐색합니다.";
                colorClass = `bg-yellow-50`; 
                break;
            case 'SUCCESS':
                title = "🌟 [해결] 최적의 솔루션 제안";
                description = `${message}. Mini-App 가입을 통해 안정성을 확보하세요.`;
                colorClass = `bg-${SOFT_GOLD}`; // Soft Gold (신뢰 기반 해결책)
                break;
            case 'ERROR':
                title = "🚨 시스템 실패: 재접속 필요";
                description = `${message}. 페이지를 새로고침하거나 나중에 다시 시도해 주세요.`;
                colorClass = `bg-red-200`; 
                break;
        }

        return (
            <div className={`p-8 rounded-xl shadow-2xl transition duration-500 ${colorClass}`}>
                <h2 className="text-3xl font-extrabold text-gray-900 mb-2">{title}</h2>
                <p className="text-lg text-gray-700 mb-4">{description}</p>
            </div>
        );
    };

    return (
        <div className="max-w-xl mx-auto p-8 bg-white rounded-lg shadow-2xl">
            <h1 className="text-4xl font-bold text-center mb-6 text-gray-900">Mini Funnel 진단 시스템</h1>
            
            {renderStatusCard()}

            {/* CTA: 핵심 전환 지점 */}
            <div className={`mt-8 p-6 rounded-lg shadow-md transition duration-500 ${status === 'SUCCESS' ? 'bg-green-100 border-l-4 border-green-500' : 'border-none'}`}>
                <h3 className="text-xl font-semibold mb-2 text-gray-800">다음 단계가 필요합니다.</h3>
                <p className="text-sm text-gray-600 mb-4">Mini-App Funnel을 통해 근본적인 해결책에 접근하세요.</p>
                <button 
                    onClick={() => alert("Mini-App으로 이동하는 로직 실행 (트래킹 API 호출)")}
                    disabled={status === 'LOADING'}
                    className={`w-full py-3 rounded-lg font-bold transition duration-200 ${status === 'SUCCESS' ? 'bg-green-600 hover:bg-green-700 text-white' : 'bg-gray-400 cursor-not-allowed'} ${status !== 'SUCCESS' && status !== 'INITIAL' ? 'text-red-600' : ''}`}
                >
                    {status === 'LOADING' ? '진단 중...' : (status === 'SUCCESS' ? '✅ Mini-App 구독 시작하기' : 'ℹ️ 더 알아보기')}
                </button>
            </div>

        </div>
    );
};

export default MiniFunnel;