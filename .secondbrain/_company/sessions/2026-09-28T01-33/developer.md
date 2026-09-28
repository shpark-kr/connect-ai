# 💻 코다리 — Designer가 제시할 3가지 버전의 A/B 테스트 변수 값들을 수용하고 통합 테스트를 수행할 수 있도록 LPO 프로토타입에 '변수 주입 인터페이스(Input UI)'를 구축하십시오. 이 인터페이스는 최소한 헤드라인, CTA 텍스트, 배경 색상 변경을 시뮬레이션하며, 각 변수가 전체 Funnel의 다른 요소들과 충돌 없이 작동하는지 단위 테스트(Unit Test) 환경을 준비해야 합니다.

💻 코다리: 작업 시작합니다.

CEO의 지시사항을 검토했습니다. LPO 프로토타입에 A/B 테스트 변수 주입 인터페이스를 구축하고, 이것이 단위 테스트 환경에서 충돌 없이 작동하는지 확인하는 것은 매우 중요합니다. 단순히 UI를 추가하는 것을 넘어, **변수의 유효성을 검사(Validation)**하는 로직을 포함해야 합니다.

현재 작업 대상은 `c:\Data\Project\FreqTrade\standalone_funnel_mockup.html` 파일입니다. 이 파일을 읽어 현재 구조와 변수 주입이 가장 적절한 위치를 파악하겠습니다.

<read_file path="c:\Data\Project\FreqTrade\standalone_funnel_mockup.html"/>


