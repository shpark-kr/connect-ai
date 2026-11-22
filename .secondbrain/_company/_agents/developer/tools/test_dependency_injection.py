import unittest
from unittest.mock import MagicMock
# 실제 프로젝트 구조에 따라 이 임포트 경로는 달라질 수 있습니다.
# 현재는 오케스트레이터의 함수가 모듈 레벨에서 접근 가능하다고 가정합니다.
from e2e_publishing_orchestrator import e2e_publishing_orchestrator 

class TestPublishingOrchestration(unittest.TestCase):
    """
    e2e_publishing_orchestrator의 핵심 의존성 주입(client) 로직을 테스트합니다.
    Goal: 'missing positional argument' 에러를 재현하고 수정하는 것을 목표로 합니다.
    """

    def setUp(self):
        # API 클라이언트를 Mocking하여 실제 외부 호출 없이 테스트할 수 있도록 설정합니다.
        self.mock_client = MagicMock()
        self.mock_content_data = {
            "title": "Defect ID 보고서 V3.0", 
            "assets": ["image1.jpg", "video2.mp4"], 
            "target_audience": "40-60대 중장년층"
        }

    def test_orchestrator_with_valid_client(self):
        """
        [SUCCESS CASE] 필수 클라이언트 객체를 성공적으로 전달했을 때 오케스트레이터가 정상 작동하는지 확인합니다.
        이 테스트는 'client' 인자가 누락되지 않았음을 보장합니다.
        """
        print("\n--- Running test_orchestrator_with_valid_client ---")
        # Mocking된 client를 전달하여 함수 호출
        try:
            e2e_publishing_orchestrator(self.mock_client, self.mock_content_data)
            print("✅ Test Passed: 오케스트레이터가 클라이언트를 통해 성공적으로 실행되었습니다.")
        except Exception as e:
            self.fail(f"Expected successful execution but failed with error: {e}")

    def test_orchestrator_missing_client_failure(self):
        """
        [FAILURE CASE] Client 객체를 누락했을 때, 예상되는 'Missing Argument' 에러가 발생하는지 확인합니다.
        이 테스트는 실제 환경에서 발생했던 버그를 재현하는 역할을 합니다.
        """
        print("\n--- Running test_orchestrator_missing_client_failure ---")
        # client 인자를 의도적으로 생략하여 실패 유도 (버그 재현)
        with self.assertRaises(TypeError) as context:
            e2e_publishing_orchestrator(self.mock_content_data) 
        
        expected_error = "missing 1 required positional argument: 'client'"
        self.assertIn(expected_error, str(context.exception))
        print(f"✅ Test Passed: 예상된 오류 '{expected_error}'를 정확히 재현했습니다.")

if __name__ == '__main__':
    unittest.main()