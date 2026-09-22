from typing import List, Dict, Any, Tuple
# Step 1에서 만든 Validator 함수를 임포트합니다.
from gap_chart_validator import GapChartData

def generate_ffmpeg_render_commands(data: GapChartData) -> List[str]:
    """
    GapChartData 객체를 받아 FFmpeg가 처리할 수 있는 시간 기반의 렌더링 명령 리스트를 생성합니다.
    
    이 함수는 단순히 데이터를 전달하는 것이 아니라, 비디오 스트림에 시각적 이벤트를 삽입하는 '명령'을 만듭니다.
    
    Args:
        data: 유효성이 검증된 GapChartData 객체.
    Returns:
        FFmpeg 명령 문자열 리스트.
    """
    commands = []
    print(f"🛠️ [Renderer] '{data.title}' 기반의 FFmpeg 렌더링 명령어 생성 시작.")

    # 비디오에 삽입될 기본 텍스트 오버레이 (Chart Title)
    commands.append("add_text_overlay --source=chart_title")
    
    for i, point in enumerate(data.data_points):
        start = point.timestamp_sec
        end = point.timestamp_sec + 5 # 예시: 각 데이터 포인트는 5초 동안 표시된다고 가정
        
        # --- 핵심 로직: Gap Area Chart 시각화 명령 생성 ---
        # FFmpeg가 이해할 수 있는 가상의 파라미터 구조를 사용합니다.
        command = (
            f"add_gap_chart_area --start={start:.2f}s --duration={end - start:.2f}s "
            f"--data_range=[{point.start_value:.0f}, {point.end_value:.0f}] "
            f"--color_key=#{int(point.data_type.split('PENSION')[-1])}:FFCCAA:AA" # 데이터 타입별 고유 색상 코드 사용
        )
        commands.append(command)

    # 마지막에 Funnel CTA를 위한 텍스트/그래픽 삽입 명령을 추가합니다.
    commands.append("add_cta_overlay --text='자세한 내용은 설명란 확인' --duration=10s")
    
    print(f"✅ [Renderer] 총 {len(commands)}개의 렌더링 명령어 생성 완료.")
    return commands

def render_gap_data_to_video_spec(json_data: Dict[str, Any]) -> Tuple[bool, List[str], str | None]:
    """
    전체 파이프라인 함수: 검증 -> 데이터 객체화 -> 명령어 생성.
    """
    # 1. 유효성 검사 (Step 1 사용)
    is_valid, error = validate_gap_chart_data(json_data)
    if not is_valid:
        return False, [], f"데이터 유효성 검증 실패: {error}"

    # 2. 데이터 객체화 및 명령어 생성 (Step 2 사용)
    try:
        validated_data = GapChartData(**json_data)
        commands = generate_ffmpeg_render_commands(validated_data)
        return True, commands, None
    except Exception as e:
        return False, [], f"렌더링 명령어 생성 중 오류 발생: {e}"

if __name__ == '__main__':
    # 테스트 실행 (실제 데이터 필요)
    pass