---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\FreqTrade\standalone_funnel_mockup.html (340줄, 18.0KB)
```
 1	<!DOCTYPE html>
 2	<html lang="ko">
 3	<head>
 4	    <meta charset="UTF-8">
 5	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
 6	    <title>🩸 온현 | 시스템적 고장 위험 진단 프로토타입</title>
 7	    <!-- Tailwind CSS CDN을 사용하여 빠른 개발 및 스타일링 통일성 확보 -->
 8	    <script src="https://cdn.tailwindcss.com"></script>
 9	    <style>
10	        /* Custom Color Palette Mapping */
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\FreqTrade\standalone_funnel_mockup.html (340줄)
```
  1	<!DOCTYPE html>
  2	<html lang="ko">
  3	<head>
  4	    <meta charset="UTF-8">
  5	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  6	    <title>🩸 온현 | 시스템적 고장 위험 진단 프로토타입</title>
  7	    <!-- Tailwind CSS CDN을 사용하여 빠른 개발 및 스타일링 통일성 확보 -->
  8	    <script src="https://cdn.tailwindcss.com"></script>
  9	    <style>
 10	        /* Custom Color Palette Mapping */
 11	        :root {
 12	            --color-navy: #0A1931; /* Background/Base */
 13	            --color-crimson: #CC0000; /* Danger/Warning */
 14	            --color-gold: #FFC72C; /* Highlight/Solution */
 15	            --color-text: #EAEAEA;
 16	        }
 17	
 18	        body {
 19	            background-color: var(--color-navy);
 20	            color: var(--color-text);
 21	            font-family: 'Arial', sans-serif;
 22	        }
 23	
 24	        /* Glitch Effect (Step 1 - Loading) */
 25	        .glitch-loading::after {
 26	            content: attr(data-text);
 27	            animation: glitch-anim 0.5s infinite alternate;
 28	        }
 29	
 30	        @keyframes glitch-anim {
 31	            0% { transform: translate(0, 0); opacity: 1; }
 32	            20% { transform: translate(-3px, 3px) scaleX(1.01); opacity: 0.9; }
 33	            40% { transform: translate(3px, -3px) scaleX(1.01); opacity: 0.8; }
 34	            60% { transform: translate(-2px, 2px) scaleX(1.01); opacity: 0.95; }
 35	            80% { transform: translate(2px, -2px) scaleX(1.01); opacity: 0.9; }
 36	            100% { transform: translate(0, 0); opacity: 1; }
 37	        }
 38	
 39	        /* Deep Crimson Red Overlay Filter (Step 1 & 2 Transition) */
 40	        #overlay {
 41	            position: fixed;
 42	            top: 0;
 43	            left: 0;
 44	            width: 100%;
 45	            height: 100%;
 46	            background-color: rgba(204, 0, 0, 0); /* Start transparent */
 47	            transition: background-color 0.5s ease-in-out;
 48	            pointer-events: none; /* Click events pass through the overlay */
 49	        }
 50	
 51	        /* Score Gauge Styling */
 52	        #scoreGaugeContainer {
 53	            height: 30px;
 54	            background: linear-gradient(to right, #1e40af, #3b82f6); /* Initial neutral color */
 55	            transition: background-color 1s ease-out;
 56	        }
 57	
 58	        #scoreFill {
 59	            height: 100%;
 60	            width: 0%;
 61	            background-color: var(--color-gold);
 62	            transition: width 2s cubic-bezier(0.68, -0.55, 0.27, 1.55); /* Springy animation */
 63	        }
 64	
 65	        /* Specific Danger Levels */
 66	        .level-red { background-color: var(--color-crimson) !important; }
 67	        .level-yellow { background-color: #f59e0b !important; }
 68	        .level-green { background-color: #16a34a !important; }
 69	
 70	    </style>
 71	</head>
 72	<body>
 73	
 74	    <!-- Deep Crimson Red Overlay Filter -->
 75	    <div id="overlay"></div>
 76	
 77	    <header class="py-12 text-center border-b border-gray-800/50">
 78	        <h1 class="text-4xl font-extrabold tracking-tight">🩸 시스템적 고장 진단 모듈</h1>
 79	        <p class="mt-3 text-lg text-muted-gold">당신의 몸이 보내는 위험 신호를 놓치지 마세요. (Mini-App Funnel Mockup)</p>
 80	    </header>
 81	
 82	    <main class="container mx-auto p-6 max-w-4xl">
 83	
 84	        <!-- Step 1: Input Form -->
 85	        <section id="inputSection" class="mb-12 bg-gray-800/50 p-8 rounded-lg shadow-2xl border border-red-900/30">
 86	            <h2 class="text-2xl font-bold mb-6 text-red-400 flex items-center"><span class="mr-2 text-3xl">⚙️</span> 시스템 입력 데이터 측정</h2>
 87	            <p class="mb-8 text-gray-400">다음 핵심 바이오마커 데이터를 최대한 정확하게 입력해 주세요. (가상 시뮬레이션)</p>
 88	
 89	            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
 90	                <!-- Input 1: Glucose Spike -->
 91	                <div>
 92	                    <label for="glucoseSpike" class="block text-sm font-medium mb-2 text-gold">혈당 스파이크 위험 지수 (0~10)</label>
 93	                    <input type="range" id="glucoseSpike" min="0" max="10" value="5" class="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer range-slider">
 94	                    <div class="text-right text-sm mt-2"><span id="glucoseValue">5</span> / 10</div>
 95	                </div>
 96	
 97	                <!-- Input 2: Sleep Quality -->
 98	                <div>
 99	                    <label for="sleepQuality" class="block text-sm font-medium mb-2 text-gold">수면 질 지표 (낮을수록 위험) (0~10)</label>
100	                    <input type="range" id="sleepQuality" min="0" max="10" value="7" class="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer range-slider">
101	                    <div class="text-right text-sm mt-2"><span id="sleepValue">7</span> / 10</div>
102	                </div>
103	
104	                <!-- Input 3: Inflammation Index -->
105	                <div>
106	                    <label for="inflammationIndex" class="block text-sm font-medium mb-2 text-gold">만성 염증 지표 (0~10)</label>
107	                    <input type="range" id="inflammationIndex" min="0" max="10" value="8" class="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer range-slider">
108	                    <div class="text-right text-sm mt-2"><span id="inflammationValue">8</span> / 10</div>
109	                </div>
110	            </div>
111	
112	            <button onclick="runDiagnosis()" class="mt-10 w-full py-3 bg-red-700 hover:bg-red-600 text-white font-bold rounded-lg transition duration-200 shadow-xl transform hover:scale-[1.01]">
113	                ⚡️ 진단 시작 (위험 점수 계산)
114	            </button>
115	        </section>
116	
117	        <!-- Step 2: Results & Funnel Display -->
118	        <section id="resultSection" class="hidden mb-12 p-8 bg-gray-900/70 rounded-lg shadow-inner border-l-4 border-red-600">
119	            <h2 class="text-3xl font-bold mb-6 flex items-center text-gold">✅ 진단 결과 보고서</h2>
120	
121	            <!-- Score Gauge -->
122	            <div class="mb-8 p-6 bg-gray-800 rounded-lg shadow-inner">
123	                <p class="text-xl mb-2 font-semibold" id="scoreText">총 위험 점수: 0점</p>
124	                <div id="scoreGaugeContainer" class="relative rounded-full shadow-inner border border-gray-700 overflow-hidden">
125	                    <div id="scoreFill" style="width: 0%;"></div>
126	                </div>
127	            </div>
128	
129	            <!-- Risk Level Display -->
130	            <div class="mb-10 p-6 text-center rounded-lg border border-red-800/50" id="riskLevelDisplay">
131	                <h3 class="text-4xl font-extrabold mb-2" id="levelTitle">대기 중...</h3>
132	                <p class="text-xl text-gray-300" id="levelDescription">측정 데이터를 입력하고 진단 버튼을 눌러주세요.</p>
133	            </div>
134	
135	            <!-- Failure Report (Escalation) -->
136	            <div class="bg-red-900/40 p-6 rounded-lg border-l-4 border-red-500 mb-12">
137	                <h3 class="text-xl font-bold text-red-400 flex items-center"><span class="mr-2 text-2xl">🚨</span> 시스템적 고장 경고:</h3>
138	                <p id="failureReportText" class="mt-2 text-gray-200"></p>
139	            </div>
140	
141	            <!-- Step 3: CTA (The Conversion Point) -->
142	            <div id="ctaSection" class="text-center p-10 bg-[#0A1931]/80 rounded-xl border border-gold/50 transition duration-500 shadow-2xl" style="opacity: 0.3;">
143	                <h4 class="text-3xl font-extrabold text-red-400 mb-4">더 이상 방치할 시간이 없습니다.</h4>
144	                <p class="text-lg text-gray-300 mb-8 max-w-md mx-auto">현재의 위험 수준은 생활 습관 교정만으로는 해결하기 어렵습니다. 전문가의 시스템적 진단이 필요합니다.</p>
145	
146	                <!-- Level 1 CTA (Primary Goal) -->
147	                <button id="ctaLevel1Button" onclick="simulatePurchase('Level 1')" class="py-4 px-12 text-xl bg-red-600 hover:bg-red-500 text-white font-bold rounded-full transition duration-300 shadow-lg transform scale-95 opacity-30 cursor-not-allowed" disabled>
148	                    ✅ Level 1 집중 컨설팅 (29,000원) 시작하기
149	                </button>
150	
151	                 <!-- Level 2 CTA (Secondary Goal - Hidden unless critical) -->
152	                <button id="ctaLevel2Button" onclick="simulatePurchase('Level 2')" class="py-4 px-12 text-xl bg-gray-600 hover:bg-gray-500 text-white font-bold rounded-full transition duration-300 shadow-lg transform scale-95 opacity-30 cursor-not-allowed mt-4" disabled>
153	                    🚀 Level 2 통합 프로그램 (299,000원) 문의하기
154	                </button>
155	
156	            </div>
157	        </section>
158	    </main>
159	
160	    <script>
161	        // === CORE LOGIC & STATE MANAGEMENT ===============================
162	
163	        const ELEMENTS = {
164	            overlay: document.getElementById('overlay'),
165	            inputSection: document.getElementById('inputSection'),
166	            resultSection: document.getElementById('resultSection'),
167	            levelTitle: document.getElementById('levelTitle'),
168	            levelDescription: document.getElementById('levelDescription'),
169	            scoreText: document.getElementById('scoreText'),
170	            scoreGaugeContainer: document.getElementById('scoreGaugeContainer'),
171	            scoreFill: document.getElementById('scoreFill'),
172	            failureReportText: document.getElementById('failureReportText'),
173	            ctaSection: document.getElementById('ctaSection'),
174	            ctaLevel1Button: document.getElementById('ctaLevel1Button'),
175	            ctaLevel2Button: document.getElementById('ctaLevel2Button')
176	        };
177	
178	        /**
179	         * 바이오마커를 기반으로 위험 점수를 계산합니다. (가중치 부여 시뮬레이션)
180	         * @param {number} g - 혈당 스파이크 지수 (0-10)
181	         * @param {number} s - 수면 질 지표 (0-10)
182	         * @param {number} i - 염증 지표 (0-10)
183	         * @returns {{score: number, level: string}} 계산된 점수와 위험 레벨 객체.
184	         */
185	        function calculateRiskScore(g, s, i) {
186	            // 가중치 적용 예시: 높은 스파이크와 낮은 수면 질이 치명적임.
187	            const score = Math.round((g * 2.5 + (10 - s) * 1.8 + i * 1.5) / 3);
188	
189	            let level;
190	            if (score >= 7) {
191	                level = 'Deep Crimson Red'; // 시스템적 고장 임계치 도달
192	            } else if (score >= 4) {
193	                level = 'Yellow'; // 주의 단계
194	            } else {
195	                level = 'Green'; // 안정 단계
196	            }
197	
198	            return { score: Math.max(0, Math.min(15, score)), level };
199	        }
200	
201	        /**
202	         * UI 상태를 업데이트하고 시각적 연출을 실행합니다. (핵심 Funnel 로직)
203	         * @param {number} score - 최종 위험 점수
204	         * @param {string} level - 'Green', 'Yellow', 'Deep Crimson Red' 중 하나
205	         */
206	        function updateUIState(score, level) {
207	            // 1. Overlay Filter (시각적 경고)
208	            ELEMENTS.overlay.style.backgroundColor = (level === 'Deep Crimson Red') ? 'rgba(204, 0, 0, 0.5)' : 'transparent';
209	
210	            // 2. Score Gauge Update
211	            const percentage = Math.min(100, score * 6); // Max 15 -> 90%로 제한 (시각적 안정성)
212	            ELEMENTS.scoreFill.style.width = `${percentage}%`;
213	            ELEMENTS.scoreGaugeContainer.className = `relative rounded-full shadow-inner border border-gray-700 overflow-hidden ${level === 'Deep Crimson Red' ? 'level-red' : level === 'Yellow' ? 'level-yellow' : 'level-green'}`;
214	            ELEMENTS.scoreFill.style.backgroundColor = getComputedStyle(document.documentElement).getPropertyValue(`--color-${level.toLowerCase()}`);
215	
216	
217	            // 3. Level Display Update
218	            let title, description, report;
219	
220	            if (level === 'Deep Crimson Red') {
221	                title = '🔴 심각한 시스템적 고장 위험';
222	                description = '⚠️ 핵심 바이오마커의 임계치를 넘어섰습니다. 단순 생활 습관 교정으로는 회복이 불가능하며, 즉각적인 전문 개입이 필요합니다.';
223	                report = '현재 신체 시스템은 여러 지표가 동시에 취약한 ' + getFailureReason(score) + ' 상태입니다. 방치할 경우 연쇄적 기능 저하로 이어질 수 있습니다.';
224	            } else if (level === 'Yellow') {
225	                title = '🟡 주의 단계: 위험 징후 감지';
226	                description = '💡 몇 가지 지표가 정상 범위를 벗어났습니다. 생활 습관 교정이 필요하며, 전문가의 가이드를 받아 점진적으로 개선해 나가세요.';
227	                report = '주요 바이오마커 중 일부에서 이상 신호가 감지되었습니다. 경고 수준은 낮으나, 지금 바로 관리가 필요한 상태입니다.';
228	            } else {
229	                title = '🟢 안정 단계: 건강한 시스템 작동';
230	                description = '✨ 현재 측정된 지표들은 매우 안정적이며 정상 범위 내에 있습니다. 꾸준한 유지 관리만으로 충분합니다.';
231	                report = '모든 핵심 바이오마커가 양호하게 작동하고 있습니다. 현재의 루틴을 유지하는 것이 가장 중요합니다.';
232	            }
233	
234	            ELEMENTS.levelTitle.textContent = title;
235	            ELEMENTS.levelDescription.textContent = description;
236	            ELEMENTS.failureReportText.innerHTML = report;
237	
238	
239	            // 4. CTA Button State Update (Funnel Trigger)
240	            const isDeepRed = level === 'Deep Crimson Red';
241	            
242	            // Level 1은 Deep Crimson Red이거나 Yellow일 때만 활성화 유도 (구매 욕구 자극)
243	            ELEMENTS.ctaLevel1Button.disabled = !(isDeepRed || level === 'Yellow');
244	            ELEMENTS.ctaLevel1Button.classList.toggle('opacity-30', ELEMENTS.ctaLevel1Button.disabled);
245	            ELEMENTS.ctaLevel1Button.classList.toggle('cursor-not-allowed', ELEMENTS.ctaLevel1Button.disabled);
246	            if (ELEMENTS.ctaLevel1Button.disabled) {
247	                ELEMENTS.ctaLevel1Button.innerHTML = '✅ Level 1 집중 컨설팅 (29,000원) 시작하기';
248	            } else if(isDeepRed){
249	                 ELEMENTS.ctaLevel1Button.innerHTML = '🚨 즉시 전문 진단 받기 (클릭)';
250	            } else {
251	                ELEMENTS.ctaLevel1Button.innerHTML = '✨ Level 1 집중 컨설팅으로 관리 시작';
252	            }
253	
254	            // Level 2는 오직 Deep Crimson Red일 때만 강하게 노출 (최대 수익화)
255	            const isCritical = level === 'Deep Crimson Red';
256	            ELEMENTS.ctaLevel2Button.disabled = !isCritical;
257	            ELEMENTS.ctaLevel2Button.classList.toggle('opacity-30', ELEMENTS.ctaLevel2Button.disabled);
258	            ELEMENTS.ctaLevel2Button.classList.toggle('cursor-not-allowed', ELEMENTS.ctaLevel2Button.disabled);
259	
260	            if (isCritical) {
261	                ELEMENTS.ctaLevel2Button.innerHTML = '🚀 Level 2 통합 프로그램 상담 요청';
262	            } else {
263	                ELEMENTS.ctaLevel2Button.innerHTML = '🚀 Level 2 통합 프로그램 문의하기';
264	            }
265	
266	
267	            // 5. Final Transition
268	            setTimeout(() => {
269	                ELEMENTS.resultSection.classList.remove('hidden');
270	                ELEMENTS.ctaSection.style.opacity = '1'; // 애니메이션 끝난 후 활성화
271	            }, 300);
272	        }
273	
274	        /**
275	         * 점수 계산에 따른 구체적인 위험 원인을 문장으로 생성합니다. (마케팅적 요소)
276	         */
277	        function getFailureReason(score) {
278	            if (score >= 12) return "급격한 혈당 변화와 만성 염증의 복합 작용";
279	            if (score >= 8) return "수면 부족으로 인한 자율신경계 교란과 높은 염증 지표 결합";
280	            return "복합적인 바이오마커 불균형";
281	        }
282	
283	        /**
284	         * 메인 진단 실행 함수. 모든 흐름을 제어합니다.
285	         */
286	        function runDiagnosis() {
287	            // 1. 입력 값 추출 및 클리닝
288	            const g = parseFloat(document.getElementById('glucoseSpike').value);
289	            const s = parseFloat(document.getElementById('sleepQuality').value);
290	            const i = parseFloat(document.getElementById('inflammationIndex').value);
291	
292	            // 2. 로딩 애니메이션 시작 (글리치 효과 시뮬레이션)
293	            ELEMENTS.levelTitle.textContent = '시스템 진단 중...';
294	            ELEMENTS.levelDescription.textContent = '';
295	            ELEMENTS.failureReportText.innerHTML = '';
296	            document.getElementById('scoreGaugeContainer').style.width = '100%'; // 가이드라인 초기화
297	
298	            // 3. 계산 및 상태 업데이트 (setTimeout을 사용해 애니메이션 시간 부여)
299	            setTimeout(() => {
300	                const result = calculateRiskScore(g, s, i);
301	                updateUIState(result.score, result.level);
302	                console.log(`Diagnosis Complete: Score=${result.score}, Level=${result.level}`);
303	            }, 1500); // 1.5초 로딩 지연 시뮬레이션
304	
305	        }
306	        
307	        /**
308	         * CTA 버튼 클릭 시 구매/상담 과정을 시뮬레이션합니다.
309	         */
310	        function simulatePurchase(level) {
311	             alert(`[구매/상담 요청 성공] ${level} 프로그램에 대한 관심이 확인되었습니다.\n\n담당 컨설턴트가 곧 연락드립니다. (실제 결제 페이지로 이동 예정)\n👏 Mini-App Funnel CTA 작동 완료 ✅`);
312	        }
313	
314	
315	        // === 초기화 및 이벤트 리스너 설정 ===============================
316	
317	        document.addEventListener('DOMContentLoaded', () => {
318	            const sliders = [
319	                { id: 'glucoseSpike', valueId: 'glucoseValue' },
320	                { id: 'sleepQuality', valueId: 'sleepValue' },
321	                { id: 'inflammationIndex', valueId: 'inflammationValue' }
322	            ];
323	
324	            // 슬라이더 이벤트 리스너 부착 (실시간 값 업데이트)
325	            sliders.forEach(slider => {
326	                const input = document.getElementById(slider.id);
327	                const display = document.getElementById(slider.valueId);
328	                
329	                input.addEventListener('input', () => {
330	                    display.textContent = input.value;
331	                });
332	            });
333	
334	            // 초기 상태 설정 (진단 전)
335	            updateUIState(0, 'Green'); // 기본값으로 Green 레벨의 낮은 점수와 안정화된 UI로 시작
336	        });
337	
338	    </script>
339	</body>
340	</html>
```
