# 🎨 Designer — 지난 의사결정 로그에서 확정된 '시스템 경고 디자인 원칙 V2.0'을 기반으로, 유튜브 영상 및 MiniFunnel에 즉시 적용 가능한 통합 비주얼 에셋 패키지를 제작해 주세요. 이 패키지에는 다음 컴포넌트가 포함되어야 합니다: 1) 시스템 오류(Defect ID)를 표시하는 공통 '오류 코드 박스' 모듈, 2) 위기감을 고조시키는 '시스템 경고 바 (Crisis Alert Red)' 디자인 명세 및 적용 가이드라인, 3) Deep Crimson Red와 CLI 콘솔 스타일을 통합한 표준 타이포그래피/배경 패턴 세트. 모든 에셋은 개발팀이 코드로 구현할 수 있도록 컴포넌트별 상세 스펙과 사용 예시를 포함해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO 지시에 따라 '시스템 경고 디자인 원칙 V2.0'을 기반으로, 유튜브 영상과 MiniFunnel에 즉시 통합 가능한 핵심 비주얼 에셋 패키지를 제작합니다. 이 산출물은 단순한 가이드가 아닌, 개발팀이 직접 코드로 구현할 수 있도록 상세 컴포넌트 스펙(CSS/HTML 구조 및 로직)을 포함하는 **디자인 시스템 브리프** 형태로 제공됩니다.

현재 가장 필요한 작업은 '공통 디자인 언어'를 확립하여 모든 콘텐츠의 신뢰도와 권위를 극대화하는 것이므로, 이 작업을 최우선으로 진행합니다.

<create_file path="c:\Data\Project\FreqTrade\assets\DesignSystem_V2.0_FinalSpec.md"># 🚨 온현 (OnHyeon) 통합 비주얼 에셋 패키지 명세서 V2.0
## 목적 및 적용 범위
본 문서는 모든 콘텐츠(유튜브 영상, MiniFunnel 웹페이지, 블로그 포스팅 등)에 걸쳐 통일된 '공학적 위기감'과 '전문성'을 부여하기 위한 표준 컴포넌트 스펙입니다. 개발팀은 이 명세서를 기반으로 React/Vue 등의 프레임워크에서 재사용 가능한 모듈로 구현해야 합니다.

---
## 🎨 1. 공통 컬러 및 타이포그래피 시스템 (The Core Palette)

### 🔴 A. 색상 팔레트 (Color Codes)
| 용도 | 이름 | HEX Code | RGB | 역할 및 사용 원칙 |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Background** | Deep Navy (Navy-900) | `#121A2E` | 18, 26, 46 | 메인 배경색. 깊고 안정적이며 전문성을 부여함. 모든 UI의 기본 바탕이 됩니다. |
| **Alert/Danger** | Crisis Red (Crimson) | `#B30029` | 179, 0, 41 | *경고 및 위협* 메시지에 사용. 시스템 오류, 위험 신호에만 제한적으로 사용해야 함. |
| **Accent/Success** | Deep Crimson (Red-600) | `#8A0023` | 138, 0, 35 | 핵심 CTA 버튼, 강조 요소 등에 사용되는 메인 액센트 컬러. 경고보다 '해결책'에 가깝습니다. |
| **Text Primary** | Light Gray (White-900) | `#F0F4F7` | 240, 244, 247 | 본문 및 주요 제목의 기본 색상. 대비를 극대화하여 가독성을 확보합니다. |
| **Code/Secondary** | Console Green (Green-300) | `#A3D18C` | 163, 209, 140 | 코드 블록, 시스템 로그 성공 메시지 등 부가 정보를 표시할 때만 사용. CLI 스타일의 핵심 색상입니다. |

### 📜 B. 타이포그래피 가이드 (Typography)
*   **Font Stack:** `'Roboto Mono', 'Source Code Pro', monospace;`
    *   *이유:* 모노스페이스 계열은 코드, 데이터, 시스템 로그를 연상시켜 기술적이고 전문적인 분위기를 즉각적으로 조성합니다. 일반 텍스트에도 적용하여 통일감을 높입니다.
*   **Heading (H1/H2):** Deep Navy 배경 위에 White-900으로 표시하되, `font-weight: 700`을 적용하여 '명령어' 같은 느낌을 주도록 합니다.
*   **Body Text:** 가독성을 위해 일반 웹폰트(예: Noto Sans KR)를 사용하고, 모노스페이스는 코드 블록이나 시스템 메시지에 한정적으로 사용합니다.

---
## 💻 2. 핵심 컴포넌트 상세 명세 (The Components)

### 📌 컴포넌트 A: 오류 코드 박스 (Error Code Box - Defect ID Module)
시스템에서 발생하는 'Defect'를 시각화하는 가장 중요한 요소입니다. 전문성을 최대로 끌어올립니다.

