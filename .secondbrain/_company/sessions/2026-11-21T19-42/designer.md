# 🎨 Designer — Instagram 릴스 포맷에 최적화된 '시스템 실패 보고서' UI/UX 애니메이션 애셋 키트(Asset Kit)를 최종 확정해 주세요. 이 키트는 (1) Defect ID 코드 표시 모듈, (2) 위기 레벨 변화 시퀀스 배경 컴포넌트, (3) MiniFunnel CTA 배너의 세 가지 핵심 요소로 구성되어야 하며, 모든 애셋은 릴스(9:16 비율)에 바로 적용 가능하도록 레이어 구조와 사용 매뉴얼을 포함해야 합니다.

🎨 Designer: 작업 시작합니다. CEO님의 지시에 따라, '시스템 실패 보고서'의 핵심 애니메이션 애셋 키트(Asset Kit)를 최종 확정하여 전달합니다. 이 애셋들은 Instagram Reels 포맷(9:16 비율)에 최적화되어 있으며, 개발팀이 즉시 구현 가능한 구조와 명확한 사용 매뉴얼을 포함했습니다.

이번 애셋 키트는 단순한 디자인 에셋 모음이 아니라, **사용자에게 '위기감 증폭'과 동시에 '전문적인 해결책 제시'라는 이중 감정을 유도하는 인터랙티브 시스템** 그 자체입니다.

### 📂 산출물: System Failure Report Asset Kit (9:16)

<create_file path="assets/system_failure_report_kit_manual.md"># 🚨 온현 MiniFunnel UI/UX 애셋 키트 최종 가이드라인
**프로젝트:** Instagram Reels - Defect ID 기반 시스템 실패 보고서
**목표:** 시청자에게 높은 '위기감(Anxiety)'을 주입하고, 전문 솔루션(MiniFunnel)으로의 전환율 극대화.
**포맷:** 9:16 (1080px x 1920px). 모든 애셋은 After Effects 또는 Framer를 기준으로 레이어 분리 원칙을 적용했습니다.

---

## I. 핵심 구성 요소 목록 및 스펙

| No. | 컴포넌트명 | 역할 | 주요 애니메이션/상태 | 필수 포함 레이어 |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Defect ID 코드 모듈 (DIDC)** | 사용자의 문제점(Pain Point)을 '시스템적 오류'로 정의. 전문성 부여. | 스캔라인 효과, 글리치(Glitch), 깜빡임, 텍스트 진동. | 배경(Grid/Scanline), Defect Code Text, Severity Level Indicator (색상 변화). |
| **2** | **위기 레벨 배경 컴포넌트 (CRB)** | 시청자의 불안감과 전문적 권위를 배경 색상으로 표현. 스토리 전개에 맞춰 단계적으로 변함. | CSS Transition/Keyframe 기반의 부드러운 색상 전환, 주기적인 플래싱 효과. | Background Gradient Layer, Risk Score Overlay Mesh, Flashing Indicator (Opacity). |
| **3** | **MiniFunnel CTA 배너 (CTA)** | 위기 상황에서 유일한 해결책을 제시하며 행동 유도. 긴급성과 신뢰성 강조. | 줌 인/아웃 효과, '클릭' 버튼의 입체적 반응(Hover Effect), 시선 집중형 애니메이션. | Main Background, Headline Text, Subtext (솔루션 요약), Call-to-Action Button. |

---

## II. 컴포넌트별 상세 디자인 브리프 및 구조

