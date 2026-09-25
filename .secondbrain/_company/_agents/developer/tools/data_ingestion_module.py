import os
import json
import time
from requests import RequestException, Timeout

# --- Configuration & Constants ---
# 환경 변수에서 API 키를 로드하도록 설계 (절대 코드에 하드코딩 금지)
API_BASE_URL = "https://api.governmentdata.gov/v1" # 예시 베이스 URL
MAX_RETRIES = 3  # 최대 재시도 횟수
INITIAL_BACKOFF_DELAY = 2 # 초기 대기 시간 (초)

class ApiClient:
    """
    외부 API 호출을 담당하는 클라이언트. 실패 시 자동 복구(Retry/Backoff) 로직을 구현합니다.
    """
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API Key가 설정되지 않았습니다.")
        self.api_key = api_key

    def fetch_data(self, endpoint: str, params: dict, method: str = 'GET', timeout: int = 10) -> dict or None:
        """
        주어진 엔드포인트로 데이터를 요청하고, 실패 시 재시도 로직을 수행합니다.
        """
        full_url = f"{API_BASE_URL}{endpoint}"
        attempt = 0
        delay = INITIAL_BACKOFF_DELAY

        while attempt < MAX_RETRIES:
            try:
                print(f"⚙️ API 호출 시도 중... (Attempt {attempt + 1}/{MAX_RETRIES}): {full_url}")
                # 실제 requests 라이브러리 사용을 가정합니다.
                # 여기서는 예시 출력을 위해 임시 로직으로 대체하고, 실제로는 요청 코드를 넣습니다.
                
                if method == 'GET':
                    # response = requests.get(full_url, params=params, timeout=timeout)
                    # response.raise_for_status() # HTTP 에러 발생 시 예외 처리
                    # return response.json()
                    
                    # --- Mock API Response for Demonstration ---
                    time.sleep(0.1) 
                    if attempt == 2 and "pension" in endpoint:
                         print("⚠️ [SIMULATION] Intentional Failure on Attempt 3.")
                         raise Timeout("Connection timed out (Simulated).")

                    return {
                        "status": "success",
                        "data_source": f"{endpoint}_mock",
                        "count": 100 + attempt * 10,
                        "result": [f"Mock data point for {endpoint}."] * 5
                    }

                elif method == 'POST':
                     # response = requests.post(full_url, json=params, timeout=timeout)
                     # return response.json()
                    return {"status": "success", "data_source": f"{endpoint}_mock", "result": ["Mock POST success."]}

            except (RequestException, Timeout, ValueError) as e:
                print(f"❌ API 호출 실패 감지 ({type(e).__name__}): {e}")
                attempt += 1
                if attempt < MAX_RETRIES:
                    print(f"⏳ [Recovery] {delay}초 후 재시도합니다. (Exponential Backoff)")
                    time.sleep(delay)
                    # 대기 시간이 지수적으로 증가하도록 조정
                    delay *= 2
                else:
                    print("🛑 최대 재시도 횟수 초과. 데이터 수집을 포기합니다.")
                    return None
        return None


