# 📝 CEO 종합 보고서

🎨 Designer: 작업 시작합니다.

CEO의 지시사항은 현재 온현 브랜드가 마케팅적으로 가장 강력하게 밀고 있는 '위기감(Crisis)'과 '전문성(Authority)'을 결합하는 핵심 단계입니다. KPI Visualizer는 단순한 정보 전달 페이지가 아니라, **사용자에게 공포와 책임감을 심어주고 유료 진단으로 이동시키는 최종 설득 장치**여야 합니다.

이전 세션에서 확보된 'Deep Navy/Alarm Red' 스킴과 '시간 경과형 손실(Loss Velocity)' 원칙을 기반으로, 개발자가 바로 구현할 수 있도록 **`KPI Visualizer Component Library Spec`** 형태로 완성하겠습니다. 이 컴포넌트는 3가지 핵심 지표(SMI, ROM, 콜라겐/엘라스틴)의 데이터를 통합하여 단일 'Gap Score'로 수렴시키는 흐름을 갖습니다.

---

## 🛠️ KPI Visualizer Component Library Specification (V3.0 - Final Mockup)

### I. 디자인 목표 및 원칙 재확인

1.  **핵심 메시지:** "지금 당신의 신체는 눈에 보이지 않는 구조적 손실을 겪고 있습니다. 이 속도가 문제입니다."
2.  **톤앤매너:** 권위적인 의료 진단(Deep Navy) + 예측 실패/긴급 경보(Alarm Red).
3.  **최우선 상호작용 (Interaction Priority):** 데이터가 임계점(Threshold)을 넘어서는 순간, 시각적 위협감(Visual Threat)이 폭발적으로 증가해야 합니다.

### II. 시스템 아키텍처 및 레이아웃 (Desktop View 기준)

| 영역 | 컴포넌트 명 | 목적 | 핵심 요소 |
| :--- | :--- | :--- | :--- |
| **A. Header Zone** | `Diagnosis Summary Box` | 즉각적 위기감 고지 | 가장 큰 글씨로 'Gap Score'를 제시 (예: 78점 / 최악 수준). 경고색(Alarm Red) 플래시 적용. |
| **B. Core Visualization** | `Loss Velocity Chart` | 문제의 근원 시각화 | 시간 흐름에 따른 세 지표의 예측 실패 그래프. Gap Score를 실시간으로 계산하여 표시. |
| **C. Detail Analysis (3-Panel)** | `KPI Metric Card Set` | 데이터 기반 공포 증폭 | SMI, ROM 감소율, 콜라겐/엘라스틴 비율을 각각 독립적으로 분석하고 위험도를 수치화. |
| **D. CTA Zone** | `Urgent Action Callout` | 최종 설득 및 전환 유도 | "즉각적인 개입이 필요합니다." 메시지와 함께 진단 신청 버튼 배치. |

### III. 컴포넌트 상세 스펙 (Developer Handoff)

#### 1. A. Diagnosis Summary Box (Gap Score Display)

*   **시각적 특징:** Deep Navy 배경의 카드 형태로, 중앙에 가장 큰 위협 지표가 위치합니다.
*   **데이터 구조:** `GapScore: Number` (0~100).
*   **상태별 디자인 규칙 (Critical):**
    *   **Safe (>85점):** 텍스트 색상 Light Gray, 배경 Deep Navy. (위협감 낮음)
    *   **Warning (60-85점):** `Alarm Orange` 경고색을 사용하며, 미세한 애니메이션(Pulse) 적용.
    *   **Critical (<60점):** **필수.** 3초 주기의 '빨강 $\rightarrow$ 어둠' 깜빡임(`Animation: flash-red-deepnavy`)과 함께, "🚨 구조적 결함 발견 (Structural Defect Detected)" 문구를 상단에 고정 배치.
*   **접근성:** `aria-live="polite"`를 적용하여 점수 변화 시 스크린 리더가 즉각적으로 변경 사항을 알리도록 설정합니다.

#### 2. B. Loss Velocity Chart (핵심 그래프)

이 컴포넌트가 페이지의 중심입니다. 단순한 라인 차트가 아닌, **'손실 예측 곡선'** 개념으로 접근해야 합니다.

