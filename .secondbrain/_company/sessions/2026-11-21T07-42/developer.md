# 💻 코다리 — 최우선 순위 과제: API 클라이언트 객체 초기화 누락(Dependency Injection Failure) 문제를 해결하는 데 집중합니다. 'content_orchestrator' 상위 레벨에서 모든 개별 외부 서비스 API 클라이언트의 생성 및 초기화 로직을 분리하고 재설계하여, 어떤 콘텐츠 유형이든 안정적으로 호출될 수 있는 구조를 확립해주세요. 또한, MockAPIService를 활용하여 실제 환경과 유사한 '클라이언트 초기화 실패' 및 '외부 서비스 장애' 상황을 시뮬레이션하는 통합 테스트 케이스 5개 이상을 작성하고 코드를 업데이트하세요.

💻 코다리: 작업 시작합니다.

CEO의 지시사항을 확인했습니다. API 클라이언트 객체 초기화 누락(Dependency Injection Failure) 문제는 시스템 안정성 측면에서 치명적인 결함입니다. 아무리 복잡한 비즈니스 로직도 외부 서비스에 대한 호출이 불안정하면 의미가 없습니다. ⚙️

요청하신 내용을 요약하면 다음과 같습니다:
1.  **아키텍처 개선:** `content_orchestrator` 레벨에서 모든 개별 API 클라이언트의 생성 및 초기화 로직을 분리/재설계하여, 콘텐츠 유형과 관계없이 안정적인 호출 구조를 확립합니다. (DI 패턴 적용)
2.  **테스트 강화:** `MockAPIService`를 활용해 '클라이언트 초기화 실패'와 '외부 서비스 장애' 상황을 시뮬레이션하는 통합 테스트 케이스 5개 이상을 작성하고 반영합니다.

이 작업은 핵심 시스템 아키텍처 수정 및 테스트 코드 작성을 포함하므로, 기존 코드를 먼저 파악한 후 진행하겠습니다.

### 🛠️ 1단계: 현황 분석 (Read & Diagnose)
먼저 `content_orchestrator`와 `MockAPIService`의 현재 구조를 확인하여 어느 부분에서 객체 초기화가 누락되었는지 진단해야 합니다.

<read_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\content_orchestrator.py"/>
<read_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\MockAPIService.py"/>

### 🧠 2단계: 계획 수립 (Refactoring & Testing)
**[아키텍처 개선 방안]**
`content_orchestrator.py` 내부에 **Service Client Factory** 패턴을 도입하겠습니다. 모든 외부 서비스 클라이언트(예: `api_client_A`, `api_client_B`)의 인스턴스는 이제 Orchestrator 클래스의 초기화 단계(`__init__`)에서 중앙 집중식으로 생성되어야 합니다. 이를 통해 의존성 주입(DI)을 명시적으로 관리하고, 실패 시에도 로깅 및 폴백 처리를 할 수 있게 됩니다.

**[테스트 강화 방안]**
`content_master_tester.py` 또는 별도의 통합 테스트 스크립트를 수정하여, `MockAPIService`가 다음과 같은 5가지 이상의 시나리오를 주입할 수 있는지 검증하겠습니다:
1.  Client A 초기화 실패 (Exception 발생)
2.  Client B 호출 중 네트워크 타임아웃 발생
3.  외부 API 서버에서 500 Internal Server Error 반환
4.  필수 입력 파라미터 누락으로 인한 유효성 검사 실패
5.  Rate Limit 초과로 인한 접근 거부 (HTTP 429)

이 작업은 시스템의 핵심 기능을 건드리는 것이므로, 변경 사항을 커밋하기 전에 반드시 `test_e2e_data_pipeline.py`와 통합하여 테스트를 진행하겠습니다.

---
*(잠시 후, 파일 내용과 진단 결과를 바탕으로 코드를 수정 및 작성할 예정입니다.)*

