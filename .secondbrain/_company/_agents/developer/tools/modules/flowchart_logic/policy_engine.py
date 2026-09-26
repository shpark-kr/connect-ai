from typing import Dict, Any, List

# 정책 구조의 핵심 상태 정의 (Designer Spec 기반 가정)
POLICY_STATES = {
    "initial": {"status": "미확인", "score": 0, "recommendation": "기본 자가 진단 시작"},
    "check_income": {"status": "소득 확인 대기", "required_input": ["annual_income"]},
    "check_family_size": {"status": "가족 규모 확인 대기", "required_input": ["family_members"]},
    "final_diagnosis": {"status": "진단 완료", "recommendation": None}
}

class PolicyEngine:
    """
    정책 비교 Flowchart의 핵심 상태 변화 로직을 관리하는 엔진.
    사용자 입력(State Data)에 따라 다음 최적화된 정책 경로를 결정한다.
    """
    def __init__(self, initial_data: Dict[str, Any]):
        # 초기 데이터는 사용자 질문 답변 등의 형태로 들어옴
        self._current_state = POLICY_STATES["initial"]
        self.user_data = initial_data

    @property
    def current_state(self) -> Dict[str, str]:
        """현재 정책 상태의 요약 정보를 반환한다."""
        return self._current_state

    def update_state(self, input_key: str, input_value: Any) -> Dict[str, str]:
        """
        사용자 입력에 따라 엔진의 상태를 전이시키고 다음 권장 사항을 산출한다.
        :param input_key: 사용자가 답변한 항목 키 (예: 'annual_income')
        :param input_value: 사용자가 제공한 값
        :return: 업데이트된 상태 정보 딕셔너리
        """
        # 입력값 유효성 검사 및 기본 데이터 저장 로직
        self.user_data[input_key] = str(input_value)

        print(f"--- [Engine Update] Key: {input_key}, Value: {input_value} ---")

        if self._current_state['status'] == "미확인":
            # 1단계: 초기 상태 -> 소득 확인 요청 (가장 먼저 필요한 정보)
            return self._transition_to_income_check()
        elif self._current_state['status'].startswith("소득"):
            # 2단계: 소득 확인 완료 -> 가족 규모 확인 요청
            if input_key == "annual_income":
                return self._transition_to_family_check(input_value)
            else:
                # 이미 다른 정보를 입력했거나 흐름이 깨진 경우 (에러 처리 필요)
                return {"status": "흐름 오류", "recommendation": "먼저 소득을 확인해주세요."}
        elif self._current_state['status'].startswith("가족"):
            # 3단계: 가족 규모 확인 완료 -> 최종 진단 실행
            if input_key == "family_members":
                return self.run_final_diagnosis()

        return {"status": "알 수 없음", "recommendation": "시스템 오류로 상태를 업데이트할 수 없습니다."}


    def _transition_to_income_check(self) -> Dict[str, str]:
        """초기 상태에서 소득 확인 단계로 전환합니다."""
        self._current_state = POLICY_STATES["check_income"].copy()
        return {"status": "소득 확인 필요", "recommendation": "가장 먼저 연간 소득을 알려주세요."}

    def _transition_to_family_check(self, income: Any) -> Dict[str, str]:
        """소득 정보가 들어오면 가족 규모 확인 단계로 전환합니다."""
        # 실제 로직에서는 이 시점에서 소득과 연동된 중간 점수 산출이 필요함.
        self._current_state = POLICY_STATES["check_family_size"].copy()
        return {"status": "가족 구성원 확인 필요", "recommendation": f"소득({income})를 바탕으로 가족 규모(명)를 알려주세요."}

    def run_final_diagnosis(self) -> Dict[str, str]:
        """모든 데이터 수집이 완료되었을 때 최종 진단 및 권고를 수행합니다."""
        # 실제로는 user_data 전체를 이용해 복잡한 가중치 기반 계산 로직 실행
        recommendation = "✅ 현재 조건으로 볼 때, 'OOO 지원 제도'의 자격 요건 충족 가능성이 높습니다. 상세 상담이 필요합니다."
        self._current_state = POLICY_STATES["final_diagnosis"].copy()
        return {"status": "진단 완료", "recommendation": recommendation}

# 예시 사용법 (테스트에서 활용됨)
if __name__ == "__main__":
    engine = PolicyEngine({})
    print("--- Initial State ---")
    print(engine.current_state)

    # 1. 소득 입력
    result1 = engine.update_state("annual_income", 50000000)
    print("\n--- Step 1 Result ---")
    print(result1)

    # 2. 가족 구성원 입력 (가정)
    result2 = engine.update_state("family_members", 4)
    print("\n--- Step 2 Result ---")
    print(result2)

    # 3. 최종 진단 실행
    result3 = engine.update_state("dummy", None) # 임시 입력으로 트리거링 가정
    print("\n--- Step 3 Result (Final Diagnosis) ---")
    print(result3)