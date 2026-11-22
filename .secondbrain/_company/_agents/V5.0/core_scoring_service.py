import json
from typing import List, Dict
# Assuming we use the schema defined above for type hinting consistency
# from .dashboard_schema import ApiInputPayload, ScoreResult 

# --- Core Scoring Logic Functions (Unit Testable) ---

def calculate_ci_score(interactions: List[Dict]) -> float:
    """
    CI-Score 계산 로직. 사용자 상호작용 이벤트의 '깊이'와 '빈도'를 분석하여 의도를 산출합니다.
    높은 스크롤 깊이 + CTA 클릭 > 높은 점수
    Args: interactions: UserInteractionEvent 리스트.
    Returns: CI Score (0.0 to 1.0).
    """
    if not interactions:
        return 0.1 # 최소 기본값 설정

    scroll_depths = [i['value'] for i in interactions if i['type'] == 'scroll_depth' and i['value'] is not None]
    cta_clicks = sum(1 for i in interactions if i['type'] == 'click')

    # 가중치 부여 로직: 스크롤 깊이 (40%) + CTA 클릭 (50%) + 빈도 (10%)
    score = 0.4 * (scroll_depths[-1] / 100) + 0.5 * min(cta_clicks, 3) * 0.2 + 0.1 * len(interactions) / 10
    
    return round(min(max(score, 0.1), 1.0), 4)


def calculate_risk_fit_score(content_meta: Dict, interactions: List[Dict]) -> float:
    """
    Risk-Fit Score 계산 로직. 콘텐츠의 위험도와 사용자 상태 적합성을 비교합니다.
    'High' Severity + 'Low' Intent (미흡한 반응) = 높은 Risk Fit (위험 노출 가능성 높음).
    Args: content_meta: ContentMetadata 딕셔너리.
    Returns: Risk-Fit Score (0.0 to 1.0).
    """
    # 위험도 가중치 정의
    risk_weights = {'Low': 0.2, 'Medium': 0.5, 'High': 0.9}
    severity_weight = risk_weights.get(content_meta.get('severityLevel', 'Medium'), 0.5)

    # 사용자의 의도 점수가 낮으면 (상호작용이 적으면), 위험 노출은 높다고 판단합니다.
    intent_score = calculate_ci_score([i for i in interactions if i['type'] == 'scroll_depth'])
    lack_of_engagement_factor = 1 - intent_score

    # 최종 점수: (위험도 가중치 * Lack of Engagement) + 기본 상수
    score = severity_weight * lack_of_engagement_factor * 0.8 + 0.2
    
    return round(min(max(score, 0.1), 1.0), 4)


# --- API Endpoint Mockup (FastAPI Style) ---

def get_dashboard_scores(payload: Dict) -> Dict:
    """
    V5.0 핵심 점수 계산을 수행하는 엔드포인트 역할의 함수입니다.
    Payload는 ApiInputPayload 구조를 가져야 합니다.
    """
    try:
        interactions = payload['interactions']
        content_meta = payload['contentMeta']

        ci_score = calculate_ci_score(interactions)
        risk_fit_score = calculate_risk_fit_score(content_meta, interactions)

        # 최종 판단 로직 (Critical Alert Trigger)
        is_critical = ci_score < 0.4 and risk_fit_score > 0.75 # 의도는 낮은데 위험 노출은 높은 상황
        suggested_action = "MiniFunnel CTA 재강조" if is_critical else "다음 Defect ID 탐색 유도"

        return {
            "ciScore": ci_score,
            "riskFitScore": risk_fit_score,
            "isCriticalAlert": is_critical,
            "suggestedAction": suggested_action
        }
    except Exception as e:
        print(f"Error processing dashboard scores: {e}")
        # 실패 시 안전한 기본값 반환 (Fallback)
        return {"ciScore": 0.3, "riskFitScore": 0.5, "isCriticalAlert": False, "suggestedAction": "Default Flow"}

if __name__ == '__main__':
    print("--- Core Scoring Service Test Run ---")
    # Mock Data for testing (High Risk Scenario)
    mock_payload = {
        "userId": "testuser123",
        "interactions": [
            {"type": "scroll_depth", "elementId": "", "timestamp": 1678880000, "value": 25}, # 스크롤 조금만 함
            {"type": "click", "elementId": "#header-logo", "timestamp": 1678880010} # 헤더 로고 클릭만 함
        ],
        "contentMeta": {
            "defectId": "ArterialStiffening",
            "severityLevel": "High",
            "targetAudienceGroup": "50-60s",
            "ctaType": "ConsultationBooking"
        }
    }
    
    scores = get_dashboard_scores(mock_payload)
    print("\n[TEST RESULT: High Risk Scenario]")
    print(json.dumps(scores, indent=4))

    # Mock Data for testing (Low Risk/High Intent Scenario)
    mock_payload_success = {
        "userId": "testuser456",
        "interactions": [
            {"type": "scroll_depth", "elementId": "", "timestamp": 1678880000, "value": 90}, # 깊게 스크롤 함
            {"type": "click", "elementId": "#cta-download", "timestamp": 1678880050}, # 다운로드 CTA 클릭
            {"type": "scroll_depth", "elementId": "", "timestamp": 1678880100, "value": 95}
        ],
        "contentMeta": {
            "defectId": "HypoglycemiaRisk",
            "severityLevel": "Medium",
            "targetAudienceGroup": "40-50s",
            "ctaType": "Download"
        }
    }

    scores_success = get_dashboard_scores(mock_payload_success)
    print("\n[TEST RESULT: Low Risk/High Intent Scenario]")
    print(json.dumps(scores_success, indent=4))