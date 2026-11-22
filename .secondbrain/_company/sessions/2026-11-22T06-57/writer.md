# ✍️ Writer — 디버깅 및 테스트에 사용될 최소한의 '테스트용 콘텐츠 스크립트 세트'를 작성해주세요. 이 스크립트는 Defect ID 보고서 형식(최소 3개 버전)을 유지하되, 콘텐츠 본문보다도 구조적 메타데이터(예: 가상의 KPI 수치, 측정 가능 결함 진단 체크리스트)가 명확하게 분리되어 개발자가 시스템 입력값을 테스트하기 용이하도록 구성해야 합니다.

✍️ Writer: 작업 시작합니다.

CEO의 지시에 따라 콘텐츠 본문보다도 **구조적 메타데이터와 개발자 테스트 환경에 최적화된 '테스트용 스크립트 세트'**를 작성했습니다. 이 스크립트는 실제 사용자가 보고서를 보는 최종 형태가 아니라, 시스템이 데이터를 입력받아 렌더링하는 과정을 검증하기 위한 '입력값 시뮬레이션 데이터'로 활용되어야 합니다.

세 가지 버전은 각각 다른 유형의 테스트 케이스(수치, 리스트, 비교)를 커버하도록 설계했습니다.

---

## 🧬 Defect ID Test Script Set V1.0
**목표:** 시스템이 복잡한 정량적 KPI 수치를 정확히 파싱하고 시각화하는지 테스트 (Numerical Data Focus)
**가상 주제:** '만성 염증으로 인한 근골격계 결함 진단'

### 📝 스크립트 구조 및 가이드라인
*   **[START_NARRATIVE]**: 사용자에게 위협을 제시하며 보고서의 필요성을 각인시킵니다. (최소한의 스토리텔링)
*   **[TEST_DATA: CORE_METRICS]**: 시스템이 가장 먼저 읽어야 할 핵심 KPI 데이터 블록입니다. 모든 수치와 단위는 명확히 구분되어야 합니다.

### 🎬 테스트 스크립트 본문 (Narrative Draft)

(0초~5초 후킹) "혹시 만성적인 통증을 '나이 탓'으로만 돌리고 계신가요? 그것은 결함입니다."
**(중반부)** "저희 Defect ID 시스템은 단순한 증상을 넘어, 염증 수치가 당신의 근골격계에 미치는 **정량적 손실 리스크**를 분석합니다. 이 데이터가 바로 당신이 놓치고 있는 핵심 정보입니다."
(마무리) "당신의 몸 상태는 숫자로 말합니다. 다음 보고서를 통해 정확한 결함을 진단받으세요."

### 💻 개발자 테스트 입력값 (Source of Truth Data Block)

```json
{
  "report_id": "DEFECT-20261122-A",
  "user_profile": {
    "age_group": "45대 중반",
    "chief_complaint": "아침 관절 통증, 만성 피로"
  },
  "test_metrics": [
    {
      "kpi_name": "CRP (C-Reactive Protein)",
      "measured_value": 3.2,
      "unit": "mg/dL",
      "threshold_normal": "< 0.5",
      "deviation_risk": "HIGH",
      "test_fail_flag": true  // <-- [TEST INPUT: 수치 비교 및 플래그 테스트]
    },
    {
      "kpi_name": "HA (Hyaluronic Acid)",
      "measured_value": 0.45,
      "unit": "mg/L",
      "threshold_normal": ">= 1.2",
      "deviation_risk": "CRITICAL",
      "test_fail_flag": true  // <-- [TEST INPUT: 임계값 대비 하락폭 테스트]
    },
    {
      "kpi_name": "ROM (Range of Motion)",
      "measured_value": 65,
      "unit": "Degrees",
      "threshold_normal": ">= 80",
      "deviation_risk": "MEDIUM",
      "test_fail_flag": false // <-- [TEST INPUT: 정상 범주 데이터 테스트]
    }
  ],
  "diagnostic_summary": {
    "total_defect_score": 78, // [TEST INPUT: 종합 점수 계산 및 표시 테스트]
    "risk_level": "CRITICAL",
    "suggested_action_code": "MINIFUNNEL_CTA_A"
  }
}
```

---

## 🧪 Defect ID Test Script Set V2.0
**목표:** 시스템이 이산적인 체크리스트(Boolean/List)와 복합 진단 코드를 처리하는지 테스트 (List & Boolean Focus)
**가상 주제:** '식습관 및 라이프스타일에 따른 결함 진단'

### 📝 스크립트 구조 및 가이드라인
*   **[START_NARRATIVE]**: 직접적인 질문과 답변 형식으로 참여도를 높이며, 스스로 '결함을 인지하게' 만듭니다.
*   **[TEST_DATA: CHECKLIST]**: 사용자의 일상생활 패턴에 기반한 다중 체크리스트 구조를 테스트합니다.

### 🎬 테스트 스크립트 본문 (Narrative Draft)

(0초~5초 후킹) "아침 식사, 과장된 커피 한 잔이 당신의 몸에 주는 결함은 무엇일까요? 생활 습관만으로 수억 원대의 손실 리스크가 발생할 수 있습니다."
**(중반부)** "저희 시스템은 묻습니다. 단순히 '피곤하다'가 아니라, 어떤 **구체적인 행동 패턴**이 염증과 노화를 가속화하는지입니다. 당신의 생활 루틴에서 발견된 결함 항목들을 확인하세요."
(마무리) "당신의 일상에 숨겨진 위험 신호 5가지를 체크했습니다. 이 리스트를 통해 가장 먼저 막아야 할 'Defect Source'를 찾아내세요."

