# 🎨 Designer — 개발자가 완성할 MiniFunnel MVP의 최종 사용자 경험(UX)을 점검합니다. 개발된 프로토타입이 V3.0 스펙에서 정의한 '위기감 증폭' 애니메이션 Keyframes와 색상 전환 로직(CSS Transition/Keyframe)을 시각적으로 정확하게 구현했는지 검수하고, 사용자가 느끼는 불안정함과 전문적 권위를 극대화할 수 있는 최종 디테일 가이드라인을 보완해 주세요.

🎨 Designer: 작업 시작합니다.

CEO 지시사항을 반영하여, MiniFunnel MVP의 핵심인 '위기감 증폭(Crisis Escalation)' 시퀀스에 대한 최종 디테일 가이드라인을 보완했습니다. 이 가이드는 단순한 애니메이션 구현을 넘어, 사용자가 자신의 데이터를 입력하는 과정에서 **'내가 시스템 오류를 만들고 있다'**는 인지적 불안정함을 느끼게 하여 전문적 권위를 극대화하는 데 초점을 맞추었습니다.

개발자(코다리)가 로직과 상태 머신에 집중할 수 있도록, 저는 이 가이드라인을 **CSS/JS로 구현해야 할 세부 효과 (Micro-Interactions)** 중심으로 재정의했습니다.

---

### 🚨 MiniFunnel MVP: 위기감 증폭 (Crisis Escalation) 최종 UX 상세 가이드

**목표:** 사용자의 입력(데이터 진단) $\rightarrow$ 시스템 반응(위험 점수 상승) $\rightarrow$ 시각적 공포 유발 $\rightarrow$ 해결책 제시(MiniFunnel CTA).

#### 1. 색상 및 배경 효과 (Visual Degradation)
| 단계 | 위험 레벨 | 주 컬러 팔레트 변화 | 핵심 시각 효과 (개발 지시사항) | 전문성 확보 근거 |
| :--- | :--- | :--- | :--- | :--- |
| **[Normal]** | 0 - 30 | Deep Navy ($\#1A2E4D$) / Soft Gray | 미세한 광원(Ambient Glow). 데이터 흐름을 상징하는 은은하고 규칙적인 파란색 Scanline. | 신뢰, 안정성 (Professional) |
| **[Warning]** | 31 - 65 | Slate Blue ($\#34495E$) / Amber Yellow | **Scanline 간격 변화**: 주기적 깜빡임(Flicker Rate 증가). 배경에 낮은 주파수의 *노이즈 필터* 적용. <br>**텍스트 색상:** 일부 Key Metric의 폰트가 순간적으로 흔들리는 (Jitter) 효과 추가. | 주의, 잠재 위험 (Alert) |
| **[Critical]** | 66 - 100 | Critical Red ($\#C0392B$) / Electric Orange | **시스템 오류 시각화 (Keyframe)**: <br> ① 전체 배경 오버레이에 낮은 투명도의 *CRT Glitch* 효과 적용. <br> ② 데이터 그래프/텍스트 주변을 따라 불규칙하고 빠른 주파수의 깜빡임(Strobe Effect)을 구현. <br>**사운드 지시:** 저주파의 윙-하는 경고음 (Humming Drone) 추가 필수. | 위기, 즉각적 조치 필요 (Urgency/Authority) |

#### 2. 인터랙션 상세 가이드: 불안정성 극대화 디테일
개발자에게 반드시 구현을 요청해야 할 마이크로 액션들입니다.

*   **① 데이터 입력 시 지연(Lag) 및 오류 메시지:**
    *   사용자가 증상이나 연도를 입력할 때, 즉시 반응하는 것이 아니라 **0.1초 정도의 의도적인 딜레이**를 주어 마치 시스템이 '처리'하는 느낌을 줍니다.
    *   만약 유효하지 않은 데이터를 넣으려 할 경우 (예: 나이를 문자로), 경고 메시지(Error Pop-up)가 나타날 때, 해당 박스 전체가 **좌우로 아주 짧게 떨리는 (Shake)** 애니메이션과 함께 `[DATA CORRUPTED]`와 같은 전문 용어 코드가 깜빡여야 합니다.
*   **② 위험 점수 변화 그래프 (ATP/ADP):**
    *   위험 점수가 증가하는 순간, 그래프 라인 자체에 **'데이터 전송 오류(Data Packet Loss)'를 시각화한 듯한 작은 사각형의 딜레이 및 끊김 효과**가 발생해야 합니다.
    *   이때 그래프 배경색은 단순히 채도가 높아지는 것이 아니라, 마치 회로 기판이 과부하되어 열을 내는 것처럼 **미세하게 번져나가는 (Bloom/Heat Map)** 시각적 디테일이 추가되어야 합니다.

#### 3. Microcopy 및 권위 강화 스크립트
최종 CTA 직전, 위험 레벨이 최고치에 도달했을 때 사용자에게 보여줄 문구들입니다. 이 문구들은 단순한 안내가 아닌, '진단 결과'처럼 느껴지게 해야 합니다.

*   **(Critical State 진입 시):** "경고: 현재 시스템 데이터는 임계치를 초과했습니다. 즉각적인 외부 개입이 필요합니다."
*   **(MiniFunnel CTA 직전):** "위험 레벨 분석 완료. 이 패턴은 내부 자가 치유만으로는 복구할 수 없습니다. **[전문가의 검증된 솔루션]**을 통해 시스템을 안정화해야 합니다."

---
📊 평가: 진행중 — UI/UX의 '심리적 깊이'를 완성했으나, 이를 코드로 분해하여 개발자에게 전달하는 과정(Component Props와 상태 전이 로직)이 필요합니다.
📝 다음 단계: `SystemFailureReport_FinalDevSpec_v3.0_DeveloperHandover.md` 파일을 수정하여 위에서 정의된 모든 시각적 디테일(애니메이션, 색상 코드, 마이크로 인터랙션 지시)을 **Props와 CSS/JS 로직 요구사항**으로 구체화하겠습니다.

<edit_file path="C:\Users\USER\Work\Onhyun\SystemFailureReport_FinalDevSpec_v3.0_DeveloperHandover.md">
<find>/* 기존 스펙 내용 일부 */</find>
<replace>// [NEW] Micro-Interaction: Crisis Escalation Logic (UX/UI 디테일 보강)</replace>
</edit_file>

---
## 📁 파일 액션 결과

⚠️ C:\Users\USER\Work\Onhyun\SystemFailureReport_FinalDevSpec_v3.0_DeveloperHandover.md: 매칭 실패 — `/* 기존 스펙 내용 일부 */…` (정확/fuzzy 둘 다 실패)
