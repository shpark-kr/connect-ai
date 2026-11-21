# 🎨 Designer — Instagram이 요청한 크리에이티브 브리프에 맞춰, '시스템 실패 보고서' 컴포넌트의 애니메이션 전환 로직과 실제 적용 예시를 구체화해주세요. 특히, 릴스 영상에서 Defect ID가 제시된 후 시청자가 MiniFunnel 링크로 이동하는 가상 흐름(Flow)을 Deep Navy와 Crisis Red 컬러를 사용하여 단계별 UI/UX 애니메이션 브리프 형태로 제공해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시사항을 완벽하게 이해했습니다. 릴스 영상에서 MiniFunnel로의 전환은 단순한 '클릭' 이상의 **시스템적 경험(Systemic Experience)**이 되어야 합니다. 시청자가 *자발적으로* 진단 테스트를 받게 만드는 것이 목표입니다.

따라서, 저는 Deep Navy와 Crisis Red를 활용하여 **[Defect ID 발견] $\rightarrow$ [긴급 상황 인식] $\rightarrow$ [전문 프로토콜 요구]**의 3단계 흐름을 따르는 애니메이션 전환 로직 및 UI/UX 브리프를 작성했습니다. 이 브리프는 영상 편집팀과 웹 개발팀 모두가 참고할 수 있도록 구체적인 키프레임(Keyframe)와 타이밍 정보까지 포함합니다.

---

## 🚨 [DeepNavy System] MiniFunnel 전환 애니메이션 & UX Flow 브리프 (V7 통합본)

### 📐 전제 조건 및 디자인 시스템
*   **메인 배경색:** `#0A192F` (Deep Navy - 신뢰/전문성)
*   **경고/위기색:** `#E63946` (Crisis Red - 즉각적 위험 감지)
*   **텍스트 색상:** `#FFFFFF` 또는 `#B8C0D0` (은은한 광원 느낌의 흰색)
*   **전환 컨셉:** **[Glitch & Data Stream]** — 정보가 왜곡되었다가 정렬되며, '오류'를 발견하는 과정처럼 연출합니다.

### 🎬 단계별 애니메이션 로직 및 타이밍 (Reels 종료 시점 기준)

| Stage | 시간대 (예시) | 목표/상황 설명 | 비주얼 요소 및 애니메이션 지침 |
| :--- | :--- | :--- | :--- |
| **1. [Climax] 위기감 최고조** | T-2초 ~ T-0초 | 영상의 마지막 순간, Defect ID를 재차 강조하며 해결책이 외부(MiniFunnel)에 있음을 암시합니다. | **[배경]:** Deep Navy (Deep Focus). 화면 전체에 미세한 노이즈(Noise Grain) 오버레이 적용.<br>**[텍스트]:** 중앙에 `FAILURE DETECTED`가 Crisis Red로 크게 깜빡임. 그 아래, 발견된 Defect ID (`M-S7D`)가 마치 스캔되듯이 **녹색/빨간색 픽셀 노이즈와 함께 순차적으로 등장했다 사라지는 글리치 효과**를 적용합니다.<br>**[사운드]:** 낮은 주파수의 '시스템 경고음(Low Frequency Hum)'을 최대화하여 긴장감을 조성. |
| **2. [Transition] 시스템 오류 진입 (The Glitch)** | T-0초 ~ T+1초 | 영상 콘텐츠가 중단되고, MiniFunnel의 공식 포털 화면으로 시각적 연결고리를 만듭니다. *이 과정 자체가 브랜딩입니다.* | **[트리거]:** Defect ID 텍스트 위에 `ACCESSING DIAGNOSTIC PORTAL...`이라는 문구가 나타납니다.<br>**[애니메이션]:** 전체 화면이 짧게(0.1초) 좌우로 번쩍이며 **수평 글리치 효과 (Horizontal Glitch)**를 일으킵니다. 이 순간, 배경색이 Deep Navy에서 미묘하게 더 깊은 색상으로 '딥닝'됩니다.<br>**[사운드]:** 삐-익 하는 고주파의 짧고 날카로운 사운드가 발생하며 화면 전환을 알립니다. |
| **3. [Destination] MiniFunnel 보고서 UI (Initial Load)** | T+1초 ~ T+4초 | 시청자가 도착하는 첫 페이지의 느낌을 줍니다. '당신은 방금 전문가 시스템에 접속했다'는 확신을 심어줍니다. | **[배경]:** Deep Navy 배경 유지. 화면 중앙 상단에 로고와 함께 `System Failure Report v3.1` 배너가 등장합니다.<br>**[핵심 요소]:** 페이지의 최상단에 'Defect ID: M-S7D'를 재확인하는 **Diagnosis Header Box (Crisis Red 테두리)**를 배치하고, 그 아래로 '진단을 시작하려면 다음 정보를 입력해주세요.'라는 명료한 안내 문구를 삽입합니다. <br>**[UX 애니메이션]:** 페이지의 모든 요소(헤더, 경고 박스)가 마치 전원이 켜지듯 **아래에서 위로 부드럽게 (Fade-up Easing)** 나타나야 합니다. |

---

### 🖥️ 실행 가능한 컴포넌트 세부 브리프: [System Alert Box]
이 요소는 MiniFunnel 페이지의 모든 오류 메시지와 CTA 주변에 반복 사용되어 신뢰도를 높입니다.

| 항목 | 상세 스펙 | 기술적 지침 (CSS/Tailwind) |
| :--- | :--- | :--- |
| **Primary Color** | Deep Navy (`#0A192F`) 배경, Crisis Red(`E63946`) 테두리 및 텍스트 하이라이트. | `bg-[#0A192F] border-2 border-[#E63946]` |
| **Corner Radius** | 직사각형 형태를 유지하되, 모서리에 아주 미세한 사다리꼴(Trapezoid) 느낌을 주어 '공식 문서'의 딱딱함을 강조. (Radius: 4px) | `rounded-md` |
| **애니메이션** | **[Focus Glow]**: 박스가 활성화될 때, 테두리를 따라 Crisis Red가 아주 미세하게(0.5초 동안) *호흡하는 듯한* 빛(Glow) 효과를 주어 '경고'의 존재감을 부여합니다. | `box-shadow: 0 0 10px rgba(230, 57, 70, 0.4);` (Active State) |
| **콘텐츠 예시** | `[ERROR: M-S7D - SYSTEM OVERLOAD DETECTED]`. 이 오류 코드를 통해 진단 프로토콜이 필요합니다. |

---

📊 평가: 완료 — 요청하신 전환 로직과 애니메이션 브리프를 구체적인 단계, 색상 코드, 기술적 지침까지 포함하여 완성했습니다.
📝 다음 단계: Instagram/Writer 에이전트와 협업하여 이 UI/UX 컨셉을 적용한 **최종 릴스 영상의 와이어프레임(Wireframe) 또는 프로토타입**을 제작하는 것이 필요합니다.
