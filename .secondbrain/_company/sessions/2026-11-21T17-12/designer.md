# 🎨 Designer — 지난 세션에서 확정된 '시스템 실패 보고서'의 UI/UX 명세(v1.0)를 기반으로, 개발자가 코딩할 수 있도록 모든 컴포넌트의 Props와 데이터 구조(JSON Schema 형태 권장) 정의서를 최종적으로 완성해 주세요. 특히, ATP/ADP 비율 변화 그래프는 데이터를 입력받았을 때의 렌더링 로직과 경고 색상(Crisis Red) 적용 기준을 명확히 제시해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시에 따라, 지난 세션에서 확정된 '시스템 실패 보고서'의 UI/UX 명세(v1.0)를 개발자가 즉시 코딩할 수 있는 컴포넌트별 **Props 및 데이터 구조 정의서**로 최종 완성했습니다.

이 문서는 디자인 에셋을 넘어, 데이터가 어떻게 시스템에 흐르고 어떤 로직으로 시각화되어야 하는지를 기술적으로 명시하는 '컴포넌트 카탈로그' 역할을 합니다. 특히 요청하신 ATP/ADP 그래프의 렌더링 로직과 경고 기준은 전용 컴포넌트에 상세히 포함했습니다.

이 정의서는 `SystemFailureReport_DeveloperSchema_v1.0.md` 파일로 저장되어 개발팀에 전달됩니다.

<create_file path="C:\Users\USER\Work\Onhyun\SystemFailureReport_DeveloperSchema_v1.0.md"># ⚙️ System Failure Report: Developer Component Schema Definition (v1.0)
**목표:** 'Defect ID 시스템 실패 보고서'의 모든 컴포넌트를 Atomic Design 원칙에 따라 재사용 가능한 Props와 데이터 구조(JSON Schema)로 정의합니다.

---

## 📊 전역 디자인 가이드라인 및 상수 (Global Constants)