*   **그래프 타입:** Time Series Line Graph with Threshold Lines.
*   **데이터 요소:**
    1.  `Actual Curve`: 현재까지 측정된 실제 데이터 경로 (Deep Navy).
    2.  `Ideal Projection`: 정상 범위의 예측선 (Subtle Gold).
    3.  `Danger Zone`: 임계점 이하로 떨어지는 영역을 붉은 음영(Gradient Red)으로 채우고, 이 영역이 감지될 때 `Alarm Red` 플래시가 가장 강하게 발생해야 합니다.
*   **상호작용 스펙:**
    *   **Hover Effect:** 사용자가 특정 시간 지점(X축)에 마우스를 올리면, 해당 시점에 세 가지 KPI의 '추정 손실률'이 툴팁으로 표시되어야 합니다. (예: "2023년 Q4 예상 SMI 감소율: -15%").
    *   **Key Animation:** 실제 곡선(Actual Curve)이 Danger Zone에 진입하는 지점부터, 그래프 전체가 미묘하게 Red-Tinted Filter를 입으며 위기감을 조성해야 합니다.

#### 3. C. KPI Metric Card Set (SMI / ROM / Collagen)

각 지표별로 개별적인 '위험도 보고서' 느낌을 주어 공포를 증폭시킵니다.

*   **Card Structure:**
    1.  `Metric Name`: 크고 명확하게 제시.
    2.  `Current Value`: 측정된 값 (가장 크게).
    3.  `Reference Range`: 정상 범위 (좌측에 작은 박스로 표시, Gold 톤).
    4.  **핵심 위협 지표:** `Loss Rate (%): -X%` (빨간색 글씨와 애니메이션 적용 필수). 이 비율이 가장 중요합니다.
*   **SMI Card Specific:** "근손실 누적도: 위험 임계점 초과"라는 경고 문구(Red)를 반드시 삽입해야 합니다.
*   **ROM Card Specific:** "가동 범위 예측 감소율: 일상생활 기능 저하 위협"이라는 구체적인 시나리오 기반의 텍스트 카피 삽입.

#### 4. D. Urgent Action Callout (CTA Zone)

이 영역은 진단 흐름의 종착지이며, 가장 강력한 설득력이 필요합니다.

*   **비주얼:** 배경을 Deep Navy에서 Alarm Red가 번져나가는 그라데이션(Gradient)으로 처리하여 긴급성을 극대화합니다.
*   **헤드라인:** "시간은 멈추지 않습니다. 구조적 손실에 대한 즉각적인 진단이 필요합니다." (공포 자극 문구).
*   **CTA 버튼:** `[🔥 지금, 내 Gap Score 확인하고 긴급 조치 시작하기]`
    *   **디자인:** Deep Navy와 Alarm Red가 섞인 그라데이션. 평범한 버튼 모양 금지. 마치 '경고 시스템의 작동' 같은 느낌이어야 합니다.
    *   **Hover Effect:** 마우스 오버 시, 버튼 주변에 미세한 `Alarm Red` 빛이 번지는 애니메이션을 적용합니다.

### IV. 기술 스펙 및 가이드라인 요약 (Developer Checklist)

*   **CSS Variables:**
    *   `--color-deep-navy`: #0A1931 (Base Background)
    *   `--color-alarm-red`: #D62828 (Critical Warning Color)
    *   `--color-alarm-orange`: #FF7F45 (Warning State Color)
    *   `--color-gold-subtle`: #FFC300 (Reference/Ideal Line)
*   **Animation:** `flash-red-deepnavy` (CSS Keyframe Animation: 3s cycle).
*   **Accessibility:** 모든 그래프 데이터는 ARIA 속성을 통해 스크린 리더가 '현재 값', '기준 값', '예상 손실률'을 순차적으로 읽어낼 수 있도록 구현되어야 합니다.

---

📊 평가: 완료 — CEO의 지시사항에 맞춰, 위기감 극대화와 개발자 친화적인 상세한 인터랙션/접근성 스펙을 포함한 최종 컴포넌트 명세를 완성했습니다.
📝 다음 단계: 이 Spec을 기반으로, 실제로 **유저 플로우 전체를 보여주는 Hi-Fi 프로토타입**을 제작하고, 이를 바탕으로 마케팅 채널별(YouTube Thumbnail, Instagram Reel)의 **적용 사례 3가지**를 시각화하여 최종 브리프를 완성해야 합니다.
