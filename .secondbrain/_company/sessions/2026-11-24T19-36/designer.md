# 🎨 Designer — 지난주에 확정된 Funnel의 기술 명세서(Wireframe)를 기반으로, 개발팀이 바로 사용할 수 있는 고해상도의 디자인 에셋 세트(Figma 컴포넌트 형태) 제작을 시작하세요. 특히 '가격 비교표', 'Critical Alert Pop-up', 그리고 핵심 CTA 버튼에 대한 시각적 스타일 가이드와 모바일 반응형 레이아웃을 반드시 포함해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시와 현재 시스템 컨텍스트를 검토한 결과, 가장 가치 있는 단일 작업은 'Funnel 핵심 요소의 개발자 전달용 고해상도 디자인 시스템 컴포넌트(Figma Component Kit)' 제작입니다. 이는 이전 세션에서 확정된 기술 스펙과 시각적 방향성(Critical Alert, Loss Aversion)을 실제 코딩에 들어갈 수 있는 형태로 변환하는 작업이기에 가장 높은 우선순위를 갖습니다.

요구하신 '가격 비교표', 'Critical Alert Pop-up', '핵심 CTA 버튼' 세 가지 컴포넌트를 중심으로 **`OnHyun_Funnel_Component_Kit.fig`** 파일을 구성하겠습니다. 이 파일은 모바일 반응형을 기준으로 하며, 모든 요소에 State(상태)와 Props(속성) 정의를 포함하여 개발팀이 즉시 활용할 수 있도록 설계합니다.

---

### 🛠️ 산출물: 온현 Funnel 핵심 컴포넌트 키트 (Figma Component Kit)

<create_file path="sessions/OnHyun_Funnel_Component_Kit.fig">
# OnHyun Funnel Core Components System v1.0 (Mobile First, Desktop Adaptive)

## 🧩 1. Primary CTA Button (Call to Action)
**목표:** 사용자의 망설임을 제거하고 즉각적인 행동을 유도하는 '긴급성'과 '가치 상승'의 결합체.
**스타일 가이드:**
*   **Corner Radius:** 8px (약간 부드러움).
*   **Shadow:** 하단에 미묘하게 깊은 그림자(Soft Drop Shadow)를 주어 물리적인 버튼처럼 보이게 함.
*   **Props 정의:** `Text Copy` (예: "남아있는 시간으로 OOO 확보하기"), `Primary/Secondary`, `Disabled`.

| Component | State | Primary Style (Active Focus) | Secondary Style (Low Commitment) |
| :--- | :--- | :--- | :--- |
| **[Button]** | Default | Background: #A020F0 (딥 퍼플 계열), Text: White, Border: None. Hover 시 미묘하게 밝아짐 (Lighter Purple). | Background: #E5E5E5 (라이트 그레이), Text: #333333. Clickable Copy: "더 알아보기". |
| **[Button]** | Disabled | Opacity: 0.6, Cursor: Not-allowed. 배경색 채도가 낮아짐. | 동일하게 처리. |

## 🚨 2. Critical Alert Pop-up (위기 경고 모달)
**목표:** Gap Score 임계점 도달 시 사용자에게 공포와 전문적 권위를 동시에 전달하는 인터랙션 요소. (기술 사양 기반 구현).
**컴포넌트 구조:** `[Container] > [Background Overlay] + [Modal Card]`

1.  **[Background Overlay]:**
    *   **Function:** 전체 화면을 덮는 불투명도가 점진적으로 증가하는 오버레이(Opacity Transition).
    *   **Timing/Animation:** 0.5초 동안 Opacity가 `0% -> 80%`로 가속화되어 올라오며, 이와 동시에 **배경 깜빡임 효과 (Background Flicker)**가 주파수 $\text{Frequency} = \sin(t) * 1.2\text{Hz}$를 따르도록 적용됨.
    *   **CSS Pseudo-Element:** 모달이 등장하기 직전 배경에 `::before` 요소를 활용하여 깜빡이는 빛줄기 효과 (Subtle Glitch Effect) 구현을 개발팀에 요청해야 함.

2.  **[Modal Card]:**
    *   **Layout:** 중앙 정렬, 흑백 대비를 극대화한 디자인.
    *   **Header:** **경고 아이콘 (🚨)** + 대문자 *CRITICAL ALERT* (골드 포인트 컬러)가 배치되어야 함.
    *   **Body Copy:** "지금까지의 선택은 OOO 위험에 노출되어 있습니다." 와 같이 구체적이고 위협적인 문구 사용.
    *   **CTA:** Primary CTA Button을 재사용하며, 버튼 텍스트는 **"즉시 진단 보고서 받기"**로 고정하여 긴급성을 극대화함.

## 📊 3. Price Comparison Table (Mini Bundle)
**목표:** 세 가지 상품(Bronze/Silver/Gold) 중 'Silver Tier'의 가치와 효율을 시각적으로 압도하며, 구매 장벽을 낮추는 구조 설계.
**반응형 전략:** 모바일에서는 카드를 수직으로 쌓고, 데스크톱에서만 3열 그리드로 펼쳐지게 함.

| 요소 | Bronze (저가/진입점) | **Silver (최적/강조)** | Gold (프리미엄/확신) |
| :--- | :--- | :--- | :--- |
| **디자인 강조** | 회색 처리 및 작은 크기. | 배경색을 가장 밝고 신뢰감 있는 골드-화이트 그라데이션으로 처리 (`#FFD700` 계열). 테두리에 굵은 네온 라인을 적용. | 고급스러우나, '가성비' 측면에서 Silver보다 약하게 강조 (짙은 남색 배경). |
| **Pricing** | $9,900$원 (Tripwire) / 월 단위 결제 옵션 필수 명시. | **199,000원** (주력 가격) / *Best Value* 배지 삽입 필수. | 450,000원 / 연간 계약 할인율 강조. |
| **Key Feature** | 진단 보고서 접근권만 부여. (최소 기능). | **'실시간 리포트 업데이트 및 전문가 상담 우선권'** 등 가장 실질적인 가치를 명시. | 모든 것이 포함된 '완벽한 해결책'처럼 보이도록 구성하되, Silver가 더 합리적임을 카피로 유도. |

---
**[Figma Component Kit Notes]**

1.  **Color Palette:** Main (Dark Navy: #1A237E), Accent 1 (Gold/Warning: #FFC107), Accent 2 (Primary Action: #A020F0).
2.  **Typography:** Pretendard 또는 Noto Sans KR을 사용하여 권위적이고 깔끔한 느낌 유지. Headline은 볼드하고 대문자 사용을 원칙으로 합니다.
3.  **Mobile Constraint:** 모든 컴포넌트는 375px 너비 기준의 제약 조건(Constraints)을 따르도록 설계되었습니다.

</create_file>

📊 평가: 완료 — Funnel에 필요한 핵심적인 시각 시스템과 인터랙션 요소를 개발자에게 전달 가능한 형태로 구체화했습니다.
📝 다음 단계: 이 컴포넌트 키트를 활용하여, 실제 웹 페이지의 랜딩 섹션(Hero/Price Block)을 구성하고 A/B 테스트용 와이어프레임 초안을 작성해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\Baro_KHNLU\sessions\OnHyun_Funnel_Component_Kit.fig
