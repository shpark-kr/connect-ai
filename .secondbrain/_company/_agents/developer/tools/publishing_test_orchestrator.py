import time
import random
from typing import Optional, Dict

# ======================================================
# 🌐 [Mock API Services] - 실제 외부 API 호출을 시뮬레이션하는 클래스들
# 실패 케이스 발생 가능성을 포함하여 설계합니다.
# ======================================================

class MockAPIError(Exception):
    """커스텀 예외: 다양한 종류의 API 실패를 시뮬레이션합니다."""
    def __init__(self, message, code="GENERIC_ERROR"):
        super().__init__(message)
        self.code = code # RateLimitExceeded, AuthTokenExpired, ServerDown

class YouTubePublisherService:
    """YouTube API 호출을 시뮬레이션합니다."""
    RATE_LIMIT_THRESHOLD = 3  # 이 테스트 세션 내에서 3회 실패를 가정
    attempt_count = 0
    
    def publish_video(self, title: str, description: str) -> bool:
        self.attempt_count += 1
        print(f"\n[🎥 YouTube] --- 시도 {self.attempt_count} : '{title}' 업로드 시작...")

        # 1. 실패 케이스 시뮬레이션 (Rate Limit 초과)
        if self.attempt_count % 4 == 0 and self.attempt_count < 6:
            print("❌ [YouTube] API 호출 실패! -> Rate Limit Exceeded가 감지되었습니다.")
            raise MockAPIError("Rate limit exceeded for this user/project.", code="RATE_LIMIT")

        # 2. 실패 케이스 시뮬레이션 (인증 만료)
        if self.attempt_count == 6:
             print("❌ [YouTube] API 호출 실패! -> 인증 토큰이 유효하지 않습니다.")
             raise MockAPIError("Authentication token expired or invalid.", code="AUTH_TOKEN_EXPIRED")

        # 성공 케이스
        time.sleep(0.5) # 네트워크 지연 시뮬레이션
        print(f"✅ [YouTube] '{title}' 업로드 완료. (Success)")
        return True

class BlogPublisherService:
    """블로그 API 호출을 시뮬레이션합니다."""
    MAX_FAILURES = 2
    attempt_count = 0

    def publish_article(self, html_content: str) -> bool:
        self.attempt_count += 1
        print(f"\n[✍️ Blog] --- 시도 {self.attempt_count} : 블로그 포스팅 시작...")
        
        # 1. 실패 케이스 시뮬레이션 (Server Down)
        if self.attempt_count == 3:
            print("❌ [Blog] API 호출 실패! -> 외부 서버 점검 중입니다.")
            raise MockAPIError("The blog publishing endpoint is temporarily down.", code="SERVER_UNAVAILABLE")

        # 성공 케이스
        time.sleep(0.3)
        print(f"✅ [Blog] 블로그 포스팅 완료. (Success)")
        return True

class InstagramPublisherService:
    """인스타그램 API 호출을 시뮬레이션합니다."""
    MAX_FAILURES = 1
    attempt_count = 0

    def post_carousel(self, media_asset_path: str) -> bool:
        self.attempt_count += 1
        print(f"\n[📸 Instagram] --- 시도 {self.attempt_count} : 카루셀 업로드 시작...")

        # 1. 실패 케이스 시뮬레이션 (네트워크 연결 불안정)
        if self.attempt_count == 2:
            print("❌ [Instagram] API 호출 실패! -> 네트워크 연결이 불안정합니다.")
            raise MockAPIError("Network connection timed out.", code="NETWORK_TIMEOUT")

        # 성공 케이스
        time.sleep(0.4)
        print(f"✅ [Instagram] 카루셀 업로드 완료. (Success)")
        return True


# ======================================================
# 🛡️ [Core Logic] - Circuit Breaker 및 Retry/Fallback 로직 구현
# ======================================================

MAX_RETRIES = 3 # 최대 재시도 횟수
BASE_WAIT_TIME = 2 # 기본 대기 시간 (초)

def circuit_breaker(api_call, *args, failure_codes: list, fallback_func):
    """
    Circuit Breaker 패턴을 구현합니다.
    특정 실패 코드가 연속적으로 감지되면 회로가 'Open'되어 즉시 예외를 발생시키고, 
    fallback_func를 호출하여 대체 로직으로 전환합니다.
    """
    failure_count = 0
    print("\n[🛡️ Circuit Breaker 활성화] 시스템 안정성 검증 시작.")
    
    try:
        # 핵심 API 호출 시도 (Retry 로직은 내부에서 처리)
        return api_call(*args)

    except MockAPIError as e:
        if e.code in failure_codes and failure_count < 2: # 연속 실패 감지
            failure_count += 1
            print(f"🚨 [CB] {e.code} 발생! 회로 차단 임계치({failure_count}/3) 도달!")
            
            # Circuit Open -> Fallback 로직 실행
            print("➡️ [CB] 시스템 안정성 저하 감지. 대체 플랜 (Fallback)을 실행합니다.")
            return fallback_func()
        else:
            print(f"⚠️ [CB] 처리 가능한 예외입니다. ({e.code}) - 일반적인 오류로 간주하고 다음으로 넘어갑니다.")
            # 회로가 Open 상태가 아니므로, 단순히 실패만 보고 넘깁니다.
            return None

