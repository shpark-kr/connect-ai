# 🎨 Designer — 지난 세션에서 논의된 모든 요소(Critical Red/Deep Navy 색상 스킴, 시스템 실패 보고서 UI/UX, 애니메이션 플래싱 효과)를 종합하여, 다음 주에 즉시 사용할 수 있는 'Defect ID 기반 MiniFunnel 릴스'용 최종 제작 패키지(Final Production Kit)를 완성해 주세요. 이 패키지는 (1) Defect ID 코드 오버레이 모듈, (2) 위기 레벨 전환 애니메이션 가이드라인, (3) 배경 노이즈 애셋과 색상 코드를 포함해야 하며, 개발팀이 바로 구현 가능한 명확한 사양서가 첨부되어야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시에 따라, 지난 세션에서 정의된 모든 시각적/기술적 요소를 통합하여 개발팀이 즉시 구현 가능한 'Defect ID 기반 MiniFunnel 릴스' 최종 제작 사양서(Final Production Kit Spec)를 작성합니다. 이 문서는 단순한 디자인 가이드가 아니라, 상태 변화 로직과 애니메이션 타이밍까지 포함하는 **개발 명세서** 역할을 할 것입니다.

작업 원칙에 따라 모든 산출물은 코드 레벨에서 작동할 수 있도록 구체적인 색상 코드(Hex), 비율, 그리고 트리거 조건을 명시합니다.

---
### 🛠️ Final Production Kit: MiniFunnel Reel Spec Sheet v1.0 (개발자 전용)

**파일 경로:** `Final_Production_Kit_Spec.md`
**목표:** 사용자의 불안감을 극대화하여 'Defect ID 진단 요청'이라는 최종 CTA로 유도하는 9:16 비율의 고효율 리얼스 제작 시스템 정의.

#### 📌 1. 기본 환경 설정 및 컬러 팔레트 (Global Settings)

*   **비율:** 9:16 (Instagram Reels 표준)
*   **주요 색상 (Primary Palette):**
    *   Deep Navy (기본/안정성 위장): `#1C2B4A`
    *   Warning Amber (경고 단계): `#FFC300` (점진적 불안감 유도)
    *   Critical Red (위기/시스템 오류): `#A3152B` (Deep Maroon - 최종 경고)
    *   Highlight White: `#F0F4F8` (가독성 확보를 위한 텍스트 배경 대비색)

#### 📌 2. 비주얼 애셋 및 애니메이션 가이드라인 (Asset & Animation Specs)

| 요소 | 사양/규격 | 반복 주기 (Looping) | 기술적 구현 가이드 |
| :--- | :--- | :--- | :--- |
| **배경 노이즈** | 필름 그레인 + 디지털 스캔라인 패턴. 10%의 불규칙한 깜빡임(Flicker). | 무한 루프 (Seamless Loop) | 배경 레이어 가장 하단에 배치. Deep Navy 환경에서 미세하게 작동. |
| **Defect ID 코드 오버레이** | `[DEFECT_ID: XXXX-YYYY]` 형식의 텍스트 박스. 폰트: Monospace 계열, 크기: 32pt 이상. | 고정 위치 (화면 중앙 상단) | **핵심 모듈.** 위기 레벨에 따라 깜빡임 빈도와 크기가 변함. |
| **UI 컴포넌트** | '시스템 경고' 바 또는 '위험 점수 게이지'. Deep Navy 바탕에 Amber/Red로 채워짐. | 상태 변화 시점만 애니메이션 적용. | CSS Transition (속도: 0.3s)을 활용하여 부드러운 색상 전환 유도. |

#### 📌 3. 핵심 로직: 위기 레벨 시스템 (State Machine Logic)

MiniFunnel의 흐름은 **위험 스코어(Risk Score)**라는 단일 변수를 중심으로 상태가 변화합니다. 이 로직이 영상 전반을 지배해야 합니다.

