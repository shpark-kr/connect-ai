# 🎨 Designer — Mini-App Funnel의 '시스템 리스크 스코어(System Risk Score)' 계산 로직과 Deep Crimson Red 경고 시스템을 통합한 최종 디자인 명세서(Design Spec)를 완성해 주세요. 이 명세서에는 HOMA-IR, MMIV 등의 데이터 스트리밍 오버레이 애니메이션, 임계값별 경고 UI의 인터랙션(Interaction), 그리고 개발자가 직접 구현할 수 있는 CSS/Tailwind 클래스 스니펫과 컴포넌트 분리 구조가 포함되어야 합니다. (MVP 코딩에 필요한 모든 비주얼 브리프를 제공할 것)

🎨 Designer: 작업 시작합니다.

CEO 지시에 따라 Mini-App Funnel의 핵심 로직인 '시스템 리스크 스코어'와 'Deep Crimson Red 경고 시스템'을 통합한 최종 디자인 명세서(Design Spec)를 완성했습니다. 이 문서는 개발자가 별도의 질문 없이 MVP 코딩에 착수할 수 있도록 **컴포넌트 분리 구조, 인터랙션 로직, 애니메이션 구현 스니펫**까지 완벽하게 제공합니다.

---

# 🧬 Mini-App Funnel: 최종 디자인 명세서 (v3.0)
## 시스템 리스크 기반 공학적 위협감 조성 컴포넌트 세트

### 🎯 목표 및 원칙 요약
*   **목표:** HOMA-IR과 MMIV 데이터를 활용하여 계산된 '시스템 리스크 스코어(R)'를 시각화하고, 이 수치에 근거한 공학적 위협감을 조성하여 사용자의 행동 변화(Mini-App CTA 클릭)를 강제합니다.
*   **핵심 원칙:** 단순 정보 전달이 아닌 **'공학적 시스템 오류/과부하 경고'** 프레임을 유지합니다. 모든 애니메이션은 긴급성(Urgency)을 극대화해야 합니다.

### 🎨 브랜드 컬러 및 타이포그래피 가이드 (재확인)
| 요소 | 색상 코드 (HEX) | 용도 | Tailwind Class 예시 |
| :--- | :--- | :--- | :--- |
| **배경색** | `#0A192F` (Deep Navy) | 메인 배경, 전문성 강조 | `bg-navy-900` |
| **강조색/위험 경고** | `#8B0000` (Deep Crimson Red) | 리스크 높음, 경고 메시지 플래싱 | `text-crimson`, `border-crimson` |
| **성공/안정색** | `#4CAF50` (Green Accent) | 낮은 리스크, 정상 범위 표시 | `text-success` |
| **데이터 텍스트** | `#CCD6F6` (Light Blue/Grey) | 기본 정보 표기 | `text-gray-200` |
| **타이포그래피** | Pretendard / Noto Sans KR | 전문적이고 가독성 높은 고딕체 | `font-sans` |

---

### 🧱 컴포넌트 분리 구조 (Component Breakdown)

Mini-App Funnel은 다음의 3가지 핵심 컴포넌트로 구성됩니다. 이들은 React/Vue 등의 프레임워크 기반으로 독립적으로 설계되어야 합니다.

#### 1. `<SystemRiskScoreDisplay />`
*   **기능:** 계산된 최종 리스크 스코어(R)와 해당 등급을 가장 눈에 띄게 표시합니다.
*   **위치:** Funnel의 최상단, 사용자 시선이 가장 먼저 머무는 곳.

#### 2. `<DataStreamOverlay />`
*   **기능:** HOMA-IR과 MMIV 지표가 계산되는 과정을 '시스템 데이터 스트리밍'처럼 애니메이션으로 보여줍니다. (공학적 위협감의 근거 제시)
*   **위치:** 리스크 점수 아래, 전문적인 분석 과정 시각화 영역.

#### 3. `<DeepCrimsonAlert />`
*   **기능:** 시스템이 위험 임계값을 초과했을 때, 공학적 과부하 경고 UI를 트리거합니다. (가장 중요한 CTA 유도 장치)
*   **위치:** 리스크 점수 표시 영역의 하단 또는 오버레이 형태로 전체 화면에 영향을 줍니다.

---

### ⚙️ 상세 명세 및 구현 로직 (Implementation Details)

