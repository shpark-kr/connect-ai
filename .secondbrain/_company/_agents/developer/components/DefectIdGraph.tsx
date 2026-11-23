"use client"; // Next.js 클라이언트 컴포넌트임을 명시합니다.

import React, { useState, useEffect } from 'react';
import { calculateDefectDiagnosis } from '../lib/apiService';
import { DiagnosticResult } from '../types';

// Defect ID 그래프의 핵심 시각화 컴포넌트입니다.
const DefectIdGraph: React.FC = () => {
    // 1. 상태 관리 (State Management) 정의
    const [diagnosis, setDiagnosis] = useState<DiagnosticResult | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    // 2. 데이터 로딩 및 모킹 API 호출 (useEffect Hook 사용)
    useEffect(() => {
        const loadDiagnosis = async () => {
            setIsLoading(true);
            setError(null);
            try {
                // ★★★ 핵심: mock API를 호출하여 Critical Gap 데이터를 받아옵니다.
                const result = await calculateDefectDiagnosis({}); 
                setDiagnosis(result);

            } catch (e) {
                console.error("Failed to load diagnosis:", e);
                setError("진단 데이터 로드에 실패했습니다. 네트워크 상태를 확인해주세요.");
            } finally {
                setIsLoading(false);
            }
        };
        loadDiagnosis();
    }, []);

    // 3. 렌더링 로직 (Rendering Logic) - State 기반 분기 처리
    if (isLoading) {
        return <div className="p-10 text-center bg-gray-50 min-h-[400px] flex items-center justify-center"><span className="animate-spin inline-block w-8 h-8 border-b-2 border-red-600 rounded-full"></span><p className="ml-3 text-lg text-gray-700">진단 엔진을 구동하는 중입니다... 잠시만 기다려주세요.</p></div>;
    }

    if (error) {
        return <div className="p-10 bg-red-50 border border-red-300 text-red-700 rounded max-w-xl mx-auto">{error}</div>;
    }

    // 4. 최종 진단 결과 출력 (데이터가 성공적으로 들어왔을 때)
    if (!diagnosis) return null;


    return (
        <div className={`p-8 ${diagnosis.isCriticalGap ? 'bg-red-100 border-l-8 border-red-600 shadow-xl' : 'bg-green-50 border-l-8 border-green-600'} rounded-lg max-w-3xl mx-auto`}>
            <h2 className="text-3xl font-bold mb-2 text-gray-900">{diagnosis.diagnosisName}</h2>
            {/* Critical Gap 경고 배지 */}
            {diagnosis.isCriticalGap && (
                <div className="bg-red-600 text-white py-1 px-3 rounded-full font-bold text-sm tracking-wider animate-pulse mb-4 inline-block">
                    🚨 CRITICAL GAP 경고: 즉각적인 관리가 필요합니다. 🚨
                </div>
            )}

            <div className="space-y-6 mt-8">
                {diagnosis.dataPoints.map((point, index) => (
                    <div key={index} className="p-4 border rounded-lg bg-white shadow-sm transition duration-300 hover:shadow-md">
                        <h3 className="text-xl font-semibold text-gray-800 mb-2">{point.name}</h3>

                        {/* 그래프 시각화 영역 (임시) */}
                        <div className="flex justify-between items-end h-16 border-b pb-1">
                            {/* 1. 현재 값 막대 (Current Value Bar) */}
                            <div style={{ height: `${(point.currentValue / 200) * 100}%` }} className={`w-full transition-all duration-700 ${diagnosis.isCriticalGap ? 'bg-red-500 hover:bg-red-600' : 'bg-green-500 hover:bg-green-600'} relative flex items-end justify-center`}>
                                <span className="text-sm font-bold text-white absolute -top-5">{point.currentValue}</span>
                            </div>

                             {/* 2. 임계치 막대 (Threshold Bar) */}
                            <div style={{ height: `${(point.threshold / 200) * 100}%` }} className="w-1/4 bg-gray-300 relative flex items-end justify-center">
                                <span className="text-xs font-bold text-gray-700 absolute -top-5">{point.threshold}</span>
                            </div>

                        </div>

                        {/* Gap 수치와 해석 */}
                        <div className="mt-3 pt-2 border-t flex justify-between items-center">
                            <p className={`text-lg font-bold ${point.defectGap > 0 ? 'text-red-700' : 'text-green-700'}`}>
                                Gap 수치: {Math.abs(point.defectGap)} ({point.unit})
                            </p>
                            <p className={`text-sm font-medium ${diagnosis.isCriticalGap ? 'text-red-600' : 'text-gray-500'}`}>
                                {point.defectGap > 0 ? "⚠️ 위험 수준 초과 (High Risk)" : "✅ 정상 범위 유지"};
                            </p>
                        </div>

                    </div>
                ))}
            </div>
        </div>
    );
};

export default DefectIdGraph;