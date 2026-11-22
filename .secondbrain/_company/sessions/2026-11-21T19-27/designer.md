# 🎨 Designer — MiniFunnel MVP의 최종 사용자 경험(UX)을 완성하기 위해, '불안정한 노이즈 패턴'과 'Deep Navy/Critical Red' 계열의 고화질 배경 애셋 패키지를 제작합니다. 특히, Critical Red로 상태가 전환되는 순간에 사용될 미세한 시각적 디테일(예: 필름 그레인 효과, 디지털 노이즈 플래시)을 정의하고, 이와 관련된 구체적인 색상 코드(Hex Code), 반복 주기(Looping Specification), 그리고 애셋 크기 가이드라인을 개발자에게 전달할 수 있도록 명확하게 정리해 주세요.

🎨 Designer: 작업 시작합니다.

CEO의 지시와 현재 MiniFunnel MVP가 요구하는 '위기감 증폭(Crisis Escalation)' 경험을 극대화하기 위해, 단순한 디자인 브리프를 넘어 개발자가 즉시 활용할 수 있는 **최종 인터랙티브 배경 애셋 스펙**을 정의합니다.

이 패키지는 사용자의 상태 변화에 따라 Background Layer가 겹치고 증폭되는 '레이어드(Layered)' 구조로 설계되어야 합니다.

---

### 🚨 MiniFunnel MVP: Crisis Escalation 배경 애셋 디자인 시스템 (V3.0 Final Spec)

**1. 목표 및 활용 시나리오:**
*   **목표:** 사용자의 Defect ID 진단 상태가 '정상(Deep Navy)'에서 '위기 임계치 돌파(Critical Red)'로 전환되는 순간, 전문적이고 불안감을 유발하는 강력한 시각적 경험 제공.
*   **애셋 타입:** Seamless Looping Video Background (Web/React Component용)

**2. 색상 팔레트 및 정의 (Hex Code 기준):**

| 상태 | 명칭 | Hex Code | 용도/의미 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **Base 0** | Deep Navy (Normal) | `#1A051B` | 기본 배경색. 은은한 전자기 회로 패턴 및 데이터 흐름을 표현. 전문적 신뢰감 부여. | 전체 루프의 베이스 레이어 |
| **Transition** | Warning Blue | `#3F0D48` | 위험 감지 직전 상태. Deep Navy보다 채도가 높아짐. 경고음을 시각화. | 1단계 위기 증폭 (Risk > 50) |
| **Peak Red** | Critical Red (Flash) | `#A3152B` | 시스템 오류 발생 및 임계치 돌파 순간의 색상. 가장 높은 위협감을 유발. | 깜빡임, 오버레이 플래시 전용 |
| **Overlay** | Digital Glitch White | `#FFFFFF` | 노이즈와 글리치 효과가 지나갈 때의 날카로운 하이라이트/플래시 색상. | 대비 극대화 목적 |

**3. 애셋 레이어 구조 및 동작 스펙 (개발자 전달용):**

| 레이어 이름 | 시각적 요소 | 애니메이션/동작 규칙 | 루핑/주기(Specification) |
| :--- | :--- | :--- | :--- |
| **Layer 1: Base Grid** | Deep Navy 배경에 미세한 회로 기판 패턴 (SVG 기반). | 매우 느리고 부드러운 데이터 흐름 애니메이션. 전반적으로 움직임이 적어 안정감을 유지하다가 불안정해지기 시작함. | 무한 루프 (Loop Duration: 10s, Seamless) |
| **Layer 2: Noise/Grain** | 미세한 디지털 노이즈 플래시와 필름 그레인 효과. | 배경 전체에 불규칙적이고 비동기적인(Asynchronous) 진폭의 떨림을 추가. | 루프 주기 무작위 (Randomized Loop): 0.5s ~ 1.5s 간격으로 노이즈 패턴 변화. |
| **Layer 3: Warning Pulse** | `Transition Blue` 색상의 낮은 주파수 깜빡임(Pulse). | 위험 점수가 상승함에 따라 Pulse의 빈도와 강도가 증가 (Frequency & Intensity increase). | 주기적으로 발생하며, Critical Red 진입 시 억제됨. |
| **Layer 4: Crisis Flash** | `Critical Red` 색상의 급격한 깜빡임(Strobe/Flash) 및 오버레이 노이즈. | 시스템 오류가 감지되면 강제로 트리거됨. 빨간색 플래시와 함께 화면 전체에 *수직적* 글리치 라인(`Digital Glitch White`)이 0.1초 동안 스캔되어 지나감. | **Trigger Point:** Risk Score $\ge$ 75% 달성 시 즉시, 비규칙적으로 폭발하듯 발생 (Non-uniform timing). |

**4. 물리적 사양 및 개발 가이드라인:**

*   **권장 해상도:** 1920px $\times$ 1080px @ 30fps 이상
*   **파일 포맷:** `.mp4` 또는 WebGL/Canvas 기반의 CSS 애니메이션 (가장 효율적).
*   **핵심 구현 로직:** 모든 레이어는 **상태 머신(State Machine)**에 의해 제어되어야 합니다.
    1.  `STATE_SAFE`: Layer 1 + Layer 2 (낮은 노이즈)
    2.  `STATE_WARNING`: Layer 1 + Layer 2 + Layer 3 (Pulse 활성화, Intensity 증가)
    3.  `STATE_CRITICAL`: Layer 1 + Layer 2 + Layer 3 + **Layer 4** (Flash 강제 트리거, 모든 레이어의 진폭 최대화).

---

📊 평가: 완료 — CEO가 요구한 기술적 디테일(Hex Code, Looping Spec)까지 포함된 최종 개발 가이드라인을 성공적으로 작성했습니다.
📝 다음 단계: 이 스펙을 바탕으로 실제 배경 영상 에셋 (MP4/GIF 등)을 제작하거나, 개발자에게 전달하여 프로토타입 구현을 시작해야 합니다.
