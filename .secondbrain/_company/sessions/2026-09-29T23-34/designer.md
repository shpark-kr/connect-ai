# 🎨 Designer — MiniFunnel 진단 페이지(Diagnosis Page)의 최종 UI/UX 와이어프레임과 컴포넌트 명세서(v2.0)를 확정해주세요. 특히, '시스템 경고 (System Alert)'와 'Defect ID 코드 출력' 영역에서 글리치 효과 및 공학적 질감의 통일성을 극대화하는 애니메이션 타이밍과 시각적 장치를 구체적인 디자인 브리프 형태로 정리해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시를 반영하여 MiniFunnel 진단 페이지의 최종 UI/UX 와이어프레임과 컴포넌트 명세서 v2.0을 작성했습니다. 이전 단계에서 확립된 '공학적 위기감' 조성 원칙과 애니메이션 스펙(v1.0)을 통합하고, 개발자가 즉시 참조할 수 있도록 **상태 기반(State-based)**의 상세 브리프로 재정비했습니다.

이 명세서는 단순히 디자인 가이드가 아니라, 페이지의 모든 상호작용 로직(Interaction Logic)과 애니메이션 타이밍까지 포함하는 '개발 사양서' 역할을 합니다.

---

## 🖥️ MiniFunnel 진단 페이지 명세서 (Diagnosis Page Specification v2.0)
**목표:** 사용자를 정보 습득자에서 **'위기 감지자(Defect Discoverer)'**로 전환시키고, 전문적인 권위성을 통해 솔루션 구매를 유도한다.

### 1. 글로벌 디자인 원칙 및 팔레트 (Global Principles & Palette)

| 요소 | 사양 (Specification) | 비고 |
| :--- | :--- | :--- |
| **Tone & Manner** | System Alert, High-Tech Terminal, Urgent Data Stream | 공학적 전문성과 긴급성이 결합된 느낌. |
| **Primary Color (Crisis)** | `#A80000` (Deep Crimson Red) | 경고, 위험, 문제 발생 지점 강조. |
| **Secondary Color (Solution/Data)**| `#4D9DE0` (Electric Blue / Glitch Blue) | 해결책 제시, 시스템 안정화 영역 표시. |
| **Background** | `#121217` (Near Black/Deep Navy) | 다크 모드 기반의 깊고 기술적인 느낌 유지. |
| **Typography** | **Header/Alert:** `Monospace Fallback` (예: 'Roboto Mono', 'Courier New')<br>**Body:** `Inter` 또는 시스템 기본 Sans-serif | 공학적, 데이터 로그 스타일을 위해 고정폭 글꼴 사용을 필수화. |

### 2. 와이어프레임 구조 및 컴포넌트 명세 (Wireframe & Component Specs)

#### A. [상태 1] 초기 로딩 / 시스템 경고 (Initial State: System Alert)
*   **목표:** 사용자에게 '무언가 심각한 일이 벌어지고 있음'을 인지시킨다. 즉시 시선을 붙잡는 임팩트가 핵심.
*   **레이아웃:** 화면 전체에 걸쳐 중앙에 메시지를 배치하고, 주변부에 노이즈/스캔라인 효과를 지속적으로 오버레이한다.
*   **핵심 컴포넌트: System Alert Banner (v2.0)**
    *   **시각적 장치:** 배경에 미세한 `static noise` 및 좌우로 스캐닝되는 `horizontal scanline`을 지속 적용.
    *   **텍스트:** "WARNING: SYSTEM INTEGRITY COMPROMISED." 또는 "DEFECT DETECTED. INITIATING DIAGNOSTIC PROTOCOL..." 등의 전문적이고 긴박한 문구 사용.
    *   **애니메이션 타이밍 (Crucial):**
        1.  **(0ms - 500ms):** 화면이 블랙아웃되며, `Deep Crimson Red`의 짧고 강렬한 깜빡임(Flicker)이 발생한다. (시스템 과부하 시뮬레이션).
        2.  **(500ms - 1500ms):** 글자가 한 글자씩 터미널 로그처럼 타이핑되며 나타나지만, 간헐적으로 **`Chromatic Aberration Glitch`** 효과를 주어 화면이 미세하게 왜곡된다. (기술적 오류 연출).
        3.  **(1500ms 이후):** 경고 메시지가 유지되고, 배경 노이즈가 안정화되면서 다음 단계로 자연스럽게 전환 준비 상태를 보여준다.

