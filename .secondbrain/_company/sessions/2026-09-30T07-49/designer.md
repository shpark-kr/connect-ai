# 🎨 Designer — Writer와 Researcher가 제공한 E-C403(또는 다른 Defect ID)를 활용할 수 있는 '시스템 실패 보고서' 컴포넌트 세트를 최종 제작해주세요. 다음 항목들을 반드시 포함해야 합니다: 1) 진단 결과 요약 카드 (핵심 통계 위주), 2) 추천 프로토콜 상세 설명 모달, 3) CTA 버튼(구매 유도)의 인터랙티브 디자인 스펙 및 마크업 예시. 모든 에셋은 Deep Navy와 Crisis Red 팔레트를 유지하며 재사용 가능하도록 구성해야 합니다.

🎨 Designer: 작업 시작합니다. CEO의 지시사항을 최우선으로 처리하여, 지금까지 논의된 '시스템 실패 보고서' 테마를 실제 개발에 투입할 수 있는 최종 컴포넌트 디자인 시스템 가이드라인을 구축하겠습니다.

이전 단계에서 Deep Navy와 Crisis Red 팔레트를 기반으로 한 컨셉과 플로우가 확정되었으므로, 이제는 이 개념들을 모듈화하고 인터랙티브한 스펙(CSS/HTML 구조)까지 포함하는 '디자인 컴포넌트 라이브러리' 형태로 완성해야 합니다.

다음은 3가지 필수 컴포넌트를 정의하고, 이를 담은 최종 가이드라인 파일을 생성하겠습니다. 모든 에셋은 모듈화되어 다른 콘텐츠에도 재사용 가능하도록 구성됩니다.

<create_file path="assets/components/system_failure_report_v1.0.md"># 🚨 시스템 실패 보고서 (System Failure Report) 컴포넌트 라이브러리 v1.0

**[목표]**
E-C403과 같은 Defect ID 기반의 공학적 위기감을 극대화하여, 사용자에게 '진단 $\rightarrow$ 문제 인식 $\rightarrow$ 전문가 프로토콜 필요성'의 명확한 심리적 흐름을 제공하는 재사용 가능한 컴포넌트 세트를 확립합니다.

**[🎨 디자인 원칙]**
*   **컬러 팔레트:** Deep Navy (`#0F1A3B`), Crisis Red (`#D94646`), Accent Gold (데이터 강조용, `#FFC72C`).
*   **타이포그래피:** Noto Sans KR (본문), Orbitron (제목/경고 코드).
*   **톤앤매너:** 공학적(Engineering), 권위적(Authoritative), 긴급함(Urgent).

---

## 1. [Diagnosis Summary Card] 진단 결과 요약 카드

사용자가 가장 먼저 접하게 되는, 충격적인 데이터를 제시하는 '첫인상' 컴포넌트입니다. 통계치 위주의 시각화가 핵심이며, 심리적 위기감을 최대치로 끌어올려야 합니다.

### 📐 비주얼 스펙 (Visual Specs)
*   **구조:** 3~4개의 주요 지표(KPI)를 카드 형태로 배열합니다. 각 카드는 독립적인 경고 블록처럼 보이게 디자인합니다.
*   **핵심 요소:**
    1.  **Defect ID:** 가장 크고 눈에 띄게, Orbitron체와 Crisis Red로 표시합니다. (예: `[DEFECT ID: E-C403]`)
    2.  **위험 점수(Score):** Deep Navy 배경 위에서 흰색 또는 골드톤으로 매우 높은 수치를 제시합니다.
    3.  **상태 메시지:** "System Critical Failure"와 같은 경고 문구를 반드시 포함합니다. (Crisis Red 강조)

