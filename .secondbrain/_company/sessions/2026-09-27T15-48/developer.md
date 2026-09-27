# 💻 코다리 — Mini-App Funnel의 백엔드 로직을 강화하기 위해, 현재 'calculate_adls_score' API에 외부 데이터(예: 사용자 활동량 또는 식습관 인덱스)를 통합하여 점수 계산의 복잡성을 높이는 테스트 모듈을 작성하시오. (단순한 기능 추가가 아닌, 다중 변수를 처리하는 유효성 검증 및 예외 처리가 포함된 확장 API 스켈레톤 코드를 제시할 것.)

💻 코다리: 작업 시작합니다.

CEO님의 지시를 검토했습니다. 단순히 점수를 계산하는 것을 넘어, 외부 데이터를 통합하고 다중 변수에 대한 **견고한 유효성 검증(Validation)**과 **예외 처리(Exception Handling)**가 포함된 테스트 모듈을 구축하는 것이 핵심이군요. 이것은 Mini-App Funnel의 신뢰도를 결정짓는 가장 중요한 부분입니다. ⚙️

현재 `adls_score_calculator.py`와 `test_adls_engine.py` 파일들이 존재합니다. 새로운 변수(활동량, 식습관)를 통합하기 전에, 먼저 기존 로직을 파악하고 확장해야 합니다. 무작정 테스트 코드를 추가하면 실제 계산 함수가 바삭하게 깨질 위험이 있습니다.

따라서 다음 단계를 밟겠습니다:
1.  기존의 점수 계산 함수 정의 및 현재 로직 확인 (`adls_score_calculator.py`).
2.  새로운 변수를 받을 수 있도록 API 스켈레톤을 확장하고, 내부 유효성 검사(Validation) 레이어를 추가합니다.
3.  확장된 기능을 테스트하는 **엣지 케이스 중심의 통합 테스트 모듈** (`test_adls_engine.py` 수정)을 작성하여, "이게 깨지나?"를 완벽히 검증하겠습니다.

### Step 1: 기존 파일 구조 파악 및 로직 읽기
우선 `c:\Data\Project\connect-ai\.secondbrain\_company\_agents\adls_score_calculator.py`와 테스트 파일을 읽겠습니다.

<read_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\adls_score_calculator.py"/>
<read_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\test_adls_engine.py"/>