| 항목 | 값/설명 | 역할 |
| :--- | :--- | :--- |
| **Primary Color** | Deep Navy (#0A1931) | 배경, 기본 텍스트, 전문성 강조 |
| **Accent Color** | Crisis Red (#C70039) | 경고, 위기감, 핵심 Defect ID 표시 (필수 사용 영역) |
| **Success Color** | #4CAF50 | 정상 상태(매우 드묾), 해결책 제시 완료 시점 |
| **Typography** | Pretendard / Noto Sans KR | 가독성 최우선. 제목은 Bold, 본문은 Regular 사용. |

### 1. 컴포넌트: 시스템 위험도 게이지 (SystemRiskGauge)
시스템의 현재 종합적인 건강 상태를 시각적으로 한눈에 보여주는 위젯입니다.

**Props 정의:**
*   `currentLevel`: (Number) 현재 위험 지수 (0부터 100까지).
*   `label`: (String) 게이지 하단에 표시될 간결한 설명 (예: "ATP/ADP Ratio Critical").

**데이터 구조 (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "currentLevel": {
      "type": "number",
      "description": "0(최상) ~ 100(최악). 비율이 높을수록 위험."
    },
    "label": {
      "type": "string"
    }
  },
  "required": ["currentLevel", "label"]
}
```

**🎨 경고 로직 (Critical Logic):**
*   `0 - 30`: Green/Deep Navy (정상)
*   `31 - 60`: Amber/Warning Orange (#FFC107) (주의 단계)
*   `61 - 100`: **Crisis Red (#C70039)** (위험/임계점 도달, 반드시 이 색상을 사용해야 함).

---

### 2. 컴포넌트: ATP/ADP 비율 추이 그래프 (SystemStatusGraph)
시간 경과에 따른 에너지 시스템의 변화를 보여주는 핵심 차트입니다. 가장 복잡한 로직을 가집니다.

**Props 정의:**
*   `dataPoints`: (Array<Object>) 시간별 데이터 배열.
*   `labelFormat`: (Function) X축 라벨 포맷터 (예: `(timestamp) => 'YYYY-MM-DD'`).
*   `warningThreshold`: (Number) 경고 임계값 (0.8).

**데이터 구조 (JSON Schema):**
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "timestamp": {"type": "string", "format": "date-time"},
      "atp_ratio": {"type": "number", "description": "ATP 비율 (0.0 ~ 1.0)"},
      "adp_ratio": {"type": "number", "description": "ADP 비율 (0.0 ~ 1.0)"}
    },
    "required": ["timestamp", "atp_ratio", "adp_ratio"]
  }
}
```

**🚨 핵심 렌더링 로직 (Rendering Logic):**
1.  **라인 색상 결정:** 현재 데이터 포인트의 `(atp_ratio + adp_ratio) / 2` 값을 기준으로 실시간으로 라인 컬러를 적용합니다.
    *   > **로직 조건:** 만약 `평균 비율 < warningThreshold` 이면, 해당 지점은 Crisis Red (#C70039) 계열의 음영 처리가 들어가야 합니다 (Shading Effect).

2.  **경고 영역 표시:** 그래프 하단에 명시적인 'Critical Zone' 배경 박스(Crisis Red와 Deep Navy의 그라데이션 활용)를 배치하여 사용자가 위험 임계점을 직관적으로 인지하게 해야 합니다. 이 존은 전체 차트 너비의 일정 비율을 차지해야 합니다.

---

### 3. 컴포넌트: 시스템 오류 로그 (ErrorLogComponent)
체내/시스템에서 발생하는 구체적인 '결함 ID' 기록 목록입니다.

**Props 정의:**
*   `logEntries`: (Array<Object>) 오류 로그 항목 배열.
*   `maxDisplayCount`: (Number, Optional) 한 번에 표시할 최대 개수 (예: 5개).

**데이터 구조 (JSON Schema):**
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "timestamp": {"type": "string", "format": "date-time"},
      "defectId": {"type": "string", "description": "예: ATP_DEFECT_001. 고유 Defect ID."},
      "severity": {"type": "string", "enum": ["CRITICAL", "HIGH", "MEDIUM", "LOW"], "description": "위험도 분류 (CSS 클래스에 영향)."},
      "description": {"type": "string", "maxLength": 150, "description": "오류 발생의 간결한 설명."},
      "status": {"type": "string", "enum": ["UNRESOLVED", "INVESTIGATING", "FIXED"], "description": "현재 조사 상태."}
    },
    "required": ["timestamp", "defectId", "severity", "description"]
  }
}
```

**🛠️ 인터랙션 요구사항:**
*   `severity`: `CRITICAL`일 경우, 해당 로그 항목의 배경에 미세한 **Glitch 애니메이션 효과**와 함께 텍스트가 깜빡이는(Flashing Red) 시각적 긴급성을 부여해야 합니다.

---

### 4. 컴포넌트: MiniFunnel CTA 버튼 (ActionCTAButton)
보고서를 본 사용자를 다음 단계로 유도하는 핵심 전환 요소입니다.

**Props 정의:**
*   `primaryText`: (String) 버튼에 표시될 문구 (예: "개인 시스템 진단 보고서 열람하기").
*   `secondaryText`: (String, Optional) 버튼 아래의 보조 설명 텍스트.
*   `targetURL`: (String) 클릭 시 이동할 MiniFunnel 페이지 URL.

**데이터 구조 (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "primaryText": {"type": "string"},
    "secondaryText": {"type": ["string"], "items": { "type": "string" }},
    "targetURL": {"type": "string", "format": "uri"}
  },
  "required": ["primaryText", "targetURL"]
}
```

---

## 📝 요약 및 개발 우선순위 (Summary & Priority)

| 순서 | 컴포넌트명 | 핵심 기능/로직 | 주의사항 |
| :--- | :--- | :--- | :--- |
| **P1** | SystemStatusGraph | ATP/ADP 변화 추이, Crisis Red 영역 자동 적용. | 데이터 바인딩 및 실시간 경고색 변경 로직 구현 최우선. |
| **P2** | ErrorLogComponent | Defect ID 기반 오류 로그 목록 표시. | `CRITICAL` 레벨에 Glitch 애니메이션 효과 필수. |
| **P3** | SystemRiskGauge | 종합 위험도 시각화 (0-100). | 전역 상수(Crisis Red)를 따르는 색상 로직 구현. |
| P4 | ActionCTAButton | MiniFunnel 전환 유도. | 버튼 클릭 시 애니메이션 피드백 및 URL 라우팅 검증. |

</create_file>

📊 평가: 완료 — CEO의 지시에 따라 핵심 컴포넌트별 기술 사양(Props, Schema, 로직)을 개발자가 바로 활용할 수 있는 형태로 완성했습니다.
📝 다음 단계: 이 스펙 기반으로 실제 Figma/Sketch 파일에 위 명시된 Props를 바인딩하고 인터랙션 시퀀스를 검증하는 작업을 진행해야 합니다. (Visual Prototype Test)

---
## 📁 파일 액션 결과

✅ 생성: ~\Work\Onhyun\SystemFailureReport_DeveloperSchema_v1.0.md
