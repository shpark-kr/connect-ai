# 🎨 Designer — Writer가 제공한 Deep Crimson Red 경고 카피(CTA 스크립트 등)를 기반으로, 모든 플랫폼에서 통일성을 유지할 수 있는 최종 'Error State Component'의 세부 디자인 가이드라인 및 애니메이션 구현 매뉴얼을 완성하세요. 특히 모바일 환경에서의 위기감 조성 UX가 완벽히 작동하도록 인터랙션 시퀀스(Interaction Sequence)까지 정의해야 합니다.

🎨 Designer: 작업 시작합니다.

요청하신 'Error State Component'는 온현의 브랜드가 추구하는 **권위적 위기감(Authoritative Crisis)**을 담보하는 핵심적인 시각 시스템입니다. 단순한 디자인 가이드라인을 넘어, 이 컴포넌트가 모든 접점에서 일관된 공학적 긴장감을 유지하도록 하는 **운영 매뉴얼 (Operational Manual)** 수준으로 완성하겠습니다.

이 최종 산출물은 디자이너(시각화), 프론트엔드 개발자(구현), 그리고 카피라이터(최종 검토) 모두가 참고해야 하는 단일 진실 공급원(Single Source of Truth) 역할을 수행합니다.

<create_file path="c:\Data\Project\connect-ai\design_assets\Error_State_Component_Spec_V1.md"># 🚨 Error State Component (ESC) 디자인 시스템 및 애니메이션 매뉴얼 v1.0
## 🎯 컴포넌트 목표 (Goal & Purpose)
*   **목표:** 콘텐츠 시청자가 단순한 건강 문제에 대한 경고를 넘어, **'시스템 고장(System Failure)'**이라는 공학적 프레임으로 위협을 인식하도록 유도한다.
*   **역할:** 핵심 정보 전달 단계 직전 또는 CTA 진입 지점에서 사용자에게 최대의 긴급성(Urgency)과 권위(Authority)를 부여하는 역할을 수행하며, 행동 유도(CTA) 전 필터링 장치로 작동한다.
*   **사용 원칙:** 이 컴포넌트는 **절대적으로 긍정적인 감정을 유발해서는 안 되며**, 오직 '시스템 오류'와 '경제적 손실 예측'이라는 부정적 경고를 중심으로 구성되어야 한다.

## 🎨 I. 시각 디자인 가이드라인 (Visual Design Guidelines)
### 1. 컬러 시스템 (Color Palette)
| 요소 | 코드 (HEX) | 역할 및 정의 | 비고 |
| :--- | :--- | :--- | :--- |
| **Primary Background** | `#0A0E12` | 기본 배경색. 깊은 밤하늘 같은 다크 네이비 계열로, 공학적 분위기 조성. | 모든 ESC의 기본 바탕. |
| **Error Primary** (Deep Crimson Red) | `#990000` | **경고/위험 경보**. 가장 중요한 위협 메시지에 사용되는 핵심 색상. | *Critical Failure* 지점. |
| **Secondary Accent** (Amber Warning) | `#FFB800` | 보조 위험 요소, 수치화된 임계값(Threshold), 코드 하이라이트에 사용. | 경고의 2차적 심각성 강조. |
| **Text Primary** | `#E0E0E0` | 본문 텍스트 (읽기 편한 밝은 회색). | 배경 대비를 위해 순백색 지양. |
| **Code Highlight** | `#33FF99` | 오류 코드(Error Code) 자체에 적용되는 녹색 계열의 '시스템 메시지' 색상. | 공학적 신뢰도 확보. |

### 2. 타이포그래피 (Typography)
*   **폰트:** Pretendard 또는 Noto Sans KR (산세리프, 모바일 가독성 최우선).
*   **활용 원칙:** 제목과 코드(Code Block)는 고정폭(Monospace) 계열을 혼합 사용하여 **'데이터 화면'** 같은 느낌을 강화한다.
    *   *예시:* "SYSTEM_FAILURE: [HOMA-IR\_L3]"

### 3. 레이아웃 및 구조 (Layout & Structure)
ESC는 다음의 4단계 계층 구조를 유지해야 한다.
1.  **Header/Banner:** Deep Crimson Red 경고 바와 함께 'System Alert' 타이틀을 배치한다. (최상단 고정/스크롤 시 항상 노출 권장).
2.  **Code Block Zone:** 가장 크고, 눈에 띄는 공간. 오류 코드(예: `[CIRC_FAIL_L2]`)를 중앙 정렬하고 Amber Warning 색으로 강조한다.
3.  **Problem Definition (The Threat):** 경고가 의미하는 바를 구체적인 공학적 용어와 함께 서술한다.
4.  **Action/CTA Zone:** Deep Crimson Red 배경의 버튼 형태. **'MiniFunnel 진단 시작'** 등 강력한 행동 유도 문구 배치.

