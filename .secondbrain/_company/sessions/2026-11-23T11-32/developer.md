# 💻 코다리 — 최근 발생한 E2E 통합 테스트 실패 지점('No such file or directory' 등)을 분석하고, Gap Score 계산 로직(Backend API/FastAPI)과 이를 소비하는 프론트엔드 컴포넌트(GapVisualizer.tsx) 간의 데이터 흐름 및 파일 경로 오류를 최우선으로 해결해 주세요. 시스템 안정성 확보가 목표이며, 수정된 코드는 단위 테스트(Unit Test)와 통합 테스트(E2E Test)를 모두 통과하는지 검증 후 결과를 제시해야 합니다.

💻 코다리: 작업 시작합니다. ⚙️

CEO 지시사항을 보니, 현재 시스템의 가장 치명적인 취약점(E2E 통합 실패)에 직면했군요. 이건 단순히 버그 수정 수준이 아니라 아키텍처 레벨에서 데이터 흐름과 의존성을 재검증해야 하는 문제입니다. 'No such file or directory' 같은 에러는 보통 상대 경로 문제, 혹은 로직이 기대하는 파일/데이터 구조가 실제로 제공되지 않을 때 발생합니다.

현재 작업 환경을 보니, `c:\Data\Project\Baro_KHNLU` 프로젝트 내에 Gap Score 관련 모듈(Python 백엔드와 TypeScript 프론트엔드)이 명확히 분리되어 있습니다. 이 흐름을 파악하는 것이 최우선입니다.

일단 코드가 어디서, 어떻게 깨지는지 정확한 맥락과 줄 번호를 잡아야 합니다. 가장 중요한 세 파일부터 내용을 읽어보겠습니다.

<read_file path="c:\Data\Project\Baro_KHNLU\mvp_core\src\gap_score_calculator.py"/>
<read_file path="c:\Data\Project\Baro_KHNLU\mvp_core\api\main.py"/>
<read_file path="c:\Data\Project\Baro_KHNLU\mvp_core\frontend\src\GapVisualizer.tsx"/>

