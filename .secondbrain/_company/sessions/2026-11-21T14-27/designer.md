# 🎨 Designer — 지난 세션에서 확정된 'Defect ID 시스템 실패 보고서'의 UI/UX 명세(v1.0)를 기반으로, 핵심 컴포넌트 에셋 패키지(Atomic Design 준수)를 완성해 주세요. 특히, 다음 3가지 요소를 포함하여 개발자가 즉시 코딩할 수 있는 High-Resolution 벡터 및 스펙 시트를 제공해야 합니다:
1. ATP/ADP Ratio 변화 추이 그래프 (Crisis Red 경고 패턴 적용)
2. Defect ID별 시스템 오류 로그 UI 컴포넌트
3. 보고서 상단에 배치될 '시스템 위험도 게이지' 위젯
최종 아웃풋은 개발자가 즉시 활용 가능한 형태로 구성하고, 이 에셋들을 developer에게 인계할 준비를 완료해 주세요.

🎨 Designer: 작업 시작합니다.

CEO의 지시를 바탕으로 'Defect ID 시스템 실패 보고서'의 핵심 컴포넌트 에셋 패키지(v2.0)를 완성했습니다. 이 스펙트는 개발자가 별도의 디자인 검토 없이 즉시 코딩에 착수할 수 있도록 Atomic Design 기반의 구조와 구체적인 CSS/Tailwind 클래스 명세를 포함하고 있습니다.

저는 이 아웃풋을 `<create_file path="C:\Users\USER\Work\Onhyun\MiniFunnel_DesignSpec_v2.0.md">` 파일로 생성하여 개발팀에 인계할 준비를 완료했습니다.

<create_file path="C:\Users\USER\Work\Onhyun\MiniFunnel_DesignSpec_v2.0.md"># 🎨 Onhyun: 시스템 실패 보고서 (System Failure Report) - 컴포넌트 스펙 시트 v2.0

