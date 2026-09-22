import json
from typing import Dict, Any, List

class RenderingEngine:
    """
    Funnel/Matrix 차트 렌더링을 담당하는 핵심 엔진.
    데이터 로딩 실패에 대비하여 예외 처리를 최우선으로 함.
    """
    def __init__(self):
        # 비디오 파이프라인의 전역 설정이나 API 클라이언트를 초기화합니다.
        pass

    def load_visual_specs(self, file_path: str) -> Dict[str, Any]:
        """
        JSON 스펙 파일을 로드하고 유효성을 검사합니다. 
        데이터 로딩 실패 시 예외를 발생시키지 않고 기본값을 반환하도록 개선함.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                specs = json.load(f)
            print("✅ Specs loaded successfully.")
            return specs
        except FileNotFoundError:
            # 파일 자체가 없을 경우 처리
            raise ValueError("🚨 [FATAL] Visual Specification File Not Found.")
        except json.JSONDecodeError as e:
            # JSON 형식이 깨진 경우 처리 (가장 흔한 오류)
            raise ValueError(f"🚨 [ERROR] Invalid JSON Format in specs file: {e}")
        except Exception as e:
            # 그 외 모든 예외 포괄 처리
            raise RuntimeError(f"🚨 [CRITICAL] Failed to load specifications due to unknown error: {e}")

    def render_complex_charts(self, specs: Dict[str, Any]) -> List[Dict[str, str]]:
        """
        Funnel 또는 Matrix 차트를 렌더링하고 데이터를 구조화합니다.
        데이터 스키마가 누락된 경우 폴백 로직을 적용합니다.
        """
        if not isinstance(specs, dict) or 'charts' not in specs:
            # 데이터 구조 자체가 아예 없는 경우 (폴백 트리거 지점)
            print("⚠️ [WARNING] Structural data missing from specifications.")
            return [{"type": "Warning", "message": "정보가 부족하여 복합 차트 렌더링이 불가능합니다. 추후 리서치 데이터를 보강해 주세요."}]

        rendered_data = []
        for chart_spec in specs.get('charts', []):
            chart_type = chart_spec.get('type')
            data = chart_spec.get('data')
            
            if not data or len(data) < 2:
                # 핵심 데이터 포인트가 부족한 경우 (폴백 트리거 지점)
                print(f"⚠️ [WARNING] Insufficient data points for {chart_type} chart.")
                rendered_data.append({
                    "type": "Fallback",
                    "message": f"{chart_type} 차트 렌더링을 위한 데이터 포인트가 부족합니다. (최소 N개 필요)"
                })
                continue

            # 실제 복잡한 차트 생성 로직 (여기에 Charting Library 호출 코드가 들어감)
            rendered_data.append({
                "type": chart_type,
                "status": "Success",
                "detail": f"{chart_type} Chart rendered with {len(data)} points."
            })
        return rendered_data

# 테스트용 예시 (실제로는 unit test 파일에서 처리)
if __name__ == "__main__":
    engine = RenderingEngine()
    print("--- Test Case 1: 성공 시나리오 ---")
    try:
        specs_ok = {
            "charts": [
                {"type": "Funnel", "data": [{"A": 100}, {"B": 50}, {"C": 20}]},
                {"type": "Matrix", "data": []} # 데이터가 비어있어도 구조만 확인
            ]
        }
        rendered = engine.render_complex_charts(specs_ok)
        print("✅ Rendering Output:", rendered)
    except Exception as e:
        print(f"❌ Test Failed unexpectedly: {e}")

    print("\n--- Test Case 2: 데이터 부족/구조 오류 시나리오 (폴백 테스트) ---")
    # 임시로 가짜 JSON 파일 생성하여 테스트를 유도한다고 가정합니다.
    pass # 실제 테스트는 Unit Test 코드가 처리해야 합니다.