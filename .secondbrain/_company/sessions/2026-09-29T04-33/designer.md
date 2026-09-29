# 🎨 Designer — MiniFunnel 핵심 컴포넌트인 '[Module_StatusIndicator]'에 대한 최종 Technical Specification Sheet를 작성해 주세요. 이 사양서는 단순한 디자인 가이드가 아닌, 개발팀(코다리)이 즉시 구현할 수 있도록 다음 요소를 포함해야 합니다: 1) 각 오류 레벨(Error Level: Red/Yellow/Gold)별 상세 UI 상태 정의와 전환 로직. 2) 애니메이션 키프레임 타이밍 및 트랜지션 속도 (CSS 변수나 코딩 레퍼런스로 제시). 3) HOMA-IR, HbA1c 등 임계치 데이터를 받았을 때의 시각적 경고 강도(Intensity) 변화 공식. 이 문서는 개발자 중심이어야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시에 따라, MiniFunnel의 핵심 컴포넌트인 `[Module_StatusIndicator]`에 대한 최종 개발자 중심 기술 사양서(Technical Specification Sheet)를 작성했습니다. 이 문서는 단순한 디자인 가이드가 아닌, 개발팀이 즉시 구현할 수 있도록 CSS 변수와 로직 흐름을 포함하여 공학적 위기감을 시각화하는 데 초점을 맞췄습니다.

---

# ⚙️ Technical Spec Sheet: Module_StatusIndicator (v1.0)
**컴포넌트 목표:** 사용자의 생체지표 데이터(HOMA-IR, HbA1c 등)를 임상적 위험도에 따라 시각화하고, 경고의 강도와 심리적 긴급감을 기술적으로 구현한다.
**타깃 개발자:** 코다리 (프론트엔드/UI/UX 엔지니어링 팀)

## 1. 컴포넌트 구조 및 입력 데이터 정의

| 요소 | 설명 | 타입 | 예시 값 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| `metricName` | 측정 생체 지표명 (Title) | String | HOMA-IR 수치 | UI 표시용 텍스트. |
| `currentValue` | 현재 사용자 데이터 값 | Number | 3.5 | 핵심 데이터. |
| `thresholds` | 임계치 설정 객체 | Object | `{ optimal: [0.5, 2.0], warning: [2.1, 3.0], critical: [3.1, Infinity] }` | 최소/최대 범위 지정 (배열 또는 숫자). |
| `errorLevel` | 최종 산정된 경고 레벨 | Enum | `CRITICAL`, `WARNING`, `OPTIMAL` | 내부 로직이 결정하는 상태. |

## 2. 오류 레벨별 UI 및 전환 로직 (State Machine)

`[Module_StatusIndicator]`는 다음의 세 가지 명확한 공학적 상태(States)를 가집니다. 이 상태들은 **데이터 기반**으로만 전환되어야 합니다.

| Level | State Name | 시각 목표 | CSS 변수 (`--color`) | 경고 강도 (Intensity) |
| :--- | :--- | :--- | :--- | :--- |
| **Red** | `CRITICAL` | 즉각적인 시스템 오류 발생 느낌. 가장 높은 위기감 조성. | `--color-red: #C0392B;` | $I \ge 0.8$ (가장 높음) |
| **Yellow** | `WARNING` | 경고 및 주의 필요. 개선이 시급함을 알림. | `--color-yellow: #F39C12;` | $0.4 \le I < 0.8$ (중간) |
| **Gold** | `OPTIMAL` | 시스템 정상 작동, 최적 상태 유지. 안정감 부여. | `--color-gold: #F1C40F;` | $I < 0.4$ (가장 낮음) |

### 2.1. 경고 레벨 결정 로직 (`determineErrorLevel(value, thresholds)`):
```typescript
// Pseudo Code for Logic Layer
function determineErrorLevel(currentValue: number, thresholds: any): 'CRITICAL' | 'WARNING' | 'OPTIMAL' {
    if (currentValue >= thresholds.critical[0] && currentValue <= thresholds.critical[1]) {
        return 'CRITICAL'; // Red State
    } else if (currentValue > thresholds.warning[0] && currentValue <= thresholds.critical[0]) {
        // Warning 범위가 Critical보다 낮고, 최적 범위보다 높은 경우
        return 'WARNING'; // Yellow State
    } else if (currentValue >= thresholds.optimal[0] && currentValue <= thresholds.optimal[1]) {
        return 'OPTIMAL'; // Gold State
    } else {
        // 데이터가 임계치를 벗어난 예외 처리 또는 기본 Warning으로 간주
        return 'WARNING'; 
    }
}
```

