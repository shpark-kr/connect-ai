# 💻 코다리 — Researcher가 제공한 새로운 정량적 건강 리스크 데이터를 기반으로, Mini-App의 핵심 로직(Mini-App Core Logic)을 업데이트해야 합니다. 이 데이터가 기존 위험도 측정 바(Risk Bar) 점수 계산에 어떻게 반영되어야 하는지, 그리고 해당 추가 항목이 유효성 검사(Validation)를 통과할 수 있도록 자바스크립트 기반의 '데이터 통합 스크립트 로직 명세서'와 함께 E2E 테스트 시나리오를 작성하십시오.

💻 코다리: 작업 시작합니다.
이거 그냥 데이터 넣는 게 아니잖아요? 단순히 항목 추가하는 걸로 끝나면 안 돼요. 이 새로운 정량적 지표들(SRI, HRV-proxy, SCFA Score)이 기존의 위험도 측정 바에 어떻게 유기적으로 녹아들어 가서, *사용자가 정말 '위험하다'*고 느끼게 만들지 로직을 짜야 합니다.

새로운 데이터 구조가 들어오면 가장 먼저 해야 할 건 **데이터 통합 스크립트 명세서**를 확정하고, 이 코드가 실제로 깨지지 않는지 **E2E 테스트 시나리오**를 만드는 겁니다.

현재 작업 대상 파일은 `c:\Data\Project\connect-ai\mini-app-funnel-mvp.html`입니다. 여기서 핵심 로직을 건드려야 하니, 먼저 이 파일을 읽어서 기존 스코어 계산 로직과 구조를 파악하겠습니다.

