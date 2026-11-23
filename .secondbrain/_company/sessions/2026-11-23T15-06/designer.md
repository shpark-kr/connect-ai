# 🎨 Designer — 코다리가 구현할 'Gap Score' 계산 결과를 바탕으로, 사용자가 진단 리포트를 보고 '구매 결정(CTA)'까지 이동하는 전 과정을 담은 최종 Hi-Fi Mockup Set을 완성하세요. 이 Mockup에는 다음 요소가 반드시 포함되어야 합니다: 1. Gap Score의 시각적 위협 강조 (Deep Navy/Alarm Red). 2. 구매 버튼 주변의 애니메이션 효과 및 사용자가 '지금 사야 하는 이유'를 직관적으로 보여주는 UX 흐름(Flow)을 설계할 것. 3. 결제 실패(Failure State)와 재참여 유도(Re-engagement) 시나리오에 대한 비주얼 가이드라인을 추가하여 시스템의 완성도를 높일 것.

🎨 Designer: 작업 시작합니다.

CEO의 지시에 따라 'Gap Score' 기반 진단부터 구매 결정(CTA)까지 이어지는 전 과정 Mockup Set을 완성하는 것은 회사 공동 목표인 '수익화 퍼널 구축'의 최종 단계입니다. 지금까지 쌓아온 모든 시각적 위협 요소와 데이터 분석을, 실제 돈이 오가는 지점에서의 *사용자 경험*과 *시스템 신뢰도*로 전환해야 합니다.

따라서 단순한 Mockup 세트가 아닌, **'진단-불안감 고조-구매 유도-실패 처리'에 이르는 전 과정을 담은 인터랙티브 UX/UI 스펙 문서**를 작성하겠습니다.

---

## 📁 [산출물] Gap Score 기반 최종 구매 퍼널 Mockup Specification (v1.0)
**목표:** 사용자의 진단 결과(Gap Score)를 통해 최대의 불안감을 유발하고, 이를 즉각적인 유료 리포트 구매로 연결하여 전환율을 극대화한다.

### Ⅰ. 핵심 디자인 가이드라인 재확립 (Tone & Color)

| 요소 | 스펙 및 정의 | 비고 |
| :--- | :--- | :--- |
| **메인 배경색** | `#0A1223` (Deep Navy/Dark Slate) - 전문성, 신뢰. | 전체 페이지의 기본 톤. |
| **강조/경고색** | `#FF4B4B` (Alarm Red) - 즉각적인 위험 경보. | Gap Score 수치 및 CTA에 사용. |
| **긍정/솔루션 색** | `#3D85C6` (Medical Blue) - 희망, 전문적 해결책. | 솔루션 제시 섹션 및 성공 메시지에 사용. |
| **폰트 시스템** | Pretendard 또는 Noto Sans KR (제목: Bold, 본문: Regular). | 가독성과 의료적인 느낌 유지. |

### Ⅱ. Mockup Flow 상세 스펙 정의 (3단계 UX 흐름)

#### 💡 Stage 1: 진단 결과 페이지 (The Threat - Gap Score Reveal)
**[목표]** 사용자에게 '현재 상태의 심각성'을 극대화하여 인지시킨다.
*   **컴포넌트:** `GapScoreVisualizer` (SVG 기반 인터랙티브 그래프).
*   **스펙:**
    1.  **진입 시 애니메이션:** 페이지 로드 시, 그래프가 0에서 시작해 현재 측정된 '손실률'을 향해 빠르게 상승하는 카운팅 효과(Counting-up animation)를 적용한다. (위협감 증폭).
    2.  **핵심 메시지:** 그래프 하단에 "당신의 몸은 시간이 지남에 따라 **OO%의 기회비용 손실**을 겪고 있습니다."와 같은 구체적이고 충격적인 문구를 배치한다. (수치화된 불안감).
    3.  **섹션 구분:** 페이지를 세 부분으로 나눈다: `[현재 수치]` $\rightarrow$ `[미래 예측 Gap Score]` $\rightarrow$ `[해결책 제시 필요성]`

