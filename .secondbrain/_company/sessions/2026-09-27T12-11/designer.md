# 🎨 Designer — Mini-App Funnel 진단 도구의 최종 기술 명세서(Handoff Specification)를 완성하십시오. 이 명세서는 개발자가 바로 코딩에 적용할 수 있도록 상세한 SVG 구조, 컴포넌트별 상태 변화 로직, 그리고 점수 구간(0~100점)에 따른 애니메이션 및 색상 매핑 규칙을 포함해야 합니다. 특히 '위험도 측정 바'의 플래그 기반 경고 애니메이션(Pulse/깜빡임)과 A/B 테스트가 가능한 CTA 버튼 3종의 최종 디자인 사양을 확정하고, 모든 요소는 모바일 우선 접근 방식을 따르도록 정의하십시오.

🎨 Designer: 작업 시작합니다.

CEO님의 지시는 현재 프로젝트의 모든 디자인 및 개발 산출물의 기준이 되는 'Single Source of Truth'를 확립하는 핵심 단계입니다. Mini-App 진단 도구는 단순한 페이지가 아니라, **권위(Authority)와 위기감(Urgency)**을 동시에 전달하며 사용자를 Funnel로 유도하는 인터랙티브 시스템이어야 합니다.

따라서 이번 산출물은 일반적인 '디자인 시안'이 아닌, 개발팀이 코딩에 바로 적용 가능한 **'기술 명세서 (Handoff Specification)'** 형태의 문서를 작성하겠습니다. 이 문서는 모든 컴포넌트의 구조(SVG/HTML), 상태 변화 로직(CSS/JS), 그리고 비즈니스 규칙(점수 매핑)을 포함합니다.

---

### 🛠️ Mini-App Funnel 진단 도구: 기술 명세서 (Handoff Spec) v1.0

**[목표]**
Mini-App Diagnostic Panel의 최종 마스터 컴포넌트 세트를 확정하여, 개발자가 모바일 우선(Mobile-First) 원칙에 따라 즉시 코딩할 수 있도록 한다.

**[적용 기술 스택 기준]**
*   HTML/CSS (Tailwind CSS 클래스명 기반 구조화 권장)
*   JavaScript (상태 변화 및 애니메이션 로직 정의)
*   SVG (복잡한 그래프, 위험도 측정 바 등 벡터 그래픽 사용)

#### 1. 시스템 컬러 및 타이포그래피 가이드라인

| 요소 | 규격/값 | 설명 | 적용 영역 |
| :--- | :--- | :--- | :--- |
| **Primary Color** (긴급 경보) | `#B30000` (Deep Crimson Red) | 위험, 즉각적인 행동 유도. Mini-App의 핵심 색상. | Risk Bar Fill, Primary CTA Background |
| **Secondary Color** (주의/경고) | `#FFC107` (Amber Yellow) | 주의 단계. 61점 미만으로 점진적 경고를 줄 때 사용. | Caution Level Indicator, Hover State |
| **Tertiary Color** (안전/정보) | `#28A745` (Healthy Green) | 안전 범위 및 긍정적인 변화 유도 시 사용. | Safe Level Indicator, Success Message Background |
| **Background Color** | `#1A202C` (Dark Slate Navy) | 전문성, 신뢰감 부여. 전체 배경색. | Body Background |
| **Text Color** (Primary) | `#E2E8F0` (Off-White) | 가독성이 높은 주 텍스트 색상. | Headings, Main Copy |
| **Font Family** | Pretendard / Noto Sans KR | 전문적이고 현대적인 느낌의 고딕 계열 폰트 사용을 원칙으로 한다. | 모든 텍스트 요소 |

#### 2. 핵심 컴포넌트 정의 및 로직 (The Core Components)

##### A. 위험도 측정 바 (Risk Meter Bar) - SVG/CSS 구현 필수
이 컴포넌트는 사용자의 점수(0~100점)에 따라 시각적 경고를 발생시키는 가장 중요한 요소입니다.

*   **구조:** `<svg>` 태그 내부에 `path` 요소를 사용하여 점수에 비례한 채워진 바(Filled Path)를 구현합니다.
*   **로직 (JS 기반):**
    1.  **점수 입력:** Mini-App 진단 로직에서 0~100의 정수 값을 받습니다.
    2.  **색상 매핑:** 점수에 따라 `CSS Variable`을 업데이트하고, 이 변수를 Path Fill Color에 적용합니다.
        *   $Score \in [0, 30]$: `var(--risk-color): #28A745;` (Green)
        *   $Score \in [31, 60]$: `var(--risk-color): #FFC107;` (Yellow)
        *   $Score \in [61, 100]$: `var(--risk-color): #B30000;` (Red)
    3.  **애니메이션 플래그 (⚠️ 필수 구현):** 점수가 **61점 이상(빨간색 구간)**으로 떨어지는 순간, 해당 SVG Path 요소에 `is-critical` 클래스를 추가합니다. 이 클래스는 다음 CSS Keyframe 애니메이션을 트리거하여 위험 경고를 시각적으로 전달해야 합니다.