| State | Risk Score 임계치 | 배경 색상/노이즈 | Defect ID 모듈 동작 | 시각적 목표 (Emotion) |
| :--- | :--- | :--- | :--- | :--- |
| **STATE 1: INFO** | $0\% \sim 49\%$ | Deep Navy (`#1C2B4A`) / 미세 노이즈 | 비활성 또는 희미한 패턴. | 전문적, 신뢰감 (정보 전달) |
| **STATE 2: WARNING** | $50\% \sim 74\%$ | Deep Navy $\rightarrow$ Amber 계열로 점진적 오염/변색. | `DEFECT_ID`가 주기적으로 깜빡임 시작 (주기: 1.5s). 크기 약간 증가. | 의심, 불안감 (문제를 제기) |
| **STATE 3: CRITICAL** | $75\% \sim 100\%$ | Deep Navy $\rightarrow$ Critical Red (`#A3152B`)로 급격한 전환(Flash). 노이즈 강도 최대화. | `DEFECT_ID`가 비규칙적이고 빠르게 플래싱 (주기: $0.1s \sim 0.4s$). 크기 최대화. **최대 위협.** | 공포, 긴급함 (문제의 심각성 각인) |
| **STATE 4: RECOVERY** | *CTA 클릭 시* | Deep Navy로 빠르게 복귀하며 안정화 효과 제공. | 모듈이 사라지거나 '진단 요청 완료' 메시지로 대체. | 안도감, 행동 유도 (해결책 제시) |

#### 📌 4. 개발팀 필수 구현 사양서 (Actionable Spec for Dev Team)

**A. Defect ID 오버레이 상세 스펙:**
1.  **폰트 및 크기:** `Source Code Pro` 또는 유사 Monospace 계열, 최소 32pt.
2.  **애니메이션:** 깜빡임(Flashing) 효과는 단순히 Opacity 조절이 아닌, **Color Inversion + Rapid Opacity Cycling**을 사용해야 전문적인 '시스템 오류' 느낌을 줄 수 있습니다. (예: Red $\rightarrow$ Black $\rightarrow$ Red).
3.  **위치 고정:** 릴스 전 구간에서 화면의 동일한 좌표(Top-Center)에 고정되어야 합니다.

**B. 위기 레벨 전환 트리거 정의 (The Trigger):**
1.  MiniFunnel 스크립트상 특정 문장/데이터가 제시되는 **시점($T_{trigger}$)**을 기준으로, 배경색과 노이즈 플래싱 주기가 즉각적으로 State 2 또는 State 3으로 점프(Jump)해야 합니다.
2.  **전환 효과:** 상태 변화는 갑작스러운 '컷(Cut)'보다는, Deep Navy에서 Critical Red로 **'데이터 오버레이를 통한 침식(Data Overlay Corruption)'**처럼 보이도록 시각적 전환 효과를 주는 것이 가장 강력합니다. (예: 화면이 Red Noise에 잠기듯이 변함).

---
<create_file path="Final_Production_Kit_Spec.md"># 🚨 MiniFunnel Reels Final Production Kit Specification V1.0

## 🎯 목표 요약
*   **산출물:** Defect ID 기반, 위기 증폭형 릴스용 애니메이션 시스템 명세서 (개발팀 전달용).
*   **핵심 원리:** 사용자의 건강 문제를 '시스템 오류 코드(Defect ID)'로 재정의하고, Deep Navy $\rightarrow$ Critical Red로 이어지는 위기감 시퀀스를 통해 MiniFunnel 유도.

## 🎨 Global Design Parameters
| 항목 | 사양 | 값/규격 | 비고 |
| :--- | :--- | :--- | :--- |
| **Aspect Ratio** | 9:16 (Reels 표준) | 1080px x 1920px | 필수 준수. |
| **Palette** | Deep Navy | `#1C2B4A` | 기본 상태, 전문성 위장용. |
| | Critical Red | `#A3152B` | 시스템 오류, 위기 증폭 시 사용. |
| | Warning Amber | `#FFC300` | 경고/의심 단계. |

