import logging
from typing import Dict, Any, List, Optional

# 로깅 설정 (디버깅 및 에러 추적용)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AdlsScoreCalculator:
    """
    ADLS (Activities of Daily Living Scale) 기반의 점수 계산 로직을 담당하는 클래스.
    입력 데이터 유효성 검사 및 예외 처리를 포함하여 신뢰성을 극대화합니다.
    """

    def __init__(self):
        # 스코어 가중치 또는 상수 정의 (필요시 확장 가능)
        self.SCORE_WEIGHTS = {
            "mobility": 0.4,
            "cognition": 0.35,
            "self_care": 0.25
        }

    def _validate_input(self, data: Dict[str, Any]) -> bool:
        """
        입력 데이터의 필수 필드 및 타입 유효성을 검사합니다.
        실패 시 True를 반환하여 호출자에게 명확히 알립니다.
        """
        required_keys = ["mobility", "cognition", "self_care"]
        for key in required_keys:
            if key not in data or data[key] is None:
                logging.error(f"Validation Failed: Missing or null critical input '{key}'.")
                return False
        
        # 추가적인 범위 검사 (예: 점수는 0점에서 1점 사이여야 함)
        for key, value in data.items():
            if isinstance(value, (int, float)) and not (0 <= value <= 1):
                 logging.warning(f"Validation Warning: '{key}' has out-of-range value {value}.")
                 # Out of range는 에러로 처리하기보다 경고 후 기본값 사용을 고려할 수 있으나, 여기서는 일단 Fail 처리
                 return False

        return True


    def calculate_adls_score(self, data: Dict[str, Any]) -> Optional[float]:
        """
        ADLS 지표 기반으로 종합 위험 점수 (0.0 ~ 1.0)를 계산합니다.

        Args:
            data: 필수 ADLS 데이터를 포함하는 딕셔너리 ({'mobility': float, 'cognition': float, ...})

        Returns:
            계산된 최종 스코어 (float), 유효성 검사 실패 시 None을 반환합니다.
        """
        logging.info("--- Starting ADLS Score Calculation ---")
        
        # 1. 데이터 유효성 검증 (Guard Clause)
        if not self._validate_input(data):
            logging.error("Cannot calculate score: Input data failed validation checks.")
            return None

        try:
            # 2. 핵심 로직 계산 (가중 평균 방식 예시)
            mobility_score = float(data["mobility"])
            cognition_score = float(data["cognition"])
            self_care_score = float(data["self_care"])

            total_weighted_score = (
                mobility_score * self.SCORE_WEIGHTS["mobility"] +
                cognition_score * self.SCORE_WEIGHTS["cognition"] +
                self_care_score * self.SCORE_WEIGHTS["self_care"]
            )

            # 3. 결과 정규화 및 반환 (Deep Crimson Red의 기준이 되는 스코어)
            final_adls_score = round(max(0.0, min(1.0, total_weighted_score)), 4)
            logging.info(f"Calculation successful. Final ADLS Score: {final_adls_score}")
            return final_adls_score

        except (ValueError, TypeError) as e:
            # 4. 예외 처리 (Critical Failure Handling)
            logging.critical(f"An unexpected type or value error occurred during score calculation: {e}")
            return None


# --- Unit Test Example Function (실제 테스트 스크립트에서 활용될 구조) ---

def run_unit_tests():
    """단위 레벨의 기능 검증을 수행하는 함수."""
    calculator = AdlsScoreCalculator()
    print("\n--- [Unit Test: Success Case] ---")
    # 1. 정상 케이스 테스트 (모든 점수가 높음 -> 낮은 위험)
    success_data = {"mobility": 0.9, "cognition": 0.8, "self_care": 0.7}
    score_good = calculator.calculate_adls_score(success_data)
    print(f"Test Case (Good): Score={score_good}")

    print("\n--- [Unit Test: Edge Case - Low Score] ---")
    # 2. 최저 점수 케이스 테스트 (모든 점수가 낮음 -> 높은 위험)
    fail_data = {"mobility": 0.1, "cognition": 0.15, "self_care": 0.05}
    score_bad = calculator.calculate_adls_score(fail_data)
    print(f"Test Case (Bad): Score={score_bad}")

    print("\n--- [Unit Test: Failure - Missing Key] ---")
    # 3. 필수 키 누락 케이스 테스트
    missing_key_data = {"mobility": 0.5, "cognition": 0.5} # self_care 누락
    score_miss = calculator.calculate_adls_score(missing_key_data)
    print(f"Test Case (Missing Key): Score={score_miss}")

    print("\n--- [Unit Test: Failure - Invalid Type] ---")
    # 4. 잘못된 타입 케이스 테스트 (문자열 입력 시도)
    invalid_type_data = {"mobility": "high", "cognition": 0.5, "self_care": 0.5}
    score_type = calculator.calculate_adls_score(invalid_type_data)
    print(f"Test Case (Invalid Type): Score={score_type}")

# 이 함수는 테스트 실행을 위해 별도로 분리하여 사용합니다.
if __name__ == '__main__':
    run_unit_tests()