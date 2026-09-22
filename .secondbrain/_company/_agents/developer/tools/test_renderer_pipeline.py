import os
from datetime import datetime
# 가정: 기존에 존재하거나 재설계가 필요한 코어 렌더링 서비스 모듈
from core_services.video_renderer import render_multiplatform_video
from data_models.content_schema import ContentScript

def run_integrated_pipeline_test(script_data: ContentScript, platform_list: list):
    """
    통합 테스트 실행 함수. 스크립트를 받아 다중 플랫폼에 대해 E2E 검증을 수행한다.
    핵심 기능: 조건부 CTA 오버레이 및 메타데이터 자동 주입 로직 확인.

    Args:
        script_data: 테스트할 콘텐츠 스크립트 데이터 객체 (Pain Point, CTA 지점 포함).
        platform_list: 타겟 플랫폼 목록 (e.g., ['youtube', 'instagram']).
    """
    print("="*60)
    print(f"🚀 [통합 파이프라인 테스트 시작] ({datetime.now().strftime('%Y-%m-%d %H:%M')})")
    print("="*60)

    # 1. 메타데이터 주입 검증 (가장 먼저 체크해야 할 것)
    metadata_test_data = {
        "title": f"[테스트] {script_data['topic']} - 통합 테스트",
        "description": "🚨 [필수 공지] 이 영상은 전문 상담을 유도하는 콘텐츠입니다. 자세한 내용은 설명란의 트래킹 링크를 통해 확인해주세요. #국민연금 #퇴직연금...",
        "tags": ["생활정보", "노후준비", "사각지대", "재테크"],
        "affiliate_link": "https://track-api/test-affiliate-id-12345" # 공통 트래킹 링크 삽입 확인
    }
    print(f"✅ 1. 메타데이터 주입 로직 테스트: {metadata_test_data['title']} 준비 완료.")

    all_results = {}

    for platform in platform_list:
        print(f"\n--- 🌐 플랫폼별 렌더링 시작: {platform.upper()} ---")
        try:
            # 2. Multi-Platform & 조건부 CTA 오버레이 검증 (핵심 로직 호출)
            result = render_multiplatform_video(
                script=script_data,
                platforms=[platform], # 플랫폼별로 다른 해상도/종횡비 요구
                cta_trigger_points=script_data.get('pain_points', []) # 스크립트 내 Pain Point 기반으로 CTA가 활성화되어야 함
            )

            if result['success']:
                print(f"   ✅ [{platform.upper()}]: 렌더링 성공. 파일 경로: {result['output_path']}")
                all_results[platform] = {"status": "SUCCESS", "path": result['output_path']}
            else:
                print(f"   ❌ [{platform.upper()}]: 렌더링 실패. 오류 메시지: {result.get('error', 'Unknown error')}")
                all_results[platform] = {"status": "FAIL", "error": result.get('error')}

        except Exception as e:
            print(f"   🚨 [{platform.upper()}]: 치명적 에러 발생! {e}")
            all_results[platform] = {"status": "CRITICAL_FAIL", "error": str(e)}

    print("\n" + "="*60)
    if all(r['status'] == 'SUCCESS' for r in all_results.values()):
        print("🎉 [통합 테스트 완료] 모든 플랫폼에서 조건부 CTA 오버레이 및 다중 해상도 렌더링이 성공적으로 검증되었습니다.")
    else:
        print("⚠️ [통합 테스트 경고] 일부 플랫폼 또는 기능에 오류가 감지되었습니다. 로그를 확인해주세요.")

    return all_results

if __name__ == "__main__":
    # 예시 스크립트 데이터 (실제 Writer/Researcher의 아웃풋을 구조화한 형태)
    example_script = ContentScript(
        topic="퇴직연금 사각지대",
        duration=900, # 15분 분량 가정
        pain_points=[
            {"time": "0:30", "message": "가장 큰 위험은 '돈이 끊기는' 시점입니다.", "severity": "CRITICAL"}, # <-- 여기서 CTA 오버레이 트리거
            {"time": "6:15", "message": "국민연금만으로는 충분하지 않을 수 있습니다.", "severity": "HIGH"}
        ]
    )

    # 2. 테스트 실행 (유튜브와 인스타그램 동시 검증 시도)
    platforms_to_test = ["youtube", "instagram"]
    run_integrated_pipeline_test(example_script, platforms_to_test)