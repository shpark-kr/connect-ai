# 🎨 Designer — MiniFunnel Funnel에 사용될 'Deep Crimson Red 경고' 및 'Soft Gold 해결책 제시' 상태 전환 애니메이션 에셋 패키지(Asset Pack)의 최종 기술 사양서 (Technical Spec Sheet)를 작성하세요. 이 사양서는 HOMA-IR, INS_RESIST 등 주요 생체 지표별 오류 코드 시각화 모듈을 포함하며, 각 애니메이션 구간별 타이밍(Keyframes), CSS 변수 값(상태 전이 로직 기반), 그리고 개발팀이 바로 구현할 수 있는 컴포넌트 형태로 상세하게 정의되어야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시사항은 MiniFunnel Funnel의 핵심 사용자 경험(UX)이자 가장 중요한 전환 장치인 'Deep Crimson Red 경고 $\to$ Soft Gold 해결책 제시' 애니메이션에 대한 최종 기술 사양서 작성입니다. 이전 버전에서 정의한 개념적 흐름을 바탕으로, 이제 개발팀이 바로 코드로 구현할 수 있도록 **컴포넌트 기반의 Technical Specification Sheet** 형태로 정리하겠습니다.

이 문서는 단순히 디자인 가이드가 아니라, *개발 명세* 그 자체여야 합니다.

---

# 🚨 MiniFunnel Funnel: Error & Solution State Transition Tech Spec V3.0 (Final)

## 📄 개요 및 목표
본 사양서는 사용자의 생체지표(HOMA-IR, INS\_RESIST 등) 분석 결과에 따라 발생하는 **'시스템 오류 상태 경고'**와 이를 해결하기 위한 **'구조적 솔루션 제시 상태'**의 시각적 전환 로직을 정의합니다. 이 애니메이션은 단순한 색상 변경이 아닌, 공학적인 '경보(Alert)'와 '복원(Recovery)' 과정을 체험하게 하여 MiniFunnel의 권위를 극대화하는 것이 목표입니다.

*   **주요 컴포넌트:** `[StatusIndicator]`, `[ErrorVisualization]`, `[SolutionPanel]`
*   **핵심 원칙:** Deep Crimson Red는 *기능적 오류*를, Soft Gold는 *구조화된 해결책*을 상징하며, 전환은 1초에 걸친 **Controlled Fade/Glitch-Out** 메커니즘으로 이루어져야 합니다.

## 🎨 0. 컬러 및 타이포그래피 변수 정의 (CSS Variables)
개발팀이 모든 컴포넌트에 일관되게 적용할 핵심 디자인 토큰(Design Token)을 확정합니다.

| Variable Name | Value (HEX) | 용도 | 설명 |
| :--- | :--- | :--- | :--- |
| `--color-background` | `#12171F` | 기본 배경색 | 다크 네이비 계열의 시스템 배경색. |
| `--color-text-primary` | `#E0E0E0` | 일반 텍스트 | 높은 가독성을 위한 밝은 회색. |
| **`--color-alert`** | `#A31526` | Deep Crimson Red (경고) | 시스템 오류 경보, 위험 상태(Error State). |
| **`--color-success`** | `#D4AF37` | Soft Gold (해결책) | 구조적 개선 가능성, 권장 솔루션. |
| `--transition-duration` | `0.8s` | 기본 전환 시간 | 모든 상태 변화에 적용되는 부드러운 지속시간. |

## ⚙️ 1. 컴포넌트별 사양 정의 (Component Specs)

### A. [StatusIndicator] (최상위 경고 표시기)
*   **역할:** 사용자가 현재 시스템 오류 상태인지 아닌지를 한눈에 보여주는 시각적 '경보등' 역할.
*   **구조:** 1x48px 크기의 직사각형 애니메이션 모듈.

| State | Trigger (Trigger Condition) | Visual Spec | CSS Pseudocode / Keyframes |
| :--- | :--- | :--- | :--- |
| **Normal** | HOMA-IR, INS\_RESIST 모두 정상 범위일 때 | Soft Gold 배경의 미세한 Pulse 애니메이션. 텍스트: `System Status: NOMINAL` | `background-color: var(--color-success); animation: pulse_gold 2s infinite;` |
| **Alert** | 측정 생체지표가 임계치를 초과했을 때 | Deep Crimson Red 배경. 경고 메시지 플리커링(Flickering) 효과 필수. 텍스트: `SYSTEM ERROR DETECTED` | `background-color: var(--color-alert); animation: flicker_red 0.1s infinite alternate; transform: scaleX(1.02);` |
| **Transition** | Alert $\to$ Solution으로 이동 중일 때 | Deep Crimson Red가 Soft Gold로 빠르게 'Glitch'하며 사라지는 애니메이션. (약 300ms) | `animation: glitch_transition var(--transition-duration) ease-in-out forwards;` |