class DataIngestor:
    """
    통합 데이터 전처리 및 수집 엔진. 여러 도메인의 데이터를 모듈화하여 처리합니다.
    """
    def __init__(self, api_client: ApiClient):
        self.api = api_client

    # --- 1. 장기요양보험 미적용 사각지대 데이터 (LTC Gap) ---
    def ingest_ltc_gap(self, region_code: str = "ALL") -> list or None:
        """
        국가 지원 외의 간병인 비용, 시설 이용료 등 '사각지대' 데이터를 수집합니다.
        """
        print("\n==============================================")
        print("💾 [Step 1/3] 장기요양보험 사각지대 데이터 수집 시작...")
        params = {"region": region_code, "period": "monthly"}
        data = self.api.fetch_data(
            endpoint="/ltc/gap-cost", 
            params=params, 
            method='GET'
        )
        if data and data.get("status") == "success":
            print(f"✅ LTC Gap 데이터 수집 성공. (레코드 수: {data['count']})")
            # 여기서 복잡한 파싱 및 정규화 로직 추가 필요
            return data["result"]
        else:
            print("❌ LTC Gap 데이터 수집 실패. 다음 단계로 진행합니다.")
            return None

    # --- 2. 국민연금/퇴직 후 소득 공백 위험 분석 (Pension Risk) ---
    def ingest_pension_risk(self, user_profile_id: str = "USER001") -> list or None:
        """
        개인화된 은퇴 시뮬레이션 데이터를 수집하여 '재정적 손실액'을 계산합니다.
        API 호출이 까다로우므로 복잡한 재시도 로직 테스트에 적합합니다.
        """
        print("\n==============================================")
        print("💾 [Step 2/3] 국민연금 및 은퇴 소득 공백 위험 분석 시작...")
        params = {"user_id": user_profile_id, "calculation_type": "loss_simulation"}
        data = self.api.fetch_data(
            endpoint="/pension/risk-assessment", 
            params=params, 
            method='GET'
        )
        if data and data.get("status") == "success":
            print(f"✅ Pension Risk 데이터 수집 성공. (레코드 수: {data['count']})")
            return data["result"]
        else:
            print("❌ Pension Risk 데이터 수집 실패. 다음 단계로 진행합니다.")
            return None

    # --- 3. 비급여 의료 리스크 증가율 추이 (Non-covered Med) ---
    def ingest_medical_risk(self, year_range: str = "2019-2024") -> list or None:
        """
        시간 경과에 따른 비급여 항목의 비용 증가 추이를 수집합니다.
        """
        print("\n==============================================")
        print("💾 [Step 3/3] 비급여 의료 리스크 데이터 수집 시작...")
        params = {"scope": "non_covered", "years": year_range}
        data = self.api.fetch_data(
            endpoint="/health/비급여-cost-trend", 
            params=params, 
            method='GET'
        )
        if data and data.get("status") == "success":
            print(f"✅ Medical Risk 데이터 수집 성공. (레코드 수: {data['count']})")
            return data["result"]
        else:
            print("❌ Medical Risk 데이터 수집 실패. 모든 전처리가 완료되었습니다.")
            return None


def run_ingestion_pipeline(api_key: str):
    """
    전체 통합 데이터 수집 파이프라인을 실행하고 최종 결과를 종합합니다.
    """
    try:
        # 1. API 클라이언트 초기화 (보안성 확보)
        api_client = ApiClient(api_key=api_key)
        ingestor = DataIngestor(api_client=api_client)

        print("\n==============================================")
        print("🚀 통합 데이터 수집 파이프라인 시작 (E2E Test)")
        print("==============================================\n")

        # 2. 각 모듈 실행 및 결과 취합
        ltc_data = ingestor.ingest_ltc_gap()
        pension_data = ingestor.ingest_pension_risk() # 이 부분이 재시도 로직을 테스트하도록 의도함
        med_data = ingestor.ingest_medical_risk()

        # 3. 최종 결과 검증 및 저장 (이후 모듈에서 실행)
        if ltc_data or pension_data or med_data:
            print("\n==============================================")
            print("✅ 모든 데이터 수집 시도가 완료되었습니다.")
            print("다음 단계: 취합된 데이터를 기반으로 '재정적 손실' Funnel을 생성합니다.")
        else:
            print("\n⚠️ 경고: 필수 핵심 데이터 중 하나 이상을 확보하지 못했습니다. 근본 원인 분석이 필요합니다.")


    except ValueError as e:
        print(f"\n🚨 치명적인 설정 오류 발생: {e}")
        return None

# --- Script Entry Point ---
if __name__ == "__main__":
    # 실제 환경에서는 os.environ['API_KEY']를 사용해야 합니다.
    # 테스트 목적으로 더미 키 사용
    DUMMY_API_KEY = "YOUR_SECURE_API_KEY" 
    run_ingestion_pipeline(api_key=DUMMY_API_KEY)