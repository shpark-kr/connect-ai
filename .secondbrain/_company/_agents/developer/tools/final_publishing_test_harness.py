import time
import random
from typing import Dict, Any
# 기존에 정의된 resilience 및 circuit breaker 모듈을 임포트한다고 가정합니다.
# 실제 환경에서는 이들이 같은 경로에 있어야 합니다.
from content_master_tester import ContentMasterTester # 예시 임포트
from circuit_breaker import CircuitBreaker # 기존 도구 활용

# --- 상수 정의 (Constants) ---
MAX_RETRIES = 5
BASE_DELAY = 2  # 초 단위 지연 시간
TARGET_PATH = r"c:\Data\Project\connect-ai\결과물"


class PublishingFailureError(Exception):
    """지정된 횟수만큼 재시도해도 실패하는 경우 발생하는 커스텀 예외."""
    pass

def simulate_platform_api_call(platform: str, metadata: Dict[str, Any]) -> bool:
    """
    플랫폼별 API 호출을 시뮬레이션하고 성공/실패를 반환합니다.
    (이 함수 내에 실제 API 클라이언트 로직이 들어갈 예정입니다.)
    """
    print(f"⚙️ [API Call] Attempting to publish to {platform}...")
    # 10% 확률로 임의 실패 시뮬레이션 (테스트 용도)
    if random.random() < 0.1:
        print(f"❌ API 호출 실패: {platform} 서버 오류 발생.")
        return False
    time.sleep(0.5) # 네트워크 지연 시간 시뮬레이션
    print(f"✅ API 호출 성공: {platform}에 메타데이터 전송 완료.")
    return True

def reliable_publish_to_platform(
    platform: str, 
    metadata: Dict[str, Any], 
    cb_manager: CircuitBreaker
) -> bool:
    """
    특정 플랫폼으로 발행을 시도하며, CB와 지수 백오프를 적용합니다.
    """
    try:
        # Circuit Breaker가 Open 상태면 즉시 실패 처리
        if cb_manager.is_open():
            raise Exception(f"Circuit Breaker is OPEN for {platform}. System failure suspected.")

        for attempt in range(MAX_RETRIES):
            try:
                # 1. API 호출 시도
                success = simulate_platform_api_call(platform, metadata)
                if success:
                    print(f"✨ 최종 성공! {platform} 발행 완료 (시도 횟수: {attempt + 1}).")
                    cb_manager.record_success() # 성공 기록
                    return True

            except Exception as e:
                # API 호출 실패 또는 임의 예외 발생 시 처리 로직
                print(f"⚠️ [Attempt {attempt + 1}] API 호출 중 에러 발생: {e}")
                cb_manager.record_failure() # 실패 기록 및 CB 카운트 증가

                if attempt < MAX_RETRIES - 1:
                    # 지수 백오프 계산 (2^attempt * BASE_DELAY)
                    delay = min(BASE_DELAY * (2 ** attempt), 30)
                    print(f"⏳ 재시도 대기 ({platform}): {delay:.2f}초 후 재시도합니다...")
                    time.sleep(delay)
                else:
                    # 최대 재시도 횟수 초과 시 실패 처리 및 CB에 신호 전달
                    raise PublishingFailureError(f"{platform}에 대한 발행이 최종적으로 실패했습니다.")

        return False # 루프가 끝났지만 성공하지 못한 경우 (안전장치)


    except PublishingFailureError as e:
        print(f"\n🛑 [CRITICAL FAILURE] {e}")
        # CB 상태 확인 및 로깅
        if cb_manager.is_open():
             print("🚨 시스템 경고: Circuit Breaker가 열렸습니다. API 종속성을 점검해야 합니다.")
        return False

def run_end_to_end_publishing_test(content_data: Dict[str, Any]):
    """
    전체 콘텐츠 패키지(메타데이터)를 받아 E2E 발행 테스트를 실행합니다.
    """
    print("==========================================================")
    print("🚀 [START] End-to-End 최종 발행 통합 테스트를 시작합니다.")
    print("==========================================================")

    # 1. 콘텐츠 마스터 데이터 검증 (기존 로직 사용 가정)
    try:
        tester = ContentMasterTester()
        if not tester.validate_metadata(content_data):
            raise ValueError("메타데이터 유효성 검사 실패. 필수 필드 누락 확인.")
        print("✅ 1단계 완료: 콘텐츠 메타데이터 구조 및 무결성 검증 통과.")
    except Exception as e:
        print(f"🛑 [FATAL ERROR] 메타데이터 검증 단계에서 치명적인 오류 발생: {e}")
        return False

    # 2. 플랫폼별 발행 테스트 실행
    platforms = ["YouTube", "Instagram_Reels", "Blog_CMS"]
    all_successful = True

    for platform in platforms:
        print(f"\n\n--- [TESTING PLATFORM: {platform}] ---")
        cb_manager = CircuitBreaker(name=platform) # 플랫폼별 CB 관리자 생성
        success = reliable_publish_to_platform(platform, content_data['metadata'], cb_manager)
        if not success:
            all_successful = False

    # 3. 최종 보고 및 검증
    print("\n==========================================================")
    if all_successful:
        print("🎉 E2E 통합 테스트 성공! 모든 플랫폼 발행 로직이 안정적으로 작동했습니다.")
        return True
    else:
        print("🛑 E2E 통합 테스트 실패. 일부 플랫폼에서 복구 불가 에러가 발생했습니다. 원인 분석 필요.")
        return False

# --- 실행 예시 (테스트용 더미 데이터) ---
if __name__ == "__main__":
    dummy_content = {
        "title": "국민연금 사각지대 점검",
        "metadata": {
            "video_script": "...", # 롱폼 스크립트 내용
            "short_hook": "...",  # 숏폼 후킹 문구
            "funnel_cta_link": "http://example.com/diagnosis-guide", # Funnel CTA 링크
            "keywords": ["국민연금", "지원금", "50대 은퇴"],
        }
    }
    run_end_to_end_publishing_test(dummy_content)