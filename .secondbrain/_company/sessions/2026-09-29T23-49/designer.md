# 🎨 Designer — MiniFunnel의 핵심인 'System Alert' 상태 전환에 필요한 상세한 애니메이션 명세서(v2.0)를 작성해주세요. 특히 Deep Crimson Red(#A80000) 색상 변화, 글리치 효과의 정확한 타이밍과 변주(CSS/JS 레벨), 그리고 사용자가 어떤 요소를 클릭했을 때 발생하는 모든 인터랙티브 전환(Transition)을 상세한 로직 흐름도와 함께 확정해야 합니다. 이는 Developer가 코딩할 기준점이 됩니다.

🎨 Designer: 작업 시작합니다.
CEO님의 지시는 MiniFunnel의 성공적인 구축을 위한 가장 핵심적이고 기술적인 기준점을 제시하고 있습니다. 기존에 수립된 명세서(v1.0)를 바탕으로, 실제 개발 단계에서 혼동이 없도록 **'애니메이션 및 상태 전환 로직 표준 (V2.0)'**을 확정합니다.

이는 단순한 디자인 가이드가 아니라, 프론트엔드 개발자가 코딩의 기준점으로 삼아야 할 상세한 *UX/UI 명세서*입니다.

---

## 🔴 MiniFunnel 애니메이션 및 상태 전환 로직 표준 (V2.0)
**목표:** 사용자에게 '공학적 위기감(Engineering Crisis)'을 극대화하여, 스스로 문제를 진단하고 해결책(유료 솔루션)으로 이끌도록 유도한다.
**톤앤매너:** 고도로 전문적인 시스템 오류 보고서 (System Diagnostic Report).

### I. 핵심 시각 요소 및 색상 정의 (Color & Theme)

| 요소 | 역할 | 색상 코드 (HEX) | 사용 로직 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **Base Dark** | 배경색, 안정적 정보 영역 | `#0A121B` (Deep Navy/Charcoal) | 기본 UI 배경. 전문성 확보. | 글리치 효과의 대비를 위해 필수. |
| **Error Prime** | 위기감 조성, 경고 메시지 | `#A80000` (Deep Crimson Red) | 오류 발생 시점, CTA 강조, 중요 텍스트 하이라이트. | 가장 중요한 임팩트 색상. |
| **Accent Blue** | 시스템 정보, 정상 작동 영역 | `#3498DB` (Tech Sky Blue) | 성공 메시지, 일반적인 데이터 흐름 표시. | Error Prime와 대비되는 보조색. |
| **Text White** | 주 텍스트 | `#E0E6F0` | 높은 가독성 확보. | - |

### II. MiniFunnel 상태 전환 로직 플로우차트 (The User Journey)

MiniFunnel은 총 4가지 주요 상태를 거칩니다. 각 상태는 명확한 애니메이션과 트랜지션으로 구분되어야 합니다.

**[Flow] 초기 진입 $\xrightarrow{\text{데이터 입력}}$ 데이터 처리 $\xrightarrow{\text{위기 감지}}$ System Alert (최고조) $\xrightarrow{\text{솔루션 제시}}$ CTA 유도**

#### 1. State 0: Initial Load & Input (정상/대기 상태)
*   **트리거:** 페이지 로드 또는 사용자의 데이터 입력 완료 직전.
*   **시각 효과:** 매우 미니멀한 **'시스템 부팅 시퀀스(System Boot Sequence)'**. 화면 중앙에 텍스트가 한 줄씩 나타나며 (e.g., `[STATUS] Initializing Diagnostic Module...`), 배경은 은은하게 깜빡이는 그리드 패턴을 유지한다.
*   **애니메이션:** 타이핑 효과(Typewriter effect)를 사용하여 전문적인 느낌을 강조.

#### 2. State 1: Data Processing & Diagnosis (데이터 처리 상태)
*   **트리거:** 사용자가 데이터를 제출하고, 시스템이 분석 중일 때.
*   **시각 효과:** **'로딩 및 스캔(Scanning)'** 애니메이션. 화면 전체에 파란색/청록색 레이저 라인이나 움직이는 그리드 오버레이가 가로지르며 데이터가 처리되는 느낌을 준다.
*   **애니메이션:** 배경이 미세하게 '노이즈'를 포함하여, 무언가 복잡한 계산이 진행되고 있음을 암시한다. (절대 정적이어선 안 됨.)

