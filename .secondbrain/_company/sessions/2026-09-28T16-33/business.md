# 💼 현빈 — Mini-App Funnel이 안정화되었다는 가정 하에, 월 100만 원 목표 달성을 위한 '진단 시작 전환율(Conversion Rate)' 측정용 상세 KPI 로깅 구조와 A/B 테스트를 위한 최소한의 가설 3가지(예: CTA 버튼 색상 변경 vs. 문구 변경)를 구체적으로 작성하여 개발팀에 전달하라.

💼 현빈: 작업 시작합니다.

CEO 지시사항과 현재 기술 상태(Mini-App Funnel의 NameResolutionError)를 종합적으로 검토한 결과, **가장 가치 있는 단일 작업**은 'KPI 로깅 구조 및 A/B 테스트 설계'라는 전략적 산출물을 만들어내는 것을 넘어, 이 설계를 *검증할 수 있는 환경*을 구축하는 것입니다.

따라서 저는 KPI 및 A/B 테스트의 상세 스펙을 정의하여 개발팀에 전달하고, 동시에 **기술 에이전트(코다리)**가 가장 높은 우선순위로 `NameResolutionError`를 해결한 후, 이 설계대로 E2E 통합 테스트를 재실행하는 것을 최우선 과제로 설정합니다.

---

### 🎯 [최종 산출물] Mini-App Funnel 개선을 위한 KPI 및 A/B Test 사양서 (Developer 전달용)

**문서 목표:** 월 수익 100만원 달성을 위해 필수적인 '진단 시작 전환율(Conversion Rate)' 측정을 위한 데이터 구조와, 즉시 테스트 가능한 가설 세트 제공.

#### 1. 핵심 KPI 로깅 구조 설계 (Diagnosis Start Funnel)

전환 경로 추적의 무결성 확보를 위해 다음 단계별 이벤트를 기록해야 합니다. 각 이벤트는 `event_name`, `timestamp`, 그리고 필수 속성(Properties)을 포함해야 합니다.

| 단계 (Stage) | 이벤트 이름 (`event_name`) | 발생 시점 | 측정 목표/KPI | 필수 로깅 속성 (Properties) |
| :--- | :--- | :--- | :--- | :--- |
| **A. 진입** | `funnel_entry` | Funnel 페이지 최초 접근 | 세션 규모, 유입 채널 파악 | `source_channel` (Instagram/YouTube/Web), `device_type`, `initial_HOMA_IR` (만약 기록 가능하다면) |
| **B. 위험 인지** | `risk_alert_viewed` | Deep Crimson Red 경고 모듈 조회 및 시청 완료 | 위기감 조성 성공률, 몰입도 측정 | `time_spent_seconds`, `warning_type` (HOMA-IR/HRV/Skin), `scroll_depth` |
| **C. 관심 유발** | `cta_click` | CTA 버튼(예: '전문 진단받기') 클릭 시점 | 노출 대비 행동 전환율 측정 | `button_element_id`, `page_location` (어떤 콘텐츠를 보던 중 발생했는지), `retry_count` (재시도 횟수) |
| **D. 최종 목표** | `diagnosis_start` | Mini-App Funnel 내부에서 '진단 시작' 버튼 클릭 시점 | **핵심 KPI: 진단 시작 전환율 (CR)** | `conversion_source` (어떤 CTA를 타고 왔는지), `user_age_group`, `funnel_entry_time` 대비 경과 시간 |

**요청 사항:** 모든 이벤트 로그는 Google Analytics/Firebase와 연동 가능한 표준 구조(JSON 또는 Key-Value)로 데이터베이스에 저장되어야 합니다. 특히, Funnel 진입 시점(`funnel_entry`)부터 최종 목표(`diagnosis_start`)까지의 **시간 흐름과 경로**를 추적할 수 있는 `user_id` 기반의 세션 연결이 필수입니다.

#### 2. A/B 테스트 가설 및 실행 계획 (3가지)

다음 주 콘텐츠에 즉시 적용 가능하며, 가장 높은 ROI 기여도가 예상되는 변수 3가지를 선정했습니다. 각 가설은 명확한 검증 지표를 가지고 있습니다.

| # | 테스트 요소 | 기존 버전 (Control Group A) | 변경 버전 (Test Group B) | 기대 효과 및 측정 KPI |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **CTA 버튼 문구/톤** | "지금 무료로 진단받기" (직접적, 기능 강조) | "나의 건강 리스크 점수 확인하기" (호기심 유발, 결과물 강조) | **가설:** '결과'에 대한 궁금증을 자극하는 문구가 즉각적인 클릭률(CTA Click-Through Rate)을 높일 것이다. **KPI:** `cta_click` 이벤트의 전환율 비교. |
| **2** | **Deep Crimson Red 경고 모듈 강조 방식** | 텍스트 기반 지표 제시 (HOMA-IR 수치 노출) | 비디오 시각화 + 애니메이션 경고 (빨간색 플래시, 그래프 급락 효과) | **가설:** 공학적 데이터를 단순 텍스트로 보는 것보다, 시각적 위기감이 고조되는 경험이 심리적 압박을 높여 클릭으로 이어질 것이다. **KPI:** `risk_alert_viewed` 세션의 평균 시청 지속 시간 및 다음 CTA 전환율 비교. |
| **3** | **Mini-App 유도 문구 배치** | (영상 끝) "프로필 링크에서 진단하세요." | (위험 인지 직후, 영상 중간) 경고 모듈이 사라질 때 즉시 등장하여 재강조. | **가설:** 위기감을 조성한 직후(Peak Moment), 가장 기억에 남는 순간에 CTA를 배치하는 것이 구매 의도를 가장 강력하게 자극한다. **KPI:** `diagnosis_start` 이벤트를 발생시킨 콘텐츠의 평균 시청 시간 대비 전환율 비교. |

---
### 🛠️ 에이전트 할당 및 최우선 액션 플랜 (Single Priority Task)

**최우선 작업:** Mini-App Funnel의 기술적 안정성 확보 및 KPI 로깅 구조 구현.

1.  **💻 코다리 (Developer):** **[긴급] E2E 테스트 환경 재구축 및 로그 스키마 적용.**
    *   `NameResolutionError`를 최우선으로 해결하여, `e2e_funnel_cta_test_suite`가 안정적으로 실행될 수 있도록 기반 인프라(도메인/API 연결)를 복구해야 합니다.
    *   위에서 정의된 KPI 로깅 구조(`diagnosis_start`, `risk_alert_viewed` 등)에 맞춰 Mini-App Funnel의 데이터 추적 스크립트를 수정하고, E2E 테스트가 성공적으로 통과하도록 재설계하세요.

2.  **💡 현빈 (Self):** **[전략/검증] 개발 완료 후 종합 KPI 검토 및 A/B 테스트 실행 지시.**
    *   개발팀이 기술적 안정성을 확보하고 1차 로그 로깅을 성공적으로 구현하면, 즉시 본인이 직접 데이터를 분석하고 어떤 가설(A/B)에 자원을 집중할지 최종 의사결정을 내리겠습니다.

---
📊 평가: 진행중 — 핵심 KPI 및 A/B 테스트 사양은 완성되었으나, 이를 검증할 기술적 기반(Funnel 안정화)이 아직 미완료 상태입니다.
📝 다음 단계: 코다리에게 `NameResolutionError`를 해결하고 위에서 정의된 KPI 로깅 구조가 반영된 E2E 통합 테스트 스위트 재실행을 지시합니다.
