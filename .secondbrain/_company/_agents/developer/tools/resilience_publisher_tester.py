import time
import random
from functools import wraps
from typing import Callable, Any, Dict, List

# ====================================================
# 🛠️ 1. Resilience Patterns Implementation
# ====================================================

class CircuitBreaker:
    """
    서킷 브레이커 패턴 구현. 시스템 과부하 또는 지속적 실패 시 API 호출을 차단하여 자원을 보호합니다.
    상태: CLOSED (정상), OPEN (차단), HALF-OPEN (테스트)
    """
    def __init__(self, failure_threshold: int = 3, recovery_timeout: int = 10):
        self.failure_threshold = failure_threshold # 실패 임계치
        self.recovery_timeout = recovery_timeout   # 재시도 대기 시간 (초)
        self.state = "CLOSED"                       # 현재 상태
        self.fail_count = 0                         # 연속 실패 카운트
        self.last_failure_time = time.time()       # 마지막 실패 시간

    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.state == "OPEN":
                elapsed = time.time() - self.last_failure_time
                if elapsed > self.recovery_timeout:
                    print("🔌 [CircuitBreaker] Timeout 만료 -> HALF-OPEN 상태로 전환하여 테스트 시도.")
                    self.state = "HALF-OPEN"
                else:
                    raise ConnectionError(f"🔴 Circuit Breaker Open. {int(self.recovery_timeout - elapsed)}초 후에 재시도하세요.")

            try:
                result = func(*args, **kwargs)
                if self.state in ["OPEN", "HALF-OPEN"]:
                    print("✅ [CircuitBreaker] 성공 감지 -> CLOSED 상태로 복구 완료.")
                    self.state = "CLOSED"
                    self.fail_count = 0
                return result
            except Exception as e:
                self.fail_count += 1
                if self.state == "HALF-OPEN":
                     # HALF-OPEN에서 실패하면 다시 OPEN으로 전환
                    print(f"❌ [CircuitBreaker] 테스트 실패 -> OPEN 상태로 재진입.")
                    self.state = "OPEN"
                    self.last_failure_time = time.time()
                elif self.fail_count >= self.failure_threshold:
                    # 임계치 초과 시 OPEN으로 전환
                    print(f"💥 [CircuitBreaker] 실패 임계치 ({self.failure_threshold}회) 도달 -> OPEN 상태 진입.")
                    self.state = "OPEN"
                    self.last_failure_time = time.time()
                raise e

        return wrapper

