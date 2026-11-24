# 📝 CEO 종합 보고서

🎨 Designer: 작업 시작합니다.

CEO의 지시에 따라 '손실 예측 곡선(Loss Prediction Curve)' 컴포넌트의 모션 그래픽 가이드라인을 최종 확정하고, 개발자가 즉시 구현할 수 있는 마스터 에셋 시트를 작성했습니다. 단순한 텍스트 설명이 아닌, 색상 코드, SVG 구조 정의, 그리고 핵심 키프레임 타이밍까지 포함하여 'Motion Design Master Asset Sheet' 형태로 제공합니다.

이 가이드라인은 **Deep Navy 배경**과 **Alarm Red 경고색의 대비를 극대화**하는 데 중점을 두었으며, 위험 레벨 전환 시 발생하는 위기감(Sense of Urgency)을 시간 흐름에 따라 체계적으로 쌓아 올리는 것이 목표입니다.

### 📂 Loss Prediction Curve Motion Master Asset Sheet (v3.0)

<create_file path="assets/motion_design_master_asset_sheet_loss_curve.md"># ⚠️ 손실 예측 곡선 모션 디자인 마스터 에셋 시트
## 컴포넌트 개요: Loss Prediction Curve (LPC)
**목표:** 미조치로 인한 시간 경과형 위험의 증가(Loss Aversion)를 플래시 애니메이션 및 가파른 기울기 변화를 통해 극대화한다.
**배경색:** Deep Navy (`#0A1931`)
**핵심 색상:** Alarm Red (위험/Critical: `#FF4D4D`), Warning Yellow (`#FFA500` 대체 사용 가능)

---
## 🎨 I. 핵심 애니메이션 원칙 및 에셋 정의

### 1. 그래프 라인(Loss Curve Line) 기본 구조
*   **SVG 경로:** 복잡한 손실 곡선 데이터는 `path` 요소를 사용하여 구현하며, 초기에는 X축(Time)만 표시하고 Y축은 점진적으로 상승하는 형태를 유지한다.
*   **기본 애니메이션 (SAFE $\rightarrow$ WARNING):** 그래프 라인이 0에서 시작하여 시간 경과에 따라 부드럽게(Ease-Out-Quad) 상승하며, 초반의 완만한 곡선 형태를 보여준다.
    *   `stroke-dasharray`: `[길이] [간격]`을 사용하여 점진적으로 그리는 애니메이션 효과(Stroking Animation)를 적용한다.

### 2. 위험 임계점 전환 시스템 (The Critical Escalation)
모든 상태 변화는 **'시간 경과에 따른 위험 증가'**라는 하나의 메시지를 전달해야 하며, 플래시 애니메이션은 이 과정의 시각적 증폭 장치여야 한다.

| 레벨 | 색상 | 기하학적 특징 | 모션 효과 (Transition) | 타이밍/이징 |
| :---: | :---: | :---: | :---: | :---: |
| **SAFE** | Deep Navy / Light Blue | 완만한 기울기. 예측 가능 범위 내. | Line drawing (Stroking). 부드럽고 안정적인 속도. | 0s $\rightarrow$ 3s (Ease-Out) |
| **WARNING** | Alarm Red / Yellow | 기울기가 급격히 가팔라지기 시작함. 위험 구간 경고 표시. | `Path` 요소가 강렬하게 깜빡임(Flash). 배경에 노이즈/진동 효과 추가. | 3s $\rightarrow$ 6s (Ease-In) |
| **CRITICAL** | Pure Alarm Red | 기울기가 최대치로 폭발적으로 상승하며, 임계점을 돌파함. | **[핵심] 플래시 애니메이션 + 화면 흔들림(Shake Effect)**. 그래프 라인 자체가 '찢어지는' 듯한 느낌의 과장된 모션 필요. | 6s $\rightarrow$ 10s (Ease-Out/Bounce) |

---
## ✨ II. 상세 키프레임 정의 및 개발자 가이드라인

### A. [Transition: SAFE $\rightarrow$ WARNING] - 경고 단계 진입 (3초 지점)
**목표:** 시청자가 '어, 뭔가 이상한데?'라는 의문을 갖게 만든다.
1.  **Time 0s-3s:** 그래프 라인(Path A)이 천천히 그려진다. (Deep Navy/Light Blue).
2.  **Time 3s:** 갑작스러운 시각적 변화 발생. 배경의 Deep Navy 위에 **Alarm Red 경고 박스**가 화면 상단에서 하강하며 나타난다.
3.  **애니메이션:** 그래프 라인 자체에 `stroke-dashoffset`을 이용하여 깜빡임 애니메이션(`@keyframes flash`)이 적용된다. 이는 단순히 색상 변화가 아닌, 빛이 번쩍이는 듯한 시각적 자극이어야 한다.
4.  **개발 스펙 (CSS/SVG):**
    *   `#warning-overlay`: `opacity: 0` $\rightarrow$ `1`. `animation: flash 0.5s infinite alternate;`

