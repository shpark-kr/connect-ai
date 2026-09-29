import unittest
import os
# 기존의 MockAPIService와 E2E Funnel Test Suite를 임포트하여 사용한다고 가정합니다.
from .MockAPIService import MockAPIService 
from .e2e_funnel_cta_test_suite import test_funnel_flow

class TestFunnelResilience(unittest.TestCase):
    """
    Mini-App Funnel의 E2E 통합 테스트를 수행하는 리질리언스 검증 스크립트.
    네트워크 오류 및 임계치 에러 주입을 핵심 목표로 합니다.
    """

    def setUp(self):
        """각 테스트가 실행되기 전에 초기화합니다."""
        print("\n--- [Test Setup] Mini-App Funnel QA Script 시작 ---")
        # Mock API 서비스 인스턴스를 생성하여 모든 테스트에서 사용 가능하게 만듭니다.
        self.mock_api = MockAPIService()

    def test_001_normal_data_submission(self):
        """SCN-001: 정상 데이터 제출 흐름 검증."""
        print("\n[TEST] SCN-001: 정상 흐름 테스트 (Success Path)")
        # Mock API를 통해 성공 케이스의 가짜 데이터를 주입합니다.
        mock_input = {"HOMA-IR": 5.2, "BMI": 28.1, "식습관 점수": 65}
        try:
            # 실제 Funnel 로직을 테스트하는 함수를 호출 (실제로는 test_funnel_flow 내부 모듈 사용)
            result = test_funnel_flow(input_data=mock_input, failure_mode=None)
            self.assertIn("분석 시작 메시지", result["status"])
            print("✅ SCN-001: 성공적인 분석 흐름을 확인했습니다.")
        except Exception as e:
            self.fail(f"SCN-001 테스트 실패: 예상치 못한 오류 발생 - {e}")

    def test_002_critical_threshold_error(self):
        """SCN-002: 임계치 경고(Deep Crimson Red) 및 에러 처리 검증."""
        print("\n[TEST] SCN-002: 심각 임계치 오류 주입 테스트 (E-02)")
        # Mock API를 통해 고의적으로 위험한 데이터를 주입합니다.
        mock_input = {"HOMA-IR": 9.8, "BMI": 35.0, "식습관 점수": 12}
        try:
            # Funnel 로직이 임계치를 감지하고 Deep Crimson Red 경고를 출력하는지 확인합니다.
            result = test_funnel_flow(input_data=mock_input, failure_mode="THRESHOLD")
            self.assertIn("Deep Crimson Red 경고 UI", result["warning"])
            print("✅ SCN-002: 임계치 초과 감지 및 Deep Crimson Red 경고 처리를 확인했습니다.")
        except Exception as e:
            self.fail(f"SCN-002 테스트 실패: 예상치 못한 오류 발생 - {e}")

    def test_003_missing_field_validation(self):
        """SCN-001의 확장: 필수 필드 누락 검증 (E-01)."""
        print("\n[TEST] SCN-003: 필수 필드 누락 테스트 (E-01)")
        # HOMA-IR 데이터가 없는 상태로 제출합니다.
        mock_input = {"BMI": 25.0, "식습관 점수": 80}
        try:
            result = test_funnel_flow(input_data=mock_input, failure_mode="MISSING_FIELD")
            self.assertIn("필수 필드 누락", result["error"])
            print("✅ SCN-003: 필수 필드 미입력에 대한 적절한 에러 메시지 표시를 확인했습니다.")
        except Exception as e:
            self.fail(f"SCN-003 테스트 실패: 예상치 못한 오류 발생 - {e}")

    def test_004_network_failure_simulation(self):
        """네트워크 연결 끊김 시뮬레이션 (가장 중요한 리질리언스 검증)."""
        print("\n[TEST] SCN-004: 네트워크 실패 시뮬레이션 테스트")
        # Mock API를 사용하여 강제로 네트워크 오류를 발생시킵니다.
        try:
            test_funnel_flow(input_data={}, failure_mode="NETWORK_FAIL")
            self.fail("네트워크 실패 상황에서 예외가 발생하지 않았습니다.") # 에러가 나야 성공!
        except ConnectionError as e:
            # Funnel이 네트워크 오류를 잡고 사용자에게 친절하게 복구 안내(Fallback)하는지 확인합니다.
            if "네트워크 연결을 다시 시도해 주세요" in str(e):
                print("✅ SCN-004: 네트워크 실패 시 적절한 폴백 로직과 사용자 가이드를 성공적으로 제공했습니다.")
            else:
                 self.fail(f"SCN-004 테스트 실패: 예상된 오류 메시지가 아닙니다 - {str(e)}")


if __name__ == '__main__':
    # unittest.main() 대신 커스텀 실행 로직을 사용합니다.
    print("=============================================")
    print("🧪 Funnel E2E QA 스크립트가 준비되었습니다.")
    print("실행할 테스트 케이스: 4가지 (정상, 임계치 오류, 필드 누락, 네트워크 실패)")
    print("=============================================")

# 주석 처리된 이 코드는 실제 실행 시 unittest 프레임워크를 사용합니다.
# unittest.main(argv=['first-arg-is-ignored'], exit=False)