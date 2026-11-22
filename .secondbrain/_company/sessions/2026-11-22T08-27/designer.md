# 🎨 Designer — Writer가 확정된 Day 1 (LDL 콜레스테롤) 스크립트와 Hook에 맞춰, 인스타그램 릴스 전용 오버레이 에셋을 최종 제작하십시오. 특히 'Critical Alert UI'와 LDL 수치 변화 그래프는 시청자가 가장 불안감을 느끼는 순간(약 3초 지점)에 최고 임팩트로 플래싱 효과를 주어 공포 요소를 극대화하도록 사양을 확정해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시와 이전 세션에서 완성한 'Production Kit V3.0'의 기술적 깊이를 결합하여, 인스타그램 릴스에 최적화된 **최종 오버레이 디자인 사양서**를 확정하겠습니다. 단순 이미지가 아닌, 영상 편집 및 개발자가 즉시 구현 가능한 애니메이션 로직과 코드를 포함하는 'Source of Truth' 문서를 생성해야 합니다.

이 문서는 Day 1 (LDL 콜레스테롤)의 Hook 시퀀스에서 공포 요소를 극대화할 수 있도록 **시간 축(Timeline)** 기반으로 설계되었습니다.

### 실행 계획
1.  `sessions/2026-11-22T07-27/designer`에 정의된 컴포넌트들을 인스타그램 릴스 비율(9:16)에 맞게 재배치합니다.
2.  3초 지점에 발생하는 'Critical Alert' 애니메이션의 구체적인 트리거, 타이밍(Timing), 시각적 변화(Opacity/Scale)를 규정하는 사양을 작성합니다.

<create_file path="sessions/2026-11-22T07-27/designer/Reels_Overlay_SourceOfTruth_V4.0.md"># 🚨 온현 - Defect ID 기반 인스타그램 릴스 오버레이 디자인 사양서 (V4.0)

## 🎯 목표
*   **플랫폼:** Instagram Reels (9:16 비율, 모바일 최적화).
*   **목표:** 시청자가 가장 불안감을 느끼는 순간(Peak Anxiety Moment, T+2.5s~T+3.5s)에 'Critical Alert' UI를 폭발적으로 노출하여 공포 요소를 극대화하고, 다음 행동(MiniFunnel 유도)으로의 전환을 강제한다.
*   **기준:** 기존 Production Kit V3.0의 모든 CSS 변수 및 애니메이션 로직을 따르되, 9:16 비율에 최적화하여 재정비함.

---

## 🎨 1. 핵심 디자인 시스템 가이드 (CSS Variables)

| 요소 | Variable 정의 | 값 (Value) | 목적/설명 |
| :--- | :--- | :--- | :--- |
| **Primary Color** | `--color-danger` | `#E63946` (진홍색 계열) | 위험 경고, 플래싱 배경. 시각적 충격 극대화. |
| **Secondary Color** | `--color-warning` | `#FFC300` (경고 노랑) | Metric Highlighting, 점멸 효과의 강조점. |
| **Background** | `--bg-dark` | `#14213D` (다크 네이비) | 전문성 및 신뢰도를 유지하는 기본 배경색. |
| **Text Color** | `--text-light` | `#F0F8FF` (밝은 청회색) | 가독성이 높은 주 텍스트 색상. |
| **Font Family** | `--font-primary` | 'Pretendard', sans-serif | 모든 타이틀 및 데이터에 일관되게 사용. |

## 📐 2. 오버레이 컴포넌트 사양 (9:16 레이아웃)

### A. Critical Alert UI (`#critical-alert`)
*   **배치:** 화면 상단 중앙 또는 하단 전면(Overlay). 다른 모든 콘텐츠를 가로지르는 **경고선 형태**가 가장 높은 임팩트를 준다.
*   **크기:** 너비 90%, 높이 15% (전체 화면 대비).
*   **애니메이션 로직 (T+2.5s ~ T+3.5s):**
    1.  **트리거:** LDL 수치가 기준치 초과 시점(스크립트 상의 불안감 최고조 지점)에 발동.
    2.  **효과 1 (배경 플래싱):** `background-color: var(--color-danger)`가 **0.1초 간격으로 3회 깜빡임(Flashing)**. (`opacity`와 `transition`을 활용한 빠른 전환 필수).
    3.  **효과 2 (텍스트 애니메이션):** "⚠️ WARNING: SYSTEM DEFECTION DETECTED" 문구가 강력하게 **Scale Up (>1.1) 후 Scale Down (1.0)** 하는 충격파(Shockwave) 효과를 동반하며 등장.
    4.  **추가 로직:** 플래싱 배경 위에 `[DEFECT ID: Elevated LDL]` 이라는 코드가 무작위로 깜빡이는 **디지털 글리치 효과**가 오버레이되어야 함.

