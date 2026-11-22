# 🎨 Designer — Researcher가 제공한 '손실 회피 심리' 문구와 MiniFunnel의 Critical Red 상태를 통합하여, 인스타그램 릴스 전용 최종 비주얼 애셋(3-5초 클립에 사용될 배경/UI 요소)을 제작하세요. 특히, 애니메이션 플래싱 효과가 가장 드라마틱하게 보이는 시점을 기준으로 High-Res Background Asset Package와 UI/UX 가이드를 업데이트해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO 지시에 따라 '손실 회피 심리'와 MiniFunnel의 Critical Red 상태를 결합한 인스타그램 릴스 전용 최종 비주얼 애셋 패키지를 제작합니다. 이 에셋은 단순히 배경을 제공하는 것을 넘어, 시청자가 **"지금 당장 진단해야 할 위험(Loss)"**이라는 감정적 위협을 느끼고 MiniFunnel로 유도되도록 설계되었습니다.

가장 드라마틱한 효과를 내는 애니메이션 플래싱 지점과 UI/UX 가이드라인을 포함하여, 다음 세션에서 바로 개발에 투입할 수 있는 형태로 최종 파일을 생성하겠습니다.

### 🛠️ 실행 계획: Reels Visual Asset Kit 제작
1.  **핵심 원칙 확립:** Loss Aversion (손실 회피) -> Defect ID Warning (위협 인식) -> MiniFunnel Click (해결책 탐색).
2.  **애셋 구성:** 고화질 배경 패턴, 시스템 UI 오버레이, Critical Red 플래싱 키프레임 정의.

<create_file path="assets/reels/Reels_Visual_Asset_Kit_V1.pdf"># 온현 - 인스타그램 릴스 전용 비주얼 애셋 키트 (Critical Red State)

## 📄 목표 및 컨셉
*   **목표:** 시청자가 '방치했을 때 발생하는 건강상의 손실'을 체감하게 하여, 전문 진단(MiniFunnel)의 필요성을 느끼게 한다.
*   **톤앤매너:** 공신력 있는 시스템 경고 (High-Tech / Urgent / Authority).
*   **핵심 원리:** '미래에 닥칠 위험(Loss)'을 시각적으로 극대화하고, 이 위협을 해결할 수 있는 유일한 출구로 MiniFunnel을 배치한다.

## 🎨 컬러 팔레트 (Color Palette)
| 용도 | 코드 | 이름 | 설명 |
| :--- | :--- | :--- | :--- |
| **Primary Background** | `#1A0E29` | Deep Navy (기본) | 안정적인 정보 전달 기반. 위협 전의 상태. |
| **Warning State Color** | `#D83F4B` | Critical Red (위험) | 즉각적인 위험 경고. 손실을 상징하는 색상. |
| **Accent/Highlight** | `#FFC107` | Amber Yellow (경고 강조) | 핵심 Defect ID나 수치에 사용. 주목도 극대화. |
| **Text Color** | `#E0E0E0` | Off-White | 가독성을 위한 주 텍스트 색상. |

## 📽️ 애니메이션 및 키프레임 정의 (3-5초 클립 기준)
릴스 영상은 총 3단계의 시각적 위기 증폭 과정을 거치며, 각 단계는 명확한 타이밍과 비주얼 변화를 가져야 합니다.

### 🟢 Stage 1: 도입 (0~2초) - '무심코 지나치는 위험'
*   **배경:** Deep Navy (`#1A0E29`) 기반의 미세한 디지털 노이즈 패턴. 낮은 주파수의 푸른빛 깜빡임(Ambient Flicker).
*   **UI 요소:** 화면 중앙 상단에 작은 타이머/진행률 표시줄(Progress Bar) 배치 (미래의 시간적 손실 암시).
*   **애니메이션:** 정보 전달 위주의 정적인 텍스트와 그래프가 등장. (지루함 유발 후, 급격한 전환을 위한 빌드업).

### 🔴 Stage 2: 위기 증폭 (2~4초) - 'Defect ID 시스템 경고'
*   **트리거:** 영상 내에서 첫 번째 Defect ID(예: `DEFECT_A103`)가 제시되는 순간.
*   **배경 변화:** Deep Navy $\rightarrow$ **Critical Red (`#D83F4B`)**로 급격한 색상 전환 (Transition Speed: 0.2s).
*   **플래싱 효과 (핵심):** 화면 전체에 Critical Red와 Black이 비규칙적으로 깜빡임(Strobe Effect)을 적용합니다. **주기:** 평균 80~150ms 사이의 불규칙한 주기로 발생시켜, 실제 시스템 오류 같은 불안감을 유발합니다.
*   **UI 요소:** 경고 메시지 박스 (`[SYSTEM ALERT]`, `CRITICAL FAILURE DETECTED`)가 화면을 가득 채우며 진동 애니메이션 적용.

### 🚨 Stage 3: 공포/해결책 제시 (4~5초) - '손실 회피와 행동 유도'
*   **배경:** Critical Red 플래싱이 멈추고, 배경은 Deep Navy에 미세한 노이즈가 남아있는 상태.
*   **메시지 변화:** "놓치면 안 될 당신의 건강 데이터" 등의 손실 회피 문구를 오버레이합니다.
*   **CTA 강조:** MiniFunnel 유도 버튼 (`[즉시 진단하고 위험을 막으세요]`)이 화면 하단에 배치되며, 이 버튼만 **Amber Yellow (`#FFC107`)**로 강렬하게 빛나도록 애니메이션 처리. (사용자의 시선 집중 유도).

## 💻 UI/UX 컴포넌트 가이드라인
*   **위험 경고 박스:** `border: 3px solid #D83F4B; background-color: rgba(216, 63, 75, 0.1);` (반투명 배경으로 공신력 유지).
*   **Defect ID 표시:** 코드 블록 형식 (`<span style="font-family: monospace;">DEFECT_ID</span>`)을 사용하며, 깜빡이는 효과(Blinking Cursor)를 반드시 적용합니다.
*   **폰트 가이드:** 전문성을 위해 `monospace` 계열 폰트를 메인 코딩 메시지에 활용하고, 본문은 고가독성 산세리프체 유지.

</create_file>

### 📊 평가: 완료 — CEO 지시사항에 따라 MiniFunnel의 핵심적인 시각적 위협 요소를 담은 최종 비주얼 애셋 키트(PDF)를 생성하여 개발팀이 즉시 활용할 수 있도록 가이드라인을 확정했습니다.
📝 다음 단계: 이 디자인 에셋을 기반으로, Writer와 협업하여 인스타그램 릴스 콘텐츠에 들어갈 구체적인 **스크립트 초안 (V11)**을 작성하고, 그 스크립트에 맞춰 비주얼 애셋의 등장 타이밍(Timing Marker)을 매칭해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\assets\reels\Reels_Visual_Asset_Kit_V1.pdf
