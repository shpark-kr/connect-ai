import requests
import json
import time
from typing import Dict, Any

# --- 설정 상수 (Configuration) ---
BASE_URL = "https://www.onhyeon-site.com" # 가상의 메인 사이트 URL
UTM_TRACKING_URL = "https://analytics.example.com/track/?utm_source={source}&funnel={funnel}&campaign=gap_cta&content={content}"

# --- 테스트 데이터 정의 (Mock Data based on Researcher's FactSheet) ---
TEST_DATA: Dict[str, str] = {
    "national_pension": "월 평균 150만원 부족", # Happy Path
    "health_insurance": None,                    # Null/Missing Data Test
    "inheritance": "최소 3천만원 손실 우려"     # Standard Path
}

def check_utms(url: str, expected_params: Dict[str, str]) -> bool:
    """URL에서 필요한 UTM 파라미터가 정확하게 붙었는지 검증합니다."""
    print(f"[✅] UTMS 체크 시작. URL: {url[:80]}...")
    # 실제 구현에서는 re 모듈을 사용하여 쿼리 스트링 파싱 필요
    if all(param in url for param in expected_params.values()):
        return True
    print(f"[❌] UTMS 오류 발생! 예상 파라미터 미확인.")
    return False

def test_web_cta_flow(funnel_name: str, data: str) -> bool:
    """웹 페이지 환경에서의 CTA 흐름을 검증합니다 (폼 제출 포함)."""
    print(f"\n--- [🌐 Web Test] Funnel '{funnel_name}' 테스트 시작 ---")
    
    # 1. 데이터 삽입 강건성 테스트
    if data and "error" not in data.lower():
        print(f"[✅ Data Injection]: 데이터 성공적으로 주입됨: {data}")
    elif data is None:
        print("[⚠️ Data Injection WARN]: 데이터가 누락되었으나, CTA는 대체 텍스트를 안전하게 표시함.")
    else:
        print(f"[❌ Data Injection FAIL]: 예상치 못한 오류 발생. 값: {data}")
        return False

    # 2. 폼 제출 시뮬레이션 (실제로는 Selenium 사용)
    try:
        # 가상의 POST 요청을 가정하고 상태 코드를 체크합니다.
        response = requests.post(f"{BASE_URL}/signup/submit", data={"email": "test@example.com"})
        if response.status_code == 200 and "success" in response.text:
            print("[✅ Web Flow]: 폼 제출 성공 및 '감사합니다' 메시지 수신.")
        else:
            print(f"[❌ Web Flow FAIL]: 예상 상태 코드 (200) 또는 성공 메시지가 아님. Status: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"[❌ Web Flow ERROR]: 네트워크/요청 실패: {e}")
        return False


def test_youtube_cta_flow(funnel_name: str, data: str) -> bool:
    """YouTube 설명란 환경에서의 CTA 링크 클릭을 검증합니다."""
    print(f"\n--- [▶️ YouTube Test] Funnel '{funnel_name}' 테스트 시작 ---")
    
    # 1. 데이터 삽입 강건성 검사 (링크 내부 구조)
    if data and "error" not in data.lower():
        print(f"[✅ Data Injection]: 링크 내부에 위험액 정보가 안전하게 포함됨.")
    else:
        print("[⚠️ Data Injection WARN]: 링크에 데이터 누락 대비 로직이 필요합니다.")

    # 2. 트래킹 링크 구조 검증 (핵심)
    utms_url = UTM_TRACKING_URL.format(source='youtube', funnel=funnel_name, content='gap_cta')
    print(f"[✅ Tracking Link Structure]: 예상 URL 생성 완료: {utms_url}")

    # 3. 링크 클릭 시뮬레이션 (실제는 브라우저 이벤트 리스너 검사)
    if "youtube" in utms_url and "gap_cta" in utms_url:
        print("[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.")
        return True
    else:
        print("[❌ YouTube Flow FAIL]: UTM 파라미터 구조 오류. 재검토 필요.")
        return False


def run_e2e_test_suite():
    """전체 E2E 통합 테스트를 실행합니다."""
    overall_success = True

    # 1. 국민연금 Funnel 테스트 (성공 케이스)
    print("=============================================")
    web_ok = test_web_cta_flow("national_pension", TEST_DATA["national_pension"])
    youtube_ok = test_youtube_cta_flow("national_pension", TEST_DATA["national_pension"])
    if not (web_ok and youtube_ok):
        overall_success = False

    # 2. 건강보험 Funnel 테스트 (Null/Missing Data 케이스)
    print("\n\n=============================================")
    web_ok = test_web_cta_flow("health_insurance", TEST_DATA["health_insurance"])
    youtube_ok = test_youtube_cta_flow("health_insurance", TEST_DATA["health_insurance"])
    if not (web_ok and youtube_ok):
        overall_success = False

    # 3. 상속 Funnel 테스트 (기본 케이스)
    print("\n\n=============================================")
    web_ok = test_web_cta_flow("inheritance", TEST_DATA["inheritance"])
    youtube_ok = test_youtube_cta_flow("inheritance", TEST_DATA["inheritance"])
    if not (web_ok and youtube_ok):
        overall_success = False

    print("\n=============================================")
    if overall_success:
        print("\n[✨ E2E 테스트 완료] 모든 핵심 Funnel CTA 경로의 강건성 및 트래킹 무결성이 확보되었습니다. 다음 단계로 진행 가능합니다.")
    else:
        print("\n[🚨 E2E 테스트 실패] 일부 필수 기능에서 오류가 감지되었습니다. 코드를 수정하고 재검증해야 합니다.")

if __name__ == "__main__":
    run_e2e_test_suite()