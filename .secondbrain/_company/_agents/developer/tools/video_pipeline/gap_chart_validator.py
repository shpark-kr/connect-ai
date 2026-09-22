import json
from typing import List, Dict, Any
from pydantic import BaseModel, Field, PositiveFloat

# Gap Area Chart의 데이터 포인트를 정의하는 Pydantic 모델 (강력한 스키마 검증)
class DataPoint(BaseModel):
    """하나의 시간대별 재정적 손실 데이터를 나타냅니다."""
    timestamp_sec: float = Field(..., description="데이터가 시작되는 시간 (초 단위).")
    start_value: float = Field(..., ge=0, description="Gap 구간의 시작 재정 값.")
    end_value: float = Field(..., ge=0, description="Gap 구간의 끝 재정 값.")
    data_type: str = Field(..., pattern="^(NationalPENSION|HealthCare|Retirement|Other)$", description="데이터 출처 유형 (필수 Enum).")

class GapChartData(BaseModel):
    """전체 Gap Chart 데이터 셋을 정의합니다."""
    title: str = Field(..., description="차트의 제목.")
    description: str = Field(None, description="Gap Chart에 대한 추가 설명.")
    data_points: List[DataPoint] = Field(..., min_length=1, description="시간 흐름에 따른 데이터 포인트 리스트.")

def validate_gap_chart_data(json_data: Dict[str, Any]) -> tuple[bool, str | None]:
    """
    JSON 형식의 Gap Chart 데이터를 로드하고, 스키마 검증을 수행합니다.
    
    Args:
        json_data: 외부에서 받은 딕셔너리 형태의 데이터.
    Returns:
        (True/False, 에러 메시지 또는 None)
    """
    try:
        # Pydantic 모델을 사용하여 로드 및 검증 시도
        gap_chart = GapChartData(**json_data)
        print(f"✅ [Validator] 데이터 스키마 유효성 검사 통과: {gap_chart.title}")
        return True, None
    except Exception as e:
        # 어떤 필드가 깨졌는지 구체적으로 에러 메시지를 반환합니다.
        error_details = str(e).split('\n')[-1].strip() if str(e) else "알 수 없는 오류"
        print(f"❌ [Validator] 데이터 스키마 유효성 검사 실패: {error_details}")
        return False, f"스키마 불일치 또는 값 범위 이탈. 상세 에러: {error_details}"

if __name__ == '__main__':
    # 테스트 예시 (실제 사용 시에는 외부 API/파일에서 받아옴)
    valid_data = {
        "title": "국민연금 사각지대 재정적 손실 격차 분석",
        "description": "현재 공공 데이터만으로는 예측하기 어려운 개인의 잠재적 손실 영역을 보여줍니다.",
        "data_points": [
            {"timestamp_sec": 0.0, "start_value": 100, "end_value": 250, "data_type": "NationalPENSION"},
            {"timestamp_sec": 30.0, "start_value": 250, "end_value": 400, "data_type": "HealthCare"}
        ]
    }
    # print(validate_gap_chart_data(valid_data))

    invalid_data = {
        "title": "깨진 테스트 데이터",
        "description": "", # description은 필수가 아님.
        "data_points": [
            {"timestamp_sec": -10.0, "start_value": 100, "end_value": 250, "data_type": "BadType"} # timestamp_sec 음수 및 BadType 위반
        ]
    }
    # print(validate_gap_chart_data(invalid_data))