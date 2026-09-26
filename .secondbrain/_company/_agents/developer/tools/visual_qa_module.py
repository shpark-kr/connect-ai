import os
import re
from typing import Tuple, Dict, List

# --- 1. 유틸리티 함수: 색상 및 대비 계산 (WCAG AA 기준) ---
def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """HEX 코드를 RGB 튜플로 변환합니다."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def calculate_luminance(rgb: Tuple[int, int, int]) -> float:
    """RGB 값을 이용해 휘도(Luminance)를 계산합니다. (ITU-R BT.709 표준 기반 근사치)"""
    r, g, b = [c / 255 for c in rgb]
    return 0.2126 * r + 0.7128 * g + 0.0722 * b

def calculate_contrast_ratio(hex1: str, hex2: str) -> float:
    """두 HEX 색상의 대비 비율을 계산합니다. (최소 4.5:1 필요)"""
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)

    l1 = calculate_luminance(rgb1)
    l2 = calculate_luminance(rgb2)

    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)

# --- 2. 테스트 로직: 시각적 무결성 검증 엔진 ---
def test_visual_integrity(asset_spec: Dict[str, str], target_platform: str) -> List[Dict]:
    """
    주어진 에셋 사양과 타겟 플랫폼을 기반으로 QA를 수행합니다.
    Returns a list of failure dictionaries.
    """
    failures = []
    print(f"\n--- [QA 시작] {target_platform} 환경에서 시각적 무결성 테스트 진행 ---")

    # 1. 색상 대비 검사 (Contrast Check)
    if 'main_bg' in asset_spec and 'text_primary' in asset_spec:
        ratio = calculate_contrast_ratio(asset_spec['main_bg'], asset_spec['text_primary'])
        MIN_CONTRAST = 4.5 # WCAG AA 기준
        if ratio < MIN_CONTRAST:
            failures.append({
                "module": "Contrast",
                "severity": "CRITICAL",
                "message": f"색상 대비 부족 (BG:{asset_spec['main_bg']} vs Text:{asset_spec['text_primary']}). 비율 {ratio:.2f}:1. 최소 요구치: 4.5:1.",
                "error_code": "VIS-001"
            })

    # 2. 플랫폼별 레이아웃 및 종횡비 검사 (Aspect Ratio & Layout)
    if target_platform == "Shorts/Reels" and asset_spec.get("ratio") != "9:16":
        failures.append({
            "module": "Layout",
            "severity": "HIGH",
            "message": f"타겟 플랫폼 ({target_platform})에 맞는 비율(9:16)이 아닙니다. 강제 크롭/왜곡 위험.",
            "error_code": "VIS-002"
        })
    elif target_platform == "YouTube Longform" and asset_spec.get("ratio") != "16:9":
         failures.append({
            "module": "Layout",
            "severity": "HIGH",
            "message": f"타겟 플랫폼 ({target_platform})에 맞는 비율(16:9)이 아닙니다. 화면 여백 낭비 위험.",
            "error_code": "VIS-003"
        })

    # 3. 정보 손실 경고 (Information Loss Check - Gap Warning Module Specific)
    if 'CTA' in asset_spec and target_platform == "Shorts/Reels":
        # Shorts는 CTA를 화면 하단이나 상단에 배치해야 함을 가정
        if not re.search(r"하단", asset_spec.get("cta_placement", "")):
             failures.append({
                "module": "Content Flow",
                "severity": "MEDIUM",
                "message": "Shorts/Reels의 CTA는 시청자가 스크롤하는 영역을 침범하지 않도록 하단 또는 상단에 명확히 배치해야 합니다.",
                "error_code": "VIS-004"
            })

    return failures

# --- 3. 메인 실행 함수 (QA Orchestrator) ---
def run_visual_qa(asset_spec: Dict[str, str]):
    """모든 주요 플랫폼에 대해 시각적 QA를 수행합니다."""
    all_failures = []

    print("=====================================================")
    print("🚀 Visual Integrity QA Module 실행 시작")
    print("=====================================================")

    # 테스트 1: Shorts/Reels (9:16)
    shorts_fails = test_visual_integrity(asset_spec, "Shorts/Reels")
    all_failures.extend(shorts_fails)

    # 테스트 2: YouTube Longform (16:9)
    longform_fails = test_visual_integrity(asset_spec, "YouTube Longform")
    all_failures.extend(longform_fails)

    print("\n=====================================================")
    if not all_failures:
        print("✅ QA 테스트 통과: 모든 주요 시각적 무결성 체크를 완료했습니다.")
        return True
    else:
        print(f"❌ QA 테스트 실패! 총 {len(all_failures)}개의 경고 및 오류가 발견되었습니다.")
        for failure in all_failures:
            print(f"\n[!!! CRITICAL ERROR !!!] 코드: {failure['error_code']}")
            print(f"  Module: {failure['module']} | Severity: {failure['severity']}")
            print(f"  Description: {failure['message']}")
        return False

if __name__ == "__main__":
    # 실제 에셋 사양을 로드하는 시뮬레이션 데이터 구조 (Designer가 정의한 Spec 참조)
    sample_asset_spec = {
        "ratio": "9:16", # 현재 테스트할 비율로 임시 설정
        "main_bg": "#1A2340", # Dark Navy
        "text_primary": "#FFD700", # Gold (Warning Color)
        "cta_placement": "하단 1/4 지점, 고대비 노란색 배경."
    }

    # 실행 및 결과 반환
    run_visual_qa(sample_asset_spec)