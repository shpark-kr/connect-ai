# 💻 코다리 — 지난번 실행된 'funnel_e2e_qa_script'의 ImportError 오류를 해결하는 것이 최우선입니다. 특히, 상대 경로 임포트(relative import) 문제와 MockAPIService 연결 문제를 수정하고, Funnel 전체 사용자 여정(유입 → 위험 감지 → 진단 보고서 구매 시도)에 걸친 E2E QA 스크립트를 완벽하게 재작성 및 디버깅하십시오. 코드를 수정한 후에는 반드시 핵심 API 호출 로직과 트래킹 시스템이 정상 작동하는지 통합 테스트를 거쳐야 합니다.

💻 코다리: 작업 시작합니다. ⚙️

CEO 지시사항을 확인했습니다. `funnel_e2e_qa_script`의 `ImportError` 해결과 E2E QA 스크립트 재작성은 현재 가장 높은 우선순위입니다. 상대 경로 임포트는 구조적 문제일 가능성이 높고, MockAPI 연결 문제는 환경 설정 또는 초기화 로직에 문제가 있다는 뜻입니다.

코드는 근거가 없으면 건드리면 안 됩니다. 먼저 기존 `funnel_e2e_qa_script`의 코드를 읽어보고, 현재 임포트 구조와 API 호출 패턴을 파악하는 것이 필수적입니다.

또한, 원래 사용자 명령에서 요청하신 대로 전체 목표를 검토했습니다. 이미 Funnel과 CTA에 대한 테스트가 집중적으로 이루어졌으므로, 다음으로 가장 가치 있는 단일 작업은 **"QA 스크립트 수정 후, 최종적인 배포 및 출판 통합 환경 자체를 점검하는 것"**입니다. 즉, QA가 성공해도 실제로 웹사이트나 콘텐츠 시스템 전체에서 문제가 발생할 수 있습니다.

따라서 1차 목표(스크립트 디버깅)에 집중하되, 이 과정은 **전체 파이프라인 안정화**라는 더 큰 맥락의 일부임을 인지하겠습니다.

### 🛠️ Step 1: 기존 QA 스크립트 코드 검토

먼저 `funnel_e2e_qa_script.py`를 읽어서 현재 어떤 모듈 간에 임포트가 발생하고, API 호출이 어떻게 이루어지는지 확인하겠습니다.

<read_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\funnel_e2e_qa_script.py"/>

📊 평가: 진행중 — QA 스크립트의 현재 구조와 의존성을 파악해야 오류 수정 작업이 가능합니다.
📝 다음 단계: (read 결과 확인 후) `ImportError`가 발생한 부분을 분석하여, 상대 경로 임포트를 수정하고 MockAPI 연결 로직을 재작성하는 방향으로 코드를 편집하겠습니다.

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\funnel_e2e_qa_script.py (89줄, 5.0KB)
```
 1	import unittest
 2	import sys
 3	from pathlib import Path
 4	
 5	CURRENT_DIR = Path(__file__).resolve().parent
 6	if str(CURRENT_DIR) not in sys.path:
 7	    sys.path.insert(0, str(CURRENT_DIR))
 8	
 9	try:
10	    from .MockAPIService import MockAPIService 
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\funnel_e2e_qa_script.py (89줄)
```
 1	import unittest
 2	import sys
 3	from pathlib import Path
 4	
 5	CURRENT_DIR = Path(__file__).resolve().parent
 6	if str(CURRENT_DIR) not in sys.path:
 7	    sys.path.insert(0, str(CURRENT_DIR))
 8	
 9	try:
