# 💻 코다리 — 현재 콘텐츠를 게재하는 모든 오케스트레이터(YouTube, Instagram 등)의 API 호출 로직을 전면 재검토하고, 필수 객체(`client`) 누락 오류가 발생하지 않도록 초기화 및 연결 테스트 코드를 수정해주세요. 특히, 배포 과정에서 발생하는 인증 만료 및 네트워크 불안정 상황에 대응할 수 있는 자동 재연결(Retry) 및 롤백 로직을 'resilience_publisher_tester' 모듈에 구현하여 안정적인 End-to-End 배포 환경을 구축하는 것이 최우선 과제입니다.

💻 코다리: 작업 시작합니다.

CEO 지시사항 분석 결과, 현재 우리 전체 콘텐츠 배포 파이프라인의 가장 치명적인 병목(Bottleneck)은 **'시스템 안정성 부재'**입니다. 여러 플랫폼에 걸쳐 API 호출 로직을 사용할 때 `client` 객체 초기화 누락 오류가 발생한다는 건, 단순한 버그를 넘어 서비스 중단으로 직결되는 심각한 구조적 결함이에요. 🐛

이건 그냥 코드 한두 줄 고치는 수준이 아니에요. **배포 자체가 믿음직하지 못하다는 뜻**입니다. 따라서 지시하신 대로 `resilience_publisher_tester` 모듈을 중심으로 전면적인 아키텍처 개선 작업을 진행하겠습니다. 목표는 '단순 실행'에서 '자가 복구(Self-Healing)' 수준의 배포 환경으로 격상시키는 겁니다.

### 🛠️ 작업 계획 (Plan)
1.  **현황 파악**: `resilience_publisher_tester` 모듈을 읽어 현재 로직 구조와 취약점을 분석합니다.
2.  **코드 개선**: 자동 재연결(Retry), 인증 만료 대응, 그리고 핵심적인 롤백 메커니즘을 추가하여 안정성을 극대화합니다. (특히 `client` 객체 초기화를 최우선으로 처리).
3.  **테스트 및 검증**: 수정된 모듈을 실제 시뮬레이션 환경에서 실행하여, 오류 조건(네트워크 끊김, API Rate Limit 초과 등)에서도 정상적으로 복구되는지 검증합니다.

---

### 🔍 Step 1: `resilience_publisher_tester` 현황 파악

먼저 현재의 테스트 모듈을 읽어봐야 어떤 로직 위에서 고쳐나갈지 감이 잡힙니다.

<read_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\resilience_publisher_tester.py"/>


