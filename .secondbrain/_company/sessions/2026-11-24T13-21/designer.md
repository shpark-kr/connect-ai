# 🎨 Designer — Developer가 구현할 Critical Alert 컴포넌트와 Gap Score CTA 페이지 전체를 포괄하는 최종 디자인 시스템 가이드라인을 완성하세요. 특히, 프로토타입에 적용될 모션 그래픽의 프레임워크(Transition/Interaction)와 폰트 스케일링 규칙을 명시하여 개발자가 즉시 활용할 수 있는 컴포넌트 라이브러리 형태로 정리해야 합니다.

🎨 Designer: 작업 시작합니다.

[CEO 지시]에 따라 Critical Alert 컴포넌트와 Gap Score CTA 페이지 전체를 포괄하는 최종 디자인 시스템 가이드라인을 완성하겠습니다. 이 문서는 단순한 디자인 스케치가 아니라, 개발팀이 즉시 프론트엔드 코드로 옮길 수 있도록 **컴포넌트별 CSS/JS 인터랙션 스펙**과 **모바일 퍼스트 원칙에 기반한 그리드 시스템**으로 구성해야 합니다.

가장 중요한 목표는 '공포를 통한 행동 유도'라는 감성적 목적을 시각적 위계(Visual Hierarchy)와 움직임(Motion)을 통해 기술적으로 구현하는 것입니다. 따라서, 가이드라인은 다음 3가지 핵심 섹션으로 분리하여 구조화하겠습니다.

1.  **Foundations:** 컬러/타이포그래피 시스템 (모든 요소의 기본 규칙).
2.  **Interaction System:** 모션 및 상태 변화 로직 (애니메이션 프레임워크).
3.  **Component Library:** 핵심 컴포넌트별 상세 구현 스펙 (개발 가이드).

가장 효율적인 전달 방식을 위해, 모든 내용을 통합한 `design_system_v2.0.md` 파일을 생성하겠습니다.

<create_file path="c:\Data\Project\Baro_KHNLU\src\assets\design_system_v2.0.md"># 🎨 온현 (Onhyun) Design System V2.0 가이드라인

## 🚀 개요 및 적용 원칙
본 시스템은 'Gap Score'를 통해 사용자에게 **미조치 손실의 위험성**을 인식시키고, 이를 해결하기 위한 필수적 서비스(CTA)로 자연스럽게 유도하는 데 초점을 맞춥니다. 모든 디자인 요소는 '권위성', '긴급성', '명확한 행동 지시'라는 3가지 원칙을 준수해야 합니다.

**✅ Mobile-First & 스크롤 기반:** 가장 중요한 CTA(Gap Score 변화, Critical Alert)가 화면 상단에 즉각 노출되도록 설계하며, 페이지 전체 구조는 세로 방향의 흐름(Flow)으로 감성적 몰입도를 유지합니다.
**✅ 톤앤매너:** 전문적인 의료/금융 정보를 다루므로, 과도한 애니메이션이나 밝은 색상 사용을 지양하고, '위험'이 높아질수록 명도가 낮아지고 채도가 높은 방향으로 시각적 압박감을 높여야 합니다.

---

## 🎨 I. Foundations (기반 시스템)

### 1. 컬러 팔레트 (Color Palette System)
Gap Score의 상태 변화에 따라 색상이 동적으로 변하는 **상태 기반(State-based)** 팔레트를 사용합니다.

| 이름 | Hex Code | 용도 | 설명 |
| :--- | :--- | :--- | :--- |
| **Primary Blue** (진단 결과) | `#007AFF` | 기본 CTA, 성공/안전 지표 강조 | 신뢰와 기술력을 상징하는 메인 컬러. |
| **Accent Gold** (전문성) | `#FFC300` | 핵심 요약, 주의 환기 (Warning) | 중요한 수치나 '꿀팁' 등 전문가적 정보를 강조할 때 사용. |
| **Success Green** (안전/정상) | `#5CB85C` | Gap Score가 안전 범위일 때 배경색 및 지표 색상 | 심리적으로 편안함과 안도감을 제공. |
| **Warning Orange** (주의) | `#FF9800` | Moderate Alert, 경고 신호 | '지금 주의해야 함'을 알리는 단계적 위험 구간. |
| **Critical Red** (위험/긴급) | `#D82B3A` | Critical Alert, 미조치 손실 공포 극대화 | 사용자의 행동 변화를 유도하는 핵심 감정적 자극 색상. *이 컬러는 절대 배경에만 쓰여서는 안 되며, 경고 요소와 포인트 라인으로 활용해야 합니다.* |
| **Background Dark** (Dark Mode/신뢰) | `#1A202C` | 페이지 메인 배경색 (다크 모드 권장) | 높은 전문성과 깊이감을 부여하여 정보의 신뢰도를 높임. |

### 2. 타이포그래피 시스템 (Typography System)
가독성이 최우선이며, 위계(Hierarchy)를 명확히 구분하는 것이 핵심입니다. (폰트 임베딩 시 `Inter` 또는 유사한 고대비 산세리프 계열 권장)

