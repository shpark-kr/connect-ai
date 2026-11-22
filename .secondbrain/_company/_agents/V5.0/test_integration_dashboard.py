import unittest
from typing import List, Dict
# 💡 실제로는 core_scoring_service에서 import 해야 합니다.
# from .core_scoring_service import get_dashboard_scores

# Mocking the functions for isolated testing environment setup
def calculate_ci_score(interactions: List[Dict]) -> float:
    if not interactions: return 0.1
    scroll_depths = [i['value'] for i in interactions if i['type'] == 'scroll_depth' and i['value'] is not None]
    cta_clicks = sum(1 for i in interactions if i['type'] == 'click')
    score = 0.4 * (scroll_depths[-1] / 100) + 0.5 * min(cta_clicks, 3) * 0.2 + 0.1 * len(interactions) / 10
    return round(min(max(score, 0.1), 1.0), 4)

def calculate_risk_fit_score(content_meta: Dict, interactions: List[Dict]) -> float:
    risk_weights = {'Low': 0.2, 'Medium': 0.5, 'High': 0.9}
    severity_weight = risk_weights.get(content_meta.get('severityLevel', 'Medium'), 0.5)
    intent_score = calculate_ci_score([i for i in interactions if i['type'] == 'scroll_depth'])
    lack_of_engagement_factor = 1 - intent_score
    score = severity_weight * lack_of_engagement_factor * 0.8 + 0.2
    return round(min(max(score, 0.1), 1.0), 4)

def get_dashboard_scores(payload: Dict) -> Dict:
    interactions = payload['interactions']
    content_meta = payload['contentMeta']
    ci_score = calculate_ci_score(interactions)
    risk_fit_score = calculate_risk_fit_score(content_meta, interactions)

    is_critical = ci_score < 0.4 and risk_fit_score > 0.75
    suggested_action = "MiniFunnel CTA 재강조" if is_critical else "다음 Defect ID 탐색 유도"
    return {"ciScore": ci_score, "riskFitScore": risk_fit_score, "isCriticalAlert": is_critical, "suggestedAction": suggested_action}


class TestDashboardEngine(unittest.TestCase):

    def setUp(self):
        # 🧪 테스트 케이스 1: 고위험/저의도 (가장 필요한 시나리오)
        self.high_risk_low_intent_payload = {
            "userId": "user_fail",
            "interactions": [
                {"type": "scroll_depth", "elementId": "", "timestamp": 1678880000, "value": 25}, # 스크롤이 매우 짧음
                {"type": "click", "elementId": "#header-logo", "timestamp": 1678880010} # 단순 탐색 클릭만 있음
            ],
            "contentMeta": {
                "defectId": "ArterialStiffening",
                "severityLevel": "High", # High Severity
                "targetAudienceGroup": "50-60s",
                "ctaType": "ConsultationBooking"
            }
        }

        # 🧪 테스트 케이스 2: 저위험/고의도 (이상적 시나리오)
        self.low_risk_high_intent_payload = {
            "userId": "user_success",
            "interactions": [
                {"type": "scroll_depth", "elementId": "", "timestamp": 1678880000, "value": 95}, # 깊게 스크롤함
                {"type": "click", "elementId": "#cta-download", "timestamp": 1678880050}, # 핵심 CTA 클릭
                {"type": "scroll_depth", "elementId": "", "timestamp": 1678880100, "value": 98}
            ],
            "contentMeta": {
                "defectId": "HypoglycemiaRisk",
                "severityLevel": "Medium", # Medium Severity
                "targetAudienceGroup": "40-50s",
                "ctaType": "Download"
            }
        }

    def test_high_risk_low_intent(self):
        """테스트 1: 위험도는 높으나 사용자의 의도가 낮은 경우 (Critical Alert 기대)"""
        result = get_dashboard_scores(self.high_risk_low_intent_payload)
        print("\n[TEST RUN] High Risk/Low Intent Test:")
        print(f"  CI Score: {result['ciScore']:.2f}, RF Score: {result['riskFitScore']:.2f}")
        self.assertTrue(result['isCriticalAlert'], "High Risk/Low Intent 상황에서 Critical Alert가 발생해야 합니다.")

    def test_low_risk_high_intent(self):
        """테스트 2: 위험도는 적정하나 사용자의 의도가 높은 경우 (Safe Zone 기대)"""
        result = get_dashboard_scores(self.low_risk_high_intent_payload)
        print("\n[TEST RUN] Low Risk/High Intent Test:")
        print(f"  CI Score: {result['ciScore']:.2f}, RF Score: {result['riskFitScore']:.2f}")
        # 이 경우 Critical Alert가 발생해서는 안 됨.
        self.assertFalse(result['isCriticalAlert'], "High Intent 상황에서 Critical Alert가 발생하면 안 됩니다.")


if __name__ == '__main__':
    unittest.main()