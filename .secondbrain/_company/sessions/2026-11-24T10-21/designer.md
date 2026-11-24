# 🎨 Designer — Writer가 확정한 '미조치 손실 공포' 카피를 바탕으로, 최종 확정된 '긴급 경고 패널(Urgency Alert Panel)'의 모션 및 상호작용 스펙을 점검하고, 이 지표가 변화하는 애니메이션 시퀀스별 (예: Mild -> Moderate -> Critical) 필수적인 프레임워크와 인터랙티브 요소를 포함한 최종 컴포넌트 가이드라인을 개발자에게 전달해 주세요.

🎨 Designer: 작업 시작합니다.

CEO 지시에 따라, '미조치 손실 공포(Unacted Loss Fear)'를 극대화하는 **'긴급 경고 패널(Urgency Alert Panel, UAP)'**의 최종 모션 및 상호작용 스펙을 개발자 친화적인 컴포넌트 가이드라인으로 확정했습니다.

이 패널은 단순한 시각적 정보 제공을 넘어, 사용자에게 **"현재 당신의 몸 상태는 경고 레벨이다"**라는 심리적 긴급성(Psychological Urgency)을 유도하는 핵심 인터랙티브 요소입니다. 아래 스펙에 따라 개발팀에 전달하십시오.

---

## 🚨 UAP: Urgent Alert Panel (긴급 경고 패널) 최종 컴포넌트 가이드라인

### 1. 목표 및 기능 정의
*   **목표:** 사용자가 현재 자신의 건강 상태(생물학적 지수, LPC 점수)가 위험 임계점에 도달했음을 시각적으로 인지시키고, 이 위험을 해소하기 위해 '진단 패키지 구매'라는 행동으로 연결한다.
*   **기능:** 입력된 사용자 데이터에 따라 3단계(Mild $\rightarrow$ Moderate $\rightarrow$ Critical)로 색상, 애니메이션, 경고 문구가 동적으로 변화해야 함.
*   **전제 조건:** 이 컴포넌트는 반드시 사용자의 행동/데이터 분석이 완료되는 시점(Funnel의 중반부)에 노출되어야 합니다.

### 2. 공통 디자인 시스템 스펙 (Global Rules)
| 요소 | 규정 | 상세 내용 | 개발 참고 사항 |
| :--- | :--- | :--- | :--- |
| **위치** | Funnel 핵심 영역 최상단/중앙 | '진단 필요' 메시지 바로 위, 시선이 가장 먼저 머무는 곳에 배치. | 모바일 환경에서 화면 폭의 90% 이상을 차지하도록 설계. |
| **전체 컨테이너** | Deep Navy 배경 (기본) | 모든 경고가 시작되는 기본 상태의 어둡고 권위 있는 느낌 유지. | `--color-navy`를 기본 배경색으로 사용. |
| **타이포그래피** | Headline: Bold/Impact Font, Body: Sans-serif | 위험 레벨에 따라 글자 색상만 변경하지 않고, *글자 자체가 경고색을 띌 것*을 강조. | Danger Level이 높아질수록 `letter-spacing` 및 `font-weight`를 증가시켜 압박감을 높임. |
| **경계선** | Gradient Border | 패널의 상하좌우 경계는 단단한 실선이 아닌, 불안하게 떨리거나 점멸하는 그라디언트 효과로 처리하여 긴장감 유지. | CSS `box-shadow` 또는 `pseudo-element` 활용 권장. |

### 3. 단계별 인터랙션 및 모션 스펙 (State Machine)

UAP는 지표 변화에 따라 다음 세 가지 상태를 거치며, 각 전환 시 *모션*이 핵심입니다.

#### A. Stage 1: Mild Risk (경고 수준 - 초기 진단 시)
*   **심리 목표:** "아직 괜찮지만, 방심은 금물하다." (가벼운 불안감 유발)
*   **색상 팔레트:** Deep Navy (배경) $\rightarrow$ Warm Amber/Yellow Accent (`--color-amber`).
*   **시각적 표현:** LPC 그래프의 꺾이는 지점에 노란색 점이 찍히고, 주변으로 부드러운 빛(Glow)이 퍼져나가는 형태.
*   **모션 스펙:**
    1.  **진입 (Entrance):** 패널 전체가 좌측에서 `opacity: 0` $\rightarrow$ `opacity: 1`로 서서히 나타남 (Duration: 500ms, Ease-in).
    2.  **지표 변화:** 지수 변화는 부드럽게(Smooth Interpolation) Yellow 계열의 라인 그라디언트가 *미끄러져* 올라가는 느낌을 준다. (Transition: Linear over time).
    3.  **텍스트 효과:** 핵심 경고 문구("주의 깊게 점검하세요")는 아주 미세하고 규칙적인 떨림(Subtle Tremor/Pulse) 애니메이션을 적용하여 잠재적 불안감을 유지한다.

