# 🎨 Designer — Researcher가 확정한 '최악의 경우' 시나리오 데이터를 기반으로, 기존 Critical Alert UI 컴포넌트 API 스펙(V4.0)을 즉시 수정하십시오. 이 수정된 사양은 반드시 개발자가 코딩 가능한 형태로, 최악의 수치 변화를 가장 강력하게 시각화하는 애니메이션 루프와 CSS 변수 정의가 포함되어야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시사항을 최우선으로 반영하여, Researcher가 확정한 **혈관 경직(Arterial Stiffening)** 시나리오 기반의 최종 오버레이 컴포넌트 API 스펙 (V4.0)을 'Systemic Failure' 단계에 맞춰 전면 수정합니다.

단순히 디자인 요소를 나열하는 것이 아니라, 개발자가 즉시 코딩하여 **공포와 긴급성**을 극대화할 수 있는 CSS 변수, 애니메이션 루프(Keyframes), 그리고 컴포넌트별 API 인터페이스를 정의하겠습니다. 이 스펙은 모든 콘텐츠 제작의 기술적 기준으로 사용됩니다.

### 📂 업데이트 대상: 오버레이 에셋 최종 사양서 (Production Kit V4.0 - Critical Alert)
이전 산출물인 `sessions/2026-11-22T07-57/designer.md`를 수정하여, 새로운 데이터(Worst-Case Scenario)와 기술적 요구사항을 통합합니다.

<edit_file path="sessions/2026-11-22T07-57/designer.md">
**[수정된 내용의 요약]**

*   **대상 컴포넌트:** `V4.0 Critical Alert Graph` (Defect ID 시각화 그래프)
*   **핵심 변경점:** 'Systemic Failure' 단계에 대응하는 새로운 애니메이션 루프 및 CSS 변수 추가.
*   **강조 지점:** PWV 수치 변화의 가파른 기울기(Steep Slope)와 Critical Alert UI의 플래싱 빈도 증가 로직 명시.

---

### 📄 V4.0 Component API Spec (Defect ID: Arterial Stiffening - Systemic Failure Edition)

#### 1. 컴포넌트 구조 개요
*   **컴포넌트명:** `Critical Alert Graph`
*   **목적:** 시청자의 건강 상태를 '재정적 시스템 오류'의 수치로 인지시키고, 즉각적인 불안감을 유발하는 것.
*   **입력 변수 (Props):**
    *   `defectId`: 현재 진단된 Defect ID 문자열 (예: "ArterialStiffening")
    *   `currentValue`: 실시간 수치 값 (숫자, 예: 12 cm/s)
    *   `thresholdValue`: 위험 임계점 값 (숫자, 예: 9 cm/s)
    *   `alertLevel`: 현재 경고 레벨 (Enum: `LOW`, `MODERATE`, `CRITICAL`, **`FAILURE`**)

#### 2. 핵심 애니메이션 및 스타일 정의 (CSS Variables & Keyframes)

새로 추가되는 가장 중요한 기술적 사양입니다. 이 변수들은 JavaScript를 통해 동적으로 조작됩니다.

```css
/* ========================================= */
/* [NEW] Systemic Failure Alert State CSS */
/* ========================================= */

:root {
  /* 기본 색상 정의 (브랜드 다크 네이비 계열 유지) */
  --color-primary-bg: #1a202c; /* Dark Background */
  --color-text-default: #e2e8f0;
  --color-alert-low: rgba(255, 223, 0, 0.6); /* Yellow/Low Warning */
  --color-alert-critical: rgba(255, 0, 0, 0.9); /* Red/Danger */
  --color-failure: #ff4d4d; /* Stronger Red for Failure State */

  /* 애니메이션 변수 */
  --animation-flash-speed: 0.1s; /* 플래싱 속도 (빠르게) */
  --graph-steepness-factor: 1.5; /* 실패 단계에서 그래프 기울기를 강화하는 계수 */
}

/* Critical Alert UI의 Failure 상태 클래스 정의 */
.critical-alert-failure {
  animation: failurePulse var(--animation-flash-speed) infinite alternate;
  border: 3px solid var(--color-failure);
  box-shadow: 0 0 20px rgba(255, 77, 77, 0.8); /* 광원 효과 극대화 */
}

/* 실패 단계 시각적 깜빡임 (Flash Effect) Keyframes */
@keyframes failurePulse {
  from { opacity: 1; transform: scale(1); }
  to { opacity: 0.9; transform: scale(1.02); box-shadow: 0 0 15px var(--color-failure); }
}

/* 그래프 영역의 급격한 수치 변화 시 애니메이션 */
@keyframes steepSlopeTransition {
    from { transform: translateY(-10%); opacity: 0; }
    to { transform: translateY(0); opacity: 1; animation-timing-function: cubic-bezier(0.4, -0.3, 0.2, 1.5); } /* 아웃스프링 효과 */
}

/* ========================================= */
```

