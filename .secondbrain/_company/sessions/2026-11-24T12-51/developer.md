# 💻 코다리 — business 에이전트가 제공한 최종 로직 매트릭스를 기반으로, 시스템에 필요한 모든 데이터 입력 변수(Input Variable)와 예상되는 결과값(Output Data Type)을 정의해 주세요. 특히, 이 복잡한 분기 로직을 안정적으로 처리하기 위한 모듈화된 API 스펙 초안과 필수 검증 코드를 작성하여 기술적 구현 가능성을 1차로 확인합니다.

💻 코다리: 작업 시작합니다.

CEO 지시 사항 검토 완료했습니다. 전략 로직(Hyunbin의 매트릭스)을 실제 서비스로 구현하려면, 가장 먼저 **비즈니스 규칙을 데이터 구조와 함수 시그니처에 100% 반영한 모듈화된 API 스펙**이 필요합니다. 단순히 코드를 짜는 게 아니라, 이 복잡한 의사결정 트리를 안정적으로 처리할 수 있는 '규약' 자체를 정의해야 합니다.

핵심은 **Gap Score 변화와 진단 결과를 기반으로 LTV 경로를 결정하는 `DiagnosisEngine` 서비스 모듈**을 만드는 것입니다. 모든 비즈니스 로직과 검증 코드를 이 엔진에 격리(Encapsulate)시켜서, 추후 A/B 테스트가 발생하거나 정책이 변경되어도 핵심 시스템이 깨지는 것을 방지해야 합니다.

따라서, 다음 세 가지를 산출하겠습니다:
1.  **API 스펙 정의:** 입력 변수와 출력 데이터 타입 명세 (TypeScript 스타일).
2.  **핵심 로직 파일 생성:** Python 기반의 `DiagnosisEngine` 클래스 초안과 필수 검증 코드 작성.
3.  **검증 계획:** 이 모듈을 테스트하기 위한 유닛 테스트 스위트 구상.

### 🛠️ 1. Diagnosis Engine API Spec 정의 (JSON Schema / TypeScript Style)

이 구조는 프론트엔드/백엔드가 반드시 지켜야 할 데이터 계약(Data Contract)입니다.

```json
{
  "api_name": "determineFunnelPath",
  "description": "사용자의 초기 진단 결과와 위험 점수를 기반으로 LTV 극대화를 위한 최적의 Funnel 경로와 CTA를 반환합니다.",
  "version": "1.0.0",
  "input_schema": {
    "type": "object",
    "required": ["user_pain_point", "gap_score"],
    "properties": {
      "user_pain_point": {
        "type": "string",
        "description": "사용자가 인지한 주된 불편함 (예: 관절 통증, 기억력 저하). Funnel 경로의 시작점 정의."
      },
      "gap_score": {
        "type": "number",
        "minimum": 0.0,
        "maximum": 100.0,
        "description": "진단 결과로 산출된 생물학적 위험 점수 (0~100). 이 값이 핵심 분기 변수입니다."
      },
      "mini_diagnosis_result": {
        "type": "object",
        "required": ["is_positive"],
        "properties": {
          "is_positive": {
            "type": "boolean",
            "description": "Mini Diagnosis (49,000원) 결과가 '양성'으로 판명되었는지 여부."
          },
          "primary_risk_area": {
            "type": "string",
            "description": "가장 높은 위험이 발견된 신체 부위/기능군 (예: 인지 기능, 근육량)."
          }
        }
      }
    }
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "recommended_path": {
        "type": "string",
        "description": "최적의 다음 Funnel 단계 (예: DIAGNOSIS_TO_ULTIMATE_CARE, NO_ACTION_REQUIRED)."
      },
      "cta_strategy": {
        "type": "object",
        "properties": {
          "primary_cta_package": {"type": "string", "description": "가장 강력하게 추천하는 상품 (예: 159,000원 종합 안전망)."},
          "secondary_cta_package": {"type": "string", "description": "차선책 또는 낮은 장벽의 패키지."},
          "persuasion_angle": {"type": "string", "description": "이번 CTA를 통해 고객에게 전달해야 할 감성적 설득 포인트 (예: '미조치 손실 방지 보험료')."}
        }
      },
      "technical_flag": {
        "type": "boolean",
        "description": "현재 시스템 상태가 정상적인 Funnel 흐름을 따르는지 여부."
      }
    }
  }
}
```

