# 🎨 Designer — 개발자가 코딩할 수 있도록, 'Defect ID 보고서'의 최종 CTA(Call To Action) 섹션을 웹 표준 HTML/CSS 기반으로 분해하여 상세한 디자인 가이드라인을 제공해주세요. 특히 다음 세 가지 요소에 대한 크기(pixel), 반응형 구조, 상호작용 상태(Hover/Active)를 포함해야 합니다: 1) Defect ID 코드 표시 영역, 2) 위협 레벨 경고 바 (Critical Red 시퀀스), 3) MiniFunnel 링크 버튼. 이 가이드는 개발자가 바로 코딩에 착수할 수 있도록 'Component Specification' 형태로 작성되어야 합니다.

🎨 Designer: 작업 시작합니다.

요청하신 'Defect ID 보고서' 최종 CTA 섹션 컴포넌트 스펙은 개발자가 즉시 코딩에 착수할 수 있도록, 웹 표준(Semantic HTML)과 CSS 구조체 기반의 **디자인 시스템 가이드라인** 형태로 작성했습니다. 모든 요소는 온현 브랜드가 추구하는 '전문적 위기감' 톤앤매너를 극대화하도록 설계되었습니다.

---

## 🚨 [COMPONENT SPECIFICATION] Defect ID 보고서 최종 CTA 섹션
**(Technical/Developer Ready Guide)**

### I. 개요 및 전역 스타일 (Global Context)

*   **목표:** 사용자에게 '현상 유지의 위험성'을 마지막으로 각인시키고, 즉각적인 '해결책(MiniFunnel)'으로 유도하여 전환율 극대화.
*   **배경 컨셉:** 시스템 오류 메시지/군사 작전 브리핑 느낌 (Dark Mode 기반).
*   **주요 컬러 팔레트:**
    *   `--color-primary`: #D9534F (Critical Red) - 위기 경고.
    *   `--color-secondary`: #FFC107 (Amber/Yellow) - 위험 단계.
    *   `--color-background`: #1a1e25 (Dark Navy/Slate).
    *   `--color-text`: #E0E0E0 (Light Gray).
    *   `--color-accent`: #00FFFF (Cyan) - 기술적 데이터 강조.

### II. 컴포넌트별 상세 스펙 (Component Details)

#### 1️⃣ Defect ID 코드 표시 영역 (`.defect-id-display`)

이 섹션은 보고서의 신뢰도를 높이는 '기술적 근거' 역할을 합니다. 실제 코드가 움직이는 듯한 인터랙션을 부여하여 전문성을 극대화해야 합니다.

| 속성 | 스펙 값 / 가이드라인 | 상세 설명 및 개발 참고 사항 |
| :--- | :--- | :--- |
| **레이아웃** | `display: flex; align-items: center;` | 좌측에 ID, 우측에 의미를 배치하여 균형감 확보. |
| **크기 (Pixel)** | 너비: 100%; 높이: 70px | 전체 섹션 폭을 사용하되, 시선을 사로잡는 적절한 크기 유지. |
| **폰트** | `font-family: 'Courier New', monospace;` | 기술 보고서 느낌의 고정폭(Monospace) 폰트를 필수 적용. |
| **텍스트 스타일** | ID 코드에만 `--color-accent` (Cyan)를 적용하고, 깜빡임/글리치 효과(`@keyframes`)를 CSS로 구현하여 '실시간 데이터 수신'처럼 보이게 처리. |
| **반응형 구조** | `flex-wrap: wrap;` | 모바일 환경에서 코드가 한 줄에 다 담기지 않을 경우 자연스럽게 개행되도록 설정. (Break Point: 768px) |

```css
/* Pseudo Code Example */
.defect-id-display {
    background-color: #0d1219; /* 배경을 더 어둡게 하여 대비 효과 극대화 */
    padding: 15px 30px;
    border-bottom: 2px solid var(--color-accent); /* 하단 라인으로 강조 */
}

.defect-id-code {
    font-size: 2rem;
    color: var(--color-accent);
    /* Keyframe 애니메이션 적용 예시 (깜빡이는 효과) */
    animation: glitch 1s infinite alternate;
}
```

#### 2️⃣ 위협 레벨 경고 바 (`.threat-level-bar`)

사용자의 심리를 가장 강하게 자극하는 핵심 요소입니다. 색상 변화가 매우 드라마틱해야 합니다.