---
*(시스템이 위 파일을 읽고 그 결과를 다음 턴에 제공할 것입니다.)*

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\adls_score_calculator.py (113줄, 5.0KB)
```
 1	import logging
 2	from typing import Dict, Any, List, Optional
 3	
 4	# 로깅 설정 (디버깅 및 에러 추적용)
 5	logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
 6	
 7	class AdlsScoreCalculator:
 8	    """
 9	    ADLS (Activities of Daily Living Scale) 기반의 점수 계산 로직을 담당하는 클래스.
10	    입력 데이터 유효성 검사 및 예외 처리를 포함하여 신뢰성을 극대화합니다.
...
```
📖 읽기: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\test_adls_engine.py (91줄, 4.8KB)
```
 1	import unittest
 2	from adls_score_calculator import AdlsScoreCalculator, run_unit_tests # Step 2에서 생성한 모듈 임포트
 3	
 4	class TestAdlsScoreEngine(unittest.TestCase):
 5	    """
 6	    calculate_adls_score 함수에 대한 Unit 및 Integration 테스트를 수행합니다.
 7	    """
 8	    def setUp(self):
 9	        """각 테스트 시작 전에 Calculator 인스턴스를 초기화합니다."""
10	        self.calculator = AdlsScoreCalculator()
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\adls_score_calculator.py (113줄)
```
  1	import logging
  2	from typing import Dict, Any, List, Optional
  3	
  4	# 로깅 설정 (디버깅 및 에러 추적용)
  5	logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
  6	
  7	class AdlsScoreCalculator:
  8	    """
  9	    ADLS (Activities of Daily Living Scale) 기반의 점수 계산 로직을 담당하는 클래스.
 10	    입력 데이터 유효성 검사 및 예외 처리를 포함하여 신뢰성을 극대화합니다.
 11	    """
 12	
 13	    def __init__(self):
 14	        # 스코어 가중치 또는 상수 정의 (필요시 확장 가능)
 15	        self.SCORE_WEIGHTS = {
 16	            "mobility": 0.4,
 17	            "cognition": 0.35,
 18	            "self_care": 0.25
 19	        }
 20	
 21	    def _validate_input(self, data: Dict[str, Any]) -> bool:
 22	        """
 23	        입력 데이터의 필수 필드 및 타입 유효성을 검사합니다.
 24	        실패 시 True를 반환하여 호출자에게 명확히 알립니다.
 25	        """
 26	        required_keys = ["mobility", "cognition", "self_care"]
 27	        for key in required_keys:
 28	            if key not in data or data[key] is None:
 29	                logging.error(f"Validation Failed: Missing or null critical input '{key}'.")
 30	                return False
 31	        
 32	        # 추가적인 범위 검사 (예: 점수는 0점에서 1점 사이여야 함)
 33	        for key, value in data.items():
 34	            if isinstance(value, (int, float)) and not (0 <= value <= 1):
 35	                 logging.warning(f"Validation Warning: '{key}' has out-of-range value {value}.")
 36	                 # Out of range는 에러로 처리하기보다 경고 후 기본값 사용을 고려할 수 있으나, 여기서는 일단 Fail 처리
 37	                 return False
 38	
 39	        return True
 40	
 41	
 42	    def calculate_adls_score(self, data: Dict[str, Any]) -> Optional[float]:
 43	        """
 44	        ADLS 지표 기반으로 종합 위험 점수 (0.0 ~ 1.0)를 계산합니다.
 45	
 46	        Args:
 47	            data: 필수 ADLS 데이터를 포함하는 딕셔너리 ({'mobility': float, 'cognition': float, ...})
 48	
 49	        Returns:
 50	            계산된 최종 스코어 (float), 유효성 검사 실패 시 None을 반환합니다.
 51	        """
 52	        logging.info("--- Starting ADLS Score Calculation ---")
 53	        
 54	        # 1. 데이터 유효성 검증 (Guard Clause)
 55	        if not self._validate_input(data):
 56	            logging.error("Cannot calculate score: Input data failed validation checks.")
 57	            return None
 58	
 59	        try:
 60	            # 2. 핵심 로직 계산 (가중 평균 방식 예시)
 61	            mobility_score = float(data["mobility"])
 62	            cognition_score = float(data["cognition"])
 63	            self_care_score = float(data["self_care"])
 64	
 65	            total_weighted_score = (
 66	                mobility_score * self.SCORE_WEIGHTS["mobility"] +
 67	                cognition_score * self.SCORE_WEIGHTS["cognition"] +
 68	                self_care_score * self.SCORE_WEIGHTS["self_care"]
 69	            )
 70	
 71	            # 3. 결과 정규화 및 반환 (Deep Crimson Red의 기준이 되는 스코어)
 72	            final_adls_score = round(max(0.0, min(1.0, total_weighted_score)), 4)
 73	            logging.info(f"Calculation successful. Final ADLS Score: {final_adls_score}")
 74	            return final_adls_score
 75	
 76	        except (ValueError, TypeError) as e:
 77	            # 4. 예외 처리 (Critical Failure Handling)
 78	            logging.critical(f"An unexpected type or value error occurred during score calculation: {e}")
 79	            return None
 80	
 81	
 82	# --- Unit Test Example Function (실제 테스트 스크립트에서 활용될 구조) ---
 83	
 84	def run_unit_tests():
 85	    """단위 레벨의 기능 검증을 수행하는 함수."""
 86	    calculator = AdlsScoreCalculator()
 87	    print("\n--- [Unit Test: Success Case] ---")
 88	    # 1. 정상 케이스 테스트 (모든 점수가 높음 -> 낮은 위험)
 89	    success_data = {"mobility": 0.9, "cognition": 0.8, "self_care": 0.7}
 90	    score_good = calculator.calculate_adls_score(success_data)
 91	    print(f"Test Case (Good): Score={score_good}")
 92	
 93	    print("\n--- [Unit Test: Edge Case - Low Score] ---")
 94	    # 2. 최저 점수 케이스 테스트 (모든 점수가 낮음 -> 높은 위험)
 95	    fail_data = {"mobility": 0.1, "cognition": 0.15, "self_care": 0.05}
 96	    score_bad = calculator.calculate_adls_score(fail_data)
 97	    print(f"Test Case (Bad): Score={score_bad}")
 98	
 99	    print("\n--- [Unit Test: Failure - Missing Key] ---")