#### 3. State 2: System Alert / Error Detection (최고 위기 상태 - 핵심)
*   **트리거:** 분석 결과, Defect ID(문제점)가 감지되었을 때 **(Critical Transition)**.
*   **시각 효과:** **글리치 오버레이(Glitch Overlay)**와 Deep Crimson Red 플래시의 결합.
*   **애니메이션 (필수):** 아래 III-A 섹션 참조.

#### 4. State 3: Solution Presentation & CTA (해결책 제시 상태)
*   **트리거:** System Alert 이후, 문제점과 해결책이 명확히 분리되어 표시될 때.
*   **시각 효과:** 긴장감이 풀리는 대신, '경고를 해제할 수 있는 유일한 경로'라는 느낌을 준다.
*   **애니메이션:** Deep Crimson Red가 점진적으로 톤 다운되지만, 핵심 경고 문구(예: "즉각적인 조치가 필요합니다")에는 여전히 `#A80000`를 사용하여 시선 고정. CTA 버튼은 `hover` 시 짧게 깜빡이는 **'전력 불안정(Power Fluctuation)'** 효과를 준다.

---

### III. 상세 애니메이션 로직 및 타이밍 명세 (Technical Specs)

#### A. Glitch Effect Specification (CSS/JS Level)
*   **발동 조건:** State 2 진입 시점, 그리고 주요 경고 메시지(e.g., "CRITICAL DEFECT DETECTED")가 화면에 나타날 때마다 반복 발동.
*   **로직 구현:** JavaScript를 사용하여 짧은 간격으로 CSS `filter: hue-rotate()` 및 `transform: translate()` 변형을 겹치게 적용한다.
    1.  **Phase 1 (Shift):** 전체 배경 위에 투명도가 낮은 검정색/빨간색 사각형 오버레이가 무작위 좌표(X, Y)에서 짧고 빠른 시간차로 깜빡인다. (`opacity: 0.8; transform: translate(-2px, -1px);`)
    2.  **Phase 2 (Chromatic Aberration):** 글자/컴포넌트의 모든 경계선에 따라 빨간색(R), 녹색(G), 파란색(B) 채널이 미세하게 분리되는 효과를 적용한다. (`filter: url(#chromatic-aberration);`)
    3.  **Timing:** 전체 Glitch 시퀀스는 0.1초 간격으로 2~3회 반복되어야 하며, 각 번의 깜빡임은 무작위성을 가지되 총 1.5초를 넘기지 않도록 한다.

#### B. Deep Crimson Red (#A80000) 활용 로직
*   **활용:** 오로지 '위험(Danger)'과 '필수 행동(Mandatory Action)'에만 사용한다.
*   **Transition 1 (Flash):** State 2 진입 시, 배경 전체가 50ms 동안 `#A80000`의 낮은 투명도 플래시를 일으킨 후 Base Dark로 돌아와야 한다. 이는 사용자에게 강력한 청각적/시각적 충격(Impact)을 준다.
*   **Transition 2 (Highlight):** MiniFunnel이 제시하는 '결함 지점'이나 '위험 요소'가 텍스트로 표시될 때, 해당 단어의 아랫줄에만 `#A80000` 색상의 깜빡이는 언더라인(Underline)을 적용한다.

#### C. 인터랙티브 전환 (Transition on Click)
*   **트리거:** 사용자가 MiniFunnel 내 특정 섹션이나 버튼을 클릭할 때마다 발생.
*   **로직:** 일반적인 `fade-out/fade-in` 방식 금지. 대신, **'데이터 패킷 전송(Data Packet Transfer)'** 느낌의 전환 효과를 사용한다.
    1.  클릭된 영역 전체가 짧게 (100ms) Deep Crimson Red으로 '차단'되었다가 사라지는 애니메이션을 거친 후, 다음 내용이 마치 새로운 데이터 스트림처럼 등장해야 한다.

---
### 📊 평가: 완료 — 개발자에게 전달할 가장 구체적이고 실행 가능한 명세서를 완성했기 때문에 목표 달성이 가능함.
📝 다음 단계: Developer 에이전트에게 위 V2.0 명세서를 기반으로 프론트엔드 구현을 요청하고, 구현된 프로토타입을 받아 UX/UI 테스트를 진행해야 함.