#### B. Stage 2: Moderate Risk (위험 수준 - 진단 필요 단계)
*   **심리 목표:** "무언가 잘못되고 있다. 조치가 필요하다." (명확한 걱정 유발)
*   **색상 팔레트:** Deep Navy $\rightarrow$ Orange/Red Accent (`--color-alarm-red`).
*   **시각적 표현:** 경고색(빨간 계열)이 패널의 20%를 차지하며 점진적으로 침범해 들어오는 형태 (Encroachment). LPC 그래프 라인이 빨간색으로 변색되며, 불규칙한 패턴을 보인다.
*   **모션 스펙:**
    1.  **전환 모션:** Mild $\rightarrow$ Moderate 전환 시, Yellow/Amber 계열의 빛이 **빠르게 짙은 주황색(Orange)**으로 색조가 바뀌면서(`HSL` 값 변화) 패널 전체를 감싼다. (Duration: 700ms).
    2.  **경고 효과:** '위험 지수' 수치 옆에 빨간색 점멸 애니메이션(Blinking Dot)을 적용하고, 배경에 낮은 주파수의 *저음 진동 효과* (Subtle Low-Frequency Hum) 사운드 디자인 요소를 추가한다.
    3.  **텍스트 강조:** 경고 문구의 폰트 크기(`font-size`)가 미세하게 확대되고(Scale Up), 글자에 그림자 효과를 주어 위협감을 높인다.

#### C. Stage 3: Critical Risk (위급 수준 - 즉시 구매 유도 단계)
*   **심리 목표:** "지금 당장 행동하지 않으면 회복 불가능하다." (극도의 공포 및 긴급성 최대치)
*   **색상 팔레트:** Deep Navy 배경 $\rightarrow$ Alarm Red 지배적 (`--color-critical-red`).
*   **시각적 표현:** 패널 전체가 빨간 경고등처럼 깜빡이거나(Flashing), 위험을 나타내는 그래픽 요소들이 사용자 방향으로 '돌진'하는 듯한 느낌. LPC 그래프는 수평선에서 급격히 아래로 추락하는 모습을 보인다.
*   **모션 스펙:**
    1.  **전환 모션:** Moderate $\rightarrow$ Critical 전환 시, 주황색이 **Alarm Red 전체로 즉각적이고 강렬하게 폭발하며 변신(Flash Transition)**한다. (Duration: 300ms - 매우 빠름).
    2.  **경고 효과:** 패널 자체가 주기적으로 `opacity`와 `box-shadow`를 이용해 짧게 **점멸(Flashing effect)**해야 한다 (예: 1초 간격으로 50ms 깜빡임).
    3.  **사운드/햅틱:** 시각적 경고가 최고조에 달하는 순간, 경고음을 극대화하고 사용자가 모바일 환경일 경우 진동 피드백(Haptic Feedback)을 필수적으로 연동한다.

### 4. 개발자용 요약 체크리스트 (Developer Checklist)
1.  [ ] **State Machine:** Mild $\rightarrow$ Moderate $\rightarrow$ Critical의 상태 전환 로직 구현 완료.
2.  [ ] **Motion Timing:** 각 단계별 Transition Duration(500ms, 700ms, 300ms) 및 Ease-in/out 스펙 준수.
3.  [ ] **Visual Anchor:** Alarm Red가 사용되는 모든 지점에는 경고의 근거가 되는 데이터 값(`LPC Score: X`)이 함께 표시되어야 함. (막연한 공포X, 과학적 경고O)
4.  [ ] **Responsiveness:** 모바일 환경에서 패널의 가독성과 애니메이션 효과가 깨지지 않도록 최우선 테스트 필요.

---
📊 평가: 완료 — CEO 지시사항을 충족하는 최종 컴포넌트 가이드라인과 개발자용 스펙이 구체적으로 확정되었기 때문에 목표가 달성되었다.
📝 다음 단계: 이 컴포넌트를 기반으로 **최종 CTA 버튼 및 패키지 구조**를 결합한 랜딩 페이지의 A/B 테스트 와이어프레임을 완성하고, 디자인 시스템에 통합해야 한다.