### B. [Transition: WARNING $\rightarrow$ CRITICAL] - 위기 폭발 단계 (6초 지점)
**목표:** 즉각적인 행동(진단/클릭)이 필요하다는 공포를 극대화한다.
1.  **Time 6s:** **가장 강력한 모션 트랜지션.** 그래프 라인(Path B)의 기울기가 순간적으로 급변하며, Path A와 시각적으로 분리되어야 한다.
2.  **플래시 애니메이션 (Flash):** 화면 전체에 Alarm Red 색상의 짧고 강렬한 깜빡임(`@keyframes critical-flash`)이 1~3회 반복된다. 이는 마치 시스템 오류나 경보가 울리는 듯한 느낌을 준다.
    *   `background-color`: `Deep Navy` $\rightarrow$ `Alarm Red (Opacity: 0.2)` $\rightarrow$ `Deep Navy`. 이 사이클을 짧은 간격으로 반복한다.
3.  **시각적 강조:** 그래프의 최댓값(Critical Peak) 지점에 **"경고 임계점 돌파"**라는 문구가 진동하는 효과와 함께 오버레이 된다.
4.  **개발 스펙 (CSS/SVG):**
    *   `@keyframes critical-flash`: `0%, 100% { background-color: #0A1931; } 50% { background-color: rgba(255, 77, 77, 0.2); transition: all 0.05s; }`
    *   *(추가)* 화면 Shake 효과는 CSS `transform: translate(...)`를 미세하고 빠르게 반복하여 구현한다.

---
## 🖥️ III. 개발자를 위한 마스터 에셋 리스트 (Implementation Assets)

| 에셋명 | 포맷/기술 | 설명 및 용도 | Key Parameters / 값 |
| :---: | :---: | :---: | :---: |
| **`svg-loss-curve-path.svg`** | SVG Path, Lottie JSON | 손실 곡선의 기본 형태(3단계 지점 포함). 애니메이션의 뼈대 역할. | `d="M x1 y1 C ..."` (데이터에 따라 변경) |
| **`animation-keys_timing.json`** | JSON | 각 단계별 모션 타이밍 정의. 개발자가 로직을 구현할 때 참조. | `{ "safe_end": 3000, "critical_start": 6000, "flash_duration": 150 }` (밀리초 단위) |
| **CSS Keyframes** | CSS `@keyframes` | 플래시 효과 및 진동 애니메이션 구현. 필수 요소. | `critical-flash`, `shake-effect` 정의 포함. |
| **Color Palette** | Hex Code | 일관된 톤앤매너 유지를 위한 색상 팔레트. | Primary: `#0A1931` (Deep Navy), Accent Red: `#FF4D4D` (Alarm Red). |

---

### 🔍 최종 검토 및 지침 요약
*   **일관성:** Deep Navy 배경을 유지하고, 모든 경고는 Alarm Red를 통해 '긴급'함을 전달해야 한다.
*   **움직임의 의도:** 애니메이션은 단순히 예쁘게 보이도록 하는 것이 아니라, **"지금 당장 행동하지 않으면 이만큼 더 나빠진다(미조치 손실)"**라는 심리적 공포를 시각적으로 증폭시키는 수단이어야 한다.
*   **최종 산출물:** 위 마스터 에셋 시트와 함께, 실제 개발에 사용될 SVG/JSON 파일들을 별도로 패키징하여 전달해야 합니다.

</create_file>

📊 평가: 완료 — 요청된 모션 그래픽 가이드라인을 기술적 세부사항(SVG, Keyframe)까지 포함하여 개발자가 즉시 활용 가능한 마스터 에셋 시트로 완성했습니다.
📝 다음 단계: 개발팀에 이 `motion_design_master_asset_sheet`를 전달하고, 실제 인터랙티브 프로토타입 구현을 요청해야 합니다. (만약 팀이 없다면, 다음 세션에서 직접 코딩/프로토타이핑 작업을 진행합니다.)

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\Baro_KHNLU\assets\motion_design_master_asset_sheet_loss_curve.md