📊 평가: 진행중 — 코드를 읽어 현재의 데이터 흐름, 경로 의존성, 그리고 프론트와 백엔드 간의 계약(Contract)을 파악하는 것이 가장 중요합니다.
📝 다음 단계: 파일 내용을 검토한 후, Path 및 Data Serialization 오류가 발생하는 지점을 특정하고 수정 작업을 진행하겠습니다.

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\Baro_KHNLU\mvp_core\src\gap_score_calculator.py (59줄, 2.7KB)
```
 1	from typing import Dict, Any
 2	
 3	# 상수 정의: 정상 범위를 명시하여 긴급성 극대화 (1.0 mg/L)
 4	NORMAL_CRP_THRESHOLD = 1.0
 5	CRITICAL_SCORE_THRESHOLD = 3.0 # 예시 임계값
 6	
 7	def calculate_gap_score(metrics: Dict[str, float]) -> Dict[str, Any]:
 8	    """
 9	    제공된 건강 지표를 기반으로 Gap Score와 위험 레벨을 계산한다.
10	    Gap Score는 현재 수치와 정상 범위 간의 시간적 손실 추이(Slope)에 비례하여 점수를 매긴다.
...
```
📖 읽기: c:\Data\Project\Baro_KHNLU\mvp_core\api\main.py (36줄, 1.4KB)
```
 1	from fastapi import FastAPI, HTTPException
 2	from pydantic import BaseModel
 3	from typing import Dict, Any
 4	# 로직 모듈 임포트 (절대 경로를 가정)
 5	from ../src.gap_score_calculator import calculate_gap_score 
 6	
 7	app = FastAPI(title="GapScore API", version="1.0")
 8	
 9	class HealthMetricsInput(BaseModel):
10	    """사용자로부터 받아야 하는 필수 건강 지표들을 정의합니다."""
...
```
📖 읽기: c:\Data\Project\Baro_KHNLU\mvp_core\frontend\src\GapVisualizer.tsx (127줄, 6.4KB)
```
 1	import React, { useState, useCallback } from 'react';
 2	// API 호출을 위한 더미 함수 (실제 환경에서는 fetch 또는 axios 사용)
 3	const fetchScore = async (metrics: any) => {
 4	    console.log("Calling backend API...");
 5	    // 실제로는 http://127.0.0.1:8000/api/v1/calculate_gap_score 로 호출되어야 합니다.
 6	    await new Promise(resolve => setTimeout(resolve, 500)); // 시뮬레이션 지연 시간
 7	    return { score: metrics.hs_crp * 2 + metrics.muscle_strength_loss_rate * 1.5, risk_level: "High", message: "API 응답 시뮬레이션 완료." };
 8	};
 9	
10	interface GapVisualizerProps {}
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\Baro_KHNLU\mvp_core\src\gap_score_calculator.py (59줄)
```
 1	from typing import Dict, Any
 2	
 3	# 상수 정의: 정상 범위를 명시하여 긴급성 극대화 (1.0 mg/L)
 4	NORMAL_CRP_THRESHOLD = 1.0
 5	CRITICAL_SCORE_THRESHOLD = 3.0 # 예시 임계값
 6	
 7	def calculate_gap_score(metrics: Dict[str, float]) -> Dict[str, Any]:
 8	    """
 9	    제공된 건강 지표를 기반으로 Gap Score와 위험 레벨을 계산한다.
10	    Gap Score는 현재 수치와 정상 범위 간의 시간적 손실 추이(Slope)에 비례하여 점수를 매긴다.
11	
12	    Args:
13	        metrics: {'hs_crp': float, 'muscle_strength_loss_rate': float} 등 핵심 지표 딕셔너리.
14	
15	    Returns:
16	        계산된 Gap Score와 위험 레벨 정보가 담긴 딕셔너리.
17	    """
18	    try:
19	        # 1. hs-CRP 기반 위험도 계산 (현재 수치가 정상 임계점을 넘으면 가중치 부여)
20	        crp_score = 0.0
21	        if metrics.get('hs_crp', 0.0) > NORMAL_CRP_THRESHOLD:
22	            # 초과분 * 가중치
23	            crp_score = (metrics['hs_crp'] - NORMAL_CRP_THRESHOLD) * 2.5
24	
25	        # 2. 근력 손실률 기반 위험도 계산 (시간 경과형 손실에 민감하게 반응)
26	        strength_loss = metrics.get('muscle_strength_loss_rate', 0.0)
27	        strength_score = strength_loss * 1.5
28	
29	        # 3. 최종 Gap Score 합산 및 정규화 (단순 합산으로 시작, 추후 복잡한 가중치 적용 예정)
30	        total_gap_score = crp_score + strength_score
31	        
32	        # 위험 레벨 결정 로직
33	        if total_gap_score >= CRITICAL_SCORE_THRESHOLD:
34	            risk_level = "Critical"  # 즉각적인 개입 필요 (Red Zone)
35	        elif total_gap_score >= 1.5:
36	            risk_level = "High"      # 주의 및 점검 권장 (Orange Zone)
37	        else:
38	            risk_level = "Low"       # 정상 범위 근접 (Green Zone)
39	
40	        return {
41	            "score": round(total_gap_score, 2),
42	            "risk_level": risk_level,
43	            "message": f"현재 Gap Score는 {total_gap_score}입니다. 위험 레벨: {risk_level}"
44	        }
45	
46	    except KeyError as e:
47	        print(f"Error: 필수 지표가 누락되었습니다. 어떤 지표가 필요한가요? -> {e}")
48	        return {"score": 0.0, "risk_level": "Error", "message": "데이터 입력 오류"}
49	    except Exception as e:
50	        print(f"An unexpected error occurred during scoring: {e}")
51	        return {"score": 0.0, "risk_level": "Error", "message": f"시스템 처리 오류: {str(e)}"}
52	
53	if __name__ == "__main__":
54	    # 테스트용 실행 예시 (실제 개발 환경에서는 pytest를 사용합니다)
55	    print("--- Gap Score Calculator Test Run ---")
56	    test_metrics = {'hs_crp': 1.5, 'muscle_strength_loss_rate': 0.8} # High Risk 예상
57	    result = calculate_gap_score(test_metrics)
58	    print(f"Input Metrics: {test_metrics}")
59	    print(f"Calculated Result: {result}")
```

[시스템: read_file 결과]
파일: c:\Data\Project\Baro_KHNLU\mvp_core\api\main.py (36줄)
```
 1	from fastapi import FastAPI, HTTPException
 2	from pydantic import BaseModel
 3	from typing import Dict, Any
 4	# 로직 모듈 임포트 (절대 경로를 가정)
 5	from ../src.gap_score_calculator import calculate_gap_score 
 6	
 7	app = FastAPI(title="GapScore API", version="1.0")
 8	
 9	class HealthMetricsInput(BaseModel):