### 1. Defect ID 코드 모듈 (DIDC)
*   **레이어 구조:**
    *   `L01_Background`: 어두운 네이비 배경 + 미세한 격자(Grid) 패턴 (Dark Navy #1A233B).
    *   `L02_Scanline`: 수평으로 이동하는 가상의 스캔라인 효과. 주기적/비규칙적 애니메이션 적용.
    *   `L03_Code_Text`: Defect ID 코드 텍스트 (예: `ERROR_CVT_4060`). 글리치 및 진동 필터 적용.
    *   `L04_Severity_Indicator`: 심각도 표시 (초기: Yellow/Orange $\rightarrow$ 최종: Red).

*   **핵심 애니메이션 로직:**
    1.  **(Enter)**: 화면에 코드가 나타날 때, 텍스트가 순간적으로 `[DATA CORRUPTED]` 글리치 효과와 함께 진입합니다.
    2.  **(State Change)**: 위기 레벨이 높아지면 (`CRB`와 동기화), 코드 주변의 **Scanline 간격이 좁아지고** 깜빡임 주기가 빨라집니다 (공포감 증폭).

### 2. 위기 레벨 배경 컴포넌트 (CRB)
*   **색상 팔레트 및 상태 정의:**
    *   **Level 1 (안정):** Deep Navy (`#1A233B`) - 전문성, 낮은 위험.
    *   **Level 2 (주의/경고):** Amber/Orange Gradient (`#FFC107` $\rightarrow$ `#FFA000`) - 주의, 문제 발생 가능성 인지.
    *   **Level 3 (위기/최대 위험):** Critical Red (`#A3152B`) - 시스템 붕괴 직전, 즉각적 행동 필요(MiniFunnel 유도).

*   **애니메이션 로직:**
    *   `Background Gradient`: 리스크 스코어에 따라 배경의 색상 그라디언트가 **선형적이지 않고 점진적으로 변화**해야 합니다. (예: Level 2 진입 시, Deep Navy에서 Amber로 서서히 '오염'되는 느낌).
    *   `Flashing Effect`: Critical Red 상태 도달 시, 배경 전체에 무작위 간격의 플래싱 효과(Opacity Cycle)를 적용하여 공포 지점을 극대화합니다.

### 3. MiniFunnel CTA 배너 (CTA)
*   **레이어 구조:**
    *   `L1_Container`: 전용 하이라이트 배경 (미세한 빛 번짐 효과).
    *   `L2_Headline`: 해결책 제시 문구 (예: "Defect ID 진단, 3단계로 시스템 복원").
    *   `L3_Button`: CTA 버튼 (`지금 시스템을 점검하세요`).

*   **핵심 애니메이션 로직:**
    1.  **(Appearance)**: 배경이 가장 위험한 Critical Red에 도달했을 때, 이 배너가 **'강제 오버레이(Forced Overlay)'** 되며 화면 전체를 덮습니다. (시청자의 시선이 다른 곳으로 갈 수 없게 만듦).
    2.  **(Button Interaction)**: 버튼은 단순 클릭이 아닌, 마치 **시스템 'Execute' 명령을 내리는 듯한 햅틱 피드백(Haptic Feedback)과 함께 미세하게 진동**하며 사용자를 유도합니다.

---

## III. 최종 사용 매뉴얼 및 워크플로우

1.  **초반부 (문제 제기):**
    *   CRB: Deep Navy $\rightarrow$ Amber로 부드럽게 전환 시작.
    *   DIDC: 코드가 서서히 노출되며 '데이터 이상 감지' 메시지를 출력합니다. (위협감 조성)
2.  **중반부 (문제 심화):**
    *   CRB: Amber $\rightarrow$ Critical Red로 빠르게 전이. 플래싱 효과가 발생하고 배경의 그리드 패턴이 빨간색으로 변조됩니다. (불안감 극대화)
3.  **후반부 (해결책 제시/MiniFunnel 유도):**
    *   CRB: Critical Red 유지.
    *   CTA 배너: 화면 중앙에 강제 오버레이되며, '지금 시스템을 점검하세요' 버튼이 가장 밝고 진동하는 상태로 고정됩니다.

</create_file>

---

📊 평가: 완료 — CEO님 지시에 따라 모든 핵심 요소와 작동 로직까지 포함한 최종 애셋 키트 가이드라인 및 사용 매뉴얼을 완성했습니다.
📝 다음 단계: 디자인 브리프를 기반으로 실제 릴스 콘텐츠 3종에 대한 구체적인 스크립트(Hook/Body)와 시각적 연출 포인트(Timing Markers)를 Writer 에이전트를 통해 생성해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\assets\system_failure_report_kit_manual.md
