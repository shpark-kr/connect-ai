import pytest
from datetime import timedelta, datetime
import json
from typing import Dict, Any, List

# --- MOCKING: 실제 데이터 로딩 및 유효성 검사 함수를 가정합니다. ---
def load_visual_specs(file_path: str) -> Dict[str, Any]:
    """실제 JSON 파일을 불러오는 모의(Mock) 함수입니다."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate_dataset_id(data_id: str) -> bool:
    """데이터셋 ID가 실제 데이터베이스에 존재하는지 검증하는 모의 함수."""
    # 실제 환경에서는 DB/API 호출을 통해 체크합니다. 여기서는 간단한 로직으로 대체합니다.
    return "DATASET_" in data_id and len(data_id) > 10

def parse_timecode(time_range: str) -> tuple[datetime, datetime]:
    """'MM:SS' 형태의 시간 문자열을 datetime 객체로 파싱하는 모의 함수."""
    # '00:05' 같은 형식을 처리합니다. 실제로는 더 복잡한 로직이 필요합니다.
    h, m, s = 0, int(time_range[:2]), int(time_range[3:])
    start = datetime(2000, 1, 1) + timedelta(minutes=m, seconds=s)
    return start, start + timedelta(seconds=1) # 임시로 1초 증가시켜 유효성 확보

# --- Core Validation Logic (테스트 대상 함수) ---
def validate_video_spec(specs: Dict[str, Any], source_file_path: str = "C:\\Data\\Project\\connect-ai\\결과물\\visual_specs_v1.0.json") -> List[str]:
    """
    비디오 스펙 JSON 전체 구조의 유효성을 검증하고 오류 리스트를 반환합니다.
    -> 이 함수가 테스트 대상입니다.
    """
    errors = []
    try:
        specs = load_visual_specs(source_file_path)
    except FileNotFoundError:
        return ["Critical Error: Source specification file not found."]

    if 'scenes' not in specs or not isinstance(specs['scenes'], list):
        errors.append("Schema Error: 'scenes' array is missing or malformed.")
        return errors

    # 1. 전체 스펙 검증 및 Global Specs 체크
    global_specs = specs.get('global_specs', {})
    if not global_specs.get('fallback_strategy'):
         errors.append("Warning: Fallback strategy is missing in global specs.")


    for i, scene in enumerate(specs['scenes']):
        scene_id = scene.get('scene_id', f'Unknown Scene {i}')
        time_range_list = scene.get('elements', [])

        # 2. 시간대 불일치 검증 (Time Discrepancy Check)
        if not time_range_list:
            errors.append(f"[{scene_id}] Error: Scene has no video elements defined.")
            continue

        sorted_times = []
        last_end_time = None # 이전 요소의 끝 시간을 추적 (순차성 검증용)

        for element in time_range_list:
            time_range = element.get('timecode_range')
            if not time_range or len(time_range) < 5:
                errors.append(f"[{scene_id}] Time Error: Malformed 'timecode_range' detected in an element.")
                continue

            try:
                start, end = parse_timecode(time_range)
            except Exception as e:
                 errors.append(f"[{scene_id}] Time Error: Failed to parse time range '{time_range}'. {e}")
                 continue


            # [핵심 로직 1] 시간 순차성 및 누락 검증 (만약 여러 장면이 연결된다면)
            if last_end_time and start < last_end_time - timedelta(seconds=2): # 2초 이내 오버랩은 허용할지 판단 가능
                errors.append(f"[{scene_id}] Time Error: Overlap or sequence break detected. Start time {start} is too close to previous end time.")

            # [핵심 로직 2] 유효한 시간 순서인지 검증 (시작 < 끝)
            if start >= end:
                 errors.append(f"[{scene_id}] Time Error: Invalid time range detected. Start ({start}) must be before End ({end}).")

            # [핵심 로직 3] 데이터셋 ID 누락 및 유효성 검증 (Dataset ID Check)
            data_id = element.get('data_id')
            if not data_id:
                errors.append(f"[{scene_id}] Data Error: 'Data Set ID' is missing for an element.")
            elif not validate_dataset_id(data_id):
                errors.append(f"[{scene_id}] Data Error: Invalid or unmapped dataset ID found: '{data_id}'.")

            last_end_time = end # 현재 요소의 끝 시간을 다음 검사에 사용
    return errors


# --- Pytest Test Cases ---
def test_01_valid_spec_load():
    """유효한 스펙 파일 로드 및 기본 구조 테스트."""
    # 실제 유효한 JSON 파일을 사용한다고 가정하고 실행
    specs = load_visual_specs("C:\\Data\\Project\\connect-ai\\결과물\\visual_specs_v1.0.json")
    assert isinstance(specs, dict)
    assert 'scenes' in specs

def test_02_missing_dataset_id():
    """[예외 케이스] 데이터셋 ID 누락 시 오류 감지 테스트."""
    # Mocking: 의도적으로 data_id가 없는 스펙을 만들었다고 가정
    mock_specs = {
        "version": "1.0", "scenes": [{
            "scene_id": 99,
            "elements": [
                {"element_type": "Text", "timecode_range": ["00:05", "00:10"], "data_id": "DATASET_A"},
                # 의도적으로 data_id 제거
                {"element_type": "Chart", "timecode_range": ["00:10", "00:20"]} 
            ]
        }]
    }
    errors = validate_video_spec(mock_specs)
    assert any("Data Error: 'Data Set ID' is missing" in err for err in errors)

def test_03_timecode_discrepancy():
    """[예외 케이스] 시간대 불일치 (순서 오류, 시작>종료) 감지 테스트."""
    # Mocking: 의도적으로 시간이 꼬인 스펙을 만들었다고 가정
    mock_specs = {
        "version": "1.0", "scenes": [{
            "scene_id": 98,
            "elements": [
                {"element_type": "Text", "timecode_range": ["00:05", "00:15"], "data_id": "DATASET_A"}, # 정상
                # 의도적으로 종료 시간이 시작 시간보다 빠른 경우 (Start > End)
                {"element_type": "Chart", "timecode_range": ["00:25", "00:20"], "data_id": "DATASET_B"}, 
            ]
        }]
    }
    errors = validate_video_spec(mock_specs)
    assert any("Start (.*?) must be before End (.*?)" in err for err in errors)

def test_04_unmapped_dataset_id():
    """[예외 케이스] 데이터셋 ID가 시스템에 등록되지 않은 경우 감지 테스트."""
    # Mocking: 존재하지 않는 fake한 data_id를 포함시킨 스펙을 만들었다고 가정
    mock_specs = {
        "version": "1.0", "scenes": [{
            "scene_id": 97,
            "elements": [
                {"element_type": "Text", "timecode_range": ["00:05", "00:15"], "data_id": "DATASET_VALID"},
                # 시스템이 알지 못하는 fake ID 사용
                {"element_type": "Chart", "timecode_range": ["00:15", "00:25"], "data_id": "FAKE_ID_XYZ"} 
            ]
        }]
    }
    errors = validate_video_spec(mock_specs)
    assert any("Invalid or unmapped dataset ID found" in err for err in errors)

# --- End of Tests ---