---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\resilience_publisher_tester.py (186줄, 9.2KB)
```
 1	import time
 2	import random
 3	from functools import wraps
 4	from typing import Callable, Any, Dict, List
 5	
 6	# ====================================================
 7	# 🛠️ 1. Resilience Patterns Implementation
 8	# ====================================================
 9	
10	class CircuitBreaker:
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\resilience_publisher_tester.py (186줄)
```
  1	import time
  2	import random
  3	from functools import wraps
  4	from typing import Callable, Any, Dict, List
  5	
  6	# ====================================================
  7	# 🛠️ 1. Resilience Patterns Implementation
  8	# ====================================================
  9	
 10	class CircuitBreaker:
 11	    """
 12	    서킷 브레이커 패턴 구현. 시스템 과부하 또는 지속적 실패 시 API 호출을 차단하여 자원을 보호합니다.
 13	    상태: CLOSED (정상), OPEN (차단), HALF-OPEN (테스트)
 14	    """
 15	    def __init__(self, failure_threshold: int = 3, recovery_timeout: int = 10):
 16	        self.failure_threshold = failure_threshold # 실패 임계치
 17	        self.recovery_timeout = recovery_timeout   # 재시도 대기 시간 (초)
 18	        self.state = "CLOSED"                       # 현재 상태
 19	        self.fail_count = 0                         # 연속 실패 카운트
 20	        self.last_failure_time = time.time()       # 마지막 실패 시간
 21	
 22	    def __call__(self, func: Callable) -> Callable:
 23	        @wraps(func)
 24	        def wrapper(*args, **kwargs):
 25	            if self.state == "OPEN":
 26	                elapsed = time.time() - self.last_failure_time
 27	                if elapsed > self.recovery_timeout:
 28	                    print("🔌 [CircuitBreaker] Timeout 만료 -> HALF-OPEN 상태로 전환하여 테스트 시도.")
 29	                    self.state = "HALF-OPEN"
 30	                else:
 31	                    raise ConnectionError(f"🔴 Circuit Breaker Open. {int(self.recovery_timeout - elapsed)}초 후에 재시도하세요.")
 32	
 33	            try:
 34	                result = func(*args, **kwargs)
 35	                if self.state in ["OPEN", "HALF-OPEN"]:
 36	                    print("✅ [CircuitBreaker] 성공 감지 -> CLOSED 상태로 복구 완료.")
 37	                    self.state = "CLOSED"
 38	                    self.fail_count = 0
 39	                return result
 40	            except Exception as e:
 41	                self.fail_count += 1
 42	                if self.state == "HALF-OPEN":
 43	                     # HALF-OPEN에서 실패하면 다시 OPEN으로 전환
 44	                    print(f"❌ [CircuitBreaker] 테스트 실패 -> OPEN 상태로 재진입.")
 45	                    self.state = "OPEN"
 46	                    self.last_failure_time = time.time()
 47	                elif self.fail_count >= self.failure_threshold:
 48	                    # 임계치 초과 시 OPEN으로 전환
 49	                    print(f"💥 [CircuitBreaker] 실패 임계치 ({self.failure_threshold}회) 도달 -> OPEN 상태 진입.")
 50	                    self.state = "OPEN"
 51	                    self.last_failure_time = time.time()
 52	                raise e
 53	
 54	        return wrapper
 55	
 56	def retry_with_backoff(max_retries: int = 5, initial_delay: float = 1.0):
 57	    """
 58	    지수 백오프 재시도 로직 데코레이터. (Exponential Backoff)
 59	    시간 간격: delay * 2^attempt
 60	    """
 61	    def decorator(func: Callable) -> Callable:
 62	        @wraps(func)
 63	        def wrapper(*args, **kwargs):
 64	            delay = initial_delay
 65	            for attempt in range(max_retries):
 66	                try:
 67	                    return func(*args, **kwargs) # API 호출 시도
 68	                except ConnectionError as e:
 69	                    if attempt == max_retries - 1:
 70	                        print(f"🚨 [Retry] 최대 재시도 횟수({max_retries}회) 초과. 최종 실패합니다.")
 71	                        raise e
 72	                    
 73	                    # 지연 시간 계산 (지수 백오프)
 74	                    sleep_time = delay * (2 ** attempt) + random.uniform(0, 1)
 75	                    print(f"⚠️ [Retry] API 호출 실패 ({e}). {int(sleep_time)}초 후 재시도합니다... (Attempt {attempt + 1}/{max_retries})")
 76	                    time.sleep(sleep_time) # 대기
 77	                except Exception as e:
 78	                    # 예상치 못한 다른 에러는 즉시 전파
 79	                    print(f"🛑 [Retry] 처리 불가능한 에러 발생: {e}")
 80	                    raise e
 81	            return None
 82	        return wrapper
 83	    return decorator
 84	
 85	# ====================================================
 86	# 🌐 2. Platform Publishing API Simulation (Mock)
 87	# ====================================================
 88	
 89	def publish_youtube(content_package: Dict[str, Any]) -> str:
 90	    """유튜브 플랫폼 발행 시뮬레이션 (API 호출 가정). 실패율이 높게 설정."""
 91	    print("\n--- 📺 유튜브 발행 시도 ---")
 92	    if random.random() < 0.3: # 30% 확률로 일시적 오류 발생 시뮬레이션
 93	        raise ConnectionError("YouTube API Rate Limit Exceeded or Temporary Server Error.")
 94	    return "SUCCESS"
 95	
 96	def publish_instagram(content_package: Dict[str, Any]) -> str:
 97	    """인스타그램 플랫폼 발행 시뮬레이션 (API 호출 가정). 실패율이 중간 수준."""
 98	    print("\n--- 📸 인스타그램 발행 시도 ---")
 99	    if random.random() < 0.25: # 25% 확률로 일시적 오류 발생 시뮬레이션
