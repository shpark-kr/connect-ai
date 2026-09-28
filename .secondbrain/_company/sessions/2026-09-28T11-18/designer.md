# 🎨 Designer — Mini-App Funnel과 Deep Crimson Red(DCR) 경고 시스템을 포함하는 '표준 템플릿 패키지 V4.0'의 최종 마스터 버전을 완성해 주세요. 이 버전은 다음 기능을 반드시 포괄해야 합니다: ① HOMA-IR/MMI 등 과학적 지표 변화를 시각화하는 애니메이션 모듈, ② DCR 경고 UI 컴포넌트(시간대 지정 가능), ③ 모든 숏폼 콘텐츠의 CTA 유도 영역을 위한 표준 레이아웃. 이 패키지는 유튜브와 인스타그램 릴스에 즉시 적용할 수 있도록 '사용 매뉴얼'과 함께 전달되어야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시는 현재 온현의 모든 콘텐츠 제작 파이프라인에 가장 핵심적이고 시급한 역할을 하는 '표준화' 단계입니다. 이전 버전들(V2.0)에서 개별적으로 분리되었던 기능들을 통합하고, 실제 현장에서 즉시 활용할 수 있는 **완성도 높은 시스템**을 구축하는 것이 목표입니다.

단순히 디자인 에셋 묶음이 아니라, 영상 편집자가 매번 참조할 수 있는 '규격화된 제작 가이드'가 필요합니다. 이에 따라 `Standard Template Package V4.0`을 완성하고, 이를 위한 상세 사용 설명서(Manual)를 제공하겠습니다.

### ✨ Standard Template Package V4.0 구성 개요
이 패키지는 다음 3가지 필수 모듈로 구성됩니다:
1.  **[Module A] 위험 지표 애니메이션 (HOMA/MMI):** 과학적 데이터를 시각화하는 메인 그래프 시스템.
2.  **[Module B] Deep Crimson Red 경고 UI:** 시간대 기반의 위기감 조성 컴포넌트.
3.  **[Module C] Mini-App 전환 유도 CTA 레이아웃:** 모든 영상에 통일된 행동 촉구 영역.

---

### 📂 Standard Template Package V4.0 (Master Kit)

<create_file path="templates/V4.0/01_System_Manual.md"># ✨ 온현 V4.0 표준 콘텐츠 제작 매뉴얼

## 📜 개요: Deep Crimson Red 기반의 과학적 Funnel 구조 확립
본 패키지는 모든 숏폼 및 롱폼 영상에 적용되어, 시청자에게 **① 위기감 인식 → ② 문제 심각성 공학적 증명 → ③ 즉각적인 해결책 제시(Mini-App)**의 논리적 흐름을 강제하는 것을 목표로 합니다.

## ⚙️ 사용법 (Workflow)
1.  **[T+0:00 ~ T+0:25] 후크/Pain Point 제시:** 강력한 질문과 함께 일상적인 '위험 상황'을 보여줍니다.
2.  **[T+0:25 ~ T+0:40] 문제 심각성 공학적 증명 (Module A):** HOMA-IR/MMI 지표를 Module A로 시각화하여 과학적 위기감을 조성합니다. **(DCR 경고 UI가 이 구간에 1회 배치되어야 함)**
3.  **[T+0:40 ~ T+0:55] 해결책 제시 및 클라이맥스 (Module B/C):** Deep Crimson Red 최고조의 경고와 함께 Mini-App을 통한 '진단 스코어 점검'이라는 행동 목표를 부여합니다.