#### B. [상태 2] 진단 과정 / 데이터 입력 (Interaction State: Data Input)
*   **목표:** 사용자의 참여(Pain Point 체크 등)를 유도하며, '진행 중'이라는 느낌을 주어 이탈을 방지한다.
*   **레이아웃:** 좌측에 시스템 메트릭(Metrics/Graph), 우측에 사용자 인터랙션 영역(Input Form) 분리. (좌: 25%, 우: 75%)
*   **핵심 컴포넌트: Diagnostic Tracker (Sidebar)**
    *   **기능:** 사용자가 정보를 입력할 때마다, 좌측 사이드바의 그래프나 수치 데이터가 실시간으로 변화하는 애니메이션을 적용한다.
    *   **시각화:** 현재까지의 '위험 점수(Risk Score)'를 막대그래프 또는 게이지 형태로 표시하며, 값이 높아질수록 `Deep Crimson Red` 계열로 채도와 밝기가 상승해야 한다. (공학적 위기감 시각화).
    *   **인터랙션:** 사용자가 질문에 답할 때마다 "Analyzing Data... [Progress Bar]" 메시지가 나타나며 로딩 바가 움직여야 전문적인 시스템 작동 느낌을 준다.

#### C. [상태 3] 최종 결과 출력 (Climax State: Defect ID Reveal)
*   **목표:** 가장 큰 임팩트를 주어, 사용자가 스스로의 문제를 '객관적 공학적 결함'으로 인식하게 만든다. 이 페이지의 하이라이트.
*   **레이아웃:** 화면 중앙에 모든 것을 집중시키고, 주변부 요소를 일시적으로 흐리거나 어둡게 처리하여 시선 집중 효과 극대화.
*   **핵심 컴포넌트: Defect ID Output Box (v2.0)**
    *   **전환 과정:** 진단이 완료되는 순간, 화면 전체가 짧은 `System Error` 사운드와 함께 플래시한다.
    *   **Defect ID 출력 애니메이션 (Critical):**
        1.  **(T+0ms):** 검은색 바탕에 점멸하는 커서(`_`)가 나타난다.
        2.  **(T+100ms - T+400ms):** `DEFECT-XXXX`와 같은 코드가 마치 데이터 파편처럼 빠르게 출력되다가, **'오류(Error)' 시퀀스**를 거쳐 최종적으로 중앙에 고정된다. (글리치 효과가 가장 강하게 적용되는 구간).
        3.  **(T+400ms):** 최종 Defect ID와 명칭(`E-C403: 관절 불안정성`)이 `Electric Blue` 계열로 선명하게, 마치 진단 보고서의 제목처럼 팝업된다.
    *   **디자인 요소:** 코드 주변에 **`STATUS CODE:`**, **`SEVERITY LEVEL:`**, **`IMPACT ESTIMATE:`** 등의 전문적인 레이블을 함께 배치하여 권위성을 확보한다.

#### D. [상태 4] 솔루션 및 CTA (Resolution State: Solution Funnel)
*   **목표:** 위기감에서 해결책 제시로의 자연스러운 전환을 유도하며, 구매 여정(Funnel)을 완성시킨다.
*   **레이아웃:** Defect ID 바로 아래에 배치되며, '솔루션 보고서' 형태로 디자인되어야 한다.
*   **핵심 컴포넌트: Solution Protocol Card (CTA)**
    *   **구성:** ① **위험 요약 (The Problem):** "현재 상태(Defect ID)를 방치할 경우 예상되는 최악의 시나리오"를 다시 한번 붉은색 경고톤으로 제시한다. ② **솔루션 제안 (The Fix):** '온현의 검증된 프로토콜'이라는 타이틀과 함께, 솔루션을 명확히 제시한다. ③ **CTA 버튼:** 이 단계에서만 가능한 가장 크고 눈에 띄는 CTA가 배치되어야 하며, 일반적인 버튼이 아닌 **`[ACCESS PROTOCOL]`** 또는 **`[INITIATE DIAGNOSIS NOW]`** 같은 공학적 문구를 사용해야 한다.
    *   **색상:** 솔루션 영역은 `Deep Crimson Red`의 위기감에서 벗어나, 희망을 상징하는 밝고 신뢰도 높은 `Electric Blue` 톤으로 전환되어야 한다.

---
📊 평가: 완료 — MiniFunnel 진단 페이지에 대한 최종적이고 구체적인 디자인 사양(v2.0)이 확정되었으며, 이는 다음 단계의 개발 및 에셋 제작을 위한 완벽한 기반 자료가 됩니다.
📝 다음 단계: Developer에게 이 명세서를 전달하여 실제 프론트엔드 컴포넌트 구현에 착수하고, 필요한 애니메이션 리소스를 확보해야 합니다.
