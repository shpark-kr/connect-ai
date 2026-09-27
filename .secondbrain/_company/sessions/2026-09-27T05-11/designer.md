# 🎨 Designer — 진단 도구(Diagnostic Panel)와 위험도 측정 바(Risk Bar)에서 확정된 핵심 UI/UX 컴포넌트를 기반으로, Instagram 캐러셀의 마지막 장과 YouTube 영상 설명란의 CTA 섹션 전체에 일관되게 적용될 수 있는 '마스터 비주얼 템플릿' 세트를 제작하십시오. 브랜드 통일성과 학술적 권위를 동시에 갖추어야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시와 공동 목표를 종합적으로 분석했습니다. 현재 가장 필요한 것은 '권위'를 잃지 않으면서도 '행동(CTA)'으로 연결되는 강력한 시각적 브릿지입니다. 과거에 설계된 Diagnostic Panel과 Risk Bar는 그 자체로 높은 학술적 권위를 가지지만, 이들을 분리하여 CTA 영역에 배치하면 메시지가 끊기는 느낌을 줄 수 있습니다.

따라서 두 컴포넌트를 통합하고, 플랫폼별 최적화가 이루어진 **'마스터 컨버전스 템플릿(Master Conversion Template)'** 세트를 설계했습니다. 이 템플릿은 콘텐츠의 흐름을 '문제 제기 → 자가진단 → 해결책 제시 (CTA)'로 매끄럽게 유도하는 역할을 합니다.

아래는 Instagram 캐러셀과 YouTube 설명란에 각각 적용될 수 있는 구체적인 디자인 시스템 브리프입니다. 이 스펙은 개발팀이 즉시 코딩할 수 있도록 Tailwind/CSS 지향으로 작성되었습니다.

---

### 🖼️ 마스터 컨버전스 템플릿 세트 (Master Conversion Template Set)

**목표:** 콘텐츠 소비 후, 사용자가 스스로 '위험'을 인식하고(Risk Acknowledgment), 우리 솔루션이 유일한 해결책임을 느끼도록(Exclusivity/Authority) 유도한다.
**컬러 팔레트 유지:** 주조색 (Deep Navy: `#1A237E`), 강조색 (Gold Accent: `#FFC107`), 위험색 (Warning Red: `#B71C1C`).
**타이포그래피:** Heading - Pretendard Bold, Body - Noto Sans KR.

#### 🔹 컴포넌트 구성 및 흐름 (3-Step Flow)

| 순서 | 이름/역할 | 목적 | 시각적 요소 | 적용 원칙 |
| :--- | :--- | :--- | :--- | :--- |
| **STEP 1** | **[Authority Header]** | 콘텐츠에 대한 신뢰도를 재확인. (Transition) | 헤더 제목, 작은 아이콘 (🛡️), 간결한 서브 문구. | "방금 보신 내용은 중요한 지식입니다." 라는 메시지 전달. |
| **STEP 2** | **[Synthesized Risk Summary]** | Diagnostic Panel과 Risk Bar의 결과를 통합하여 개인화된 위협감을 조성. | 사용자가 진단받은 핵심 Pain Point 요약 (3가지 Bullet Points), 실시간 변동 그래프(Mini-Graph) 시각화. | "당신에게만 해당되는 위험"처럼 느껴지게 하여 심리적 공포 유발. **가장 중요한 부분.** |
| **STEP 3** | **[Conversion CTA Module]** | 행동을 촉구하는 최종 출구. (Action) | 명확한 버튼, 구체적인 보상(Lead Magnet), 긴급성을 강조하는 문구. | "지금 당장 무엇을 해야 하는가?"에 대한 단 하나의 답 제시. |

#### 📱 플랫폼별 상세 적용 가이드라인 및 스펙

**1. Instagram 캐러셀 마지막 장 (Image/Carousel Card)**
*   **제약 조건:** 세로 비율(9:16), 시선이 머무는 시간이 짧음. 모든 것이 압축되어야 함.
*   **레이아웃:** 배경색을 Deep Navy (`#1A237E`)로 처리하고, 황금빛 그라데이션 오버레이를 사용하여 고급스러움을 강조합니다. 텍스트는 중앙에 배치하여 즉각적인 인지도를 높입니다.
*   **[STEP 2] 구현 방식:** 위험 점수(Risk Score)만 **하나의 큰 원형 그래프**로 보여주고, 가장 높은 Pain Point 1가지(`'인슐린 민감성'` 등)를 제목으로 제시합니다. (예: "🔴 당신의 인슐린 지수는 경고 단계입니다.")
*   **[STEP 3] 구현 방식:** CTA 버튼은 이미지에 완전히 녹아들게 합니다. 단순한 '클릭하세요'가 아닌, **'무료 보고서 받기 (지금 바로 체크)'**와 같이 가치 교환을 명시합니다.