10	    from .MockAPIService import MockAPIService 
11	    from .e2e_funnel_cta_test_suite import test_funnel_flow
12	except ImportError:
13	    from MockAPIService import MockAPIService 
14	    from e2e_funnel_cta_test_suite import test_funnel_flow
15	
16	class TestFunnelResilience(unittest.TestCase):
17	    """
18	    Mini-App Funnel의 E2E 통합 테스트를 수행하는 리질리언스 검증 스크립트.
19	    네트워크 오류 및 임계치 에러 주입을 핵심 목표로 합니다.
20	    """
21	
22	    def setUp(self):
23	        """각 테스트가 실행되기 전에 초기화합니다."""
24	        print("\n--- [Test Setup] Mini-App Funnel QA Script 시작 ---")
25	        # Mock API 서비스 인스턴스를 생성하여 모든 테스트에서 사용 가능하게 만듭니다.
26	        self.mock_api = MockAPIService()
27	
28	    def test_001_normal_data_submission(self):
29	        """SCN-001: 정상 데이터 제출 흐름 검증."""
30	        print("\n[TEST] SCN-001: 정상 흐름 테스트 (Success Path)")
31	        # Mock API를 통해 성공 케이스의 가짜 데이터를 주입합니다.
32	        mock_input = {"HOMA-IR": 5.2, "BMI": 28.1, "식습관 점수": 65}
33	        try:
34	            # 실제 Funnel 로직을 테스트하는 함수를 호출 (실제로는 test_funnel_flow 내부 모듈 사용)
35	            result = test_funnel_flow(input_data=mock_input, failure_mode=None)
36	            self.assertIn("분석 시작 메시지", result["status"])
37	            print("✅ SCN-001: 성공적인 분석 흐름을 확인했습니다.")
38	        except Exception as e:
39	            self.fail(f"SCN-001 테스트 실패: 예상치 못한 오류 발생 - {e}")
40	
41	    def test_002_critical_threshold_error(self):
42	        """SCN-002: 임계치 경고(Deep Crimson Red) 및 에러 처리 검증."""
43	        print("\n[TEST] SCN-002: 심각 임계치 오류 주입 테스트 (E-02)")
44	        # Mock API를 통해 고의적으로 위험한 데이터를 주입합니다.
45	        mock_input = {"HOMA-IR": 9.8, "BMI": 35.0, "식습관 점수": 12}
46	        try:
47	            # Funnel 로직이 임계치를 감지하고 Deep Crimson Red 경고를 출력하는지 확인합니다.
48	            result = test_funnel_flow(input_data=mock_input, failure_mode="THRESHOLD")
49	            self.assertIn("Deep Crimson Red 경고 UI", result["warning"])
50	            print("✅ SCN-002: 임계치 초과 감지 및 Deep Crimson Red 경고 처리를 확인했습니다.")
51	        except Exception as e:
52	            self.fail(f"SCN-002 테스트 실패: 예상치 못한 오류 발생 - {e}")
53	
54	    def test_003_missing_field_validation(self):
55	        """SCN-001의 확장: 필수 필드 누락 검증 (E-01)."""
56	        print("\n[TEST] SCN-003: 필수 필드 누락 테스트 (E-01)")
57	        # HOMA-IR 데이터가 없는 상태로 제출합니다.
58	        mock_input = {"BMI": 25.0, "식습관 점수": 80}
59	        try:
60	            result = test_funnel_flow(input_data=mock_input, failure_mode="MISSING_FIELD")
61	            self.assertIn("필수 필드 누락", result["error"])
62	            print("✅ SCN-003: 필수 필드 미입력에 대한 적절한 에러 메시지 표시를 확인했습니다.")
63	        except Exception as e:
64	            self.fail(f"SCN-003 테스트 실패: 예상치 못한 오류 발생 - {e}")
65	
66	    def test_004_network_failure_simulation(self):
67	        """네트워크 연결 끊김 시뮬레이션 (가장 중요한 리질리언스 검증)."""
68	        print("\n[TEST] SCN-004: 네트워크 실패 시뮬레이션 테스트")
69	        # Mock API를 사용하여 강제로 네트워크 오류를 발생시킵니다.
70	        try:
71	            test_funnel_flow(input_data={}, failure_mode="NETWORK_FAIL")
72	            self.fail("네트워크 실패 상황에서 예외가 발생하지 않았습니다.") # 에러가 나야 성공!
73	        except ConnectionError as e:
74	            # Funnel이 네트워크 오류를 잡고 사용자에게 친절하게 복구 안내(Fallback)하는지 확인합니다.
75	            if "네트워크 연결을 다시 시도해 주세요" in str(e):
76	                print("✅ SCN-004: 네트워크 실패 시 적절한 폴백 로직과 사용자 가이드를 성공적으로 제공했습니다.")
77	            else:
78	                 self.fail(f"SCN-004 테스트 실패: 예상된 오류 메시지가 아닙니다 - {str(e)}")
79	
80	
81	if __name__ == '__main__':
82	    # unittest.main() 대신 커스텀 실행 로직을 사용합니다.
83	    print("=============================================")
84	    print("🧪 Funnel E2E QA 스크립트가 준비되었습니다.")
85	    print("실행할 테스트 케이스: 4가지 (정상, 임계치 오류, 필드 누락, 네트워크 실패)")
86	    print("=============================================")
87	
88	# 주석 처리된 이 코드는 실제 실행 시 unittest 프레임워크를 사용합니다.
89	# unittest.main(argv=['first-arg-is-ignored'], exit=False)
```