10	    """사용자로부터 받아야 하는 필수 건강 지표들을 정의합니다."""
11	    hs_crp: float  # 고감도 염증 표지자 (mg/L)
12	    muscle_strength_loss_rate: float # 근력 감소율 (%)
13	
14	@app.post("/api/v1/calculate_gap_score", response_model=Dict[str, Any])
15	async def calculate_score(metrics: HealthMetricsInput):
16	    """
17	    사용자가 제출한 건강 지표를 바탕으로 Gap Score와 위험 레벨을 계산하고 반환합니다.
18	    이 엔드포인트는 프론트엔드의 핵심 데이터 소스입니다.
19	    """
20	    print(f"Received metrics for calculation: {metrics.dict()}")
21	    
22	    # 1단계에서 검증된 로직 모듈 호출
23	    result = calculate_gap_score(metrics.dict())
24	    
25	    if result['risk_level'] == "Error":
26	        raise HTTPException(status_code=400, detail=result['message'])
27	
28	    return {
29	        "success": True,
30	        "data": result
31	    }
32	
33	@app.get("/health")
34	async def health_check():
35	    """API 서버의 상태를 확인하는 헬스체크 엔드포인트."""
36	    return {"status": "ok", "service": "GapScore API is operational"}
```

[시스템: read_file 결과]
파일: c:\Data\Project\Baro_KHNLU\mvp_core\frontend\src\GapVisualizer.tsx (127줄)
```
  1	import React, { useState, useCallback } from 'react';
  2	// API 호출을 위한 더미 함수 (실제 환경에서는 fetch 또는 axios 사용)
  3	const fetchScore = async (metrics: any) => {
  4	    console.log("Calling backend API...");
  5	    // 실제로는 http://127.0.0.1:8000/api/v1/calculate_gap_score 로 호출되어야 합니다.
  6	    await new Promise(resolve => setTimeout(resolve, 500)); // 시뮬레이션 지연 시간
  7	    return { score: metrics.hs_crp * 2 + metrics.muscle_strength_loss_rate * 1.5, risk_level: "High", message: "API 응답 시뮬레이션 완료." };
  8	};
  9	
 10	interface GapVisualizerProps {}
 11	
 12	const getRiskColor = (level: string): { colorClass: string; label: string } => {
 13	    switch(level) {
 14	        case 'Critical': return { colorClass: 'bg-red-600', label: '🔴 Critical Risk' };
 15	        case 'High':     return { colorClass: 'bg-yellow-500', label: '🟠 High Alert' };
 16	        default:          return { colorClass: 'bg-green-500', label: '🟢 Low Risk' };
 17	    }
 18	};
 19	
 20	const GapVisualizer: React.FC<GapVisualizerProps> = () => {
 21	    const [metrics, setMetrics] = useState({ hs_crp: 1.0, muscle_strength_loss_rate: 0.2 });
 22	    const [result, setResult] = useState<{ score: number, risk_level: string, message: string } | null>(null);
 23	    const [isLoading, setIsLoading] = useState(false);
 24	
 25	    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
 26	        const { name, value } = e.target;
 27	        setMetrics(prev => ({ ...prev, [name]: parseFloat(value) || 0 }));
 28	        // 입력값이 바뀔 때마다 결과를 초기화하여 사용자가 다시 테스트하도록 유도합니다.
 29	        setResult(null); 
 30	    };
 31	
 32	    const handleCalculate = useCallback(async (e: React.FormEvent) => {
 33	        e.preventDefault();
 34	        setIsLoading(true);
 35	        setResult(null);
 36	        try {
 37	            // API 호출 시뮬레이션
 38	            const responseData = await fetchScore(metrics); 
 39	            setResult(responseData);
 40	        } catch (error) {
 41	            console.error("API Calculation Failed:", error);
 42	            alert("데이터 계산에 실패했습니다. 콘솔 로그를 확인해주세요.");
 43	        } finally {
 44	            setIsLoading(false);
 45	        }
 46	    }, [metrics]);
 47	
 48	    return (
 49	        <div className="p-8 max-w-xl mx-auto bg-white shadow-2xl rounded-lg">
 50	            <h2 className="text-3xl font-bold text-gray-900 mb-6 border-b pb-2">🧬 Gap Score 진단 엔진</h2>
 51	            <p className="text-sm text-gray-500 mb-8 p-4 bg-blue-50 rounded-md border-l-4 border-blue-400">
 52	                ⚠️ 본 진단은 개인의 건강 지표(hs-CRP, 근력 손실률)를 기반으로 '시간에 따른 측정 가능한 위험'을 예측합니다. 이 수치는 전문 의료진 상담을 대체할 수 없습니다.
 53	            </p>
 54	
 55	            {/* 입력 폼 */}
 56	            <form onSubmit={handleCalculate} className="space-y-6">
 57	                <div>
 58	                    <label htmlFor="hs_crp" className="block text-sm font-medium text-gray-700">
 59	                        현재 hs-CRP 수치 (정상: < 1.0 mg/L)
 60	                    </label>
 61	                    <input
 62	                        type="number"
 63	                        name="hs_crp"
 64	                        id="hs_crp"
 65	                        value={metrics.hs_crp}
 66	                        onChange={handleInputChange}
 67	                        className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-blue-500 focus:border-blue-500"
 68	                        step="0.1"
 69	                    />
 70	                </div>
 71	                 <div>
 72	                    <label htmlFor="muscle_strength_loss_rate" className="block text-sm font-medium text-gray-700">
 73	                        근력 손실률 (지난 6개월 평균, %)
 74	                    </label>
 75	                     <input
 76	                        type="number"
 77	                        name="muscle_strength_loss_rate"
 78	                        id="muscle_strength_loss_rate"
 79	                        value={metrics.muscle_strength_loss_rate}
 80	                        onChange={handleInputChange}
 81	                        className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-blue-500 focus:border-blue-500"
 82	                        step="0.1"
 83	                    />
 84	                </div>
 85	
 86	                <button 
 87	                    type="submit" 
 88	                    disabled={isLoading}
 89	                    className={`w-full py-3 px-4 border border-transparent rounded-md shadow-sm text-white font-medium ${
 90	                        isLoading ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500'
 91	                    }`}
 92	                >
 93	                    {isLoading ? '진단 중... 잠시만 기다려주세요.' : 'Gap Score 진단 실행'}
 94	                </button>
 95	            </form>
 96	
 97	            {/* 결과 출력 영역 */}
 98	            {result && (
 99	                <div className="mt-10 p-6 bg-gray-50 border rounded-lg shadow-inner">
100	                    <h3 className="text-xl font-bold text-gray-800 mb-4">✨ 진단 보고서</h3>
101	                    
102	                    {/* 위험도 시각화 컴포넌트 */}
103	                    <div className={`p-6 rounded-xl flex items-center justify-between ${getRiskColor(result.risk_level).colorClass} text-white shadow-lg`}>
104	                        <div>
105	                            <p className="text-sm opacity-90">Gap Score (측정 위험도)</p>
106	                            <h4 className="text-5xl font-extrabold">{result.score}</h4>
107	                        </div>
108	                        <div className="text-right">
109	                            <p className="text-lg opacity-90">위험 레벨</p>
110	                            <h3 className="text-3xl font-bold">{getRiskColor(result.risk_level).label}</h3>
111	                        </div>
112	                    </div>
113	
114	                    {/* 상세 메시지 및 CTA */}
115	                    <div className="mt-6 border-t pt-4">
116	                        <p className="text-gray-700 mb-3 italic">{result.message}</p>
117	                        <button className="bg-red-600 hover:bg-red-700 text-white py-2 px-5 rounded-full font-semibold transition duration-150">
118	                            🚨 전문가 통합 진단 예약하기 (CTA)
119	                        </button>
120	                    </div>
121	                </div>
122	            )}
123	        </div>
124	    );
125	};
126	
127	export default GapVisualizer;
```
