# tests/test_gap_api.py
"""
Gap 계산 모듈에 대한 통합 테스트(SIT) 스크립트입니다.
Mock 데이터셋을 사용하여 로직의 안정성과 정확성을 검증합니다.

테스트 목표: 
1. 정상적인 Gap 금액 계산 확인 (Happy Path).
2. 입력값 누락 또는 잘못된 타입 시 오류 발생 여부 확인 (Error Handling).
3. 모든 Gap이 0인 경우(이미 완벽한 케이스)의 처리 로직 확인.
"""

import unittest
from src.gap_calculator import calculate_gap, WEIGHTS # 경로 수정 필요할 수 있음

class TestGapCalculatorAPI(unittest.TestCase):
    
    def setUp(self):
        # 테스트를 위한 공통 더미 데이터 설정 (가정된 단위: 원)
        pass

    # --- 1. Happy Path 테스트: 모든 Gap이 정상적으로 계산되는 경우 ---
    def test_successful_gap_calculation(self):
        """모든 영역에서 명확한 Gap이 발생하여 총합을 구하는 시나리오."""
        mock_inputs = {
            "nursing_care": {"ideal_cost": 5000, "available_resource": 1000}, # (4000 * 0.4) = 1600.0
            "pension": {"ideal_cost": 3000, "available_resource": 2500},       # (500 * 0.3) = 150.0
            "housing": {"ideal_cost": 2000, "available_resource": 1800}        # (200 * 0.3) = 60.0
        }
        
        expected_total_gap = 1600.0 + 150.0 + 60.0 # 1810.0
        
        try:
            result = calculate_gap(mock_inputs)
            self.assertEqual(result["status"], "success")
            # Gap 계산 결과의 정밀도와 총합을 검증합니다.
            self.assertAlmostEqual(result["total_gap_amount"], expected_total_gap, places=2)
        except Exception as e:
            self.fail(f"Gap 계산 중 예상치 못한 오류 발생: {e}")

    # --- 2. Edge Case 테스트: Gap이 전혀 없는 경우 (Ideal = Reality) ---
    def test_zero_gap_calculation(self):
        """모든 자원이 이상 비용을 충족하여 Gap 금액이 0인 시나리오."""
        mock_inputs = {
            "nursing_care": {"ideal_cost": 1000, "available_resource": 1000}, # Gap: 0
            "pension": {"ideal_cost": 5000, "available_resource": 5000},       # Gap: 0
            "housing": {"ideal_cost": 3000, "available_resource": 3000}        # Gap: 0
        }
        
        result = calculate_gap(mock_inputs)
        self.assertAlmostEqual(result["total_gap_amount"], 0.0, places=2)

    # --- 3. Error Handling 테스트: 필수 입력값이 누락된 경우 ---
    def test_missing_input_error(self):
        """요양 서비스 데이터가 누락되었을 때 ValueError를 발생시키는지 확인."""
        incomplete_inputs = {
            "nursing_care": None, # 의도적으로 잘못된 타입이나 키를 넣음
            "pension": {"ideal_cost": 3000, "available_resource": 2500},
            "housing": {"ideal_cost": 2000, "available_resource": 1800}
        }
        
        # ValueError가 발생하는지 테스트합니다.
        with self.assertRaises(ValueError):
            calculate_gap(incomplete_inputs)

    # --- 4. Error Handling 테스트: 구조적 데이터 오류 발생 시 ---
    def test_incorrect_structure_error(self):
        """'available_resource' 필드가 없는 등, 내부 구조가 깨졌을 때 발생하는 예외를 테스트."""
        badly_structured_inputs = {
            "nursing_care": {"ideal_cost": 5000}, # available_resource 누락
            "pension": {"ideal_cost": 3000, "available_resource": 2500},
            "housing": {"ideal_cost": 2000, "available_resource": 1800}
        }

        # KeyError가 발생하는지 테스트합니다.
        with self.assertRaises(ValueError):
            calculate_gap(badly_structured_inputs)


if __name__ == '__main__':
    # 이 스크립트는 독립적으로 실행되어야 합니다.
    unittest.main()