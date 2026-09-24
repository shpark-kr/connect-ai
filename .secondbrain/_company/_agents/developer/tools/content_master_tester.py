import json
from typing import Dict, List, Tuple

# --- Configuration Schema ---
# 필수 요소의 정의 (어떤 플랫폼에 어떤 것이 반드시 있어야 하는가)
REQUIRED_SCHEMA = {
    "blog": ["H1", "CTA_linkage", "Keywords_set"], # 블로그는 구조와 링크를 중시
    "youtube": ["Funnel_CTA_struct", "Hashtags_min20", "Strong_Hooking_Title"], # 유튜브는 시각적 요소가 중요
    "instagram": ["Question_type_CTA", "ShotList_detailed", "Hashtags_min20"] # 인스타는 몰입감과 직관성이 중요
}

def load_content_packages(file_path: str) -> Dict[str, List[Dict]]:
    """
    JSON 파일에서 모든 콘텐츠 패키지(버전별 3개)를 로드합니다.
    실제로는 파일을 읽어 파싱하는 단계입니다.
    """
    print(f"🔍 [INFO] Loading content packages from {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # 예시 데이터 구조를 가정하고 반환합니다. (실제로는 파일 파싱 로직이 필요함)
        return data.get("content_versions", [])[:3] # 상위 3개 버전만 사용한다고 가정
    except FileNotFoundError:
        print("[ERROR] Content package file not found.")
        return []
    except json.JSONDecodeError:
        print("[FATAL] Invalid JSON format in the content package.")
        return []

def validate_content(package: Dict[str, str], version_name: str) -> Tuple[bool, List[str]]:
    """
    단일 콘텐츠 패키지가 모든 필수 요건을 갖추었는지 검증합니다.
    Args:
        package (Dict): 플랫폼별 핵심 요소가 담긴 딕셔너리.
        version_name (str): 현재 버전 이름 (예: 'Blog Version A').
    Returns:
        Tuple[bool, List[str]]: 유효성 여부와 실패 이유 목록.
    """
    failures = []
    is_valid = True

    print(f"\n--- [Validation Start] {version_name} ---")

    # 1. 플랫폼별 필수 요소 검증 (Schema Check)
    for platform, required_elements in REQUIRED_SCHEMA.items():
        platform_data = package.get(platform, {})
        missing_elements = []
        
        for element in required_elements:
            if not platform_data.get(element) or str(platform_data[element]).strip() == "":
                missing_elements.append(f"'{element}' (필수 누락)")

        if missing_elements:
            failures.append(f"[🚨 {platform} 실패] 필수 요소 누락: {', '.join(missing_elements)}")
            is_valid = False
        else:
            print(f"[✅ {platform} 통과] 모든 핵심 요소가 발견되었습니다.")

    # 2. 전반적인 일관성 검증 (Coherence Check)
    if package.get("blog", "").count("국민연금") > 0 and package.get("youtube", "").count("국민연금") == 0:
         failures.append("[⚠️ 일관성 경고] '국민연금' 키워드가 블로그에는 있으나, 유튜브 설명란 초안에서 누락되었습니다. 내용 통일성을 확인하세요.")

    if not failures:
        print(f"✨ [SUCCESS] {version_name}는 모든 구조적 요건을 완벽하게 충족합니다.")

    return is_valid, failures


def main():
    """메인 실행 함수: 전체 콘텐츠 패키지 검증 오케스트레이션."""
    # 🚨 실제 테스트를 위해서는 유효한 JSON 파일 경로가 필요합니다.
    # 여기서는 임시 더미 파일을 사용한다고 가정하고 로직만 보여줍니다.
    DUMMY_INPUT_PATH = "dummy_content_package.json" 

    # 1. 콘텐츠 패키지 로드
    content_packages = load_content_packages(DUMMY_INPUT_PATH)

    if not content_packages:
        print("\n🛑 [FAILURE] 검증할 콘텐츠 패키지를 불러오지 못했습니다. 입력 데이터를 확인해주세요.")
        return False

    all_passed = True
    
    # 2. 각 버전별로 순차적 검증 수행
    for i, package in enumerate(content_packages):
        version_name = f"Version {i+1}"
        is_valid, failures = validate_content(package, version_name)
        
        if not is_valid:
            print("\n========================================================")
            print(f"❌ [CRITICAL FAILURE] {version_name}의 구조적 오류가 발견되었습니다.")
            for failure in failures:
                print(f"   - {failure}")
            print("========================================================\n")
            all_passed = False
        else:
             print("\n--------------------------------------------------------")

    if all_passed and content_packages:
        print("\n🎉 [SYSTEM CHECK] 모든 콘텐츠 패키지가 구조적 요건을 충족했습니다. 다음 단계로 진행할 수 있습니다.")
    else:
        print("\n🛑 [STOPPED] 하나 이상의 콘텐츠 패키지에서 치명적인 결함이 발견되었습니다. 수정 후 재실행하십시오.")

    return all_passed

if __name__ == "__main__":
    # 테스트를 위해 더미 JSON 파일 생성 (실제 사용 시 이 부분은 필요 없음)
    dummy_data = {
        "content_versions": [
            { # Version 1: Perfect Example (Passed)
                "blog": {"H1": "제목", "CTA_linkage": "링크A", "Keywords_set": "키워드"},
                "youtube": {"Funnel_CTA_struct": "구조B", "Hashtags_min20": "태그", "Strong_Hooking_Title": "후킹C"},
                "instagram": {"Question_type_CTA": "질문D", "ShotList_detailed": "샷리스트E", "Hashtags_min20": "태그"}
            },
            { # Version 2: Missing CTA (Failed)
                "blog": {"H1": "제목", "CTA_linkage": "", "Keywords_set": "키워드"}, # CTA 누락 가정
                "youtube": {"Funnel_CTA_struct": "구조B", "Hashtags_min20": "태그", "Strong_Hooking_Title": "후킹C"},
                "instagram": {"Question_type_CTA": "질문D", "ShotList_detailed": "샷리스트E", "Hashtags_min20": "태그"}
            },
            { # Version 3: Missing Hashtag (Failed)
                "blog": {"H1": "제목", "CTA_linkage": "링크A", "Keywords_set": "키워드"},
                "youtube": {"Funnel_CTA_struct": "구조B", "Hashtags_min20": "", "Strong_Hooking_Title": "후킹C"}, # 해시태그 누락 가정
                "instagram": {"Question_type_CTA": "질문D", "ShotList_detailed": "샷리스트E", "Hashtags_min20": "태그"}
            }
        ]
    }
    dummy_path = "c:\\Data\\Project\\connect-ai\\.secondbrain\\_company\\agents\\developer\\tools\\dummy_content_package.json"
    with open(dummy_path, 'w', encoding='utf-8') as f:
        json.dump(dummy_data, f)

    main()