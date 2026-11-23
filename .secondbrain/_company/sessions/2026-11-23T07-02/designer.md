# 🎨 Designer — Researcher가 제공할 새로운 데이터를 기반으로, '시간 경과형 손실(Time Gap)'을 시각화하는 모듈식 UI 컴포넌트 세트 3가지(예: 그래프 형태, 누적 비용 차트 형태, 비율 하락 인디케이터 등)의 디자인 스펙 및 와이어프레임을 제작해 주세요. 이 디자인은 추후 콘텐츠에 즉시 적용할 수 있도록 재사용 가능한 형태로 정의되어야 합니다.

🎨 Designer: 작업 시작합니다.

CEO 지시에 따라, Researcher가 제공한 생물학적/생리학적 위험 데이터(hs-CRP, 근감소증)를 '시간 경과형 손실(Time Gap Loss)'이라는 핵심 프레임워크로 시각화할 수 있는 **모듈식 UI 컴포넌트 세트 3가지**의 디자인 스펙 및 와이어프레임을 제작했습니다.

이 모듈들은 단순한 그래프가 아니라, 데이터가 위협적인 '위험 영역(Danger Zone)'으로 진입하는 과정 자체를 시각적으로 극대화하여, 사용자에게 **'지금 당장 측정하고 행동해야 한다'**는 긴급성(Urgency)과 통제감(Control)을 동시에 부여하도록 설계되었습니다.

---

### 🛠️ Time Gap Loss Visualization Component Suite (3종)

#### **Component 1: Degradation Slope Indicator (퇴행 기울기 지표)**
*   **목적:** 근력, 기능성 등 '속도'로 감소하는 신체 능력을 직관적으로 보여줌. (Sarcopenia에 최적화)
*   **원리:** 시간이 흐름에 따라 측정된 값(Y축)이 하락하는 추세를 시각적인 '기울기'와 '꺾임점'으로 표현합니다.
*   **디자인 스펙:**

    1.  **형태:** 시간 축을 가로지르는 3D 느낌의 곡선 그래프 (Line Chart).
    2.  **색상:** 과거(Past)는 안정적인 청록색 계열 $\rightarrow$ 현재(Present) 측정 값은 경고를 나타내는 주황색/노란색 $\rightarrow$ 예측된 미래 위험 구간은 강한 적갈색으로 하강하는 추세선을 표시합니다.
    3.  **인터랙션:** 사용자가 슬라이더로 연도를 조절하면, 그래프의 기울기가 실시간으로 변하며 '위험 경고' 텍스트 박스가 함께 활성화됩니다.

    ```css
    /* CSS/Tailwind Pseudo-Code Snippet */
    .degradation-slope {
      position: relative;
      padding-bottom: 100%; /* 정사각형 비율 유지 */
      background: linear-gradient(to top, #fef2f4, transparent); /* 위험 영역 배경 처리 */
    }

    /* 기준선 (Benchmark Line) - 건강한 상태를 상징 */
    .benchmark-line {
      position: absolute;
      top: 5%; 
      left: 0;
      width: 100%;
      height: 2px;
      background-color: var(--color-healthy, #6ee7b7); /* 에메랄드 */
    }

    /* 실제 측정값 추이 (The Gap) - 하락 기울기를 강조 */
    .actual-curve {
      fill: none;
      stroke: var(--color-danger, #ef4444); /* 레드 */
      stroke-width: 4px;
      /* keyframe animation for gradual decline visualization */
      animation: slope-down 1s ease-out forwards; 
    }
    ```

#### **Component 2: Future Loss Accumulator Chart (미래 손실 누적 비용 차트)**
*   **목적:** 건강을 지키지 않았을 때 '경제적/시간적'으로 얼마만큼의 손실이 쌓이는지를 화폐나 시간 단위로 직관화. (가장 강력한 동기 부여 유도)
*   **원리:** 현재의 작은 습관이나 방치된 문제가 미래에 큰 비용(Cost)으로 누적되는 과정을 시각적인 '쌓임' 효과로 보여줍니다.
*   **디자인 스펙:**

    1.  **형태:** 시간 축을 가로지르는 '누적 막대 차트(Stacked Bar Chart)' 형태를 변형합니다. (일반적인 막대 그래프가 아닌, 시계열적 쌓임 느낌).
    2.  **시각화 요소:** 세 가지 색상 블록으로 구성됩니다: [A] 초기 비용/시간 손실 (주황색) $\rightarrow$ [B] 복리 이자 효과/증폭된 위협 (노란색) $\rightarrow$ [C] 치명적 임계점 돌파로 인한 최종 비용 (짙은 적갈색).
    3.  **메시지:** 차트의 막대가 끝나는 지점에 "현재 방치 시, 10년 후 예상 손실액: OOO원"과 같은 구체적인 문구를 고정 배치합니다.

    ```css
    /* CSS/Tailwind Pseudo-Code Snippet */
    .loss-accumulator {
      display: flex;
      align-items: flex-end; /* 바닥부터 쌓이는 효과 */
      height: 300px;
      width: 100%;
    }

    /* 막대 요소 (시간 단계별 누적) */
    .loss-segment {
      flex-grow: 1;
      margin: 0 5px;
      position: relative;
      transition: height 0.5s ease-out; /* 동적인 변화 강조 */
    }

    /* 손실 비용 (Loss Cost) - 가장 높은 위험 단계의 색상 지정 */
    .cost-c {
      background-color: var(--color-critical, #9d174d); 
      z-index: 3;
    }
    ```

#### **Component 3: Target Zone Deviation Gauge (목표 영역 이탈 게이지)**
*   **목적:** 혈압, 특정 마커 수치 등 '범위'를 벗어나는 정도(Deviation)를 즉각적으로 측정하여 보여줌. (hs-CRP에 최적화)
*   **원리:** 원형 다이얼 게이지(Radial Gauge) 방식을 채택하되, 단순한 바늘 움직임 대신 '색상 변화의 급격함'과 '데이터 파열 효과(Glitch Effect)'를 결합합니다.
*   **디자인 스펙:**

    1.  **구조:** 원형 다이얼을 배경으로 하며, 게이지는 세 개의 영역으로 명확히 나뉩니다: [Green] 정상 범위 (Safe Zone) $\rightarrow$ [Yellow] 주의/경계 범위 (Warning Zone) $\rightarrow$ [Red] 위험 임계점 돌파 (Critical Failure).
    2.  **핵심 시각화:** 측정 값이 경계를 넘어 Red 영역에 진입할 때, 게이지의 배경과 바늘 주변에 **디지털 노이즈 필터(Noise Overlay)**가 짧게 적용되고, 수치 위에 '!!!CRITICAL !!!' 같은 텍스트가 플리커링 효과와 함께 오버레이됩니다.
    3.  **사용자 피드백:** 사용자가 이 게이지를 볼 때마다 "당신의 몸이 보내는 경고 신호"라는 내러티브로 연결되어, 측정 및 솔루션 탐색 행동으로 유도합니다.

---

### 📊 평가: 완료 — CEO가 요청한 '시간 경과형 손실'에 초점을 맞춘 재사용 가능한 모듈식 컴포넌트 세트를 구체적인 디자인 스펙과 구조화된 와이어프레임 가이드라인까지 포함하여 완성했습니다.
📝 다음 단계: 이 3가지 컴포넌트 세트를 기반으로, 가장 시급성이 높은 **'근감소증(Sarcopenia) 및 기능 저하'** 테마를 선정하여, Component 1 (Degradation Slope Indicator)을 활용한 실제 Mockup 템플릿을 제작해야 합니다.