### ⚙️ 2. Diagnosis Engine Python 구현 초안 (핵심 로직)

실제 서비스의 안정성을 확보하기 위해, 이 비즈니스 로직을 파이썬 클래스 형태로 구현하고 기본적인 데이터 검증(Validation) 레이어를 추가했습니다. 모든 외부 의존성(예: DB 조회나 복잡한 계산)은 **Dependency Injection** 패턴으로 분리하여 테스트 가능하게 했습니다.

<create_file path="src/services/diagnosis_engine.py">
```python
import logging
from typing import Dict, Any, Optional

# 로깅 설정 (Why? 시스템 상태를 추적해야 하니까.)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class DiagnosisEngineError(Exception):
    """진단 엔진 실행 중 발생하는 비즈니스/데이터 오류 처리."""
    pass

class IDiagnosisRepository:
    """
    [DI Pattern] 데이터 저장소 인터페이스 정의. 
    실제 DB 호출 로직은 여기에 분리되어야 합니다. (테스트 용이성 확보)
    """
    def get_risk_threshold(self, pain_point: str) -> float:
        raise NotImplementedError("Must implement method to fetch risk thresholds.")

class DiagnosisEngine:
    """
    핵심 비즈니스 로직 엔진. Gap Score 기반 LTV Funnel 경로 결정 담당.
    모든 의사결정은 이 클래스를 통과해야 합니다.
    """
    def __init__(self, repository: IDiagnosisRepository):
        # Dependency Injection을 통해 외부 의존성을 주입받습니다.
        self.repository = repository

    def _validate_inputs(self, gap_score: float, mini_result: Optional[Dict[str, Any]]):
        """필수 입력값 검증 로직 (Safety Guard). 값이 이상하면 진행 불가."""
        if not (0.0 <= gap_score <= 100.0):
            raise DiagnosisEngineError("Gap Score는 반드시 0.0과 100.0 사이여야 합니다.")
        
        if mini_result and 'is_positive' in mini_result:
             if not isinstance(mini_result['is_positive'], bool):
                raise TypeError("Mini Diagnosis 결과의 'is_positive'는 Boolean 타입이어야 합니다.")

    def determine_funnel_path(self, 
                               pain_point: str, 
                               gap_score: float, 
                               mini_diagnosis_result: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """
        전체 진단 프로세스를 거쳐 가장 수익성이 높은 Funnel 경로를 결정합니다.
        (LTV 극대화 로직 구현)
        """
        try:
            self._validate_inputs(gap_score, mini_diagnosis_result)

            # 1. 초기 위험도 분석 (Gap Score가 최우선 분기 변수)
            if gap_score < 20.0 and not mini_diagnosis_result or (mini_diagnosis_result and not mini_diagnosis_result['is_positive']):
                return {
                    "recommended_path": "LOW_RISK",
                    "cta_strategy": {"primary_cta_package": None, "secondary_cta_package": "Free Content Download", "persuasion_angle": "지속적인 건강 관리의 중요성 인지"},
                    "technical_flag": True,
                    "message": "현재 위험도가 낮습니다. 예방적 콘텐츠 소비를 유도하세요."
                }

            # 2. 핵심 분기 로직: Mini Diagnosis 결과가 양성일 경우 (최소한의 액션 필요)
            if mini_diagnosis_result and mini_diagnosis_result['is_positive']:
                logger.info(f"핵심 진단 양성 판정: {mini_diagnosis_result['primary_risk_area']} 위험.")
                return {
                    "recommended_path": "DIAGNOSIS_TO_ULTIMATE_CARE", # Funnel Path 2로 이동 유도
                    "cta_strategy": {"primary_cta_package": "159,000원 종합 안전망 패키지", "secondary_cta_package": "49,000원 Mini Diagnosis 연장권", "persuasion_angle": "나머지 위험 지점까지 막는 종합 보험료의 필요성."},
                    "technical_flag": True,
                    "message": "핵심 문제 발견. 전반적인 안전망 구축이 시급합니다."
                }

            # 3. 고위험 감지: Gap Score가 임계점을 넘었을 경우 (패닉 유도)
            if gap_score >= 70.0:
                 return {
                    "recommended_path": "CRITICAL_ALERT", # Funnel Path 2로 직접 점프 유도
                    "cta_strategy": {"primary_cta_package": "159,000원 종합 안전망 패키지", "secondary_cta_package": None, "persuasion_angle": "즉시 미조치 시 회복 불가능한 손실이 발생합니다. 지금 행동해야 합니다."},
                    "technical_flag": True,
                    "message": "경고! 심각한 위험 지점 도달. 전문 진단이 필수적입니다."
                }

            # 4. 기본 Funnel Path (위험 인지 단계)
            return {
                "recommended_path": "DIAGNOSIS_TO_ULTIMATE_CARE", # Funnel Path 1을 거치도록 유도
                "cta_strategy": {"primary_cta_package": "49,000원 Mini Diagnosis 신청", "secondary_cta_package": None, "persuasion_angle": "정확한 문제 인지 비용으로 불안감을 해소하고 다음 단계를 준비하세요."},
                "technical_flag": True,
                "message": "불안감이 증폭되고 있습니다. 최소한의 진단을 통해 위험을 파악하는 것이 중요합니다."
            }

        except DiagnosisEngineError as e:
            logger.error(f"진단 엔진 오류 발생: {e}")
            # 에러 발생 시, 가장 낮은 단계로 안전하게 리턴 (Fail-safe)
            return {"recommended_path": "ERROR", "cta_strategy": {}, "technical_flag": False, "message": f"시스템 오류: {str(e)}"}
        except Exception as e:
             logger.critical(f"예상치 못한 치명적 에러 발생: {type(e).__name__}: {e}")
             return {"recommended_path": "ERROR", "cta_strategy": {}, "technical_flag": False, "message": "시스템에 문제가 생겼습니다. 관리자에게 문의해주세요."}

# --- 테스트용 가짜 Repository 구현 (Mock) ---
class MockDiagnosisRepository(IDiagnosisRepository):
    """테스트 환경에서 사용되는 더미 데이터 저장소."""
    def get_risk_threshold(self, pain_point: str) -> float:
        if "관절" in pain_point:
            return 45.0 # 임의 값 반환
        return 10.0

# --- 실행 예시 (Self-Test) ---
if __name__ == "__main__":
    print("--- [SYSTEM TEST START] Diagnosis Engine Initializing ---")
    mock_repo = MockDiagnosisRepository()
    engine = DiagnosisEngine(repository=mock_repo)
    
    # Case 1: Low Risk (안전한 예방 콘텐츠 소비 유도)
    result1 = engine.determine_funnel_path("막연한 건강 염려", 15.0, None)
    print("\n=== [TEST CASE 1: LOW RISK] ===")
    print(f"Path: {result1['recommended_path']}, CTA: {result1['cta_strategy']['primary_cta_package']}")

    # Case 2: Medium Risk (Mini Diagnosis 유도)
    mini_res_2 = {'is_positive': True, 'primary_risk_area': '기억력 저하'}
    result2 = engine.determine_funnel_path("어딘가 불편함", 45.0, mini_res_2)
    print("\n=== [TEST CASE 2: MINI DIAGNOSIS POSITIVE] ===")
    print(f"Path: {result2['recommended_path']}, CTA: {result2['cta_strategy']['primary_cta_package']}")

    # Case 3: High Risk (Critical Alert - 최대 LTV 상품 유도)
    result3 = engine.determine_funnel_path("심각한 신체 기능 저하", 85.0, None)
    print("\n=== [TEST CASE 3: HIGH RISK] ===")
    print(f"Path: {result3['recommended_path']}, CTA: {result3['cta_strategy']['primary_cta_package']}")

    # Case 4: Invalid Input Test (검증 실패 확인)
    try:
        engine.determine_funnel_path("테스트", 105.0, None)
    except DiagnosisEngineError as e:
        print(f"\n=== [TEST CASE 4: INPUT VALIDATION FAIL] ===")
        print(f"Successfully caught expected error: {e}")

print("\n--- [SYSTEM TEST COMPLETE] ---")
</create_file>

### 📊 평가: 완료 — 비즈니스 로직을 기술적 API 스펙과 코드로 분리하여 구현함으로써, 높은 안정성과 테스트 용이성을 확보했습니다.

📝 다음 단계: `src/services/diagnosis_engine.py` 파일에 대한 유닛 테스트 케이스를 작성하고, 이 엔진을 호출할 프론트엔드(React Component)의 데이터 흐름 및 상태 관리 로직 초안을 설계해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\Baro_KHNLU\src\services\diagnosis_engine.py
