# 📝 CEO 종합 보고서

🎨 Designer: 작업 시작합니다.

CEO님의 지시사항을 검토했습니다. 현재까지의 모든 기획 및 와이어프레임 작업을 바탕으로, Mini Bundle Funnel LP가 개발팀에 즉시 전달되어 구현될 수 있는 **최종 디자인 시스템 에셋 키트(Component Kit)**를 완성하는 것이 가장 가치 높은 단일 작업입니다.

이는 단순한 시각 자료 제작을 넘어, 개발자가 코드를 작성할 때 참고해야 할 명확한 **컴포넌트 레벨의 기술 사양서** 역할을 수행해야 합니다. 따라서 Figma 파일 생성만으로는 부족하며, CSS/Tailwind 기반의 스타일 브리프와 사용 규칙까지 포함하여 산출하겠습니다.

최근 편집된 파일을 참조하여(`c:\Data\Project\Baro_KHNLU\sessions\OnHyun_Funnel_Component_Kit.fig`), 다음 세 가지 핵심 컴포넌트를 최종 확정하고, 그 개발 명세를 파일로 정리합니다.

---

### 💻 [산출물] Mini Bundle Funnel LP 디자인 시스템 에셋 키트 (Developer Ready)

**파일명:** `OnHyun_Funnel_Component_Kit_V3.md`
<create_file path="c:\Data\Project\Baro_KHNLU\sessions\OnHyun_Funnel_Component_Kit_V3.md"># 🎨 On현 Funnel LP 디자인 시스템 에셋 키트 (개발자 버전)

## 🚀 1. 핵심 스타일 가이드 및 변수 정의 (Design Tokens)

이 모든 컴포넌트는 다음의 공통 토큰을 기반으로 합니다. 개발 시 이 값을 기준으로 삼아 주세요.

| 속성 | 값 (Hex Code) | 역할/용도 | 비고 |
| :--- | :--- | :--- | :--- |
| **Primary Color** (Action) | `#B52A2A` | 가장 중요한 CTA, 경고 배너의 강조색. 손실 공포를 유발하는 깊은 버건디 톤. | `background-color: #B52A2A;` |
| **Secondary Color** (Trust) | `#3C4E60` | 섹션 배경, 신뢰성/전문성을 담는 헤더 및 보조 정보 박스. 다크 네이비 계열. | `background-color: #3C4E60;` |
| **Highlight Color** (Value) | `#FFD700` | 가장 큰 가치(Best Value), 핵심 혜택을 강조하는 골드 포인트. | `border-color: #FFD700;` |
| **Background Color** | `#1A1A2E` | 전체 페이지 배경색. 고급스러우면서 긴장감을 주는 어두운 계열. | `background-color: #1A1A2E;` |
| **Text Color (Primary)** | `#F0F0F5` | 본문 텍스트 색상. 높은 가독성을 보장하는 오프화이트. | `color: #F0F0F5;` |

**Typography Tokens:**
*   **Headline Font:** Pretendard / Noto Sans KR (Bold, Weight: 700) - 권위적이고 명확한 느낌.
*   **Body Font:** Pretendard / Noto Sans KR (Regular, Weight: 400) - 높은 가독성.
*   **Spacing Unit:** 8px Grid System 사용 필수 (`p-4`, `gap-y-8` 등).

---

## 💰 2. 가격 비교표 컴포넌트 (Pricing Comparison Table Component)

이 컴포넌트는 Funnel의 핵심 전환 지점입니다. 'Silver Tier'가 가장 넓고, 시각적으로 빛나도록 디자인되어야 합니다.

**[구조 및 레이아웃 명세]**
*   **레이아웃:** 3단 카드 구조 (Bronze | Silver | Gold). 전체 가로 폭을 최대한 활용하여 **비교감(Comparative Sense)** 극대화.
*   **핵심 인터랙션:** 마우스 호버 시, 선택된 티어의 모든 요소가 미세하게 커지고 (`transform: scale(1.03);`), 그림자 효과(`box-shadow`)와 함께 팝업 경고 문구가 나타나야 함.

**[기술 사양 (CSS/Tailwind)]**
*   **카드 배경:** `background-color: #252A40;` (전체 섹션보다 살짝 밝은 네이비).
*   **강조 티어 (Silver):** 가장 넓게 설정 (`flex-grow: 1.5;`). 테두리를 `#FFD700`으로 강조하고, 배경에 은은한 `box-shadow`를 주어 '최적의 선택'임을 암시합니다.
*   **가격 표시:** `$XXX/월`. 가격 숫자(`39,900`)는 **골드색(Highlight Color)**을 사용하며 가장 크게 배치합니다. (`font-size: 2.5rem;`).

