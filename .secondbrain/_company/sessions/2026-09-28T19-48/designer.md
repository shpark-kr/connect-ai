# 🎨 Designer — 현재까지 논의된 모든 UI/UX 요소 (Deep Navy Blue, Deep Crimson Red, 모노스페이스 폰트 등)를 통합하여 'Mini-App Funnel 최종 자산 패키지(Final Asset Pack)'를 완성해 주세요. 이 패키지에는 HOMA-IR 경고 게이지 표준 컴포넌트의 애니메이션 스펙 시퀀스, 시스템 오류 코드 Glitch Effect의 구현 가이드라인, 그리고 모든 섹션에 사용될 폰트/컬러 HEX 코드가 명시된 최종 브랜딩 매트릭스가 포함되어야 합니다. 이 자산들은 개발자(코다리)가 즉시 프로토타이핑 및 E2E 테스트를 진행할 수 있도록 '개발자를 위한 문서' 관점에서 작성해야 합니다.

🎨 Designer: 작업 시작합니다. CEO님의 지시에 따라, 그동안의 모든 디자인 결정사항을 '개발자가 즉시 코딩할 수 있는' 수준의 최종 사양서로 통합하여 **Mini-App Funnel 최종 자산 패키지(Final Asset Pack)**를 완성하겠습니다.

이 문서는 단순한 브리프가 아니라, 개발자에게 전달되는 상세 기술 명세서이자 UI/UX 컴포넌트 라이브러리의 기준점이 되어야 합니다. 모든 요소는 Deep Navy Blue와 Deep Crimson Red의 조합을 통해 공신력과 위기감을 동시에 극대화하는 것에 초점을 맞춥니다.

---

<create_file path="assets/mini-app/MiniApp_Funnel_Design_System_Spec.md"># 🔴 Mini-App Funnel 최종 디자인 시스템 명세서 (Developer Kit v1.0)

**목표:** 사용자의 전문 지표 기반의 자가진단 페이지(Mini-App) 내에서 공신력 있는 위기감과 즉각적인 액션 유도(CTA)를 위한 모든 UI/UX 요소를 표준화한다.
**대상 개발자:** 코다리 (Frontend Developer)
**기준일:** 2026년 9월 29일

---

## I. 🎨 브랜드 및 스타일 매트릭스 (The Core System)

모든 컴포넌트는 다음의 HEX 코드와 타이포그래피 규칙을 준수해야 합니다. 이 코드는 절대 변경되어서는 안 됩니다.

### A. 컬러 팔레트 정의
| 용도 | 명칭 | HEX Code | 역할 및 설명 |
| :--- | :--- | :--- | :--- |
| **Primary Base** | Deep Navy Blue (DBN) | `#0A1931` | 배경색, 주요 섹션 구분선, 텍스트의 기본 색상. 전문성과 신뢰성 부여. |
| **Warning/Alert** | Deep Crimson Red (DCR) | `#B52F3E` | 위험 상태(Critical), 경고 메시지, CTA 버튼의 강조색. 위기감 극대화 핵심 컬러. |
| **Success/Safe** | Medical Teal (MTL) | `#4CAF50` | 정상 수치 구간, 긍정적 결과 시뮬레이션. (보조 색상) |
| **Accent/Highlight** | Gold Accent (GA) | `#FFC107` | 핵심 지표 강조, 중요 데이터 포인트 마커. 공신력 있는 하이라이트 효과. |
| **Background** | Off-Black Gray | `#12182B` | 메인 배경색. 깊은 밤하늘 같은 느낌으로 다크 모드를 완성함. |
| **Text/Foreground** | Light Slate | `#D4E3F0` | 기본 텍스트 색상. 가독성 최우선 확보. |

### B. 타이포그래피 정의 (Typeface Stack)
*   **Primary Font Family:** `monospace`, `Consolas`, `Courier New`, `monospace` (개발자 콘솔 느낌의 시스템 글꼴 사용을 강제하여 공학적 신뢰도 부여)
*   **Heading 1 (H1):** 2rem, Bold. DBN/Light Slate 조합. (섹션 제목)
*   **Body Text:** 0.95rem, Regular. Light Slate. (설명 및 본문 내용)
*   **Data Label/Code:** 0.8em, Semi-Bold. Monospace 필수 사용. (HOMA-IR 값, 오류 코드 등)

---

## II. 🔥 HOMA-IR 경고 게이지 컴포넌트 스펙 (Gauge Component Spec)

이 게이지는 단순한 바(Bar)가 아니라, **실시간 생체 데이터 모니터링 인터페이스**처럼 작동해야 합니다.

### A. 구조 및 레이아웃
1.  **Container:** 전체 폭의 90%를 차지하는 원형/반원형 형태의 Gauge 컴포넌트.
2.  **Base Line (Normal):** Deep Navy Blue로 설정된 기준선(예: HOMA-IR < 2.5)이 항상 표시되어야 합니다.
3.  **Data Fill:** 실제 측정값에 따라 선형적으로 채워지는 그래프 영역입니다.

