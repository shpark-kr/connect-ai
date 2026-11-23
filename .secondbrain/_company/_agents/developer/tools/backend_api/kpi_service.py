from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
import datetime
from typing import List

# --- 1. 데이터 계약 (Pydantic Models) 정의 ---
class KpiDataPoint(BaseModel):
    """특정 시점의 측정 가능한 KPI 값."""
    date: str # YYYY-MM-DD 형식
    value: float # 예: SMI 점수, ROM 각도

class PredictionPoint(BaseModel):
    """손실 예측 그래프에 사용될 데이터 포인트 (시간대별 손실 예상)."""
    time_index: int # 0부터 시작하는 시간 축 인덱스
    predicted_loss_value: float # 이 값이 높을수록 위험함 (Loss Velocity)

class KpiResponse(BaseModel):
    """KPI Visualizer 컴포넌트에 전달될 최종 데이터 구조."""
    user_id: str
    current_score: float = random.uniform(30, 95)
    is_critical: bool # 위기 임계점 도달 여부 (빨간 깜빡임 트리거)
    kpi_history: List[KpiDataPoint]
    loss_prediction_curve: List[PredictionPoint]

# --- 2. FastAPI 앱 초기화 및 엔드포인트 설정 ---
app = FastAPI(title="KPI Visualizer API", description="신체 기능 손실 예측 및 위기감 조성 서비스")

@app.get("/api/v1/kpi/diagnose", response_model=KpiResponse)
async def diagnose_kpi(user_id: str):
    """사용자 ID를 기반으로 KPI 진단 데이터를 생성하고, 손실 예측 곡선을 반환합니다."""
    print(f"--- [API] {user_id}의 KPI 진단 요청 수신 ---")

    # 가상의 사용자 데이터 생성 (재현성을 위해 고정 로직 사용)
    if user_id == "test-critical-user":
        # Critical 상태 시뮬레이션: 초기 점수가 낮고, 급격한 손실 예측이 필요함
        initial_score = random.uniform(35, 45)
        is_critical = True # 강제 크리티컬 설정

        kpi_history = [
            KpiDataPoint(date="2024-10-01", value=initial_score),
            KpiDataPoint(date="2024-11-01", value=initial_score * 0.95), # 약간의 감소
        ]
        # 손실 예측: 시간이 지날수록 급격히 하락하는 패턴을 강제합니다.
        loss_curve = [
            PredictionPoint(time_index=i, predicted_loss_value=20 + i * 3) for i in range(10)
        ]

    elif user_id == "test-normal-user":
        # Normal 상태 시뮬레이션: 점수가 안정적이고 위험하지 않음
        initial_score = random.uniform(75, 85)
        is_critical = False # 정상 상태 설정

        kpi_history = [
            KpiDataPoint(date="2024-10-01", value=initial_score),
            KpiDataPoint(date="2024-11-01", value=initial_score * 0.98), # 안정적 유지
        ]
        # 손실 예측: 완만한 곡선을 유지합니다.
        loss_curve = [
            PredictionPoint(time_index=i, predicted_loss_value=5 + i * 0.5) for i in range(10)
        ]

    else: # Default (Normal/Mildly At Risk)
        initial_score = random.uniform(50, 70)
        is_critical = False

        kpi_history = [
            KpiDataPoint(date="2024-10-01", value=initial_score),
            KpiDataPoint(date="2024-11-01", value=initial_score * 0.97),
        ]
        loss_curve = [
            PredictionPoint(time_index=i, predicted_loss_value=10 + i * 1) for i in range(10)
        ]

    return KpiResponse(
        user_id=user_id,
        current_score=initial_score,
        is_critical=is_critical, # Critical Flag 전달이 핵심입니다.
        kpi_history=kpi_history,
        loss_prediction_curve=loss_curve
    )

# --- 3. API 테스트 엔드포인트 (개발 용이성 확보) ---
@app.get("/test/simulate")
async def simulate_diagnosis():
    """테스트 목적으로 강제로 Critical 데이터를 반환합니다."""
    return await diagnose_kpi(user_id="test-critical-user")

# 개발자용 실행 명령어 (실제 사용 시에는 uvicorn을 통해 실행됨)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("kpi_service:app", host="127.0.0.1", port=8000, reload=True)

# NOTE: 이 서비스는 백엔드에서 '위기감'을 결정하는 권한을 가집니다.