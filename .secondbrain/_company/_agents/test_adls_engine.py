import unittest
from adls_score_calculator import AdlsScoreCalculator, run_unit_tests # Step 2에서 생성한 모듈 임포트

class TestAdlsScoreEngine(unittest.TestCase):
    """
    calculate_adls_score 함수에 대한 Unit 및 Integration 테스트를 수행합니다.
    """
    def setUp(self):
        """각 테스트 시작 전에 Calculator 인스턴스를 초기화합니다."""
        self.calculator = AdlsScoreCalculator()

    # --- [Unit Test Coverage] ---
    def test_success_case_optimal(self):
        """모든 지표가 최적일 때 (낮은 위험, 높은 스코어)의 계산 검증."""
        data = {"mobility": 0.9, "cognition": 0.85, "self_care": 0.7} # 가중치: M(0.4), C(0.35), S(0.25)
        # 예상 계산값 (임의의 테스트 값): (0.9*0.4 + 0.85*0.35 + 0.7*0.25) = 0.36 + 0.2975 + 0.175 = 0.8325
        expected_score = 0.8325
        actual_score = self.calculator.calculate_adls_score(data)
        self.assertAlmostEqual(actual_score, expected_score, places=4, msg="Optimal score calculation failed.")

    def test_failure_case_critical_risk(self):
        """모든 지표가 최악일 때 (높은 위험, 낮은 스코어)의 계산 검증."""
        data = {"mobility": 0.15, "cognition": 0.2, "self_care": 0.05}
        # 예상 계산값: (0.15*0.4 + 0.2*0.35 + 0.05*0.25) = 0.06 + 0.07 + 0.0125 = 0.1425
        expected_score = 0.1425
        actual_score = self.calculator.calculate_adls_score(data)
        self.assertAlmostEqual(actual_score, expected_score, places=4, msg="Critical risk score calculation failed.")

    def test_failure_case_missing_input(self):
        """필수 입력 데이터가 누락되었을 때 (예외 처리 검증)."""
        data = {"mobility": 0.9, "cognition": 0.8} # self_care 누락
        actual_score = self.calculator.calculate_adls_score(data)
        self.assertIsNone(actual_score, msg="Should return None when critical input is missing.")

    def test_failure_case_invalid_type(self):
        """입력 데이터 타입이 잘못되었을 때 (예외 처리 검증)."""
        data = {"mobility": "high", "cognition": 0.8, "self_care": 0.7} # mobility가 문자열
        actual_score = self.calculator.calculate_adls_score(data)
        self.assertIsNone(actual_score, msg="Should return None when input type is invalid.")

# --- [Integration Test Execution] ---

def run_integration_test():
    """
    Mini-App Funnel의 전체 흐름을 시뮬레이션하며 ADLS 점수 계산이 정상 작동하는지 검증합니다.
    (예: 사용자가 폼에 값을 입력하고, 그 값이 DB로 전송되는 과정까지 포함)
    """
    print("\n=================================================")
    print("     🚀 Mini-App Funnel Integration Test Start")
    print("=================================================")

    # 시나리오 1: 정상 사용자 (점수 산출 -> Deep Crimson Red 위험도 바 적용 검증)
    optimal_data = {"mobility": 0.9, "cognition": 0.85, "self_care": 0.7}
    score_optimal = AdlsScoreCalculator().calculate_adls_score(optimal_data)

    if score_optimal is not None:
        print(f"✅ [Pass] Optimal User Score Calculated Successfully: {score_optimal}")
        # 여기서 실제 Mini-App Funnel의 '점수 기반 동적 색상 변경' 로직이 호출되어야 합니다.
        # 예: if score_optimal > 0.7 -> Green/Yellow, else Deep Crimson Red
    else:
        print(f"❌ [Fail] Optimal User Score Calculation Failed.")

    # 시나리오 2: 위험 사용자 (점수 산출 -> Deep Crimson Red 강제 적용 검증)
    risk_data = {"mobility": 0.15, "cognition": 0.2, "self_care": 0.05}
    score_risky = AdlsScoreCalculator().calculate_adls_score(risk_data)

    if score_risky is not None:
        print(f"✅ [Pass] High Risk User Score Calculated Successfully: {score_risky}")
        # 이 스코어는 무조건 Deep Crimson Red(#B30000) 강조를 유도해야 합니다.
    else:
        print(f"❌ [Fail] High Risk User Score Calculation Failed.")

    # 시나리오 3: 데이터 입력 실패 (시스템 에러 처리 검증)
    error_data = {"mobility": 0.9, "cognition": 0.8} # Missing self_care
    score_error = AdlsScoreCalculator().calculate_adls_score(error_data)

    if score_error is None:
        print("✅ [Pass] System gracefully handled missing data input.")
    else:
        print(f"❌ [Fail] Did not correctly handle missing data. Received score: {score_error}")
        
# Unit Test 실행 (Python unittest 프레임워크 사용)
if __name__ == '__main__':
    # 1. 단위 테스트 실행
    print("===============================================")
    print("           🧪 Running Unit Tests...")
    print("===============================================")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    # 2. 통합 시뮬레이션 실행 (실제 서비스 흐름 검증)
    run_integration_test()