def retry_with_backoff(api_func, *args):
    """
    지수 백오프(Exponential Backoff)를 적용한 재시도 로직입니다.
    Rate Limit이나 일시적 서버 오류에 대비합니다.
    """
    for attempt in range(MAX_RETRIES):
        try:
            # 1차 시도
            return api_func(*args)

        except MockAPIError as e:
            print(f"   -> [RETRY] 실패 유형 감지 ({e.code}). 재시도 {attempt + 1}/{MAX_RETRIES} 진행...")
            if attempt < MAX_RETRIES - 1:
                # 지수 백오프: 대기 시간 = BASE * (2^attempt)
                wait_time = BASE_WAIT_TIME * (2 ** attempt)
                print(f"   -> [RETRY] {wait_time}초 대기 후 재시도합니다.")
                time.sleep(wait_time)
            else:
                print("❌ [RETRY] 최대 재시도 횟수 초과. 해당 작업은 실패로 간주하고 스킵합니다.")
                return None # 모든 시도가 실패했으므로 None 반환

def fallback_plan(platform: str, content: str):
    """
    최종 안전장치 (Fallback Plan)입니다. API가 아예 먹통일 때 대체할 수 있는 계획을 제시합니다.
    -> 즉시 이메일 발송 또는 백업 채널에 경고 로그를 남깁니다.
    """
    print(f"\n🚨 [FALLBACK TRIGGERED] {platform} 플랫폼의 모든 발행 시도가 실패했습니다.")
    if "YouTube" in platform:
        # 핵심 내용만 가지고 내부 QA팀에게 이메일 알림을 보냅니다. (가장 중요)
        return f"[EMAIL ALERT]: {content[:50]}... 콘텐츠는 성공적으로 저장되었으나, API 장애로 인해 발행 실패. 수동 검토 필수."
    elif "Blog" in platform:
        # 백업으로 워드프레스 FTP에 HTML 파일을 직접 업로드하는 로직을 실행합니다.
        return f"[FTP UPLOAD]: {content[:50]}... 콘텐츠는 성공적으로 저장되었으나, API 장애로 인해 발행 실패. 수동 파일 전송 필요."
    elif "Instagram" in platform:
        # 인스타그램의 경우, 이미지 파일을 클라우드 스토리지를 통해 공유합니다.
        return f"[CLOUD SHARE]: {content[:50]}... 콘텐츠는 성공적으로 저장되었으나, API 장애로 인해 발행 실패. 이미지 에셋을 공유했습니다."
    return "Fallback Plan 실행 완료: 대체 로그 생성 및 알림 로직 수행됨."

# ======================================================
# 🚀 [Main Orchestrator] - 통합 테스트 시나리오 실행
# ======================================================

def run_publishing_stress_test():
    """
    전체 파이프라인에 대한 무인 발행 스트레스 통합 테스트를 실행합니다.
    """
    print("="*80)
    print("✨ [START] 온현 미디어 스튜디오: Multi-Platform 자동 발행 파이프라인 스트레스 테스트")
    print("================================================================================")

    # 1. 핵심 콘텐츠 정의 (가정된 성공 결과물)
    video_title = "퇴직 후 재정 Gap! 놓치기 쉬운 국민연금 사각지대 총정리"
    video_desc = "공적 데이터를 기반으로 본, 여러분이 모르는 은퇴 자금의 위험 신호와 해결책을 제시합니다."
    blog_content = "<article><h1>국민연금 Gap 리스크 분석</h1><p>...</p></article>"
    insta_asset = "c:\\Data\\Project\\connect-ai\\결과물\\03_기획_디자인\\senior_care_carousel.jpg"

    # -------------------------
    # A. 유튜브 테스트 시나리오 (Circuit Breaker + Retry)
    # -------------------------
    print("\n\n==========================================")
    print("▶️ [TEST PHASE A] YouTube API 안정성 검증")
    print("==========================================")

    def youtube_fallback():
        return fallback_plan("YouTube", video_title)

    # 유튜브 호출에 Rate Limit 및 Auth Token 만료가 발생하도록 설계된 테스트
    youtube_api = lambda: YouTubePublisherService().publish_video(video_title, video_desc)
    
    # Circuit Breaker를 적용하여 핵심 API 호출
    youtube_result = circuit_breaker(
        api_call=youtube_api, 
        failure_codes=["RATE_LIMIT", "AUTH_TOKEN_EXPIRED"],
        fallback_func=youtube_fallback
    )
    print(f"\n[FINAL YOUTUBE RESULT] : {youtube_result}")


    # -------------------------
    # B. 블로그 테스트 시나리오 (Retry + Fallback)
    # -------------------------
    print("\n\n==========================================")
    print("▶️ [TEST PHASE B] Blog API 안정성 검증")
    print("==========================================")

    def blog_fallback():
        return fallback_plan("Blog", blog_content)

    # 블로그 호출에 Server Unavailable이 발생하도록 설계된 테스트
    blog_api = lambda: BlogPublisherService().publish_article(blog_content)
    
    # Retry 로직을 적용하여 핵심 API 호출 (3회 재시도 가능)
    blog_result = retry_with_backoff(blog_api)

    # 만약 Retry 후에도 실패했다면, Circuit Breaker의 fallback 논리를 따름
    if blog_result is None:
        print("\n[⚠️ Blog] 모든 재시도가 실패했습니다. Fallback Plan을 수동으로 실행합니다.")
        blog_fallback_result = fallback_plan("Blog", blog_content)
        print(f"[FINAL BLOG RESULT]: {blog_fallback_result}")


    # -------------------------
    # C. 인스타그램 테스트 시나리오 (Retry Only - Network Timeout)
    # -------------------------
    print("\n\n==========================================")
    print("▶️ [TEST PHASE C] Instagram API 안정성 검증")
    print("==========================================")

    def insta_fallback():
        return fallback_plan("Instagram", "")

    # 인스타그램 호출에 Network Timeout이 발생하도록 설계된 테스트
    insta_api = lambda: InstagramPublisherService().post_carousel(insta_asset)

    # Retry 로직을 적용하여 핵심 API 호출
    insta_result = retry_with_backoff(insta_api)


if __name__ == "__main__":
    run_publishing_stress_test()
#