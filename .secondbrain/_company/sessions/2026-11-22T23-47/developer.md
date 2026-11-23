# 💻 코다리 — 이전에 개발한 DefectIDGraph.tsx 컴포넌트를 기반으로, 가상의 데이터(Dummy Data)와 E2E Funnel 추적 로직을 통합한 'lp_standalone_final.html' 형태의 랜딩 페이지 프로토타입을 완성해 주세요. 특히, 그래프가 Critical Failure 상태일 때 발생하는 사용자 행동 시뮬레이션(예: CTA 클릭 전 망설임)에 대한 트래킹 API 호출 구조를 반드시 구현하고 주석 처리하여 다음 테스트를 준비해야 합니다.

💻 코다리: 작업 시작합니다.
CEO 지시사항을 검토했습니다. `DefectIDGraph.tsx` 컴포넌트와 E2E Funnel 추적 로직을 통합하여, 사용자가 가장 망설이는(Hesitation) 순간의 데이터를 포착하는 것이 핵심 목표입니다. 단순한 프로토타입이 아니라 '테스트 가능한' 구조여야 합니다.

시니어 엔지니어로서, 먼저 현재 컴포넌트의 정의와 의존성을 파악하겠습니다.

<read_file path="c:\Data\Project\Baro_KHNLU\src\components\DefectIDGraph.tsx"/>
<|tool_call>call:list_files{path:c:\Data\Project\Baro_KHNLU\src\components}<tool_call|>