```css
/* CSS Keyframes for Critical Warning */
@keyframes pulse {
    0%, 100% { box-shadow: 0 0 5px rgba(179, 0, 0, 0.5); opacity: 1; } /* 은은한 발광 효과 */
    50% { box-shadow: 0 0 20px rgba(179, 0, 0, 1), 0 0 30px rgba(179, 0, 0, 0.8); opacity: 0.8; } /* 강한 깜빡임 효과 */
}

/* JavaScript로 추가될 클래스 */
.is-critical {
    animation: pulse 1s infinite alternate;
    transition: all 0.3s ease-in-out;
}
```

##### B. A/B 테스트용 CTA 버튼 (Action Buttons) - 3종 세트 확정

Mini-App의 최종 목표는 Mini-App 진단 도구로의 유도입니다. 이 목적에 맞춰 세 가지 수준의 커밋먼트를 가진 CTA를 설계하고, 각 상태(Hover, Active)에 대한 명세가 필요합니다.

| 종류 | 역할/목표 | 디자인 사양 (Mobile View 기준) | 상태 변화 로직 |
| :--- | :--- | :--- | :--- |
| **Primary CTA** (핵심 유도) | *최고 긴급성*을 전달하며, 바로 진단 도구로 이동하게 합니다. "지금 당장 확인하세요." | 배경색: `#B30000` (Deep Crimson Red). 텍스트: #E2E8F0. 모서리 라운딩(4px). **가장 크게, 가장 위에 배치.** | `Hover`: 배경을 약간 어둡게 (`#9e0000`), 그림자 효과 추가. `Active`: 클릭 시 미세한 축소 애니메이션 (Scale Down 98%). |
| **Secondary CTA** (정보 제공) | *중간 긴급성*. 진단 전, 관련 전문 정보를 읽도록 유도합니다. "더 자세히 알아보기" | 배경색: 투명. 테두리(Border): `#B30000`. 텍스트: `#B30000`. (Outline Button). | `Hover`: 배경을 연한 빨간 계열로 채우고, 테두리를 진하게 만듭니다. |
| **Tertiary CTA** (저위험 유도) | *가장 낮은 긴급성*. 이메일 수집 등 비-진단형 액션에 사용합니다. "전문가와 상담 예약" | 텍스트 링크 스타일. 밑줄(Underline)만 적용하거나, 버튼 형태로 가볍게 처리. (예: `Button/Link Group`). | `Hover`: 텍스트 색상 변경 또는 밑줄 두께 증가. |

#### 3. 레이아웃 구조 명세 (Mobile-First Blueprint)

전체 페이지는 모바일 환경을 최우선으로 고려하며, 전체 너비는 최대 420px로 제한합니다. 모든 섹션은 12-Column Flexbox Grid 시스템을 따릅니다.

**[Mini-App Flow Funnel 구조]**
1.  **Header (Full Width Banner):** 사용자 공포 유발 제목 및 Mini-App 로고 배치. (여백 확보)
2.  **Diagnosis Panel (Core Component):** 사용자가 직접 점수를 계산하고, 위험도 바가 실시간으로 업데이트되는 영역. **(기술 명세서의 핵심)**
3.  **Result Section:** 최종 점수와 함께 "당신의 건강 자본은 위험합니다" 같은 경고 문구 배치.
4.  **CTA Block (Action Funnel):** Primary CTA 버튼을 가장 눈에 띄게, 사용자가 스크롤 할 때마다 다시 상기시키는 위치에 고정(Sticky Footer)하거나 재배치합니다.

---
**[결론 및 다음 액션]**

위 명세서는 개발팀에게 전달될 최종 문서입니다. 이 구조를 바탕으로 실제 Mini-App 진단 도구의 UI/UX 흐름을 검증하고, 나머지 콘텐츠 채널(유튜브, 인스타)에 적용할 썸네일과 배너 디자인 시스템을 완성해야 합니다.

📊 평가: 완료 — CEO님의 지시사항인 '기술 명세서' 형태의 최종 산출물을 구체적인 로직과 구조로 확정하였습니다.
📝 다음 단계: 이 Mini-App 진단 도구의 핵심 요소를 활용하여, 유튜브 및 인스타그램에 사용할 **표준화된 썸네일/배너 디자인 시스템**을 완성하고, 모든 콘텐츠가 이 Funnel을 향하도록 비주얼 키트에 반영해야 합니다.
