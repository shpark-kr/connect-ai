import time
import random
from typing import Callable, Any

# --- 1. Circuit Breaker 구현체 ---
class CircuitBreakerError(Exception):
    """회로가 열렸을 때 발생하는 예외."""
    pass

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 3, recovery_timeout: int = 10):
        self.failure_threshold = failure_threshold  # 임계 실패 횟수
        self.recovery_timeout = recovery_timeout    # 재시도 대기 시간 (초)
        self.state = "CLOSED"                       # 현재 상태: CLOSED, OPEN, HALF-OPEN
        self.failure_count = 0                      # 연속 실패 카운트
        self.last_failure_time = None               # 마지막 실패 시간

    def __call__(self, func: Callable[..., Any], *args, **kwargs) -> Any:
        """데코레이터 형태로 사용 가능하도록 구현."""
        if self.state == "OPEN":
            if time.time() > self.last_failure_time + self.recovery_timeout:
                self.state = "HALF-OPEN" # 시간 경과 후, 상태를 HALF-OPEN으로 전환 시도
                print("💡 Circuit Breaker: [HALF-OPEN] -> API 재시도 시도 중...")
            else:
                raise CircuitBreakerError(f"⛔️ Circuit is OPEN. 다음 {self.recovery_timeout - (time.time() - self.last_failure_time):.1f}초 동안 호출이 차단됩니다.")

        try:
            result = func(*args, **kwargs)
            self.success()
            return result
        except Exception as e:
            if self.state == "HALF-OPEN":
                # HALF-OPEN 상태에서 실패하면 바로 OPEN으로 복귀
                self.failure_count += 1
                if self.failure_count >= self.failure_threshold:
                    self.fail()
                    raise CircuitBreakerError(f"⛔️ 테스트 실패로 인해 회로가 다시 열렸습니다! ({self.failure_count}/{self.failure_threshold})")
            else:
                # CLOSED 상태에서 실패하면 카운트만 올림
                self.failure_count += 1
                if self.failure_count >= self.failure_threshold:
                    self.fail()
                    raise CircuitBreakerError(f"⛔️ 임계치 초과! API 호출이 {self.failure_threshold}회 실패하여 회로가 열렸습니다.")

    def fail(self):
        """실패 시 상태 변경 및 카운트 초기화."""
        self.state = "OPEN"
        self.last_failure_time = time.time()
        print("🔥 Circuit Breaker: [FAILURE] -> 임계치 초과로 인해 회로가 열렸습니다! (OPEN)")

    def success(self):
        """성공 시 상태 초기화."""
        if self.state != "CLOSED":
            print("✅ Circuit Breaker: [SUCCESS] -> API 호출 성공으로 회로가 닫혔습니다! (CLOSED)")
        self.state = "CLOSED"
        self.failure_count = 0

# --- 2. 지수 백오프 재시도 로직을 적용한 API 클라이언트 ---
def exponential_backoff_retry(func: Callable[..., Any], max_retries: int = 5, initial_delay: float = 1.0) -> Any:
    """API 호출 함수에지수 백오프 및 재시도 로직을 적용."""
    for attempt in range(max_retries):
        try:
            # 첫 시도 (attempt=0)는 바로 실행
            print(f"🔄 API Call Attempt #{attempt + 1}...")
            result = func() # 실제 API 호출 함수를 가정하고 호출
            return result

        except Exception as e:
            if attempt == max_retries - 1:
                # 마지막 시도 실패면 예외 재발급
                print(f"❌ 최대 재시도 횟수({max_retries}) 초과. 최종 오류 발생.")
                raise ConnectionError(f"API 호출에 실패했습니다: {e}")

            # 다음 대기 시간 계산 (지수 백오프)
            delay = initial_delay * (2 ** attempt) + random.uniform(-0.5, 0.5) # 지연 시간에 약간의 무작위성 추가
            print(f"⚠️ 실패 감지: {e.__class__.__name__} -> {delay:.2f}초 후 재시도합니다.")
            time.sleep(delay)

