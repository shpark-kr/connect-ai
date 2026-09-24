import subprocess
import os
import time
from typing import Optional, Tuple

# --- Utility Components ---
class PipelineError(Exception):
    """파이프라인 전반의 오류를 처리하기 위한 커스텀 예외."""
    pass

class CircuitBreaker:
    """외부 시스템 호출 실패 시 회로 차단 및 복구 로직을 구현합니다."""
    def __init__(self, failure_threshold=3, recovery_timeout=60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN
        self.failure_count = 0
        self.last_failure_time = None

    def __call__(self, func):
        """데코레이터 형태로 사용됩니다."""
        async def wrapper(*args, **kwargs):
            if self.state == "OPEN":
                # 회로가 열리면 즉시 실패 처리하고 재시도 횟수를 줄임
                raise PipelineError("Circuit Breaker Open: 외부 API/시스템 과부하 상태입니다.")

            try:
                result = await func(*args, **kwargs)
                self.success() # 성공 시 카운트 리셋
                return result
            except Exception as e:
                print(f"[⚠️ CB Triggered] 실패 감지: {e}")
                self.failure_count += 1
                if self.failure_count >= self.failure_threshold:
                    self.state = "OPEN"
                    self.last_failure_time = time.time()
                    raise PipelineError(f"Circuit Open! 임계치 초과. {self.recovery_timeout}초 후 재시도 필요.")
                # 실패 시 상태 변경 없이 다시 발생하도록 함 (Retry 로직에서 처리)
                raise e

        return wrapper

    def success(self):
        if self.state != "CLOSED":
            print("[✅ CB Reset] 성공적으로 복구됨. 회로를 CLOSED 상태로 전환합니다.")
            self.state = "CLOSED"
            self.failure_count = 0

    def attempt_half_open(self) -> bool:
        """HALF-OPEN 상태에서만 시도 가능."""
        if self.state == "OPEN":
            time_passed = time.time() - self.last_failure_time
            if time_passed > self.recovery_timeout:
                print("[🔄 CB Transition] 시간 초과 감지. HALF-OPEN 상태로 전환하여 테스트를 시도합니다.")
                self.state = "HALF-OPEN"
                return True
            else:
                raise PipelineError(f"Circuit Open. 재시도까지 {int(self.recovery_timeout - time_passed)}초 남음.")
        return False

# --- Core Renderer Class ---
class VideoRendererCore:
    """
    숏폼 콘텐츠 렌더링 및 멀티 플랫폼 업로드 파이프라인의 핵심 로직을 담당합니다.
    Circuit Breaker 패턴과 재시도(Retry) 전략이 내장되어 있습니다.
    """
    def __init__(self, output_dir: str = "temp/renders"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    @CircuitBreaker() # 렌더링 핵심 로직에 CB 적용
    async def render_video_from_script(self, script_path: str, target_duration: float, aspect_ratio: str = "9:16") -> Optional[str]:
        """
        스크립트와 디자인 에셋을 기반으로 FFmpeg를 이용해 비디오 클립을 렌더링합니다.

        Args:
            script_path: 원본 스크립트 파일 경로 (텍스트/마크다운).
            target_duration: 목표 영상 길이 (초).
            aspect_ratio: 출력 비율 (예: "9:16", "1:1").

        Returns:
            렌더링된 임시 비디오 파일의 절대 경로.
        """
        print(f"\n--- [▶️ 렌더링 시작] 스크립트 기반 영상 생성 ({aspect_ratio}, {target_duration}s) ---")
        try:
            # 1. FFmpeg 명령어 구성 (매우 단순화된 예시, 실제는 복잡함)
            # -i script.mp4 : 입력 파일
            # -vf "drawtext=..." : 자막 및 오버레이 로직
            # -filter_complex : BGM + 영상 합치기 등 복합 필터 적용
            ffmpeg_command = [
                "ffmpeg", "-y", 
                "-i", "temp/input_base.mp4",  # 가정된 기본 영상 입력
                "-vf", f"drawtext=fontfile=/path/to/pretendard.ttf:text='자동 생성 자막':fontsize=32:color=yellow:(t-1)*0.05,box=1:r:1:c:s@b(t*0.05):enable='between(t,0,{}?)'.format(target_duration)",
                "-af", "aresample=48000:all=1" # 오디오 리샘플링 (LUFS 최적화 전 단계)
            ]

            # 2. FFmpeg 실행 및 에러 체크 (실제로는 subprocess.Popen 사용 권장)
            print("   -> [Simulating] FFmpeg 명령 실행... (자막, BGM 합성 로직 호출)")
            # 실제 환경에서는 아래와 같이 run_command를 통해 호출합니다:
            # result = await asyncio.to_thread(subprocess.run, ffmpeg_command, capture_output=True)

            if "ERROR" in str(ffmpeg_command): # 시뮬레이션 실패 로직
                 raise subprocess.CalledProcessError(1, f"FFmpeg 실행 중 예상 오류 발생: {random_string}")
            
            # 성공 시 가짜 파일 생성 (실제는 ffmpeg가 파일을 만듦)
            output_file = os.path.join(self.output_dir, "temp_rendered_" + str(int(time.time())) + ".mp4")
            with open(output_file, 'w') as f:
                f.write("Simulated MP4 Content (15-30s)") # 파일 내용이 아님을 명시
            
            print(f"   ✅ 렌더링 성공. 임시 파일 경로: {output_file}")
            return output_file

        except subprocess.CalledProcessError as e:
            # FFmpeg 자체의 구체적 오류 처리 (예: 코덱 문제, 인풋파일 없음)
            print(f"   ❌ [FFmpeg Failure] 렌더링 실패. 에러 코드 {e.returncode}. 메시지: {e.stderr}")
            raise PipelineError("FFmpeg 실행 단계에서 치명적인 미디어 처리 오류가 발생했습니다.")

    @CircuitBreaker() # API 호출에 CB 적용
    async def upload_to_platform(self, video_path: str, platform: str) -> bool:
        """
        렌더링된 영상을 지정된 플랫폼(YouTube, Insta 등)에 업로드합니다.
        이 부분은 실제 외부 API 클라이언트와 연동되어야 합니다.
        """
        print(f"\n--- [📤 업로드 시도] {platform} 플랫폼으로 영상 전송 시작 ---")
        try:
            # 1. API 인증 및 초기화 (실제로는 config에서 로드)
            api_key = "SECRET_API_KEY" 
            if not api_key: raise Exception("API 키 누락.")

            # 2. 전송 과정 시뮬레이션
            print(f"   -> [Simulating] {platform} API 호출 중... (파일 크기, 메타데이터 동시 전송)")
            await asyncio.sleep(0.5) # 비동기 대기 시간 가정

            # 임의로 실패 로직 추가: 5회 중 2번은 실패한다고 가정
            if time.time() % 10 > 6 and platform == "YouTube":
                 raise Exception("HTTP 503 Service Unavailable - Rate Limiting.")
                
            print(f"   ✅ 업로드 성공! {platform}에 콘텐츠가 발행되었습니다.")
            return True

        except Exception as e:
            # API 통신 오류, 인증 만료 등 외부 장애 처리
            raise PipelineError(f"{platform} 업로드 실패. 원인: {e}")


# --- Test Runner (실행 로직) ---
async def main_pipeline_test():
    """최종 테스트베드 실행 함수."""
    renderer = VideoRendererCore()
    video_path = None

    try:
        # 1. 렌더링 시도 (Circuit Breaker가 실패를 감지할 수 있도록 여러 번 호출)
        print("\n=========================================")
        print("== [TEST RUN] 비디오 렌더링 파이프라인 테스트 시작 ==")
        print("=========================================")
        video_path = await renderer.render_video_from_script(
            script_path="scripts/gap_funnel_v1.md", 
            target_duration=25.0, 
            aspect_ratio="9:16"
        )

        # 2. 업로드 시도 (최대 3번 재시도 로직 구현 필요 - 여기서는 CB가 담당)
        print("\n=========================================")
        print("== [TEST RUN] 멀티 플랫폼 업로드 테스트 시작 ==")
        
        await renderer.upload_to_platform(video_path, "YouTube") # 1차 시도
        # 재시도가 필요하다면 여기에 반복문과 지연시간을 추가해야 함
        await renderer.upload_to_platform(video_path, "Instagram Reels") # 2차 시도

    except PipelineError as e:
        print(f"\n🚨 [최종 파이프라인 실패] {e}")
    finally:
        # 정리 작업 (Cleanup)
        if video_path and os.path.exists(video_path):
            os.remove(video_path)
            print("\n[🧹 Cleanup] 임시 렌더링 파일 삭제 완료.")

# Python의 비동기 기능을 사용하기 위해 asyncio를 import 해야 함.
import asyncio
asyncio.run(main_pipeline_test())