**[구조적 스펙]**
*   **클래스명:** `.code-error-box`
*   **배경:** `Deep Navy (#121A2E)`에 약간의 어두운 그라디언트(Dark Gradient)를 적용하여 깊이감을 줍니다.
*   **테두리:** 좌측 상단에 `Crisis Red (#B30029)` 두께 2px 라인트를 강하게 삽입합니다 (시스템 경고 느낌).
*   **내부 레이아웃:** 3개 열 구조 (`[ID] - [Severity] - [Description]`)

**[HTML/Pseudo Code 예시]**
```html
<div class="code-error-box">
    <span class="defect-id">[DEFECT ID: E-C403]</span>
    <span class="severity">| SEVERITY: CRITICAL |</span>
    <p class="description">메커니즘 결함 설명. 이 오류는 사용자의 생활 패턴에 구조적 위험을 초래합니다.</p>
</div>
```

**[CSS 스펙 (핵심)]**
*   `border-left`: `2px solid #B30029;`
*   `.defect-id`: `color: #A3D18C; font-family: 'Roboto Mono', monospace; font-size: 1.2em; margin-right: 15px;`
*   `.severity`: `background-color: rgba(179, 0, 41, 0.1); padding: 3px 8px; border-radius: 3px; font-size: 0.9em;`

### 📌 컴포넌트 B: 시스템 경고 바 (Crisis Alert Bar)
페이지 상단 또는 특정 섹션에 위치하여 시청자/독자의 주의를 강제로 끌어당기는 요소입니다. (Sticky Header 기능 고려)

**[구조적 스펙]**
*   **클래스명:** `.crisis-alert-bar`
*   **배경:** `Crisis Red (#B30029)`를 꽉 채우고, 미세하게 어두운 노이즈 패턴(Noise Pattern)을 오버레이하여 '긴급'함을 강조합니다.
*   **텍스트:** 흰색(`White-900`)으로 중앙 정렬하며, `SYSTEM ALERT:` 접두사를 반드시 붙입니다.
*   **로직/상호작용:** 페이지 스크롤 시, 5초 후 자동으로 페이드 아웃되거나, 사용자가 특정 CTA(MiniFunnel)에 접근할 때만 강제로 유지되는 로직을 포함해야 합니다.

**[HTML/Pseudo Code 예시]**
```html
<div class="crisis-alert-bar">
    <span class="prefix">[SYSTEM ALERT: ]</span> 
    <p>현재 당신의 [Pain Point]는 구조적 결함(Structural Defect) 상태입니다. 즉각적인 진단이 필요합니다.</p>
</div>
```

### 📌 컴포넌트 C: CLI 콘솔/패턴 배경 (The Background Pattern)
웹페이지나 영상의 전반적인 분위기를 '운영 체제 인터페이스'처럼 보이게 만듭니다.

**[구조적 스펙]**
*   **배경:** `Deep Navy (#121A2E)`를 기본으로 하되, 배경 전체에 매우 낮은 투명도의 그리드 패턴(Grid Pattern)을 적용합니다 (Opacity: 3% ~ 5%).
*   **효과:** 마치 서버실이나 콘솔 화면처럼 보이는 시각적 질감입니다.
*   **사용처:** 섹션 구분선이나 중요한 정보가 배치되는 박스 영역의 배경으로 활용하여 '정보의 깊이'를 부여합니다.

---
## 🖥️ 3. 통합 적용 가이드라인 (Implementation Flow)

| 단계 | 컴포넌트 사용 순서 | 목적 및 효과 | 개발 지침 |
| :--- | :--- | :--- | :--- |
| **[Intro]** | `.crisis-alert-bar` $\rightarrow$ H1/H2 | 위기감 고조 (Attention Grab). 주제를 '문제'로 인식시킴. | 페이지 최상단에 위치시키고, 스크롤과 함께 페이드 아웃되도록 설계할 것. |
| **[Problem]** | `.code-error-box` $\rightarrow$ 본문 텍스트 | 문제의 전문적 정의 (Defect ID 제시). 단순 증상이 아닌 '시스템 결함'임을 인식시킴. | Defect ID와 메커니즘 설명을 분리하여 명확하게 보여줄 것. |
| **[Solution]** | `.deep-crimson-cta` 버튼 $\rightarrow$ CLI 패턴 배경 | 해결책 제시 및 행동 유도 (Action Trigger). 전문 솔루션으로의 전환을 유도. | CTA 섹션만 그리드 패턴과 `Deep Crimson` 톤을 강화하여 대비 효과를 극대화할 것. |

---
***[최종 산출물 경로]***: c:\Data\Project\FreqTrade\assets\DesignSystem_V2.0_FinalSpec.md
</create_file>

📊 평가: 완료 — CEO의 지시사항을 충족하는 수준 높은, 개발 가능한 통합 디자인 시스템 스펙 문서를 완성했습니다.
📝 다음 단계: 이 명세서에 따라 실제 UI 컴포넌트 시안(Mockup)을 제작하거나, Writer에게 콘텐츠 초안 작성 전 최종 검토를 요청하여 텍스트와 비주얼의 일관성을 점검해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\FreqTrade\assets\DesignSystem_V2.0_FinalSpec.md