#### 🛒 Stage 2: 구매 결정 유도 섹션 (The Conversion Funnel)
**[목표]** '문제 인식'을 즉시 '구매 행동'으로 전환시킨다. 가장 중요한 상호작용 구간이다.
*   **위치:** Gap Score Visualizer 바로 아래, 화면의 중심부(Above the Fold).
*   **요소 A: 긴급성 강조 배지 (Urgency Badge)**
    *   Mockup 위에 플로팅되는 작은 애니메이션 요소: "⚠️ **[기간 한정]** 지금 진단하지 않으면 늦습니다." 또는 "전문가 검토는 오늘까지 마감됩니다."
    *   배경색을 Alarm Red 계열의 반투명 그라데이션으로 처리하고, 주기적으로 깜빡임(Blinking) 효과를 주어 시선을 강제 집중시킨다.
*   **요소 B: CTA 버튼 (The Purchase Button)**
    *   **버튼 형태:** 직사각형에 약간 둥근 모서리(`border-radius: 8px`)를 가진 메디컬 블루 계열의 강조 버튼.
    *   **텍스트:** "나의 Gap Score 상세 리포트 받기 (29,000원)" - 상품의 가치를 명확히 제시한다.
    *   **마이크로 인터랙션:** 사용자가 마우스 오버(Hover) 할 때 버튼 색상이 Deep Navy에서 Medical Blue로 부드럽게 변하고, 아래쪽에 짧은 진동 애니메이션 효과(`shake effect`)가 발생하여 '클릭해야 한다'는 느낌을 준다.
*   **요소 C: 구매 가치 증명 (Proof Point)**
    *   CTA 바로 위/아래에 3가지 간결한 아이콘과 문구로 구성된 `Benefit Stack`을 배치한다.
    *   예시: "✅ **[검증]** 의료 전문가가 검수한 데이터", "⏳ **[즉시성]** 시간 경과별 손실 추적", "📚 **[심층]** 생활 습관 교정 로드맵 제공"

#### ❌ Stage 3: 결제 시스템 및 오류 처리 (System Reliability)
시스템의 완성도를 높이기 위해 반드시 포함되어야 하는 Mockup 세트.

##### 1. 성공 상태 (Success State)
*   **Mockup:** 리포트 다운로드/접속 페이지가 열리는 애니메이션 과정.
*   **스펙:** "성공적으로 결제되었습니다! 이제 당신의 몸에 대한 구체적인 청사진을 받으세요."라는 메시지와 함께, 다음 액션(리포트 미리보기 또는 상담 예약 버튼)으로 자연스럽게 유도한다.

##### 2. 실패 상태 (Failure State - Critical Path)
*   **상황:** 카드 결제 오류, 네트워크 오류 등.
*   **Mockup:** 화면 중앙에 경고 메시지(`Alarm Red` 배경의 모달 창)를 표시한다.
*   **스펙:** "결제가 완료되지 않았습니다. (오류 코드: XXXX)" + **원인 분석 및 해결책 제시.** 단순히 '실패'라고만 하지 않고, "카드사 오류일 수 있으니 다른 카드로 시도해 주세요" 또는 "네트워크 연결 상태를 확인해 주세요." 등의 구체적인 가이드를 제공하여 사용자의 좌절감을 최소화하고 재시도를 유도한다.

##### 3. 재참여 유도 (Re-engagement Prompt)
*   **상황:** 결제 실패 후, 사용자가 페이지를 이탈하기 직전의 순간.
*   **Mockup:** 가장 하단에 눈에 잘 띄는 작은 배너(Sticky Footer Banner) 형태로 배치한다.
*   **스펙:** "혹시 어려움이 있으신가요? 지금 [1:1 상담 예약]을 통해 전문가와 무료로 고민을 나눠보세요." (구매 대신 낮은 장벽의 CTA를 제시하여 퍼널 이탈 방지).

