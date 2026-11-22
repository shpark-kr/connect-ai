# 💻 코다리 — Designer가 확정한 'Defect ID 시스템 실패 보고서' UI/UX 명세(v1.0)를 기반으로, 프로토타입 페이지의 코딩을 즉시 시작합니다. 목표는 정적 Mockup이 아닌 데이터 바인딩 및 인터랙션이 가능한 최소 기능 제품(MVP)입니다. 특히 다음 기능을 구현해야 합니다: 1. '진단 결과' 섹션에 ATP/ADP 비율 변화를 보여주는 오류 로그 그래프 컴포넌트 (Deep Navy 배경, Crisis Red 경고색 사용). 2. 사용자 입력 필드 및 보고서 제출 시 발생하는 애니메이션 효과(Glitch 또는 Pulse)와 전문적인 에러 메시지 처리 로직을 JavaScript로 구현합니다. 3. 모든 컴포넌트는 Atomic Design 원칙에 따라 구조화하고, 향후 대규모 확장을 염두에 둔 재사용 가능한 API 클라이언트 인터페이스를 포함하도록 설계합니다.

💻 코다리: 작업 시작합니다.

CEO 지시사항을 확인했습니다. 'Defect ID 시스템 실패 보고서' 프로토타입은 단순한 Mockup이 아니라, 데이터 바인딩과 인터랙션 로직이 살아있는 MVP가 되어야 합니다. 이 정도 복잡도면 백엔드 API 클라이언트부터 시작해서 프론트엔드의 상태 관리까지 고려해야 하죠. ⚙️

MVP의 핵심은 **데이터 기반の 위기감 조성**입니다. 따라서 다음 단계로 진행하기 전에, 먼저 기존에 존재하는 `index.html` 파일을 읽어서 어떤 구조 위에 작업을 진행할지 파악하는 게 순서상 맞습니다.

