# src/gap_calculator.py
"""
Gap 금액 계산 핵심 로직 모듈 (Single Responsibility Principle 준수)
이 파일은 비즈니스 로직을 담고 있으며, FastAPI 엔드포인트와 독립적으로 테스트 가능하도록 설계되었습니다.

[공적 지원 시스템의 Gap 자각 모델]
전제: 사용자가 현재 받는 공적/개인 자원(Resource)과 필요한 이상적인 수준(Ideal State) 간의 격차를 수치화합니다.
Gap 금액 = Ideal Cost - Available Resource (가중치 적용)
"""

from typing import Dict, Any
import math

# --- 가중치 정의 (비즈니스 변수) ---
WEIGHTS = {
    "nursing_care": 0.4,  # 요양: 가장 중요도가 높음
    "pension": 0.3,       # 연금: 재정적 안정성 관련
    "housing": 0.3        # 주거: 생활 기반 필수 요소
}

def calculate_gap(user_inputs: Dict[str, Any]) -> Dict[str, float]:
    """
    요양, 연금, 주거 3가지 영역별 Gap 금액을 계산합니다.
    :param user_inputs: 각 영역의 '이상 비용'과 '현재 수입/지원을 담은 Dictionary'.
                         예: {"nursing_care": {"ideal_cost": 5000, "available_resource": 2000}}
    :return: 계산된 Gap 금액을 포함하는 JSON 형식의 Dictionary.
    """
    gap_results = {}

    # 필수 입력값 검증 (Defensive Coding)
    if not all(key in user_inputs for key in ["nursing_care", "pension", "housing"]):
        raise ValueError("Gap 계산을 위해서는 요양, 연금, 주거 3가지 영역의 데이터가 모두 필요합니다.")

    try:
        # 1. 요양 서비스 Gap 계산
        nc = user_inputs["nursing_care"]
        gap_nc = nc["ideal_cost"] - nc["available_resource"]
        gap_results["nursing_care_gap"] = max(0.0, round(gap_nc * WEIGHTS["nursing_care"], 2))

        # 2. 연금 Gap 계산
        pen = user_inputs["pension"]
        gap_pen = pen["ideal_cost"] - pen["available_resource"]
        gap_results["pension_gap"] = max(0.0, round(gap_pen * WEIGHTS["pension"], 2))

        # 3. 주거 서비스 Gap 계산
        house = user_inputs["housing"]
        gap_house = house["ideal_cost"] - house["available_resource"]
        gap_results["housing_gap"] = max(0.0, round(gap_house * WEIGHTS["housing"], 2))

    except KeyError as e:
        # 특정 키가 누락되었을 때 발생하는 오류 처리
        raise ValueError(f"입력 데이터 구조 오류: 필수 필드 {e}를 확인해 주세요.")


    # 최종 총 Gap 금액 계산 (합산 및 반올림)
    total_gap = sum([
        gap_results["nursing_care_gap"], 
        gap_results["pension_gap"], 
        gap_results["housing_gap"]
    ])
    
    return {
        "status": "success",
        "message": "Ideal-Reality Gap 계산이 완료되었습니다. 총 Gap 금액을 확인하세요.",
        # 각 영역별 Gap 금액 제공 (세부 분석용)
        "detailed_gaps": gap_results,
        # 최종 사용자에게 제시할 수치화된 손실액 (Critical Red 강조 부분)
        "total_gap_amount": round(total_gap, 2)
    }

def calculate_overall_risk_score(gap_amounts: Dict[str, float]) -> float:
    """
    전체 Gap 금액을 바탕으로 서비스 이용의 '구조적 위험 점수'를 산출합니다. (0~100점)
    Gap이 클수록 높은 점수를 부여하여 긴급성을 강조합니다.
    (가상의 로직, 실제 비즈니스 모델에 따라 조정 필요)
    """
    total = sum(gap_amounts.values())
    # 예: 총 Gap 금액을 100만 원 단위로 나누어 스케일링 (예시 공식)
    risk_score = min(100.0, total / 50000.0 + 20.0) # 최소 점수 20점 보장
    return round(risk_score, 2)

if __name__ == "__main__":
    # 로컬 테스트용 실행 예시 (직접 호출 시)
    print("--- Gap Calculator Module Test Run ---")
    mock_inputs = {
        "nursing_care": {"ideal_cost": 5000, "available_resource": 1000}, # Gap: 4000 * 0.4 = 1600
        "pension": {"ideal_cost": 3000, "available_resource": 2500},       # Gap: 500 * 0.3 = 150
        "housing": {"ideal_cost": 2000, "available_resource": 1800}        # Gap: 200 * 0.3 = 60
    }
    try:
        result = calculate_gap(mock_inputs)
        print("\n[✅ Success] API Result:")
        import json
        print(json.dumps(result, indent=4))
        risk_score = calculate_overall_risk_score(result["detailed_gaps"])
        print(f"\n[⚠️ Risk Score] 계산된 전체 구조적 위험 점수: {risk_score}점")

    except ValueError as e:
        print(f"\n[❌ Error] Gap 계산 실패: {e}")