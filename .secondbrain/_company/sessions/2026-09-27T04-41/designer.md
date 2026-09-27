# 🎨 Designer — Writer가 작성한 구조적 초안과 Researcher의 학술 근거를 결합하여, '권위 구축형' 블로그 시리즈 게시글에 필요한 마스터 HTML/CSS 컴포넌트 세트를 디자인해 주세요. 단순히 텍스트 레이아웃이 아니라, 독자의 지식 여정을 시각화하고 정보의 위계를 높이는 다음 모듈들을 포함해야 합니다: ① 주제별 '위험도 측정 바(Risk Bar)'와 같은 인터랙티브 요소 브리프, ② 핵심 개념을 단계적으로 설명하는 '단계별 프로세스 시각화(Step-by-Step Visualizer)' 컴포넌트, ③ 그리고 최종적으로 검진을 유도하는 명확한 CTA가 포함된 'Action Funnel' 모듈입니다. 모든 것은 코다리가 웹에 바로 통합할 수 있는 구조적이고 재사용 가능한 HTML/CSS 블록 형태로 브리프해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지침과 Writer/Researcher가 제공한 구조적 콘텐츠를 바탕으로, 단순 텍스트 배치 수준을 넘어 독자의 **인지적 여정(Cognitive Journey)**을 디자인하는 '권위 구축형' 블로그 마스터 컴포넌트 세트를 설계했습니다.

이 모듈들은 모든 시리즈 글에 통일성 있게 적용되어, 전문성을 극대화하고 정보의 위계를 높이는 데 초점을 맞추었습니다. 코다리가 바로 웹사이트 구조에 통합하여 사용할 수 있도록 HTML 기반의 CSS 클래스 브리프 형태로 제공합니다.

---

# 🧬 [Master Component Set] 블로그 시리즈 디자인 가이드 (HTML/CSS Brief)

## 🎨 컬러 팔레트 및 타이포그래피 정의
모든 컴포넌트는 다음 원칙을 따릅니다.

*   **메인 배경색:** `#FFFFFF` (깨끗한 신뢰도)
*   **텍스트 기본색:** `#333333` (가독성 최우선)
*   **강조/경고색 (Risk):** `var(--color-danger, #CC0000)` (위험 감지 시 사용)
*   **학습/전문 강조색 (Authority):** `var(--color-authority, #1E8449)` (녹색 계열의 건강함과 권위를 상징)
*   **CTA 최종 유도색:** `#FFC300` (골드톤, '기회'와 '행동 촉구'를 의미)
*   **폰트:** Noto Sans KR 또는 Pretendard (San-serif 계열의 모던함과 가독성 확보)

## 🧪 Module 1: 인터랙티브 위험도 측정 바 (The Risk Bar)
*   **목표:** 추상적인 데이터를 독자 개인의 현재 상태로 끌어와 즉각적인 경고를 주어 '불안감'을 자극합니다.
*   **구현 방식:** 마치 건강 검진 결과지를 보는 것처럼, 주요 지표별 위험도를 시각화하고 그에 따른 해석 텍스트를 배치합니다.

```html
<!-- MODULE_1: RISK_BAR -->
<section class="component-risk-bar py-12 px-4 bg-gray-50 border-t border-b border-gray-200">
    <div class="container mx-auto max-w-3xl">
        <h2 class="text-2xl font-bold mb-8 text-[#333333]">🚨 내 몸의 위험 지표 자가 체크</h2>
        <p class="mb-6 text-lg text-gray-600">현재 생활 습관과 건강 데이터를 바탕으로, 4060 세대가 놓치기 쉬운 핵심 위험 지표를 점검해 보세요. (진단 도구에 대한 기대감 유발)</p>

        <!-- Risk Bar Container -->
        <div class="space-y-8">
            <!-- 지표 A: 만성 염증 (hs-CRP) -->
            <div class="risk-indicator p-6 bg-white shadow-lg rounded-xl border-l-4" style="border-color: var(--color-danger);">
                <div class="flex justify-between items-baseline mb-2">
                    <h3 class="text-xl font-semibold text-[#333333]">🩸 만성 염증 지표 (hs-CRP)</h3>
                    <span class="text-2xl font-bold" id="result-crp">1.5 mg/L</span> 
                </div>
                <!-- 시각화 바 -->
                <div class="w-full bg-gray-200 rounded-full h-3 mb-4 relative">
                    <!-- 동적 배경색 적용: 높을수록 빨갛게, 낮을수록 초록하게 변화 -->
                    <div id="bar-crp" class="bg-[var(--color-danger)] h-3 rounded-full transition-all duration-1000" style="width: 65%;"></div>
                </div>
                <!-- 해석 텍스트 (핵심 메시지) -->
                <div class="text-sm text-red-700 font-medium">
                    ⚠️ **[위험 단계]** 정상 범위 초과. 지속적인 염증 관리가 필요합니다. 전문 진단이 필수입니다.
                </div>
            </div>

            <!-- 지표 B: 인슐린 민감성 (HOMA-IR) -->
            <div class="risk-indicator p-6 bg-white shadow-lg rounded-xl border-l-4" style="border-color: var(--color-authority);">
                <div class="flex justify-between items-baseline mb-2">
                    <h3 class="text-xl font-semibold text-[#333333]">🧬 인슐린 민감성 (HOMA-IR)</h3>
                    <span class="text-2xl font-bold" id="result-homa">1.8</span> 
                </div>
                <!-- 시각화 바 -->
                <div class="w-full bg-gray-200 rounded-full h-3 mb-4 relative">
                    <div id="bar-homa" class="bg-[var(--color-authority)] h-3 rounded-full transition-all duration-1000" style="width: 75%;"></div>
                </div>
                <!-- 해석 텍스트 -->
                <div class="text-sm text-[#1E8449] font-medium">
                    🟢 **[주의 단계]** 수치가 높아지기 시작했습니다. 생활 패턴 개선 및 전문 검진을 권장합니다.
                </div>
            </div>
        </div>
    </div>
</section>
<!-- END MODULE_1 -->
```

