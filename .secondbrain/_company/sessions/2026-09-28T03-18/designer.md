# 🎨 Designer — Developer가 즉시 사용할 수 있도록, 'Deep Crimson Red' 배경 및 'SYSTEM OVERLOAD' 플래싱 효과(깜빡임/맥동)를 위한 최종 CSS/Tailwind 클래스 스니펫 세트를 제공하십시오. 특히 애니메이션의 시작점, 변화 속도(Easing), 그리고 공학적 전문성이 느껴지는 미세한 디테일(예: 데이터 스트리밍 오버레이 효과)까지 포함해야 합니다.

🎨 Designer: 작업 시작합니다.

요청하신 'Deep Crimson Red' 기반의 시스템 경고 및 애니메이션 CSS/Tailwind 스니펫 세트를 개발자가 즉시 사용할 수 있도록 구조화하여 제공하겠습니다. 이 코드는 단순히 색상을 입히는 것을 넘어, 공학적 전문성과 긴장감(Tension)을 유발하는 것이 목표입니다.

---

### 🚨 System Overload Visual Kit (CSS/Tailwind Snippets)

다음은 핵심 애니메이션과 스타일링이 포함된 CSS 및 Tailwind 클래스 스니펫입니다. 이 코드 블록 전체를 프로젝트의 `globals.css` 파일에 통합해야 합니다.

#### 1. Deep Crimson Red Color Palette & Variables
핵심 색상을 정의하고, 대비 효과를 위한 어두운 배경을 설정합니다.

```css
/* globals.css (or custom CSS file) */
:root {
  --color-deep-crimson: #8B0000; /* 핵심 경고색 */
  --color-alert-bg: rgba(139, 0, 0, 0.1); /* 은은한 배경 강조 */
  --color-system-text: #FFD700; /* 골드톤의 시스템 텍스트 (높은 가독성 확보) */
  --color-dark-void: #0A0A0E; /* 주 배경색 - 거의 검정에 가까운 진공 상태 */
}

/* Tailwind Utility 클래스 사용을 위해 변수 정의 */
.bg-deep-crimson { background-color: var(--color-deep-crimson); }
.text-system-gold { color: var(--color-system-text); }
```

#### 2. The Flashing / Pulsing Effect (SYSTEM OVERLOAD)
가장 핵심적인 요소입니다. `keyframes`를 사용하여 시각적 불안정성을 유도합니다.

```css
/* @keyframes for the core flashing effect */
@keyframes criticalPulse {
  0%, 100% { opacity: 1; box-shadow: 0 0 5px rgba(139, 0, 0, 0.8); }
  50% { opacity: 0.7; transform: scale(1.01); box-shadow: 0 0 15px rgba(255, 0, 0, 1); }
}

/* 적용 클래스 (Tailwind 조합) */
.animate-critical-pulse {
  animation: criticalPulse 1.5s infinite ease-in-out;
}
```

#### 3. Data Streaming / Glitch Overlay Effect
공학적 전문성을 부여하는 미세한 애니메이션입니다. 배경이나 중요 섹션에 적용하여 마치 데이터가 흘러나오는 듯한 느낌을 줍니다.

```css
/* @keyframes for the horizontal scan line/glitch effect */
@keyframes dataStream {
  0% { background-position: -200% 0; } /* 좌측에서 오른쪽으로 이동 시작 */
  100% { background-position: 200% 0; } /* 충분히 이동하여 반복되는 느낌 부여 */
}

/* 적용 클래스 (Tailwind 조합) */
.bg-data-stream {
  background-image: repeating-linear-gradient(
    90deg,
    rgba(139, 0, 0, 0.1), /* Crimson Red의 낮은 투명도 패턴 */
    rgba(139, 0, 0, 0.1) 2px,
    transparent 2px,
    transparent 4px
  );
  background-size: 8px 100%; /* 스트리밍 간격 설정 */
  animation: dataStream 6s linear infinite; /* 느리고 지속적인 흐름 */
}

/* 추가: Glitch Text Effect (텍스트가 깨지는 효과) */
@keyframes glitch {
  0% { transform: translate(0); }
  20% { transform: translate(-3px, -2px); text-shadow: 2px 0 #f44336; }
  40% { transform: translate(5px, 2px); text-shadow: -1px 0 #ffeb3b; }
  60% { transform: translate(-2px, 1px); text-shadow: 3px 0 #f44336; }
  80% { transform: translate(0); }
}

.animate-glitch-text {
    animation: glitch 0.5s steps(1) infinite alternate;
}
```

---

### 🚀 Single Most Valuable Task 결정 및 실행 계획

**[최종 결정된 작업]: Deep Crimson Red Funnel 전역 비주얼 언어 가이드 확립 (Visual Language Guide)**

지금까지의 모든 작업은 '시스템 과부하'라는 테마를 다루었지만, 각 채널(웹/앱/SNS)별로 이 시스템 경고 톤앤매너가 일관되게 적용되지 않으면 브랜드 전문성이 떨어집니다. 가장 가치 있는 다음 단계는 **Deep Crimson Red**와 **System Error** 콘셉트를 모든 마케팅 및 Funnel 접점에 통일적으로 녹여낸 '디자인 언어 가이드'를 완성하는 것입니다.