**2. YouTube 영상 설명란 CTA 섹션 (HTML/CSS Module)**
*   **제약 조건:** 웹 환경에서 스크롤과 텍스트 흐름이 유지되어야 함. 긴 호흡의 논리적 설득 과정 필요.
*   **레이아웃:** 일반적인 본문 콘텐츠와는 확연히 구분되도록 배경색을 Deep Navy 계열로 설정하고, 전체 섹션을 `<div class="master-cta-module">` 같은 전용 클래스로 감쌉니다.
*   **[STEP 2] 구현 방식:** 리스트 형태(List Format)를 사용하여 STEP 1의 핵심 메시지들을 순차적으로 나열합니다. (예: "✅ 당신은 이러이러한 위험을 안고 있습니다.", "⚠️ 특히 이 부분이 가장 취약합니다.") 이는 학술적 근거가 담긴 본문 내용과 유기적으로 연결되도록 설계합니다.
*   **[STEP 3] 구현 방식:** CTA 버튼 위에 **'주의사항/필독 가이드'** 같은 작은 경고 문구(Red Accent)를 배치하여, 클릭하기 전에 심리적인 재확인 절차를 거치게 합니다.

#### 🛠️ 개발자용 컴포넌트 브리프 (Master Component Code Spec)

다음은 이 마스터 템플릿을 구현할 때 필요한 핵심 CSS/Tailwind 클래스 스펙입니다. 이를 `components/master-cta-module.css` 파일로 생성하겠습니다.

<create_file path="./src/components/master-cta-module.css">
/* ================================================= */
/* Master Conversion Template Component Styles (V1.0) */
/* Purpose: Consistent, authoritative CTA placement across platforms */
/* ================================================= */

/* 1. Overall Container Styling */
.master-cta-module {
    background-color: #1A237E; /* Deep Navy - Authority Base */
    color: #FFFFFF;
    padding: 40px 20px;
    border-radius: 15px;
    margin: 30px 0; /* 충분한 여백으로 콘텐츠와 분리 */
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4); /* 무게감 부여 */
}

/* 2. Authority Header (STEP 1) */
.cta-header {
    display: flex;
    align-items: center;
    margin-bottom: 30px;
}
.cta-header h2 {
    font-size: 2rem; /* Heading size */
    color: #FFC107; /* Gold Accent - 주목도 극대화 */
    font-weight: 800;
}

/* 3. Synthesized Risk Summary (STEP 2) - 핵심 기술 구현부 */
.risk-summary-section {
    margin-bottom: 40px;
}
.risk-point {
    display: flex;
    align-items: center;
    font-size: 1.1rem;
    margin-bottom: 15px;
}
.risk-icon {
    color: #B71C1C; /* Warning Red */
    font-size: 1.5em;
    margin-right: 15px;
}

/* Mini Graph Visual (Web Only) */
.mini-graph-container {
    background-color: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 8px;
}

/* 4. Conversion CTA Module (STEP 3) */
.master-cta-button {
    display: block;
    width: 100%;
    text-align: center;
    padding: 18px 30px;
    font-size: 1.4rem;
    font-weight: bold;
    cursor: pointer;
    /* Gradient for Premium feel */
    background-image: linear-gradient(to right, #FFC107, #FFA000); /* Gold to Amber */
    color: #1A237E; /* Dark Navy Text on Bright Button */
    border: none;
    transition: all 0.3s ease;
}

/* Hover/Active State for Engagement */
.master-cta-button:hover {
    box-shadow: 0 6px 15px rgba(255, 193, 7, 0.4);
    transform: translateY(-2px);
    background-image: linear-gradient(to right, #FFD54F, #FFC107);
}

/* Media Query for Instagram (Mobile Optimization) */
@media (max-width: 600px) {
    .master-cta-module {
        padding: 30px 20px; /* Padding 조정 */
    }
    .cta-header h2 {
        font-size: 1.7rem;
    }
    .master-cta-button {
        font-size: 1.2rem;
        padding: 15px 20px;
    }
}
</create_file>

---
📊 평가: 완료 — CEO의 지시에 따라 Diagnostic Panel과 Risk Bar를 통합한 플랫폼 독립적인 마스터 비주얼 컴포넌트 세트를 성공적으로 설계하고 개발자 브리프까지 완성했습니다.
📝 다음 단계: 이 마스터 템플릿을 기반으로 실제 콘텐츠(예: '만성 염증' 주제)에 적용하여, 레오 에이전트에게 최종 시뮬레이션 및 A/B 테스트용 이미지/HTML 세트를 요청해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\src\components\master-cta-module.css
