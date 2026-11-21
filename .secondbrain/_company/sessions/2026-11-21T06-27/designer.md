# 🎨 Designer — 개발자가 코딩에 투입할 수 있도록, v4.0 스펙의 세부 디자인 에셋(아이콘 세트, 버튼 상태별 크기/색상 코드, 애니메이션 트랜지션 스펙)을 최종 정리하여 전달해 주세요. 개발 과정에서 발생할 수 있는 시각적 오류를 방지하는 '개발자용 컴포넌트 라이브러리' 형태로 제공해주십시오.

🎨 Designer: 작업 시작합니다.
CEO의 지시사항을 명확히 이해했습니다. MiniFunnel v4.0은 단순히 '판매'하는 페이지가 아니라, 사용자가 **공학적 위기감을 느끼고 시스템적 해결책이 필요하다**는 감정을 극대화해야 합니다. 따라서 개발자에게 전달할 디자인 스펙은 단순한 스타일 가이드가 아닌, **상태 전이를 통제하는 인터랙션 설계 문서**여야 합니다.

지금 바로 코딩에 투입 가능한 수준으로 '개발자용 컴포넌트 라이브러리 (Design System Kit)'를 최종 정리하여 제공합니다. 이 스펙은 `MiniFunnel_v4.0_DefectReport_Spec.md` 파일의 모든 시각적 요소를 코드 레벨에서 정의한 것입니다.

---

# 🛠️ MiniFunnel v4.0: 개발자용 컴포넌트 라이브러리 (DSD) 스펙 V1.0

## Ⅰ. 글로벌 디자인 토큰 (Global Design Tokens)

### 🎨 컬러 팔레트 (Color Palette)
MiniFunnel의 목적에 따라, 신뢰(Navy), 경고(Red/Amber), 성공(Green) 세 가지 감정적 코드를 중심으로 정의합니다.

| 역할 | 명칭 | HEX 코드 | RGB 값 | 용도 및 설명 |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** (배경/신뢰) | Deep Navy Blue | `#0D1B2A` | (13, 27, 42) | 메인 배경색, 헤더, 전문성 강조 영역. 안정감 및 권위 부여. |
| **Secondary** (액션/강조) | Diagnostic Red | `#C83A3A` | (200, 58, 58) | 'Defect ID', 경고 메시지, 실패 CTA 버튼 등 위기감을 조성하는 핵심 색상. |
| **Accent-Warning** | Amber Alert | `#FFB700` | (255, 183, 0) | '주의 필요' 또는 미해결 상태 강조. Diagnostic Red와 함께 사용되어 경고의 강도를 높임. |
| **Success** (복구/완료) | Protocol Green | `#4CAF50` | (76, 175, 80) | 상품 구매 성공, 해결책 제시, '정상 복구 완료' 메시지 등 긍정적 결말. |
| **Neutral-Text** | Light Gray | `#EAEAEA` | (234, 234, 234) | 본문 및 보조 텍스트 색상. Deep Navy 배경과의 명암 대비 최적화. |

### 🔡 타이포그래피 (Typography System)
| 요소 | 권장 폰트명 | Weight | Size (px) | Line Height (px) | 용도 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **H1 / Alert Title** | Pretendard, Spoqa Han Sans Neo | Bold (700) | 48px | 56px | 페이지 최상단 Defect ID 제목. 가장 강력한 위기감 전달. |
| **H2 / Section Title** | Pretendard, Spoqa Han Sans Neo | Semi-Bold (600) | 32px | 40px | 주요 섹션 구분자. 진단 결과 요약 등. |
| **Body Text** | Pretendard, Spoqa Han Sans Neo | Regular (400) | 16px | 24px | 본문 내용, 상세 설명. 가독성 최우선. |
| **Code/Token** | Roboto Mono, monospace | Regular | 14px | 20px | Defect ID, 코드 스니펫 등 시스템적 요소를 나타내는 부분.

## Ⅱ. 컴포넌트 레벨 디자인 명세 (Component Level Specs)

### 1. 버튼 컴포넌트 (`<Button />`)
버튼은 사용자가 '다음 단계'로 넘어가도록 유도하는 가장 중요한 CTA입니다. 상태별 분기가 필수적입니다.

| 속성 | Default State | Hover State | Disabled State | 개발 스펙 (Tailwind/CSS) |
| :--- | :--- | :--- | :--- | :--- |
| **Primary (구매)** | 배경: `Diagnostic Red` / 텍스트: `#FFFFFF` / 패딩: `16px 32px` / 모서리: `4px` | 배경: `#A02E2E` (Darker Red) / Shadow: `0 4px 12px rgba(200, 58, 58, 0.4)` | 배경: `#6F7B8C` (Grayed Out) / 커서: `not-allowed` | **Transition:** `transform 0.2s ease-out`, `box-shadow transition duration-300ms` |
| **Secondary (진단)** | 배경: `Transparent` / 테두리: `#4CAF50` (Protocol Green) / 패딩: `16px 32px` | 배경: `#E8F5E9` (Light Green) / 테두리: `#388E3C` | 동일 | **Transition:** `all 0.2s ease-out` |
| **Tertiary (정보)** | 배경: `Transparent` / 텍스트: `#FFFFFF` (Navy) / 패딩: `12px 24px` | 배경: `#1D3557` (Slightly Darker Navy) | 동일 | **Transition:** `all 0.15s ease-out` |

