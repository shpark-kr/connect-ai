import React from 'react';

// 1. 스키마 기반의 Props 정의 (VoucherComparisonSchema.json 참조)
interface ComparisonFeature {
    featureName: string;
    conditionValue: string | boolean | number;
    requirementType: "must_meet" | "optional" | "not_applicable";
}

interface VoucherData {
    voucherName: string;
    regionIdentifier: string;
    supportEntity: string;
    comparisonFeatures: ComparisonFeature[];
    eligibilitySummary: string;
}

// 2. 컴포넌트 정의 (단일 책임 원칙 유지)
const VoucherComparatorComponent: React.FC<{ data: VoucherData }> = ({ data }) => {
    if (!data || !data.comparisonFeatures || data.comparisonFeatures.length === 0) {
        return <div className="p-4 text-red-500">⚠️ 비교할 데이터가 부족하거나 스키마를 따르지 않았습니다.</div>;
    }

    // 3. 렌더링 로직 (핵심: 모듈화된 테이블 구조)
    const renderComparisonTable = () => {
        return (
            <div className="my-6 bg-gray-50 p-4 rounded-lg shadow-inner">
                <h3 className="text-xl font-bold mb-4 text-blue-700">{data.voucherName} 비교 분석</h3>
                <table className="min-w-full divide-y divide-gray-200">
                    <thead>
                        <tr>
                            <th className="px-6 py-3 bg-blue-100 text-left text-xs font-medium uppercase tracking-wider w-4/12">비교 항목</th>
                            <th className="px-6 py-3 bg-blue-100 text-left text-xs font-medium uppercase tracking-wider w-3/12">조건 상세</th>
                            <th className="px-6 py-3 bg-blue-100 text-left text-xs font-medium uppercase tracking-wider w-3/12">필수 여부</th>
                        </tr>
                    </thead>
                    <tbody className="bg-white divide-y divide-gray-200">
                        {data.comparisonFeatures.map((feature, index) => (
                            <tr key={index}>
                                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{feature.featureName}</td>
                                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{String(feature.conditionValue)}</td>
                                <td className={`px-6 py-4 whitespace-nowrap text-sm font-bold ${
                                    feature.requirementType === "must_meet" ? "text-red-600 bg-red-50" : 
                                    feature.requirementType === "optional" ? "text-yellow-700 bg-yellow-50" : "text-green-700 bg-green-50"
                                }`}>{feature.requirementType}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        );
    };

    return (
        <div className="p-6 border rounded-xl shadow-lg bg-white">
            <h2 className="text-3xl font-extrabold text-gray-800 mb-1">{data.voucherName}</h2>
            <p className="text-md text-blue-600 mb-4">지역: {data.regionIdentifier} | 주체: {data.supportEntity}</p>
            {renderComparisonTable()}
            <div className="mt-6 p-3 border-l-4 border-yellow-500 bg-yellow-50 text-sm">
                <strong>✅ 최종 자격 요건 요약:</strong> {data.eligibilitySummary}
            </div>
        </div>
    );
};

export default VoucherComparatorComponent;