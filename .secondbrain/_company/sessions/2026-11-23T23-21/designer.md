# 🎨 Designer — Deep Navy & Alarm Red 테마의 '손실 예측 곡선(Loss Prediction Curve)' 시각화 컴포넌트의 최종 UI/UX 스펙을 완성하세요. 특히, 위험 임계점(Warning/Critical) 도달 시 플래시 애니메이션 및 시간 흐름에 따른 가파른 기울기 변화를 위한 인터랙션 상세 가이드라인과 모든 에셋(SVG 경로 포함)을 개발자가 바로 구현할 수 있도록 명확히 분리하여 전달해야 합니다.

🎨 Designer: 작업 시작합니다.
CEO 지시에 따라 '손실 예측 곡선(Loss Prediction Curve)' 시각화 컴포넌트의 최종 UI/UX 스펙을 완성했습니다. 이 스펙은 개발자가 바로 코드로 구현할 수 있도록, 디자인 가이드라인, 인터랙션 상세 로직, 그리고 SVG 에셋 구조를 명확하게 분리하여 담았습니다.

이 문서는 단순히 이미지를 보여주는 것이 아니라, **시간에 따른 사용자 심리적 위기감(Loss Aversion)**을 극대화하는 *경험* 그 자체를 설계한 것입니다.

---

# 📐 Loss Prediction Curve: 최종 UI/UX & 개발 스펙 가이드

## 1. 디자인 시스템 개요 (Visual Identity)

| 요소 | 정의 및 목적 | 상세 스펙 | 비고 |
| :--- | :--- | :--- | :--- |
| **브랜드 컬러** | Deep Navy (신뢰, 배경), Alarm Red (위험, 경고) | `#0A1931` (Deep Navy - Background/Primary Text) / `#D42E2E` (Alarm Red - Critical Danger) | 톤앤매너의 핵심. 불안감을 극대화하기 위해 고채도 대비 사용. |
| **보조 컬러** | Off-White, Light Gray | `#F7F9FA` (Card/Text Background), `#CCCCCC` (De-emphasized Data) | 가독성 확보 및 깊이감 부여용. |
| **타이포그래피** | 전문적이고 권위 있는 느낌의 산세리프체 | Pretendard / Noto Sans KR (가장 높은 가독성을 가진 폰트 사용을 전제) | 제목: Bold, 본문: Regular. 명확한 위계 설정 필수. |
| **레이아웃 구조** | 전체 컴포넌트는 다크 네이비 배경 위에 배치되며, 곡선은 시각적 초점을 중앙에 집중시킨다. | 캔버스 크기: 16:9 비율 권장. Y축(손실액)과 X축(시간 경과) 명확한 라벨링 필수. |

## 2. 인터랙션 및 UX 로직 (The Core Logic: Fear of Loss)

이 컴포넌트의 핵심은 **정적 데이터가 아닌, 시간 흐름에 따른 위기감**을 전달하는 것입니다. 곡선 애니메이션과 경고 시스템을 분리하여 정의합니다.

### 2.1. 그래프 기본 구조
*   **축:** Y축 (손실액 / Loss Magnitude), X축 (시간 경과 / Time Elapsed).
*   **곡선 라인(SVG):** 손실 예측 곡선을 표현하는 주 요소. 시간이 흐름에 따라 이 곡선의 기울기($\text{Slope}$)가 핵심 변수입니다.

### 2.2. 상태별 인터랙션 상세 가이드라인 (State Transition)

| 상태 | 시간/위험도 | 시각적 특징 | 애니메이션 로직 |
| :--- | :--- | :--- | :--- |
| **✅ SAFE** | $Risk < \text{Warning Threshold}$ | 곡선은 완만하고, 색상은 Deep Navy 계열의 어두운 파란색 사용. 데이터 포인트는 분산되어 보임. | `ease-in` (느리고 부드러움). 기울기 변화 거의 없음. **(안심감)** |
| **⚠️ WARNING** | $\text{Warning} \le Risk < \text{Critical Threshold}$ | 곡선이 눈에 띄게 가팔라지며, 주 색상이 Red 계열로 전환되기 시작함 (Red-Orange). 데이터 포인트 주변에 미세한 노란색/주황색 점멸 효과 추가. | `ease-out` (점점 빨라짐). 기울기 변화가 선형적 증가를 보임. **(주의 환기)** |
| **🚨 CRITICAL** | $Risk \ge \text{Critical Threshold}$ | 곡선 전체가 Alarm Red `#D42E2E`로 채색되며, 가장 가파른 기하급수적 기울기를 유지함. 곡선의 윗부분에 `Flash Overlay`를 적용하여 깜빡임을 유도. | **Exponential Curve:** 애니메이션이 가장 급격하게 빨라지고(Acceleration), 예측 실패의 위기감을 극대화해야 함. (e.g., $\text{Time}^{2.5}$ 형태). |