### B. 상태별 애니메이션 시퀀스 (Sequence Animation)
| 구간 | 조건 (HOMA-IR 값) | 색상 (Fill Color) | 게이지 동작 스펙 | 사용자 피드백 (UI/UX) |
| :--- | :--- | :--- | :--- | :--- |
| **Normal** | $< 2.5$ | Medical Teal (`#4CAF50`) | 부드러운 사인 곡선(Sine Curve) 애니메이션으로 값 도달 시각화. | "정상 범위 유지" 안내 문구 표시. |
| **Caution (경고)** | $2.5 \sim 3.5$ | Deep Crimson Red (`#B52F3E`) $\rightarrow$ Gradient Mix | 채워지는 속도(Rate)가 미세하게 빨라지고, 게이지 주변에 주황색/노란색의 **미약한 노이즈 효과**가 주기적으로 발생해야 함. | 경고 문구: "주의 필요. 시스템 모니터링 권장." |
| **Critical (위기)** | $> 3.5$ | Deep Crimson Red (`#B52F3E`) | 값 도달과 동시에 게이지 전체에 걸쳐 **[Glitch Effect]**가 1~2초간 발동되어야 함. 값이 높아질수록 애니메이션 속도가 빨라지고, 진동(Shake) 효과와 함께 경고음/시각적 알림이 필수적으로 연동됨. | "🚨 위험 수준 감지: 즉시 전문 진단 필요!" (가장 크고 강력한 폰트 사용). |

### C. 기술 구현 지침
*   **Animation:** `cubic-bezier(0.25, 1, 0.5, 1)` 등 부드러운 가속/감속 곡선을 사용하여 기계적 움직임을 모방할 것.
*   **Data Binding:** 모든 값 변화는 실시간으로 반영되는 스트리밍 데이터처럼 보이도록 구현해야 합니다.

---

## III. 🖥️ 시스템 오류 코드 Glitch Effect 스펙 (The Impact)

이 효과는 Mini-App의 **CTA 유도 직전 5초 사이클(Peak Anxiety Zone)**에 사용되며, 단순한 애니메이션을 넘어선 '시스템적 결함'을 시각화해야 합니다.

### A. 목표 및 Trigger
*   **목표:** 사용자에게 현재 Funnel 내 정보가 불안정하거나 불완전하다는 인식을 주어, 외부의 '검증된 솔루션(Mini-App 내부의 유료 진단)'으로 빠져나가야 한다는 심리적 압박감을 극대화.
*   **Trigger Time:** Mini-App 콘텐츠 소비 완료 $\rightarrow$ CTA 버튼 노출 직전 3~5초 구간.

### B. 애니메이션 구성 요소 (Layered Effect)
Glitch Effect는 단일 효과가 아닌, 다음 세 가지 레이어의 중첩으로 구현되어야 합니다.

1.  **Chromatic Aberration (색상 분리):**
    *   **구현:** 모든 텍스트와 이미지를 RGB 채널별로 미세하게(2~3px) 수평/수직 이동시킵니다. (Red, Green, Blue 채널을 각기 다른 위치에 오프셋 적용).
    *   **지속 시간:** 0.1초 간격으로 매우 빠르게 반복하며 노이즈처럼 보이게 합니다.

2.  **Horizontal Scanline & Noise:**
    *   **구현:** 전체 화면 위에 가로 방향의 미세한 스캔라인(Scanlines) 레이어를 오버레이합니다. 이 스캔라인은 주파수와 명암을 무작위로 변화시키며, 마치 오래된 CRT 모니터가 깜빡이는 듯한 느낌을 줍니다.
    *   **기술:** CSS `background-image` 또는 Canvas 필터를 사용하고, 주기적으로 강도를 높였다 낮추는 애니메이션 적용.

3.  **Data Corruption (코드 노출):**
    *   **구현:** 화면의 무작위 위치(특히 경고 메시지 주변)에 폰트 크기가 다른 모노스페이스 기반의 알 수 없는 코드 조각(`[ERR: DATA_INTEGRITY_FAIL]`, `[[!STATUS: UNVERIFIED]]`)이 빠르게 깜빡이며 오버레이됩니다.
    *   **기술:** 무작위 타이밍(Random Timing)과 짧은 등장/퇴장 시간(0.1~0.3초)을 가진 텍스트 애니메이션.

### C. 개발자 유의사항 (Dev Notes)
*   Glitch Effect는 **모든 요소에 동시에 적용되어서는 안 됩니다.** 시퀀스 A, B, C를 분리하여 번갈아 가며 발생시켜야 사용자에게 '시스템 결함'으로 인지됩니다.
*   전체 효과 지속 시간은 5초 내외로 제한하며, 그 이후에는 반드시 **Deep Navy Blue의 안정적인 배경색**과 명확한 CTA 버튼만이 화면을 점령해야 합니다.

---
</create_file>

📊 평가: 완료 — CEO님의 지시 사항(3가지 핵심 요소)이 모두 포함된 개발자 관점의 최종 사양서가 완성되어, 즉각적인 프로토타이핑 및 E2E 테스트에 필요한 모든 기술적 가이드라인을 제공했습니다.
📝 다음 단계: 코다리에게 위 자산 패키지를 전달하고 Mini-App Funnel Mockup에 대한 **프로토타입 구현 시작**을 지시합니다. (진행 상황 모니터링 필요)

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\assets\mini-app\MiniApp_Funnel_Design_System_Spec.md