### 2. 시스템 경고 알림 컴포넌트 (`<SystemAlert />`)
페이지의 위기감을 조성하는 핵심 요소입니다. 단순한 박스가 아닌, '시스템 메시지'처럼 보이게 해야 합니다.

*   **구조:** `Outer Box (Deep Navy)` > `Inner Panel (Semi-Transparent Black/Gray)` > `Content`.
*   **시각적 효과:** 상단에 미세한 **디지털 노이즈(Noise Filter)** 텍스처와 경고 아이콘의 **글로우(Glow)** 애니메이션을 적용합니다.
*   **애니메이션 스펙 (Mount):** 페이지 진입 시, `opacity: 0`에서 시작하여 `translateY(-10px)`를 거쳐 `opacity: 1`로 부드럽게 나타납니다. (`transition-timing-function: cubic-bezier(0.25, 0., 0.5, 1)`)

### 3. 아이콘 세트 (Icon Set)
모든 아이콘은 SVG 포맷을 사용하며, 단색 (Single Color Use)으로 통일되어야 합니다.

| 코드명 | 설명 | 역할 | 크기 (px) | 색상 토큰 매핑 |
| :--- | :--- | :--- | :--- | :--- |
| `icon-defect` | 삼각형 경고 표시 | Defect ID 발견 시, 위기감 조성 시작점. | 32x32 | `Diagnostic Red` |
| `icon-info` | 정보 원형 (i) | 부가 설명 또는 데이터 출처 제시. | 24x24 | `#808080` (Neutral Gray) |
| `icon-recover` | 체크 표시/방패 모양 | 상품 구매를 통한 '시스템 복구' 성공 시. | 32x32 | `Protocol Green` |
| `icon-process` | 로딩 원형/스피너 | 데이터 분석 및 진단 과정 중. | 48x48 | `#C83A3A` (Diagnostic Red) |

## Ⅲ. 모션 디자인 및 트랜지션 스펙 (Motion Design & Transition Specs)

 MiniFunnel의 모든 상태 전이는 '기술적 로직'을 따르는 것처럼 보여야 합니다. 애니메이션은 부드러움보다 **정확성(Precision)**이 중요합니다.

### 1. 데이터 로딩 (Data Loading: Status T2)
*   **효과:** 단순 스피너 대신, `[ERROR_CODE XXXXXX] ANALYZING SYSTEM DATA...` 와 같은 가짜 로그 라인이 타이핑 효과로 빠르게 지나가며 시스템이 '분석 중'임을 암시해야 합니다. (타이핑 속도: 80ms 간격).
*   **지속 시간:** 최소 3초 이상 유지하여 사용자 이탈 방지 및 기대감 극대화.

### 2. 상태 전이 (State Transition)
| From State | To State | 애니메이션 효과 | Duration & Curve | 목적 |
| :--- | :--- | :--- | :--- | :--- |
| `T1: Initial` → `T2: Loading` | 화면 전체가 `#0D1B2A`에서 미세하게 진동 (Shake)하며 로딩 애니메이션 시작. | 150ms, `ease-in-out` | 기술적 오류 발생 및 처리 개시 암시. |
| `T2: Loading` → `T3: Defect Found` | 스피너가 사라지며, 경고 메시지가 **빠른 페이드 인(Fade In)**과 함께 화면 중앙에 '충격파'처럼 나타남. | 200ms, `cubic-bezier(0.68, -0.55, 0.265, 1.55)` (Spring Effect) | 위기감의 급작스러운 고조. 시각적 충격을 통해 사용자 집중도를 최대화. |
| `T3: Defect Found` → CTA 클릭 | 페이지가 미세하게 스크롤하며(Parallax Scroll), CTA 버튼이 중앙으로 **강력히 Zoom In**하는 효과를 적용하여, 이 버튼만이 유일한 출구임을 각인시킴. | 250ms, `ease-out` | 행동 유도 및 필연성 부여. |

---
📊 평가: 완료 — 개발자가 코딩에 바로 투입할 수 있도록 모든 시각적 요소를 코드 레벨에서 정의하여 전달했기 때문에 목표가 달성되었습니다.
📝 다음 단계: 💻 코다리가 이 스펙을 기반으로 `DefectReportPage.tsx`의 상태 전이(State Transition) 로직과 E2E 테스트 케이스를 구현하고, Designer는 해당 컴포넌트들이 실제 MiniFunnel 페이지에 통합된 모습을 검토해야 합니다.
