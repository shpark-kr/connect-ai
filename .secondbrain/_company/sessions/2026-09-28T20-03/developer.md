# 💻 코다리 — Mini-App Funnel의 핵심 진단 로직(test_diagnosis_engine.py)을 전면 재점검하고, 과거 발생했던 SyntaxError 및 네트워크 흐름 에러를 모두 수정하여 E2E 테스트가 가능한 수준으로 코드를 안정화하십시오. 특히 'HOMA-IR 하락' 등 위기 상황 데이터 주입 시 Funnel이 멈추지 않고 다음 단계(Mini-App 화면)로 매끄럽게 이탈하는 로직을 최우선으로 확보해야 합니다.

💻 코다리: 작업 시작합니다.

CEO 지시 내용과 기존 메모리를 종합해 보니, 현재 가장 높은 우선순위를 가진 병목 구간은 **Mini-App Funnel 진입의 기술적 안정성**입니다. 특히 'HOMA-IR 하락' 같은 위기 상황 데이터가 발생했을 때 시스템이 멈추는 것은 치명적인 사용자 경험(UX) 오류이며, 이는 곧 수익화 퍼널 이탈로 이어집니다.

저는 우선 `test_diagnosis_engine.py`를 전면 분석하여 과거에 보고된 SyntaxError와 네트워크 흐름 에러를 모두 수정하고, 위기 데이터 발생 시 다음 단계(Mini-App 진입 로직)로의 매끄러운 비동기 이탈을 최우선 목표로 코드를 안정화하겠습니다.

가장 먼저, 현재 `test_diagnosis_engine.py`의 코드가 어떤 구조인지 파악하는 작업이 필요합니다. 제가 직접 파일을 읽어보겠습니다.

<read_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\test_diagnosis_engine.py"/>

📊 평가: 진행중 — 핵심 진단 로직의 현황 파악이 선행되어야 안정화 작업 착수가 가능합니다.
📝 다음 단계: 파일 내용 분석 후, 발견된 에러 포인트와 흐름 제어 로직을 수정하고 E2E 테스트를 재실행할 것입니다.

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\test_diagnosis_engine.py (61줄, 3.1KB)
```
 1	import unittest
 2	from c.Data.Project.connect-ai.services.diagnosis_engine import ( # Mocked import path for testing
 3	    DiagnosisEngineService, 
 4	    UserProfile, 
 5	    PolicyData, 
 6	    failed_attempts, # 테스트를 위해 글로벌 상태 접근 필요
 7	    MAX_RETRIES,
 8	    INITIAL_BACKOFF
 9	)
10	
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\test_diagnosis_engine.py (61줄)
```
 1	import unittest
 2	from c.Data.Project.connect-ai.services.diagnosis_engine import ( # Mocked import path for testing
 3	    DiagnosisEngineService, 
 4	    UserProfile, 
 5	    PolicyData, 
 6	    failed_attempts, # 테스트를 위해 글로벌 상태 접근 필요
 7	    MAX_RETRIES,
 8	    INITIAL_BACKOFF
 9	)
10	
11	# NOTE: 실제 환경에서는 'time.sleep'을 모킹하는 것이 좋으나, 여기서는 구조적 검증에 집중합니다.
12	
13	class TestDiagnosisEngine(unittest.TestCase):
14	
15	    def setUp(self):
16	        """테스트 시작 전 초기화"""
17	        self.engine = DiagnosisEngineService()
18	        # 테스트를 위해 재시도 횟수 카운터를 리셋하는 가상의 함수가 필요함 (실제로는 __init__에서 해결되어야 함)
19	        global failed_attempts
20	        failed_attempts = 0
21	
22	    def test_successful_gap_calculation(self):
23	        """정상적인 데이터 흐름으로 Gap 계산이 정상적으로 이루어지는지 확인합니다."""
24	        print("\n--- Running Test: Successful Calculation ---")
25	        # Mocking Success Path (API가 처음부터 성공한다고 가정)
26	        original_fetch = DiagnosisEngineService.fetch_policy_data_from_api # 가상의 원본 함수 호출 방지
27	        DiagnosisEngineService.fetch_policy_data_from_api = lambda g, u: PolicyData(g, 20_000_000, 6_000_000)
28	
29	        user = UserProfile(age=58, retirement_savings=120.0, current_pension=130)
30	        policy_data = PolicyData("장기 간병/돌봄 서비스", 20_000_000, 6_000_000)
31	
32	        # 기대 값 계산: (20M - 6M) = 14M. Safety Margin(예시): 1.2억*0.1 + 390만 = 1,500만원. Max(14M, 14M-15M) -> 14M
33	        result = self.engine.calculate_gap(policy_data, user)
34	
35	        self.assertIsNotNone(result)
36	        # 계산 로직에 따라 값이 달라질 수 있으므로 'Gap 항목'과 결과가 성공적으로 도출되는지만 검증합니다.
37	        self.assertTrue("장기 간병/돌봄 서비스" in result.gap_name)
38	        print("✅ Test Passed: 기본 Gap 계산 및 구조체 반환 확인 완료.")
39	
40	    def test_api_resilience_with_backoff(self):
41	        """API 호출 실패 -> 재시도 -> 성공하는 시나리오를 테스트합니다 (가장 중요)."""
42	        print("\n--- Running Test: API Resilience & Backoff ---")
43	        
44	        # Mocking Failure/Success Path (실제 코드가 2회 실패 후 성공하도록 설계됨)
45	        # NOTE: 이 테스트는 실제로 내부의 _mock_api_call 함수를 호출하게 됩니다.
46	
47	        user = UserProfile(age=58, retirement_savings=100.0, current_pension=100)
48	        policy_data = PolicyData("장기 간병/돌봄 서비스", 20_000_000 * (1 + failed_attempts), 6_000_000)
49	
50	        # 이 호출이 내부적으로 재시도 로직을 통과해야 함
51	        result = self.engine.calculate_gap(policy_data, user)
52	
53	        self.assertIsNotNone(result)
54	        print("✅ Test Passed: API가 여러 번의 실패(ConnectionError)를 겪은 후 성공적으로 데이터를 가져와 Gap 계산에 사용했음을 확인했습니다.")
55	
56	
57	if __name__ == '__main__':
58	    # 테스트 실행 (실제 환경에서는 pytest -m test_diagnosis_engine.py 를 권장합니다.)
59	    unittest.main()
60	
61	###
```