100	        raise ConnectionError("Instagram Graph API Error: Invalid Media Format.")
101	    return "SUCCESS"
102	
103	def publish_naver_blog(content_package: Dict[str, Any]) -> str:
104	    """네이버 블로그 플랫폼 발행 시뮬레이션 (API 호출 가정). 실패율이 낮음."""
105	    print("\n--- 📰 네이버 블로그 발행 시도 ---")
106	    if random.random() < 0.15: # 15% 확률로 일시적 오류 발생 시뮬레이션
107	        raise ConnectionError("Naver Blog API Error: Authentication Failed.")
108	    return "SUCCESS"
109	
110	def publish_youtube_shorts(content_package: Dict[str, Any]) -> str:
111	    """유튜브 쇼츠/클립 플랫폼 발행 시뮬레이션 (API 호출 가정). 실패율이 높음."""
112	    print("\n--- 🎬 유튜브 쇼츠/클립 발행 시도 ---")
113	    if random.random() < 0.35: # 35% 확률로 가장 높은 오류 발생률 설정
114	        raise ConnectionError("YouTube Shorts API Overload or Geo-Restriction Error.")
115	    return "SUCCESS"
116	
117	# ====================================================
118	# 🧪 3. Orchestrator & Execution Logic
119	# ====================================================
120	
121	@CircuitBreaker(failure_threshold=2, recovery_timeout=15)
122	@retry_with_backoff(max_retries=4, initial_delay=0.5)
123	def publish_content_package(platform: str, package: Dict[str, Any]) -> str:
124	    """지수 백오프와 서킷 브레이커가 적용된 핵심 발행 로직."""
125	    if platform == "YouTube":
126	        result = publish_youtube(package)
127	    elif platform == "Instagram":
128	        result = publish_instagram(package)
129	    elif platform == "NaverBlog":
130	        result = publish_naver_blog(package)
131	    elif platform == "Shorts":
132	        result = publish_youtube_shorts(package)
133	    else:
134	        raise ValueError("Unknown Platform")
135	    return result
136	
137	def run_e2e_publishing_simulation(content_package: Dict[str, Any]) -> Dict[str, str]:
138	    """4대 플랫폼에 대한 E2E 통합 테스트를 실행하고 결과를 수집합니다."""
139	    platforms = ["YouTube", "Instagram", "NaverBlog", "Shorts"]
140	    results = {}
141	
142	    print("=============================================================")
143	    print("🚀 숏폼 콘텐츠 대량 발행 시뮬레이션 시작 (Resilience Test)")
144	    print(f"📅 대상 콘텐츠: {content_package.get('title', '미정')} ({content_package['script'][:20]}...)")
145	    print("=============================================================")
146	
147	    for platform in platforms:
148	        try:
149	            # 핵심 함수 호출 (여기서 CB와 Backoff가 자동으로 작동함)
150	            status = publish_content_package(platform, content_package)
151	            results[platform] = f"✅ 성공적으로 발행됨. ({status})"
152	        except ConnectionError as e:
153	            results[platform] = f"❌ 실패 (API 오류/속도 제한): {e}"
154	        except Exception as e:
155	            results[platform] = f"🛑 치명적 오류 발생: {type(e).__name__} - {str(e)}"
156	
157	    return results
158	
159	
160	if __name__ == "__main__":
161	    # 가상의 최종 콘텐츠 패키지 데이터 (Writer가 제공한 것을 기반으로 구성)
162	    simulated_content_package = {
163	        "title": "5060 디지털 소득 공백 리스크 진단",
164	        "script": "AI가 대체하는 3가지 직무...",
165	        "keywords": ["중장년 재취업", "디지털 격차"],
166	        "cta": "전문가진단가이드.zip 다운로드"
167	    }
168	
169	    # 시뮬레이션 실행 및 결과 수집
170	    final_results = run_e2e_publishing_simulation(simulated_content_package)
171	
172	    # 테스트 보고서 출력
173	    print("\n\n=============================================================")
174	    print("📊 E2E 통합 발행 시스템 테스트 완료 보고서")
175	    print("-------------------------------------------------------------")
176	    for platform, result in final_results.items():
177	        print(f"[{platform}]: {result}")
178	    print("=============================================================\n")
179	
180	    # 최종 검증: 모든 플랫폼이 성공적으로 실행될 때만 '완료' 처리 가능함을 명시
181	    success_count = sum(1 for res in final_results.values() if "성공" in res)
182	    total_platforms = len(final_results)
183	    if success_count == total_platforms:
184	        print("✨ 시스템 검증 결과: 모든 플랫폼에 대한 발행 기능 테스트가 성공적으로 완료되었습니다.")
185	    else:
186	        print("⚠️ 시스템 검증 경고: 일부 플랫폼에서 오류가 발생했습니다. 이는 정상적인 부하/실패 시뮬레이션 과정일 수 있습니다.")
```
