import pytest
from fastapi.testclient import TestClient
# 방금 만든 API 서비스 임포트
from backend_api.kpi_service import app

client = TestClient(app)

def test_diagnosis_normal_state():
    """Case 1: 정상 사용자 ID로 호출 시, is_critical이 False여야 한다."""
    response = client.get("/api/v1/kpi/diagnose?user_id=test-normal-user")
    assert response.status_code == 200
    data = response.json()
    # 핵심 검증: Critical 플래그가 False여야 함
    assert data['is_critical'] is False, "Normal user state should not trigger critical flag."

def test_diagnosis_critical_state():
    """Case 2: Critical 상태를 강제 호출 시, is_critical이 True여야 한다."""
    # 테스트용 엔드포인트 사용 (Mocking된 로직)
    response = client.get("/api/v1/kpi/diagnose?user_id=test-critical-user")
    assert response.status_code == 200
    data = response.json()
    # 핵심 검증: Critical 플래그가 True여야 함
    assert data['is_critical'] is True, "Critical user state must trigger critical flag."

def test_loss_curve_steepness():
    """Case 3: 임계점(Critical) 데이터의 손실 예측 곡선 기울기가 급격해야 한다."""
    # Critical 유저 데이터를 다시 받아와서 그래프가 위협적인지 확인
    response = client.get("/api/v1/kpi/diagnose?user_id=test-critical-user")
    data = response.json()
    
    loss_curve = data['loss_prediction_curve']
    
    # 첫 지점 대비 마지막 지점의 손실 증가량 계산 (지표적 검증)
    start_loss = loss_curve[0]['predicted_loss_value']
    end_loss = loss_curve[-1]['predicted_loss_value']
    
    expected_min_increase = 50 # 최소한의 증가 폭을 정의합니다. (상황에 맞게 조정)
    actual_increase = end_loss - start_loss

    # 검증: 손실 예측 곡선이 충분히 가파른지 확인합니다.
    assert actual_increase >= expected_min_increase, f"Loss curve increase ({actual_increase:.2f}) is not steep enough for critical state (Min {expected_min_increase})."