## 📈 Module 2: 단계별 프로세스 시각화 (Step-by-Step Visualizer)
*   **목표:** 복잡한 생리학적 과정(예: '인슐린 저항성이 발생하는 메커니즘')을 시간의 흐름이나 인과관계로 단순하게 분해하여 보여줍니다. 학술적인 내용을 쉽게 이해시키는 핵심 장치입니다.
*   **구현 방식:** 수평형 플로우 차트 형태로 구성하며, 각 단계는 명확한 아이콘과 연결선으로 구분됩니다.

```html
<!-- MODULE_2: STEP_VISUALIZER -->
<section class="component-step-visualizer py-16 px-4 bg-white">
    <div class="container mx-auto max-w-5xl">
        <h2 class="text-3xl font-extrabold text-[#333333] mb-10 border-b pb-3">🔬 인슐린 저항성, 몸속에서 무슨 일이 벌어지는가?</h2>
        <p class="mb-12 text-lg text-gray-600 max-w-3xl">인슐린 저항성은 단순히 혈당 문제로 끝나지 않습니다. 복잡하게 얽힌 신체 메커니즘을 세 단계로 나누어 이해할 수 있습니다.</p>

        <!-- Flow Container (Flexbox/Grid 사용 권장) -->
        <div class="flex justify-between items-start relative">
            <!-- 배경 연결선 -->
            <div class="absolute top-10 left-[5%] right-[5%] h-2 bg-gray-200 transform -translate-y-1/2 z-0"></div>

            <!-- Step 1: 원인 (Trigger) -->
            <div class="flex-shrink-0 w-full text-center relative z-10" style="margin-right: 4%;">
                <div class="w-20 h-20 bg-[var(--color-danger)] rounded-full flex items-center justify-center mx-auto mb-3 shadow-xl">
                    <span class="text-white text-3xl font-bold">①</span>
                </div>
                <h3 class="text-xl font-semibold mb-2 text-[#333333]">지속적인 과식 및 염증</h3>
                <p class="text-sm text-gray-700">→ 지방 축적, 만성 염증 물질 증가. 몸에 부담을 줍니다.</p>
            </div>

            <!-- Step 2: 메커니즘 (Process) -->
            <div class="flex-shrink-0 w-full text-center relative z-10" style="margin-right: 4%;">
                <div class="w-20 h-20 bg-[#FFC300] rounded-full flex items-center justify-center mx-auto mb-3 shadow-xl">
                    <span class="text-gray-900 text-3xl font-bold">②</span>
                </div>
                <h3 class="text-xl font-semibold mb-2 text-[#333333]">인슐린 과분비 및 저항성 발생</h3>
                <p class="text-sm text-gray-700">→ 췌장이 무리하여 인슐린을 많이 분비하고, 세포가 이를 거부합니다.</p>
            </div>

            <!-- Step 3: 결과 (Action Needed) -->
            <div class="flex-shrink-0 w-full text-center relative z-10">
                <div class="w-20 h-20 bg-[var(--color-authority)] rounded-full flex items-center justify-center mx-auto mb-3 shadow-xl">
                    <span class="text-white text-3xl font-bold">③</span>
                </div>
                <h3 class="text-xl font-semibold mb-2 text-[#333333]">만성 대사 증후군으로 발전</h3>
                <p class="text-sm text-gray-700">→ 전신적인 에너지 불균형이 발생. 생활 습관 개선과 전문 진단이 필요합니다.</p>
            </div>
        </div>
    </div>
</section>
<!-- END MODULE_2 -->
```