**작성 목적:** Defect ID 기반의 과학적 위기감 조성 및 단계별 구매 유도 MiniFunnel UI/UX 개발을 위한 핵심 에셋 패키지 제공.
**디자인 원칙:** Atomic Design 준수, Deep Navy (#1A2338) & Crisis Red (#C70039) 사용, 공학적 보고서 톤 유지.

---

## ⚙️ Component 1: 시스템 위험도 게이지 (System Risk Level Gauge Widget)
**위치:** 보고서 상단 헤더 영역 (H1 바로 아래). 즉각적인 시선 집중 및 위기감 조성 역할.
**형태:** 원형/반원형 아날로그 스타일의 게이지 바.

### 💡 Spec & 구조
*   **크기:** 가로 600px, 높이 120px (최소 너비 보장).
*   **배경:** Deep Navy (#1A2338) 배경 위, 미세한 그리드 라인 오버레이.
*   **위험도 단계 및 색상 정의 (Color Palette):**
    *   **Optimal Zone (녹색 계열):** #4CAF50 - 초기 정상 상태를 의미하며 사용 빈도는 낮음.
    *   **Warning Zone (노란/주황):** #FFC107 - 경계선 도달, 관리를 요하는 단계.
    *   **Critical Zone (위기):** #C70039 - 시스템 결함(Defect ID)이 명확히 확인된 위험 상태.

### 🖥️ 개발자 가이드라인 (Mockup HTML/Tailwind Classes)
```html
<div class="risk-gauge-container w-[600px] h-[120px] bg-[#1A2338] p-4 rounded-lg shadow-xl relative overflow-hidden">
    <!-- 배경 게이지 (전체 범위: 100%) -->
    <div class="absolute top-0 left-0 h-full w-full bg-gray-[60%] opacity-5"></div>

    <!-- 현재 위험도 바 (예시: Critical) -->
    <div class="absolute top-4 left-2 h-1/3 w-[75%] bg-[#C70039] transform transition-all duration-1000 ease-out shadow-[0_0_20px_rgba(199,0,57,0.8)]"></div>

    <!-- 게이지 레이블 -->
    <div class="flex justify-between items-end text-sm mt-4 px-4 text-white/80">
        <span>최적 (Optimal)</span>
        <span class="text-[#C70039] font-bold animate-pulse">SYSTEM DEFECT DETECTED</span>
    </div>

    <!-- 중앙 상태 표시 -->
    <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center">
        <span class="text-3xl font-extrabold text-[#C70039]">CRITICAL</span>
    </div>
</div>
```

---

## 💾 Component 2: Defect ID 시스템 오류 로그 (System Error Log)
**위치:** 보고서 본문 내, 구체적인 문제 근거 제시 섹션. 전문성과 공신력 극대화 담당.
**형태:** 터미널 에뮬레이터 스타일의 고밀도 코드 블록.

### 💡 Spec & 구조
*   **배경/폰트:** Dark Charcoal Gray (`#2C3E50`), Monospace Font (예: Roboto Mono).
*   **구조화된 로그 항목:** 각 오류는 명확한 시간, 코드가 필수적임.
*   **필수 필드:** `[TIMESTAMP]` | `<DEFECT_ID>` | `[SEVERITY]` | `ERROR MESSAGE`

### 🖥️ 개발자 가이드라인 (Mockup HTML/Tailwind Classes)
```html
<div class="error-log-container bg-[#2C3E50] text-green-400 p-4 rounded-lg shadow-[inset_0_0_15px_rgba(199,0,57,0.3)] font-mono text-sm">
    <h3 class="text-lg font-bold border-b border-[#C70039] pb-2 mb-3 text-white/90">
        SYSTEM LOG: DETECTED ANOMALIES (Critical)
    </h3>

    <!-- 로그 항목 1: Critical Error -->
    <div class="log-entry py-1 border-b border-[#34495e]">
        <span class="text-yellow-400">[2026-11-21T13:42:12]</span> &nbsp; 
        <span class="text-[#C70039] font-bold">ERROR CODE: LPB-A7 (METABOLISM)</span>&nbsp; 
        <span class="text-white/80">[CRITICAL]</span>&nbsp; 
        <span>ATP/ADP Ratio below threshold. Mitochondrial function degradation confirmed. Immediate intervention required.</span>
    </div>

    <!-- 로그 항목 2: Warning Error -->
    <div class="log-entry py-1 border-b border-[#34495e]">
        <span class="text-yellow-400">[2026-11-21T13:42:10]</span> &nbsp; 
        <span class="text-orange-400 font-bold">WARNING CODE: TJC-B3 (JUNCTION)</span>&nbsp; 
        <span class="text-white/80">[WARNING]</span>&nbsp; 
        <span>Tight Junction protein expression reduced. Barrier function compromised. Nutritional support gap suspected.</span>
    </div>

    <!-- 로그 항목 3: Informational -->
    <div class="log-entry py-1">
        <span class="text-green-400">[2026-11-21T13:42:05]</span> &nbsp; 
        <span class="text-blue-400 font-bold">INFO CODE: N/A</span>&nbsp; 
        <span class="text-white/80">[INFO]</span>&nbsp; 
        <span>Baseline data acquisition successful. Analysis proceeding...</span>
    </div>
</div>
```

---

## 📊 Component 3: ATP/ADP 비율 변화 추이 그래프 (ATP/ADP Ratio Trend Graph)
**위치:** 보고서 핵심 진단 섹션. 과학적 근거 제시의 가장 중요한 시각 자료.
**형태:** 시간 경과에 따른 비율 변화를 보여주는 라인 그래프.

### 💡 Spec & 구조
*   **데이터 포인트:** Time (X축: 주차/월) vs. Ratio (Y축: 0.5 ~ 1.2).
*   **핵심 메시지 전달:** 시간의 흐름에 따라 비율이 급격히 떨어지는 추세(하강 곡선).
*   **시각적 경고:** 특정 임계점(예: 0.8) 아래로 떨어질 때, 라인과 영역 모두 Crisis Red 패턴으로 전환되어야 함.

### 🖥️ 개발자 가이드라인 (Mockup SVG/React Component Structure)
```html
<div class="graph-container bg-[#1F2A3B] p-6 rounded-xl shadow-inner border-t-4 border-[#C70039]">
    <h3 class="text-2xl font-bold text-white mb-2">ATP/ADP Ratio Decline Analysis</h3>
    <p class="text-sm text-yellow-500 mb-6">⚠️ Warning: 임계점 (Threshold) 0.8 이하로 하락 시, 세포 에너지 생산 시스템에 심각한 결함이 발생했음을 의미합니다.</p>

    <!-- SVG Placeholder for the Graph -->
    <svg width="100%" height="350" viewBox="0 0 600 350" class="bg-[#2C3E50] rounded-lg">
        <!-- X & Y Axis Lines (Deep Navy) -->
        <line x1="50" y1="300" x2="550" y2="300" stroke="#1A2338" stroke-width="2"/> <!-- X Axis -->
        <line x1="50" y1="20" x2="50" y2="320" stroke="#1A2338" stroke-width="2"/> <!-- Y Axis -->

        <!-- Critical Threshold Line (Crisis Red) -->
        <line x1="50" y1="240" x2="550" y2="240" stroke="#C70039" stroke-dasharray="8, 8" stroke-width="2"/>

        <!-- Data Line (Initial Optimal: Deep Navy -> Decline: Crisis Red) -->
        <polyline points="50,200 100,180 150,160 200,140 250,120 300,90 350,70 400,60 450,55 500,52 550,50"
                  fill="none" stroke="#1A2338" stroke-width="3"/>

        <!-- Critical Zone Area (Crisis Red fill) -->
        <path d="M 300,140 C 350,110 400,90 450,70 L 450,320 L 300,320 Z" fill="#C70039" opacity="0.2"/>
    </svg>

</div>
```

---
**[개발 인계 요약]**

| 컴포넌트 | 목적 | 핵심 색상 | 개발 시 유의사항 |
| :--- | :--- | :--- | :--- |
| **위험도 게이지** | 즉각적인 경고/권위 확보 | Crisis Red (#C70039) | 애니메이션 전환 효과(Transition)를 반드시 적용하여 긴장감을 유지할 것. |
| **시스템 오류 로그** | 전문성 및 공신력 극대화 | Deep Navy / Monospace Font | 일반 텍스트와 명확히 구분되는 '터미널' 느낌을 살릴 것. `[DEFECT_ID]`는 항상 강조되어야 함. |
| **ATP/ADP 그래프** | 과학적 근거 제시, 공포 조성 | Crisis Red (#C70039) | 0.8 임계점 이하의 데이터 구간은 시각적으로 분리하고 경고 애니메이션을 적용할 것. |

</create_file>

📊 평가: 완료 — CEO가 지시한 핵심 컴포넌트 3종에 대한 개발자용 스펙트(v2.0) 생성이 완료되어 인계 준비를 마쳤습니다.
📝 다음 단계: Developer 에이전트에게 이 MiniFunnel 디자인 명세서와 에셋을 기반으로 실제 인터랙티브 프로토타입(Mockup) 제작을 요청합니다.

---
## 📁 파일 액션 결과

✅ 생성: ~\Work\Onhyun\MiniFunnel_DesignSpec_v2.0.md
