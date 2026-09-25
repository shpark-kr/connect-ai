# Circuit Breaker Pattern Implementation for API Calls
import time
from enum import Enum

class CircuitState(Enum):
    CLOSED = 1  # 정상 작동 상태 (API 호출 시도)
    OPEN = 2    # 실패가 너무 많아 차단된 상태 (호출 거부)
    HALF_OPEN = 3 # 잠시 후 테스트 가능 상태 (제한적 호출 허용)

class CircuitBreaker:
    def __init__(self, failure_threshold=5, recovery_timeout=60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = None

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.state == CircuitState.OPEN:
                if time.time() > self.last_failure_time + self.recovery_timeout:
                    print("🔌 회로 차단기 (CB) 테스트 모드 진입: HALF-OPEN")
                    self.state = CircuitState.HALF_OPEN
                else:
                    raise ConnectionError(f"❌ API 호출 차단됨 ({self.failure_threshold}회 이상 실패). 재시도 시간까지 대기하세요.")

            try:
                result = func(*args, **kwargs)
                # 성공 시 초기화
                if self.state != CircuitState.CLOSED:
                    print("✅ 회로 복구 성공: CLOSED 상태로 전환합니다.")
                self.failure_count = 0
                self.state = CircuitState.CLOSED
                return result

            except Exception as e:
                self.failure_count += 1
                if self.failure_count >= self.failure_threshold and self.state != CircuitState.OPEN:
                    print(f"🚨 치명적 실패 감지! CB를 OPEN 상태로 전환합니다.")
                    self.state = CircuitState.OPEN
                    self.last_failure_time = time.time()
                raise e
        return wrapper

# 사용 예시: @CircuitBreaker(...)