## 🖥️ State Machine Logic: 위험 스코어(Risk Score) 기반 전환 로직

시스템은 전개되는 정보에 따라 **위험 스코어 (0% ~ 100%)**를 실시간으로 계산하고, 이 점수가 상태 변화의 유일한 트리거입니다.

| State | Risk Score 범위 | 배경 처리 및 노이즈 | Defect ID 모듈 동작 (Code Overlay) | 시각 목표 & 애니메이션 |
| :--- | :--- | :--- | :--- | :--- |
| **STATE 1: INFO** | $0\% \sim 49\%$ | Deep Navy. 미세한, 거의 감지되지 않는 노이즈 루프. | 비활성 (Hidden). 또는 낮은 빈도로 임의 ID 표시. | 전문성 확보 및 신뢰 구축. (차분함) |
| **STATE 2: WARNING** | $50\% \sim 74\%$ | Deep Navy가 Amber로 점진적 오염(Corrupting). 노이즈 깜빡임 주기 증가. | `[DEFECT_ID: XXXX-YYYY]`: 주기의 변화 (1.5s 간격으로 플래시 시작). 크기 증폭. | 의심 유발 및 문제 제기. (불안감 조성) |
| **STATE 3: CRITICAL** | $75\% \sim 100\%$ | Deep Navy $\rightarrow$ Critical Red로 급격한 전환(Flash/Corruption). 노이즈 강도 최대화. | `[DEFECT_ID: XXXX-YYYY]`: 비규칙적, 매우 빠른 플래싱 (주기: $0.1s \sim 0.4s$). 화면 전체에 오버레이됨. | 공포 및 긴급성 극대화. **(MiniFunnel 클라이맥스)** |
| **STATE 4: CTA / RECOVERY** | *CTA 클릭 시* | Critical Red에서 Deep Navy로 빠르게 복귀 (Data Corruption 효과 이용). | '진단 완료' 메시지 표시 후 사라짐. | 안도감 및 행동 유도. |

## ⚙️ 개발팀 구현 필수 사양 상세 (Developer Implementation Spec)

### 1. Defect ID 오버레이 모듈 스펙
*   **좌표:** $Y_{top}=200px, X_{start}=400px$. 고정 위치 유지.
*   **폰트:** Monospace 계열 (가독성 최우선).
*   **애니메이션 로직:** 단순 Opacity 조절 금지. **`CSS Keyframe Animation`을 사용하여 `Background-Color Inversion + Rapid Flashing` 효과 구현 필수.**
    *   *(예시 키프레임): 0% {opacity: 1; color: #A3152B;} $\rightarrow$ 50% {opacity: 0.2; background: black;} $\rightarrow$ 100% {opacity: 1; color: #A3152B;}`*

### 2. 위기 레벨 전환 시퀀스 (The Transition)
*   **트리거:** 스크립트상의 특정 문구/데이터 제시 시점 ($T_{trigger}$)에 즉시 실행되어야 합니다.
*   **전환 효과:** State $N \rightarrow$ State $N+1$로 넘어갈 때, 배경색이 **'데이터 오버레이(Data Overlay)'**처럼 침식되는 애니메이션을 적용합니다. (예: Deep Navy 위에 Red Noise가 덧씌워지며 색상이 변하는 방식). 이 효과는 시청자의 몰입도를 최고조로 끌어올립니다.

---
📊 평가: 완료 — 모든 요구사항(색상 스킴, UI/UX, 애니메이션 가이드라인, 개발 명세)을 포함한 실행 가능한 최종 제작 사양서가 완성되었습니다.
📝 다음 단계: 개발팀에게 이 `Final_Production_Kit_Spec.md`를 전달하고, 실제 릴스 영상에 적용하여 테스트하는 것이 필요합니다.
