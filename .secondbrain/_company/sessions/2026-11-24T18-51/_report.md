# 📝 CEO 종합 보고서

🎨 Designer: 작업 시작합니다.
요청하신 Mini Bundle 판매 페이지(Landing Page)의 '기술 명세서 수준' 와이어프레임을 작성했습니다. 이 문서는 단순히 레이아웃을 보여주는 것이 아니라, 각 컴포넌트가 어떤 상태(State)와 속성(Prop)을 가져야 하며, 사용자가 어느 지점에서 심리적 압박(Loss Aversion)과 구매 욕구(Benefit Recognition)를 느끼도록 설계되었는지를 개발자 관점에서 명확하게 정의합니다.

아래의 와이어프레임은 **[섹션별 구조]**와 **[컴포넌트 기술 사양]** 두 가지 방식으로 분리하여, 프론트엔드 개발팀과 백엔드 기획팀 모두가 참조할 수 있도록 구성했습니다.

---

# 🚀 Mini Bundle 판매 랜딩 페이지: 기술 명세서 (Developer Spec Sheet)

## 📄 개요 및 목적
*   **페이지 목표:** 방문자가 '자신의 현재 상태(Pain Point)'를 인지하고 $\rightarrow$ 온현의 솔루션(Mini Bundle)이 **필수적임**을 깨달아 $\rightarrow$ 가장 높은 가치를 가진 Silver Tier에 결제하도록 유도하는 것.
*   **톤 앤 매너:** 권위성, 긴급 경고 (Dark Navy/Gold 기반), 전문적인 데이터 기반 설득력.
*   **핵심 전략:** 미조치 손실 공포(Loss Aversion)를 최상단에 배치하고, 가격 비교표에서 가치 대비 '최적의 선택'임을 극대화하여 구매 결정을 압박함.

## 📐 I. UX 흐름 및 섹션별 배치 (The Purchase Journey Flow)

| 섹션 번호 | 섹션 제목/목표 | 사용자 심리 단계 | 주요 컴포넌트 역할 | CTA 목표 |
| :---: | :--- | :--- | :--- | :--- |
| **Hero** | **긴급 경고 및 후킹 (Hooking)** | ⚡️ '위험하다'는 감정 자극 (Attention) | 크라이시스 배너, 헤드라인, Gap Score 진단 위젯(Mockup), CTA 버튼 (Urgency) | 즉각적인 문의 유도 (Low Friction) |
| **Section 2** | **Pain Point 증폭 및 근거 제시** | 🤔 '왜 나에게 필요한가?' (Value Recognition) | 데이터 비교 차트(Before/After), 전문가 코멘트 박스, 서비스 개요. | 솔루션에 대한 신뢰 구축 |
| **Section 3** | **솔루션 제시 및 가치 재정의** | ✨ '이것만 있으면 해결된다' (Aha Moment) | Mini Bundle 구성 요소 나열, 핵심 이점(Benefit) 강조 애니메이션. | 상품 자체에 대한 기대감 상승 |
| **Section 4** | **가격 비교표 (The Decision Point)** | ⚖️ '어떤 것이 최적의가?' (Comparison & Choice) | Bronze/Silver/Gold 티어 비교 테이블, 가격 차별화 요소 시각화. | Silver Tier로 유도 (Conversion Focus) |
| **Section 5** | **최종 클로징 및 리스크 제거** | ✅ '지금이 기회다!' (Commitment & Final Push) | FAQ, 보증/환불 정책 명시, 최종 CTA 버튼 (Loss Aversion). | 결제 직행 유도 (High Friction) |

---

## 💻 II. 컴포넌트 기술 사양 및 개발 가이드라인

### 1. [Hero Section] - 긴급 경고 & 후킹
*   **배경:** Dark Navy 계열, 전체 섹션에 미세한 '위험'을 상징하는 어두운 그라데이션 오버레이 적용.
*   **컴포넌트 A: 크라이시스 배너 (Crisis Banner)**
    *   `Prop`: `alert_level` (e.g., CRITICAL, WARNING)
    *   `State`: `:focus`, `:hover` 시 경고 텍스트가 미세하게 진동(Flicker Effect)해야 함.
    *   `Motion Spec`: 배너 배경이 점진적으로 어두워지며 긴장감을 조성하는 시간 기반 애니메이션 (e.g., `cubic-bezier(0.2, 1, 0.3, 1)`).
