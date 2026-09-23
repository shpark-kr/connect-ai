import time
from typing import Dict, Any, List, Optional
import random

# --- 1. Data Models (Schema Definition) ---
# 시니어 엔지니어 관점에서 명시적인 타입 정의는 필수입니다.
class UserProfile:
    """사용자 프로필 정보를 담는 데이터 구조."""
    def __init__(self, age: int, retirement_savings: float, current_pension: float):
        self.age = age
        self.retirement_savings = retirement_savings # 개인 자산 (억 원)
        self.current_pension = current_pension     # 국민연금 예상액 (월 만원 단위)

    def __repr__(self):
        return f"UserProfile(Age={self.age}, Savings={self.retirement_savings:.2f}억, Pension={self.current_pension}만원)"


class PolicyData:
    """공적 정책 및 Gap 항목 데이터를 담는 데이터 구조."""
    def __init__(self, gap_type: str, required_expense: float, public_support_estimate: float):
        self.gap_type = gap_type # 예: '장기 간병/돌봄 서비스'
        self.required_expense = required_expense  # 연간 예상 필요 비용 (원)
        self.public_support_estimate = public_support_estimate # 공적 지원 추정액 (원)


class DiagnosisResult:
    """진단 결과를 담는 구조체."""
    def __init__(self, gap_name: str, calculated_gap: float, message: str):
        self.gap_name = gap_name
        self.calculated_gap = calculated_gap # Gap 금액 (원)
        self.message = message

    def to_dict(self) -> Dict[str, Any]:
        return {
            "Gap 항목": self.gap_name,
            "추정 부족액 (Gap)": f"{int(self.calculated_gap):,} 원",
            "경고 메시지": self.message
        }

# --- 2. External API Mocking & Resilience Logic ---

MAX_RETRIES = 3 # 최대 재시도 횟수
INITIAL_BACKOFF = 1 # 초기 백오프 시간 (초)

def _mock_api_call(attempt: int, endpoint: str) -> bool:
    """
    외부 API 호출을 시뮬레이션하는 모킹 함수.
    첫 N번의 호출은 의도적으로 실패하게 만듭니다.
    """
    global failed_attempts
    print(f"   [API Call] Attempt {attempt} to {endpoint}...")

    if attempt < 2 and endpoint == "gap_service/v1":
        # 첫 두 번은 API가 다운된 것처럼 에러 발생 시뮬레이션
        raise ConnectionError(f"Service Unavailable: {endpoint} is temporarily down.")
    elif random.random() < 0.15 and attempt >= 2:
        # 세 번째부터는 간헐적인 네트워크 오류 가능성 추가 (불안정성 테스트)
         raise TimeoutError("Network timeout encountered.")

    print(f"   [API Call] Success! Data retrieved from {endpoint}.")
    return True


def fetch_policy_data_from_api(gap_type: str, user_id: str) -> PolicyData:
    """
    외부 정책 데이터 API를 호출하고 재시도 로직을 구현합니다.
    지수 백오프(Exponential Backoff) 전략 적용.
    """
    global failed_attempts
    failed_attempts = 0 # 시뮬레이션 초기화

    for attempt in range(MAX_RETRIES):
        try:
            # API 호출 시도 (모킹된 함수 사용)
            _mock_api_call(attempt + 1, "gap_service/v1")
            
            # 성공 시 반환되는 가상의 데이터 로직
            if gap_type == "장기 간병/돌봄 서비스":
                return PolicyData(
                    gap_type=gap_type,
                    required_expense=20_000_000 * (1 + attempt), # 시도 횟수에 따라 요구 비용이 미세하게 변동하는 것처럼 모킹
                    public_support_estimate=6_000_000
                )
            else:
                 raise ValueError("Unsupported Gap Type")

        except (ConnectionError, TimeoutError) as e:
            failed_attempts += 1
            if attempt < MAX_RETRIES - 1:
                # 지수 백오프 계산: sleep(initial_backoff * (2 ** failed_attempts))
                wait_time = INITIAL_BACKOFF * (2 ** failed_attempts)
                print(f"   [Error] {e}. Retrying in {wait_time:.1f} seconds...")
                time.sleep(wait_time) # 실제로는 time.sleep을 사용하지만, 테스트 환경에서는 주석 처리하거나 최소화합니다.
            else:
                # 최대 재시도 횟수 초과 시 실패를 알립니다.
                print("   [Fatal] API Call failed after maximum retries.")
                raise ConnectionError(f"Failed to retrieve policy data for {gap_type} due to persistent service errors.")
        except Exception as e:
            # 예상치 못한 에러는 즉시 전파합니다.
             raise RuntimeError(f"Unexpected error during API call: {e}")

    # 이 라인은 이론적으로 도달하지 않아야 합니다.
    raise ConnectionError("Logic flow error in fetch_policy_data.")


