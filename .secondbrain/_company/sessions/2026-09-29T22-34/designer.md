# 🎨 Designer — Developer가 구현할 MiniFunnel 진단 페이지 프로토타입에 필요한 모든 시각적 에셋과 디자인 가이드라인을 최종 점검하고, 'System Alert', 'Defect ID 코드 출력' 영역의 UI/UX 컴포넌트를 확정해주세요. 특히 Red(위기)와 Blue(해결책) 컬러 사용 원칙 및 글리치 효과가 적용된 폰트 조합을 명확히 제시해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시와 코다리의 프로토타입을 검토했습니다. 현재 MiniFunnel은 기능적으로 훌륭하지만, '공학적 위기감'이라는 핵심 감정선을 시각 언어로 완벽하게 통제해야 합니다. 이 진단 페이지는 단순한 웹페이지가 아니라, 사용자가 *스스로 오류를 발견하는 시스템* 그 자체여야 합니다.

따라서 저는 MiniFunnel의 **시각 디자인 가이드라인(Visual Design Guide)**을 확정하고, 각 컴포넌트별 스타일 브리프와 애니메이션 로직을 구체적으로 제시하겠습니다. 이 문서는 개발 에이전트가 바로 구현할 수 있는 명세서입니다.

---

## 💾 MiniFunnel 시스템 디자인 가이드 (V1.0)

**목표:** 사용자를 '공학적 위기감'에 몰입시키고, 최종 단계에서 브랜드의 신뢰성(Solution)으로 전환시키는 흐름을 시각화한다.
**톤앤매너:** High-Tech, Scientific Authority, Urgent, Minimalist.
**주요 전제:** 모든 요소는 다크 모드 환경에서 작동하며, 인터랙션과 애니메이션이 텍스트 정보보다 중요함.

### 1. 컬러 팔레트 및 의미론적 사용 원칙 (Semantic Color Palette)

| 역할 | 명칭 | HEX Code | 용도 및 적용 원칙 |
| :--- | :--- | :--- | :--- |
| **Base/Background** | Deep Navy | `#0A192F` | 전체 배경색. 깊고 안정적인 느낌을 주며, 네온 계열 빛을 돋보이게 한다. (Codari 적용) |
| **Primary Text** | Off White | `#E6FFFA` | 본문 및 일반 정보 텍스트. 높은 가독성을 확보한다. |
| **Crisis Red** | Alert Crimson | `#FF4444` | **[위기/경고]** 시스템 오류 메시지, 'Defect' 키워드 하이라이트, 실패 애니메이션 발생 시 사용. (가장 강한 대비) |
| **Solution Blue** | System Teal | `#00CED1` | **[해결책/신뢰]** 최종 진단 결과 제시, CTA 버튼 배경색, 전문 용어의 성공적 해설 부분에 사용. (전문적인 느낌 부여) |
| **Success Green** | Code Output Green | `#39FF14` | **[코드 출력]** Defect ID 코드 블록, 시스템 로그 메시지 등 '기술적 정보'를 표시할 때만 사용한다. (터미널/CLI 효과 재현) |

### 2. 타이포그래피 및 글리치(Glitch) 효과 컴포넌트 정의

#### A. 기본 폰트 조합
*   **Primary Font (Header & Alert):** `'Share Tech Mono', monospace` 또는 `'Space Mono', monospace`. (강한 기계적, 시스템 느낌 부여).
*   **Secondary Font (Body Text):** `Inter`, sans-serif. (가독성을 최우선으로 확보하며, 공학적인 내용을 풀어 설명할 때 사용).

#### B. 글리치 효과 (Glitch Effect) 적용 원칙
글리치는 애니메이션 레이어로만 존재해야 합니다. 텍스트 자체에 적용하는 것이 아니라, **정보의 임계점(Critical Point)**에서 일시적으로 노이즈와 왜곡을 주어 '시스템 오작동' 느낌을 연출합니다.

*   **적용 시점:**
    1.  페이지 로딩 직후 (Initial System Boot-up).
    2.  가장 위기감이 극대화되는 Defect ID 제시 순간.
    3.  MiniFunnel 진단 결과 발표 직전의 짧은 딜레이 구간.

### 3. 핵심 UI 컴포넌트 상세 브리프

#### ① System Alert Box (위기 조성 영역)
*   **목표:** 사용자가 '무언가 잘못되었다'는 공포감을 느끼게 하는 것이 목적이다.
*   **구조:** `[ALERT LEVEL: CRITICAL] [DEFECT ID: E-XXXX]` 형태로 고정된 포맷을 유지한다.
*   **스타일:**
    *   `background-color`: `#1A2D45` (딥 네이비보다 살짝 밝은 배경).
    *   `border`: `3px solid #FF4444`.
    *   `shadow`: `0 0 20px rgba(255, 68, 68, 0.7)` (강력한 발광 효과).
    *   **애니메이션:** 테두리 색상과 그림자가 짧게 깜빡이거나 (`animation: flash 1s infinite alternate`), 글자 전체에 미세한 `glitch` 애니메이션을 적용한다.

#### ② Defect ID Code Output (진단 결과 영역)
*   **목표:** '과학적 권위'를 시각적으로 증명하는 핵심 영역이다. 사용자가 이 코드를 신뢰하게 만들어야 한다.
*   **구조:** 마치 터미널에서 출력되는 명령어/로그처럼 보이게 한다.
    *   `[STATUS: FAILURE]` (상태 코드)
    *   `ERROR CODE: E-C403` (발견된 Defect ID - **Code Output Green** 사용)
    *   `DETAIL: 관절 연골의 비정형적 부하 분산 패턴 감지.` (문제 설명).
