import unittest
from policy_engine import PolicyEngine

class TestPolicyEngine(unittest.TestCase):
    """
    PolicyEngine의 상태 전이 로직을 테스트합니다.
    복잡한 정책 구조가 단계별로 정상 작동하는지 검증하는 것이 목표입니다.
    """

    def setUp(self):
        """테스트 케이스 실행 전에 초기화합니다."""
        self.initial_data = {}

    def test_01_initial_state_to_income_check(self):
        """초기 상태에서 첫 번째 입력이 들어올 때, 소득 확인 단계로 정확히 전이하는지 테스트합니다."""
        engine = PolicyEngine(self.initial_data)
        # 엉뚱한 키를 먼저 넣어도, 로직은 초기화되어야 함을 가정하고 테스트
        result = engine.update_state("dummy", "test")
        self.assertIn("소득 확인 필요", result['status'])

    def test_02_income_check_to_family_check(self):
        """소득 정보가 정확히 입력되었을 때, 다음 단계인 가족 규모 확인으로 전이하는지 테스트합니다."""
        engine = PolicyEngine({})
        # 1. 소득 입력 (초기화)
        engine.update_state("dummy", "dummy") # 초기 상태를 건너뛰는 임시 처리 가정
        
        # 2. 실제 소득 정보 업데이트
        result = engine.update_state("annual_income", 60000000)
        self.assertIn("가족 구성원 확인 필요", result['status'])

    def test_03_full_flow_completion(self):
        """모든 필수 단계를 거쳐 최종 진단까지 성공적으로 완료하는 전체 흐름을 테스트합니다."""
        engine = PolicyEngine({})
        
        # 1. 소득 입력 (가정)
        state_step1 = engine.update_state("annual_income", 60000000)
        self.assertIn("소득 확인 필요", state_step1['status'])

        # 2. 가족 구성원 입력 (가정)
        state_step2 = engine.update_state("family_members", 4)
        self.assertIn("가족 구성원 확인 필요", state_step2['status'])
        
        # 3. 최종 진단 실행을 유도하는 임의의 데이터 입력 (진짜는 버튼 클릭 트리거)
        final_result = engine.update_state("diagnosis_trigger", True)
        self.assertEqual(final_result['status'], "진단 완료")

    def test_04_invalid_input_handling(self):
        """흐름을 건너뛰는 잘못된 입력이 들어왔을 때, 오류 메시지를 반환하는지 테스트합니다."""
        engine = PolicyEngine({})
        # 소득 정보 없이 갑자기 진단 트리거를 보내는 경우 (비정상적 흐름)
        result = engine.update_state("diagnosis_trigger", True)
        self.assertIn("흐름 오류", result['status'])

if __name__ == '__main__':
    unittest.main()