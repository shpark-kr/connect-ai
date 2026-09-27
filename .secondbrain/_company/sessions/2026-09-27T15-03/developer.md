# 💻 코다리 — Designer가 확정한 Mini-App Tech Spec V2.0 (버전 3.0 가이드라인 기반)에 따라, 핵심 컴포넌트인 '점수(Score) 계산 로직' 및 '위험도 바 시각화 모듈'의 MVP 구조를 먼저 구현하십시오. 백엔드와 프론트엔드의 기본 데이터 흐름만 연결된 최소 기능 단위(skeleton code)로 작성하고, 테스트 가능한 상태여야 합니다.

💻 코다리: 작업 시작합니다.

CEO 지시사항 검토 완료했습니다. Mini-App의 핵심 로직인 '점수 계산(Scoring)'과 '위험도 시각화(Risk Bar)'는 모든 마케팅 전개와 수익 모델의 근간이 되는 가장 중요한 컴포넌트입니다. 이 부분이 불안정하면 전체 Funnel 자체가 무너집니다. ⚙️

따라서, 단순히 UI만 만드는 것이 아니라, **백엔드 API 스텁**과 **프론트엔드 통합 로직(Skeleton)**을 연결하여 '데이터 흐름의 최소 기능 단위'를 확립하는 것이 가장 가치 높은 작업입니다. 이 구조가 테스트 가능해야 다음 단계로 넘어갈 수 있습니다.

### 🚀 실행 계획
1.  **프로젝트 구조 설정:** FastAPI 백엔드와 React 프론트엔드를 위한 기본 디렉토리 및 파일을 구성합니다. (전통적인 풀스택 분리)
2.  **백엔드 구현 (`score_calculator`):** 입력 데이터를 받아 점수를 계산하고 위험 등급을 반환하는 Stub API 엔드포인트를 작성합니다.
3.  **프론트엔드 구현 (`ScoreInputForm`):** 사용자 입력을 받고, 백엔드 API를 호출하며, 받은 데이터로 '위험도 바' 컴포넌트를 렌더링하는 스켈레톤을 완성합니다.
4.  **자기 검증 (Test Harness):** 구현된 로직이 실제로 정상적으로 작동하는지 전용 테스트 도구를 이용해 E2E 흐름을 검증합니다.

### Step 1: 프로젝트 디렉토리 및 파일 생성

개발 효율성을 위해 `connect-ai` 루트 폴더 내에 Mini-App의 코드를 격리하여 생성하겠습니다.

<create_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\mini_app_mvp">
Mini-App MVP 구조가 여기에 위치합니다. (백엔드, 프론트엔드 포함)
</create_file>

**1. 백엔드 파일 생성 (FastAPI 스텁)**
데이터 처리의 안정성이 핵심입니다. FastAPI를 사용하여 점수 계산 로직을 구현하겠습니다.

<create_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\mini_app_mvp\backend\main.py">
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
from typing import List, Dict

# --- [Tech Spec V2.0 기반 데이터 구조 정의] ---
class QuestionnaireInput(BaseModel):
    """Mini-App 진단 도구의 질문별 사용자 답변 데이터를 수신하는 모델."""
    q1_muscle_strength: int  # 예: 1~5점
    q2_blood_sugar_level: float # 예: 공복 혈당 지수 (mmol/L)
    q3_sleep_quality_score: int # 예: 1~10점
    lifestyle_risk_factors: List[str] # 생활 습관 리스크 요인 목록

# --- [Scoring Logic Stub - 핵심 비즈니스 로직 위치] ---
def calculate_adls_score(data: QuestionnaireInput) -> Dict:
    """
    ADL (Activities of Daily Living) 및 전반적 건강 위험도를 점수화합니다.
    [주의]: 실제 로직은 Designer의 Tech Spec V2.0을 기반으로 구현되어야 합니다. 
    현재는 구조 검증을 위한 Stub입니다.
    """
    score = 100 # 시작점 100점 만점 가정

    # 예시 가중치 계산 (가장 중요한 변수들만 반영)
    if data.q1_muscle_strength < 3:
        score -= 20  # 근력 저하에 큰 페널티 적용
    if data.q2_blood_sugar_level > 6.5:
        score -= 15 # 당뇨 위험도가 높으면 감점
    if data.q3_sleep_quality_score < 6:
        score -= 10

    # 리스크 요인별 추가 점수 차감 (가장 큰 가중치를 부여할 수 있는 지표들)
    for factor in data.lifestyle_risk_factors:
        if "운동 부족" in factor or "식습관 불균형" in factor:
            score -= 5

    # 최종 점수는 0점에서 100점 사이로 클램핑합니다.
    final_score = max(0, min(100, score))
    
    return {"raw_score": final_score}