<read_file path="c:\Data\Project\connect-ai\mini-app-funnel-mvp.html"/>

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\mini-app-funnel-mvp.html (224줄, 12.2KB)
```
 1	<!DOCTYPE html>
 2	<html lang="ko" class="scroll-smooth">
 3	<head>
 4	    <meta charset="UTF-8">
 5	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
 6	    <title>온현 Mini-App Funnel MVP - 건강 점검</title>
 7	    <!-- Tailwind CSS CDN 사용 -->
 8	    <script src="https://cdn.tailwindcss.com"></script>
 9	    <style>
10	        /* 커스텀 색상 및 폰트 설정 (브랜드 톤 반영) */
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\mini-app-funnel-mvp.html (224줄)
```
  1	<!DOCTYPE html>
  2	<html lang="ko" class="scroll-smooth">
  3	<head>
  4	    <meta charset="UTF-8">
  5	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  6	    <title>온현 Mini-App Funnel MVP - 건강 점검</title>
  7	    <!-- Tailwind CSS CDN 사용 -->
  8	    <script src="https://cdn.tailwindcss.com"></script>
  9	    <style>
 10	        /* 커스텀 색상 및 폰트 설정 (브랜드 톤 반영) */
 11	        :root {
 12	            --primary-color: #3b82f6; /* Blue 500 - 신뢰감/권위 */
 13	            --success-color: #10b981; /* Emerald Green - 안전/안정 */
 14	            --warning-color: #f59e0b; /* Amber Yellow - 주의/경고 */
 15	            --danger-color: #ef4444; /* Red 500 - 위험/위기감 */
 16	        }
 17	
 18	        body {
 19	            font-family: 'Pretendard', sans-serif;
 20	            background-color: #f7fafc;
 21	        }
 22	
 23	        /* 커스텀 리스크 바 스타일링 (Designer Spec 반영) */
 24	        .risk-bar__container {
 25	            width: 100%;
 26	            max-width: 600px;
 27	            margin: 2rem auto;
 28	        }
 29	        .risk-bar__svg {
 30	            display: block;
 31	        }
 32	        .risk-bar__track {
 33	            fill: #e0e7ff; /* 배경색 */
 34	        }
 35	        /* JavaScript로 동적으로 색상과 너비가 변경됨 */
 36	
 37	        /* CTA 버튼 강조 */
 38	        .cta-button {
 39	            transition: all 0.3s ease;
 40	            box-shadow: 0 10px 20px rgba(59, 130, 246, 0.3);
 41	        }
 42	        .cta-button:hover {
 43	            transform: translateY(-2px);
 44	            box-shadow: 0 15px 25px rgba(59, 130, 246, 0.5);
 45	            background-color: #2563eb; /* Darker blue on hover */
 46	        }
 47	
 48	        /* 섹션 구분자를 위한 스타일링 */
 49	        section {
 50	            padding: 6rem 1rem;
 51	            border-bottom: 1px solid #e2e8f0;
 52	        }
 53	    </style>
 54	</head>
 55	<body>
 56	
 57	    <!-- 헤더 및 네비게이션 (Landing Kit 구조 반영) -->
 58	    <header class="bg-white shadow sticky top-0 z-50">
 59	        <div class="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
 60	            <h1 class="text-3xl font-extrabold text-gray-900">온현 <span class="text-blue-600">Mini-App</span></h1>
 61	            <nav>
 62	                <!-- CTA는 메인 Funnel로 통합 -->
 63	                <a href="#diagnosis-module" class="px-5 py-2 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition duration-300">
 64	                    나의 위험도 진단하기
 65	                </a>
 66	            </nav>
 67	        </div>
 68	    </header>
 69	
 70	    <main>
 71	        <!-- 🟢 Section 1: 문제 제기 (Problem Statement) -->
 72	        <section id="problem" class="bg-gradient-to-r from-blue-50 to-white">
 73	            <div class="max-w-4xl mx-auto text-center p-8">
 74	                <h2 class="text-base tracking-wider uppercase font-semibold text-red-600 mb-3">혹시, 몸의 경고 신호를 무시하고 계신가요?</h2>
 75	                <h1 class="text-5xl md:text-6xl font-extrabold text-gray-900 mb-6 leading-tight">
 76	                    나이 탓만 할 수 없습니다. <span class="text-blue-600">데이터</span>가 답을 알려줍니다.
 77	                </h1>
 78	                <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
 79	                    40대 이후, 만성적인 피로와 체중 증가를 '노화' 탓으로 돌리기 쉽습니다. 하지만 진짜 문제는 단순히 시간이 흐른 것이 아니라, 몸속의 <strong class="text-red-600">미세한 염증 수치</strong>나 <strong class="text-red-600">인슐린 민감성 저하</strong>와 같은 정량적 지표에 있습니다.
 80	                </p>
 81	            </div>
 82	        </section>
 83	
 84	        <!-- 🟡 Section 2: 위험도 진단 모듈 (Mini-App Core - Interactive) -->
 85	        <section id="diagnosis-module" class="bg-white">
 86	            <div class="max-w-5xl mx-auto text-center p-8">
 87	                <h2 class="text-4xl font-bold text-gray-900 mb-3">정확한 진단으로, 나의 몸 상태를 체크하세요.</h2>
 88	                <p class="text-lg text-gray-600 mb-12">
 89	                    아래 질문에 최대한 솔직하게 답해주시면, 현재 위험도 점수와 개선 포인트를 즉시 확인하실 수 있습니다. (가상 진단 모듈)
 90	                </p>
 91	
 92	                <!-- Mini-App 가상 체크리스트 -->
 93	                <div class="bg-gray-50 p-8 rounded-xl shadow-lg max-w-3xl mx-auto">
 94	                    <h3 class="text-2xl font-semibold mb-6 text-blue-700">🧬 나의 건강 습관 체크리스트</h3>
 95	
 96	                    <!-- 가상의 진단 질문들 -->
 97	                    <div id="quiz-form" class="space-y-4 text-left">
 98	                        <label class="flex items-center cursor-pointer bg-white p-3 rounded-lg shadow hover:shadow-md transition duration-150 border border-gray-200">
 99	                            <input type="checkbox" data-weight="5" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500">
