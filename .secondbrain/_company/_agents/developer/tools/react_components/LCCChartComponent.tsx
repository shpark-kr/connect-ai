// src/components/LCCChartComponent.tsx
import React, { useState, useEffect } from 'react';
import { validateAndNormalizeLccData, LccValidatedData } from '../utils/lccValidator';

interface LCCProps {
    rawData: any; // 원본 데이터를 받음
}

/**
 * 손실 대비 그래프를 렌더링하는 React 컴포넌트.
 * 데이터 유효성 검증 및 오류 처리를 최우선으로 합니다.
 */
const LCCChartComponent: React.FC<LCCProps> = ({ rawData }) => {
    const [validatedData, setValidatedData] = useState<LccValidatedData | null>(null);
    const [validationErrors, setValidationErrors] = useState<string[]>([]);

    useEffect(() => {
        // 1. 데이터 검증 및 전처리 실행
        const result = validateAndNormalizeLccData(rawData);
        setValidatedData(result.validatedData);
        setValidationErrors(result.errors);
    }, [rawData]);

    if (validationErrors.length > 0) {
        return (
            <div className="p-6 bg-red-50 border border-red-300 rounded-lg max-w-4xl mx-auto">
                <h2 className="text-xl font-bold text-red-700 mb-4">⚠️ 데이터 경고: LCC 렌더링 실패</h2>
                <p className="mb-3 text-sm text-gray-600">제공된 원본 데이터를 검증하는 과정에서 다음 오류가 발견되었습니다. 로직을 확인하고 재시도해 주세요.</p>
                <ul className="list-disc pl-5 space-y-1 text-sm text-red-800">
                    {validationErrors.map((error, index) => (
                        <li key={index}>{error}</li>
                    ))}
                </ul>
            </div>
        );
    }

    if (!validatedData) {
         return <div className="text-center p-10 text-gray-500">데이터를 로딩 중이거나, 유효성 검사 실패로 렌더링할 수 없습니다.</div>;
    }

    // 실제 차트 라이브러리(예: Recharts, D3)가 들어갈 영역 (현재는 Mockup으로 대체)
    return (
        <div className="p-8 bg-white shadow-xl rounded-lg max-w-4xl mx-auto border border-gray-200">
            <h1 className="text-3xl font-extrabold text-[#A31D2C] mb-2">{validatedData.title.primary}</h1>
            <h2 className="text-xl font-semibold text-[#B8860B] mb-8 border-b pb-4">
                {validatedData.title.secondary || "전문 컨설팅을 통한 기회비용 비교"}
            </h2>

            {/* 💡 실제 그래프 라이브러리 호출 지점 */}
            <div className="h-[350px] bg-gray-100 flex items-center justify-center rounded-lg border border-dashed">
                <p className="text-gray-400 text-lg">
                    [💡 LCC 그래프 렌더링 영역]<br/>
                    (데이터셋: {validatedData.dataSets.length}개)<br/>
                    활용 데이터: {JSON.stringify(validatedData.dataSets)}
                </p>
            </div>

            <div className="mt-8 grid md:grid-cols-2 gap-6 text-sm">
                {/* 범례/요약 정보 */}
                <div>
                    <h3 className="font-bold mb-3 text-lg">📈 데이터 분석 요약</h3>
                    <ul className="space-y-2">
                        {validatedData.dataSets.map(ds => (
                            <li key={ds.id} className="flex items-center gap-2">
                                <span style={{ backgroundColor: ds.colorCode, width: '10px', height: '10px' }}></span>
                                <span>{ds.label}: {ds.dataPoints.length}개 데이터 포인트 ({Math.max(...ds.dataPoints.map(p => p.value))}/{ds.dataPoints[0].unit})</span>
                            </li>
                        ))}
                    </ul>
                </div>
                {/* CTA 박스 */}
                <div className="p-4 bg-[#B8860B] text-white rounded-lg shadow-md">
                    <h3 className="font-bold mb-2">✨ 핵심 메시지 (CTA)</h3>
                    <p>이 격차(The Gap)를 메우는 것이 곧 수익화의 시작입니다. 지금 전문가 진단을 받으세요.</p>
                </div>
            </div>
        </div>
    );
};

export default LCCChartComponent;