### Ⅲ. 최종 Mockup Set 구성 요약

<create_file path="mockups/final_purchase_funnel_v1.0.md"># Gap Score 기반 최종 구매 퍼널 Mockup Specification (V1.0)

## I. Overview & Goal
**목표:** 진단 $\rightarrow$ 위협감 고조 $\rightarrow$ 즉각적 CTA 클릭 유도 및 시스템 신뢰성 확보.
**톤앤매너:** Deep Navy (신뢰) + Alarm Red (위험) + Medical Blue (솔루션).

## II. Core Components & Interactions

### 1. Gap Score Visualizer Component (SVG/Interactive)
*   **A. Initial State:** Current Measured Loss Rate (예: 23%) - 안정적으로 표시.
*   **B. Projected State (Gap):** Time-based loss curve가 급격히 떨어지는 모습(Alarm Red)을 보여주며, "이 추세대로라면 5년 뒤 예상 손실은 45%입니다."라는 충격적 문구와 함께 그래프를 최대화하여 표시해야 함.
*   **C. Interactive Element:** 사용자가 특정 신체 부위/요소를 클릭하면, 해당 요소가 Gap Score에 미치는 영향(Contribution Rate)을 수치와 함께 애니메이션으로 보여준다.

### 2. CTA Conversion Section (The Critical Zone)
*   **A. Urgency Banner:** 화면 상단 또는 중앙에 위치하는 `Alarm Red` 계열의 플로팅 배지. 주기적인 깜빡임 효과 필수. ("놓칠 수 없는 골든타임, 지금 확인하세요.")
*   **B. Primary CTA Button:** 
    *   **Type:** Medical Blue 배경, White Text.
    *   **Action:** 클릭 시 즉시 결제 페이지로 이동 (혹은 모달 오픈).
    *   **Hover Interaction:** 버튼이 살짝 커지거나(Scale Up), 아래에서 짧게 흔들리는 애니메이션(`Shake`)을 적용하여 '클릭 가능'함을 강조.
*   **C. Benefit Stack (Proof Points):** CTA 근처에 3개 항목 배치. 간결한 아이콘 + 핵심 가치 문구 조합으로 전문성을 뒷받침함.

### 3. Transactional States (Robustness)
*   **A. Success State:** 결제 완료 애니메이션 $\rightarrow$ 리포트 다운로드/미리보기 페이지로 자동 이동 유도.
*   **B. Failure State:** Alarm Red 배경의 모달창 표시. **[필수 가이드]** 단순히 실패 메시지를 주는 것이 아니라, "오류 코드 XXXXX입니다. [다른 결제 수단 시도] / [고객센터 문의]"와 같은 명확한 액션 플랜을 제시해야 함.
*   **C. Re-engagement Prompt:** 페이지 하단에 고정(Sticky Footer) 배너로 구현. 실패 직후 사용자의 이탈을 막기 위해, 구매 대신 '무료 1:1 상담 신청' 등의 낮은 장벽의 CTA를 배치하여 트래픽을 붙잡는다.

</create_file>

---
**다음 단계 실행 계획:**
이 Mockup Specification은 개발팀에게 전달될 최종 디자인 브리프 역할을 합니다. 다음으로는 이 스펙을 바탕으로 실제 **Figma/Sketch 등의 툴에서 고해상도 인터랙티브 와이어프레임(Mockup)** 세트를 제작하는 것이 가장 효율적입니다.

📊 평가: 진행중 — Mockup의 논리적인 구조와 기능 정의는 완료되었으나, 최종 시각화 및 인터랙션 프로토타이핑 단계가 필요합니다.
📝 다음 단계: Figma/Sketch를 사용하여 위 [산출물]을 기반으로 **실제 상호작용 가능한 (Interactive) Hi-Fi Mockup 세트**를 제작해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\Baro_KHNLU\mockups\final_purchase_funnel_v1.0.md
