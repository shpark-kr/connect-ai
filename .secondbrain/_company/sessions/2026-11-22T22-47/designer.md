# 🎨 Designer — Researcher가 제공한 '정상 인슐린 작용' $\rightarrow$ '염증 사이토카인 유입'의 3단계 시퀀스를 구현할 Defect ID 그래프 컴포넌트의 최종 디자인 명세서를 작성해 주세요. 이 명세서는 개발자가 React State 로직으로 읽을 수 있도록, CSS 변수와 애니메이션 단계별(Step-by-step) 인터랙션 상세 스펙을 포함해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시에 따라, '정상 인슐린 작용'에서 '염증 사이토카인 유입'으로 변이하는 과정을 시각화할 **Defect ID 그래프 컴포넌트(v2.0)**의 최종 디자인 명세서를 작성했습니다. 이 스펙은 개발팀이 React State 로직을 기반으로 애니메이션과 인터랙션을 구현하는 데 최적화되어 있습니다.

---

## 🔬 Defect ID Graph Component Spec Sheet (v2.0)
**목표:** 인슐린 저항성 및 만성 염증의 메커니즘을 과학적으로 설명하며, 사용자에게 '시스템 오류'라는 위협감을 극대화한다.
**기술 스택 가정:** React State 기반 컴포넌트, CSS Variables를 이용한 동적 스타일링 및 애니메이션 제어.
**브랜드 준수 요소:** 다크 네이비 배경(`--color-bg-primary`), 골드 강조색(`--color-accent-gold`), 위험 경고색(앰버/레드).

### 1. 컴포넌트 구조 개요 (Conceptual Architecture)

| 섹션 | 내용물 | 역할 및 목적 |
| :--- | :--- | :--- |
| **A. 배경 & 레이아웃** | 다크 네이비(`--color-bg-primary`) 바탕의 시스템 맵 형태. 복잡한 생명과학 이미지를 단순화된 '시스템 플로우차트'로 재해석. | 전문성과 신뢰도 극대화. 눈에 보이는 흐름(Flow)을 통해 이해도를 높임. |
| **B. 핵심 요소 (The Core)** | 인슐린 분자, 수용체, 염증 세포(Macrophage), 사이토카인 입자 등의 3D/애니메이션 벡터 그래픽. | '시스템 오류'의 주체를 시각화하고, 흐름 변화에 따른 위협을 체감하게 함. |
| **C. 스토리텔링 플로우** | Step 0 (정상) $\rightarrow$ Step 1 (저항성 발생) $\rightarrow$ Step 2 (염증 유입). 이 세 단계가 순차적으로 애니메이션되어야 함. | 사용자 몰입도를 높이고, 콘텐츠의 논리적 흐름을 강제함. |

### 2. 상태별 인터랙션 및 애니메이션 스펙 (State-by-State Animation Logic)

이 컴포넌트는 **`data-step="{0|1|2}"`** 속성을 통해 개발자가 State를 제어할 수 있도록 설계합니다. 각 단계 전환 시, 다음의 변화가 순차적으로 발생해야 합니다.

#### Step 0: 정상 인슐린 작용 (Baseline / Healthy)
*   **시각화:** 혈액(혈류 경로)을 따라 움직이는 규칙적이고 균일한 **인슐린 분자 입자** 애니메이션.
*   **핵심 이벤트:** 인슐린이 수용체에 결합하고, 세포 내부로 신호가 전달되어 포도당 흡수가 원활하게 일어나는 플로우를 보여줌.
*   **애니메이션 로직:**
    *   `--color-insulin-flow`: 밝고 깨끗한 골드빛(`rgba(255, 214, 0, 0.8)`) 사용.
    *   `animation-duration: 3s;` (부드럽고 규칙적인 흐름).
    *   **State:** Stable / Normal.

#### Step 1: 인슐린 저항성 발생 (The Defect Initiates)
*   **시각화 변화:** 정상적인 흐름이 방해받기 시작함. 수용체 표면에 **'방어막/장벽'** 같은 시각적 장애물이 형성됨.
*   **핵심 이벤트:** 인슐린 분자가 수용체에 접근하지만, 결합 효율이 떨어지거나 신호 전달 경로가 막히는 현상(저항성)을 표현해야 함.
*   **애니메이션 로직 (Transition from Step 0 $\rightarrow$ Step 1):**
    1.  **(Failure Signal)** 인슐린 입자의 속도와 규칙성이 점차 느려지고 불규칙해짐. (`--speed-modifier: 0.5;`)
    2.  **(Blockage)** 수용체 근처에 미세한 **'교란 파동(Disruption Wave)'**이 나타나며, 인슐린 분자가 이 파동을 통과할 때마다 시각적으로 에너지를 잃는 효과를 부여함. (`opacity` 및 `transform: scale()` 변화 활용).
    3.  **State:** Warning / Stalled.

