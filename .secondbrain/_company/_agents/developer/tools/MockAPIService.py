import random
from datetime import datetime
# NameResolutionError는 실제 네트워크 라이브러리에서 발생하지만, 여기서는 시뮬레이션을 위해 임포트합니다.
class NameResolutionError(Exception):
    """DNS Resolution Failure Simulation."""
    pass

def run_scan_diagnosis(user_id: str, metrics: list) -> dict:
    """
    /diagnosis/run_scan 엔드포인트 모킹. 
    핵심 진단 로직의 실패 및 폴백 테스트를 담당합니다.
    """
    print(f"--- [MockAPI] Running diagnosis scan for User ID: {user_id} ---")

    # 1. NameResolutionError 강제 시뮬레이션 (네트워크 인프라 문제)
    if random.random() < 0.2: # 20% 확률로 네트워크 오류 발생 가정
        print("[⚠️ MOCK ERROR] Simulated Name Resolution Failure.")
        raise NameResolutionError("Failed to resolve host name for diagnosis service endpoint.")

    # 2. 데이터 유효성 검사 (400 Bad Request Simulation)
    if not metrics or any(m['metric_name'] == 'HOMA-IR' and m['value'] is None for m in metrics):
        return {
            "status": "ERROR",
            "code": "INVALID_INPUT",
            "message": "진단에 필수적인 생체지표 데이터가 누락되었거나 유효하지 않습니다."
        }

    # 3. 정상 로직 (Soft Gold 해결책 제시)
    total_score = sum(m['value'] for m in metrics if m['metric_name'] == 'HOMA-IR') / len(metrics) * 10
    
    if total_score > 80:
        recommendation = "매우 양호한 상태입니다. 생활 습관을 유지해 주세요."
        status = "SUCCESS"
    elif 60 <= total_score <= 80:
        recommendation = "생활 패턴 점검이 필요합니다. 식이요법 개선에 집중하세요."
        status = "SUCCESS"
    else: # Critical Warning Zone (Deep Crimson Red Trigger)
        recommendation = "🚨 임계점 위험! 전문적인 검진과 생활 변화가 시급합니다. MiniFunnel을 통해 추가 점검이 필요합니다."
        status = "WARNING"

    return {
        "status": status,
        "diagnosis_score": round(total_score, 1),
        "recommendation": recommendation
    }


def get_user_profile_status(user_id: str) -> dict:
    """
    /user/profile/{user_id}/status 엔드포인트 모킹.
    사용자 존재 여부 및 서비스 가용성 폴백 테스트를 담당합니다.
    """
    print(f"--- [MockAPI] Checking user profile status for User ID: {user_id} ---")

    # 1. 사용자 부재 시뮬레이션 (404 Not Found Simulation)
    if user_id == "nonexistent_user":
        return {
            "status": "NOT_FOUND",
            "error_code": "USER_MISSING",
            "message": f"ID '{user_id}'에 해당하는 사용자 데이터를 찾을 수 없습니다. 계정 확인이 필요합니다."
        }

    # 2. 서비스 가용성 저하 시뮬레이션 (503 Service Unavailable)
    if random.random() < 0.1: # 10% 확률로 서버 다운 가정
        return {
            "status": "SERVICE_UNAVAILABLE",
            "error_code": "SERVER_OVERLOAD",
            "fallback_action": "현재 시스템 과부하 상태입니다. 잠시 후 다시 시도해 주십시오. (재시도 로직 필수)"
        }

    # 3. 정상 조회
    return {
        "status": "OK",
        "is_active": True,
        "last_check": datetime.now().isoformat() + 'Z'
    }

if __name__ == '__main__':
    print("============================================")
    print("✅ Mock API Service Initialized: Testing Resilience")
    print("============================================")
    
    # 1. NameResolutionError 테스트 시뮬레이션
    try:
        run_scan_diagnosis("userA", [{"metric_name": "HOMA-IR", "value": 5.0}])
    except NameResolutionError as e:
        print(f"\n[SUCCESS] Handled Expected Error: {e}")
    except Exception as e:
        print(f"[FAILURE] Caught unexpected error type: {type(e)}")

    # 2. Invalid Input 테스트 시뮬레이션
    result_400 = run_scan_diagnosis("userB", [])
    print(f"\n[TEST RESULT 400]: {result_400}")

    # 3. Service Unavailable (Fallback) 테스트 시뮬레이션
    # 이 부분은 랜덤이므로 여러 번 실행해야 합니다.
    get_user_profile_status("test_user")