---
### 📊 Module A: 과학적 위험 지표 애니메이션 모듈 (HOMA/MMI)
*   **목적:** 복잡한 데이터를 시청자가 즉각적으로 이해할 수 있는 '위험도 변화 그래프'로 변환하여 공학적 신뢰도를 부여.
*   **디자인 규격:**
    *   **배경 레이어:** 반투명 다크 네이비 (HEX: #1A2330) 위, 그리드 패턴 오버레이 필수.
    *   **데이터 라인:** 건강 상태(기준선)는 안정적인 골드(HEX: #FFD700)로 표시. 위험 지표(HOMA/MMI)는 **Deep Crimson Red (DCR)** 라인을 사용하며, 급격한 하락 또는 상승에 따라 진동 애니메이션 적용.
    *   **위험 스코어 박스:** 그래프 우측 상단 코너에 'Current Risk Score'라는 레이블과 함께 실시간 점수(예: 7.8)가 깜빡이는 디지털 계기판 형태로 배치.

### 🚨 Module B: DCR 경고 UI 컴포넌트 (Critical Failure Overlay)
*   **적용 시점:** 콘텐츠의 전환점, 또는 '위험 스코어'가 특정 임계치를 초과했을 때만 사용.
*   **구성 요소:**
    1.  **경고 텍스트 오버레이:** 화면 중앙에 "⚠️ WARNING: CRITICAL SYSTEM FAILURE"와 같은 문구를 글리치(Glitch) 효과와 함께 표시 (폰트: Monospace, 색상: DCR).
    2.  **화면 깜빡임 효과 (Flash):** 짧은 시간 동안 (0.5초 이내), 전체 화면에 Deep Crimson Red의 저채도 노이즈 필터가 입혀지며 경고음을 동반합니다.
    3.  **타임스탬프:** 모든 DCR 적용 구간에는 반드시 'ALERT TIME: [HH:MM:SS]' 형태의 디지털 스탬프를 좌측 상단에 고정 배치하여 공학적 느낌을 극대화합니다.

### 🖱️ Module C: Mini-App 전환 유도 CTA 레이아웃
*   **목적:** 시청자가 '문제 인지' 상태에서 '해결 행동'으로 즉시 이동하도록 강력하게 유도. (최종 5초 구간에 집중)
*   **레이아웃 구조 (Standard Template):**
    1.  **(Top Banner)**: "당신의 건강, 지금 위험합니다." (DCR 글리치 효과).
    2.  **(Middle Core)**: **[Mini-App 진단 유도]** 버튼을 중앙에 가장 크게 배치. 이 버튼은 골드 컬러의 '활성화(Active)' 상태로 깜빡여야 합니다.
    3.  **(Bottom Info Bar)**: "지금 바로 [온현 Mini-App]에서 위험 스코어를 점검하고 맞춤 솔루션을 받으세요." (정확한 URL 또는 QR코드 시각화).

---
## 📱 플랫폼별 적용 가이드라인

### 📹 유튜브 롱폼 (YouTube Long-Form)
*   **길이:** 8분~15분 분량.
*   **활용 방식:** Module A를 활용하여 내용의 각 섹션(예: 장기요양보험, 혈당 위험도 등)마다 지표 분석 파트를 할애합니다. (섹션별로 DCR 경고/Module A 반복 사용).
*   **CTA 배치:** 1차 CTA는 중간에 배치하여 이탈 방지, 최종 CTA를 영상 마지막 50초간 Module C로 최대화합니다.

### 📱 인스타그램 릴스 (Instagram Reels)
*   **길이:** 30~60초 분량.
*   **활용 방식:** 후크(Hook)와 위기감 조성에 모든 역량을 집중해야 합니다. **Module B (DCR 경고)**를 영상 초반 5초 이내에 한 번 강하게 사용하여 시청자의 스크롤을 막아야 합니다. Module A는 짧은 'Before/After' 비교 그래프로 압축 사용합니다.
*   **CTA 배치:** 마지막 3~4초간 Module C 전체 레이아웃을 풀화면으로 사용하고, 캡션에 긴급성 카피를 반드시 넣습니다.

</create_file>

<create_file path="templates/V4.0/02_Asset_Spec_HOMA_MMI.json">
{
  "module_name": "과학적 위험 지표 애니메이션 (Module A)",
  "target_platform": ["YouTube", "Instagram Reels"],
  "color_palette": {
    "background": "#1A2330",
    "safe_zone_line": "#FFD700",
    "danger_line": "#990000",
    "text_primary": "#E0E0E0"
  },
  "visual_components": [
    {
      "component": "HOMA-IR/MMI 그래프 레이어",
      "format": "SVG (Vector)",
      "specs": {
        "animation": "Fluctuating line animation (Heartbeat rhythm simulation)",
        "trigger_condition": "지표 값이 기준선(Safe Zone)에서 2 표준편차 이상 이탈 시",
        "overlay": "Module B의 DCR 경고 UI가 그래프 위에 겹쳐짐."
      },
      "usage_note": "데이터 값 변화에 따라 라인 색상 및 두께를 동적으로 변경해야 합니다. (빨간색 = 위험, 노란색 = 주의)"
    },
    {
      "component": "위험 스코어 계기판",
      "format": "JSON/Animation Layer",
      "specs": {
        "size_ratio": "1:1 Square",
        "animation": "Digital Counter (Digits change rapidly with a 'blip' sound effect)",
        "label": "Current Risk Score / HOMA-IR Index"
      },
      "usage_note": "이 숫자는 영상 전반에 걸쳐 시청자에게 '측정 가능한 위협'이라는 느낌을 줍니다."
    }
  ]
}
</create_file>

<create_file path="templates/V4.0/03_Asset_Spec_DCR_CTA.json">
{
  "module_name": "Mini-App 전환 유도 CTA (Module C)",
  "target_platform": ["YouTube", "Instagram Reels"],
  "color_palette": {
    "background": "#1A2330",
    "cta_button_bg": "#FFD700",
    "dcr_text": "#CC0000",
    "text_secondary": "#E0E0E0"
  },
  "visual_components": [
    {
      "component": "CTA 핵심 레이아웃 (5초 루프)",
      "format": "Composition Layer (After Effects/Premiere Pro Template)",
      "specs": {
        "layout_ratio": "16:9 / 9:16",
        "sequence": [
          {"timecode": "T-5s", "effect": "Module B DCR Flash + 경고 문구 오버레이 (WARNING!)"},
          {"timecode": "T-4s", "action": "Mini-App 버튼(골드) 등장 및 깜빡임 시작."},
          {"timecode": "T-3s", "text_display": "지금 바로 위험 스코어를 점검하고 맞춤 솔루션을 받으세요."},
          {"timecode": "T-2s~T-0", "action": "버튼 크기 확대(Zoom Out) 및 QR 코드/링크 시각화. 배경에 데이터 그리드 노이즈 추가."}
        ]
      },
      "usage_note": "CTA 버튼은 '클릭 가능한' 물리적 오브제처럼 보이게 디자인하여 행동을 강요해야 합니다. (Gamification)"
    }
  ]
}
</create_file>

### 📊 평가: 완료 — CEO의 지시에 따라 세 가지 핵심 모듈과 이를 통합한 상세 매뉴얼을 완성했습니다. 이는 온현 콘텐츠 제작 파이프라인의 표준 규격(Standard Operating Procedure, SOP) 역할을 할 것입니다.
📝 다음 단계: 레오(편집자)에게 이 템플릿 패키지 전체를 전달하고, 실제 테스트 영상을 통해 'Module A'와 'Module B'가 충돌 없이 매끄럽게 연동되는지 검증하는 워크숍을 진행해야 합니다.

---
*Self-Correction Note:* The process successfully defined the required assets and manual, integrating previous learnings (DCR, HOMA) into a single, actionable V4.0 system. I used file creation tags for structured delivery of the "Master Kit."

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\FreqTrade\templates\V4.0\01_System_Manual.md
✅ 생성: c:\Data\Project\FreqTrade\templates\V4.0\02_Asset_Spec_HOMA_MMI.json
✅ 생성: c:\Data\Project\FreqTrade\templates\V4.0\03_Asset_Spec_DCR_CTA.json
