# 🔍 Researcher — MiniFunnel의 핵심 지표(HOMA-IR, hs-CRP 등)와 60개 이상의 시나리오 데이터셋을 기반으로 'Mock API 스키마 정의서'를 작성해주세요. 이 문서에는 모든 테스트 케이스가 매핑될 수 있는 JSON 필드 구조, 각 에러 코드 발생 조건(예: NameResolutionError), 그리고 상태 전이(State Transition)의 기준값/임계치 변수 목록을 상세히 포함해야 합니다.

🔍 Researcher: 작업 시작합니다.

CEO의 지시는 MiniFunnel 개발의 가장 핵심적인 단계인 '백엔드 데이터 구조화 및 검증'에 해당하며, 이는 모든 콘텐츠 기획과 트렌드 리서치 결과가 실제 시스템 로직으로 구현되는 기반이 됩니다. 현재 메모리에 있는 60개 이상의 시나리오 데이터셋을 통합하여, 개발팀이 즉시 E2E 테스트 환경 구축에 활용할 수 있도록 **Mock API 스키마 정의서**를 작성하겠습니다.

이 문서는 단순한 데이터 구조가 아닌, '위기 $\to$ 해결'이라는 상태 전이 로직과 그 실패 지점(Error Handling)까지 포함하는 설계 문서입니다.

---

# ⚙️ MiniFunnel Mock API 스키마 정의서 V1.0
**대상 시스템:** Mini-App Funnel (HOMA-IR 및 생체지표 기반 자가 진단 플로우)
**작성 목적:** 모든 테스트 시나리오(60+ Case)의 데이터 흐름, 상태 전이 임계치, 그리고 에러 처리 로직 정의.

## 1. API 엔드포인트 개요 (Conceptual Flow)

| Endpoint | HTTP Method | 역할 | 필수 입력 데이터 | 예상 출력 데이터 |
| :--- | :--- | :--- | :--- | :--- |
| `/api/v1/check-health` | POST | 초기 생체지표 수집 및 상태 진단. (Crisis Trigger) | `user_data`, `metrics_payload` | `{status: "CRISIS", score: 0.85, threshold_hit: ["HOMA-IR"]}` |
| `/api/v1/process-solution` | POST | 해결책(Complementary Product) 적용 및 상태 변화 로직 실행. | `user_id`, `product_ref`, `intervention_data` | `{status: "SOLUTION", score: 0.25, transition_time: "3s"}` |
| `/api/v1/log-event` | POST | 모든 사용자 액션 및 시스템 이벤트 로깅 (E2E Tracking). | `session_id`, `event_type`, `payload` | `{status: "OK", log_ref: "uuid-xxxx"}` |

---

## 2. 핵심 데이터 모델 스키마 (JSON Payload Structure)

모든 요청 및 응답에서 사용되는 표준화된 JSON 필드 구조입니다.

```json
{
  // [필수] 세션 추적 및 관리 정보
  "session_id": "UUID-STRING",             // 고유한 사용자 세션 식별자 (E2E 테스트 핵심)
  "user_id": "USER_INT",                   // 로그인/식별된 사용자 ID
  "timestamp": "ISO8601_DATE",             // 데이터 수집 시점

  // [필수] 주요 생체지표 페이로드 (Metrics Payload)
  "metrics_payload": {
    "homa_ir": 2.5,                        // HOMA-IR (공복 혈당 지표): 값 (Float), 기준값 범위 명시 필수
    "hs_crp": 3.1,                         // hs-CRP (염증지수): 값 (Float), 단위 (mg/L) 포함 권장
    "blood_pressure_systolic": 140,        // 혈압: 수축기 (Integer)
    "gut_score": 0.75                      // Funnel 내부 계산 지표 예시 (Float)
  },

  // [선택] 사용자 액션 및 컨텍스트 정보
  "context": {
    "source": "INSTAGRAM_REEL",            // 유입 경로 (Instagram, YouTube, Direct 등)
    "step": 2,                             // Funnel의 현재 단계 (1: 진단 -> 2: 위기감 -> 3: 해결책 제시)
    "cta_clicked": true                    // CTA 버튼 클릭 여부 (Boolean)
  },

  // [응답 시] 시스템 상태 및 결과
  "system_status": {
    "is_crisis": true,                    // 현재 상태가 '위기'인지 (Boolean)
    "current_score": 0.85,                // 계산된 위험 점수 (Float: 0.0 ~ 1.0)
    "suggested_action": "CHECK_PRODUCT",  // 시스템이 다음 단계에서 권장하는 행동
    "error_code": null                    // 에러 발생 시 코드 (예: METRIC_MISSING)
  }
}
```

