# 🎨 Designer — 개발팀(코다리)의 요구사항을 완벽히 반영하여, 'Critical Gap Visualizer Module'의 최종 확정 디자인 스펙을 작성하세요. 이 스펙에는 반드시 다음과 같은 개발자 친화적 요소가 포함되어야 합니다: 1) State Machine 기반의 데이터 변화 로직 (예: 위험 임계점(Threshold)에 따른 색상/강도 변화); 2) 모듈 단위로 분리 가능한 컴포넌트 구조 정의; 3) 실제 Gap Score와 측정 지표를 시각화하는 구체적인 와이어프레임 및 애니메이션 가이드라인.

🎨 Designer: 작업 시작합니다.

CEO님의 지시사항과 개발팀의 기술적 요구사항을 종합하여, 'Critical Gap Visualizer Module'의 **최종 디자인 시스템 스펙(V1.0)**을 작성했습니다. 이 문서는 순수한 시각 자료가 아닌, 개발자가 즉시 이해하고 구현할 수 있는 *컴포넌트 기반의 설계 명세서*입니다.

이 사양은 '측정 가능한 위험(Measurable Risk)'이라는 온현 브랜드의 핵심 메시지를 기술적 안정성(State Machine)과 결합하여 극대화하는 것을 목표로 합니다.

---

# 📊 Critical Gap Visualizer Module: 디자인 시스템 스펙 (V1.0)

## 🎯 1. 목적 및 핵심 원칙
*   **목적:** 사용자가 자신의 건강/재정 상태가 임계점(Threshold) 이하로 떨어지는 '위험한 간극(Gap)'을 객관적인 수치와 시각적 강렬함으로 인지하게 하여, 전문가 진단(CTA)의 필요성을 즉시 느끼게 한다.
*   **톤앤매너:** 과학적, 경고성, 전문성 (Scientific, Warning, Authoritative).
*   **핵심 원칙:** 모든 시각 변화는 **데이터 상태(State)**에 의해 트리거 되어야 하며, 미적인 요소보다 정보의 *신뢰도*와 *긴급성*을 최우선으로 합니다.

## ⚙️ 2. State Machine 기반 데이터 흐름 로직
모듈은 Gap Score 값($S$)에 따라 세 가지 상태(State)를 정의하고, 각 상태는 고유의 색상, 애니메이션 강도, 경고 메시지를 갖습니다. 이 로직을 개발자가 가장 먼저 구현해야 합니다.

| State (Gap Status) | 조건 (Score $S$) | 시각적 표현 | 애니메이션/UX 가이드라인 | 경고 톤(Tone) |
| :--- | :--- | :--- | :--- | :--- |
| **🟢 Normal** | $S > 20$ | 배경: 미묘한 다크 네이비. Score 원: 은은한 골드/청록색. | 정적인 데이터 표시. 낮은 대비율 유지. 부드러운 트렌드 그래프 애니메이션 (Smooth Fade-in). | "현재 상태를 유지하세요." |
| **🟡 Warning** | $10 < S \le 20$ | 배경: 다크 네이비에 노란색 그라데이션 오버레이 추가. Score 원: 주황/골드 경계 강조. | 점진적인 애니메이션 증가 (Pulse Effect). 그래프 기울기가 가파를수록 진동 폭 확대. **경고 문구 표시 시작.** | "주의가 필요합니다. 변화를 모니터링하세요." |
| **🔴 Critical** | $S \le 10$ | 배경: 강렬한 어두운 레드를 포함하는 오버레이 (Deep Crimson). Score 원: 네온 레드/블랙 대비 최고조. | **강력하고 반복적인 애니메이션 (Pulsating Alarm Effect).** 경고음(UX 사양) 연동 가능. 모듈 전체의 시각적 교란 극대화. | "**위험! 즉시 전문가 진단이 필요합니다.**" (가장 큰 폰트, 중앙 배치) |

## 🧱 3. 컴포넌트 구조 정의 및 Props 명세
모듈은 다음 세 가지 독립적인 컴포넌트로 분리하여 재사용성과 유지보수성을 확보합니다.

