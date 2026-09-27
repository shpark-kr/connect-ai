# 🎨 Designer — Mini-App Funnel의 핵심 컴포넌트(위험도 바 SVG, 진단 체크박스 모듈, A/B 테스트 CTA 버튼)를 실제 코드로 구현할 때 필요한 최종 CSS 클래스 명세와 SVG 구조(레이아웃 및 접근성 포함) 목록을 개발팀에 전달하십시오. 디자인 시안이 아닌, 코드 레벨의 컴포넌트 가이드가 필요합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시에 따라, Mini-App Funnel의 핵심 컴포넌트 3가지에 대한 **개발자 전달용 최종 기술 명세(Developer Handoff Specification)**를 작성했습니다. 이는 단순한 디자인 설명이 아닌, 즉시 코딩에 적용할 수 있는 CSS 클래스 구조, SVG 구조 및 접근성(Accessibility) 가이드라인을 포함합니다.

모든 컴포넌트의 일관성을 위해 이 명세를 `Master_Design_Briefs` 폴더 내 새로운 파일로 저장하고, 개발팀이 이곳을 **Single Source of Truth**로 사용하도록 지정했습니다.

<create_file path="C:\Users\USER\Designs\Onhyun\Master_Design_Briefs\Component_Spec_Sheet_v1.0.md"># 🛠️ Mini-App Funnel 핵심 컴포넌트 기술 명세 (Developer Handoff)

**목표:** 개발팀이 기반 환경(Staging Environment)에 즉시 통합할 수 있는, 반응형 웹 환경용 고정된 시각 요소 라이브러리 제공.
**사용 가이드라인:** 모든 클래스는 BEM(Block Element Modifier) 원칙을 따르며, Tailwind CSS 또는 유사한 유틸리티 우선순위의 구조를 가정합니다.

---

## 1️⃣ 위험도 측정 바 (Risk Score Indicator - `__risk-bar`)

*   **목적:** 사용자의 진단 결과 점수(0~100)에 따라 즉각적인 시각적 위기감을 조성하고, 학술적 권위를 유지하는 게이지.
*   **구조:** SVG를 사용하여 부드러운 색상 변화와 정확한 길이 측정이 가능하도록 구현합니다.

### 🔹 기술 명세 (Technical Spec)

**1. 기본 HTML/SVG 구조:**

```html
<div class="risk-bar__container" role="status" aria-label="현재 염증 위험도 점수">
  <svg class="risk-bar__svg" width="100%" height="30" viewBox="0 0 100 10" preserveAspectRatio="none">
    <!-- 배경 트랙 (Background Track) -->
    <rect x="0" y="0" width="100%" height="10" fill="#e0e7ff" class="risk-bar__track"/>
    <!-- 현재 위험도 채움 영역 (Filled Area - Dynamic) -->
    <rect id="risk-score-fill" x="0" y="0" width="[SCORE_PERCENTAGE]%" height="10" fill="[COLOR_CODE]" class="risk-bar__fill"/>
  </svg>
</div>
```

**2. CSS/JS 로직:**

*   `--score`: 현재 위험도 점수 (0~100).
*   `width`: `calc($score / 100 * 100%)`로 동적 계산합니다.
*   `[COLOR_CODE]`는 JS에서 Score에 따라 결정됩니다.

| Score Range | Color Class | Hex Code | 의미/활용 |
| :---: | :---: | :---: | :---: |
| 75-100 | `risk-bar__danger` | `#dc2626` (Red) | **위험 경고:** 즉각적인 행동 촉구 필요. 강렬함. |
| 40-74 | `risk-bar__warning` | `#f59e0b` (Amber) | **주의 단계:** 생활 습관 개선 권장. 중간 톤. |
| 0-39 | `risk-bar__safe` | `#16a34a` (Green) | **안정 단계:** 현재 상태 유지 및 관리. 안정감. |

**3. 접근성 (Accessibility):**
*   SVG 전체에 `role="status"`와 `aria-label`을 적용하여 스크린 리더가 점수 범위를 명확히 읽도록 합니다.
*   위험도 설명 텍스트를 반드시 별도의 `<p>` 태그로 제공하고, SVG는 시각적 보조 수단으로만 사용합니다.

---

