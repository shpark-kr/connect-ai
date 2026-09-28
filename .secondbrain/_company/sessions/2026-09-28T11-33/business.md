# 💼 현빈 — 현빈이 정의한 Mini-App Funnel의 3가지 A/B 테스트 변수 세트(예: CTA 문구, 이미지 배치 등)에 대해, 성공 기준으로 설정된 KPI를 달성했는지 검증할 수 있는 가장 정교하고 구체적인 '추적 로직(Tracking Logic)'을 최종 확정해 주세요. 단순한 '전환율 증가'가 아닌, 어느 시점에서 어떤 이벤트가 발생해야 카운트되는지 (Event Trigger Points) 정의하는 것이 핵심입니다.

💼 현빈: 작업 시작합니다.

CEO 지시에 따라, Mini-App Funnel의 A/B 테스트 변수 세트별 성과 검증을 위한 가장 정교하고 구체적인 **'추적 로직(Tracking Logic)'**을 최종 확정하였습니다. 단순한 전환율 측정 단계를 넘어, 사용자의 심리적 동선(Emotional Journey)에 기반하여 이탈 지점과 핵심 액션 포인트를 명확히 정의했습니다.

이 문서는 개발팀 및 데이터 분석가에게 직접 전달되어 즉시 구현 가능한 수준의 상세 스펙으로 구성되었습니다.

---

# ⚙️ Mini-App Funnel A/B 테스트 추적 로직 (V3.0) 확정본

## 🎯 목적
Mini-App 사용자의 여정(User Journey) 전체를 세분화하여, 단순히 최종 전환 여부만 보는 것이 아니라 **'어떤 단계에서 이탈이 발생했고, 어떤 자극에 반응했는지'**를 정량적으로 분석함으로써 A/B 테스트의 성공 기준을 명확히 합니다.

## 🛠️ 추적 이벤트 정의 (Event Trigger Points)
모든 측정은 Google Analytics 4(GA4) 또는 Firebase 기반의 커스텀 이벤트를 활용하며, 각 단계별로 최소한의 임계값(Threshold)이 설정되어야 합니다.

### Step 1: 유입 및 인식 단계 (Awareness & Entry)
| 이벤트명 | 트리거 조건 (Event Trigger) | 측정 목적 | 비고/최소 임계치 |
| :--- | :--- | :--- | :--- |
| `mini_app_page_view` | LP 진입 시점. **(필수)** | Funnel 시작점 카운트 및 유입 경로 분석. | 페이지 로드 완료 기준 (DOM Ready) |
| `scroll_depth_25%` | 사용자가 랜딩 페이지 콘텐츠의 25% 이상 스크롤 했을 때. | 초기 관심도 측정. (이탈 방지 핵심 지표). | 스크롤 깊이는 '직선적'으로 카운트되어야 함. |
| `risk_score_view` | Deep Crimson Red(DCR) 경고 UI 컴포넌트를 화면에 로드하고 **최소 5초 이상 체류**했을 때. | 위기감 자극의 성공 여부 측정. (가장 중요한 지표). | 시간 기반 이벤트 (`time_on_element: 5s+`) 필수. |

### Step 2: 참여 및 흥미 단계 (Engagement & Interest)
| 이벤트명 | 트리거 조건 (Event Trigger) | 측정 목적 | 비고/최소 임계치 |
| :--- | :--- | :--- | :--- |
| `cta_click` | **'위험 스코어 점검하기'** 버튼을 클릭했을 때. | 명시적인 행동 의도(Intent) 포착. (핵심 전환 유입). | CTA 영역의 JS 이벤트 리스너 필수. |
| `data_input_start` | Mini-App 내 문의 폼/설문지 입력 필드 중 **최소 1개 이상**에 커서가 활성화되었을 때. | 실제 행동 개시(Action Initiation) 측정. (실제 참여도). | 빈칸으로 인한 이탈과 구분해야 함. |
| `mini_app_scroll` | Mini-App 내부 콘텐츠를 스크롤 할 때마다 10%씩 카운트하여 누적. | 깊이 있는 정보 습득 정도 분석. | 사용자가 페이지 하단까지 도달했는지 확인. |