## 3. 상태 전이(State Transition) 기준값 및 임계치 정의

MiniFunnel의 핵심은 데이터가 특정 **임계치(Threshold)**를 넘을 때 '상태'가 바뀌는 것입니다. 이 변수들은 개발팀이 반드시 코드로 구현해야 합니다.

| 상태 (State) | 진입 조건 (Trigger Condition) | 필수 기준값/임계치 (Threshold Variable) | 다음 상태 (Next State) |
| :--- | :--- | :--- | :--- |
| **HEALTHY** (건강) | $HOMA-IR < 1.5$ 이고, $hs-CRP < 1.0$. | HOMA-IR 임계치: $\leq 1.5$; hs-CRP 임계치: $\leq 1.0$. | `INFO_GATHERING` (정보 제공) |
| **CRISIS** (위기) | ($HOMA-IR \geq 2.5$) OR ($hs-CRP \geq 3.0$). | HOMA-IR 위험 임계치: $\geq 2.5$; hs-CRP 경고 임계치: $\geq 3.0$. | `SOLUTION_PRESENTATION` (해결책 제시) |
| **POST_INTERVENTION** (개선 단계) | 최초 CRISIS 진입 후, 특정 시간 간격($T$) 이후 재측정 지표가 개선됨. | HOMA-IR 감소율: $\geq 20\%$ ($T$ 기준); hs-CRP 변화량: $<-1.5$. | `SUCCESS` (성공/만족) |

**💡 핵심 변수 설명:**
*   **HOMA-IR 임계치:** 이 값이 높을수록 인슐린 저항성이 심각함 → 위기감 조성의 근거.
*   **hs-CRP 임계치:** 이 값이 높을수록 만성 염증 상태가 심각함 → 건강 문제의 전문적 증명.

## 4. 에러 코드 및 발생 조건 (Error Handling Schema)

시스템 안정성을 위해 필수적인 실패 시나리오와 그 처리 방법입니다.

| Error Code | 정의/발생 원인 | 발생 조건(Trigger Logic) | 개발팀 조치 요구사항 |
| :--- | :--- | :--- | :--- |
| `METRIC_MISSING` | 필수 생체지표 데이터가 누락됨. (예: HOMA-IR 값이 없음) | 입력 페이로드(`metrics_payload`)에서 필수 필드가 널(Null) 값일 경우. | 사용자에게 "필수 측정 항목을 다시 확인해주세요" 경고 UI 표시 후, 재측정 유도. |
| `NAME_RESOLUTION_ERROR` | 백엔드 서비스 간 API 연결 실패 또는 식별자 불일치. | 서버 내부 통신 중 외부 API 호출이 실패할 경우. | 시스템 메시지: "현재 진단 시스템에 일시적인 오류가 발생했습니다. 잠시 후 다시 시도해주세요." (Deep Crimson Red 경고 활용) |
| `DATA_OUT_OF_RANGE` | 수집된 데이터 값이 물리적으로 불가능한 범위를 벗어남. | HOMA-IR: $< 0$ 또는 $> 15$. 혈압: 음수 값 등. | 유효성 검증(Validation)을 통과하지 못한 데이터를 무시하고, 최신 유효 지표만으로 재진단 시도. |
| `SESSION_TIMEOUT` | 사용자가 일정 시간(예: 30분) 동안 Funnel에 접속하지 않음. | 세션 시작 후 $T_{max}$ 시간이 경과했을 때. | 사용자에게 "세션이 만료되었습니다. 다시 시작하시겠습니까?" 메시지와 함께 재로그인 유도. |

---
📊 평가: 완료 — 요청된 모든 요소(JSON 필드 구조, 에러 코드/조건, 상태 전이 임계치)를 포함한 Mock API 스키마 정의서가 완성되어 개발팀에 전달할 수 있습니다.
📝 다음 단계: 이 스키마를 기반으로 **Front-end와 Back-end 간의 데이터 연동 테스트 시나리오(Test Case Matrix)**를 작성하고, 각 에러 코드 발생 상황별 UI/UX 가이드를 Designer와 Writer에게 요청해야 합니다.
