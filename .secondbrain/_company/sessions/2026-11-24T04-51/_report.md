# 📝 CEO 종합 보고서

🎨 Designer: 작업 시작합니다.

CEO의 지시사항을 종합하고 지난 사이클에서 확립된 '손실 예측 곡선(Loss Prediction Curve)'의 모든 시각적, 심리적 동력(공포, 긴급성)을 한 곳에 응집하여 **'긴급 경고 시스템 (Urgency Alert System)'**의 최종 UI/UX 개발 스펙 문서를 작성합니다.

이 산출물은 단순 와이어프레임을 넘어, 코다리 개발자가 프론트엔드에서 즉시 구현할 수 있도록 색상 코드(HEX), 모션 타이밍(MS), 그리고 상태별 애니메이션 로직을 정의한 **디자인 시스템 컴포넌트 명세서**입니다.

---

# 🚨 [최종 스펙] 긴급 경고 패널 (Urgency Alert Panel) 개발 설계 문서

## 1. 목표 및 범위
*   **목표:** 사용자가 자신의 위험 지수(Gap Score)가 일정 임계점을 넘어서는 순간, 심리적 충격을 극대화하고 '즉각적인 행동'을 유도하는 인터랙티브 컴포넌트를 완성합니다.
*   **범위:** 손실 예측 곡선 MVP의 2단계 (Moderate) 및 3단계 (Critical) 구간 진입 시 작동하는 반응형 패널 전반에 대한 스펙 정의.

## 2. 디자인 시스템 가이드라인 통합
| 요소 | Deep Navy Background (Base) | Moderate Alert (Stage 2) | Critical Alert (Stage 3) | Action/Authority |
| :--- | :--- | :--- | :--- | :--- |
| **HEX 코드** | `#1A2438` | `#FFC107` (Amber) | `#D32F2F` (Alarm Red) | `#FFB300` (Gold/CTA) |
| **심리적 역할** | 안정성, 전문성 (Baseline) | 주의, 경고, 불안감 조성 | 패닉, 즉각적 위험, 공포 극대화 | 해결책 제시, 신뢰성 확보 |
| **폰트 스케일** | Body: 16px / Heading: 24px | Body: 16px / Heading: 20px (비중 증가) | Body: 18px (강조) / Heading: 30px (최대 강조) | Button: 18px |
| **경고 패턴** | 없음 | 은은한 깜빡임(Pulsating Glow) | 강렬하고 빠른 플래시/진동 애니메이션 | 명확하고 고정된 버튼 형태 |

## 3. 컴포넌트 상세 스펙: '긴급 경고 패널'
이 패널은 손실 곡선 그래프의 특정 지점을 통과할 때, 화면 중앙에 오버레이(Overlay) 되거나 해당 섹션 전체를 감싸는 형태로 작동해야 합니다.

### 💡 A. Stage 2 (Moderate Alert) 스펙: '주의 경고'
*   **발동 조건:** Gap Score가 **임계치 $T_{M}$** 에 도달할 때.
*   **시각적 변화:** 배경에 은은하게 황금빛/앰버(Amber)의 빛이 감돌며, 그래프 라인 자체가 주황색으로 변합니다.
*   **애니메이션 (Motion):**
    1.  **패널 등장:** `opacity: 0` $\rightarrow$ `opacity: 1` (Transition Time: $400\text{ms}$ Ease-in).
    2.  **경고 문구 효과:** "주의! 위험 지수 상승 감지" 카피가 배경에서 부드럽게 떠오르며(Float-up) 나타납니다. (Animation Delay: $100\text{ms}$).
    3.  **그래프 반응:** 그래프의 해당 구간이 느리지만 규칙적으로 **황금빛으로 맥동(Pulsing)** 합니다. (Interval: $2$초 $\rightarrow 400\text{ms}$ on / $2$초 $\rightarrow 400\text{ms}$ off).
*   **CTA 변화:** CTA 버튼이 황금색(`\#FFB300`)으로 변하며, "지금 점검해 보세요" (Soft Nudge) 카피가 표시됩니다.

### 🔥 B. Stage 3 (Critical Alert) 스펙: '최고 위험 경보'
*   **발동 조건:** Gap Score가 **임계치 $T_{C}$** 에 도달할 때. (사용자의 미조치 손실이 임박했을 때).
*   **시각적 변화:** 화면 전체에 Alarm Red 배경 오버레이(Opacity: $0.8$)가 적용됩니다. Deep Navy 본문 콘텐츠의 가독성은 떨어지나, 경고 패널은 최고 대비로 강조되어야 합니다.
*   **애니메이션 (Motion):**
    1.  **패널 등장:** 즉각적이고 강렬하게 나타납니다. `opacity: 0` $\rightarrow$ `opacity: 1` (Transition Time: $150\text{ms}$ Snap).
    2.  **플래시 효과 (필수):** 경고 패널의 배경 전체에 **초당 2회 이상** 주기로 Alarm Red 플래시가 깜빡여야 합니다. (`@keyframes flash { 0%, 100% { background-color: #D32F2F; } 50% { background-color: #FFEEEE; } }` $\rightarrow$ `animation: flash 0.1s linear infinite;`).
    3.  **진동 효과 (필수):** 패널 전체에 미세한 진동 애니메이션을 적용하여 긴급성을 극대화합니다. (`transform: translate(1px, 1px) !important`를 주기적으로 적용).
*   **CTA 변화:** CTA 버튼이 강렬하게 대비되는 Gold 색상으로 유지되며, **"즉시 자산 보호 계획 수립하기 (무료 진단 예약)"**라는 카피가 표시됩니다. 이 순간부터 모든 내용은 '공포' $\rightarrow$ '행동'의 흐름을 가져야 합니다.

## 4. 개발자 전달용 요약 테이블 (Codari Handover)
| 속성 | Stage 2 (Moderate) | Stage 3 (Critical) | 비고 |
| :--- | :--- | :--- | :--- |
| **배경색** | Deep Navy (`#1A2438`) | Red Overlay (`#D32F2F` @ $0.8$) | 오버레이는 반드시 `z-index: 999`로 최상위 배치. |
| **핵심 색상** | Amber (`#FFC107`) | Alarm Red (`#D32F2F`) | 모든 경고 요소에만 사용하도록 제한. |
| **주요 애니메이션** | Pulsing Glow (느린 맥동) | Flash & Shake (빠른 깜빡임/진동) | 플래시 빈도는 $50\text{ms}$ 주기로 설정. |
| **CTA 카피** | 점검 권유형 ("지금 확인해 보세요") | 패닉 유도형 ("즉시 행동해야 합니다!") | CTA 문구는 공포와 해결책의 대비를 강조. |

---
📊 평가: 완료 — CEO 지시에 따라, 개발자가 바로 구현 가능한 수준의 구체적인 디자인 시스템 컴포넌트 스펙과 모션 가이드라인을 완성했습니다.
📝 다음 단계: 이 최종 스펙에 맞춰, **랜딩 페이지 섹션별 와이어프레임**에 위 '긴급 경고 패널' 컴포넌트를 실제로 삽입하고, 전체 사용자 여정(User Flow)의 톤앤매너를 통일하는 작업을 진행해야 합니다.