<read_file path="c:\Data\Project\connect-ai\.secondbrain\_company_agents\mockups\system_failure_report\index.html"/>

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\.secondbrain\_company_agents\mockups\system_failure_report\index.html (229줄, 10.1KB)
```
 1	<!DOCTYPE html>
 2	<html lang="ko" class="scroll-smooth">
 3	<head>
 4	    <meta charset="UTF-8">
 5	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
 6	    <title>ATP/ADP 시스템 실패 보고서 (프로토타입)</title>
 7	    <!-- Tailwind CSS CDN - 빠른 프로토타이핑을 위해 사용 -->
 8	    <script src="https://cdn.tailwindcss.com"></script>
 9	    <!-- Chart.js for Graph Visualization -->
10	    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\.secondbrain\_company_agents\mockups\system_failure_report\index.html (229줄)
```
  1	<!DOCTYPE html>
  2	<html lang="ko" class="scroll-smooth">
  3	<head>
  4	    <meta charset="UTF-8">
  5	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  6	    <title>ATP/ADP 시스템 실패 보고서 (프로토타입)</title>
  7	    <!-- Tailwind CSS CDN - 빠른 프로토타이핑을 위해 사용 -->
  8	    <script src="https://cdn.tailwindcss.com"></script>
  9	    <!-- Chart.js for Graph Visualization -->
 10	    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
 11	    <style>
 12	        /* Deep Navy (Primary) 및 Crisis Red (Danger) 색상 정의 */
 13	        :root {
 14	            --color-deep-navy: #0F1B3A; /* Primary Background */
 15	            --color-crisis-red: #C70039; /* Danger/Warning */
 16	            --color-secondary-blue: #4D6DAE; /* Secondary UI elements */
 17	        }
 18	
 19	        body {
 20	            background-color: var(--color-deep-navy);
 21	            color: #E0E0E0;
 22	        }
 23	
 24	        .container-section {
 25	            border-left: 3px solid var(--color-secondary-blue);
 26	            padding-left: 2rem;
 27	        }
 28	
 29	        /* 위험도 게이지 애니메이션 커스텀 */
 30	        #riskGaugeBarContainer .gauge-fill {
 31	            transition: width 1s ease-out, background-color 0.5s ease-in-out;
 32	        }
 33	        
 34	        /* 에러 로그 스크롤링을 위한 스타일 */
 35	        #defectLogOutput {
 36	            height: 300px; /* 고정 높이 설정 */
 37	            overflow-y: auto; /* 스크롤 가능하게 만듦 */
 38	            background-color: rgba(25, 30, 60, 0.7); /* Deep Navy의 약간 밝은 버전 */
 39	            padding: 1rem;
 40	            border-radius: 0.5rem;
 41	        }
 42	
 43	    </style>
 44	</head>
 45	<body>
 46	
 47	    <header class="bg-[#1a2948] py-6 shadow-lg">
 48	        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center">
 49	            <h1 class="text-3xl font-bold text-white tracking-wider">🧬 ATP/ADP 시스템 실패 보고서</h1>
 50	            <div class="text-lg text-yellow-400 bg-[#2c3e50] px-4 py-2 rounded-full shadow-inner">
 51	                Defect ID: <span id="currentDefectId" class="font-bold">LPB-A7</span>
 52	            </div>
 53	        </div>
 54	    </header>
 55	
 56	    <main class="max-w-7xl mx-auto p-6 sm:p-10">
 57	
 58	        <!-- 1. 결함 수준 및 에너지 레벨 요약 (상단 배너) -->
 59	        <section id="summaryStatus" class="mb-12 bg-[#1a2948] p-8 rounded-xl shadow-2xl border border-[var(--color-secondary-blue)]">
 60	            <h2 class="text-2xl font-semibold mb-6 text-white">시스템 상태 개요</h2>
 61	
 62	            <!-- 위험도 게이지 컴포넌트 (Atomic Component) -->
 63	            <div class="mb-8 p-4 bg-[#0f1b3a] rounded-lg shadow-inner">
 64	                <p class="text-sm uppercase tracking-widest text-gray-400 mb-2">결함 수준 위험도 게이지 (ATP/ADP Ratio)</p>
 65	                <div class="flex justify-between items-center mt-3 px-6">
 66	                    <span id="ratioDisplay" class="text-4xl font-extrabold text-[#f97316]">0.85</span>
 67	                    <div>
 68	                        <span class="mr-2 text-sm text-gray-300">안정 (Green)</span>
 69	                        <div class="w-24 bg-gray-600 h-2 rounded-full mr-4 relative">
 70	                            <!-- Dynamic Gauge Fill -->
 71	                            <div id="riskGaugeBar" class="gauge-fill h-full rounded-full transition duration-1000 ease-out" style="width: 85%; background-color: #10b981;"></div>
 72	                        </div>
 73	                        <span class="text-sm text-gray-300">위험 (Red)</span>
 74	                    </div>
 75	                </div>
 76	            </div>
 77	
 78	        </section>
 79	
 80	
 81	        <!-- 2. 에너지 생산량 감소 추이 그래프 (Atomic Component) -->
 82	        <section id="energyGraph" class="mb-16 p-8 bg-[#1a2948] rounded-xl shadow-2xl">
 83	            <h2 class="text-2xl font-semibold mb-6 text-white border-b pb-3 border-[var(--color-secondary-blue)]">🔬 Defect ID별 에너지 생산량 감소 추이</h2>
 84	            <!-- Chart.js가 여기에 캔버스를 그리게 됩니다 -->
 85	            <div style="max-height: 400px;">
 86	                <canvas id="energyChart"></canvas>
 87	            </div>
 88	        </section>
 89	
 90	        <!-- 3. 시스템 에러 로그 (Atomic Component) -->
 91	        <section class="mb-16">
 92	            <h2 class="text-2xl font-semibold mb-6 text-white border-b pb-3 border-[var(--color-secondary-blue)]">🚨 실시간 Defect Log & 경고 기록</h2>
 93	            <div id="defectLogOutput" class="shadow-inner shadow-black/50">
 94	                <!-- 로그가 여기에 동적으로 추가됩니다 -->
 95	                <p class="text-gray-400">[시스템 가동 중... 초기 진단 데이터 수집 중]</p>
 96	            </div>
 97	        </section>
 98	
 99	    </main>
