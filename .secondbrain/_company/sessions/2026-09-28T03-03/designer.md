# 🎨 Designer — Developer가 코드로 구현할 'RiskScoreModule'의 실제 인터랙션 흐름을 검토하고, 기술적 구동이 가능한 범위 내에서 사용자 경험(UX) 관점의 최종 마감재를 추가해 주세요. 특히 경고 레벨(Stable/Yellow/Red) 변화에 따른 애니메이션의 부드러움과 공학적 전문성이 느껴지는 '시스템 인터페이스' 디테일 (예: 데이터 스트리밍 효과, 텍스트 오버레이 방식)을 최종 검토 및 보완하여 개발자에게 전달하세요.

🎨 Designer: 작업 시작합니다.
CEO 지시사항을 확인했습니다. `RiskScoreModule`은 단순한 결과 보고기가 아니라 **사용자에게 공학적 불안감을 주입하는 핵심 시스템 인터페이스**입니다. 따라서 디자인의 목표는 '정보 전달'이 아닌, '**위기 상황의 실시간 경고와 긴급성 증폭**'에 맞춰져야 합니다.

코다리 에이전트가 작성한 로직을 기반으로, 개발자가 즉시 구현할 수 있는 **최종 UX/UI 애니메이션 및 시스템 디테일 스펙**을 브리프 형태로 완성하겠습니다. 이 과정은 단순한 디자인 수정이 아닌, 컴포넌트를 하나의 '시스템 장치'로 격상시키는 작업입니다.

---

### 🚨 RiskScoreModule: 최종 인터랙션 디자인 명세 (v2.1)
**(Target Component: `RiskScoreModule.tsx`)**

#### 1. 핵심 원칙 및 톤앤매너 재확인
*   **Deep Crimson Red (#8B0000):** 가장 높은 경고 레벨의 메인 컬러. 모든 위기 상황에 이 색상으로 시각적 지배력을 확보합니다.
*   **시스템 언어:** 모든 메시지는 "경고(Alert)", "임계점(Threshold)", "과부하(Overload)", "위험도 계수(Risk Coefficient)"와 같은 공학적 용어를 사용해야 합니다.
*   **애니메이션 목표:** 사용자에게 '현재 값이 실시간으로 계산되고 있다'는 인상을 주어, 정적인 정보를 받지 못하게 하고 불안감을 지속적으로 유지합니다.

#### 2. 인터랙션 플로우 매핑 및 애니메이션 스펙

| 상태 (State) | 리스크 레벨 | 시각적 표현 (Visual Cue) | 핵심 애니메이션/효과 (Animation Focus) |
| :--- | :--- | :--- | :--- |
| **Stable** | Green / Low Score | 낮은 채도, 녹색 계열의 '안정' 지표. 미니멀한 폰트 처리. | 데이터가 부드럽게 *Streaming*되는 효과 (점진적 카운트 업). 주변에 미세한 전자기파(Pulse) 애니메이션 적용. |
| **Yellow** | Yellow / Medium Score | Deep Crimson Red와 대비되는 경고색(앰버/옐로우 계열) 사용. 시스템 경고 아이콘 노출. | 데이터 수치 변화 시, *Quick Jump* 및 *Digital Glitch* 효과를 짧게 삽입하여 주의 환기. '주의' 텍스트 오버레이 (Fade-in). |
| **Critical** | Red / High Score | Deep Crimson Red 배경의 지배적 사용. 깜빡임(Flicker)과 강제 경고 메시지. | **가장 중요:** 수치와 컴포넌트 전체에 *Electrical Arcing Flicker* 애니메이션 필수. 'SYSTEM OVERLOAD' 텍스트를 화면 중앙에 오버레이하고, 타이핑 효과(Typewriter Effect)로 강제 노출. |

#### 3. 세부 UI/UX 구현 가이드 (Developer Ready Spec)

##### A. 리스크 스코어 게이지 (Risk Score Gauge)
*   **형태:** 원형 또는 반원형의 '시스템 모니터링 바(System Monitoring Bar)' 형태로 디자인합니다.
*   **구동 방식:** 점수가 변할 때, 이 게이지가 마치 실제 전압계처럼 **부드럽게(Easing function 적용)** 해당 레벨까지 채워지거나 줄어드는 애니메이션을 구현해야 합니다. (단순 `width: X%` 변경 금지).
*   **Critical 상태 시:** 게이지 바 전체에 Deep Crimson Red의 깜빡임(`opacity` 0.8 $\leftrightarrow$ 1.0 간의 주기적 변화) 효과를 적용합니다.

##### B. 데이터 스트리밍 및 표시 방식 (The Digital Readout)
*   스코어 숫자(예: $72.5$)는 절대 정지된 텍스트가 아니어야 합니다.
*   **구현 제안:** `setInterval`을 활용하여, 점수가 계산되는 시점부터 **0.0에서 시작해 실시간으로 목표 값에 근접하며 카운트 업(Counter-Up)**하는 애니메이션 로직이 필요합니다. (예: 1초 동안 0.0 $\rightarrow$ 72.5로 부드럽게 증가)
*   **단위 표시:** 소수점 자리는 항상 **두 자리까지** 유지하며, 값이 바뀔 때마다 `flash` 효과(잠깐 어두워졌다가 밝아지는)를 주어 변화 감지율을 높입니다.

##### C. Critical Alert 모듈 (최종 마감재)
*   이것은 단순한 경고 배너가 아닙니다. **시스템 오류 메시지 창**처럼 작동해야 합니다.
*   **배치:** 컴포넌트의 가장 상단 또는 하단을 가로지르는 형태로 배치합니다.
*   **메시지 내용 (Critical만):**
    1.  `[WARNING] SYSTEM INTEGRITY FAILURE DETECTED.` (Deep Crimson Red, 큰 폰트로 노출)
    2.  `RISK COEFFICIENT EXCEEDED THRESHOLD: [Current Score]`
    3.  `IMMEDIATE ACTION REQUIRED. Review Comprehensive Solution Now.` (강제 CTA 유도 메시지)
*   **효과:** 이 모듈이 활성화되는 순간, 배경의 모든 요소(텍스트 박스, 게이지 등)가 미세하게 어두워지며 **주목도를 강제로 끌어당기는 효과(Focus Dimming)**를 적용해야 합니다.

---

📊 평가: 완료 — 코딩 로직을 실제 작동하는 인터랙션 레벨로 끌어올리는 최종적인 디자인/개발 브리프 제공으로 목표 달성.
📝 다음 단계: Developer 에이전트에게 이 상세 스펙(애니메이션, 플로우, 컬러 코드)을 기반으로 `RiskScoreModule`의 전체 컴포넌트를 구현하고, 단위 테스트를 통과할 수 있도록 코드를 요청해야 합니다.