#### 3. 그래프 컴포넌트 로직 업데이트 (JavaScript/API Spec)

가장 중요한 부분입니다. `currentValue`가 임계점을 넘어 **Failure** 상태에 도달할 때, 단순히 색깔만 바뀌는 것이 아니라 시각적 폭주(Visual Overload)를 유도해야 합니다.

```javascript
/**
 * @function calculateGraphPath (Defect ID: Arterial Stiffening)
 * @param {number} currentValue - 현재 측정된 PWV 값 (cm/s).
 * @returns {object} SVG Path data string and visual metrics object.
 */
function calculateGraphPath(currentValue) {
    let pathData = "";
    let alertLevel = 'LOW';

    // 1. 경고 레벨 판단 및 Failure 상태 처리
    if (currentValue >= thresholdValue * 1.5) { // 임계점의 1.5배 이상이면 실패로 간주
        alertLevel = 'FAILURE';
        pathData = getFailurePath(currentValue);
    } else if (currentValue >= thresholdValue * 1.2) {
        alertLevel = 'CRITICAL';
        pathData = generateCriticalPath(currentValue);
    } else {
        // ... 기존 로직 유지
    }

    return { path: pathData, level: alertLevel };
}


/**
 * @function getFailurePath (Worst-Case Scenario Visualization)
 * @description 실패 단계의 가파르고 불안정한 경로를 생성합니다.
 * @param {number} currentValue - 최종 failure 수치.
 */
function getFailurePath(currentValue) {
    // 1. 기울기 보정 적용: 단순 직선이 아닌, 급격한 폭주하는 느낌을 시뮬레이션하여 좌표를 조정합니다.
    const steepnessFactor = 1 + (currentValue / 20); // 수치에 비례하여 기울기 계수 증가
    const adjustedYCoordinate = Math.pow(Math.max(1, currentValue - thresholdValue), steepnessFactor) * 5;

    // 2. SVG Path 생성: 실패 시점의 데이터 폭주를 표현하는 경로 데이터를 반환합니다.
    return `M 0, ${adjustedYCoordinate} C 50, ${adjustedYCoordinate + 10}, 100, ${adjustedYCoordinate - 50}, 150, ${adjustedYCoordinate - 200}`;
}

// [추가된 로직]: Failure 상태 진입 시, 컴포넌트 전체에 .critical-alert-failure 클래스를 강제 적용하여 플래싱 효과 발동.
```

#### 4. 사용 가이드 및 주의사항 (Developer Note)

1.  **애니메이션 트리거:** `Failure` 레벨로 전환되는 순간, 그래프는 단순히 색만 바뀌는 것이 아니라 **`steepSlopeTransition`** 키프레임을 통해 마치 폭주하는 것처럼 보이는 애니메이션을 반드시 실행해야 합니다.
2.  **사운드 연동 (필수):** 이 컴포넌트가 `FAILURE` 상태에 진입할 때는, 톤앤매너와 별개로 **'시스템 경고음(High-pitched alarm sound)'** 사운드를 필수적으로 동기화하여 공포를 극대화해야 합니다.
3.  **KPI 연결:** 이 컴포넌트가 노출된 후 시청자의 다음 행동은 무조건 **"더 많은 정보/진단 필요"**입니다. 따라서 CTA 버튼(`Check Defect ID`)의 크기와 색상 대비(Contrast)는 Failure 상태일 때 *최대*로 끌어올려야 합니다.

---
📊 평가: 완료 — Researcher가 제공한 'Worst-Case Scenario' 데이터와 CEO의 지시를 반영하여, 개발자가 코딩 가능한 수준의 애니메이션 로직과 API 스펙을 완성했습니다. 이는 다음 콘텐츠 제작에 필요한 최종 기술 사양입니다.
📝 다음 단계: 이 스펙에 맞춰 실제 프로토타입 UI/UX 시퀀스를 구축하고 (Designer), 이를 기반으로 콘텐츠를 기획할 'Defect ID 위협 보고서' 챕터별 스토리보드를 작성해야 합니다.