---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\Baro_KHNLU\src\components\DefectIDGraph.tsx (184줄, 6.2KB)
```
 1	import React, { FC } from 'react';
 2	import './DefectIDGraph.css'; // 별도의 CSS 모듈을 사용할 것을 가정합니다.
 3	
 4	// 📌 [Props 정의] 개발자가 테스트 및 데이터를 주입하기 쉽도록 명확하게 정의했습니다.
 5	interface DefectIDGraphProps {
 6	  /** 정상 상태에서의 기준 수치 (예: 정상 인슐린 작용 지수) */
 7	  normalValue: number;
 8	  /** 현재 측정된 오류/문제 수치 (Gap을 보여줄 값) */
 9	  defectiveValue: number;
10	  /** 시스템이 'Critical Failure' 상태에 진입했는지 여부. 이 값에 따라 깜빡임 애니메이션이 트리거됩니다. */
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\Baro_KHNLU\src\components\DefectIDGraph.tsx (184줄)
```
  1	import React, { FC } from 'react';
  2	import './DefectIDGraph.css'; // 별도의 CSS 모듈을 사용할 것을 가정합니다.
  3	
  4	// 📌 [Props 정의] 개발자가 테스트 및 데이터를 주입하기 쉽도록 명확하게 정의했습니다.
  5	interface DefectIDGraphProps {
  6	  /** 정상 상태에서의 기준 수치 (예: 정상 인슐린 작용 지수) */
  7	  normalValue: number;
  8	  /** 현재 측정된 오류/문제 수치 (Gap을 보여줄 값) */
  9	  defectiveValue: number;
 10	  /** 시스템이 'Critical Failure' 상태에 진입했는지 여부. 이 값에 따라 깜빡임 애니메이션이 트리거됩니다. */
 11	  isCriticalFailure: boolean;
 12	}
 13	
 14	// 그래프의 핵심 로직 컴포넌트 (단일 책임 원칙 준수)
 15	const DefectIDGraph: FC<DefectIDGraphProps> = ({ 
 16	    normalValue, 
 17	    defectiveValue, 
 18	    isCriticalFailure 
 19	}) => {
 20	  
 21	  // Gap 계산 및 시각화를 위한 비율 조정
 22	  // (Min-Max 스케일링을 가정하여 최대치를 100으로 정규화했다고 가정합니다. 실제 데이터에 맞게 수정 필요)
 23	  const maxPossibleValue = Math.max(normalValue, defectiveValue);
 24	
 25	  // Defective Value가 normalValue보다 높으면 gap이 크게 보입니다.
 26	  const effectiveDefectRatio = Math.min(1, defectiveValue / (maxPossibleValue || 1));
 27	  // Normal Ratio는 항상 기준치를 보여줍니다.
 28	  const normalRatio = Math.min(1, normalValue / (maxPossibleValue || 1));
 29	
 30	  /**
 31	   * 그래프 시각화 요소의 스타일을 결정합니다.
 32	   * Critical Failure 상태일 때 깜빡이는 클래스를 동적으로 추가/제거합니다.
 33	   */
 34	  const graphContainerClasses = `defect-id-graph ${isCriticalFailure ? 'critical-failure' : ''}`;
 35	
 36	  return (
 37	    <div className={graphContainerClasses}>
 38	      <h3 className="component-title">Defect ID 측정 결과: 시스템 오류 지수</h3>
 39	      <p className="subtext">정상 범위 대비 수치적 Gap을 시각화합니다. (기준 값: {normalValue.toFixed(2)})</p>
 40	
 41	      <div 
 42	        className="graph-container" 
 43	        role="img" // 접근성 확보를 위해 role 지정
 44	        aria-label={`Defect ID Graph showing ${defectiveValue} against normal of ${normalValue}`}
 45	      >
 46	        {/* 1. 정상 범위 (Normal Range) - 비교 기준 */}
 47	        <div 
 48	          className="graph-bar normal-bar" 
 49	          style={{ width: `${Math.max(5, normalRatio * 90)}%` }} // 최소 너비 보장
 50	          title={`정상 수치 (${normalValue.toFixed(2)})`}
 51	        ></div>
 52	
 53	        {/* 2. 오류 지수 (Defect ID) - 문제점 시각화 */}
 54	        <div 
 55	          className="graph-bar defect-bar" 
 56	          style={{ width: `${Math.max(5, effectiveDefectRatio * 90)}%` }}
 57	          title={`오류 수치 (${defectiveValue.toFixed(2)})`}
 58	        ></div>
 59	
 60	      </div>
 61	
 62	      <div className="value-summary">
 63	        <span className="metric normal-metric">정상 기준: {normalValue.toFixed(2)}</span>
 64	        <span className={`metric defect-${isCriticalFailure ? 'critical' : ''} metric`}>
 65	            실측 오류 지수: <strong style={{ fontSize: '1.5em' }}>{defectiveValue.toFixed(2)}</strong>
 66	        </span>
 67	      </div>
 68	
 69	      <p className="warning-text">
 70	        {isCriticalFailure 
 71	          ? "⚠️ 경고: 시스템 Critical Failure 감지! 즉각적인 관리가 필요합니다." 
 72	          : (defectiveValue > normalValue * 1.1 ? "🚨 주의: 정상치 대비 높은 Gap이 확인됩니다. 정밀 검진을 권장합니다." : "✅ 현재 데이터는 안정적입니다.")}
 73	      </p>
 74	
 75	    </div>
 76	  );
 77	};
 78	
 79	export default DefectIDGraph;
 80	```
 81	
 82	### 2. 필수 CSS (애니메이션 및 스타일링) 추가
 83	
 84	깜빡이는 애니메이션과 그래프의 시각적 강조를 위한 CSS가 필요합니다. 이는 `src/components/DefectIDGraph.css`에 작성되어야 합니다.
 85	
 86	<create_file path="src/components/DefectIDGraph.css">
 87	/* --- 💡 코다리 검증: Critical Failure 깜빡임 애니메이션 (CSS Keyframes) --- */
 88	@keyframes blink {
 89	  0%, 100% { opacity: 1; }
 90	  50% { opacity: 0.3; } /* 깜빡이는 효과를 위한 불투명도 감소 */
 91	}
 92	
 93	/* Critical Failure 상태의 그래프 전체에 적용 */
 94	.critical-failure .graph-container {
 95	    animation: blink 0.8s infinite alternate; /* 0.8초 주기로 무한 반복 깜빡임 */
 96	}
 97	
 98	/* 일반 스타일링 및 레이아웃 정의 (가독성 및 전문성 확보) */
 99	.component-title {
100	    color: #1e3a5d; /* 다크 네이비 계열로 신뢰감 부여 */
101	    font-size: 1.4em;
102	    margin-bottom: 0.2em;
103	}
104	
105	.subtext {
106	    color: #6b7280;
107	    margin-bottom: 1.5em;
108	    font-style: italic;
109	}
110	
111	/* 그래프 컨테이너 (시각적 강조) */
112	.graph-container {
113	    display: flex;
114	    align-items: flex-end; /* 바가 바닥에서 시작하게 함 */
115	    height: 80px; /* 고정 높이로 시각화 통일 */
116	    width: 100%;
117	    margin-bottom: 2em;
118	    border-bottom: 2px solid #9ca3af; /* 기준선 */
119	}
120	
121	/* 그래프 바 공통 스타일 */
122	.graph-bar {
123	    height: 100%;
124	    transition: width 0.8s cubic-bezier(0, 0, 0.5, 1); /* 부드러운 변화 효과 */
125	    display: flex;
126	    align-items: center;
127	    justify-content: center;
128	    padding: 0 10px;
129	}
130	
131	/* 정상 범위 (Normal) - 신뢰감을 주는 색상 */
132	.normal-bar {
133	    background-color: #4ade8b; /* 그린 계열 */
134	    opacity: 0.7;
135	}
136	
137	/* 오류 지수 (Defect ID) - 경고와 긴급성을 나타내는 색상 */
138	.defect-bar {
139	    background-color: #f97316; /* 오렌지/앰버 계열 (Warning Signal) */
140	    box-shadow: 0 0 5px rgba(249, 115, 22, 0.8); /* Glow 효과 추가 */
141	}
142	
143	/* 값 요약 섹션 */
144	.value-summary {
145	    display: flex;
146	    justify-content: space-between;
147	    align-items: baseline;
148	    margin-bottom: 1em;
149	}
150	
151	.metric {
152	    font-size: 1.1em;
153	    padding: 5px 10px;
154	    border-radius: 4px;
155	}
156	
157	.normal-metric {
158	    background-color: #d1fae5; /* 연한 배경 */
159	    color: #166534;
160	}
161	
162	/* Critical Failure 상태일 때의 강조 스타일 */
163	.defect-critical .graph-bar {
164	    animation: blink 0.8s infinite alternate;
165	}
166	
167	.warning-text {
168	    padding: 10px;
169	    border-radius: 6px;
170	    background-color: #fef2f2; /* 연한 빨간 배경 */
171	    color: #b91c1c; /* 다크 레드 텍스트 */
172	    font-weight: bold;
173	}
174	
175	/* 모바일 반응형 고려 (가독성 확보) */
176	@media (max-width: 600px) {
177	    .graph-container {
178	        height: auto;
179	    }
180	    .value-summary {
181	        flex-direction: column;
182	        gap: 10px;
183	    }
184	}
```
