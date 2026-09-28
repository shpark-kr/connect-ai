# 🎨 Designer — 이전에 완성한 '위기 → 해결' 전환 프로토콜 인터랙티브 스펙 시트 V2.0를 기반으로, 개발자가 바로 코딩할 수 있는 최종 UI 컴포넌트 명세서(CSS/HTML 레벨의 상세 지침)를 완성하여 전달하십시오. 특히 Deep Crimson Red 경고가 끝난 후 Soft Gold(`#F5E6C7`)로 전환되는 시각적 계층 구조를 재확인해주세요.

🎨 Designer: 작업 시작합니다.

CEO 지시사항 확인했습니다. Funnel의 전환 프로토콜은 이 미디어 스튜디오의 가장 핵심적인 수익화 경로입니다. 단순히 예쁘게 보이는 디자인이 아니라, **사용자의 심리적 위기감을 극대화하고(Deep Crimson Red), 그 직후에 즉각적으로 해결책을 제시하며 신뢰를 구축하는(Soft Gold)** 공학적인 인터랙션이 필요합니다.

개발자가 바로 코딩할 수 있도록, `Funnel Transition Module`의 최종 UI 컴포넌트 명세서와 CSS/HTML 레벨 지침을 완성하여 전달하겠습니다. 이 모듈은 **Deep Crimson Red 경고 $\to$ Soft Gold 전환**이라는 시각적 계층 구조(Visual Hierarchy) 변화에 초점을 맞췄습니다.

### 📦 Funnel Transition Module (V2.0 Final Spec)

이 컴포넌트는 세 개의 명확한 상태(State)를 가집니다. 각 상태별로 배경 오버레이, 주 색상, 애니메이션 타이밍을 지정합니다.

#### 1. Global Variables & Color Palette
| 역할 | 이름 | Hex Code | 용도 |
| :--- | :--- | :--- | :--- |
| **Crisis Warning** (경고) | Deep Crimson Red | `#800020` | 위험 알림, 경고 메시지 배경. 강한 시각적 주의 집중. |
| **Solution Phase** (해결책) | Soft Gold | `#F5E6C7` | 전환 완료 후의 신뢰 구간 배경 및 CTA 하이라이트. 부드러운 수용 유도. |
| **Primary Accent** (강조) | Navy Blue | `#1A237E` | 텍스트, 핵심 타이틀. 전문성 유지. |
| **Neutral Background** | Light Gray | `#F9FAFB` | 기본 콘텐츠 영역 배경. |

#### 2. HTML/Tailwind Skeleton Structure
전체 모듈은 `relative` 컨테이너 내부에 오버레이 레이어와 실제 콘텐츠 레이어를 분리하여 깊이감을 부여합니다.

```html
<div id="funnel-transition-module" class="relative w-full min-h-[60vh] overflow-hidden">
    <!-- 1. The Overlay Layer (Background Color & Warning Effect) -->
    <div id="overlay-layer" class="absolute inset-0 transition-all duration-1000 ease-in-out pointer-events-none z-10 opacity-0"></div>

    <!-- 2. The Content Area (Text, Stats, CTAs) -->
    <div class="relative z-20 py-24 px-6 max-w-5xl mx-auto text-center">
        <!-- [Section A: Crisis Indicator / Warning Message] -->
        <section id="warning-indicator" class="transition-opacity duration-700 opacity-0 mb-12">
            <!-- Deep Crimson Red 경고 배지/텍스트가 여기에 삽입됩니다. -->
        </section>

        <!-- [Section B: Core Problem Presentation (Stats Comparison)] -->
        <div id="problem-stats" class="mb-20 grid grid-cols-1 md:grid-cols-3 gap-8 opacity-0 transition-opacity duration-700">
            <!-- A/B 비교형 인포그래픽 컴포넌트가 들어갑니다. (다크 네이비/골드톤) -->
        </div>

        <!-- [Section C: Solution & CTA Card] -->
        <section id="solution-card" class="opacity-0 transition-opacity duration-1000">
            <h2 class="text-4xl font-bold text-navy-blue mb-6">최적의 해결책을 만나보세요.</h2>
            <!-- The Optimal Combo Card Component -->
        </section>
    </div>
</div>
```

#### 3. State별 CSS/JS 로직 지침 (Developer Focus)

**A. 초기 상태 (Pre-Warning / Default):**
*   `#overlay-layer` opacity: `0`
*   전체 모듈 배경: Soft Gold의 아주 미묘한 그라데이션을 사용하여 안정적인 느낌만 줍니다. (`background: linear-gradient(to bottom, #F5E6C7 0%, #FFFFFF 100%);`)

**B. 경고 상태 (Crisis Warning State):**
*   **트리거:** 특정 시점 도달 또는 사용자가 데이터를 입력했을 때.
*   **지연 시간 (Delay):** 0초부터 시작하여, Deep Crimson Red로의 변화를 **0.5초~1.0초**에 걸쳐 진행합니다. (부드러운 불안감 조성)
*   **CSS 적용:**
    ```css
    #overlay-layer {
        background-color: #800020; /* Deep Crimson Red */
        opacity: 0.95; 
        /* 강한 경고 느낌을 주기 위해 배경에 미세한 노이즈 패턴(Noise Pattern) 오버레이 추가 권장 */
    }
    #warning-indicator {
        opacity: 1; /* 즉시 등장 (Deep Crimson Red 바탕 위에) */
        color: white;
        /* 애니메이션 예: Scale up + Flash 효과 */
    }
    #problem-stats, #solution-card {
        opacity: 0.4; /* 경고가 최고조일 때는 해결책에 대한 내용이 흐릿하게 보여 불안감을 증폭시킵니다. */
    }
    ```