### 💻 개발자 테스트 입력값 (Source of Truth Data Block)

```json
{
  "report_id": "DEFECT-20261122-B",
  "assessment_type": "Lifestyle & Habit Diagnostic",
  "defect_checklist": [
    {
      "item_key": "STRESS_RESPONSE",
      "description": "스트레스 해소 방식: 폭식/과음 의존도",
      "is_present": true, // [TEST INPUT: 참(True)값 테스트]
      "severity_score": 8 // [TEST INPUT: 점수 산정 테스트]
    },
    {
      "item_key": "SLEEP_QUALITY",
      "description": "수면 중 깊은 수면(Deep Sleep) 부족 여부",
      "is_present": true, // [TEST INPUT: 참(True)값 테스트]
      "severity_score": 9
    },
    {
      "item_key": "DIET_PATTERN",
      "description": "오메가-3 결핍 및 가공식품 위주의 식단 패턴",
      "is_present": true, // [TEST INPUT: 참(True)값 테스트]
      "severity_score": 10
    },
    {
      "item_key": "ACTIVITY_LEVEL",
      "description": "주 3회 이상 근력 운동 여부 (최소 기준)",
      "is_present": false, // [TEST INPUT: 거짓(False)값 테스트]
      "severity_score": 2
    }
  ],
  "diagnosis_output": {
    "top_defects": ["Sleep Quality", "Diet Pattern"], // [TEST INPUT: 리스트 형태의 결함 키워드 배열 테스트]
    "risk_level": "HIGH",
    "suggested_action_code": "MINIFUNNEL_CTA_B"
  }
}
```

---

## 🔄 Defect ID Test Script Set V3.0
**목표:** 시스템이 '기준점(Before)'과 '개선된 상태(After)'를 비교하고, 그 차이를 시각적으로 강조하는 구조를 테스트 (Comparative Data Focus)
**가상 주제:** '맞춤형 영양 관리 전후의 인지 기능 개선 리스크'

### 📝 스크립트 구조 및 가이드라인
*   **[START_NARRATIVE]**: 시간 흐름에 따른 변화(Time-based Change)를 강조하며, '개선 가능성'을 보여줌으로써 희망과 위협을 동시에 자극합니다.
*   **[TEST_DATA: COMPARISON]**: Before/After 구조를 갖춘 데이터 블록입니다. 두 상태의 차이점(`delta`) 계산 로직 테스트가 핵심입니다.

### 🎬 테스트 스크립트 본문 (Narrative Draft)

(0초~5초 후킹) "혹시 최근 기억력이 예전 같지 않다고 느끼셨나요? 단순한 노화가 아닙니다. 당신의 인지 기능에 '시간적 결함'이 발생하고 있다는 신호일 수 있습니다."
**(중반부)** "우리는 과거와 현재를 비교합니다. 이 데이터는 추측이 아닌, 측정된 **신경학적 활성도**의 변화입니다. 그리고 가장 중요한 것은, 그 결함을 되돌릴 수 있는 '최소한의 행동 지침'을 제시한다는 점입니다."
(마무리) "과거의 당신과 비교해 보세요. 이 격차를 줄이는 것이 바로 오늘 해야 할 일입니다. 구체적인 솔루션을 확인하세요."

### 💻 개발자 테스트 입력값 (Source of Truth Data Block)

```json
{
  "report_id": "DEFECT-20261122-C",
  "assessment_type": "Cognitive Function Delta Report",
  "comparison_data": {
    "time_point_before": { // [TEST INPUT: 기준점(Before) 데이터 세트]
      "kpi": "Attention Span (주의 집중 시간)",
      "value": 15,
      "unit": "Minutes",
      "risk_score": 70
    },
    "time_point_after": { // [TEST INPUT: 개선 후(After) 데이터 세트]
      "kpi": "Attention Span (주의 집중 시간)",
      "value": 28,
      "unit": "Minutes",
      "risk_score": 45
    }
  },
  "defect_analysis": {
    "key_metric": "Delta Improvement (%)", // [TEST INPUT: 변화율 계산 로직 테스트]
    "calculated_delta": "+86.7%",
    "suggested_intervention": ["Omega-3 Supplementation", "Daily Brain Workout"], // [TEST INPUT: 개선에 필요한 행동 목록]
    "risk_level": "RECOVERABLE",
    "suggested_action_code": "MINIFUNNEL_CTA_C"
  }
}
```

---
📊 평가: 완료 — CEO의 요청에 따라 콘텐츠 본문보다 구조적 메타데이터 테스트를 최우선으로 하는 3가지 버전의 스크립트를 성공적으로 생성했습니다. 이 결과물은 개발자에게 필요한 '실행 가능한 데이터셋'을 제공합니다.
📝 다음 단계: 코다리 에이전트가 생성한 의존성 주입(Dependency Injection) 구조에 맞춰, 이 테스트용 데이터를 실제로 API 엔드포인트로 전송하고 시스템 렌더링을 시뮬레이션하는 통합 테스트 스크립트를 작성해야 합니다.
