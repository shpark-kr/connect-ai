# 🎨 Designer — Developer가 코딩을 시작할 수 있도록, Funnel의 '시스템 리스크 스코어' 측정 모듈에 대한 최종적인 인터랙션 흐름도(Flowchart) 및 컴포넌트별 상세 디자인 가이드라인(색상 코드, 폰트 규격 포함)을 문서화하여 Developer에게 전달해 주십시오. 특히, 점수가 임계점을 초과할 때의 애니메이션 트리거와 Deep Crimson Red 경고 UI가 작동하는 로직적 조건을 명확히 정의해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO 지시사항과 코다리 에이전트가 작성한 `RiskScoreModule.tsx` 스켈레톤을 기반으로, 개발자가 즉시 구현 가능한 수준의 **최종 시스템 디자인 명세서**를 작성했습니다. 이 문서는 단순히 '예쁘게' 만드는 것이 아니라, 점수 변화에 따라 사용자에게 공학적 위기감을 전달하는 ‘살아있는 UI 로직’을 정의하는 데 초점을 맞췄습니다.

이 산출물은 `funnel_design_spec_v1.md` 파일로 작성하여 개발팀(Developer)에게 공식적으로 전달해야 합니다.

<create_file path="src/docs/funnel_design_spec_v1.md">
# 🧬 온현 Funnel - 시스템 리스크 스코어 측정 모듈 최종 디자인 명세서 (V1.0)

**작성자:** 🎨 Designer Agent
**대상:** Developer Team
**핵심 목표:** 단순 데이터 표시를 넘어, 임상적 바이오마커 점수를 기반으로 사용자에게 '시스템 과부하'와 '즉각적인 개입 필요성'이라는 감정적 위기감을 전달하는 인터랙티브 컴포넌트를 구현한다.

---

## Ⅰ. 글로벌 디자인 시스템 및 규격 정의 (Global Specs)

### 1. 컬러 팔레트 및 사용 목적
| 이름 | HEX 코드 | RGB 값 | 용도 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **Deep Crimson Red** (Critical) | `#8B0000` | (139, 0, 0) | **위험 경보**, 과부하 시뮬레이션, 임계점 초과 배경 오버레이. | 가장 중요함. 공포와 긴급성을 유발하는 색. |
| **System Warning Amber** (Moderate) | `#FFC300` | (255, 195, 0) | 주의 단계, 경고성 강조 표시, 점수 변화 그래프의 '경계' 구간. | 위험도가 높아지기 시작했음을 알림. |
| **Deep Navy Blue** (Base/Primary) | `#0A1931` | (10, 25, 49) | 배경색(Dark Mode), 주요 타이포그래피 색상. 전문적이고 신뢰감 있는 기반을 제공. | 메인 배경색으로 사용. |
| **Accent Gold** (Success/Action) | `#FFD700` | (255, 215, 0) | 성공적인 결과(솔루션 발견), CTA의 활성화 상태 강조. | 희망과 해결책을 상징하며 Deep Crimson Red와 대비를 이룸. |
| **Neutral Text** (Secondary) | `#EAEAEA` | (234, 234, 234) | 본문 및 보조 설명 텍스트. 가독성을 높임. |

### 2. 타이포그래피 규격 (Typography Specification)
*   **메인 폰트:** Noto Sans KR 또는 Pretendard 계열의 산세리프체. (가독성 최우선)
*   **제목/헤드라인:** `font-size: 2rem` (32px), `font-weight: 700`. Deep Navy Blue 사용.
*   **점수 표시(Score Display):** `font-size: 4rem` (64px), **볼드체**, Dynamic Color 적용. 이 부분이 가장 크고 눈에 띄어야 함.
*   **본문:** `font-size: 1rem` (16px), Neutral Text 사용.

---

## Ⅱ. 인터랙션 흐름도 및 로직 정의 (Flowchart & Logic)

사용자 입력(Biomarkers) $\rightarrow$ **[CORE LOGIC: Risk Score Calculation]** $\rightarrow$ **[UI/UX Triggering]** $\rightarrow$ 결과 제시