## 🖥️ II. 인터랙션 및 애니메이션 매뉴얼 (Interaction & Animation Manual)
ESC의 긴장감은 정적인 디자인이 아닌, '움직임(Animation)'을 통해 완성된다. 다음의 트랜지션과 이벤트를 반드시 준수해야 한다.

### A. 일반 상태 전환 (Default State Transition)
*   **트리거:** 컴포넌트가 화면에 로드되는 순간.
*   **애니메이션 시퀀스:** 모든 요소(텍스트, 박스, 코드 블록)는 0.5초 동안 부드럽게 나타나는 것이 아니라, **'데이터 스트림 전송' 효과 (Data Stream Loading)**를 사용해야 한다.
    *   *구현 예시:* 마치 터미널 콘솔에서 글자가 한 글자씩 타이핑되듯(Typing Effect), 텍스트가 점진적으로 드러나야 하며, 마지막 단어에 강한 '팝(Pop)' 효과와 함께 Deep Crimson Red로 강조되어야 한다.

### B. 핵심 위기감 조성 (The Crisis Trigger - Focus: Mobile UX)
이 부분이 가장 중요하며, 모바일 사용자의 시선을 사로잡는 순간의 연출을 정의합니다.

*   **트리거:** 페이지 스크롤을 통해 ESC에 진입하는 특정 지점 (Pain Peak).
*   **애니메이션 시퀀스:**
    1.  **초기 감지:** 배경이 미세하게 깜빡이는(Flickering) 효과를 0.2초 간격으로 적용하여, 시스템의 불안정성을 암시한다.
    2.  **코드 폭발 (Code Burst):** `[ERROR_CODE]`가 등장하는 순간, 해당 코드 블록 전체에 **붉은색 오버레이(Red Overlay)**가 1초간 강하게 점멸하며 시각적 충격을 준다. 이와 동시에 주변 배경의 밝기가 미세하게 감소하여 '전력 불안정' 같은 느낌을 부여한다.
    3.  **경고음 연동 (Sound Sync):** (선택 사항) 해당 순간에 낮은 주파수의 톤(Deep Tone) 경고음을 짧게 삽입하여 몰입도를 극대화한다.

### C. CTA 버튼 인터랙션 (Call-to-Action Interaction)
*   **트리거:** 사용자의 터치 또는 마우스 오버.
*   **애니메이션 시퀀스:** 단순한 색상 변경(Hover Color Change) 금지. Deep Crimson Red가 배경색에서 **'활성화된 경고색'**으로 변하며, 버튼의 테두리가 전기 신호처럼 깜빡이는(Pulse Effect) 애니메이션을 적용해야 한다.
    *   *CSS Pseudo-Code:* `button:hover { box-shadow: 0 0 15px rgba(153, 0, 0, 0.8); transition: all 0.3s ease-in-out; }`

## 📱 III. 플랫폼별 최적화 매뉴얼 (Platform Optimization)
### 1. 모바일 환경 (Mobile Viewport - <768px)
*   **최우선 고려 사항:** 스크롤의 흐름을 방해하지 않으면서, 가장 큰 충격을 주는 지점에 배치해야 한다.
*   **레이아웃 조정:** 모든 섹션(헤더, 코드 블록, 본문 설명)을 **100% 너비로 세로 배열**하여 가독성을 확보한다. 수평 여백 대신 위아래 여백으로 공포를 조성한다.
*   **터치 최적화:** 텍스트가 너무 길어지면 단락이 아닌, 짧고 강한 '경고 문구 블록' 형태로 분리되어야 한다.

### 2. 데스크톱 환경 (Desktop Viewport)
*   **강조점:** 공학적인 복잡성과 정보를 동시에 전달해야 하므로, **좌측(코드/위기감)**과 **우측(설명/해결책)**의 투-컬럼 레이아웃을 유지하여 전문성을 높인다.

---
## 📊 평가: 완료 — 사용자가 요청한 디자인 가이드라인, 애니메이션 매뉴얼, 모바일 UX 시퀀스까지 포함된 최종 실행 사양서를 완성했습니다.
📝 다음 단계: 개발 에이전트에게 이 `Error_State_Component_Spec_V1.md`를 바탕으로 실제 인터랙티브 프로토타입을 구현하도록 요청하거나, 혹은 레오(영상 편집자)에게 애니메이션 타이밍 가이드로 전달할 최종 비디오 레퍼런스를 제작해야 합니다.