| 속성 | 스펙 값 / 가이드라인 | 상세 설명 및 개발 참고 사항 |
| :--- | :--- | :--- |
| **레이아웃** | `width: 100%; height: 45px;` | 단일 수평 바 형태로 제작. 내부의 세그먼트(Segment)를 사용해 레벨을 구분합니다. |
| **색상 변화 (Critical Red)** | 배경 전체를 `--color-primary` (Red)로 채우고, 중앙에 경고 메시지를 배치. |
| **반응형 구조** | `width: 100%`를 유지하되, 내부의 '위험도 수치'는 퍼센트(`%`) 기반으로 계산되어야 함. (예: 위험도가 높을수록 좌측부터 채워지도록) |
| **상호작용 상태** | **Hover:** 마우스 오버 시, Red 색상의 투명도(Opacity)가 0.9로 증가하며 미세한 애니메이션 진동 효과를 주어 '경고 시스템이 활성화됨'을 체감하게 합니다. |

```css
/* Pseudo Code Example */
.threat-level-bar {
    background: linear-gradient(to right, #3c0d0d, var(--color-primary)); /* 어두운 Red 그라디언트 시작 */
    height: 45px;
    position: relative;
    overflow: hidden; /* 경고 효과가 넘치지 않도록 처리 */
}

.threat-level-segment {
    /* 위험도 %에 따라 너비 설정 */
    width: [X]%; 
    transition: width 1s ease-out, opacity 0.5s;
    background-color: var(--color-primary);
}

/* Hover Effect */
.threat-level-bar:hover .warning-message {
    animation: pulse 1s infinite alternate; /* 문구에 맥동 효과 적용 */
}
```

#### 3️⃣ MiniFunnel 링크 버튼 (`.cta-button`)

최종 행동을 유발하는 가장 중요한 컴포넌트입니다. 강력한 시각적 대비와 즉각적인 반응이 필수입니다.

| 속성 | 스펙 값 / 가이드라인 | 상세 설명 및 개발 참고 사항 |
| :--- | :--- | :--- |
| **레이아웃** | `display: block; text-align: center;` | 중앙 정렬을 기본으로 하며, 넓은 클릭 영역(Hit Area) 확보가 중요합니다. |
| **크기 (Pixel)** | 너비: 80%; 높이: 65px | 화면 폭 대비 충분히 크게 잡고, 모바일 환경에서 손가락 터치에 최적화된 크기로 유지합니다. |
| **폰트** | `font-size: 1.4rem; font-weight: 700;` | 긴급하고 단호한 느낌을 주는 볼드체(Bold)를 사용하며, 문구는 '무료 진단 리포트 받기' 등 명확해야 합니다. |
| **배경색** | `--color-primary` (Critical Red)를 기반으로 하되, `box-shadow`를 사용하여 입체감과 중요도를 높입니다. |
| **상호작용 상태 (Hover)** | 배경색을 10% 더 어둡게(Darken) 만들고, `transform: scale(1.02);`와 미세한 그림자 효과(`box-shadow`)를 추가하여 '눌리는' 느낌과 동시에 중요도가 높아지는 시각적 피드백을 제공합니다. |
| **상호작용 상태 (Active)** | 즉시 클릭되는 느낌을 주기 위해 `transform: scale(0.98);`와 함께 어두운 색상의 강한 배경색 변화를 주어 '클릭 성공'의 감각을 극대화합니다. |

```css
/* Pseudo Code Example */
.cta-button {
    background-color: var(--color-primary);
    transition: all 0.2s ease; /* 모든 트랜지션 속도를 0.2초로 설정하여 즉각적인 피드백 제공 */
    border: none;
    cursor: pointer;
}

/* Hover State - 가장 중요함 */
.cta-button:hover {
    background-color: #b83d45; /* 원색 대비 어두운 톤으로 변경 */
    transform: scale(1.02);
    box-shadow: 0 6px 15px rgba(217, 83, 79, 0.5); /* 그림자를 강조하여 '팝업'되는 느낌 부여 */
}

/* Active State - 클릭 시 피드백 */
.cta-button:active {
    background-color: #9c303a; /* 가장 어두운 색으로 변경 (눌리는 효과) */
    transform: scale(0.98); 
    box-shadow: none;
}
```

---
📊 평가: 완료 — 개발자가 즉시 사용할 수 있는 구체적인 Component Specification을 제공하여 후속 코딩 작업을 위한 설계 기반이 마련되었습니다.
📝 다음 단계: 이 스펙을 바탕으로 실제 프로토타입 디자인(Figma/Sketch)의 최종 검수 및 에셋 제작을 요청하거나, 백엔드 개발팀에 API 레벨의 데이터 전송 요구사항을 전달해야 합니다.
