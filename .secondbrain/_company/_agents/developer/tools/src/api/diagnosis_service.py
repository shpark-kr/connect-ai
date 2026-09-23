import time
import random
from typing import Dict, Any
# 실제 프로젝트에서는 tenacity 라이브러리 사용 권장
# from tenacity import retry, wait_exponential, stop_after_attempt

# Researcher님이 제공한 Gap 데이터를 모듈 레벨에서 참조합니다.
PENSION_GAP_DATA = {
    "target_need": 21000000,  # 연간 최소 생활비 목표값 (원)
    "current_estimate": 15600000, # 기대 연금 수령액 평균값 (원)
    "risk_factor": 500000, # 공적 제도의 불안정성 반영 추가 위험 비용 (원)
}

def calculate_gap(inputs: Dict[str, float]) -> float:
    """
    사용자 입력값을 받아 재정적 Gap을 계산하는 핵심 로직.
    @param inputs: 사용자의 현재 상황 데이터 {annual_income: 10000000, years_contributed: 20} 등
    @return Gap 금액 (원)
    """
    # 임시 구현: 실제로는 복잡한 시뮬레이션 모델이 들어갑니다.
    gap = PENSION_GAP_DATA["target_need"] - (inputs.get("annual_income", 0) + PENSION_GAP_DATA["current_estimate"])
    return max(0, gap * random.uniform(1.05, 1.2)) # 약간의 변동성 추가

def call_external_api_with_backoff(endpoint: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    외부 데이터 API 호출을 시뮬레이션하며 지수 백오프 로직을 구현합니다.
    실패하는 경우(503 Service Unavailable 등) 재시도하여 안정성을 확보합니다.
    """
    max_retries = 4
    delay = 1 # 초기 대기 시간 (초)

    for attempt in range(max_retries):
        print(f"-> API 호출 시도 중: {endpoint} (Attempt {attempt+1})")
        try:
            # --- START: 외부 시스템 연동 시뮬레이션 ---
            if random.random() < 0.3 and attempt < max_retries - 1: # 30% 확률로 실패 가정
                raise ConnectionError("503 Service Unavailable: External API Rate Limit Exceeded.")

            # 성공 시 정상 데이터 반환
            return {
                "status": "success",
                "data": {"external_score": random.randint(60, 95), "report_date": time.strftime("%Y-%m-%d")}
            }
            # --- END: 외부 시스템 연동 시뮬레이션 ---

        except ConnectionError as e:
            if attempt < max_retries - 1:
                print(f"   [⚠️ 실패] {e}. 재시도까지 대기합니다. ({delay:.2f}초)")
                time.sleep(delay)
                # 지수 백오프 로직 적용: delay = delay * 2 + random_jitter
                delay *= 2
            else:
                print("   [❌ 최종 실패] 최대 재시도 횟수를 초과했습니다.")
                return {"status": "error", "message": f"외부 API 연동에 최종 실패했습니다. {e}"}

    # Fallback 에러 핸들링
    return {"status": "error", "message": "알 수 없는 시스템 오류가 발생했습니다."}


def diagnose_user_pension_risk(inputs: Dict[str, float]) -> Dict[str, Any]:
    """
    메인 진단 함수. Gap 계산 및 외부 데이터 로딩을 통합 관리합니다.
    """
    try:
        # 1. 핵심 Gap 계산 (로컬 프로세스)
        gap_amount = calculate_gap(inputs)

        # 2. 외부 리스크 점수 가져오기 (불안정 API 호출 테스트)
        external_data = call_external_api_with_backoff("PensionScoreAPI", inputs)

        if external_data["status"] == "error":
            # 데이터가 없을 경우의 명확한 에러 처리 로직 실행
            return {
                "success": False, 
                "message": f"진단 정보 수집 실패: {external_data['message']}",
                "details": None
            }

        # 3. 최종 결과 조합 (성공 케이스)
        return {
            "success": True,
            "gap_amount": round(gap_amount),
            "external_score": external_data["data"]["external_score"],
            "report_date": external_data["data"]["report_date"],
            "recommendation": "구체적인 자산 포트폴리오 재편성이 필요합니다."
        }

    except Exception as e:
        # 예측하지 못한 치명적 오류 (Catch-all)
        return {
            "success": False, 
            "message": f"시스템 내부 처리 중 예외 발생: {str(e)}",
            "details": None
        }

if __name__ == '__main__':
    # 테스트 실행 코드
    test_inputs = {"annual_income": 10000000, "years_contributed": 20}
    result = diagnose_user_pension_risk(test_inputs)
    print("\n--- [진단 결과] ---")
    if result['success']:
        print(f"성공적으로 진단을 완료했습니다. Gap: {result['gap_amount']:,}원, Score: {result['external_score']}")
    else:
        print("⚠️ 경고! 위젯 로딩 실패.")

# 💡 참고: 이 파일은 FastAPI 엔드포인트로 배포되어야 합니다.
# @app.get("/api/diagnose")
# def diagnose(inputs: UserInputs): ...
<|"|>