100	                            <span class="ml-3 text-gray-700">최근 공복 혈당이 120mg/dL 이상으로 측정된 적이 있다.</span>
101	                        </label>
102	                        <label class="flex items-center cursor-pointer bg-white p-3 rounded-lg shadow hover:shadow-md transition duration-150 border border-gray-200">
103	                            <input type="checkbox" data-weight="8" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500">
104	                            <span class="ml-3 text-gray-700">아침에 일어나서 붓기가 심하고, 관절 통증이 느껴진다.</span>
105	                        </label>
106	                         <label class="flex items-center cursor-pointer bg-white p-3 rounded-lg shadow hover:shadow-md transition duration-150 border border-gray-200">
107	                            <input type="checkbox" data-weight="4" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500">
108	                            <span class="ml-3 text-gray-700">식사 후 2시간이 지나도 졸음이 오거나 집중력이 떨어진다.</span>
109	                        </label>
110	                         <label class="flex items-center cursor-pointer bg-white p-3 rounded-lg shadow hover:shadow-md transition duration-150 border border-gray-200">
111	                            <input type="checkbox" data-weight="7" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500">
112	                            <span class="ml-3 text-gray-700">식단 관리가 어렵고, 가공 탄수화물 섭취가 잦다.</span>
113	                        </label>
114	                    </div>
115	
116	                    <!-- 결과 표시 영역 -->
117	                    <div id="result-area" class="mt-12 p-6 bg-white rounded-xl shadow-2xl border-t-4 border-blue-500 transition duration-500 opacity-0 max-h-0 overflow-hidden">
118	                        <!-- 위험도 측정 바 (Designer Spec 반영) -->
119	                        <div class="risk-bar__container">
120	                            <svg class="risk-bar__svg" width="100%" height="30" viewBox="0 0 100 10" preserveAspectRatio="none">
121	                                <rect x="0" y="0" width="100%" height="10" fill="#e0e7ff" class="risk-bar__track"/>
122	                                <rect id="risk-score-fill" x="0" y="0" width="0%" height="10" fill="#cccccc" class="risk-bar__fill transition-all duration-1000 ease-out"/>
123	                            </svg>
124	                        </div>
125	                        <p class="text-xl font-bold text-gray-700 mt-4">당신의 현재 염증 위험도: <span id="score-display" class="text-3xl text-blue-600">0</span>점 (낮음)</p>
126	
127	                         <!-- 진단 결과 메시지 -->
128	                        <div id="diagnosis-message" class="mt-8 p-4 border-l-4 border-gray-300 bg-gray-50 hidden"></div>
129	                    </div>
130	                </div>
131	
132	
133	                <!-- CTA Button (Final Funnel Gate) -->
134	                <button id="run-test-btn" onclick="calculateRiskAndRunTest()" class="mt-12 px-16 py-4 text-xl font-bold bg-blue-600 text-white rounded-full cta-button hover:bg-blue-700 transition duration-300">
135	                    나의 위험도 즉시 측정하기 ⚙️
136	                </button>
137	
138	            </div>
139	        </section>
140	
141	
142	        <!-- 🔵 Section 3: CTA (Call to Action) -->
143	        <section id="cta" class="bg-blue-600 text-white text-center py-20">
144	            <div class="max-w-4xl mx-auto px-4">
145	                <h2 class="text-4xl md:text-5xl font-extrabold mb-4">
146	                    더 이상 추측하지 마세요. 정량적 근거가 필요합니다.
147	                </h2>
148	                <p class="text-xl mb-10 opacity-90">
149	                    Mini-App에서 확인된 위험도 점수와 맞춤형 관리 플랜이 궁금하신가요? 🧐
150	                </p>
151	
152	                <!-- 최종 CTA 버튼 -->
153	                <a href="#" onclick="alert('✅ Mini-App 진단 페이지로 이동합니다. (API 연동 Mock)'); return false;" class="inline-block px-12 py-4 text-2xl font-bold bg-yellow-400 text-gray-900 rounded-full cta-button hover:bg-yellow-300 transition duration-300">
154	                    [무료 진단 받기] Mini-App 바로 접속하기 📲
155	                </a>
156	
157	                 <p class="mt-6 text-sm opacity-70">
158	                    *Mini-App에서 상세한 개인화 컨설팅을 제공받으실 수 있습니다. (최종 전환 목표)
159	                </p>
160	            </div>
161	        </section>
162	
163	    </main>
164	
165	
166	    <!-- 자바스크립트 로직 -->
167	    <script>
168	        // 1. 진단 점수 계산 및 UI 업데이트 로직
169	        function calculateRisk() {
170	            let totalScore = 0;
171	            const checkboxes = document.querySelectorAll('#quiz-form input:checked');
172	            checkboxes.forEach(cb => {
173	                totalScore += parseInt(cb.getAttribute('data-weight'));
174	            });
175	            return Math.min(100, totalScore); // 최대 100점 제한
176	        }
177	
178	        function updateRiskBar(score) {
179	            const fill = document.getElementById('risk-score-fill');
180	            const scoreDisplay = document.getElementById('score-display');
181	            const messageDiv = document.getElementById('diagnosis-message');
182	            const diagnosisTitle = messageDiv.querySelector('.font-bold');
183	
184	            // 1. SVG 업데이트 (Designer Spec 반영)
185	            fill.style.width = `${score}%`;
186	
187	            let color;
188	            let statusText;
189	
190	            if (score >= 85) {
191	                color = 'var(--danger-color)'; // 빨강
192	                statusText = "🚨 위험 단계: 즉각적인 생활 개선이 필요합니다.";
193	                messageDiv.className = 'mt-8 p-4 border-l-4 border-red-500 bg-red-50';
194	            } else if (score >= 50) {
195	                color = 'var(--warning-color)'; // 주황/노랑
196	                statusText = "⚠️ 주의 단계: 현재 패턴을 점검하고 생활 습관 개선이 필요합니다.";
197	                messageDiv.className = 'mt-8 p-4 border-l-4 border-yellow-500 bg-yellow-50';
198	            } else {
199	                color = 'var(--success-color)'; // 초록
200	                statusText = "✅ 안정 단계: 현재 관리가 잘 되고 있으나, 지속적인 관심이 필요합니다.";
201	                messageDiv.className = 'mt-8 p-4 border-l-4 border-green-500 bg-green-50';
202	            }
203	
204	            // 2. UI 업데이트
205	            fill.style.backgroundColor = color;
206	            scoreDisplay.textContent = score;
207	            scoreDisplay.className = `text-3xl ${color === 'var(--danger-color)' ? 'text-red-600' : (color === 'var(--warning-color)' ? 'text-yellow-600' : 'text-green-600')}`;
208	
209	            diagnosisTitle.textContent = statusText;
210	            messageDiv.innerHTML = `<strong>${statusText}</strong><p class="mt-2 text-gray-700">현재 점수는 ${score}점으로, 초기 단계의 건강 문제를 시사합니다. 정확한 원인 분석과 맞춤형 솔루션은 Mini-App에서 확인하세요.</p>`;
211	            messageDiv.classList.remove('hidden');
212	        }
213	
214	        // 2. 메인 실행 함수 (버튼 클릭 핸들러)
215	        function calculateRiskAndRunTest() {
216	             const score = calculateRisk();
217	             updateRiskBar(score);
218	             // 스크롤을 결과 영역으로 부드럽게 이동시켜 사용자 경험 개선
219	             document.getElementById('result-area').scrollIntoView({ behavior: 'smooth' });
220	        }
221	
222	    </script>
223	</body>
224	</html>
```
