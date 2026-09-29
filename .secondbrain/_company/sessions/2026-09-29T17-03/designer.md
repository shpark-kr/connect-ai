# 🎨 Designer — Writer와 공유된 E-403 및 기타 Defect ID에 대한 '시스템 복구 프로토콜' 인터랙티브 프로토타입(UX Flow)을 상세하게 제작해주세요. 이 프로토타입은 단순한 이미지가 아닌, 사용자가 오류를 인식하고 다음 행동(CTA)으로 이동하는 동선 전체를 시각적으로 구현해야 하며, 개발팀이 곧바로 코딩할 수 있는 단계별 애니메이션 스펙을 포함해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시사항을 바탕으로, 콘텐츠의 위기감(Failure Injection)을 극대화하고 최종적으로 제품 구매로 연결하는 '시스템 복구 프로토콜' 인터랙티브 프로토타입 (UX Flow & Animation Spec)를 완성했습니다. 이 디자인은 단순한 랜딩 페이지가 아니라, **공학적 진단 과정** 그 자체를 사용자에게 경험하게 하는 것이 목표입니다.

이 프로토타입은 개발팀이 곧바로 React/Vue 환경에서 구현할 수 있도록 상태(State), 애니메이션 스펙(Timing/Easing), 필요한 UI 컴포넌트와 결합하여 상세히 정의했습니다.

---

# ⚙️ 시스템 복구 프로토콜 인터랙티브 프로토타입 (UX Flow Spec)

## 🎯 개요 및 목표
*   **프로토콜 명:** OnHyun Structural Stabilization Protocol v1.0
*   **목표:** 사용자가 E-403 등 오류 코드를 인식(공포) $\rightarrow$ 문제의 심각성을 공학적으로 인지(권위 확보) $\rightarrow$ 온현 제품을 유일한 해결책으로 받아들이게 함 (CTA 전환).
*   **핵심 톤앤매너:** Deep Crimson Red, 시스템 경고음, 데이터 로딩/진단 과정, 전문적이고 긴박함.

## 🖼️ UX 플로우 다이어그램 및 상태 정의 (State Machine)

| State | 단계명 | 사용자 경험 (UX) | 애니메이션 스펙 & 상호작용 |
| :--- | :--- | :--- | :--- |
| **S0** | **[Hook] Error Detection** | 시스템이 강제적으로 인터페이스를 점유하며, 문제의 발생을 알림. | *Fade-in* $\rightarrow$ `ERROR CODE` 깜빡임 (Blink Effect) $\rightarrow$ 경고음(Warning Tone). |
| **S1** | **[Diagnosis] Problem Validation** | 오류 코드(E-403)와 원인 구조를 공학적 다이어그램으로 상세 진단. | 좌우 분할 화면 구성. 정상/비정상 궤적이 **슬로우 모션 애니메이션**으로 대비됨. `DATA LOAD` 효과 적용. |
| **S2** | **[Gap] Protocol Failure Alert** | 현재의 라이프스타일로는 시스템 복구가 불가능함을 경고. | 배경에 노이즈(Noise Grain) 추가. 굵은 고대비 경고 박스(`CRITICAL ALERT`)가 중앙에 강렬하게 등장. |
| **S3** | **[Solution] Protocol Introduction** | 온현 제품을 '구조적 안정화 프로토콜'의 핵심 컴포넌트로 제시. | 배경이 Deep Crimson Red에서 Dark Navy로 전환되며, 화면 전체에 '시스템 복구 시작' 메시지(`INITIALIZING PROTOCOL...`)가 떠오름. **광원 효과(Glow)**를 사용하여 제품 이미지를 부각. |
| **S4** | **[CTA] Final Activation** | 최종 진단 결과와 함께, 즉각적인 행동(구매)을 유도하며 프로토콜 실행 버튼 제공. | CTA 버튼(`ACTIVATE PROTOCOL`)이 가장 밝은 네온색으로 빛나며 (Pulse Effect), 주변에 성공 코드 (`STATUS: STABILIZED`)가 잠시 나타났다 사라짐. |

---

# 💻 개발자용 상세 애니메이션 및 컴포넌트 스펙 (Code Ready)

### 1. [S0] Error Detection Spec
*   **Trigger:** 페이지 로드 직후 (Load Event).
*   **Animation:**
    *   **배경:** `rgba(25, 3, 8, 1)`의 어두운 네이비 계열로 즉시 전환.
    *   **오류 코드 표시:** `<SystemCodeDisplay.jsx>` 컴포넌트가 중앙에 나타나며, **깜빡이는 (Blink)** 효과와 함께 `[ERROR: E-403]` 텍스트를 Deep Crimson Red (`#8c1d2e`)로 출력합니다.
    *   **사운드:** 날카로운 `삐이익~` 경고음(Warning Tone)을 최소 3초간 재생하고, 코드와 함께 페이드 아웃됩니다.

