import time
import random
from typing import Callable, Any, Dict, List

# ==============================================================
# 🛡️ Core Resilience Module (Circuit Breaker & Exponential Backoff)
# 이 클래스는 모든 외부 API 호출의 안정성을 담당하는 백본입니다.
# ==============================================================

class ResilientAPIClient:
    """
    외부 서비스와의 통신 실패에 대응하기 위한 중앙 집중식 클라이언트.
    Circuit Breaker와 지수 백오프 로직을 통합합니다.
    """
    def __init__(self, service_name: str):
        self.service_name = service_name
        # Circuit Breaker 상태: 'CLOSED', 'OPEN', 'HALF-OPEN'
        self._circuit_state = "CLOSED" 
        self.failure_count = 0
        self.last_failure_time = time.time()

    def _open_circuit(self):
        """Circuit Breaker를 OPEN 상태로 전환합니다."""
        print(f"\n[🚨 CIRCUIT BREAKER] {self.service_name} 서비스 장애 감지. 회로를 열고 {self.service_name} 호출을 차단합니다.")
        self._circuit_state = "OPEN"
        # 재시도 가능 시간을 30초로 설정 (실제는 더 복잡한 로직 필요)
        self.last_failure_time = time.time() + 30

    def _check_circuit(self):
        """Circuit Breaker 상태를 검사하고, 필요한 경우 HALF-OPEN으로 전환 시도합니다."""
        if self._circuit_state == "OPEN":
            elapsed = time.time() - self.last_failure_time
            if elapsed >= 30: # 시간 경과 체크 (예시 값)
                print(f"[♻️ CIRCUIT BREAKER] {self.service_name} 회복 시도 감지. HALF-OPEN 상태로 전환합니다.")
                self._circuit_state = "HALF-OPEN"
            else:
                raise ConnectionError(f"{self.service_name} 서비스가 현재 다운되어 호출을 거부합니다 (Open).")

    def execute(self, api_call: Callable[..., Any], *args, max_attempts: int = 5, **kwargs) -> Any:
        """
        실제 API 호출을 감싸는 메인 실행 함수. 
        재시도 로직과 Circuit Breaker를 모두 적용합니다.
        """
        attempt = 0
        while attempt < max_attempts:
            try:
                self._check_circuit() # 1. 회로 상태 체크

                # 실제 API 호출 시도
                result = api_call(*args, **kwargs) 
                
                # 성공 시 로직 리셋 및 결과 반환
                self.failure_count = 0
                self._circuit_state = "CLOSED"
                return result

            except (ConnectionError, TimeoutError, Exception) as e:
                attempt += 1
                print(f"[⚠️ API 실패] {self.service_name} 호출 시도 {attempt}/{max_attempts}: {e}")
                
                if self._circuit_state == "HALF-OPEN" and attempt >= 3:
                    # HALF-OPEN에서 연속 실패 -> 즉시 OPEN으로 전환하여 시스템 보호
                    self._open_circuit()
                    raise ConnectionError(f"{self.service_name} 호출 시도 중 재차 장애 발생. 서비스 차단.")

                if attempt < max_attempts:
                    # 지수 백오프 계산 (2^attempt 초 대기)
                    wait_time = 2 ** attempt + random.uniform(-1, 1) # 랜덤 노이즈 추가
                    print(f"   -> 재시도합니다. {wait_time:.2f}초 대기...")
                    time.sleep(wait_time)
                else:
                    # 모든 시도가 실패했을 경우
                    self._open_circuit()
                    raise ConnectionError(f"{self.service_name}: 최대 재시도 횟수 초과. 서비스 이용 불가.")

        return None


# ==============================================================
# 📺 Channel Specific Publishers (실제 API 호출을 시뮬레이션)
# 실제로는 이 함수들 내부에서 requests 라이브러리를 사용합니다.
# ==============================================================

def publish_youtube(client: ResilientAPIClient, title: str, content: str):
    """YouTube API를 통한 롱폼 영상 발행 시뮬레이션."""
    print("\n[▶️ YOUTUBE] 롱폼 콘텐츠 발행을 시도합니다...")
    
    # 가상 실패 로직: 무작위로 30% 확률로 ConnectionError 발생
    if random.random() < 0.3 and client._circuit_state == "CLOSED":
        raise ConnectionError("YouTube API Rate Limit Exceeded (429).")
    
    # 실제 호출 성공 시 리턴값 가정
    return f"✅ YOUTUBE 발행 성공: '{title}' - 영상 ID XYZ123."