## 3. 애니메이션 및 기술 사양 (Animation & CSS Variables)

위기감을 조성하는 핵심은 **정적 색상**이 아닌 **동적인 변화(Kinetic Effect)**입니다. 모든 상태 전환에 다음의 공통 트랜지션을 적용해야 합니다.

### A. 기본 트랜지션 정의
```css
/* Root Component Wrapper */
.status-indicator {
    transition: background-color 0.5s ease-in-out, box-shadow 0.5s ease-in-out;
}
```

### B. 상태별 애니메이션 구현 (CSS Keyframes)

| State | 효과 | CSS Implementation Detail | 목적 및 근거 |
| :--- | :--- | :--- | :--- |
| **CRITICAL** | **Flashing/Pulsing Alarm** | `animation: pulse-red 1s infinite alternate;` <br> `@keyframes pulse-red { from { box-shadow: 0 0 5px var(--color-red); opacity: 1; } to { box-shadow: 0 0 20px var(--color-red), 0 0 30px rgba(192, 57, 43, 0.8); opacity: 0.9; } }` | **위험 임계치 시각화.** 강한 빛과 어두운 그림자의 대비로 공포감 조성. 주파수는 `calc(1s / var(--flash-frequency))`에 따라 조절. |
| **WARNING** | **Subtle Pulse/Breathing Effect** | `animation: breathe-yellow 2s infinite ease-in-out;` <br> `@keyframes breathe-yellow { from { transform: scale(1); opacity: 0.8; } to { transform: scale(1.03); opacity: 1; } }` | **주의 단계 시각화.** 너무 강하지 않으나, 현재 상태가 '정상 아님'을 지속적으로 상기시킴. |
| **OPTIMAL** | **Soft Glow (Ambient)** | `box-shadow: inset 0 0 8px rgba(241, 196, 15, 0.7);` <br> 애니메이션 없음. 배경을 은은하게 밝혀 안정감을 극대화. | **해결책 제시 단계 시각화.** 위협감에서 벗어났음을 안심시키며, 다음 액션(CTA)에 집중시킴. |

## 4. 경고 강도 변화 공식 (Intensity Scaling Formula)

단순히 범주형(`Red`/`Yellow`)으로만 표현하는 것이 아니라, **임계치 대비 얼마나 벗어났는지**를 수치화하여 시각적 강도를 조정해야 합니다.

### A. 지표 변동성 계수 ($D$) 계산
$D = \frac{|C - T_{avg}|}{T_{max} - T_{min}}$
*   $C$: `currentValue` (현재 값)
*   $T_{avg}$: 해당 레벨의 평균 임계치 (예: Warning 범위의 중간값)
*   $T_{max}, T_{min}$: 전체 임계치의 최대/최소 범위

### B. 시각적 경고 강도 ($I$) 산출 공식
$$ I = \text{Clamp}(\left(D - 1\right)^2 \times S, 0, 1) $$
*   $S$: Scale Factor (조정 가능한 상수, 예: 1.5). 이 값을 조정하여 경고의 민감도를 조절합니다.
*   $\text{Clamp}(x, min, max)$: $x$를 $[min, max]$ 범위로 제한하는 함수입니다.

**실제 적용:** 산출된 $I$ 값은 다음 세 가지 변수에 사용됩니다.
1.  `--intensity-factor`: (0.2 $\sim$ 1.0) CSS `box-shadow`의 확산 반경 및 투명도에 직접 적용되어, **시각적 크기**를 조정합니다.
2.  `--flash-frequency`: (0.5s $\sim$ 3s) Critical 상태에서 깜빡이는 주기를 결정하여, $I$가 높아질수록 **주파수를 높여 불안정성**을 극대화합니다.
3.  `background-saturation`: 배경 색상 코드에 투명도(Opacity)를 적용할 때, $I$ 값만큼 채도를 낮추거나 높여 **전반적인 톤의 긴급함**을 조정합니다.

---
📊 평가: 완료 — 개발팀이 바로 이해하고 구현 가능한 수준의 기술 사양서와 로직 흐름을 정의하여 목표가 달성되었습니다.
📝 다음 단계: 이 스펙 시트를 기반으로 실제 Figma/Sketch 파일에서 **인터랙티브 프로토타입**을 생성하고, 레오(영상 편집자) 및 코다리(개발팀)에게 테스트용 에셋 패키지를 전달해야 합니다.