# --- 3. Core Diagnosis Engine Service ---

class DiagnosisEngineService:
    """
    국민연금 외 소득 공백을 진단하는 핵심 서비스 로직입니다.
    API 통신 및 복잡한 계산 과정을 담당합니다.
    """
    def __init__(self):
        print("✅ DiagnosisEngineService 초기화 완료. API 재시도/백오프 메커니즘 준비됨.")

    def calculate_gap(self, policy_data: PolicyData, user_profile: UserProfile) -> Optional[DiagnosisResult]:
        """
        주어진 정책 데이터와 사용자 프로필을 기반으로 소득 Gap을 계산합니다.
        
        Args:
            policy_data: Gap 항목별 공적/사적 필요 비용 구조체.
            user_profile: 사용자 개인 자산 및 연금 정보.

        Returns:
            진단 결과를 담은 DiagnosisResult 객체 또는 None (계산 실패 시).
        """
        print("\n[Service] 핵심 Gap 계산 로직 실행 중...")
        
        # 1. 정책 데이터 기반의 기본 Gap 계산
        # 공식: 필요한 총 비용 - 공적 지원 추정액 = 초기 Gap
        initial_gap = policy_data.required_expense - policy_data.public_support_estimate

        # 2. 사용자 개인 자산/연금 고려 (보수성 추가)
        # 사용자의 남은 여유 자금을 감안하여, 계산된 Gap에서 일정 비율(예: 10%)을 차감합니다.
        # 이는 '개인이 통제할 수 있는 최소한의 안전 마진'을 확보하는 효과를 주어 진단 강도를 높입니다.
        safety_margin = user_profile.retirement_savings * 0.1 + (user_profile.current_pension * 3) # 예시 가중치 적용

        final_gap = max(initial_gap, initial_gap - safety_margin)
        
        # Gap이 안전 마진보다 너무 크지 않으면 경고 수준을 낮춥니다.
        warning_message = (
            f"⚠️ {policy_data.gap_type} 항목에서 예상되는 소득 공백 규모가 심각합니다. "
            f"(계산 근거: 필요한 비용({int(policy_data.required_expense):,}원) 대비, 공적 지원만으로는 부족하여 약 {initial_gap:,}원의 Gap 발생)."
        )

        return DiagnosisResult(
            gap_name=policy_data.gap_type, 
            calculated_gap=final_gap, 
            message=warning_message
        )


# --- [테스트 코드용 전역 변수] ---
failed_attempts = 0 # 테스트를 위해 global 상태 사용
# ------------------------------------

if __name__ == '__main__':
    print("--- Diagnosis Engine Self-Test Start ---")
    
    engine = DiagnosisEngineService()
    
    try:
        user = UserProfile(age=58, retirement_savings=120.0, current_pension=130) # 1.2억, 130만원
        policy_data = fetch_policy_data_from_api("장기 간병/돌봄 서비스", "user1")
        
        result = engine.calculate_gap(policy_data, user)

        print("\n=======================================")
        print("✅ 진단 엔진 테스트 성공!")
        print("---------------------------------------")
        for key, value in result.to_dict().items():
            print(f"  {key}: {value}")
        print("=======================================")
    except (ConnectionError, RuntimeError) as e:
        print(f"\n❌ 진단 엔진 테스트 실패! 시스템 안정성 검토 필요.")
        print(f"   [에러 상세] {e}")

# 💡 주석 처리된 부분은 실제 서비스 배포 시 사용될 로직입니다.
#     - API 호출 전후의 트랜잭션 관리 (DB 커밋/롤백)를 추가해야 합니다.
#     - 입력값 유효성 검사(Input Validation)를 강화하여, 0 또는 음수 값이 들어오는 경우 예외 처리를 해야 합니다.

###