*   **컴포넌트 B: CTA 버튼 (Urgency Focus)**
    *   `Button Type`: Primary / High Contrast (Red Alert Color: `#D82B3A`).
    *   `Copy/Prop`: "🚨 지금 점검하세요! 놓치면 후회할 3가지 위험 신호" (Loss Aversion 카피).
    *   `Action Flow`: 클릭 시 **[팝업 CTA 1]** 즉시 활성화.

### 2. [Pricing Comparison Table] - 핵심 비교표 (Requirement 1)
*   **디자인 원칙:** Silver Tier가 가장 넓고, 중앙에 위치하며, 'Best Value' 배지(Gold Color)가 부착되어야 합니다. Bronze는 빈약하게, Gold는 비현실적으로 보이도록 연출합니다.
*   **레이아웃 구조 (3 Columns):** `Bronze | SILVER (Recommended) | GOLD`
*   **컴포넌트: 티어 비교 카드 (`TierCard`)**
    *   `Prop`: `tier_name`, `price`, `feature_list[]`
    *   `State`: **Silver Card**: 배경에 은은한 'Spotlight' 효과(가장 밝게)를 적용하여 시각적 집중 유도.
    *   `Feature Logic`: 각 티어별로 제공되는 기능이 단순히 나열되는 것이 아니라, `Bronze`에서 `Silver`로 넘어갈 때 **핵심 가치가 급증**하는 지점을 강조해야 합니다. (예: Bronze는 '기초 진단'만 가능 $\rightarrow$ Silver는 '맞춤 로드맵 설계' 가능).

### 3. [CTA 통합 및 변환 플로우] (Requirement 2 & 3)
페이지 전반에 걸쳐 3가지 카피를 다음과 같은 지점과 형태로 배치합니다.

| CTA 유형 | 위치 섹션 | 형태 | Prop/Copy 정의 | 전환 유도 논리 |
| :---: | :--- | :--- | :--- | :--- |
| **1. 긴급성 (Urgency)** | Hero Section 직후 | Primary Button + 팝업 모달 | "🚨 지금 바로 내 몸의 '위험 지표' 확인하기" | *즉각적 행동* 유도. 망설일 시간을 주지 않음. |
| **2. 이점 제시 (Benefit)** | Mini Bundle 구성 요소 설명 직후 | Secondary Button + 섹션 바너 | "✅ 전문가가 설계한 3단계 솔루션을 한 번에 받아보세요." | *논리적 확신* 부여. 상품의 가치를 머리로 납득시킴. |
| **3. 손실 공포 (Loss Aversion)** | Footer/최종 구매 직전 | Sticky Pop-up / 마지막 CTA 버튼 | "⚠️ 이대로 방치하면, 5년 뒤 당신의 관절은... [Gap Score 진단]" | *감정적 압박* 극대화. 결제하지 않을 경우 발생할 미래 위험을 상기시킴. |

---

## ✨ III. 최종 점검 및 개발자 체크리스트 (To-Do List)
개발팀에게 전달해야 할 필수 기능 목록입니다. 이 중 하나라도 누락되면 페이지의 설득력이 크게 저하됩니다.

1.  **[Must Have] 스크롤 기반 스토리텔링:** 사용자가 섹션 2(Pain Point)에서 섹션 4(Pricing)로 이동할 때, 배경 애니메이션이 단순한 색 변화가 아닌 **'위험도 수치 하락 $\rightarrow$ 안정화된 가치 상승'**의 시각적 흐름을 따라야 합니다.
2.  **[Must Have] 인터랙티브 비교:** 가격 비교표에서 사용자가 Bronze/Silver/Gold를 마우스 오버했을 때, 각 티어에 해당하는 '핵심 이점(Benefit)'이 팝업 형태로 즉시 보여져야 합니다 (Tooltip/Modal).
3.  **[Must Have] A/B 테스트 플래그 통합:** Hero 섹션의 CTA 버튼은 반드시 `cta_source=hero` 플래그를 통해 트래픽 추적 시스템에 연결되어야 하며, Funnel 진입 경로별로 전환율을 측정할 준비가 되어 있어야 합니다.

---
📊 평가: 완료 — CEO 지시사항과 Designer 개인 목표(표준화된 템플릿 제작)를 완벽하게 만족시키는 기술 명세서 형태의 와이어프레임을 완성했음.
📝 다음 단계: 이 와이어프레임 기반으로, 실제로 Figma 등에서 컴포넌트별 스타일 가이드와 고해상도 에셋(SVG/PNG)을 추출하여 개발팀에 전달해야 함.
