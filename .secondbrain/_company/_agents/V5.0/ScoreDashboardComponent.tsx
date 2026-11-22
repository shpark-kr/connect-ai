import React, { useState, useEffect } from 'react';
// Assuming the scoring function is available via a mocked API call
// import { mockApiCall, ScoreResult } from './dashboard_schema';

interface ScoreDashboardProps {
    initialPayload: any; // 실제 사용 시 스키마를 맞춰야 함
}

const ScoreDashboardComponent: React.FC<ScoreDashboardProps> = ({ initialPayload }) => {
    const [scores, setScores] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        // 🚨 실제 구현에서는 fetch('/api/v5.0/scores', { method: 'POST', body: JSON.stringify(initialPayload) })를 사용해야 합니다.
        // 여기서는 로직 테스트를 위해 Mock API 호출을 시뮬레이션합니다.
        const runAnalysis = async () => {
            setLoading(true);
            try {
                // 💡 핵심: 백엔드 서비스가 정의한 엔드포인트를 호출하는 구조
                console.log("🚀 Initiating V5.0 Scoring Engine Analysis...");
                await new Promise(resolve => setTimeout(resolve, 800)); // Simulate API call delay

                // Mock Result based on assumed successful backend calculation
                const mockResult: any = {
                    ciScore: initialPayload?.interactions.length > 1 ? Math.min(Math.random() * 0.4 + 0.6, 1) : 0.3, // High chance of high score if enough interactions exist
                    riskFitScore: Math.max(0.4, Math.random()),
                    isCriticalAlert: initialPayload?.contentMeta.severityLevel === 'High' && Math.random() > 0.7,
                    suggestedAction: "MiniFunnel CTA 재강조"
                };

                setScores(mockResult);

            } catch (e) {
                setError("데이터 분석 중 오류가 발생했습니다. 서버 로그를 확인해주세요.");
            } finally {
                setLoading(false);
            }
        };
        runAnalysis();
    }, [initialPayload]);


    if (loading) return <div className="dashboard-card">⚙️ V5.0 Scoring Engine 분석 중... 잠시만 기다려 주세요.</div>;
    if (error) return <div className="dashboard-card error">{error}</div>;

    const { ciScore, riskFitScore, isCriticalAlert, suggestedAction } = scores;

    // Critical Alert 상태에 따른 스타일링 로직
    const getAlertClass = () => {
        return isCriticalAlert ? "bg-red-600 animate-pulse" : (riskFitScore > 0.7 ? "bg-yellow-500" : "bg-green-500");
    };

    return (
        <div className="dashboard-container p-6 bg-gray-50 rounded-xl shadow-2xl">
            <h2 className="text-3xl font-bold mb-6 text-gray-800">V5.0 진단 대시보드: 의도 점수 & 위험 적합도</h2>

            {/* 🚨 Critical Alert Zone */}
            <div className={`p-4 rounded-lg shadow-lg mb-6 ${getAlertClass}`}>
                <h3 className="text-xl font-extrabold tracking-widest">
                    {'🔥 CRITICAL ALERT 🔥'.split('').join(' ')}
                </h3>
                <p className="mt-1 text-sm opacity-90">🚨 즉각적인 개입이 필요합니다. 다음 액션을 최우선으로 수행하세요.</p>
            </div>

            {/* Scoring Cards */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                {/* CI Score Card */}
                <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-blue-500">
                    <p className="text-sm font-semibold text-gray-500 uppercase">Content Intent Score (CI)</p>
                    <h3 className="text-4xl font-bold mt-1 text-blue-700">{ciScore.toFixed(2)}</h3>
                    <p className='text-sm text-gray-600'>사용자가 콘텐츠에 기울인 관심과 액션의 정도를 나타냅니다.</p>
                </div>

                {/* Risk Fit Score Card */}
                <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-red-500">
                    <p className="text-sm font-semibold text-gray-500 uppercase">Risk-Fit Score (RF)</p>
                    <h3 className="text-4xl font-bold mt-1 text-red-700">{riskFitScore.toFixed(2)}</h3>
                    <p className='text-sm text-gray-600'>현재 콘텐츠가 사용자에게 적절한 수준의 위험성을 전달하는지 나타냅니다.</p>
                </div>
            </div>

            {/* Suggested Action & Visualization */}
            <div>
                <h4 className="text-xl font-semibold mb-3">✅ 시스템 진단 및 다음 액션</h4>
                <div className="bg-indigo-50 p-4 rounded-lg shadow-inner border-l-4 border-indigo-600 mb-8">
                    <p className="font-bold text-indigo-800">💡 추천 액션: {suggestedAction}</p>
                </div>

                {/* Visualization Placeholder */}
                <h4 className="text-xl font-semibold mb-3">📊 점수 변화 추이 시각화 (Mockup)</h4>
                <div className="bg-gray-100 p-6 rounded-lg h-64 flex items-center justify-center text-gray-500 border border-dashed">
                    [여기에 D3.js/Chart.js를 이용한 CI Score 및 Risk-Fit Score의 시간 경과에 따른 그래프가 렌더링됩니다.]
                </div>
            </div>

        </div>
    );
}

export default ScoreDashboardComponent;