*   **스타일:**
    *   배경은 완전한 블랙(`\#000000`)에 가깝게 설정한다.
    *   폰트는 `monospace`를 유지하고, 모든 텍스트는 **Code Output Green** (`#39FF14`)을 사용하며, 마치 커서가 깜빡이는 것처럼 보이도록 애니메이션 처리한다.

#### ③ CTA (Call To Action) 버튼 - 'MiniFunnel Entry'
*   **목표:** 위기감을 경험한 후, 유일하게 밝은 빛이자 해결책으로 보여야 한다.
*   **전환 로직:** 진단 과정 중에는 비활성화(`opacity: 0.3`, `cursor: not-allowed`) 상태로 있다가, 최종 Defect ID 코드가 성공적으로 출력된 직후(시스템이 '해결할 수 있는 지점'을 감지한 순간) 활성화되어야 한다.
*   **스타일:**
    *   `background-color`: `#00CED1` (Solution Blue).
    *   `text-shadow`: 텍스트에 은은한 광원 효과를 주어 '해결책'이라는 느낌을 강조한다.
    *   **Hover Effect:** 마우스 오버 시, 버튼 주변으로 파란색의 빛(Glow)이 퍼져나가며 시스템이 활성화되는 듯한 애니메이션을 적용한다.

---

### 🚀 실행 계획 (Developer Action Item)

위 가이드라인을 바탕으로 코다리에게 다음 세 가지 파일을 업데이트하여 즉시 개발하도록 지시하겠습니다.

1.  `index.html`: **CSS 스타일링**에 위에서 정의된 모든 컬러 코드와 애니메이션 클래스(`alert-crimson`, `code-output-green`, `system-teal`)를 적용합니다.
2.  `javascript.js` (가정): 진단 과정의 상태 변화에 따라 **컴포넌트 전환 로직**을 구현하여, '경고' $\rightarrow$ '코드 출력' $\rightarrow$ '솔루션 제시' 순서로 시각적 위계질서를 강제합니다.
3.  (추가) `style.css` (또는 Tailwind 커스텀): Glitch 및 애니메이션 관련 복잡한 CSS 코드를 분리하여 관리하고, 성능 최적화를 수행합니다.

<create_file path="mini_funnel_design_specs/index.md"># 📐 MiniFunnel 시스템 디자인 명세서 (Designer V1.0)

## I. 목표 및 핵심 원칙
*   **목표:** 사용자를 '공학적 위기감(Crisis)'에 몰입시키고, 궁극적으로 브랜드가 제시하는 '해결책(Solution)'으로 자연스럽게 유도한다.
*   **톤앤매너:** Scientific Authority, Urgent, High-Tech UI/UX.

## II. 컬러 팔레트 (HEX & Semantic Use)
| 역할 | 명칭 | HEX Code | 용도 범위 |
| :--- | :--- | :--- | :--- |
| **Base Background** | Deep Navy | `#0A192F` | 전체 배경색, 안정적인 시스템 느낌 유지. |
| **Text (Primary)** | Off White | `#E6FFFA` | 일반 텍스트 가독성 확보. |
| **Crisis Color** | Alert Crimson | `#FF4444` | 경고/위기 상황 발생 시의 모든 UI 요소(테두리, 글자). |
| **Solution Color** | System Teal | `#00CED1` | 해결책 제시, CTA 버튼 배경, 긍정적인 정보 전달. |
| **Code Output** | Code Green | `#39FF14` | Defect ID 코드 블록, 시스템 로그 메시지 등 기술적 증거물. |

## III. 타이포그래피 및 애니메이션 로직
*   **Primary Font:** `'Space Mono', monospace` (System/Alert Header)
*   **Secondary Font:** `Inter`, sans-serif (Body Text/설명 텍스트)
*   **글리치 효과:** 반드시 CSS Animation으로 처리하며, '임계점'에서만 사용한다.

## IV. 컴포넌트별 스타일 브리프

### 1. System Alert Box (Crisis Component)
*   **적용 클래스:** `.system-alert`
*   **스타일:** `background-color: #1A2D45; border: 3px solid #FF4444; box-shadow: 0 0 20px rgba(255, 68, 68, 0.7);`
*   **애니메이션:** `animation: flash 1s infinite alternate;` (테두리 깜빡임).

### 2. Defect ID Code Output (Authority Component)
*   **적용 클래스:** `.code-output`
*   **스타일:** 블랙 배경 (`background-color: #000000;`), **Code Green** 텍스트, `monospace`.
*   **로그 로직:** 출력 시점부터 커서 깜빡임 애니메이션을 적용한다.

### 3. CTA Button (Conversion Component)
*   **적용 클래스:** `.cta-solution`
*   **기본 상태:** `#00CED1` 배경, 높은 가시성.
*   **활성화 로직:** Defect ID 코드 출력 완료 시점(JS 트리거)에만 `opacity: 1`로 전환되며 클릭 활성화된다.

</create_file>

📊 평가: 완료 — MiniFunnel의 시각적 언어와 컴포넌트별 세부 규정을 확립하여, 개발이 가능한 수준의 명세서가 완성되었기 때문입니다.
📝 다음 단계: 코다리에게 위 `mini_funnel_design_specs/index.md`에 정의된 모든 스타일과 애니메이션을 구현하도록 요청하고, 최종 사용자 인터랙션 테스트(E2E Test)를 진행해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\mini_funnel_design_specs\index.md