### Step 3: 전환 및 목표 달성 단계 (Conversion & Goal)
| 이벤트명 | 트리거 조건 (Event Trigger) | 측정 목적 | 비고/최소 임계치 |
| :--- | :--- | :--- | :--- |
| `lead_magnet_download` | 리드 마그넷(PDF 등) 다운로드 버튼 클릭 및 파일 로딩 시점. | **1차 목표 달성 (가장 쉽고 빠른 전환)**. | 성공적으로 파일이 브라우저에 저장되는 순간 카운트. |
| `consultation_inquiry_start` | 상담 문의 폼의 첫 필드(`이름` 또는 `연락처`)를 입력하고 다음 단계로 이동하려 할 때. | **2차 목표 달성 (최종 매출 전환)**. | 이탈 전까지의 모든 데이터 수집에 사용됨. |
| `conversion_success` | 상담 예약 완료 페이지 도달 시점. (결제/신청 성공) | 최종 KPI 측정 기준점. | *Funnel의 End Point.* |

---

## 📊 핵심 성과 지표 (KPI) 정의 및 계산 로직

단순한 전환율 증가가 아닌, 이탈 원인을 추적하는 세 가지 계층적 KPI를 사용합니다.

### 1. 위기감 유도 효율성 (Criticality Score)
*   **측정 목표:** 콘텐츠가 시청자에게 충분한 '위험 인지'를 심어줬는지 측정.
*   **KPI:** $\text{Criticality Ratio} = \frac{\text{risk\_score\_view 이벤트 발생 사용자 수}}{\text{mini\_app\_page\_view 총 사용자 수}}$
*   **A/B 테스트 가설 검증:** A안(DCR 강도 높음) vs B안(DCR 강도 낮음) 중, 비율이 더 높은 변수가 승리한다.

### 2. 참여율 (Engagement Rate)
*   **측정 목표:** 사용자가 콘텐츠에 흥미를 느끼고 다음 단계로 나아갈 의향을 보였는지 측정.
*   **KPI:** $\text{Engagement Rate} = \frac{\text{cta\_click 이벤트 발생 사용자 수}}{\text{mini\_app\_page\_view 총 사용자 수}}$
*   **A/B 테스트 가설 검증:** CTA 문구와 배치가 다른 변수 세트 간의 비율 비교.

### 3. 최종 전환 퍼널 완성도 (Funnel Completion Rate) - **최종 KPI**
*   **측정 목표:** 전체 유입 대비 실제 수익화 행동까지 도달한 사용자 비율.
*   **KPI:** $\text{Completion Rate} = \frac{\text{conversion\_success 이벤트 발생 사용자 수}}{\text{mini\_app\_page\_view 총 사용자 수}}$

## 📝 개발팀 구현 요구사항 (Implementation Checklist)
1.  **데이터 계층화:** 모든 추적 이벤트는 `(Event Name, Value, User ID)` 세 가지 축을 기준으로 반드시 기록되어야 합니다.
2.  **세션 유지:** 사용자가 이탈했다가 재방문했을 때도 'Mini-App Funnel' 내에서의 활동 여부를 **Unique Device ID 기반으로 7일간 추적**할 수 있도록 설정해야 합니다.
3.  **A/B 그룹 매핑:** 각 트래킹 이벤트에는 해당 세션이 어떤 A/B 테스트 변수(예: `ab_group_a`, `ab_group_b`)를 적용받았는지 태그가 필수적으로 붙어야 합니다.

---
📊 평가: 완료 — CEO 지시에 따라 요청된 모든 추적 로직 및 KPI 정의를 완성하여, 개발팀이 즉시 구현 가능한 형태로 산출물화했습니다.
📝 다음 단계: 데이터 분석 환경(GA4/Amplitude)에 본 트래킹 스펙을 반영하고, 실제 A/B 테스트 변수 세트 2가지를 선정하여 **'Mockup 기반의 초기 테스트 실행 준비'**를 진행해야 합니다.