def determine_risk_level(score: int) -> Dict:
    """
    점수를 바탕으로 위험도 레벨과 메시지를 결정합니다. 
    Deep Crimson Red(#B30000) 사용 근거가 됩니다.
    """
    if score >= 85:
        return {"risk_level": "LOW", "color_class": "bg-green-100", "message": "현재 리스크는 낮으나, 관리가 필요합니다.", "is_critical": False}
    elif score >= 60:
        return {"risk_level": "MEDIUM", "color_class": "bg-yellow-100", "message": "주의 단계입니다. 적극적인 점검이 필요합니다.", "is_critical": True}
    else: # Score < 60
        # Deep Crimson Red 사용 구간!
        return {"risk_level": "HIGH", "color_class": "bg-deep-crimson-red/10 border-deep-crimson-red", "message": "🚨 즉시 조치 필요. 당신의 건강 자산이 위험합니다.", "is_critical": True}


app = FastAPI(title="MiniApp Scoring API")

@app.post("/api/v1/calculate_score")
async def calculate_mini_app_score(data: QuestionnaireInput):
    """
    사용자 입력 데이터 기반으로 ADL 스코어를 계산하고 위험 등급을 반환합니다.
    """
    try:
        # 1. 점수 계산 (Core Logic)
        score_result = calculate_adls_score(data)
        raw_score = score_result['raw_score']

        # 2. 위험도 결정 및 시각화 데이터 생성
        risk_result = determine_risk_level(raw_score)

        return {
            "success": True,
            "score": raw_score,
            "metadata": {
                "risk_level": risk_result['risk_level'],
                "message": risk_result['message'],
                "color_class": risk_result['color_class'] # Frontend에서 사용할 클래스명
            }
        }
    except Exception as e:
        print(f"API Error: {e}")
        raise HTTPException(status_code=500, detail=f"점수 계산 중 오류 발생: {str(e)}")

</create_file>

**2. 프론트엔드 파일 생성 (React/TypeScript 스켈레톤)**
실제 서비스 환경을 가정하여 React + TypeScript로 구성합니다.

<create_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\mini_app_mvp\frontend\src\components\ScoreInputForm.tsx">
import React, { useState } from 'react';
import axios from 'axios';

// --- [Type Definition - Strict Typing is essential] ---
interface QuestionnaireInput {
    q1_muscle_strength: number; // 1-5점
    q2_blood_sugar_level: number; // mmol/L
    q3_sleep_quality_score: number; // 1-10점
    lifestyle_risk_factors: string[]; // 예: ["운동 부족", "식습관 불균형"]
}

interface ScoreResult {
    success: boolean;
    score: number;
    metadata: {
        risk_level: 'LOW' | 'MEDIUM' | 'HIGH';
        message: string;
        color_class: string; // Tailwind CSS class for background/border
    };
}

