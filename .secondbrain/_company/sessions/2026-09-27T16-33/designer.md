# 🎨 Designer — 개발팀이 요청할 Mini-App Funnel의 기술적 아키텍처(데이터 흐름, 상태 변화)를 바탕으로, Deep Crimson Red 기반의 UI 컴포넌트가 시스템적으로 어떻게 연동되어야 하는지 '상호작용 시각화 가이드'를 작성해 주십시오. 특히, 점수가 특정 임계값에 도달했을 때 발생하는 애니메이션 타이밍과 경고 메시지의 비주얼적 강도를 개발팀이 구현하기 쉽도록 구체적인 액션(Action) 단위로 보강해야 합니다.

🎨 Designer: 작업 시작합니다. CEO의 지시사항은 개발팀이 실제 구현 단계에서 가장 혼란스러워할 수 있는 '경계면(Boundary)'의 시각적 규칙을 정의하는 것입니다. 코다리 에이전트가 기술 아키텍처와 로직 흐름을 담당했으므로, 저는 이를 기반으로 **'위기감 조성 및 상호작용 타이밍'**에 초점을 맞춘 상세한 디자인 스펙 문서를 작성해야 합니다.

저는 현재 `c:\Data\Project\FreqTrade\assets\mini-app\MiniAppFunnel_DesignSystem_V3.0_Manual.md` 파일과 코다리 에이전트가 수행한 테스트 결과를 모두 참조하여, **'위험도 변화에 따른 애니메이션 및 시각적 피드백 가이드'**를 작성하겠습니다.

### 📄 산출물: Mini-App Funnel - 상호작용 비주얼 스펙 (Dev Handoff Ver.)

다음 내용을 `MiniAppFunnel_InteractionSpec_V1.0.md` 파일로 생성하여 개발팀에 전달합니다. 이 문서는 단순한 디자인 브리프가 아니라, **CSS/JS의 행동(Behavior)**을 규정하는 기술 사양서입니다.

<create_file path="c:\Data\Project\FreqTrade\assets\mini-app\MiniAppFunnel_InteractionSpec_V1.0.md"># 🚨 Mini-App Funnel: 위험도 변화에 따른 상호작용 시각화 가이드 (Dev Handoff Ver.)

## 🎯 목적
본 문서는 'calculate\_adls\_score' 함수가 산출한 점수(Score)의 임계값 변경이 사용자 인터페이스(UI) 및 애니메이션 시스템에서 어떻게 **'위험 신호'**로 시각화되어야 하는지 정의합니다. 개발팀은 이 가이드에 따라 컴포넌트 간의 타이밍, 색상 변화, 피드백 강도를 구현해야 합니다.

## 🛠️ 핵심 디자인 요소 (Components)
1.  **Score Risk Bar:** 점수를 표시하는 메인 막대. (위험도 시각화 주체)
2.  **Deep Crimson Overlay:** 위험 임계값 도달 시 배경을 덮는 오버레이. (경고 강도 증폭 주체)
3.  **CTA Button Group:** 진단 유도를 위한 핵심 버튼들. (액션 유도 및 반응 주체)

## 🧪 State Machine & Interaction Flow Specification

### A. 상태 정의 및 임계값 기준 (Thresholds)

| Score Range | Risk Level | Visual State Name | Primary Color Code (CSS Variable) | Required Action/Behavior |
| :---: | :---: | :---: | :---: | :---: |
| 80점 이상 | Safe | `state-safe` | `--color-green-600` (#48BB78) | 안정적. 미묘한 광원 효과(Subtle Glow). 애니메이션 없음. |
| 50~80점 | Caution | `state-caution` | `--color-yellow-500` (#ECC94B) | 주의 단계. 배경에서 부드러운 '펄스(Pulse)' 시작 (1초 간격, 약하게). |
| 30~50점 | Warning | `state-warning` | `--color-deep-crimson` (#8C1A2D) | **주의/위험.** 점수 바 주변에 경고 테두리(Border Glow) 적용. 메시지 애니메이션 강도 증가. |
| 30점 이하 | Critical | `state-critical` | `--color-alarm-red` (#A5182E) | **최고 위험.** 화면 전체를 Deep Crimson Overlay로 덮음. 시각적/청각적 긴급성 극대화. 강한 진동(Vibration) 피드백 필수. |

### B. 애니메이션 및 타이밍 규칙 (Timing & Animation Rules)
모든 상태 변화는 즉각적으로 느껴지도록 **점진적인 전이(Gradual Transition)** 방식을 사용합니다.

| 이벤트 | 목표 컴포넌트 | 시작 시점 | 지속 시간 (Duration) | 동작 설명 (Action) |
| :---: | :---: | :---: | :---: | :---: |
| **Score 계산 완료** | Score Risk Bar | API 응답 수신 직후 (T=0ms) | 300ms | 점수 바가 비어있다가 목표 값까지 부드럽게 채워지며(Fill Animation), 최종 색상으로 전환. |
| **Warning 진입 (50→30)** | Score Risk Bar / Overlay | T=300ms 경과 시점 | 100ms | `state-caution` -> `state-warning`로의 급격한 색상 변화와 함께, 점수 바 주변에 빠르게 깜빡이는(Flash) 애니메이션 발생. **사용자 시선 집중 유도.** |
| **Critical 진입 (30→20)** | Entire Viewport | T=500ms 경과 시점 | 1s | Deep Crimson Overlay가 배경 전체를 덮으며(Opacity: 0 -> 90%), 화면이 살짝 어둡게 처리됨. 동시에, 모든 CTA 버튼이 **강한 맥동 효과(Strong Pulse Effect)**를 일으키며 깜빡임 (200ms 간격). |
| **CTA 클릭 시** | 해당 버튼 | 클릭 이벤트 발생 시 | 150ms | 버튼이 살짝 눌리는 듯한(Depress) 애니메이션을 보이며, 피드백 색상으로 짧게 채워졌다가 원래 상태로 복귀. (전체 시스템의 안정성을 상기시킴). |

### C. 경고 메시지 및 CTA 연동 스펙
1.  **위험 감지 시 팝업/배너:** `state-warning` 이상 진입 시, 화면 중앙에 "⚠️ **전문가의 정밀 진단이 필요합니다.**"와 같은 문구의 배너가 최소 5초 동안 고정되어야 합니다. 이 배너는 배경의 위험도 색상(Deep Crimson)을 사용하여 위화감 없이 녹아들도록 디자인해야 합니다.
2.  **CTA 활성화 조건:** Mini-App Funnel CTA 버튼들은 점수 바가 `state-warning` 이하로 떨어지는 순간, **즉시 시각적/기능적으로 활성화 상태**여야 하며, 이 변화는 사용자가 '무언가를 놓치고 있다'는 심리적 압박감을 느끼도록 설계되어야 합니다.

---
</create_file>

📊 평가: 완료 — 개발팀이 즉시 참조하여 구현 가능한 수준의 행동 기반 디자인 스펙을 제공했기 때문에 목표가 달성되었습니다.
📝 다음 단계: 코다리 에이전트와 협업하여, 이 상호작용 가이드에 맞추어 프론트엔드 컴포넌트 레벨의 애니메이션 코드 예시(예: React/Tailwind CSS)를 구체적으로 작성하는 것이 필요합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\FreqTrade\assets\mini-app\MiniAppFunnel_InteractionSpec_V1.0.md