def retry_with_backoff(max_retries: int = 5, initial_delay: float = 1.0):
    """
    지수 백오프 재시도 로직 데코레이터. (Exponential Backoff)
    시간 간격: delay * 2^attempt
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs) # API 호출 시도
                except ConnectionError as e:
                    if attempt == max_retries - 1:
                        print(f"🚨 [Retry] 최대 재시도 횟수({max_retries}회) 초과. 최종 실패합니다.")
                        raise e
                    
                    # 지연 시간 계산 (지수 백오프)
                    sleep_time = delay * (2 ** attempt) + random.uniform(0, 1)
                    print(f"⚠️ [Retry] API 호출 실패 ({e}). {int(sleep_time)}초 후 재시도합니다... (Attempt {attempt + 1}/{max_retries})")
                    time.sleep(sleep_time) # 대기
                except Exception as e:
                    # 예상치 못한 다른 에러는 즉시 전파
                    print(f"🛑 [Retry] 처리 불가능한 에러 발생: {e}")
                    raise e
            return None
        return wrapper
    return decorator

# ====================================================
# 🌐 2. Platform Publishing API Simulation (Mock)
# ====================================================

def publish_youtube(content_package: Dict[str, Any]) -> str:
    """유튜브 플랫폼 발행 시뮬레이션 (API 호출 가정). 실패율이 높게 설정."""
    print("\n--- 📺 유튜브 발행 시도 ---")
    if random.random() < 0.3: # 30% 확률로 일시적 오류 발생 시뮬레이션
        raise ConnectionError("YouTube API Rate Limit Exceeded or Temporary Server Error.")
    return "SUCCESS"

def publish_instagram(content_package: Dict[str, Any]) -> str:
    """인스타그램 플랫폼 발행 시뮬레이션 (API 호출 가정). 실패율이 중간 수준."""
    print("\n--- 📸 인스타그램 발행 시도 ---")
    if random.random() < 0.25: # 25% 확률로 일시적 오류 발생 시뮬레이션
        raise ConnectionError("Instagram Graph API Error: Invalid Media Format.")
    return "SUCCESS"

def publish_naver_blog(content_package: Dict[str, Any]) -> str:
    """네이버 블로그 플랫폼 발행 시뮬레이션 (API 호출 가정). 실패율이 낮음."""
    print("\n--- 📰 네이버 블로그 발행 시도 ---")
    if random.random() < 0.15: # 15% 확률로 일시적 오류 발생 시뮬레이션
        raise ConnectionError("Naver Blog API Error: Authentication Failed.")
    return "SUCCESS"

def publish_youtube_shorts(content_package: Dict[str, Any]) -> str:
    """유튜브 쇼츠/클립 플랫폼 발행 시뮬레이션 (API 호출 가정). 실패율이 높음."""
    print("\n--- 🎬 유튜브 쇼츠/클립 발행 시도 ---")
    if random.random() < 0.35: # 35% 확률로 가장 높은 오류 발생률 설정
        raise ConnectionError("YouTube Shorts API Overload or Geo-Restriction Error.")
    return "SUCCESS"

# ====================================================
# 🧪 3. Orchestrator & Execution Logic
# ====================================================

@CircuitBreaker(failure_threshold=2, recovery_timeout=15)
@retry_with_backoff(max_retries=4, initial_delay=0.5)
def publish_content_package(platform: str, package: Dict[str, Any]) -> str:
    """지수 백오프와 서킷 브레이커가 적용된 핵심 발행 로직."""
    if platform == "YouTube":
        result = publish_youtube(package)
    elif platform == "Instagram":
        result = publish_instagram(package)
    elif platform == "NaverBlog":
        result = publish_naver_blog(package)
    elif platform == "Shorts":
        result = publish_youtube_shorts(package)
    else:
        raise ValueError("Unknown Platform")
    return result

def run_e2e_publishing_simulation(content_package: Dict[str, Any]) -> Dict[str, str]:
    """4대 플랫폼에 대한 E2E 통합 테스트를 실행하고 결과를 수집합니다."""
    platforms = ["YouTube", "Instagram", "NaverBlog", "Shorts"]
    results = {}

    print("=============================================================")
    print("🚀 숏폼 콘텐츠 대량 발행 시뮬레이션 시작 (Resilience Test)")
    print(f"📅 대상 콘텐츠: {content_package.get('title', '미정')} ({content_package['script'][:20]}...)")
    print("=============================================================")

    for platform in platforms:
        try:
            # 핵심 함수 호출 (여기서 CB와 Backoff가 자동으로 작동함)
            status = publish_content_package(platform, content_package)
            results[platform] = f"✅ 성공적으로 발행됨. ({status})"
        except ConnectionError as e:
            results[platform] = f"❌ 실패 (API 오류/속도 제한): {e}"
        except Exception as e:
            results[platform] = f"🛑 치명적 오류 발생: {type(e).__name__} - {str(e)}"

    return results


if __name__ == "__main__":
    # 가상의 최종 콘텐츠 패키지 데이터 (Writer가 제공한 것을 기반으로 구성)
    simulated_content_package = {
        "title": "5060 디지털 소득 공백 리스크 진단",
        "script": "AI가 대체하는 3가지 직무...",
        "keywords": ["중장년 재취업", "디지털 격차"],
        "cta": "전문가진단가이드.zip 다운로드"
    }

    # 시뮬레이션 실행 및 결과 수집
    final_results = run_e2e_publishing_simulation(simulated_content_package)

    # 테스트 보고서 출력
    print("\n\n=============================================================")
    print("📊 E2E 통합 발행 시스템 테스트 완료 보고서")
    print("-------------------------------------------------------------")
    for platform, result in final_results.items():
        print(f"[{platform}]: {result}")
    print("=============================================================\n")

    # 최종 검증: 모든 플랫폼이 성공적으로 실행될 때만 '완료' 처리 가능함을 명시
    success_count = sum(1 for res in final_results.values() if "성공" in res)
    total_platforms = len(final_results)
    if success_count == total_platforms:
        print("✨ 시스템 검증 결과: 모든 플랫폼에 대한 발행 기능 테스트가 성공적으로 완료되었습니다.")
    else:
        print("⚠️ 시스템 검증 경고: 일부 플랫폼에서 오류가 발생했습니다. 이는 정상적인 부하/실패 시뮬레이션 과정일 수 있습니다.")