```css
/* 예시 CSS - Silver Tier 호버 효과 */
.tier-silver {
  transition: all 0.3s ease-in-out; /* 부드러운 전환 애니메이션 필수 */
}
.tier-silver:hover {
  transform: translateY(-5px) scale(1.02); /* 살짝 떠오르는 효과 */
  box-shadow: 0 15px 30px rgba(255, 215, 0, 0.4); /* 골드 그림자 강조 */
}
```

---

## 🚨 3. Critical Alert Pop-up 컴포넌트 (FOMO 유발)

이 컴포넌트는 사용자에게 '지금 행동하지 않으면 손해'라는 감정을 즉각적으로 전달해야 합니다. 위치와 크기에 따른 가이드라인을 제시합니다.

**A. Exit Intent Banner (페이지를 떠나려는 순간):**
*   **목표:** 이탈 방지. 사용자가 스크롤을 내리거나 브라우저 닫기 시 트리거.
*   **디자인:** 화면 전체 폭(100%)에 걸친 고대비 배너. 배경은 Primary Color (`#B52A2A`)를 사용하여 충격감을 극대화합니다.
*   **카피 구조:** [긴급성/손실 공포] + [즉각적 해결책 제시] + [CTA 버튼].
*   **기술 사양:** `position: fixed;`와 JavaScript 이벤트 리스너(Exit Intent)를 사용하여 구현해야 합니다. 배너가 나타날 때 **빠른 진동 애니메이션(`animation: pulse 0.5s infinite;`)**을 적용하여 시각적 긴장감을 높입니다.

**B. In-Content Warning Pop-up (본문 내 삽입):**
*   **목표:** 특정 정보(예: 경쟁사 대비 위험성)를 본 직후, 전문가의 경고 메시지로 전환 유도.
*   **디자인:** 작은 크기(좌우 25% 폭), 배경은 다크 네이비(`Secondary Color`)에 `#FFD700` 테두리를 둘러 '공식적인 알림' 느낌을 줍니다.
*   **사용 지침:** 본문 그래프가 가장 위험한 데이터 포인트를 보여주는 직후(ex: "당신의 연금 수령액은 평균 대비 O% 낮습니다.")에 배치합니다.

---

## ✨ 4. CTA 버튼 및 배너 컴포넌트 (Call-to-Action)

CTA는 단순한 버튼이 아닌, 가치 상승 구조의 '결정적 순간'을 만들어내는 인터랙션입니다. 반응형과 긴급성을 최우선으로 설계합니다.

**A. Primary CTA Button (즉시 구매 유도):**
*   **기본 상태:** 배경 `#B52A2A` (Primary Color). 텍스트는 흰색(`#F0F0F5`).
*   **호버 상태:** 버튼 크기가 약간 커지고 (`transform: scale(1.05);`), 배경의 명암이 깊어지며 그림자 효과(`box-shadow`)를 주어 '누르면 반응할 것 같은' 물리적 느낌을 부여합니다.
*   **기술 사양:** `transition: all 0.2s ease;`를 반드시 적용하여 애니메이션의 부드러움을 유지해야 합니다.

**B. Lead Magnet Banner (Free Diagnosis 유도):**
*   **목표:** Funnel 상단이나 하단, 또는 회원가입 직전에 배치되어 '진단 보고서' 다운로드를 유도합니다.
*   **디자인:** 배경은 신뢰를 주는 다크 네이비(`Secondary Color`)와 대비되는 골드 포인트(`#FFD700`)를 사용하여 시선을 끌어야 합니다.
*   **카피 구조:** "🚨 **[위험 알림]** 5분 만에 당신의 재정적 위험도를 진단하세요." (손실 공포 극대화).

---

### 요약 및 개발 가이드라인

1.  **기술 구현 필수 요소:** 모든 컴포넌트에는 `rem` 또는 `px` 단위 기반의 명확한 Spacing Rule과 Hex Code가 주석으로 포함되어야 합니다.
2.  **반응형 원칙:** 모든 레이아웃은 모바일(375px 기준) 환경에서 100% 가독성을 유지해야 하며, 특히 가격 비교표는 세로 스택 구조로 자연스럽게 변환되어야 합니다.

</create_file>

📊 평가: 완료 — CEO의 지시사항을 모두 반영하여 개발자가 바로 사용할 수 있는 최종 컴포넌트 라이브러리 형태의 명세서를 작성함으로써 목표를 달성했습니다.
📝 다음 단계: 이 에셋 키트를 기반으로, Writer와 함께 **전체 LP 흐름에 맞는 카피라이팅(AIDA/Pain-Agitate-Solve)을 확정하고, 각 컴포넌트 배치 지점별 CTA의 최종 문구를 통일**시켜야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\Baro_KHNLU\sessions\OnHyun_Funnel_Component_Kit_V3.md