| 요소 | 크기 (Desktop/Mobile) | Weight | 색상 (Dark Background 기준) | 사용 목적 |
| :--- | :--- | :--- | :--- | :--- |
| **H1 (Hero Headline)** | 48px / 32px | Bold (700) | `#FFFFFF` | 페이지의 핵심 메시지. 충격적이고 직관적이어야 함. |
| **H2 (Section Title)** | 36px / 24px | SemiBold (600) | `#E2E8F0` | 섹션별 주제를 구분하고 시선을 모으는 역할. |
| **Body Large** | 18px / 16px | Regular (400) | `#CBD5E0` | 주요 설명을 담는 본문. 가장 가독성이 중요함. |
| **Body Small/Caption** | 14px / 12px | Regular (400) | `#A0aec0` | 출처, 법적 고지, 부가 정보 등 보조적인 내용. |
| **Metric Number** | 64px / 48px | ExtraBold (800) | *State Color* | Gap Score 또는 수치를 가장 크게 노출하여 시각적 충격 극대화. |

---

## ⚡ II. Interaction System (모션 및 상호작용 프레임워크)
애니메이션은 '정보 전달'의 보조 수단일 뿐, 주역이 되어서는 안 됩니다. **위험 지표가 변할 때만** 모션을 사용해야 합니다.

### 1. 상태 변화 로직 (State Transition Logic: Gap Score)
Gap Score 값이 낮아지거나(안전해지거나), 높아질 때(위험해질 때)의 애니메이션 정의입니다.

| 상태 | 색상 | 트랜지션/애니메이션 | 속도 및 Easing | 개발 스펙 |
| :--- | :--- | :--- | :--- | :--- |
| **Mild (양호)** | `Success Green` | Subtle Fade-in / None | N/A | 점진적인 변화는 부드러운 opacity 변화로 처리. |
| **Moderate (주의)** | `Warning Orange` | Gentle Pulsing (Soft Glow) | 1.5s 주기, Easing: Cubic-bezier(0.2, 1, 0.3, 1) | 배경 색상에 오렌지 계열의 부드러운 그림자 애니메이션 적용. |
| **Critical (위험)** | `Critical Red` | **Rapid Blink + Scale Up** | **0.5s 주기, Easing: Linear (급격함 강조)** | **[필수] 깜빡임(Blink)과 함께 폰트 크기가 1.1배로 커지면서 나타나야 함.** 시각적 충격을 최대로 유도하는 핵심 로직. |

### 2. CTA 버튼 인터랙션 (Button Interaction)
*   **Default:** 부드러운 `ease-out` 트랜지션. 마우스 오버 시 배경색이 어두워지고(Darken), 그림자(Shadow)가 깊어지는 효과.
*   **Click/Action:** 클릭 시 버튼이 2px만큼 눌리는 듯한(Press Down) **'햅틱 피드백'** 애니메이션과 함께, 짧은 시간 동안 `Primary Blue` 색상의 로딩 스피너가 전개되어야 합니다.

---

## 🧱 III. Component Library (핵심 컴포넌트 라이브러리)

### 1. Gap Score Metric Display (지표 시각화)
*   **구조:** 큰 숫자(`Metric Number`)를 중앙에 배치하고, 그 아래에 상태 변화 그래프(꺾은선/도넛 차트)를 배치합니다.
*   **핵심 인터랙션:** 사용자가 스크롤을 내릴 때(ViewPort 진입 시), 이 지표는 단순히 나타나는 것이 아니라 **'실시간으로 측정되어 수치가 올라가는 듯한 (Data Streaming)'** 애니메이션 효과가 적용되어야 합니다.

### 2. Critical Alert Panel (긴급 경고 패널)
*   **목적:** 사용자가 무시할 수 없도록 설계된, 페이지 내 가장 높은 시각적 위계의 컴포넌트입니다.
*   **스펙 (HTML/CSS):** 코다리가 구현한 MVP를 기반으로 하며, 다음 요소가 필수적으로 포함되어야 합니다.
    1.  **Header:** `Critical Red` 배경 위에 `H2` 폰트로 "🚨 위험 임계점 도달! 즉각적인 진단이 필요합니다." 노출. (반드시 깜빡임 애니메이션 적용).
    2.  **Core Message:** 위험의 원인(예: '근력 감소', '관절 불안정')을 구체적이고 공포감 있게 제시.
    3.  **Action Button:** `Primary Blue` 배경의 CTA 버튼이 가장 크고, 다른 요소보다 높은 대비를 가져야 합니다.

### 3. Standard CTA Button (Call to Action)
*   **Text:** '49,000원 Gap Score 진단 받기'와 같이 구체적인 가치와 비용을 명시합니다.
*   **레이아웃:** 모바일에서는 100% 너비로, 데스크톱에서는 콘텐츠 폭에 맞게 배치하되 시선이 분산되지 않도록 처리합니다.

</create_file>

📊 평가: 완료 — CEO 지시 사항(디자인 시스템 가이드라인, 모션 프레임워크, 컴포넌트 스펙)을 모두 포함한 개발자 레벨의 상세 문서를 완성했습니다.
📝 다음 단계: 코다리에게 이 디자인 시스템 파일을 기반으로 Critical Alert MVP에 정의된 모든 애니메이션 및 컴포넌트 스타일(CSS 변수/Keyframes)을 통합하여 적용하도록 지시해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\Baro_KHNLU\src\assets\design_system_v2.0.md