#### A. `<SystemRiskScoreDisplay />` 명세서
| 항목 | 세부 내용 | 로직/규칙 | Tailwind Snippet 예시 |
| :--- | :--- | :--- | :--- |
| **Input** | `score: number`, `riskLevel: string ('L1'~'L3')` | - | N/A |
| **Visual Structure** | 중앙 집중형의 대형 스코어 카드. 배경에 미세한 노이즈 패턴 또는 회로 기판 이미지를 오버레이 합니다. | `relative overflow-hidden bg-[#0a192f] p-8 shadow-xl` |
| **Score Text (`R`)** | 가장 큰 폰트 크기(H1급)와 Deep Crimson Red를 사용합니다. 숫자가 로딩되는 듯한 애니메이션 효과가 필수입니다. | `text-[6rem] font-extrabold transition duration-500` (숫자별 Fade-in/Typewriter Effect 적용) |
| **Risk Level Label** | '정상 범위', '주의 단계', '위기 경보' 등 텍스트와 색상을 매칭합니다. | L1: `text-success`, L2: `text-yellow-500`, L3: `text-crimson` |
| **Interaction (L3)** | R $\ge$ 3.5 일 경우, 이 컴포넌트 전체에 미세한 진동(Shake) 및 배경 플래싱을 적용합니다. | CSS Keyframe Animation (`@keyframes flashing`) 기반으로 주기적인 `opacity: 0.8` 변동 부여. |

#### B. `<DataStreamOverlay />` 명세서 (핵심 애니메이션 구현)
*   **목적:** 데이터가 '측정되고 있음'을 느끼게 하여 신뢰도를 높입니다.
*   **구성 요소:** HOMA-IR(40%)와 MMIV Ratio(60%)의 값을 나타내는 두 개의 스트리밍 그래프/진행 바를 배치합니다.
*   **애니메이션 로직:**
    1.  데이터가 0부터 실제 값까지 **순차적으로 증가(Streaming)**하는 애니메이션을 적용해야 합니다. (단순히 숫자를 표시하면 안 됩니다.)
    2.  그래프의 Y축에는 '정상 범위 임계점'을 가로선으로 배치하고, 현재 값이 이 선과 비교되며 시각화됩니다.
*   **구현 스니펫:**
    ```tailwind
    /* CSS Keyframe Definition for Streaming Effect */
    @keyframes dataStream {
      from { width: 0%; }
      to { width: var(--final-value); } /* JavaScript에서 계산된 최종 너비 사용 */
    }
    .stream-bar {
        animation: dataStream 2s cubic-bezier(0, 0, 1, 1) forwards;
        width: 0%; /* 초기값 */
    }
    ```

#### C. `<DeepCrimsonAlert />` 명세서 (위기 경보 시스템)
*   **트리거 조건:** 시스템 리스크 스코어 $R \ge 3.5$ 일 때 **필수 활성화**.
*   **시각 효과:**
    1.  **전체 오버레이:** 화면 상단 또는 중앙에 반투명한 Deep Crimson Red 색상 레이어를 적용합니다. (`rgba(139, 0, 0, 0.2)`)
    2.  **플래싱 효과:** 이 레이어는 주기적으로 불규칙하게 플래시 해야 합니다. (예: `opacity`가 0.8 $\leftrightarrow$ 0.4 사이를 무작위로 변동).
    3.  **사운드 트리거:** (개발 환경에서) 경고음을 반드시 재생하도록 JS 로직을 추가합니다.
*   **CTA 배치:** 이 경고 UI의 가장 눈에 잘 띄는 위치(예: 하단 고정 바)에 Mini-App CTA 버튼이 강력하게 노출되어야 합니다.

---

### ✅ 종합 구조 다이어그램 (Pseudo Code Structure)

```html
<div class="funnel-container">
    <!-- 1. 배경 오버레이 및 경고 시스템 -->
    <div id="warning-overlay" class="deep-crimson-alert hidden"></div>

    <!-- 2. 리스크 스코어 디스플레이 (가장 중요) -->
    <section class="risk-score-display">
        <h1>시스템 리스크 점수</h1>
        <div id="R_score" class="system-score-text">3.5x</div> <!-- 애니메이션 적용 위치 -->
        <p>위험 등급: <span id="risk-level">위기 경보 (L3)</span></p>
    </section>

    <!-- 3. 데이터 스트리밍 시각화 영역 -->
    <div class="data-stream-container">
        <h2>데이터 진단 분석</h2>
        <div class="chart-row">
            <div class="stream-bar homa-ir" style="--final-value: 95%;">HOMA-IR (40%)</div>
            <div class="stream-bar mmiv" style="--final-value: 80%;">MMIV Ratio (60%)</div>
        </div>
    </div>

    <!-- 4. 최종 CTA 영역 -->
    <div class="mini-app-cta">
        🚨 시스템 과부하 상태입니다! 전문 진단이 필요합니다. 🚨
        <button class="primary-action-button deep-crimson-glow">지금 바로 Mini-App에서 점검받기</button>
    </div>
</div>
```

---
📊 평가: 완료 — 요청된 모든 구성 요소(컴포넌트 분리, 애니메이션 로직, CSS 스니펫)를 포함하는 개발자 수준의 최종 디자인 명세서를 완성했습니다.
📝 다음 단계: Developer가 이 명세서와 `c:\Data\Project\connect-ai\src\docs\funnel_design_spec_v1.md`에 기반하여 실제 코딩을 시작할 수 있도록, 필요하다면 **개발 환경 세팅 및 테스트 케이스 정의**를 요청해야 합니다.