### 2.3. 필수 인터랙션 이벤트
1.  **시간 흐름 시뮬레이션:** 사용자가 페이지에 진입하거나 콘텐츠가 로드될 때, 곡선은 **'0에서 현재 시점까지의 손실 누적 과정'을 시간 순서대로 재생(Play)**해야 합니다. 이 재생 속도는 3초 내외로 설정하여 즉각적인 위기감을 조성합니다.
2.  **Critical Flash Alert:** Critical Threshold에 도달하는 순간, 컴포넌트 전체 배경 위에 **Red/Black 플래시 애니메이션 (100ms On / 50ms Off)**이 최소 3회 반복되어야 합니다. 이와 동시에 경고음(System Error Sound)을 의무 적용합니다.
3.  **Hover Effect:** 마우스를 곡선 위로 올리면, 해당 지점의 손실액과 예측 시간을 팝업으로 보여주되, 배경에 **Deep Navy 색상의 반투명 오버레이**를 사용하여 집중도를 높입니다.

## 3. 개발자용 에셋 및 구조 명세 (Developer Assets)

개발자가 즉시 구현할 수 있도록 SVG 기반의 컴포넌트 구조와 가이드를 제공합니다.

### 3.1. SVG 경로 구조 설계
곡선은 단일 복잡한 SVG Path가 아닌, **`[Base Curve]` + `[Loss Marker]`** 두 개의 요소로 분리하여 관리해야 합니다.

```svg
<svg width="100%" height="400" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
  <!-- 1. 배경 그리드 및 축 (Deep Navy 계열) -->
  <rect x="0" y="0" width="800" height="400" fill="#0A1931"/>

  <!-- 2. 손실 예측 곡선 (Loss Curve Path) -->
  <!-- d 속성 값은 JavaScript로 계산된 시점별 좌표를 받아와야 함 -->
  <path id="loss-curve" 
        d="M 50,350 C 150,320 300,280 450,200 C 600,150 750,100" 
        fill="none" 
        stroke="#D42E2E" 
        stroke-width="4" 
        class="curve-line"/>

  <!-- 3. 경고 임계점 (Threshold Lines - Static Guide) -->
  <line x1="0" y1="150" x2="800" y2="150" stroke="#A0B0C0" stroke-dasharray="10 5"/>
  <line x1="0" y1="250" x2="800" y2="250" stroke="#FFCC00" stroke-dasharray="10 5"/>

</svg>
```

### 3.2. 컴포넌트별 스타일 가이드 (CSS/Tailwind 지침)
*   **`loss-curve` 클래스:** `transition: all 1s cubic-bezier(0.2, 1.0, 0.4, 1.5);`를 적용하여 애니메이션에 과장된 탄성 효과(Overshoot/Spring Effect)를 주어 위기감을 높입니다.
*   **`flash-overlay` 클래스 (Critical State):** `animation: flash 0.2s linear infinite;`를 사용하며, `keyframes`는 다음과 같이 정의합니다:
    ```css
    @keyframes flash {
        from { opacity: 0.1; background-color: #D42E2E; }
        to { opacity: 0.1; background-color: transparent; }
    }
    ```

---

📊 평가: 완료 — 개발자가 바로 코드로 옮길 수 있는 구체적인 UI/UX 스펙, 애니메이션 로직, 그리고 SVG 구조를 제공했으므로 목표가 달성되었습니다.
📝 다음 단계: 이 디자인 시스템을 활용하여 실제 콘텐츠에 적용할 **표준 썸네일 배너** 및 **인포그래픽 섹션의 최종 CTA 버튼 세트**를 제작해야 합니다.
