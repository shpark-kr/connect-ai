# Mini-App Funnel Risk Assessment API Contract v1.0
## 🎯 목적 (Purpose)
사용자가 제출한 여러 건강 지표 점수(Input Score Array)를 기반으로, 독립생활 상실 위험도를 수치화하고, 그에 따른 경고 수준을 정의합니다. 이 API는 클라이언트와 백엔드 사이의 **논리적 계약**입니다.

## 🔄 엔드포인트 (Endpoint)
*   **URI:** `/api/v1/assess_risk`
*   **Method:** `POST`
*   **인증:** Bearer Token (API 키 사용 권장)

## 📥 요청 바디 (Request Body - JSON Schema)
점수 입력은 최소 N개의 지표가 필요하며, 각 지표는 개별 점수를 가집니다.

```json
{
  "user_id": "string",              // 사용자 고유 ID
  "timestamp": "datetime",          // 요청 시간 (UTC)
  "score_inputs": [                  // 핵심: 입력된 모든 건강 지표의 원점수 배열
    { "metric_name": "hs-cpr_level", "score": 3.5 },
    { "metric_name": "insulin_sensitivity", "score": 72 },
    { "metric_name": "sleep_quality_index", "score": 6 }
  ]
}
```

## 📤 응답 바디 (Response Body - JSON Schema)
위험도 평가 결과와 함께 사용자에게 보여줄 구조화된 데이터를 반환합니다.

```json
{
  "success": true,                     // API 호출 성공 여부 (boolean)
  "timestamp": "datetime",             // 처리 시간
  "calculated_score": 85,              // 통합 위험 점수 (0~100)
  "risk_level": "CRITICAL",            // 핵심: 위험 레벨 (LOW, MEDIUM, HIGH, CRITICAL)
  "threshold_explanation": "독립생활 유지에 심각한 위협이 감지되었습니다. 즉각적인 전문가 상담이 필요합니다.", // 사용자에게 보여줄 설명 텍스트
  "data_breakdown": {                   // 디버깅/추가 정보용 구조화 데이터
    "hs-cpr_risk_factor": "High",
    "overall_alert_status": "Deep Crimson Red"
  }
}
```

## 🛡️ 상태 전이 규칙 (State Transition Logic)
1.  **점수 입력 $\rightarrow$ 위험 임계치 감지**: 백엔드 로직은 `score_inputs`를 받아 가중 평균 및 개별 지표의 심각도를 계산하여 최종 `calculated_score`와 이에 따른 `risk_level`을 결정합니다. (Critical: 75점 이상)
2.  **위험 임계치 감지 $\rightarrow$ 경고 UI 렌더링**: 프론트엔드는 `risk_level` 값에 따라 Deep Crimson Red 배경, 특정 애니메이션(예: 점수 게이지가 빨간색으로 변하며 깜빡임), 그리고 강력한 CTA(`threshold_explanation`)를 조건부로 렌더링해야 합니다.

---
**[기술 검증 포인트]**
*   백엔드는 반드시 API 계약에 정의된 스키마를 지켜야 하며, 유효성 검사를 거쳐야 합니다.
*   프론트엔드는 상태 전이에 따른 애니메이션 로직을 먼저 완성하고, 그 이후 데이터 바인딩을 진행해야 합니다.