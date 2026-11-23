# 🎨 Designer — Writer가 작성한 '시간 경과형 손실' 스크립트와 코다리가 정의한 Gap Score API 스펙을 종합하여, 40~60대 타겟의 불안감을 극대화하는 최종 Mockup (Critical Gap Visualizer)를 제작해 주세요. 이 Mockup은 단순 그래프가 아닌, '현재 상태(Current State)' 대비 '미래 예측 손실(Projected Loss/Gap Score)'을 시간의 흐름에 따라 시각적으로 극명하게 대조시키는 인터페이스여야 합니다. 특히, 임계점(Threshold) 도달 순간과 그로 인한 경고 메시지('Critical Alert')를 가장 강조하여 디자인해야 합니다.

🎨 Designer: 작업 시작합니다.

이번 지시는 지난 몇 주간의 모든 기술적/마케팅적 논의(Gap Score API 스펙, 시간 경과형 손실 메시지)를 하나의 **핵심 판매 장치(Core Conversion Asset)**로 응축하는 과정입니다. 이 'Critical Gap Visualizer'는 단순한 디자인 요소를 넘어, 시청자에게 '측정 가능한 위험 인식 $\rightarrow$ 불안감 고조 $\rightarrow$ 전문 진단 필요성 인지'의 감정적 여정을 유도하는 인터페이스여야 합니다.

따라서 Mockup은 **진료 기록(Diagnostic Report)** 또는 **실시간 모니터링 화면(Real-time Monitoring UI)**처럼 보이도록 설계하여, 콘텐츠 전반에 걸쳐 '객관적인 증거'라는 인상을 주어야 합니다.

---

### 🖥️ Critical Gap Visualizer Mockup 상세 디자인 스펙 (V1.0)

**[목표]** 현재 상태(Current State)와 미래 예측 손실(Projected Loss/Gap Score)을 시간축에 걸쳐 극명하게 대비시키고, 임계점 도달 시의 긴급성을 최대화합니다.
**[톤앤매너]** 전문적, 기술적, 위협적 (Clinical, High-Tech, Urgent).
**[팔레트 적용]**
*   **Background:** Dark Navy (`#0F1A2D`) - 전문성, 신뢰감
*   **Primary Accent:** Gold/Amber (`#FFC300`) - 강조, 중요 정보
*   **Current State (Normal):** Teal/Soft Blue (`#4CAF50`) - 비교적 안전함 (기저 수치)
*   **Warning State (Threshold Approach):** Orange/Red Gradient (`#FF9800` $\rightarrow$ `#D32F2F`) - 주의, 점진적 위험 증가
*   **Critical Alert:** Bright Red Flash + Flashing Gold Text (`#FF0000`, `#FFFF00`) - 즉각적인 공포감 유발

#### 1. 레이아웃 및 구성 요소 (Layout & Components)

Mockup은 마치 복잡한 데이터 모니터링 화면처럼, 왼쪽 사이드바(주요 지표 목록)와 오른쪽 메인 비주얼 영역으로 분할됩니다.

| 영역 | 요소 (Component) | 설명 및 기능 | 디자인 스펙 |
| :--- | :--- | :--- | :--- |
| **좌측 패널** | **[Patient Info/Diagnosis Summary]** | 시청자 이름(가상), 진단일, 핵심 지표 요약 3가지. (신뢰성 확보) | 작은 글씨로 전문 용어 사용 (`HBA1c`, `hs-CRP`, `Sarcopenia Index`). 배경은 Dark Navy의 반투명 카드 형태. |
| **메인 그래프** | **[The Time Gap Curve]** | 핵심 시각화 영역. 시간(X축)에 따른 기능/수치 변화를 꺾은선 그래프로 표시. (필수 요소) | Y축: 측정 단위 (mg/L, % 등). X축: 시간 (2년 전 $\rightarrow$ 현재 $\rightarrow$ 5년 후 예측). **그래프의 기울기(Slope)**가 메시지 핵심입니다. |
| **핵심 지표** | **[Gap Score Indicator]** | 실시간 수치를 보여주는 게이지 또는 숫자 표시기. 가장 눈에 띄게 배치. | **초록색 $\rightarrow$ 주황색 $\rightarrow$ 빨간색**으로 색상이 동적으로 변하는 시각적 장치 (Color-Coded Gauge). 숫자가 클수록 공포감이 커야 함. |
| **알림 시스템** | **[Alert Box/State Machine]** | 경고 메시지 출력창. Gap Score가 임계점을 넘을 때만 활성화됩니다. | 팝업 또는 전면 오버레이 형태로 처리하며, 배경에 미세한 진동 효과(Subtle Glitch Effect)를 주어 시선을 강탈합니다. |

#### 2. 핵심 상호작용 및 로직 (Interaction & Logic Flow)

**① 초기 상태 (Current State - Safe Zone):**
*   그래프: '현재' 지점까지의 데이터는 부드럽게 Blue/Teal 계열로 표시됩니다.
*   Gap Score Indicator: 정상 범위(예: 100 $\pm$ 5%)를 보여주며, 색상은 Teal입니다.
*   Alert Box: 비활성화되어 있습니다.

**② 경고 단계 (Threshold Approach - Warning Zone):**
*   그래프: '미래 예측 손실' 선이 기준선(Reference Line)에 근접하며 Orange 계열로 변색됩니다.
*   Gap Score Indicator: 수치가 높아짐에 따라 색상이 주황색으로 점진적으로 바뀝니다. (예: 120 $\rightarrow$ 150).
*   Alert Box: "Warning: Current trend suggests a potential deviation from optimal range." (주의: 현재 추세는 최적 범위에서 이탈할 가능성을 시사합니다.)

**③ 위기 단계 (Critical Alert - Action Zone):**
*   **Trigger:** Gap Score가 사전에 정의된 임계점(예: 200)을 돌파하는 순간.
*   **시각 효과:** 전체 화면에 **Bright Red** 필터 오버레이가 걸리며, 배경이 미세하게 떨리는 '전기적 노이즈' 효과를 추가합니다.
*   **Alert Box (최대 강조):** 중앙에 크고 굵은 글씨로 다음과 같은 메시지가 플래시(Flashing)됩니다.
    > **🚨 CRITICAL GAP ALERT: IMMEDIATE INTERVENTION REQUIRED.**
    > **[구체적 위협 제시]:** "Your current rate of decline suggests a loss of [X] years of functional capacity within the next 3 years." (현재 기능 저하 속도로 볼 때, 향후 3년 내에 [X]년의 기능 손실이 예측됩니다.)
*   **CTA 연동:** 이 순간, 그래프 하단이나 옆에 'Diagnosis Required' 버튼이 강한 골드톤으로 빛나며 활성화되어야 합니다.

#### 3. 필요한 추가 에셋 (Implementation Assets)

1.  **Iconography Set:** 위험 경고(🚨), 측정기(🔬), 시간 화살표($\rightarrow$) 등 전문적인 느낌의 아이콘 세트 (SVG 포맷 권장).
2.  **Data Visualization Component:** 상기 정의된 'Time Gap Curve'를 구현할 수 있는 반응형 차트 컴포넌트 코드 스니펫 또는 고해상도 SVG 에셋.

---

📊 평가: 완료 — CEO 지시에 따라 불안감 극대화를 위한 인터랙티브 Mockup의 상세한 구조와 디자인 로직을 명확히 정의했습니다.
📝 다음 단계: 개발팀(코다리)에게 이 V1.0 스펙과 시각화 로직을 전달하여, 실제로 작동하는 **프로토타입 구현**을 요청해야 합니다.