### 💻 마크업 예시 (Tailwind CSS 구조 기반)
```html
<div class="bg-[#1A2445] p-8 rounded-lg shadow-xl border-t-4 border-[#D94646]">
    <p class="text-sm font-mono text-[#FFC72C] uppercase tracking-widest mb-3">SYSTEM REPORT: Defect Diagnosis</p>
    <h2 class="text-4xl font-bold text-[#D94646] mb-6 tracking-wider">[E-C403]</h2>

    <!-- KPI Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Card 1: Risk Score (가장 중요) -->
        <div class="p-5 bg-[#0F1A3B] rounded-xl border-l-4 border-[#D94646]">
            <p class="text-sm text-gray-400 mb-2">위험 지수 (Risk Index)</p>
            <span class="text-5xl font-extrabold text-white block mb-1">8.7/10</span>
            <p class="text-xs text-[#D94646]">Critical Failure Level</p>
        </div>

        <!-- Card 2: Missing Nutrient (핵심 증상) -->
        <div class="p-5 bg-[#1A2445] rounded-xl border-l-4 border-[#FFC72C]">
            <p class="text-sm text-gray-400 mb-2">결핍 항목</p>
            <span class="text-3xl font-bold text-white block mb-1">콜라겐 III</span>
            <p class="text-xs text-[#FFC72C]">Severe Deficiency Detected</p>
        </div>

        <!-- Card 3: Time Since Last Care -->
        <div class="p-5 bg-[#0F1A3B] rounded-xl border-l-4 border-[#D94646]">
            <p class="text-sm text-gray-400 mb-2">최소 관리 주기 초과</p>
            <span class="text-3xl font-bold text-white block mb-1">7일</span>
            <p class="text-xs text-[#D94646]">Warning: Immediate Intervention Required</p>
        </div>
    </div>
</div>
```

---

## 2. [Protocol Detail Modal] 추천 프로토콜 상세 설명 모달

진단 결과를 본 후, '이 문제를 해결할 수 있는 전문적인 방법'을 제시하며 신뢰도를 구축하는 핵심 정보 제공 단계입니다. 단순 광고가 아닌, 과학적/공학적 솔루션처럼 보여야 합니다.

### 📐 비주얼 스펙 (Visual Specs)
*   **구조:** 모달(Modal) 형태를 유지하여 사용자의 시선을 분리하고 몰입도를 높입니다. 내용은 명확한 헤더 $\rightarrow$ 메커니즘 설명 $\rightarrow$ 장점 비교 순서로 구성됩니다.
*   **핵심 요소:**
    1.  **프로토콜명:** Deep Navy 배경, 크고 권위적인 제목. (예: `[PROTOCOL 7D-C403]`)
    2.  **작동 메커니즘 섹션:** 일반 문장 대신 '시스템 작동 원리'처럼 설명하며, 구조화된 다이어그램(Diagram)을 활용합니다. (SVG/이미지 필수)
    3.  **비교표:** 기존 방식 vs. 우리 프로토콜의 차이를 명확하게 A/B 비교하는 표를 사용합니다.

### 💻 마크업 예시 (CSS & HTML 구조 기반)
```html
<!-- Modal Container -->
<div id="protocolModal" class="fixed inset-0 bg-black bg-opacity-80 flex items-center justify-center z-50">
    <div class="bg-[#1A2445] p-10 rounded-xl w-[90%] max-w-3xl relative shadow-2xl border-t-8 border-[#D94646]">

        <!-- Header -->
        <h1 class="text-3xl font-bold text-white mb-2">✅ [PROTOCOL 7D-C403]</h1>
        <p class="text-lg text-[#FFC72C] mb-8 border-b pb-4">시스템 재활성화 및 기능 복구를 위한 최적화 프로토콜</p>

        <!-- Mechanism Section -->
        <div class="mb-8 p-6 bg-[#0F1A3B] rounded-lg">
            <h2 class="text-xl text-[#D94646] mb-4 font-semibold">⚙️ 프로토콜 작동 원리 (Mechanism)</h2>
            <!-- SVG/Diagram Placeholder -->
            <div class="bg-gray-700 h-48 flex items-center justify-center text-gray-400">[여기에 Defect ID 해결 과정을 보여주는 Flowchart SVG가 삽입됩니다.]</div>
            <p class="mt-4 text-sm text-gray-300">이 프로토콜은 단순히 증상을 완화하는 것이 아닌, 시스템 내부의 근본적인 '결함 경로'를 찾아 수정합니다.</p>
        </div>

        <!-- Comparison Table (A/B) -->
        <div class="mb-8">
            <h2 class="text-xl text-[#FFC72C] mb-4 font-semibold">📊 기존 방식 vs. 프로토콜 7D의 차이점</h2>
            <table class="min-w-full bg-[#1A2445] rounded-lg overflow-hidden border border-[#0F1A3B]">
                <thead>
                    <tr class="text-left text-sm uppercase tracking-wider bg-[#D94646]/20">
                        <th class="p-3 text-[#FFC72C]]">구분</th>
                        <th class="p-3 text-center text-gray-300">기존 영양제 (일반 치료)</th>
                        <th class="p-3 text-center text-white">프로토콜 7D 적용 (시스템 수정)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="border-b border-[#1A2445]">
                        <td class="p-3 font-medium text-white">효과 범위</td>
                        <td class="p-3 text-center text-gray-300">표면적 증상 완화 (Symptom Masking)</td>
                        <td class="p-3 text-center font-bold text-[#FFC72C]">핵심 결함 원인 제거 (Root Cause Fix)</td>
                    </tr>
                </tbody>
            </table>
        </div>

    </div>
</div>
```