100	
101	
102	    <script>
103	        // ==============================================
104	        // 🔬 JavaScript Logic (Business Logic / Interactivity)
105	        // ==============================================
106	        
107	        const R_GAUGE_ELEMENT = document.getElementById('riskGaugeBar');
108	        const R_RATIO_DISPLAY = document.getElementById('ratioDisplay');
109	        const R_LOG_OUTPUT = document.getElementById('defectLogOutput');
110	        const E_CHART_CANVAS = 'energyChart';
111	
112	        // -------------------
113	        // 1. 위험도 게이지 로직 (Risk Gauge)
114	        // -------------------
115	        function updateRiskGauge(ratio) {
116	            let widthPercent = Math.max(0, Math.min(100, ratio * 100));
117	            let color;
118	
119	            if (ratio >= 0.85) {
120	                color = '#10b981'; // Green: Stable
121	            } else if (ratio >= 0.6) {
122	                color = '#f59e0b'; // Yellow/Orange: Warning
123	            } else {
124	                color = 'var(--color-crisis-red)'; // Red: Critical
125	            }
126	
127	            // CSS 트랜지션을 활용하여 애니메이션 효과 구현
128	            R_GAUGE_ELEMENT.style.width = `${widthPercent}%`;
129	            R_GAUGE_ELEMENT.style.backgroundColor = color;
130	            R_RATIO_DISPLAY.textContent = ratio.toFixed(2);
131	
132	            // (TODO: 이 비율 값을 기반으로 Chart.js 데이터도 업데이트해야 함)
133	        }
134	
135	
136	        // -------------------
137	        // 2. 에러 로그 로직 (Defect Log)
138	        // -------------------
139	        function generateRandomErrorLog() {
140	            const time = new Date().toLocaleTimeString('ko-KR');
141	            const defectCodes = ['LPB-A7', 'MITO-C3', 'ATP-D01', 'JUNCTION-E5'];
142	            const messages = [
143	                'Warning: Energy production rate significantly dropping.',
144	                'Critical Defect Detected. ATP/ADP imbalance confirmed.',
145	                'System integrity check failed. Requires immediate intervention.',
146	                'Module failure in Mitochondria network processing.'
147	            ];
148	            
149	            const randomCode = defectCodes[Math.floor(Math.random() * defectCodes.length)];
150	            const randomMessage = messages[Math.floor(Math.random() * messages.length)];
151	
152	            const logEntry = document.createElement('div');
153	            logEntry.className = 'text-sm border-b border-gray-700 py-1';
154	            logEntry.innerHTML = `<span class="text-yellow-400">[${time}]</span> <strong class="text-red-500">${randomCode}</strong>: ${randomMessage}`;
155	
156	            R_LOG_OUTPUT.prepend(logEntry); // 최신 로그가 위로 가도록
157	        }
158	        
159	        // 3초마다 무작위 로그를 생성하여 추가
160	        setInterval(generateRandomErrorLog, 3000);
161	
162	
163	        // -------------------
164	        // 3. 그래프 로직 (Energy Graph)
165	        // -------------------
166	        let energyChart;
167	
168	        function initializeGraph() {
169	            const ctx = document.getElementById('energyChart').getContext('2d');
170	            energyChart = new Chart(ctx, {
171	                type: 'line',
172	                data: {
173	                    labels: ['T-1h', 'T-30m', 'Now'], // 시간 축
174	                    datasets: [{
175	                        label: 'ATP/ADP Ratio 추이',
176	                        data: [0.95, 0.82, 0.75], // 초기 데이터 (높은 곳에서 낮은 곳으로)
177	                        borderColor: '#C70039', // Crisis Red 기본값
178	                        backgroundColor: 'rgba(199, 0, 57, 0.2)',
179	                        fill: true,
180	                        tension: 0.4,
181	                        pointRadius: 8
182	                    }]
183	                },
184	                options: {
185	                    responsive: true,
186	                    maintainAspectRatio: false,
187	                    scales: {
188	                        y: {
189	                            title: { display: true, text: 'ATP/ADP Ratio (0.0 - 1.0)' },
190	                            min: 0,
191	                            max: 1.0
192	                        },
193	                        x: {
194	                             grid: { color: '#3f5678' } // 그리드 색상 지정
195	                        }
196	                    },
197	                    plugins: {
198	                        legend: { display: false },
199	                        title: { display: true, text: '시간 경과에 따른 에너지 레벨 변화 분석', font: { size: 18 } }
200	                    }
201	                }
202	            });
203	        }
204	
205	        // ==============================================
206	        // 🚀 메인 초기화 함수 실행
207	        // ==============================================
208	        document.addEventListener('DOMContentLoaded', () => {
209	            initializeGraph();
210	            
211	            // 초기 상태값 설정: 0.85 (Yellow/Orange 경고)
212	            updateRiskGauge(0.85);
213	
214	            // 시뮬레이션 시작을 위해 주기적으로 비율 하락 시뮬레이션 추가
215	            setInterval(() => {
216	                let currentRatio = parseFloat(R_RATIO_DISPLAY.textContent);
217	                if (!isNaN(currentRatio)) {
218	                    // 1~3초 간격으로 무작위로 비율을 조금씩 떨어뜨리는 시뮬레이션
219	                    const dropAmount = Math.random() * 0.02 + 0.005; // 0.005 ~ 0.02 사이 하락
220	                    let newRatio = Math.max(0.1, currentRatio - dropAmount);
221	                    updateRiskGauge(newRatio);
222	
223	                    // TODO: 실제 구현에서는 이 비율 변화에 맞춰 Chart.js의 데이터셋도 업데이트해야 합니다.
224	                }
225	            }, 3500); // 3.5초마다 상태 변화 시뮬레이션
226	        });
227	    </script>
228	</body>
229	</html>
```