📊 평가: 진행중 — 핵심 아키텍처 refactoring이 필요하며, 기존 코드 분석 및 새로운 테스트 케이스 작성이 선행되어야 합니다.
📝 다음 단계: `content_orchestrator`와 `MockAPIService`의 내용을 바탕으로 Factory 패턴을 적용한 리팩토링된 코드를 작성하고, 이를 검증할 통합 테스트 스크립트를 업데이트하겠습니다.

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\content_orchestrator.py (197줄, 8.9KB)
```
 1	import time
 2	import random
 3	from typing import Callable, Any, Dict, List
 4	
 5	# ==============================================================
 6	# 🛡️ Core Resilience Module (Circuit Breaker & Exponential Backoff)
 7	# 이 클래스는 모든 외부 API 호출의 안정성을 담당하는 백본입니다.
 8	# ==============================================================
 9	
10	class ResilientAPIClient:
...
```
📖 읽기: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\MockAPIService.py (97줄, 4.1KB)
```
 1	import random
 2	from datetime import datetime
 3	# NameResolutionError는 실제 네트워크 라이브러리에서 발생하지만, 여기서는 시뮬레이션을 위해 임포트합니다.
 4	class NameResolutionError(Exception):
 5	    """DNS Resolution Failure Simulation."""
 6	    pass
 7	
 8	def run_scan_diagnosis(user_id: str, metrics: list) -> dict:
 9	    """
10	    /diagnosis/run_scan 엔드포인트 모킹. 
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\content_orchestrator.py (197줄)
```
  1	import time
  2	import random
  3	from typing import Callable, Any, Dict, List
  4	
  5	# ==============================================================
  6	# 🛡️ Core Resilience Module (Circuit Breaker & Exponential Backoff)
  7	# 이 클래스는 모든 외부 API 호출의 안정성을 담당하는 백본입니다.
  8	# ==============================================================
  9	
 10	class ResilientAPIClient:
 11	    """
 12	    외부 서비스와의 통신 실패에 대응하기 위한 중앙 집중식 클라이언트.
 13	    Circuit Breaker와 지수 백오프 로직을 통합합니다.
 14	    """
 15	    def __init__(self, service_name: str):
 16	        self.service_name = service_name
 17	        # Circuit Breaker 상태: 'CLOSED', 'OPEN', 'HALF-OPEN'
 18	        self._circuit_state = "CLOSED" 
 19	        self.failure_count = 0
 20	        self.last_failure_time = time.time()
 21	
 22	    def _open_circuit(self):
 23	        """Circuit Breaker를 OPEN 상태로 전환합니다."""
 24	        print(f"\n[🚨 CIRCUIT BREAKER] {self.service_name} 서비스 장애 감지. 회로를 열고 {self.service_name} 호출을 차단합니다.")
 25	        self._circuit_state = "OPEN"
 26	        # 재시도 가능 시간을 30초로 설정 (실제는 더 복잡한 로직 필요)
 27	        self.last_failure_time = time.time() + 30
 28	
 29	    def _check_circuit(self):
 30	        """Circuit Breaker 상태를 검사하고, 필요한 경우 HALF-OPEN으로 전환 시도합니다."""
 31	        if self._circuit_state == "OPEN":
 32	            elapsed = time.time() - self.last_failure_time
 33	            if elapsed >= 30: # 시간 경과 체크 (예시 값)
 34	                print(f"[♻️ CIRCUIT BREAKER] {self.service_name} 회복 시도 감지. HALF-OPEN 상태로 전환합니다.")
 35	                self._circuit_state = "HALF-OPEN"
 36	            else:
 37	                raise ConnectionError(f"{self.service_name} 서비스가 현재 다운되어 호출을 거부합니다 (Open).")
 38	
 39	    def execute(self, api_call: Callable[..., Any], *args, max_attempts: int = 5, **kwargs) -> Any:
 40	        """
 41	        실제 API 호출을 감싸는 메인 실행 함수. 
 42	        재시도 로직과 Circuit Breaker를 모두 적용합니다.
 43	        """
 44	        attempt = 0
 45	        while attempt < max_attempts:
 46	            try:
 47	                self._check_circuit() # 1. 회로 상태 체크
 48	
 49	                # 실제 API 호출 시도
 50	                result = api_call(*args, **kwargs) 
 51	                
 52	                # 성공 시 로직 리셋 및 결과 반환
 53	                self.failure_count = 0
 54	                self._circuit_state = "CLOSED"
 55	                return result
 56	
 57	            except (ConnectionError, TimeoutError, Exception) as e:
 58	                attempt += 1
 59	                print(f"[⚠️ API 실패] {self.service_name} 호출 시도 {attempt}/{max_attempts}: {e}")
 60	                
 61	                if self._circuit_state == "HALF-OPEN" and attempt >= 3:
 62	                    # HALF-OPEN에서 연속 실패 -> 즉시 OPEN으로 전환하여 시스템 보호
 63	                    self._open_circuit()
 64	                    raise ConnectionError(f"{self.service_name} 호출 시도 중 재차 장애 발생. 서비스 차단.")
 65	
 66	                if attempt < max_attempts:
 67	                    # 지수 백오프 계산 (2^attempt 초 대기)
 68	                    wait_time = 2 ** attempt + random.uniform(-1, 1) # 랜덤 노이즈 추가
 69	                    print(f"   -> 재시도합니다. {wait_time:.2f}초 대기...")
 70	                    time.sleep(wait_time)
 71	                else:
 72	                    # 모든 시도가 실패했을 경우
 73	                    self._open_circuit()
 74	                    raise ConnectionError(f"{self.service_name}: 최대 재시도 횟수 초과. 서비스 이용 불가.")
 75	
 76	        return None
 77	
 78	
 79	# ==============================================================
 80	# 📺 Channel Specific Publishers (실제 API 호출을 시뮬레이션)
 81	# 실제로는 이 함수들 내부에서 requests 라이브러리를 사용합니다.
 82	# ==============================================================
 83	
 84	def publish_youtube(client: ResilientAPIClient, title: str, content: str):
 85	    """YouTube API를 통한 롱폼 영상 발행 시뮬레이션."""
 86	    print("\n[▶️ YOUTUBE] 롱폼 콘텐츠 발행을 시도합니다...")
 87	    
 88	    # 가상 실패 로직: 무작위로 30% 확률로 ConnectionError 발생
 89	    if random.random() < 0.3 and client._circuit_state == "CLOSED":
 90	        raise ConnectionError("YouTube API Rate Limit Exceeded (429).")
 91	    
 92	    # 실제 호출 성공 시 리턴값 가정
 93	    return f"✅ YOUTUBE 발행 성공: '{title}' - 영상 ID XYZ123."
 94	
 95	def publish_blog(client: ResilientAPIClient, article_html: str):
 96	    """블로그 CMS API를 통한 아티클 발행 시뮬레이션."""
 97	    print("[✍️ BLOG] 블로그 플랫폼에 HTML 콘텐츠를 게시합니다...")
 98	    
 99	    # 가상 실패 로직: 무작위로 20% 확률로 TimeoutError 발생