#### Step 2: 만성 염증 사이토카인 유입 (The Defect Escalates)
*   **시각화 변화:** 가장 극적이고 경고성이 높은 단계. 배경색의 미세한 노이즈(Noise Grain)가 증가하고, 흐름 자체가 '혼란' 상태로 변함.
*   **핵심 이벤트:** 방치된 시스템에서 염증성 대식세포(Macrophage)가 활성화되어 **사이토카인 입자**를 분비하며, 이 사이토카인이 인슐린 경로와 결합하여 추가적인 손상을 일으키는 과정. (Positive Feedback Loop).
*   **애니메이션 로직 (Transition from Step 1 $\rightarrow$ Step 2):**
    1.  **(Inflammatory Burst)** 시스템 전체에서 무작위적이고 불안정한 **빨간/주황색 입자(Cytokine)**가 폭발적으로 분사되기 시작함. (`--color-cytokine: #ff4d4d;`)
    2.  **(Cross-Talk)** 이 사이토카인 입자가 Step 1의 '방어막'을 무너뜨리고, 인슐린 수용체와 직접 상호작용하여 결함을 심화시키는 애니메이션(예: 충돌 효과)이 필수적임.
    3.  **State:** Critical / Defect Confirmed.

### 3. 개발자를 위한 기술 명세 (Developer Blueprint)

#### A. CSS Variables 정의 (Global Scope)
```css
/* --- Color Palette --- */
--color-bg-primary: #0a192f; /* Dark Navy Background */
--color-text-main: #e6fffa;   /* Light Teal Text */
--color-accent-gold: #ffc300; /* Healthy/Normal State Highlight */
--color-warning: #ffd700;     /* Step 1 - Stalled Warning */
--color-critical: #cc0000;    /* Step 2 - Cytokine Danger Red */

/* --- Animation Variables --- */
--transition-speed: 1.5s; /* Overall transition duration for steps */
--flow-intensity-step0: 1;  /* Step 0 Flow Intensity (Max) */
--flow-intensity-step1: 0.3; /* Step 1 Flow Intensity (Reduced) */
--flow-intensity-step2: 0.8; /* Step 2 Flow Intensity (Chaotic/High energy) */
```

#### B. 컴포넌트 구조 및 클래스 예시 (React State Integration)
개발자는 다음과 같은 `useState`와 `useEffect`를 사용하여 애니메이션을 순차적으로 트리거해야 합니다.

**[Pseudo-Code Logic]**
```javascript
const [currentStep, setCurrentStep] = useState(0); // 0 -> 1 -> 2
// Step 변경 시 CSS 클래스 및 데이터 속성 업데이트
<div className={`defect-id-graph step-${currentStep}`} data-step={currentStep}>
    {/* A. Flow Container (Animation Target) */}
    <div className="insulin-flow" style={{ '--flow-intensity': flowIntensity }}> 
        {/* SVG or Canvas rendering of particles/wave */}
    </div>

    {/* B. Defect Visualizer (State Specific Overlay) */}
    {currentStep === 1 && <DefectBlockageOverlay />}
    {currentStep === 2 && <CytokineInfluxSystem(color={critical}) />}
</div>
```

### 4. 결론 및 기대 효과

이 명세서에 따라 구현된 Defect ID 컴포넌트는 단순한 정보 전달을 넘어, **사용자가 인체 내부에서 발생하는 '시스템적인 위협'을 직접 체험하게 만드는 몰입형 교육 콘텐츠**가 될 것입니다. 이는 콘텐츠의 전문성을 극대화하고, 자연스럽게 다음 단계인 리드 마그넷(Defect ID 진단 체크리스트) 다운로드로 연결하는 가장 강력한 시각적 근거 자료 역할을 수행할 것입니다.

---
📊 평가: 완료 — CEO님의 지시에 따라 개발자가 즉시 구현 가능한 수준의 기술 명세서를 완성했기 때문에 목표가 달성되었습니다.
📝 다음 단계: Researcher에게 이 디자인 스펙에 맞춰 사용할 수 있는 **정확한 과학 용어 및 데이터 포인트(예: 사이토카인 종류, 인슐린 저항성의 임계점)**를 최종 검증받아 전달받아야 합니다.