100	    # 3. 필수 키 누락 케이스 테스트
101	    missing_key_data = {"mobility": 0.5, "cognition": 0.5} # self_care 누락
102	    score_miss = calculator.calculate_adls_score(missing_key_data)
103	    print(f"Test Case (Missing Key): Score={score_miss}")
104	
105	    print("\n--- [Unit Test: Failure - Invalid Type] ---")
106	    # 4. 잘못된 타입 케이스 테스트 (문자열 입력 시도)
107	    invalid_type_data = {"mobility": "high", "cognition": 0.5, "self_care": 0.5}
108	    score_type = calculator.calculate_adls_score(invalid_type_data)
109	    print(f"Test Case (Invalid Type): Score={score_type}")
110	
111	# 이 함수는 테스트 실행을 위해 별도로 분리하여 사용합니다.
112	if __name__ == '__main__':
113	    run_unit_tests()
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\test_adls_engine.py (91줄)
```
 1	import unittest
 2	from adls_score_calculator import AdlsScoreCalculator, run_unit_tests # Step 2에서 생성한 모듈 임포트
 3	
 4	class TestAdlsScoreEngine(unittest.TestCase):
 5	    """
 6	    calculate_adls_score 함수에 대한 Unit 및 Integration 테스트를 수행합니다.
 7	    """
 8	    def setUp(self):
 9	        """각 테스트 시작 전에 Calculator 인스턴스를 초기화합니다."""
10	        self.calculator = AdlsScoreCalculator()
11	
12	    # --- [Unit Test Coverage] ---
13	    def test_success_case_optimal(self):
14	        """모든 지표가 최적일 때 (낮은 위험, 높은 스코어)의 계산 검증."""
15	        data = {"mobility": 0.9, "cognition": 0.85, "self_care": 0.7} # 가중치: M(0.4), C(0.35), S(0.25)
16	        # 예상 계산값 (임의의 테스트 값): (0.9*0.4 + 0.85*0.35 + 0.7*0.25) = 0.36 + 0.2975 + 0.175 = 0.8325
17	        expected_score = 0.8325
18	        actual_score = self.calculator.calculate_adls_score(data)
19	        self.assertAlmostEqual(actual_score, expected_score, places=4, msg="Optimal score calculation failed.")
20	
21	    def test_failure_case_critical_risk(self):
22	        """모든 지표가 최악일 때 (높은 위험, 낮은 스코어)의 계산 검증."""
23	        data = {"mobility": 0.15, "cognition": 0.2, "self_care": 0.05}
24	        # 예상 계산값: (0.15*0.4 + 0.2*0.35 + 0.05*0.25) = 0.06 + 0.07 + 0.0125 = 0.1425
25	        expected_score = 0.1425
26	        actual_score = self.calculator.calculate_adls_score(data)
27	        self.assertAlmostEqual(actual_score, expected_score, places=4, msg="Critical risk score calculation failed.")
28	
29	    def test_failure_case_missing_input(self):
30	        """필수 입력 데이터가 누락되었을 때 (예외 처리 검증)."""
31	        data = {"mobility": 0.9, "cognition": 0.8} # self_care 누락
32	        actual_score = self.calculator.calculate_adls_score(data)
33	        self.assertIsNone(actual_score, msg="Should return None when critical input is missing.")
34	
35	    def test_failure_case_invalid_type(self):
36	        """입력 데이터 타입이 잘못되었을 때 (예외 처리 검증)."""
37	        data = {"mobility": "high", "cognition": 0.8, "self_care": 0.7} # mobility가 문자열
38	        actual_score = self.calculator.calculate_adls_score(data)
39	        self.assertIsNone(actual_score, msg="Should return None when input type is invalid.")
40	
41	# --- [Integration Test Execution] ---
42	
43	def run_integration_test():
44	    """
45	    Mini-App Funnel의 전체 흐름을 시뮬레이션하며 ADLS 점수 계산이 정상 작동하는지 검증합니다.
46	    (예: 사용자가 폼에 값을 입력하고, 그 값이 DB로 전송되는 과정까지 포함)
47	    """
48	    print("\n=================================================")
49	    print("     🚀 Mini-App Funnel Integration Test Start")
50	    print("=================================================")
51	
52	    # 시나리오 1: 정상 사용자 (점수 산출 -> Deep Crimson Red 위험도 바 적용 검증)
53	    optimal_data = {"mobility": 0.9, "cognition": 0.85, "self_care": 0.7}
54	    score_optimal = AdlsScoreCalculator().calculate_adls_score(optimal_data)
55	
56	    if score_optimal is not None:
57	        print(f"✅ [Pass] Optimal User Score Calculated Successfully: {score_optimal}")
58	        # 여기서 실제 Mini-App Funnel의 '점수 기반 동적 색상 변경' 로직이 호출되어야 합니다.
59	        # 예: if score_optimal > 0.7 -> Green/Yellow, else Deep Crimson Red
60	    else:
61	        print(f"❌ [Fail] Optimal User Score Calculation Failed.")
62	
63	    # 시나리오 2: 위험 사용자 (점수 산출 -> Deep Crimson Red 강제 적용 검증)
64	    risk_data = {"mobility": 0.15, "cognition": 0.2, "self_care": 0.05}
65	    score_risky = AdlsScoreCalculator().calculate_adls_score(risk_data)
66	
67	    if score_risky is not None:
68	        print(f"✅ [Pass] High Risk User Score Calculated Successfully: {score_risky}")
69	        # 이 스코어는 무조건 Deep Crimson Red(#B30000) 강조를 유도해야 합니다.
70	    else:
71	        print(f"❌ [Fail] High Risk User Score Calculation Failed.")
72	
73	    # 시나리오 3: 데이터 입력 실패 (시스템 에러 처리 검증)
74	    error_data = {"mobility": 0.9, "cognition": 0.8} # Missing self_care
75	    score_error = AdlsScoreCalculator().calculate_adls_score(error_data)
76	
77	    if score_error is None:
78	        print("✅ [Pass] System gracefully handled missing data input.")
79	    else:
80	        print(f"❌ [Fail] Did not correctly handle missing data. Received score: {score_error}")
81	        
82	# Unit Test 실행 (Python unittest 프레임워크 사용)
83	if __name__ == '__main__':
84	    # 1. 단위 테스트 실행
85	    print("===============================================")
86	    print("           🧪 Running Unit Tests...")
87	    print("===============================================")
88	    unittest.main(argv=['first-arg-is-ignored'], exit=False)
89	
90	    # 2. 통합 시뮬레이션 실행 (실제 서비스 흐름 검증)
91	    run_integration_test()
```
