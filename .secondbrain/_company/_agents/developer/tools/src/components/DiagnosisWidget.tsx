import React, { useState } from 'react';
// 실제 프로젝트에서는 백엔드 API 호출을 위한 axios 등을 사용합니다.

interface UserInputs {
    annualIncome: number; // 연간 소득 (원)
    yearsContributed: number; // 가입 기간 (년)
}

interface DiagnosisResult {
    success: boolean;
    message: string;
    gap_amount?: number;
    external_score?: number;
    report_date?: string;
    recommendation?: string;
    details?: any;
}

// 🎯 핵심 컴포넌트: 48px 터치 영역 및 상태 관리 적용
const DiagnosisWidget: React.FC = () => {
    const [inputs, setInputs] = useState<UserInputs>({ annualIncome: 0, yearsContributed: 0 });
    const [result, setResult] = useState<DiagnosisResult | null>(null);
    const [isLoading, setIsLoading] = useState(false);

    // 사용자 입력 변경 핸들러 (모든 input에 적용되어야 함)
    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setInputs(prev => ({
            ...prev,
            [name]: parseFloat(value) || 0 // 숫자로 변환하고 기본값 설정
        }));
    };

    // 진단 실행 로직 (백엔드 호출 시뮬레이션)
    const handleDiagnose = async () => {
        if (inputs.annualIncome <= 0 || inputs.yearsContributed < 1) {
            alert("⚠️ 필수 정보를 입력해 주세요.");
            return;
        }

        setIsLoading(true);
        setResult(null);
        console.log("진단 로직 실행 시작...");

        // 💡 실제로는 여기서 백엔드 API를 호출합니다. (axios.post('/api/diagnose', inputs))
        // 여기서는 간단한 비동기 시뮬레이션을 사용하여 Loading 상태와 에러 처리를 테스트합니다.
        await new Promise(resolve => setTimeout(resolve, 1500)); // 로딩 시간 대기

        // 백엔드 실패 확률을 모방하여 테스트합니다. (30% 확률로 실패 가정)
        if (Math.random() < 0.3) {
             setResult({
                success: false,
                message: "데이터 전송 오류: 서버가 일시적으로 과부하 상태입니다.",
                details: null
            });
        } else {
            // 성공 시뮬레이션 (실제 API 응답 구조와 유사하게)
            const simulatedGap = Math.floor(Math.random() * 5000000 + 10000000); // 1000만원 ~ 6000만원 Gap
            setResult({
                success: true,
                message: "전문 진단이 완료되었습니다.",
                gap_amount: simulatedGap,
                external_score: Math.floor(Math.random() * (95 - 70 + 1) + 70), // 70~95점
                report_date: new Date().toISOString().slice(0, 10),
                recommendation: "지금 당장 자산 포트폴리오 재검토가 필요합니다. 전문 상담을 받으세요.",
            });
        }

        setIsLoading(false);
    };

    // --- UI 렌더링 부분 (스타일은 Tailwind CDN 사용 가정) ---
    return (
        <div className="p-6 max-w-xl mx-auto bg-white shadow-2xl rounded-xl border-t-4 border-[#FFB800] transition duration-300">
            <h2 className="text-2xl font-bold mb-6 text-gray-800 flex items-center">
                ⚙️ 전문가 진단 위젯 
                <span className="ml-2 text-sm bg-[#74D9D5] p-1 rounded">실시간 리스크 분석</span>
            </h2>

            {/* 1. 입력 폼 (Accessibility/Touch Area Focus) */}
            <div className="mb-8 space-y-6">
                <h3 className="text-lg font-semibold text-gray-700 border-b pb-2">👤 사용자 기본 정보 입력</h3>

                {/* Input Field: 연간 소득 (48px 영역 확보) */}
                <div>
                    <label htmlFor="annualIncome" className="block text-sm font-medium text-gray-700 mb-1">
                        연간 총소득 (A): <span className="text-red-600">*</span>
                    </label>
                    <input
                        type="number"
                        id="annualIncome"
                        name="annualIncome"
                        value={inputs.annualIncome || ''}
                        onChange={handleInputChange}
                        placeholder="예) 50,000,000"
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-[#FFB800] focus:border-[#FFB800] transition duration-150 text-xl touch-area-48px" 
                        required
                    />
                </div>

                {/* Input Field: 가입 기간 (48px 영역 확보) */}
                <div>
                    <label htmlFor="yearsContributed" className="block text-sm font-medium text-gray-700 mb-1">
                        국민연금 가입 기간 (B): <span className="text-red-600">*</span>
                    </label>
                    <input
                        type="number"
                        id="yearsContributed"
                        name="yearsContributed"
                        value={inputs.yearsContributed || ''}
                        onChange={handleInputChange}
                        placeholder="예) 25"
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-[#FFB800] focus:border-[#FFB800] transition duration-150 text-xl touch-area-48px"
                        required
                    />
                </div>

                {/* CTA 버튼 (터치 영역 확보) */}
                <button
                    onClick={handleDiagnose}
                    disabled={isLoading}
                    className={`w-full py-3 rounded-lg font-bold text-white transition duration-200 
                        ${isLoading ? 'bg-gray-400 cursor-not-allowed' : 'bg-[#FFB800] hover:bg-[#e6a100] shadow-md'} 
                        touch-area-48px`}
                >
                    {isLoading ? (
                         <div className="flex items-center justify-center">
                            <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle><path className="opacity-80" d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0z"></path></svg>
                            분석 중... (잠시만 기다려주세요)
                         </div>
                    ) : "위험 진단 실행 (Gap 분석 및 API 호출)"}
                </button>
            </div>

            {/* 2. 결과 표시 영역 */}
            <div className="mt-8 pt-6 border-t">
                <h3 className="text-xl font-bold text-[#74D9D5] mb-4">💡 진단 결과</h3>

                {isLoading && (
                    <div className="p-6 bg-yellow-50 border-l-4 border-[#FFB800] text-gray-700 flex items-center">
                        <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-[#FFB800]" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle><path className="opacity-80" d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0z"></path></svg>
                        분석 엔진이 최신 데이터를 수집하는 중입니다. (지수 백오프 로직 작동 테스트...)
                    </div>
                )}

                {/* Success State */}
                {result && result.success ? (
                    <div className="space-y-6">
                        {/* Gap 경고 섹션 (가장 중요) */}
                        <div className={`p-5 rounded-lg shadow-lg border-l-8 ${result.gap_amount > 0 ? 'bg-red-50 border-[#FFB800]' : 'bg-green-50 border-green-600'}`}>
                            <h4 className="text-2xl font-bold text-gray-900 mb-2">🚨 재정적 리스크 경고: Gap 규모 파악</h4>
                            <p className="text-sm text-gray-600 mb-3">현재 공적 지원 시스템만으로는 생활 유지에 다음과 같은 'Gap'이 예상됩니다.</p>
                            <div className="text-5xl font-extrabold text-[#FFB800]">{result.gap_amount?.toLocaleString() || '0'}원</div>
                            <p className="mt-2 text-lg font-semibold">⚠️ 이 Gap을 메우기 위한 추가적인 자산/수입 계획이 시급합니다.</p>
                        </div>

                        {/* 상세 진단 정보 */}
                        <div className="grid grid-cols-2 gap-4 text-sm">
                            <DetailCard title="최신 보고서 기준일" value={result.report_date || 'N/A'} color="#74D9D5"/>
                            <DetailCard title="외부 리스크 점수 (100점 만점)" value={`${result.external_score}%`} isScore={true}/>
                        </div>

                        {/* 추천 및 CTA */}
                        <div className="p-4 bg-[#74D9D5] text-white rounded-lg">
                            <h5 className="font-bold mb-1">✅ 코다리의 전문 진단 요약:</h5>
                            <p>{result.recommendation}</p>
                        </div>
                    </div>
                ) : (
                    /* Error State */
                    result && !result.success ? (
                        <div className="p-6 bg-red-100 border-l-4 border-red-500 text-red-800 rounded-lg">
                            <h4 className="font-bold text-xl mb-2 flex items-center">
                                <svg className="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.5-1.73 2.5-3.73V5.5a1 1 0 00-1-1H6a1 1 0 00-1 1v11.73c0 2-1.5 3.73-2.5 3.73z"></path></svg>
                                진단 서비스 이용 불가 (에러 핸들링 테스트)
                            </h4>
                            <p className="mb-3"><strong>오류 메시지:</strong> {result.message}</p>
                            <p className="text-sm">데이터 수집 또는 API 연동 과정에서 문제가 발생했습니다. 잠시 후 다시 시도해 주세요.</p>
                        </div>
                    ) : (
                        /* 초기 상태 */
                        <div className="p-6 bg-gray-50 rounded-lg text-gray-600 border-l-4 border-dashed border-gray-300">
                            위젯을 사용하려면 상단의 사용자 정보를 입력하고 '진단 실행' 버튼을 눌러주세요.
                        </div>
                    )
                }
            </div>

        </div>
    );
};

// 재사용 가능한 하위 컴포넌트 (가독성 향상 및 48px 준수 명시)
interface DetailCardProps {
    title: string;
    value: string | number;
    color?: string;
    isScore?: boolean;
}

const DetailCard: React.FC<DetailCardProps> = ({ title, value, color, isScore }) => (
    <div className="p-3 bg-white border rounded-lg shadow-sm">
        <p className="text-xs font-medium text-gray-500">{title}</p>
        <p className={`mt-1 text-xl font-bold ${isScore ? 'text-[#FFB800]' : ''}`}>{value} {isScore ? '%' : ''}</p>
    </div>
);

export default DiagnosisWidget;