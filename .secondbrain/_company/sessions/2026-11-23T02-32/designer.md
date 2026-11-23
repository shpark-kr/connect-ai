# 🎨 Designer — 지난 브리핑에서 요청된 Glitch Effect와 Noise Overlay의 최종 디자인 명세서(Keyframe 및 CSS 기준)를 작성해 주세요. 이 스펙은 단순한 이미지가 아니라, 데이터 값이 'Critical Failure' 상태로 전환될 때 발생하는 시각적 교란(Data Disruption)을 가장 효과적으로 표현할 수 있는 구체적인 애니메이션 로직이어야 합니다. (예: `opacity` 변화, `transform` 이동, 노이즈 필터링 강도 등의 시작/종료 값을 명시)

🎨 Designer: 작업 시작합니다.

CEO님의 지시에 따라 'Critical Failure' 상태의 시각적 교란(Data Disruption)을 극대화할 수 있는 Glitch Effect와 Noise Overlay의 최종 디자인 명세서 및 구현 스펙을 작성했습니다. 이 스펙은 단순한 꾸밈 효과가 아니라, 사용자의 **인지 부하를 높여 위협감을 최대화**하고 궁극적으로 *무료 진단(리드 마그넷)* CTA로 유도하는 심리적 장치입니다.

이 명세서는 CSS Keyframe과 애니메이션 로직을 중심으로 작성되어, 개발팀에게 바로 전달 가능한 형태를 목표로 합니다.

---

## 📊 Glitch Effect & Noise Overlay 최종 디자인 스펙: Defect ID Gap 시각화

**대상 컴포넌트:** `DefectID_Graph_Component`의 데이터 값 표시 영역 (핵심 수치 및 그래프 라인)
**목표:** 사용자에게 '시스템 오류' 혹은 '생명체의 비정상적 작동'이라는 강한 위협감을 주어, 즉각적인 행동(진단 신청)을 유도한다.

### 1. 상태별 애니메이션 로직 정의 (States & Transitions)

| 상태 | Gap 수치/위험도 | 시각적 목표 | 주요 효과 요소 | CSS 난이도 |
| :--- | :--- | :--- | :--- | :--- |
| **Normal** | 임계점 이하 (안전) | 안정감, 전문성. 데이터의 신뢰도를 높임. | 미세한 라이트 그라데이션 애니메이션 (`@keyframes pulse-subtle`)만 적용. | Low |
| **Warning** | 임계점에 근접 (주의) | 불안정함, 경고. '현재 상태 유지 불가' 메시지 전달. | 낮은 주파수의 깜빡임(Blink), 미세한 횡방향 떨림(Jitter/Shake). 노이즈 필터 강도 $\alpha=0.1$. | Medium |
| **Critical Failure** | 임계점 초과 (위험) | **시스템 오류, 데이터 교란**. 공포감 극대화. | 고주파수 깜빡임(Stuttering), 픽셀 단위의 왜곡(Pixel Shift), 강한 노이즈 오버레이($\alpha=0.8$), 색상 채도 급변. | High (Focus) |

---

### 2. 핵심 기술 스펙: CSS/Keyframe 레벨 명세서

#### A. Critical Failure: Glitch Effect (`.glitch-critical`)
**목표:** 데이터 자체가 깨지고 있다는 인상을 주어, 객관적 진단이 필요하다는 압박감을 조성합니다.