## 2️⃣ 진단 체크박스 모듈 (Diagnostic Module - `__diagnosis-checkbox`)

*   **목적:** 복잡한 질문을 통해 사용자 스스로 자신의 상태를 인지하게 하는 인터랙티브 요소.
*   **구조:** 네이티브 `<input type="checkbox">`의 기본 UI를 오버레이하여 커스터마이징하며, 사용자가 명확히 클릭할 수 있는 큰 영역을 제공합니다.

### 🔹 기술 명세 (Technical Spec)

**1. HTML 구조:**
```html
<div class="diagnosis-module__item" role="checkbox" aria-checked="false">
  <!-- Custom Hidden Input -->
  <input type="checkbox" id="q-[ID]" name="question-[ID]" class="visually-hidden">
  <!-- Visible Label/Trigger Area -->
  <label for="q-[ID]" class="diagnosis-module__label">
    <span class="icon-container"></span> <!-- 커스텀 체크박스 영역 -->
    <span class="text-content">[질문 내용]</span>
  </label>
</div>
```

**2. CSS/JS 로직:**

*   **`:checked` 상태 (활성화):** `border-color: #3b82f6; background-color: #eff6ff;`로 변경되며, 커스텀 체크박스 영역에 짙은 파란색 체크 마크(SVG)가 나타나야 합니다.
*   **`:focus` 상태 (접근성):** 포커스를 맞춘 요소 주변에 `box-shadow: 0 0 0 2px #60a5fa;`와 같은 명확한 포커스 인디케이터를 반드시 구현합니다.
*   **레이아웃:** 체크박스와 텍스트는 Flexbox로 정렬하며, 전체 모듈의 간격은 `18px`을 유지합니다.

---

## 3️⃣ A/B 테스트 CTA 버튼 (Conversion Button - `__cta-button`)

*   **목적:** Funnel의 최종 목표(Mini-App 진단)로 사용자를 유도하는 핵심 전환 장치. 감정 상태에 따른 두 가지 버전 제공.
*   **구조:** 표준적인 버튼 컴포넌트가 아닌, '긴급한 행동'을 촉구하는 위젯 형태여야 합니다.

### 🔹 기술 명세 (Technical Spec)

**1. 기본 HTML 구조:**
```html
<button type="button" class="cta-button cta-button--variant-[A/B]" onclick="handleConversion(this)">
  [CTA 최종 문구]
</button>
```

**2. CSS/JS 로직 및 A/B 테스트 변형:**

| 속성 | Variant A (공포/위기감) | Variant B (신뢰/낮은 장벽) | 공통 스타일 (Base) |
| :---: | :---: | :---: | :---: |
| **색상** | `#ef4444` (강렬한 빨간색 계열) | `#2563eb` (신뢰감 있는 파란색 계열) | `border-radius: 10px;` |
| **텍스트** | "🚨 지금 즉시 위험도 진단하기 (늦으면 안 됩니다)" | "나에게 맞는 솔루션 무료로 확인하기" | `font-weight: bold;` |
| **호버 효과** | 배경 색상이 어두워지며, 펄스(Pulse) 애니메이션을 짧게 적용. | 부드럽하게 미세히 커지는 트랜지션(`scale(1.02)`). | `:active` 시 약간 눌리는 느낌의 `transform: translateY(1px);`. |
| **클릭 액션** | Funnel 진단 결과 페이지로 리디렉션 (경고성 URL) | Mini-App 서비스 랜딩 페이지로 리디렉션 (안정적 URL) | `cursor: pointer;` |

---
</create_file>

📊 평가: 완료 — 모든 핵심 컴포넌트에 대한 코드 레벨의 기술 명세와 접근성을 포함한 가이드라인을 개발팀에 전달하여, 디자인 확정 단계를 성공적으로 마무리했습니다.
📝 다음 단계: 영숙 에이전트가 정의한 대로, 이 기술 사양을 기반으로 **실제 작동하는 Funnel MVP 프로토타입**의 백본(Shell) 구축을 개발팀에게 요청하고, 동시에 Writer와 Researcher는 Mock Data를 완성하여 로직 검증 준비에 돌입해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: ~\Designs\Onhyun\Master_Design_Briefs\Component_Spec_Sheet_v1.0.md
