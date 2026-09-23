# Gap 계산 API 명세서 (v2.0) - 코다리 검증 완료 버전
## 📄 개요 및 목적
본 사양서는 Master Archive 기반의 공적 지원 데이터와 사용자 입력 데이터를 결합하여 '재정 Gap 금액'을 산출하는 백엔드 API 엔드포인트의 구조를 정의합니다. 이 스펙은 프론트엔드의 Mini-Assessment 컴포넌트를 개발할 Designer에게 전달되며, 모든 인터랙션 및 계산 로직의 근거가 됩니다.

## ⚙️ 1. 핵심 API 엔드포인트
*   **Endpoint:** `/api/v2/calculate_gap` (POST)
*   **기능:** 사용자 프로필(나이, 소득 등)와 Master Archive 기반 필수 항목을 결합하여 '재정적 Gap' 금액과 주요 원인을 산출합니다.

## 📋 2. 요청 Body 스키마 (Input: Pydantic Model)
사용자 입력 및 시스템 전송 데이터는 아래 구조를 반드시 준수해야 합니다. 이 필드들은 프론트엔드의 `Gap-Assessment` 폼 컴포넌트에 매핑됩니다.

```json
{
  "user_profile": {
    "age": "Integer",           // 사용자 나이 (필수)
    "monthly_income": "Float",   // 월평균 가구 소득 (필수, 단위: 원)
    "household_size": "Integer" // 가구 구성원 수 (필수)
  },
  "assessment_items": [
    {
      "category": "요양/돌봄",       // 예: '장기요양', '간병'
      "needs_level": "String",     // 사용자 필요 수준 (예: '중증', '경증')
      "estimated_monthly_cost": "Float" // 예상 월 비용 (Master Archive 기반)
    },
    {
      "category": "주거/생활",       // 예: '교통비', '가사도우미'
      "needs_level": "String",
      "estimated_monthly_cost": "Float"
    }
  ],
  "master_archive_version": "YYYY-MM-DD" // 데이터 기준일자 (버전 관리를 위한 필드)
}
```

## 📊 3. 응답 Body 스키마 (Output: Pydantic Model)
API 호출 성공 시, 다음 구조의 JSON 객체를 반환합니다. 모든 Gap 계산 결과는 **Critical Red** 색상을 강조할 수 있는 `gap_amount`에 집중되어야 합니다.

```json
{
  "success": "Boolean",          // 처리 성공 여부 (True/False)
  "calculated_gap": {
    "total_gap_amount": "Float", // 최종 Gap 금액 (가장 중요, Critical Red 강조 대상)
    "unit": "KRW"                // 통화 단위
  },
  "breakdown": [                 // Gap 발생 세부 항목 목록
    {
      "category": "요양/돌봄",
      "gap_amount": "Float",     // 이 카테고리에서 부족한 금액
      "description": "공적 지원 대비 예상되는 추가 지출액입니다." // 사용자에게 보여줄 설명 텍스트
    },
    {
      "category": "주거/생활",
      "gap_amount": "Float",
      "description": ""
    }
  ],
  "source_data_links": [         // 근거 자료 제공 (신뢰도 확보 목적)
    {"type": "정책", "name": "국민연금 개정안"} // 사용자가 더 찾아보게 유도하는 링크
  ]
}
```

## ✅ 4. 핵심 로직 검증 포인트 (Developer Notes)
1.  **Gap 계산 공식:** `Total Gap = SUM(Needs Cost) - MIN(Public Support)`
2.  **오차 범위:** 모든 Floating Point 연산은 소수점 둘째 자리에서 반올림하여 원 단위로 표시해야 합니다.
3.  **에러 처리:** 필수 입력 필드 누락 시, `success: false`와 함께 명확한 에러 메시지 배열을 반환해야 합니다.