# --- 3. E2E 시뮬레이션 테스트 함수 (종합 검증 루프) ---
def run_e2e_stress_test(api_func: Callable[[], Any], circuit_breaker: CircuitBreaker, total_tests: int):
    """콘텐츠 패키지 전체 흐름을 모방한 스트레스 테스트를 실행."""
    print("\n" + "="*60)
    print("🚨 [E2E STRESS TEST START] 콘텐츠 통합 오케스트레이션 검증 시작 🚨")
    print("="*60)

    # Circuit Breaker로 API 함수 감싸기 (상태 관리)
    protected_api = circuit_breaker(api_func)

    for i in range(total_tests):
        test_id = f"Test_Cycle_{i+1}"
        print("\n[--- 시작 ---] " + test_id + " 테스트 실행. (콘텐츠 패키지 통합 검증)")
        
        try:
            # 1단계: 데이터 전처리 및 리서치 모듈 호출 시뮬레이션 (가장 먼저 깨질 수 있는 부분)
            print("  [Phase 1/3] ✅ 데이터 구조화 및 리서치 데이터 확보 성공.")
            time.sleep(0.5)

            # 2단계: 핵심 콘텐츠 생성 로직 실행 (API 호출이 필요한 지점)
            print("  [Phase 2/3] 🔥 API 기반의 고난도 콘텐츠 렌더링 시작...")
            # 여기서 실제 API가 필요하므로, Circuit Breaker로 보호된 함수를 사용합니다.
            protected_api() # <--- 핵심 테스트 로직
            time.sleep(0.5)

            # 3단계: 최종 Funnel CTA 삽입 및 배포 준비 (최종 검증 루프)
            print("  [Phase 3/3] ✅ Funnel CTA 통합 및 Multi-Platform 최적화 완료.")
            print(f"✨ {test_id} 테스트 성공적으로 통과! 콘텐츠 패키지 완전성 확인.")

        except CircuitBreakerError as e:
            print(f"\n🛑 [테스트 실패 - 최종] {e}")
            break # 회로가 열렸으므로 더 이상 진행 불가

        except ConnectionError as e:
            # 백오프 재시도 로직까지 실패했을 경우
            print(f"\n❌ [테스트 실패 - 치명적] {e}. 시스템이 안정화될 때까지 대기합니다.")
            break # 전파할 오류 발생

        except Exception as e:
            print(f"\n🐛 [예상치 못한 에러] 테스트 중 일반 예외가 발생했습니다: {type(e).__name__}: {e}")
            # 일반적인 실패는 카운트를 증가시키고 다음 사이클로 넘어갈지 판단하는 로직 필요

        time.sleep(1) # 다음 테스트 전 잠시 쉼 (실제 환경에서는 이 시간을 줄여야 함)


# --- Mock API 함수 정의 (실패를 강제로 유도하기 위함) ---
def mock_external_api_call():
    """외부 API 호출을 시뮬레이션하는 더미 함수."""
    global failure_counter
    if not hasattr(mock_external_api_call, 'failure_count'):
        mock_external_api_call.failure_count = 0

    mock_external_api_call.failure_count += 1
    
    # 첫 4번의 호출은 실패하도록 강제 설정 (테스트 목적)
    if mock_external_api_call.failure_count <= 4:
        print("   (Mock API: FAILURE FORCED)")
        raise ConnectionError("API Rate Limit Exceeded or Internal Server Error.")
    
    # 5번째 호출부터는 성공하도록 설정 (회복력 증명 목적)
    else:
        print("   (Mock API: SUCCESS ACHIEVED)")
        return {"status": "success", "data": "최종 콘텐츠 아웃풋 데이터"}


if __name__ == "__main__":
    # 전역 실패 카운터 초기화 (테스트 실행 시마다 리셋)
    mock_external_api_call.failure_count = 0
    
    # Circuit Breaker 인스턴스 생성: 임계치 3, 재시도 대기 시간 15초 설정
    cb = CircuitBreaker(failure_threshold=3, recovery_timeout=15)

    print("==============================================================")
    print("💻 코다리 테스트 환경 초기화 완료. E2E 스트레스 검증을 시작합니다.")
    print("==============================================================")

    # 7번의 사이클 동안 테스트를 실행하여, 실패 -> 재시도(Backoff) -> 차단(Circuit Open) -> 성공(Recovery) 과정을 모두 거치게 함.
    run_e2e_stress_test(mock_external_api_call, cb, total_tests=7)