### 1. 리스크 점수 계산 모듈 (RiskScoreModule Component Logic)
| 상태 (State) | 임계점 조건 (Trigger Condition) | Deep Crimson Red 작동 여부 | UI 반응 및 애니메이션 트리거 | CTA 강제 유도 여부 |
| :--- | :--- | :--- | :--- | :--- |
| **🔴 CRITICAL** | $HOMA-IR > 3.5$ 또는 $MMIV > 12$ (복합 위험) | **필수 작동** | 점수 표시 영역 전체가 Deep Crimson Red로 깜빡임(Flash Effect). 주변 컴포넌트에 경고 오버레이(`opacity: 0.8`, `background-color: #8B0000`). 에러 메시지("시스템 과부하 감지!")가 중앙에 플래시 출력됨. | **최상** (즉시 행동 유도) |
| **🟡 HIGH** | $HOMA-IR > 2.5$ 또는 $MMIV \in [8, 12)$ | **부분 작동** | 점수 표시 영역 테두리가 Deep Crimson Red로 깜빡임(Pulse Effect). 경고 배너가 상단에 고정되어 나타나며 "위험 임계점 접근" 문구 출력. | **강함** (빠른 행동 유도) |
| **🟠 MODERATE** | $HOMA-IR \in [1.5, 2.5)$ 또는 기타 위험 지표 상승 시작 | 미작동 / 경고성 노란색 사용 | 점수 변화 그래프에 System Warning Amber 강조 표시. 부드러운 애니메이션(Smooth Transition). | **보통** (정보 제공 및 탐색 유도) |
| **🟢 LOW/SAFE** | 모든 지표가 정상 범위 내에 있을 때 | 비작동 | 차분하고 신뢰감 있는 Deep Navy Blue 톤 유지. 점수 변화 그래프가 안정적임(Stable Line). | **낮음** (교육 자료 열람 권유) |

### 2. 애니메이션 트리거 정의
1.  **Critical Flash:** `[CSS Animation]` - 주기적인 깜빡임 효과를 주어 긴급성을 극대화해야 함. (예: `@keyframes flash { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; background-color: #8B0000; } }`)
2.  **Score Transition:** 점수가 업데이트될 때, 수치 변화가 '점프'하는 것이 아니라, 마치 계기판이 움직이듯 부드러운 트랜지션(`transition: all 0.4s ease-out;`)을 사용해야 전문적임.

---

## Ⅲ. 컴포넌트별 상세 디자인 가이드 (Component Details)

### 1. 리스크 점수 게이지 모듈 (`RiskScoreModule` - 코다리 작업물 기반)
*   **기능:** 현재 상태를 한눈에 보여주는 시각적 대시보드 역할.
*   **디자인:** 중앙에 가장 큰 폰트로 **점수 값 (숫자)**을 표시하고, 그 아래에 직관적인 '위험 레벨' 배지(Badge)가 위치해야 함.
    *   Critical: 배경 전체를 `#8B0000`으로 채우고 흰색 글자로 위험 레벨 명시.
    *   Moderate: `System Warning Amber` 색상 그라디언트 사용.

### 2. 경고 메시지 모듈 (`WarningBanner`)
*   **위치:** 페이지 상단에 고정(Sticky Header)되어, Critical 상태일 때만 나타나야 함.
*   **내용:** "⚠️ **경고: 시스템 과부하 감지!** 즉각적인 생활 패턴 점검이 필요합니다." (Deep Crimson Red 텍스트 사용).

### 3. CTA 모듈 (`SystemErrorCTA`)
*   **변화:** 단순 버튼(Button) 형태가 아닌, 시스템 오류를 해결해야 하는 **'긴급 패치/업그레이드'** 버튼처럼 디자인되어야 함.
*   **Critical 상태 시 로직:**
    1.  사용자가 점수 확인 후 스크롤을 내릴 때까지 `SystemErrorCTA`는 회색 처리되며, 배경에 미세한 오류 노이즈(Noise/Glitch Effect)가 오버레이됨.
    2.  위험 레벨이 Critical로 판단되는 순간, CTA 버튼의 색상이 `#FFD700` (Accent Gold)으로 변하며 **'시스템 복구 패치 적용하기'** 문구가 활성화되고, 클릭을 강제 유도하는 애니메이션(Pulse/Shake)가 발생해야 함.

---
**개발 가이드 요약:** 모든 컴포넌트는 Deep Navy Blue와 Deep Crimson Red의 공학적 대비를 활용하여, 사용자에게 '정보'가 아닌 **'위기 경고'**라는 경험을 제공하는 것에 집중할 것.
</create_file>

📊 평가: 완료 — CEO 지시사항(Flowchart, 디자인 가이드라인, 로직 정의)을 충족시키며 개발자가 코딩에 필요한 모든 구체적인 스펙과 트리거를 문서화했습니다.
📝 다음 단계: Developer에게 위 문서를 전달하고, 코다리 에이전트가 작성한 `RiskScoreModule.tsx`와 연동하여 실제 UI/UX 테스트 환경을 구축해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\src\docs\funnel_design_spec_v1.md
