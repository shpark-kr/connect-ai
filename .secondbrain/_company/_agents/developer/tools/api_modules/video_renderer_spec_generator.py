# api_modules/video_renderer_spec_generator.py

import json
from typing import Dict, List, Any, Tuple

def validate_lcc_data(raw_json_data: str) -> Tuple[Dict[str, Any] | None, List[str]]:
    """
    JSON 문자열로 받은 LCC 데이터를 파싱하고, 재정적 유효성을 검증합니다.
    실제 API 게이트웨이의 첫 번째 방어선 역할을 수행합니다.
    :param raw_json_data: JSON 형식의 원본 데이터 (문자열).
    :return: 딕셔너리 형태의 검증된 스펙 또는 None, 오류 메시지 리스트.
    """
    errors = []
    parsed_data: Dict[str, Any] = {}

    # 1. JSON 파싱 단계 검증 (Parsing Failure)
    try:
        raw_data = json.loads(raw_json_data)
    except json.JSONDecodeError as e:
        errors.append(f"❌ JSON Parsing Error: 입력 데이터가 유효한 JSON 형식이 아닙니다. ({e})")
        return None, errors

    parsed_data = raw_data

    # 2. 구조적 검증 (Schema Validation)
    if not isinstance(raw_data, dict):
        errors.append("❌ 데이터는 최상위 레벨에서 객체여야 합니다.")
        return None, errors

    chart_id = raw_data.get('chartId', 'unknown')
    title = raw_data.get('title', {})
    data_sets = raw_data.get('dataSets', [])

    if not title or not isinstance(title, dict) or not title.get('primary'):
        errors.append("❌ 제목 정보 (Title.Primary)가 누락되었습니다.")
    if not isinstance(data_sets, list):
         errors.append("❌ dataSets는 리스트여야 합니다.")

    # 3. 데이터 포인트 검증 (Core Business Logic Validation)
    validated_datasets = []
    for i, dataset in enumerate(data_sets):
        dataset_errors = []
        if not isinstance(dataset, dict) or 'id' not in dataset:
            dataset_errors.append("데이터셋 객체 자체가 유효하지 않습니다.")
            continue

        valid_points = []
        for point in dataset.get('dataPoints', []):
            # Year 검증 (정수, 양수)
            if not isinstance(point, dict) or 'year' not in point:
                dataset_errors.append("데이터 포인트가 유효하지 않습니다.")
                continue

            try:
                year = int(float(point['year'])) # float -> int 변환을 통해 정밀도를 확보
                if year < 1950: # 의미있는 과거 시점 제한
                    raise ValueError("너무 오래된 연도입니다.")
                
                # Value 검증 (숫자)
                value = float(point.get('value'))
                if value is None or (isinstance(point.get('value'), str) and not point['value'].strip()):
                     raise ValueError("값이 비어있습니다.")

                valid_points.append({"year": year, "value": value})
            except (ValueError, TypeError):
                dataset_errors.append(f"유효하지 않은 데이터 포인트 값: Year={point.get('year')}, Value={point.get('value')}")


        if dataset_errors:
             errors.extend([f"[Dataset {i} ({dataset['id']})]: {e}" for e in dataset_errors])

        validated_datasets.append({
            "id": dataset["id"], 
            "label": dataset["label"], 
            "colorCode": dataset["colorCode"], 
            "dataPoints": valid_points
        })


    if errors:
        return None, errors

    # 최종 성공 스펙 구조 생성
    final_spec = {
        "chartId": chart_id,
        "metadata": {"source": "LCC-V2.0", "timestamp": "..." }, # 실제로는 타임스탬프 삽입
        "title": title,
        "dataSets": validated_datasets
    }

    return final_spec, []


def generate_ffmpeg_commands(final_spec: Dict[str, Any]) -> List[str]:
    """
    검증된 최종 스펙을 기반으로 FFmpeg 렌더링 파이프라인에 필요한 명령 목록을 생성합니다.
    이 함수는 순수하게 로직만 담당하며, 실제 비디오 코드를 건드리지 않습니다.
    """
    print("\n--- 📽️ [FFmpeg 렌더링 스펙 자동 생성 성공] ---")
    commands = []
    
    # 예시: 각 데이터셋별로 그래프 영역을 정의하고 오버레이를 계산하는 로직이 필요함.
    for ds in final_spec['dataSets']:
        print(f"✅ DataSet '{ds['id']}' ({ds['label']}) 분석 완료.")
        commands.append(
            f"ffmpeg -i input_{ds['id']}.mp4 -vf \"drawbox=y:={ds['colorCode']}:h=10:x=200:y=50:w=800\" output_spec_{ds['id']}.png"
        )

    # 최종 합성 명령 예시 (Mock Command)
    final_command = "ffmpeg -i input.mp4 -filter_complex [v][s1][s2]overlay=... output_final.mp4"
    commands.append(f"\n[FINAL COMPOSITE]: {final_command}")

    return commands

# --- 테스트 코드 (필수) ---
if __name__ == '__main__':
    print("=============================================")
    print("           LCC API Validator 테스트 시작")
    print("=============================================\n")

    # 1. 정상 데이터 케이스
    good_json = """
    {
      "chartId": "test-success-001",
      "title": {
        "primary": "재정적 손실 격차 분석 (Success)",
        "secondary": "전문가 진단으로 달성 가능한 수익"
      },
      "dataSets": [
        {
          "id": "baseline_risk",
          "label": "현상 유지 시 예상되는 손실액 (Before)",
          "colorCode": "#A31D2C",
          "dataPoints": [{"year": 2024, "value": 5000, "unit": "만원"}, {"year": 2025, "value": 6200, "unit": "만원"}]
        }
      ]
    }
    """
    spec, errors = validate_lcc_data(good_json)
    print("--- [Test Case 1: SUCCESS] ---")
    if spec:
        print("✅ 성공적으로 검증된 스펙을 얻었습니다.")
        commands = generate_ffmpeg_commands(spec)
        for cmd in commands:
            print(cmd)

    # 2. 오류 데이터 케이스 (Year/Value 타입 불일치, 누락 등)
    bad_json = """
    {
      "chartId": "test-fail-002",
      "title": {
        "primary": "재정적 손실 격차 분석 (Failure)",
        "secondary": ""
      },
      "dataSets": [
        {
          "id": "risk_bad",
          "label": "불량 데이터 테스트",
          "colorCode": "#A31D2C",
          "dataPoints": [
            {"year": 2024, "value": 5000},           // Unit 누락 (허용)
            {"year": 2026, "value": "invalid_text"}, // 값 타입 오류 -> 실패 지점
            {"year": 1899, "value": 100}             // 연도 범위 오류 -> 실패 지점
          ]
        },
        {
          "id": "empty_data",
          "label": "빈 데이터셋",
          "colorCode": "#B8860B",
          "dataPoints": [] // 포인트 없음
        }
      ]
    }
    """
    spec, errors = validate_lcc_data(bad_json)
    print("\n--- [Test Case 2: FAILURE] ---")
    if not spec and errors:
        print("❌ 예상대로 오류가 발생했습니다. 발견된 오류 목록:")
        for error in errors:
            print(f"  - {error}")