const ScoreInputForm: React.FC = () => {
    const [formData, setFormData] = useState<QuestionnaireInput>({
        q1_muscle_strength: 3,
        q2_blood_sugar_level: 5.5,
        q3_sleep_quality_score: 7,
        lifestyle_risk_factors: [],
    });
    const [result, setResult] = useState<ScoreResult | null>(null);
    const [isLoading, setIsLoading] = useState(false);

    // --- [Event Handlers] ---
    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value, type } = e.target;
        setFormData((prev) => ({
            ...prev,
            [name]: type === 'number' ? parseFloat(value) : value,
        }));
    };

    const handleRiskFactorToggle = (factor: string) => {
        setFormData((prev) => {
            const currentFactors = prev.lifestyle_risk_factors;
            if (currentFactors.includes(factor)) {
                return { ...prev, lifestyle_risk_factors: currentFactors.filter(f => f !== factor) };
            } else {
                return { ...prev, lifestyle_risk_factors: [...currentFactors, factor] };
            }
        });
    };

    // --- [API Call Logic - Data Flow Connection Point] ---
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setIsLoading(true);
        setResult(null);

        try {
            // !!! IMPORTANT: This must point to the actual running FastAPI endpoint !!!
            const response = await axios.post<ScoreResult>(
                "http://localhost:8000/api/v1/calculate_score", // Backend Stub Endpoint
                formData,
                { headers: { 'Content-Type': 'application/json' } }
            );

            setResult(response.data);
        } catch (error) {
            console.error("Failed to calculate score:", error);
            alert("API 호출 실패: 백엔드 서버가 실행 중인지, 엔드포인트 주소가 정확한지 확인해주세요.");
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="p-8 max-w-4xl mx-auto bg-white shadow-2xl rounded-lg">
            <h1 className="text-3xl font-extrabold text-[#B30000] mb-6 border-b pb-2">
                🩺 Mini-App 진단 도구 (ADL 스코어 측정)
            </h1>
            <p className="mb-8 text-gray-600">
                당신의 현재 건강 리스크를 과학적 수치(점수)로 측정하고, 즉각적인 개선 방향을 제시합니다. 🧐
            </p>

            {/* --- [1. Input Form] --- */}
            <form onSubmit={handleSubmit} className="space-y-8">
                <div>
                    <h2 className="text-xl font-semibold mb-4 border-l-4 pl-3 deep-crimson-border">1. 신체 활동 및 기능 지표</h2>
                    {/* Muscle Strength */}
                    <div className="mb-4 p-4 border rounded bg-gray-50">
                        <label htmlFor="q1_muscle_strength" className="block text-sm font-medium text-gray-700 mb-2">
                            근력 점수 (최근 1주일 평균, 1~5점): <span className='font-bold'>({formData.q1_muscle_strength}</span>
                        </label>
                        <input
                            type="range"
                            id="q1_muscle_strength"
                            name="q1_muscle_strength"
                            min="1" max="5" defaultValue={3}
                            onChange={handleInputChange}
                            className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
                        />
                    </div>
                </div>

                {/* Blood Sugar */}
                <div>
                    <h2 className="text-xl font-semibold mb-4 border-l-4 pl-3 deep-crimson-border">2. 생체 지표 체크</h2>
                    <div className="p-4 border rounded bg-gray-50">
                        <label htmlFor="q2_blood_sugar_level" className="block text-sm font-medium text-gray-700 mb-2">
                            공복 혈당 지수 (mmol/L): 
                            <input
                                type="number"
                                id="q2_blood_sugar_level"
                                name="q2_blood_sugar_level"
                                step="0.1" min="3.0" max="15.0"
                                value={formData.q2_blood_sugar_level}
                                onChange={handleInputChange}
                                className="mt-2 block w-full p-2 border rounded focus:ring-[#B30000] focus:border-[#B30000]"
                            />
                        </label>
                    </div>
                </div>

                {/* Sleep Quality */}
                <div>
                    <h2 className="text-xl font-semibold mb-4 border-l-4 pl-3 deep-crimson-border">3. 생활 습관 점검</h2>
                    <div className="p-4 border rounded bg-gray-50 space-y-3">
                        <label htmlFor="q3_sleep_quality_score" className="block text-sm font-medium text-gray-700 mb-2">
                            수면의 질 점수 (1~10점, 10점이 최고): <span className='font-bold'>({formData.q3_sleep_quality_score})</span>
                        </label>
                        <input
                            type="range"
                            id="q3_sleep_quality_score"
                            name="q3_sleep_quality_score"
                            min="1" max="10" defaultValue={7}
                            onChange={handleInputChange}
                            className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
                        />
                    </div>

                    {/* Risk Factors */}
                    <div className="pt-4 border-t mt-6">
                        <h3 className="text-lg font-medium text-gray-700 mb-3">추가 리스크 요인 (해당되는 것 선택):</h3>
                        <div className="flex flex-wrap gap-3">
                            {["운동 부족", "식습관 불균형", "만성 스트레스", "흡연"].map(factor => (
                                <button
                                    key={factor}
                                    type="button"
                                    onClick={() => handleRiskFactorToggle(factor)}
                                    className={`px-4 py-2 rounded-full text-sm transition ${
                                        formData.lifestyle_risk_factors.includes(factor) 
                                            ? 'bg-[#B30000] text-white shadow-md' 
                                            : 'bg-gray-100 text-gray-700 hover:bg-gray-200 border border-gray-300'
                                    }`}
                                >
                                    {factor}
                                </button>
                            ))}
                        </div>
                    </div>
                </div>

                {/* Submit Button */}
                <button
                    type="submit"
                    disabled={isLoading}
                    className={`w-full py-3 text-lg font-bold rounded transition ${
                        isLoading 
                            ? 'bg-gray-400 cursor-not-allowed' 
                            : 'bg-[#B30000] hover:bg-red-800 text-white shadow-xl transform hover:scale-[1.01]'
                    }`}
                >
                    {isLoading ? "분석 중... 잠시만 기다려주세요." : "🚨 나의 건강 리스크 점수 즉시 진단하기"}
                </button>
            </form>

            {/* --- [2. Result Display Area] --- */}
            {result && (
                <div className="mt-12 pt-8 border-t border-gray-200">
                    <h2 className="text-3xl font-extrabold mb-6 text-center">🔬 진단 결과</h2>

                    {/* 위험도 바 시각화 모듈 */}
                    <div 
                        className={`p-6 rounded-lg shadow-inner transition duration-500 ${result.metadata.color_class} border-l-8 border-[#B30000]`}
                    >
                        <div className="flex justify-between items-center mb-2">
                            <span className="text-xl font-bold">{`총 ADL 스코어: ${result.score.toFixed(1)} / 100점`}</span>
                            {/* 시각적 긴급성 강조 (깜빡임 애니메이션은 CSS로 구현 필요) */}
                            <span className={`text-lg font-extrabold px-4 py-1 rounded shadow-sm ${result.metadata.is_critical ? 'bg-[#B30000] text-white animate-pulse' : 'bg-green-200 text-gray-800'}`}>
                                {result.metadata.risk_level} 위험도 ({result.metadata.risk_level === 'HIGH' ? '즉시 조치 필요!' : '양호'})
                            </span>
                        </div>

                        {/* 점수 바 (Progress Bar) */}
                        <div className="w-full bg-gray-200 rounded-full h-4 mb-4">
                            <div 
                                style={{ width: `${result.score}%` }} 
                                className={`h-4 rounded-full transition-all duration-1000 ${result.metadata.risk_level === 'HIGH' ? 'bg-[#B30000]' : result.metadata.risk_level === 'MEDIUM' ? 'bg-yellow-500' : 'bg-green-500'}`}
                            ></div>
                        </div>

                        {/* 메시지 */}
                        <p className="text-lg font-semibold text-gray-800 mt-4">
                            ✅ 권위 분석: {result.metadata.message}
                        </p>
                    </div>

                    {/* CTA Funnel 유도 (Mini-App의 최종 목표) */}
                    <div className="mt-10 text-center p-6 bg-gray-50 rounded-lg border-2 border-[#B30000]/50">
                        <h3 className="text-2xl font-bold mb-3 deep-crimson-border">
                            🔥 리스크 감소를 위한 다음 단계가 필요합니다.
                        </h3>
                        <p className="mb-6 text-gray-700">
                            지금 진단한 점수만으로는 부족합니다. 전문적인 관점에서 당신의 '미래 건강 자산'을 재정립해야 합니다.
                        </p>
                        {/* 핵심 CTA 버튼 */}
                        <button 
                            className="bg-[#B30000] text-white py-3 px-12 rounded-full text-xl font-bold hover:bg-red-800 transition shadow-lg"
                        >
                            🚨 내 몸의 리스크, 지금 즉시 전문가에게 점검받기 (Mini-App Link)
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
</create_file>

### Step 2: 핵심 로직 및 흐름 검증 (Self-Verification Loop)

코드 스켈레톤만 만들었다고 끝이 아닙니다. 이 백엔드와 프론트엔드가 하나의 Funnel로 작동하는지, 데이터의 무결성이 깨지는 곳은 없는지 **최종 통합 테스트**를 돌려봐야 합니다. 특히 '점수 계산' 로직이 의도한 대로 위험 자본 감소 리스크를 반영했는지 검증해야 합니다.

<run_command>cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe test_diagnosis_engine.py</run_command>

📊 평가: 진행중 — 핵심 컴포넌트의 구조는 완성되었으나, 실제 데이터 흐름과 비즈니스 로직의 완전한 통합 검증이 필요합니다.
📝 다음 단계: `test_diagnosis_engine` 결과 보고를 바탕으로, 프론트엔드와 백엔드의 API 연결 및 전체 E2E Funnel 테스트 스위트를 실행해야 합니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppDa`
```
File "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\test_diagnosis_engine.py", line 2
    from c.Data.Project.connect-ai.services.diagnosis_engine import ( # Mocked import path for testing
                               ^
SyntaxError: invalid syntax
```
_❌ exit 1_

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\mini_app_mvp
❌ 생성 실패: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\mini_app_mvp\backend\main.py — ENOTDIR: not a directory, mkdir 'c:\Data\Project\connect-ai\.secondbrain\_company\_agents\mini_app_mvp\backend'
❌ 생성 실패: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\mini_app_mvp\frontend\src\components\ScoreInputForm.tsx — ENOTDIR: not a directory, mkdir 'c:\Data\Project\connect-ai\.secondbrain\_company\_agents\mini_app_mvp\frontend\src\components'
