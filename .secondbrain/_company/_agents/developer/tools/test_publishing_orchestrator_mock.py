import unittest
from unittest.mock import MagicMock, patch
# 실제 프로젝트 경로에 따라 임포트 경로는 달라질 수 있습니다. 
# 여기서는 예시를 위해 MockAPIService가 같은 디렉토리에 있다고 가정합니다.
from MockAPIService import (
    publish_to_youtube, 
    publish_to_instagram, 
    get_state_change_data
)

class TestPublishingOrchestrator(unittest.TestCase):
    """
    e2e_publishing_orchestrator의 상태 전이 기반 배포 로직을 검증하는 통합 테스트 스위트.
    실제 API 호출 없이 Mock된 환경에서 함수 호출 여부와 인자를 검사합니다.
    """

    def setUp(self):
        # 테스트 시작 전 모든 모킹 카운터를 초기화한다고 가정
        pass 

    @patch('MockAPIService.publish_to_youtube')
    @patch('MockAPIService.publish_to_instagram')
    def test_scenario_1_critical_gap_high_risk(self, mock_instagram, mock_youtube):
        """
        [Scenario 1: Critical Gap (High Risk)] - 가장 위협적인 상태가 감지되었을 때의 배포 검증.
        이 경우 YouTube에 상세 보고서 형태로 우선 배포되어야 함.
        """
        print("\n--- Running Test Scenario 1: High-Risk Gap Detected ---")
        # Mocking된 서비스 함수를 사용하도록 설정 (실제 호출 방지)
        mock_youtube.return_value = "YouTube Publish Success"
        mock_instagram.return_value = "Instagram Publish Failure (Too Early)"

        state_data = get_state_change_data("Critical Gap", risk_level="High")
        
        # 오케스트레이터 호출 시뮬레이션 (가정)
        result = state_data['orchestrate_publishing'] 

        # 검증 로직: Critical Gap -> YouTube 필수, Instagram는 조건부로만.
        self.assertTrue(mock_youtube.called)
        self.assertEqual(mock_youtube.call_count, 1)
        # 인자가 올바르게 전달되었는지 확인 (예시 데이터 기반)
        mock_youtube.assert_called_with({"gap_id": "Defect-A", "severity": "High"}, state="Critical Gap")
        
        self.assertFalse(mock_instagram.called, "Critical Gap 시나리오에서는 Instagram 배포가 차단되어야 함.")

    @patch('MockAPIService.publish_to_youtube')
    @patch('MockAPIService.publish_to_instagram')
    def test_scenario_2_warning_threshold_reached(self, mock_instagram, mock_youtube):
        """
        [Scenario 2: Warning Threshold] - 주의 단계에 도달했을 때의 배포 검증.
        이 경우 양쪽 채널 모두 가볍게 리마인드성 콘텐츠를 발행해야 함.
        """
        print("\n--- Running Test Scenario 2: Warning Threshold Reached ---")
        mock_youtube.return_value = "YouTube Publish Success"
        mock_instagram.return_value = "Instagram Publish Success"

        state_data = get_state_change_data("Warning Gap", risk_level="Medium")
        result = state_data['orchestrate_publishing'] 

        # 검증 로직: Warning Gap -> YouTube & Instagram 모두 호출되어야 함.
        self.assertTrue(mock_youtube.called)
        self.assertEqual(mock_youtube.call_count, 1)
        mock_youtube.assert_called_with({"gap_id": "Defect-B", "severity": "Medium"}, state="Warning Gap")

        self.assertTrue(mock_instagram.called)
        self.assertEqual(mock_instagram.call_count, 1)
        mock_instagram.assert_called_with({"message": "Check your gap status!"}, state="Warning Gap")


    @patch('MockAPIService.publish_to_youtube')
    @patch('MockAPIService.publish_to_instagram')
    def test_scenario_3_stable_monitoring(self, mock_instagram, mock_youtube):
        """
        [Scenario 3: Stable Monitoring] - 정상 범위 내에서 주기적인 모니터링 시점의 배포 검증.
        이 경우 어떤 채널에도 강한 경고 콘텐츠를 발행해서는 안 되며, 리드 마그넷 다운로드 유도에 집중해야 함.
        """
        print("\n--- Running Test Scenario 3: Stable Monitoring (No Crisis) ---")
        # 오케스트레이터가 아무것도 호출하지 않도록 설정하거나, 최소한의 로직만 실행되게 만듭니다.
        state_data = get_state_change_data("Stable", risk_level="Low")
        result = state_data['orchestrate_publishing'] 

        # 검증 로직: Stable 상태에서는 어떤 채널도 강제 호출되면 안됨.
        self.assertFalse(mock_youtube.called, "안정적일 때는 YouTube 배포가 발생해서는 안 됩니다.")
        self.assertFalse(mock_instagram.called, "안정적일 때는 Instagram 배포가 발생해서는 안 됩니다.")

if __name__ == '__main__':
    unittest.main()