**C. 전환 및 해결 상태 (Solution Reveal State):**
*   **트리거:** Deep Crimson Red 경고가 최고조에 달한 후, 시스템 메시지("해결책을 찾아드립니다.")와 함께 **0.5초~1.0초**의 애니메이션 지연 시간 후에 발동합니다.
*   **CSS 적용 (핵심):**
    ```css
    #overlay-layer {
        background-color: #F5E6C7; /* Soft Gold로 부드럽게 전환 */
        opacity: 0.98;
        /* transition 속성을 이용해 Deep Crimson Red에서 Soft Gold로의 배경색 변화를 구현합니다. */
    }
    #warning-indicator {
        display: none; /* 경고 문구는 사라지거나 축소되어 신뢰 구간에 자리를 내줍니다. */
    }
    #problem-stats, #solution-card {
        opacity: 1; /* 모든 콘텐츠가 선명하게 다시 나타나며 (Fade In), 문제의 명확한 정의와 해결책이 동시에 제시됩니다. */
        /* 이 때, Soft Gold 배경 위에서 '해결책 제안 카드'를 가장 크게 보이게 배치합니다. */
    }
    ```

<create_file path="c:\Data\Project\connect-ai\assets\mini-app\FunnelTransitionModule_SpecSheet_V2.0.md"># Funnel Transition Module (V2.0) - 개발자 컴포넌트 명세서

## 🚀 개요
사용자의 '위기 인지(Crisis Recognition)'에서 '해결책 수용(Solution Acceptance)'으로의 전환을 유도하는 핵심 UI/UX 모듈입니다. Deep Crimson Red 경고 상태와 Soft Gold 신뢰 상태 간의 시각적 계층 구조 변화가 가장 중요합니다.

## 🎨 컬러 & 타이포그래피
*   **Deep Crimson Red:** `#800020` (Crisis Alert)
*   **Soft Gold:** `#F5E6C7` (Solution Trust)
*   **Primary Text:** `#1A237E` (Navy Blue)

## 🖥️ HTML 구조 (Skeleton)
\`\`\`html
<div id="funnel-transition-module" class="relative w-full min-h-[60vh] overflow-hidden">
    <!-- Background Overlay Layer: 상태 변화를 담당하는 핵심 요소 -->
    <div id="overlay-layer" class="absolute inset-0 transition-all duration-1000 ease-in-out pointer-events-none z-10 opacity-0"></div>

    <!-- Content Area (z-20): 모든 콘텐츠는 이 위에 배치됨 -->
    <div class="relative z-20 py-24 px-6 max-w-5xl mx-auto text-center">
        <!-- [A] 경고 섹션: Deep Crimson Red가 지배할 때 활성화 -->
        <section id="warning-indicator" class="...">...</section>

        <!-- [B] 문제 진단 섹션: A/B 비교 인포그래픽 컴포넌트 -->
        <div id="problem-stats">...</div>

        <!-- [C] 해결책 CTA 카드: Soft Gold로 전환되며 가장 강조됨 -->
        <section id="solution-card">...</section>
    </div>
</div>
\`\`\`

## ⚙️ 핵심 인터랙션 로직 (JavaScript/CSS)

### State A: Crisis Warning Activation (Deep Crimson Red Dominance)
1.  **Trigger:** Funnel 진입 직후 또는 특정 지표 하락 시.
2.  **Animation:** `overlay-layer`의 배경색을 `#800020`으로, Opacity를 0.95로 설정하며 **transition duration: 1000ms** 애니메이션을 적용합니다.
3.  **Hierarchy Effect:** 이 상태에서 모든 콘텐츠(B와 C)는 **불안감을 조성하기 위해 시각적으로 흐릿하게(`opacity: 0.4`)** 처리되어야 합니다. 경고 메시지(`warning-indicator`)만 선명해야 합니다.

### State B: Transition to Solution (Soft Gold Reveal)
1.  **Trigger:** Deep Crimson Red 경고가 최고조에 달한 후, 개발자가 코딩할 수 있도록 **0.5초~1.0초의 지연 시간(Delay)**을 확보합니다.
2.  **Animation:** `overlay-layer`의 배경색이 `#800020`에서 `#F5E6C7`로 부드럽게 (Soft Gold) 전환됩니다. **transition duration: 1000ms.**
3.  **Hierarchy Effect:** 모든 콘텐츠(B와 C)는 동시에 `opacity: 1`로 돌아오면서 선명해져야 합니다. 특히, `#solution-card` 영역은 가장 높은 시각적 위계를 가져가도록 설계합니다.

---
*주의사항: 이 컴포넌트는 반응형 디자인을 반드시 적용해야 하며, 모든 섹션 간의 여백(Spacing)과 정렬(Alignment)이 일관되어야 합니다.*</create_file>

📊 평가: 완료 — 요청된 개발자 레벨의 최종 UI 컴포넌트 명세서(CSS/HTML 구조 및 상태 전환 로직 포함)를 성공적으로 완성했습니다.
📝 다음 단계: 코다리가 Funnel E2E 테스트 안정화 작업을 완료하고, 이 명세서를 기반으로 실제 프론트엔드 구현을 시작해야 합니다.

---
*(참고: 다른 에이전트의 목표와 나의 개인 목표가 모두 "Mini-App Funnel UI 컴포넌트 완성"이라는 동일한 최종 산출물을 지향하고 있으므로, 현재는 이 명세서 전달로 최적화된 작업을 완료했습니다.)*

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\assets\mini-app\FunnelTransitionModule_SpecSheet_V2.0.md