## 🔗 Module 3: Action Funnel 및 CTA (Conversion Focus)
*   **목표:** 독자가 '학습'을 끝내고 '행동(진단/검사)'으로 넘어갈 수 있도록 강력하게 유도합니다. 전문적인 흐름도를 통해 진단의 필요성을 강조합니다.
*   **구현 방식:** 3단계의 심리적 전환 과정을 거치는 모듈로 구성됩니다.

```html
<!-- MODULE_3: ACTION_FUNNEL -->
<section class="component-action-funnel py-20 px-4 bg-[#F7F9FA]">
    <div class="container mx-auto max-w-xl text-center">
        <h2 class="text-3xl font-extrabold mb-6 text-[#333333]">🔍 이제, 나의 몸 상태를 객관적인 데이터로 확인하세요.</h2>
        <p class="text-lg text-gray-700 mb-10">글에서 배운 지식은 중요하지만, 가장 중요한 것은 '나의 현재 수치'입니다. 전문 진단 도구를 통해 정확한 위험도를 체크해 보세요.</p>

        <!-- Funnel Step 1: 문제 인식 (Before) -->
        <div class="funnel-step mb-6 p-5 bg-white rounded-lg shadow-md border-b-4" style="border-bottom-color: var(--color-danger);">
            <p class="text-xl font-semibold text-gray-800">STEP 1. 현재 상태 추측 (불확실성)</p>
        </div>

        <!-- Funnel Step 2: 학습 및 전문성 확보 (Learning) -->
        <div class="funnel-step mb-6 p-5 bg-[#E9F7EF] rounded-lg shadow-md border-b-4" style="border-bottom-color: var(--color-authority);">
            <p class="text-xl font-semibold text-[#1E8449]">STEP 2. 과학적 지식 습득 (정보의 확신)</p>
        </div>

        <!-- Funnel Step 3: 행동 유도 (Action/CTA) -->
        <div class="funnel-step p-6 bg-white rounded-lg shadow-2xl border-4" style="border-color: var(--color-authority);">
            <p class="text-sm text-gray-500 mb-3">👉 이 정보들을 나에게 적용하는 마지막 단계입니다.</p>

            <!-- 최종 CTA 버튼 그룹 -->
            <div class="mt-8 space-y-4">
                <!-- Primary CTA: 진단 도구 (가장 중요) -->
                <a href="#mini-app-funnel" 
                   class="inline-block w-full py-4 text-xl font-bold rounded-lg shadow-xl transition duration-300 transform hover:scale-[1.02]" 
                   style="background-color: var(--color-authority); color: white;">
                    ✅ [무료 진단] 만성 염증/인슐린 민감도 Mini-App 실행하기 (가장 강력한 버튼)
                </a>

                <!-- Secondary CTA: 심화 자료 -->
                 <a href="#deep-dive" 
                   class="inline-block w-full py-3 text-lg font-semibold rounded-lg shadow-md transition duration-300 transform hover:bg-[#E0F2E4]" 
                   style="background-color: #FFFFFF; color: var(--color-authority); border: 1px solid var(--color-authority);">
                    📖 심화 가이드 다운로드 (PDF) - 전반적인 라이프스타일 개선책 보기
                </a>
            </div>
        </div>
    </div>
</section>
<!-- END MODULE_3 -->
```

---
**브리프 요약 및 통합 지침:**

1.  **순서 유지:** 모든 콘텐츠는 `Module 1 (경고)` $\rightarrow$ `Module 2 (학습)` $\rightarrow$ `Module 3 (행동 유도)` 순서로 배치되어야 합니다.
2.  **UX 강조:** `Module 1`의 위험 지표 수치는 **애니메이션(Transition)** 효과를 주어 마치 살아있는 데이터를 보여주는 듯한 경험을 제공하는 것이 중요합니다.
3.  **재사용성:** 위의 세 컴포넌트 구조와 컬러 팔레트를 모든 블로그 시리즈에 통일적으로 적용하여, 온현 브랜드의 '전문성과 신뢰도'라는 정체성을 확립해야 합니다.

📊 평가: 완료 — 요청된 3가지 핵심 기능(위험도 바, 단계별 프로세스, 액션 퍼널)을 모두 포함한 구조적 HTML/CSS 컴포넌트 세트를 제공하여 목표가 달성되었습니다.
📝 다음 단계: 코다리에게 이 마스터 컴포넌트들을 실제 블로그 플랫폼의 템플릿 파일에 적용하고, 동적인 요소(예: `Mini-App` 연동)를 구현하도록 전달해야 합니다.