### B. Metric Display (LDL 수치 변화 그래프)
*   **배치:** 화면 하단, Critical Alert UI와 겹치는 지점(Overlap Zone). 가장 큰 가시성을 확보해야 한다.
*   **형식:** 단순 숫자가 아닌 **'변화율'과 '위험 범위 시각화'**에 집중한다.
    1.  **핵심 수치 (현재 LDL):** `--color-danger` 배경 위에 `font-size: 8rem;` 크기로 크게 표시.
    2.  **기준선:** 과거 대비 상승 폭(예: +35%)을 화살표와 함께 명확히 보여주되, 이 화살표가 **강력한 진동 애니메이션 (Shake Animation)** 을 가져야 한다.
    3.  **위험 범위 그래프:** 단순 꺾은선이 아닌, 기준치 범위를 벗어나는 부분에만 `--color-danger`의 **'차폐(Shading)' 효과**를 주어 시각적 경고를 강화한다.

---

## ⚙️ 3. 개발자 구현 스펙 (Source of Truth)

### A. CSS Pseudo Code
```css
/* T+2.5s - T+3.5s 동안 적용될 애니메이션 */
@keyframes flash-danger {
    0%, 100% { background-color: var(--bg-dark); opacity: 1; }
    20% { background-color: rgba(230, 57, 70, 0.8); opacity: 1; } /* Flashing 1 */
    40% { background-color: transparent; opacity: 0.6; }
    60% { background-color: rgba(230, 57, 70, 0.8); opacity: 1; } /* Flashing 2 */
    80% { background-color: transparent; opacity: 0.6; }
}

#critical-alert {
    animation: flash-danger 0.4s ease-in-out infinite; /* 빠른 반복 효과 부여 */
    /* ... 기타 레이아웃 속성 정의 ... */
}

@keyframes scale-shockwave {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.2); opacity: 1; } /* 최대 크기 */
    100% { transform: scale(1); opacity: 1; }
}

#alert-text {
    animation: scale-shockwave 0.6s ease-out forwards;
}
```

### B. Timeline & Interaction Flow (가장 중요)

| 시간대 | 이벤트 (스크립트 내용) | 시각적 목표 | 오버레이 작동 사양 |
| :--- | :--- | :--- | :--- |
| **T+0s ~ T+2s** | *[훅 시작]* "혹시 당신의 콜레스테롤 수치를 안심하고 계신가요?" (전반적인 문제 제기) | 낮은 경각심, 전문성 강조. | Minimal Alert: 하단에 `Defect ID Monitor Active` 작은 텍스트만 배치. (`--color-warning` 포인트 색상 사용). |
| **T+2s ~ T+3s** | "하지만 이 수치는 당신의 혈관이 보내는 **최초 경고 신호**입니다." (불안감 고조) | 긴장감 조성, 시선 집중 유도. | Metric Display: LDL 수치 카운터가 급격히 올라가기 시작하며 배경에 미세한 노이즈(Noise Filter) 효과 추가. |
| **T+3s ~ T+5s** | "**당신의 콜레스테롤은 평균보다 몇 배 높습니다.** (실제 데이터 제시 지점)" (**Peak Anxiety**) | 최대 공포 자극, 시스템 오류 느낌 부여. | 🔴 **Critical Alert 발동:** 플래싱 배경 (`@keyframes flash-danger`) 작동. LDL 수치에 진동/충격파 효과 적용. 경고 문구(`⚠️ WARNING...`)가 화면을 장악하며 강제 시청 유도. |
| **T+5s ~ T+7s** | "이대로 방치하면, 미래의 당신은 막대한 비용을 치르게 됩니다." (문제 심화) | 공포를 재정적 손실 리스크와 연결. | Metric Display: 과거 대비 '재정적 손실 리스크' 그래프가 붉게 변하며 강조됨. Critical Alert는 점차 Opacity 감소하며 MiniFunnel CTA로 공간을 비움. |

---
</create_file>

**산출물 설명:**
이번에 생성된 `Reels_Overlay_SourceOfTruth_V4.0.md` 파일은 단순한 디자인 스펙이 아닙니다. 이는 **영상 편집자, 모션 그래픽 디자이너, 프론트엔드 개발자가 바로 코드를 짜거나 애니메이션을 적용할 수 있는 기술 사양서**입니다. 특히, 공포 요소 극대화를 위한 'Critical Alert'의 3단계 플래싱 및 충격파(Shockwave) 타이밍과 CSS 애니메이션 로직을 구체적으로 정의했습니다.

📊 평가: 완료 — CEO 지시사항인 '공포 요소를 극대화하는 오버레이 에셋 사양 확정'이 기술적 스펙과 타임라인 구조로 완성되었기 때문에 목표가 달성되었습니다.
📝 다음 단계: Writer에게 최종 Hook 및 스크립트의 **구체적인 데이터 수치(숫자, 백분율)**를 요청하여, 이 오버레이 사양서에 들어갈 '실제 임시 데이터'를 채우고 A/B 테스트용 텍스트 버전을 준비해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\sessions\2026-11-22T07-27\designer\Reels_Overlay_SourceOfTruth_V4.0.md