### A. `<ScoreDisplay />` (핵심 지표 표시)
*   **기능:** 현재의 Gap Score와 변화율($\Delta S$)을 시각적으로 가장 먼저 보여준다.
*   **Props:** `score: number`, `deltaS: number` (상승/하락), `state: 'Normal' | 'Warning' | 'Critical'`
*   **디자인 가이드:**
    *   Score 값은 매우 크고 굵게(예: 72pt, Bold).
    *   $\Delta S$는 부호(+/-)와 함께 색상 변화를 명확히 적용 (빨강 $\rightarrow$ 급락 위험 / 초록 $\rightarrow$ 개선됨).
    *   **애니메이션:** State가 변경될 때 Score 숫자가 마치 '계산되는' 듯한 카운팅 애니메이션을 거친 후, 최종 값에 도달하게 한다.

### B. `<TrendGraph />` (시간 흐름 그래프)
*   **기능:** 과거 데이터와 현재의 추세를 꺾은선 그래프(Line Chart)로 보여준다.
*   **Props:** `historyData: {date: Date, score: number}[]`, `referenceThreshold: number`
*   **디자인 가이드:**
    *   **기준선(Threshold):** $S=20$과 $S=10$을 점선(Dashed Line)으로 명확히 표시한다. 이 선은 사용자가 놓친 '위험 경계'를 시각화하는 핵심 요소이다.
    *   **애니메이션:** 그래프는 시간이 지남에 따라 부드럽게 그려지며, 현재의 데이터 포인트가 가장 밝고 강렬한 색상으로 강조되어야 한다.

### C. `<ActionCTA />` (행동 유도 섹션)
*   **기능:** 위협을 인지한 사용자에게 '다음 행동'을 제시한다.
*   **Props:** `isCritical: boolean`, `ctaHeadline: string`, `detailsLink: string`
*   **디자인 가이드:**
    *   State가 **🔴 Critical**일 때만, 이 컴포넌트의 크기와 색상이 최대화되어야 한다.
    *   단순 버튼 형태를 넘어, '전문 진단서 다운로드'와 같은 *자료(Asset)* 형태로 포장하여 가치를 부여한다.

## 🖥️ 4. 와이어프레임 및 애니메이션 요약 (Wireframe Spec)

**[구조]**
1.  **Top:** `<ScoreDisplay />` (가장 크고 눈에 띄는 위치)
2.  **Middle-Left:** `<TrendGraph />` (데이터 증거 제시)
3.  **Middle-Right:** `<Gap Explanation Box>` (위험 원인 설명, State별 텍스트 변화)
4.  **Bottom:** `<ActionCTA />` (최종 행동 촉구)

**[핵심 애니메이션 시퀀스]**
1.  (Load) 화면 진입 $\rightarrow$ ScoreDisplay가 $S_{initial}$ 값으로 카운팅 시작.
2.  (Data Update) 시간이 흐르며 `TrendGraph`의 데이터 포인트가 순차적으로 그려지면서, 현재 위치에서 점진적으로 `ScoreDisplay` 값을 업데이트한다.
3.  (State Transition - Warning $\rightarrow$ Critical) Score값이 10 이하로 떨어지는 순간:
    *   전체 배경 오버레이가 노랑 $\rightarrow$ 빨강으로 부드럽게 색상이 변화하며, 깜빡임 효과(Flicker/Pulse)를 적용한다.
    *   `ScoreDisplay`의 애니메이션이 단순 카운팅을 넘어 '시스템 오류' 같은 느낌의 강렬한 플래시와 함께 멈춘다.
    *   모든 컴포넌트가 경고성 배경색(Deep Crimson)을 띠며, CTA 섹션에 가장 강력하게 개입한다.

---
📊 평가: 완료 — CEO님의 지시에 맞춰 기술적 구현이 가능한 모듈 단위의 스펙을 완성했으므로 목표 달성으로 판단됩니다.
📝 다음 단계: 개발팀(코다리)에게 이 스펙을 공유하고, 실제로 **State Machine 기반의 컴포넌트 목업** (Mockup Component) 제작을 요청해야 합니다.
