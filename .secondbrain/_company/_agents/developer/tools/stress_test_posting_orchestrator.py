import time
import random
import logging

# 로깅 설정: 실패와 복구 프로세스 추적에 필수
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

MAX_RETRIES = 5
INITIAL_BACKOFF_DELAY = 1  # 초 단위

def simulate_api_call(attempt: int, max_retries: int) -> bool:
    """
    외부 API 호출을 시뮬레이션합니다. 실패 조건과 재시도 로직을 테스트합니다.
    가장 첫 번째와 세 번째 시도는 의도적으로 실패하게 설정하여 백오프를 유발합니다.
    """
    if attempt < 3 and attempt <= max_retries:
        # 초기 호출 및 몇 번의 재시도는 Rate Limit Fail을 가정
        logging.warning(f"[API Call Failed] Attempt {attempt}/{max_retries}: API Rate Limit Exceeded (HTTP 429).")
        return False
    elif attempt == max_retries + 1:
         # 최종 시도 실패 조건 테스트 (예: 계정 비활성화)
        logging.error(f"[API Call Failed] Final Attempt {attempt}: Critical API Failure (HTTP 500). Max retries reached.")
        return False
    else:
        # 성공 케이스
        logging.info(f"[SUCCESS] Attempt {attempt}/{max_retries + 1}: Content published successfully after recovery.")
        return True

def posting_orchestrator_stress_test(content_id: str):
    """
    PostingOrchestrator의 핵심 로직을 시뮬레이션합니다.
    지수 백오프(Exponential Backoff)와 재시도 제한을 테스트합니다.
    """
    logging.info("===========================================================")
    logging.info(f"🚀 Starting Stress Test for Content ID: {content_id}")
    logging.info("===========================================================")

    attempt = 1
    success = False

    while attempt <= MAX_RETRIES + 1 and not success:
        try:
            # 실제 API 호출 시뮬레이션 (이 함수가 핵심)
            is_successful = simulate_api_call(attempt, MAX_RETRIES)

            if is_successful:
                logging.info("✅ Publishing successful!")
                success = True
            else:
                # 실패 처리 로직: 지수 백오프 계산
                wait_time = INITIAL_BACKOFF_DELAY * (2 ** (attempt - 1))
                
                if attempt <= MAX_RETRIES:
                    logging.warning(f"😴 Backing off for {wait_time:.2f} seconds...")
                    # 실제 테스트에서는 time.sleep()을 사용하지만, 여기서는 시뮬레이션 로그만 남김
                    pass 
                    
                attempt += 1

        except Exception as e:
            logging.critical(f"❌ Unhandled Exception during orchestration: {e}")
            break
    
    if not success:
        logging.error("===========================================================")
        logging.error("🚨 Stress Test FAILED. All retries and recovery attempts exhausted.")
        logging.error("Action required: Check API key credentials or underlying service stability.")

# 메인 실행 블록
if __name__ == "__main__":
    posting_orchestrator_stress_test(content_id="HOMA-IR_StressTest_001")