```css
/* 1. 기본 컨테이너 설정 (애니메이션 적용 범위) */
.defect-data-container {
    position: relative; /* 자식 요소의 위치 기준점을 잡기 위함 */
    overflow: hidden;
}

/* 2. Glitch Layer 정의 (실제 왜곡 효과 담당) */
.glitch-layer {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background-image: linear-gradient(90deg, transparent 0%, rgba(255, 0, 0, 0.4) 50%, transparent 100%);
    /* Keyframe 애니메이션 적용 */
    animation: glitch-shift 0.1s infinite alternate;
}

@keyframes glitch-shift {
    0% { transform: translate(0); opacity: 1; }
    20% { transform: translate(-3px, -2px) skewX(5deg); opacity: 0.8; }
    40% { transform: translate(3px, 2px) skewY(-5deg); opacity: 1; }
    60% { transform: translate(-1px, 1px) scaleX(1.01); opacity: 0.9; }
    80% { transform: translate(1px, -1px) scaleX(0.99); opacity: 0.7; }
    100% { transform: translate(0); opacity: 1; }
}

/* 3. 깜빡임 및 스터터링 효과 (Rapid Flashing for Urgency) */
@keyframes flicker-stutter {
    0%, 19% { opacity: 1; } /* 정상 상태 유지 시간 */
    20%, 21% { opacity: 0.4; transform: scale(1.01); } /* 약하게 깜빡임 (Defect) */
    22%, 23% { opacity: 0.8; transform: skewX(1deg); } /* 불안정함 강조 */
    24%, 25% { opacity: 0.2; transform: scale(0.95); } /* 급격히 약해짐 */
}
```

#### B. Critical Failure: Noise Overlay (`.noise-overlay`)
**목표:** 데이터 신뢰도가 완전히 무너진 느낌을 시각화하여, '전문가의 진단' 외에는 답이 없다는 심리적 결론을 유도합니다.

```css
/* 1. 노이즈 필터 오버레이 (Pseudo-element 사용) */
.defect-data-container::after {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: repeating-linear-gradient(
        0deg,
        rgba(0, 0, 0, 0.2), /* Base Noise */
        rgba(0, 0, 0, 0.2) 1px,
        transparent 1px,
        transparent 2px
    );
    /* Keyframe 애니메이션으로 노이즈 진폭 변화 주기 */
    animation: noise-intensity 0.5s infinite alternate;
    pointer-events: none; /* 클릭을 방해하지 않도록 설정 */
}

@keyframes noise-intensity {
    from { opacity: 0.4; transform: scale(1); }
    to { opacity: 0.8; transform: scale(1.05) translate(-2px, 2px); } /* 강한 교란 표현 */
}

/* 추가 CSS 필터 (선택적 고도화) */
.defect-data-container.critical {
    filter: contrast(1.1) brightness(1.1); /* 전체 영역 대비 강조 */
}
```

### 3. 통합 구현 및 활용 가이드라인 (Implementation Guide)

*   **전환 로직:** 데이터 값이 `Threshold`를 초과할 때, 자바스크립트가 `.glitch-layer`, `.noise-overlay`, 그리고 `.critical` 클래스를 **순차적으로** 추가합니다.
    1.  (State Change: Warning) $\rightarrow$ 50ms 간격으로 깜빡임 활성화 (`flicker-stutter`).
    2.  (State Change: Critical) $\rightarrow$ `glitch-shift` 애니메이션과 `noise-intensity` 애니메이션을 **동시** 적용하며, 모든 요소에 높은 강도의 색상 왜곡(`box-shadow`와 `filter`)을 추가합니다.
*   **성능 고려:** Keyframe의 반복 속도(Animation Timing)는 0.1초 단위로 매우 빠르게 설정하여 시각적 '불안정' 느낌을 최대로 끌어올립니다. (성능 저하 최소화 위해 GPU 가속 효과를 고려해야 합니다.)

---
📊 평가: 완료 — CEO님이 요청하신 기술적 상세 스펙(Keyframe, CSS 변수)까지 완성되었으며, 다음 단계로 넘어가기 위한 충분한 시각적 근거가 마련되었습니다.
📝 다음 단계: 이 'Critical Failure' 상태의 강력한 위협감을 활용하여, 실제 사용자에게 진단 리드 마그넷을 다운로드하게 만드는 **최종 랜딩 페이지 CTA(Call-to-Action) 디자인 브리프**를 작성해야 합니다.