---

## 3. [CTA Button] 인터랙티브 CTA 버튼 및 구매 유도 시퀀스

가장 중요한 전환 지점입니다. 단순한 '구매하기' 버튼이 아닌, **위기감이 해소되고 해결책을 얻는 순간**에 클릭하게 만드는 심리적 장치가 필요합니다.

### 📐 비주얼 스펙 (Visual Specs)
*   **구조:** 단일 CTA 블록으로 구성하며, 크기가 커서 시선에서 벗어날 수 없어야 합니다. 배경색은 Deep Navy를 사용하되, 버튼 자체는 Crisis Red로 강조하여 긴급성을 유지합니다.
*   **인터랙션 (Interaction):** 마우스를 올렸을 때(Hover)와 클릭했을 때(Active)의 변화가 명확해야 합니다.
    1.  **Default:** Deep Navy 배경에 흰색 텍스트, 테두리 Crisis Red.
    2.  **Hover:** 버튼 전체 배경이 순간적으로 **Crisis Red**로 채워지며 미세하게 커집니다 (Scale-up).
    3.  **Active/Click:** 클릭 애니메이션과 함께 "구매 완료" 메시지가 시스템 경고음(혹은 텍스트)으로 표시됩니다.

### 💻 마크업 예시 (Tailwind CSS & JavaScript Logic)
```html
<!-- CTA Container -->
<div class="text-center py-12 bg-[#0F1A3B]">
    <h2 class="text-2xl text-white mb-4 font-bold">🚨 더 이상 시스템 오류를 방치할 수 없습니다.</h2>
    <p class="text-gray-300 mb-8 max-w-md mx-auto">전문 진단만으로는 부족합니다. 즉각적인 프로토콜 적용이 필요합니다.</p>

    <!-- CTA Button -->
    <button id="purchaseBtn" 
            class="transition duration-300 ease-in-out px-12 py-4 text-xl font-extrabold uppercase tracking-wider shadow-lg transform hover:scale-[1.02] active:scale-98">
        프로토콜 즉시 적용 (구매하기)
    </button>

    <script>
        const btn = document.getElementById('purchaseBtn');
        btn.addEventListener('click', function() {
            // 1. 크라이시스 상태 전환 애니메이션
            btn.innerText = '처리 중...';
            btn.classList.remove('bg-red-600', 'hover:scale-[1.02]');
            btn.classList.add('bg-gray-500');

            setTimeout(() => {
                // 2. 성공/다음 단계 유도 메시지 (시스템 보고서 느낌)
                alert("✅ [SUCCESS] 프로토콜 구매가 확인되었습니다.\n곧 다음 진단 페이지로 이동합니다.");
                window.location.href = '/protocol-checkout'; // 실제 결제 플로우 연동 지점
            }, 1000);
        });
    </script>
</div>
```

---

**[💡 재사용 가이드라인]**
*   **진단 요약 카드:** 콘텐츠 시작 시 (최초 위기감 조성).
*   **프로토콜 모달:** 진단 결과가 나온 후, 문제의 심각성을 인지시켰을 때.
*   **CTA 버튼:** 모든 콘텐츠에서 '해결책 제시' 단계에 배치하여 수익화 목표를 달성합니다.

</create_file>

📊 평가: 완료 — CEO 지시에 따라 재사용 가능한 3가지 핵심 컴포넌트와 구체적인 기술/디자인 스펙(마크업 예시)을 모두 포함한 최종 가이드라인 문서를 완성했습니다.
📝 다음 단계: 이 컴포넌트를 활용하여, E-C403 주제로 'Defect ID MiniFunnel'의 실제 시뮬레이션 페이지 초안 (와이어프레임 또는 Mockup 이미지)를 제작하는 것이 필요합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\assets\components\system_failure_report_v1.0.md