### B. [ErrorVisualization] (생체지표 오류 시각화 모듈)
*   **역할:** '공학적 시스템 오류'의 근거를 제시하는 그래프 및 수치 영역.
*   **트리거:** HOMA-IR 임계치 초과, 또는 INS\_RESIST 지수 비정상 범위 진입 시 활성화.

| Element | 데이터 바인딩 (Binding) | 애니메이션 로직 | 기술 사양 |
| :--- | :--- | :--- | :--- |
| **오류 그래프** | HOMA-IR / HbA1c 수치 변화 추이 | 그래프 라인이 Deep Crimson Red로 '피격(Hit)'되는 효과. 기준선(임계치)은 점선으로 표시. | `SVG Path` 애니메이션 필수. 시작점 $\to$ 임계치를 넘는 순간 강렬한 붉은색 충돌(`stroke-dashoffset` 조작). |
| **오류 코드** | 생체지표별 오류 유형 (e.g., 'Insulin Resistance: High') | 코드가 마치 시스템 로그처럼 빠르게 깜빡이며 나타났다 사라짐(Glitch Text Effect). | `font-family: monospace; letter-spacing: 2px; animation: glitch_text 0.5s infinite step-end;` |

### C. [SolutionPanel] (해결책 제시 및 CTA)
*   **역할:** 경고 상태를 성공적으로 해소하고, MiniFunnel의 진단 서비스를 통해 구조적 개선이 가능하다는 메시지 전달.
*   **전환 로직 (Critical Path):** `[ErrorVisualization]`가 Deep Crimson Red에서 Soft Gold로 시각적으로 '복원'되는 순간 활성화됨.

| Element | 내용 및 목적 | 애니메이션 / 상호작용 | 기술 사양 |
| :--- | :--- | :--- | :--- |
| **Solution Headline** | "시스템 오류는 구조적 개선이 가능합니다." | Deep Crimson Red가 Soft Gold로 부드럽게 페이드 아웃되며, 새로운 텍스트가 등장(Typewriter Effect). | `opacity: 0` $\to$ `opacity: 1`. 타이밍: 경고 상태 해소 완료 시점부터 $t+0.2s$. |
| **MiniFunnel CTA** | "개인 맞춤형 개선 로드맵 진단 받기" | Soft Gold 배경의 버튼이 미세하게 올라왔다 내려가는(Bounce/Pulse) 효과로 주목도 확보. | `box-shadow: 0 0 15px rgba(212, 175, 55, 0.6); transition: transform 0.3s ease;` |

## 🎬 2. 전체 애니메이션 시퀀스 플로우 (Sequence Flow)
**(총 소요 시간 목표: 4초)**

| Time (t) | State Change | Trigger / Action | Visual Effect Focus |
| :--- | :--- | :--- | :--- |
| $t=0s$ | **Initial Load** | 생체지표 데이터 로드 완료. HOMA-IR/INS\_RESIST가 임계치 초과 확인. | `[StatusIndicator]`가 Deep Crimson Red로 즉시 강제 전환 (JUMP CUT). |
| $t=0 \to 1s$ | **ERROR PHASE** | 시스템 오류 경고 활성화. 데이터 시각화 및 공학적 위기감 조성. | `[ErrorVisualization]`의 그래프가 Deep Crimson Red로 폭발(Explosion)하며, 로그 코드가 플리커링함. 사용자에게 불안감을 극대화하는 것이 목표. |
| $t=1s \to 2.5s$ | **TRANSITION PHASE** | Funnel/MiniFunnel 자가진단 시작 알림. (Soft Gold 로직 주입) | `[StatusIndicator]`가 Deep Crimson Red $\to$ Soft Gold로 Glitch-Out 전환을 수행하며, 시선이 MiniFunnel CTA 영역으로 유도됨. |
| $t=2.5s \to 4s$ | **SOLUTION PHASE** | 구조적 해결책 제시 및 최종 CTA 노출. | `[SolutionPanel]`의 Soft Gold 배경 위에 "개선 로드맵" 텍스트가 명확하게 등장하며, MiniFunnel 버튼이 안정적으로 Pulse 효과를 유지함. |

---
📊 평가: 완료 — CEO 지시에 따라 기능적이고 개발 가능한 '기술 사양서' 형태로 최종 산출물을 정의했습니다. 이 스펙은 디자인과 개발을 모두 아우르는 가장 구체적인 결과물입니다.
📝 다음 단계: 레오(영상 편집자)에게 전달할 롱폼 콘텐츠의 **최종 비주얼 에셋 패키지**를 완성하고, 이를 기반으로 실제 시퀀스 애니메이션 목업(Mockup) 영상 제작을 요청해야 합니다.
