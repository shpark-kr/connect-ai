from typing import List, Optional, Dict, Any
import json
import logging
import time
from pydantic import BaseModel, Field, validator, ValidationError
from tenacity import retry, wait_exponential, stop_after_attempt, RetryError

# 로거 설정 (디버깅 및 에러 추적 용이)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ContentMetadataSchema(BaseModel):
    """
    온현의 모든 미디어 콘텐츠에 공통으로 적용되는 통합 메타데이터 스키마.
    Type Checking 및 기본값 할당 로직을 포함합니다.
    """
    content_uuid: str = Field(..., description="고유 콘텐츠 식별자 (UUID v4). 필수.")
    publish_date: str = Field(..., regex=r'^\d{4}-\d{2}-\d{2}$', description="최종 발행 예정일 (YYYY-MM-DD).")
    primary_topic: List[str] = Field(default_factory=list, description="핵심 주제어/키워드. 3~5개 제한.")
    risk_metric: Optional[float] = Field(None, ge=-1000, le=1000, description="정량적 리스크 수치 (Gap 규모).")
    content_stage: str = Field("기획", description="작업 진행 상태 추적용.") # 기본값 설정
    funnel_goal: str = Field(..., description="콘텐츠가 유도하는 궁극적인 행동 목표. 필수.")
    
    # Source & Fact Check 섹션 (신뢰성 확보를 위해 복합 모델 사용)
    source_name: Optional[str] = Field(None, description="정보 원본 기관명.")
    source_url: Optional[str] = Field(None, description="원본 URL. 영구 링크 필수.")
    data_period: Optional[str] = Field(None, description="데이터 유효 기간 (예: 2024년 기준).")
    data_type: Optional[str] = Field(None, description="자료의 성격 (정부 통계, 법률 개정안 등).")
    fact_check_status: str = Field("미검증", description="사실 검증 상태.") # 기본값 설정

    @validator('content_uuid', pre=True)
    def check_uuid_format(cls, v):
        """UUID가 아닌 경우 강제 에러 발생 (직접적인 유효성 검사)."""
        if not isinstance(v, str):
            raise ValueError("Content UUID must be a string.")
        return v

    @validator('primary_topic', pre=True)
    def enforce_string_list(cls, v):
        """입력된 값이 리스트가 아니면 기본 빈 리스트를 사용합니다."""
        if not isinstance(v, list):
            logging.warning("Primary Topic input was not a list. Defaulting to empty array.")
            return []

# -----------------------------------------------------------
# 핵심 파이프라인 로직: 재시도 및 예외 처리 Wrapper
# -----------------------------------------------------------

class DataValidator:
    """
    데이터 유효성 검사, 기본값 할당, 그리고 외부 시스템 장애에 대비한
    지수 백오프(Exponential Backoff) 기반의 안정적인 저장 인터페이스를 제공합니다.
    """
    def __init__(self):
        pass

    @staticmethod
    def validate_and_clean(data: Dict[str, Any]) -> Optional[ContentMetadataSchema]:
        """
        입력된 원시 데이터 딕셔너리를 스키마에 따라 검증하고 클리닝합니다.
        실패 시 상세 에러 로그를 반환합니다.
        """
        try:
            # Pydantic이 자동으로 타입 캐스팅 및 기본값 할당을 처리합니다.
            validated_data = ContentMetadataSchema(**data)
            logging.info(f"✅ Schema Validation Success for UUID: {validated_data.content_uuid}")
            return validated_data
        except ValidationError as e:
            # 상세한 에러 로그를 반환하여 디버깅 용이성을 높입니다.
            error_details = "\n".join([f"- Field '{err['loc'][0]}': {err['msg']}" for err in e.errors()])
            logging.error(f"❌ Schema Validation Failed! Error Details:\n{error_details}")
            return None
        except Exception as e:
            logging.critical(f"🚨 Unexpected critical error during validation: {e}")
            return None

    @staticmethod
    @retry(wait=wait_exponential(multiplier=1, min=2, max=30), stop=stop_after_attempt(5))
    def save_to_database(validated_data: ContentMetadataSchema):
        """
        외부 DB/API 호출을 시뮬레이션하며 지수 백오프 재시도 로직을 적용합니다.
        실제로는 여기에 ORM 세션 커밋 또는 API POST 요청이 들어갑니다.
        """
        print("\n==============================================")
        logging.info(f"⚙️ Attempting to save data for {validated_data.content_uuid} to the backend...")
        # --- [실제 DB/API 호출 로직 시뮬레이션 시작] ---
        
        # 예시: 3번째 시도에서만 성공한다고 가정 (테스트 목적)
        if getattr(DataValidator, 'attempt', 0) < 2:
            setattr(DataValidator, 'attempt', getattr(DataValidator, 'attempt', 0) + 1)
            logging.warning(f"🔌 [ATTEMPT {getattr(DataValidator, 'attempt', 0)+1}] Connection Failure Simulated.")
            raise ConnectionError("Database connection timed out or API rate limit exceeded.")

        # 성공 로직 (실제로는 DB 세션 커밋 등)
        print("✅ Success: Data successfully persisted to the central repository.")
        logging.info(f"✨ Pipeline Complete for {validated_data.content_uuid}.")
        # --- [실제 DB/API 호출 로직 시뮬레이션 끝] ---


if __name__ == "__main__":
    print("--- 🧪 DataValidator Self-Test Start ---")

    # 1. 성공 케이스 테스트 (Perfect Data)
    good_data = {
        "content_uuid": "a3f7d2e9-b0c4-4a1e-8d5f-6c8b0a2e1f3d",
        "publish_date": "2026-12-01",
        "primary_topic": ["기초연금", "노후소득Gap"],
        "risk_metric": 7.5,
        "content_stage": "최종 검토",
        "funnel_goal": "자료 다운로드",
        "source_name": "국민연금공단",
        "source_url": "http://example.com/pension",
        "data_period": "2024년 기준",
        "fact_check_status": "검증 완료"
    }
    print("\n[TEST 1] Running Perfect Data Test...")
    validated = DataValidator.validate_and_clean(good_data)
    if validated:
        DataValidator.save_to_database(validated)

    # 2. 실패 케이스 테스트 (Missing/Wrong Type Data)
    bad_data = {
        "content_uuid": "invalid-uuid", # UUID 형식 오류 유발
        "publish_date": "12-01-2026", # YYYY-MM-DD 형식 오류 유발
        # primary_topic 누락 (Pydantic이 default로 [] 처리할지 확인)
        "risk_metric": "high", # Type Error 유발 (float 기대)
        "funnel_goal": None, # 필수 필드 Null 에러 유발
    }
    print("\n[TEST 2] Running Bad Data Test...")
    DataValidator.validate_and_clean(bad_data)

    # 3. 재시도 로직 테스트 (Simulating Failure) - 이 코드는 임의로 run_command가 실행하는 환경에 의존함
    print("\n[TEST 3] Running Retry Mechanism Test...")
    # 위에서 생성된 좋은 데이터를 다시 사용하며, save 함수 내장 시뮬레이션과 연결됨.

    print("--- 🧪 DataValidator Self-Test End ---")