*   **목표:** Web/App UI의 Deep Crimson Red 경고 시스템을 Instagram 릴스, 배너 등 비(非)웹 콘텐츠에도 일관되게 적용할 수 있는 **시각적 규칙 세트**를 만듭니다.
*   **수행 에이전트:** 🎨 Designer (Lead Designer)가 주도하고, 📸 Instagram/📺 Leo가 검토합니다.

저는 이 가이드의 초기 초안을 작성하여 다음 단계로 넘기겠습니다.

<create_file path="~/Projects/OnHyun/System_Error_Visual_Language_Guide_v1.0.md"># 🚨 OnHyun System Error Visual Language Guide v1.0 (Draft)

## 1. 핵심 디자인 원칙
**목표:** 온현의 Funnel 전체에 걸쳐 '공학적 신뢰성'과 '생명의 긴급성'을 동시에 전달한다. 단순한 경고가 아닌, **"복잡한 시스템 모니터링 결과"**처럼 보이게 한다.

**핵심 테마 키워드:** System Overload, Deep Crimson Red (#8B0000), Data Leakage, Critical Alert, Binary Code.
**메인 컬러 팔레트:**
*   Primary Background: `#0A0A0E` (Dark Void)
*   Accent Color 1 (Alert): `#8B0000` (Deep Crimson Red) - *시스템 경고에 사용.*
*   Accent Color 2 (Data/Text): `#FFD700` (System Gold) - *핵심 데이터, 해결책 제시 시 강조.*
*   Secondary Text: `#AAAAAA` (Subdued Gray)

## 2. 타이포그래피 가이드라인
**폰트:** 전문성과 기계적 느낌을 주기 위해 모노스페이스(Monospace) 또는 기술적인 산세리프를 사용한다.
*   **Primary Font:** [Developer 선택 필요 - 예: 'Space Mono' 또는 'Roboto Mono']
    *   사용 영역: 시스템 메시지, 데이터 값, 경고 텍스트. (가장 높은 공학적 전문성 부여)
*   **Secondary Font:** [Developer 선택 필요 - 예: 'Inter' or 'Prestige']
    *   사용 영역: 본문 설명, 일반 카피라이팅. (높은 가독성 유지)

## 3. 필수 비주얼 컴포넌트 표준화
| 컴포넌트 | 목적/설명 | 디자인 지침 | 적용 예시 |
| :--- | :--- | :--- | :--- |
| **🚨 Alert Banner** | 임계점 초과 시 공지하는 최상위 경고. (Funnel, 웹 전체) | `Deep Crimson Red` 배경. `#FFD700`로 타이포그래피 강조. 양 끝에 미세한 데이터 스트리밍 애니메이션 적용. 텍스트는 모노스페이스체 필수. | "SYSTEM ALERT: HOMA-IR Threshold Exceeded" |
| **📉 Data Readout Card** | 위험 지표를 보여주는 카드 UI. (Funnel 핵심) | 다크 배경에 `Deep Crimson Red`의 '경고 레벨'을 시각적으로 표시. 수치 자체는 `#FFD700`으로 강조하고, 변화 추이(Trendline)만 애니메이션 효과 적용. | [HOMA-IR: 3.2] (Red Pulse/Flash) |
| **⚡️ Glitch Text Module** | 중요한 경고 문구나 슬로건을 전달할 때 사용. | 특정 키워드나 숫자 주변에 `animate-glitch-text`를 적용하여, 화면이 순간적으로 깨지거나 깜빡이는 효과 부여. 긴급성과 충격 극대화. | "당신의 시스템은 **[CRITICAL]** 상태입니다." |
| **⚙️ System Footer/Overlay** | 페이지 하단 또는 배경에 은은하게 깔리는 데이터 오버레이. | 투명도 낮은 `Deep Crimson Red`의 그리드 패턴과, 주기적으로 수평으로 지나가는 미세한 스캔 라인(`data-stream`)을 적용하여 '모니터링 중' 느낌 부여. | (전체 섹션 배경에 은은하게 배치) |

## 4. 채널별 변형 전략 (Adaptation Strategy)
*   **[Web/App Funnel]:** 모든 컴포넌트가 위 가이드라인을 따르며, 애니메이션 로직(Pulse/Glitch)이 핵심이다.
*   **[SNS Reel/Story]:** 배경 전체를 `#0A0A0E`로 설정하고, Deep Crimson Red의 경고 UI를 **프레임 오버레이** 형태로 강하게 삽입한다. 텍스트는 크고 충격적이며, 반드시 모노스페이스체를 사용해 전문성을 유지해야 한다.
*   **[Ad Banner]:** 가장 중요한 수치(예: HOMA-IR 값)만 `Deep Crimson Red`의 Pulse 효과를 적용하고, 나머지는 블랙/골드톤으로 구성하여 시선 집중도를 극대화한다.

---

📊 평가: 완료 — CSS 스니펫 제공 및 비주얼 언어 가이드라인 초안 작성을 통해 Funnel 개발에 필요한 핵심 디자인 자원과 방향성이 확립되었습니다.
📝 다음 단계: Developer에게 이 Visual Language Guide와 CSS 스니펫을 전달하여, 실제 Mini-App 프로토타입의 **컴포넌트 레벨 구현(Component Implementation)**을 요청해야 합니다.
