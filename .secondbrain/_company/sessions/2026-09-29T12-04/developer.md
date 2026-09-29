# 💻 코다리 — tools/funnel_e2e_qa_script.py에서 발생한 'ImportError: attempted relative import with no known parent package' 오류를 수정하세요. 이 문제는 프로젝트 구조(패키징) 문제일 가능성이 높으므로, 해당 모듈이 올바르게 임포트되도록 코드를 수정하고, 테스트 환경 설정(예: PYTHONPATH 추가 또는 __init__.py 파일 점검)을 포함한 해결 방안을 제시합니다.

💻 코다리: 작업 시작합니다.

`ImportError`는 코드 자체의 문제가 아니라, Python 인터프리터가 해당 파일을 '패키지의 일부'로 인식하지 못해서 생기는 구조적 문제입니다. 단순히 `import` 구문을 수정하는 것만으로는 해결이 안 돼요. 프로젝트의 패키징(Packaging) 레벨에서 접근해야 합니다.

먼저 문제를 진단하기 위해 문제가 되는 스크립트의 내용을 읽어보겠습니다. 내부 임포트를 확인해야 어느 부분이 상대 경로 참조(`.` 또는 `..`)를 잘못 사용하고 있는지 파악할 수 있습니다.

<read_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\funnel_e2e_qa_script.py"/>

***(시스템이 파일 내용을 반환하면 다음 단계 진행)***

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\funnel_e2e_qa_script.py (80줄, 4.8KB)
```
 1	import unittest
 2	import os
 3	# 기존의 MockAPIService와 E2E Funnel Test Suite를 임포트하여 사용한다고 가정합니다.
 4	from .MockAPIService import MockAPIService 
 5	from .e2e_funnel_cta_test_suite import test_funnel_flow
 6	
 7	class TestFunnelResilience(unittest.TestCase):
 8	    """
 9	    Mini-App Funnel의 E2E 통합 테스트를 수행하는 리질리언스 검증 스크립트.
10	    네트워크 오류 및 임계치 에러 주입을 핵심 목표로 합니다.
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\funnel_e2e_qa_script.py (80줄)
```
 1	import unittest
 2	import os
 3	# 기존의 MockAPIService와 E2E Funnel Test Suite를 임포트하여 사용한다고 가정합니다.
 4	from .MockAPIService import MockAPIService 
 5	from .e2e_funnel_cta_test_suite import test_funnel_flow
 6	
 7	class TestFunnelResilience(unittest.TestCase):
 8	    """
 9	    Mini-App Funnel의 E2E 통합 테스트를 수행하는 리질리언스 검증 스크립트.
10	    네트워크 오류 및 임계치 에러 주입을 핵심 목표로 합니다.
11	    """
12	
13	    def setUp(self):
14	        """각 테스트가 실행되기 전에 초기화합니다."""
15	        print("\n--- [Test Setup] Mini-App Funnel QA Script 시작 ---")
16	        # Mock API 서비스 인스턴스를 생성하여 모든 테스트에서 사용 가능하게 만듭니다.
17	        self.mock_api = MockAPIService()
18	
19	    def test_001_normal_data_submission(self):
20	        """SCN-001: 정상 데이터 제출 흐름 검증."""
21	        print("\n[TEST] SCN-001: 정상 흐름 테스트 (Success Path)")
22	        # Mock API를 통해 성공 케이스의 가짜 데이터를 주입합니다.
23	        mock_input = {"HOMA-IR": 5.2, "BMI": 28.1, "식습관 점수": 65}
24	        try:
25	            # 실제 Funnel 로직을 테스트하는 함수를 호출 (실제로는 test_funnel_flow 내부 모듈 사용)
26	            result = test_funnel_flow(input_data=mock_input, failure_mode=None)
27	            self.assertIn("분석 시작 메시지", result["status"])
28	            print("✅ SCN-001: 성공적인 분석 흐름을 확인했습니다.")
29	        except Exception as e:
30	            self.fail(f"SCN-001 테스트 실패: 예상치 못한 오류 발생 - {e}")
31	
32	    def test_002_critical_threshold_error(self):
33	        """SCN-002: 임계치 경고(Deep Crimson Red) 및 에러 처리 검증."""
34	        print("\n[TEST] SCN-002: 심각 임계치 오류 주입 테스트 (E-02)")
35	        # Mock API를 통해 고의적으로 위험한 데이터를 주입합니다.
36	        mock_input = {"HOMA-IR": 9.8, "BMI": 35.0, "식습관 점수": 12}
37	        try:
38	            # Funnel 로직이 임계치를 감지하고 Deep Crimson Red 경고를 출력하는지 확인합니다.
39	            result = test_funnel_flow(input_data=mock_input, failure_mode="THRESHOLD")
40	            self.assertIn("Deep Crimson Red 경고 UI", result["warning"])
41	            print("✅ SCN-002: 임계치 초과 감지 및 Deep Crimson Red 경고 처리를 확인했습니다.")
42	        except Exception as e:
43	            self.fail(f"SCN-002 테스트 실패: 예상치 못한 오류 발생 - {e}")
44	
45	    def test_003_missing_field_validation(self):
46	        """SCN-001의 확장: 필수 필드 누락 검증 (E-01)."""
47	        print("\n[TEST] SCN-003: 필수 필드 누락 테스트 (E-01)")
48	        # HOMA-IR 데이터가 없는 상태로 제출합니다.
49	        mock_input = {"BMI": 25.0, "식습관 점수": 80}
50	        try:
51	            result = test_funnel_flow(input_data=mock_input, failure_mode="MISSING_FIELD")
52	            self.assertIn("필수 필드 누락", result["error"])
53	            print("✅ SCN-003: 필수 필드 미입력에 대한 적절한 에러 메시지 표시를 확인했습니다.")
54	        except Exception as e:
55	            self.fail(f"SCN-003 테스트 실패: 예상치 못한 오류 발생 - {e}")
56	
57	    def test_004_network_failure_simulation(self):
58	        """네트워크 연결 끊김 시뮬레이션 (가장 중요한 리질리언스 검증)."""
59	        print("\n[TEST] SCN-004: 네트워크 실패 시뮬레이션 테스트")
60	        # Mock API를 사용하여 강제로 네트워크 오류를 발생시킵니다.
61	        try:
62	            test_funnel_flow(input_data={}, failure_mode="NETWORK_FAIL")
63	            self.fail("네트워크 실패 상황에서 예외가 발생하지 않았습니다.") # 에러가 나야 성공!
64	        except ConnectionError as e:
65	            # Funnel이 네트워크 오류를 잡고 사용자에게 친절하게 복구 안내(Fallback)하는지 확인합니다.
66	            if "네트워크 연결을 다시 시도해 주세요" in str(e):
67	                print("✅ SCN-004: 네트워크 실패 시 적절한 폴백 로직과 사용자 가이드를 성공적으로 제공했습니다.")
68	            else:
69	                 self.fail(f"SCN-004 테스트 실패: 예상된 오류 메시지가 아닙니다 - {str(e)}")
70	
71	
72	if __name__ == '__main__':
73	    # unittest.main() 대신 커스텀 실행 로직을 사용합니다.
74	    print("=============================================")
75	    print("🧪 Funnel E2E QA 스크립트가 준비되었습니다.")
76	    print("실행할 테스트 케이스: 4가지 (정상, 임계치 오류, 필드 누락, 네트워크 실패)")
77	    print("=============================================")
78	
79	# 주석 처리된 이 코드는 실제 실행 시 unittest 프레임워크를 사용합니다.
80	# unittest.main(argv=['first-arg-is-ignored'], exit=False)
```
