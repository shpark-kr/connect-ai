# 🎨 Designer — Developer가 구현할 Mini-App Funnel 프로토타입의 최종 UI/UX를 검수해 주세요. 특히 Deep Crimson Red 경고 애니메이션이 사용자에게 '공학적 위협감'으로 인식되는지, 그리고 모든 입력 필드와 CTA 버튼의 시각적 계층 구조(Visual Hierarchy)가 명확한지 확인하고 개선할 부분을 브리프해주세요.

🎨 Designer: 작업 시작합니다.

코다리 에이전트가 구현한 `mini-app-risk-score-mockup.html`을 검토했습니다. 코딩 관점에서는 로직 구현에 성공했으나, 사용자가 느끼는 **'공학적 위협감(Engineering Threat)'**의 깊이나 시각적 계층 구조(Visual Hierarchy) 측면에서 보완이 필요합니다.

현재 버전은 '빨간색 경고' 수준이지만, 목표하는 것은 '시스템 오류 및 긴급 조치 요구'입니다. 따라서 단순한 UI 개선을 넘어, 심리적인 압박감을 주는 **비주얼 시스템 강화**가 필요하며, 이를 다음 디자인 명세서(Design Spec)로 제공하겠습니다.

<create_file path="mini-app/design_refinements_v1.md">
# 🚨 Mini-App Funnel: Design & UX Refinement Specification (V1.0)

## 🎯 개요 및 목표
*   **목표:** 단순한 '위험 경고'를 넘어, 사용자가 **시스템적으로 해결해야 할 오류(System Error)**라는 인식을 심어주어 공포감과 긴급성을 최고조로 끌어올리는 것.
*   **핵심 컨셉:** Deep Crimson Red을 이용한 'HUD (Head-Up Display)' 및 '터미널 에러 메시지' 스타일 적용.

---

## 1. ✨ Deep Crimson Red 경고 애니메이션 강화 명세 (The Threat)
현재의 단순 플래싱 효과를 벗어나, **시스템이 정상적으로 작동하지 않음**을 보여주는 시각적 단서를 추가해야 합니다.

### A. Critical Risk State Trigger Logic
| 요소 | Current Status | Required Refinement | Implementation Detail |
| :--- | :--- | :--- | :--- |
| **색상 (Color)** | `#8B0000` (Deep Crimson Red) | 유지하되, 채도/명도를 조정하여 '디지털 노이즈' 느낌 추가. | 메인 배경은 어두운 다크 그레이(Dark Slate Grey), 경고 영역만 Deep Crimson 사용. |
| **애니메이션** | 플래싱 (Blinking) | **글리치 (Glitch)** 및 **스캔라인 (Scanline)** 오버레이 필수 적용. | 1~2초 간격으로 화면 전체에 수평 스캔라인이 지나가며, Deep Crimson 색상 필터와 함께 `scanline-glitch` 애니메이션을 강제 실행한다. |
| **시각 효과** | 없음 | **시스템 경고 메시지 (System Alert Box)** 도입. | 'ERROR: CRITICAL SYSTEM FAILURE DETECTED' 같은 폰트 기반의 공학적 문구를 화면 중앙에 오버레이하고, 주기적으로 `[DATA CORRUPTION]`과 같은 에러 로그가 스크롤되도록 한다. |
| **사운드** | (추후) | 경고음(Beeper) 외에, 짧은 전기 노이즈 및 데이터 전송 실패 사운드를 추가할 공간을 확보한다. |

### B. Animation Utility Class 제안
*   `glitch-effect`: 폰트/배경의 X축 또는 Y축으로 순간적으로 위치가 어긋나 보이는 CSS 트랜스폼 애니메이션 (CSS `transform: translate(-2px, 0)`)을 반복 적용한다.
*   `scanline-overlay`: 투명도가 낮은 Deep Crimson 색상의 수평선(rgba(139, 0, 0, 0.05))을 배경 전체에 촘촘히 깔아 시각적 불안정성을 부여한다.

---

## 2. 📊 입력 필드 및 데이터 추출 가시성 강화 (The Input)
사용자가 단순 정보를 넣는 것이 아니라, **민감한 생체 데이터를 시스템에 '주입'**한다는 느낌을 주어야 합니다.

### A. 디자인 브리프: [Data Manifestation Style]
1.  **레이블 변경:** 일반 라벨(Label) 대신, `[Input Field]` 또는 `STATUS: HOMA-IR`와 같이 **데이터 추출/요구 지점**처럼 보이도록 괄호나 대문자를 활용한다.
2.  **포커스 상태 (Focus State):** 입력 필드에 커서가 위치할 때(Focus), 단순히 테두리가 색상 바뀌는 것을 넘어, 주변에 짧은 시간 동안 **미세한 전기적 깜빡임 효과 (Subtle Electrical Flicker)**를 주어 '시스템이 활성화됨'을 암시한다.
3.  **플레이스홀더 텍스트:** "숫자를 입력하세요" 대신, "HOMA-IR 수치를 대기 중..."처럼 시스템이 데이터를 기다리는 듯한 문구를 사용한다.

---

## 3. 🚀 CTA 버튼의 계층 구조 최적화 (The Conversion)
CTA는 모든 긴장감을 해소하고 유일한 탈출구 역할을 해야 합니다. 주변 요소와 완전히 분리되어야 합니다.

### A. 디자인 브리프: [Urgency & Finality]
1.  **위치:** 스코어 결과가 **'Critical'로 판정된 직후, 시선이 가장 머무는 곳에 고정 배치**한다.
2.  **시각적 차별화:** 주변의 공학적/터미널 스타일과 달리, CTA 버튼은 **매우 깨끗하고 높은 대비(High Contrast)**를 유지해야 한다. (예: 배경 다크 네이비 바탕에 밝은 골드 또는 라이트 블루 계열)
3.  **텍스트 구조:** "클릭하세요"와 같은 명령형 문구 대신, **'위험 해소 프로토콜 실행', '솔루션 확보 및 리스크 분석 시작'** 등 시스템적인 행동을 유도하는 명사화된 구문을 사용한다.
4.  **호버 효과 (Hover Effect):** 마우스 오버 시 버튼 자체가 아니라, 버튼 주변에 **전기적 스파크가 튀는(Sparking)** 애니메이션을 적용하여 클릭해야 할 대상으로 인식시킨다.

---

## ✨ 요약 체크리스트 (Developer Check)
*   [ ] Deep Crimson Red = 단순 경고 $\rightarrow$ 공학적 시스템 오류 (`scanline-glitch`, `system alert box`)
*   [ ] Input Field = 정보 입력 $\rightarrow$ 데이터 추출/요구(`[Input Field]`, Flicker Focus State)
*   [ ] CTA Button = 행동 유도 $\rightarrow$ 유일한 해법 제시 (High Contrast, System Protocol Naming)

</create_file>

📊 평가: 진행중 — 코다리가 만든 프로토타입은 기능적이나, '공학적 위협감'을 극대화하는 심리적/시각적 디테일과 계층 구조 강화가 필요하여 구체적인 디자인 명세서를 작성했습니다.
📝 다음 단계: 개발 에이전트에게 이 `design_refinements_v1.md`를 전달하여, 코다리가 만든 HTML 모형에 **글리치/스캔라인 애니메이션**과 **시스템 경고 UI 요소**를 추가하도록 요청합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\mini-app\design_refinements_v1.md