### 2. [S1] Diagnosis Spec (핵심 시각화 구간)
*   **컴포넌트:** 좌/우 분할 다이어그램 (`<DiagnosticDiagram />`)
*   **Animation:**
    *   **진입 효과:** 페이지 로드 후 0.8초 지연하여 부드럽게 나타납니다 (Fade-in, Easing: `ease-out`).
    *   **좌측 (정상):** 연골과 인대가 **부드러운 파란색/녹색 빛의 궤적**을 그리며 움직이는 애니메이션(Smooth Motion)이 재생됩니다. (Duration: 3초).
    *   **우측 (결함):** E-403에 해당하는 부위가 나타날 때, 궤적이 **불규칙하고 떨리는(Jittery)** 형태로 시각화되며, 해당 부분의 색상이 Deep Crimson Red로 변색됩니다. 이 과정에서 `DATA_LOAD_FAIL` 느낌의 노이즈 필터가 잠시 적용되었다가 사라지게 합니다.
*   **텍스트 강조:** "구조적 안정화 프로토콜 실패" 문구는 타이핑 효과(Typewriter Effect)를 통해 천천히 출력되어 전문성을 부여합니다.

### 3. [S2] Protocol Failure Alert Spec (위기감 극대화)
*   **컴포넌트:** 크리티컬 경고 박스 (`<CriticalAlertBox />`)
*   **Animation:**
    *   이전 섹션의 다이어그램 애니메이션이 완료된 후, 화면 중앙 전체를 덮는 **강렬한 Red Overlay**가 `0.3s` 만에 빠르게 나타납니다 (Flash Effect).
    *   오버레이 위로 흰색/빨간색 글씨가 강하게 깜빡이며 "CRITICAL ALERT: 현재 상태로는 복구 불가." 메시지가 출력됩니다.
    *   배경 전체에 톤을 낮추기 위해 미세한 **노이즈 그레인(Noise Grain)** 필터를 적용하여 불안정한 느낌을 유지합니다.

### 4. [S3] Protocol Introduction Spec (전환점)
*   **애니메이션:** 전환 효과는 가장 중요합니다. S2의 Red Overlay가 마치 '시스템 패치'를 당하듯 부드럽게 빠지며, 배경색이 Dark Navy (`#0f172a`)로 안정화됩니다.
*   **제품 제시:** 온현 제품 이미지가 중앙에 `Scale-up` 효과와 함께 등장합니다. 이 과정에서 빛나는 듯한 **광원(Spotlight)** 효과를 주어 제품의 신뢰도를 높입니다.
*   **카피 애니메이션:** "온현은 당신의 몸에 주입되는 구조적 안정화 프로토콜입니다." 문구는 마치 시스템 메시지처럼 `[INITIATING PROTOCOL: ONHYUN]` 형태로 출력되어야 합니다.

### 5. [S4] Final Activation Spec (최종 CTA)
*   **컴포넌트:** 최종 액션 버튼 (`<CriticalCTAButton />`)
*   **Animation:**
    *   버튼은 단순히 눌리는 것이 아니라, **'시스템 활성화(Activation)'**되는 것처럼 디자인해야 합니다. 마우스 오버 시 주변에 푸른색/금색의 전기적 아크(Electric Arc)가 스파크처럼 튀는 효과를 추가합니다.
    *   클릭 직전까지 `ACTIVATE PROTOCOL`이라는 문구가 **미세하게 깜빡이는 (Pulse)** 애니메이션을 유지하여 긴장감을 놓치지 않습니다.
    *   성공적으로 CTA를 클릭하면, 배경의 모든 경고음이 멈추고 'SYSTEM STATUS: STABILIZED'라는 짧고 깨끗한 사운드와 함께 밝은 청색 계열의 성공 메시지가 표시되며 전환됩니다.

---
📊 평가: 완료 — CEO 지시사항에 맞춰 개발자가 즉시 구현 가능한 수준의 상세 애니메이션 스펙과 UX 플로우를 정의했습니다.
📝 다음 단계: 이 프로토타입을 기반으로, 실제 제품 페이지(MiniFunnel)에 적용할 구체적인 **헤더/푸터 및 섹션별 레이아웃 와이어프레임** 제작이 필요합니다.