100	    if random.random() < 0.2 and client._circuit_state == "CLOSED":
101	        raise TimeoutError("Blog CMS Connection Timeout.")
102	
103	    return f"✅ BLOG 발행 성공: 아티클 내용 길이 {len(article_html)}자로 게시 완료."
104	
105	
106	def publish_instagram(client: ResilientAPIClient, media_url: str, caption: str):
107	    """Instagram Graph API를 통한 숏폼/캐러셀 업로드 시뮬레이션."""
108	    print("[📸 INSTAGRAM] 숏폼 미디어와 캡션을 게시합니다...")
109	
110	    # 가상 실패 로직: 무작위로 40% 확률로 ConnectionError 발생
111	    if random.random() < 0.4 and client._circuit_state == "CLOSED":
112	        raise ConnectionError("Instagram API Authentication Failed (401).")
113	
114	    return f"✅ INSTAGRAM 발행 성공: 미디어 {media_url} 업로드 완료."
115	
116	
117	# ==============================================================
118	# 🚀 Main Orchestrator Logic
119	# 모든 채널의 배포를 통제하고 결과 로깅을 수행합니다.
120	# ==============================================================
121	
122	def run_full_content_orchestration(youtube_content, blog_content, insta_content):
123	    """
124	    전체 콘텐츠 패키지를 받아 각 채널별로 안정적인 발행을 시도하는 메인 함수.
125	    """
126	    print("=========================================================")
127	    print("🌟 [오케스트레이터 시작] 통합 콘텐츠 배포 파이프라인 가동 🌟")
128	    print("=========================================================")
129	
130	    # 각 채널별 클라이언트 인스턴스 생성 (독립적인 상태 관리)
131	    youtube_client = ResilientAPIClient(service_name="YouTube")
132	    blog_client = ResilientAPIClient(service_name="BlogCMS")
133	    insta_client = ResilientAPIClient(service_name="Instagram")
134	
135	    results: List[str] = []
136	
137	    # 1. YouTube 발행 시도 (가장 중요한 롱폼)
138	    try:
139	        youtube_result = youtube_client.execute(
140	            publish_youtube, 
141	            title=youtube_content['title'], 
142	            content=youtube_content['script']
143	        )
144	        results.append(youtube_result)
145	    except ConnectionError as e:
146	        results.append(f"❌ [FATAL ERROR] YouTube 발행 실패: {e}")
147	
148	    # 2. Blog 발행 시도 (검색 유입 트래픽 확보)
149	    try:
150	        blog_result = blog_client.execute(
151	            publish_blog, 
152	            article_html=blog_content['html']
153	        )
154	        results.append(blog_result)
155	    except ConnectionError as e:
156	        results.append(f"❌ [FATAL ERROR] Blog 발행 실패: {e}")
157	
158	    # 3. Instagram 발행 시도 (빠른 트래픽 유입 및 노출)
159	    try:
160	        insta_result = insta_client.execute(
161	            publish_instagram, 
162	            media_url=insta_content['media'], 
163	            caption=insta_content['caption']
164	        )
165	        results.append(insta_result)
166	    except ConnectionError as e:
167	        results.append(f"❌ [FATAL ERROR] Instagram 발행 실패: {e}")
168	
169	    print("\n=========================================================")
170	    print("✅ 배포 파이프라인 최종 검증 완료.")
171	    for result in results:
172	        print(result)
173	    return results
174	
175	# ==============================================================
176	# 🧪 Test Data and Execution Block (실제 실행 예시)
177	# 이 블록을 통해 스크립트의 동작 원리를 확인합니다.
178	# ==============================================================
179	
180	if __name__ == "__main__":
181	    print("--- 시스템 테스트 데이터 로드 ---")
182	    YOUTUBE_DATA = {
183	        'title': '국민연금 사각지대, 놓치면 손해 보는 3가지 구조적 위험',
184	        'script': "...", # 실제 스크립트 내용
185	    }
186	    BLOG_DATA = {
187	        'html': "<article><h1>국민연금 리스크 진단</h1><p>...</p></article>",
188	    }
189	    INSTA_DATA = {
190	        'media': "https://example.com/reel_asset.mp4", 
191	        'caption': "#노후준비 #재테크꿀팁"
192	    }
193	
194	    print("\n--- 오케스트레이터 실행 시작 (실패 시도 유발) ---")
195	    run_full_content_orchestration(YOUTUBE_DATA, BLOG_DATA, INSTA_DATA)
196	    print("=========================================================")
197	    print("🔥 테스트 완료. Circuit Breaker 및 Exponential Backoff 로직이 정상적으로 동작했습니다.")
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\MockAPIService.py (97줄)
```
 1	import random
 2	from datetime import datetime
 3	# NameResolutionError는 실제 네트워크 라이브러리에서 발생하지만, 여기서는 시뮬레이션을 위해 임포트합니다.
 4	class NameResolutionError(Exception):
 5	    """DNS Resolution Failure Simulation."""
 6	    pass
 7	
 8	def run_scan_diagnosis(user_id: str, metrics: list) -> dict:
 9	    """
10	    /diagnosis/run_scan 엔드포인트 모킹. 
11	    핵심 진단 로직의 실패 및 폴백 테스트를 담당합니다.
12	    """
13	    print(f"--- [MockAPI] Running diagnosis scan for User ID: {user_id} ---")
14	
15	    # 1. NameResolutionError 강제 시뮬레이션 (네트워크 인프라 문제)
16	    if random.random() < 0.2: # 20% 확률로 네트워크 오류 발생 가정
17	        print("[⚠️ MOCK ERROR] Simulated Name Resolution Failure.")
18	        raise NameResolutionError("Failed to resolve host name for diagnosis service endpoint.")
19	
20	    # 2. 데이터 유효성 검사 (400 Bad Request Simulation)
21	    if not metrics or any(m['metric_name'] == 'HOMA-IR' and m['value'] is None for m in metrics):
22	        return {
23	            "status": "ERROR",
24	            "code": "INVALID_INPUT",
25	            "message": "진단에 필수적인 생체지표 데이터가 누락되었거나 유효하지 않습니다."
26	        }
27	
28	    # 3. 정상 로직 (Soft Gold 해결책 제시)
29	    total_score = sum(m['value'] for m in metrics if m['metric_name'] == 'HOMA-IR') / len(metrics) * 10
30	    
31	    if total_score > 80:
32	        recommendation = "매우 양호한 상태입니다. 생활 습관을 유지해 주세요."
33	        status = "SUCCESS"
34	    elif 60 <= total_score <= 80:
35	        recommendation = "생활 패턴 점검이 필요합니다. 식이요법 개선에 집중하세요."
36	        status = "SUCCESS"
37	    else: # Critical Warning Zone (Deep Crimson Red Trigger)
38	        recommendation = "🚨 임계점 위험! 전문적인 검진과 생활 변화가 시급합니다. MiniFunnel을 통해 추가 점검이 필요합니다."
39	        status = "WARNING"
40	
41	    return {
42	        "status": status,
43	        "diagnosis_score": round(total_score, 1),
44	        "recommendation": recommendation
45	    }
46	
47	
48	def get_user_profile_status(user_id: str) -> dict:
49	    """
50	    /user/profile/{user_id}/status 엔드포인트 모킹.
51	    사용자 존재 여부 및 서비스 가용성 폴백 테스트를 담당합니다.
52	    """
53	    print(f"--- [MockAPI] Checking user profile status for User ID: {user_id} ---")
54	
55	    # 1. 사용자 부재 시뮬레이션 (404 Not Found Simulation)
56	    if user_id == "nonexistent_user":
57	        return {
58	            "status": "NOT_FOUND",
59	            "error_code": "USER_MISSING",
60	            "message": f"ID '{user_id}'에 해당하는 사용자 데이터를 찾을 수 없습니다. 계정 확인이 필요합니다."
61	        }
62	
63	    # 2. 서비스 가용성 저하 시뮬레이션 (503 Service Unavailable)
64	    if random.random() < 0.1: # 10% 확률로 서버 다운 가정
65	        return {
66	            "status": "SERVICE_UNAVAILABLE",
67	            "error_code": "SERVER_OVERLOAD",
68	            "fallback_action": "현재 시스템 과부하 상태입니다. 잠시 후 다시 시도해 주십시오. (재시도 로직 필수)"
69	        }
70	
71	    # 3. 정상 조회
72	    return {
73	        "status": "OK",
74	        "is_active": True,
75	        "last_check": datetime.now().isoformat() + 'Z'
76	    }
77	
78	if __name__ == '__main__':
79	    print("============================================")
80	    print("✅ Mock API Service Initialized: Testing Resilience")
81	    print("============================================")
82	    
83	    # 1. NameResolutionError 테스트 시뮬레이션
84	    try:
85	        run_scan_diagnosis("userA", [{"metric_name": "HOMA-IR", "value": 5.0}])
86	    except NameResolutionError as e:
87	        print(f"\n[SUCCESS] Handled Expected Error: {e}")
88	    except Exception as e:
89	        print(f"[FAILURE] Caught unexpected error type: {type(e)}")
90	
91	    # 2. Invalid Input 테스트 시뮬레이션
92	    result_400 = run_scan_diagnosis("userB", [])
93	    print(f"\n[TEST RESULT 400]: {result_400}")
94	
95	    # 3. Service Unavailable (Fallback) 테스트 시뮬레이션
96	    # 이 부분은 랜덤이므로 여러 번 실행해야 합니다.
97	    get_user_profile_status("test_user")
```
