import json
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, ValidationError, Field

# ==============================================================================
# 1. 데이터 모델 정의 (Pydantic 기반 스키마 정의)
# 강제된 표준화: 모든 입력 데이터는 이 구조를 따라야 합니다.
# ==============================================================================

class FinancialDataPoint(BaseModel):
    """단일 재정적 데이터 포인트를 정의합니다."""
    data_id: str = Field(..., description="데이터셋의 고유 ID (예: 국민연금/퇴직연금)")
    year: int = Field(..., ge=2000, le=2100) # 연도 범위 제한
    value: float = Field(..., gt=0.0, description="해당 시점의 금액 값")

class GapDataPoint(BaseModel):
    """비교 분석을 위한 핵심 Gap 데이터를 정의합니다."""
    gap_id: str = Field(..., description="Gap 데이터셋 고유 ID (예: 비급여사각지대)")
    reference_value: float = Field(..., gt=0.0, description="기준가치 또는 예상 수령액")
    actual_loss_potential: float = Field(..., ge=0.0, description="실제 놓칠 수 있는 손실 잠재액 (Gap 크기)")

class VisualizationInputSchema(BaseModel):
    """최종 시각화 API 호출에 필요한 표준 JSON 스키마."""
    title: str = Field(..., description="차트 제목")
    data_points: List[FinancialDataPoint]
    gap_analysis: List[GapDataPoint]

# ==============================================================================
# 2. 핵심 비즈니스 로직 (calculate_loss_comparison)
# 재정적 손실 Gap을 계산하고 이를 표준화하는 함수입니다.
# ==============================================================================

def calculate_loss_comparison(data_points: List[FinancialDataPoint], gap_points: List[GapDataPoint]) -> Optional[Dict[str, Any]]:
    """
    주어진 데이터를 기반으로 재정적 손실 비교 분석을 수행합니다.
    이 로직은 Gap Area Chart의 핵심 백엔드 로직입니다.
    """
    if not data_points or not gap_points:
        print("⚠️ [ERROR] 필수 데이터 포인트가 부족하여 계산을 중단합니다.")
        return None

    # 가상의 복잡한 비교 분석 수행 (예: 연도별 성장률 대비 Gap의 변화 추적)
    total_potential_loss = sum(gap.actual_loss_potential for gap in gap_points)
    latest_value = max([d.value for d in data_points])

    print(f"✅ [INFO] 총 잠재 손실액 계산 완료: {total_potential_loss:,.0f}원")
    print(f"✅ [INFO] 최신 분석 데이터 기준값 확보: {latest_value:,.0f}원")

    # 최종 구조화된 결과를 반환합니다.
    return {
        "status": "SUCCESS",
        "summary_message": f"최대 잠재 손실액은 {total_potential_loss:,.0f}원으로, 현행 시스템으로는 연도별 격차를 메우기 어렵습니다.",
        "comparison_metrics": {
            "aggregate_gap": total_potential_loss,
            "latest_data_marker": latest_value
        }
    }

# ==============================================================================
# 3. End-to-End 통합 테스트 파이프라인 (메인 로직)
# 데이터 유효성 검증 -> 비즈니스 로직 적용 -> 최종 구조화 순서로 실행합니다.
# ==============================================================================

def run_e2e_data_pipeline(raw_input_data: Dict[str, Any]) -> Optional[VisualizationInputSchema]:
    """
    E2E 데이터 처리 파이프라인을 실행하고 유효성 검증 및 구조화까지 완료합니다.
    """
    print("\n========================================================")
    print("🚀 [STAGE 1/3] 원시 데이터 입력 및 유효성 검증 (Validation)")
    try:
        # 단계 1: 개별 데이터 포인트 모델링 및 검증
        data_points = [FinancialDataPoint(**d).model_dump() for d in raw_input_data.get("financial", [])]
        gap_points = [GapDataPoint(**d).model_dump() for d in raw_input_data.get("gap", [])]

    except ValidationError as e:
        print(f"❌ [FAIL] 🔴 데이터 유효성 검증 실패 (ValidationError): {e}")
        return None
    except Exception as e:
        print(f"❌ [FATAL] 🔴 예기치 않은 오류 발생: {e}")
        return None

    # 단계 2: 비즈니스 로직 적용 및 분석 수행
    print("\n🚀 [STAGE 2/3] 핵심 비즈니스 로직 실행 (Loss Comparison)")
    comparison_result = calculate_loss_comparison(data_points, gap_points)
    if comparison_result is None:
        return None

    # 단계 3: 최종 시각화 JSON 스키마로 구조화 및 반환
    print("\n🚀 [STAGE 3/3] 최종 Visualization 스키마 확정 (Structuring)")
    try:
        final_schema = VisualizationInputSchema(
            title="노후 자금 재정적 손실 Gap 비교 분석",
            data_points=data_points,
            gap_analysis=gap_points
        )
        print("✅ [SUCCESS] 모든 단계가 성공적으로 완료되었으며, 최종 스키마를 반환합니다.")
        return final_schema

    except ValidationError as e:
        print(f"❌ [FAIL] 🔴 최종 구조화 실패 (스키마 오류): {e}")
        return None


if __name__ == "__main__":
    # --- A. 성공 케이스 테스트 (Happy Path) ---
    print("========================================================")
    print("✨ === 테스트 케이스 A: 정상 데이터 입력 (Happy Path) 실행 시작 ===")
    successful_data = {
        "financial": [
            {"data_id": "국민연금", "year": 2025, "value": 15.5},
            {"data_id": "퇴직연금", "year": 2025, "value": 8.0}
        ],
        "gap": [
            {"gap_id": "비급여 사각지대 A", "reference_value": 100.0, "actual_loss_potential": 30.0},
            {"gap_id": "국민연금 미포함 영역", "reference_value": 50.0, "actual_loss_potential": 25.0}
        ]
    }
    final_output = run_e2e_data_pipeline(successful_data)

    if final_output:
        print("\n================== [최종 JSON 출력 결과 예시] ==================")
        # 실제 시각화 API 호출에 사용될 최종 객체
        print(json.dumps(final_output.model_dump(), indent=2, ensure_ascii=False))

    # --- B. 실패 케이스 테스트 (Negative Path) ---
    print("\n\n========================================================")
    print("💔 === 테스트 케이스 B: 데이터 유효성 검증 실패 (Negative Path) 실행 시작 ===")
    invalid_data = {
        "financial": [
            {"data_id": "국민연금", "year": 1990, "value": -5.0} # year 범위를 벗어남, value가 음수임
        ],
        "gap": []
    }
    run_e2e_data_pipeline(invalid_data)