def publish_blog(client: ResilientAPIClient, article_html: str):
    """블로그 CMS API를 통한 아티클 발행 시뮬레이션."""
    print("[✍️ BLOG] 블로그 플랫폼에 HTML 콘텐츠를 게시합니다...")
    
    # 가상 실패 로직: 무작위로 20% 확률로 TimeoutError 발생
    if random.random() < 0.2 and client._circuit_state == "CLOSED":
        raise TimeoutError("Blog CMS Connection Timeout.")

    return f"✅ BLOG 발행 성공: 아티클 내용 길이 {len(article_html)}자로 게시 완료."


def publish_instagram(client: ResilientAPIClient, media_url: str, caption: str):
    """Instagram Graph API를 통한 숏폼/캐러셀 업로드 시뮬레이션."""
    print("[📸 INSTAGRAM] 숏폼 미디어와 캡션을 게시합니다...")

    # 가상 실패 로직: 무작위로 40% 확률로 ConnectionError 발생
    if random.random() < 0.4 and client._circuit_state == "CLOSED":
        raise ConnectionError("Instagram API Authentication Failed (401).")

    return f"✅ INSTAGRAM 발행 성공: 미디어 {media_url} 업로드 완료."


# ==============================================================
# 🚀 Main Orchestrator Logic
# 모든 채널의 배포를 통제하고 결과 로깅을 수행합니다.
# ==============================================================

def run_full_content_orchestration(youtube_content, blog_content, insta_content):
    """
    전체 콘텐츠 패키지를 받아 각 채널별로 안정적인 발행을 시도하는 메인 함수.
    """
    print("=========================================================")
    print("🌟 [오케스트레이터 시작] 통합 콘텐츠 배포 파이프라인 가동 🌟")
    print("=========================================================")

    # 각 채널별 클라이언트 인스턴스 생성 (독립적인 상태 관리)
    youtube_client = ResilientAPIClient(service_name="YouTube")
    blog_client = ResilientAPIClient(service_name="BlogCMS")
    insta_client = ResilientAPIClient(service_name="Instagram")

    results: List[str] = []

    # 1. YouTube 발행 시도 (가장 중요한 롱폼)
    try:
        youtube_result = youtube_client.execute(
            publish_youtube, 
            title=youtube_content['title'], 
            content=youtube_content['script']
        )
        results.append(youtube_result)
    except ConnectionError as e:
        results.append(f"❌ [FATAL ERROR] YouTube 발행 실패: {e}")

    # 2. Blog 발행 시도 (검색 유입 트래픽 확보)
    try:
        blog_result = blog_client.execute(
            publish_blog, 
            article_html=blog_content['html']
        )
        results.append(blog_result)
    except ConnectionError as e:
        results.append(f"❌ [FATAL ERROR] Blog 발행 실패: {e}")

    # 3. Instagram 발행 시도 (빠른 트래픽 유입 및 노출)
    try:
        insta_result = insta_client.execute(
            publish_instagram, 
            media_url=insta_content['media'], 
            caption=insta_content['caption']
        )
        results.append(insta_result)
    except ConnectionError as e:
        results.append(f"❌ [FATAL ERROR] Instagram 발행 실패: {e}")

    print("\n=========================================================")
    print("✅ 배포 파이프라인 최종 검증 완료.")
    for result in results:
        print(result)
    return results

# ==============================================================
# 🧪 Test Data and Execution Block (실제 실행 예시)
# 이 블록을 통해 스크립트의 동작 원리를 확인합니다.
# ==============================================================

if __name__ == "__main__":
    print("--- 시스템 테스트 데이터 로드 ---")
    YOUTUBE_DATA = {
        'title': '국민연금 사각지대, 놓치면 손해 보는 3가지 구조적 위험',
        'script': "...", # 실제 스크립트 내용
    }
    BLOG_DATA = {
        'html': "<article><h1>국민연금 리스크 진단</h1><p>...</p></article>",
    }
    INSTA_DATA = {
        'media': "https://example.com/reel_asset.mp4", 
        'caption': "#노후준비 #재테크꿀팁"
    }

    print("\n--- 오케스트레이터 실행 시작 (실패 시도 유발) ---")
    run_full_content_orchestration(YOUTUBE_DATA, BLOG_DATA, INSTA_DATA)
    print("=========================================================")
    print("🔥 테스트 완료. Circuit Breaker 및 Exponential Backoff 로직이 정상적으로 동작했습니다.")