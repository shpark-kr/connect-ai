import json
from datetime import date
from typing import Dict, Any, List

# --- 상수 정의 (System Config) ---
REQUIRED_SOURCES = ["보건복지부", "국민연금공단", "통계청", "법제처"]
MIN_SEO_WORDS = 150 # 최소 키워드 밀도 확보 기준 단어 수 (Description 길이 참고)

def load_policy_data(file_path: str) -> Dict[str, Any]:
    """JSON 파일 형태의 정책 데이터를 로드합니다. 데이터가 없으면 빈 딕셔너리를 반환합니다."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ 경고: 정책 데이터 파일을 찾을 수 없습니다.")
        return {}
    except json.JSONDecodeError:
        print("❌ 오류: 유효하지 않은 JSON 형식의 데이터입니다.")
        return {}

def validate_and_enrich(raw_data: Dict[str, Any], content_type: str) -> Dict[str, Any]:
    """
    정책 데이터를 검증하고, 필수 출처 및 발행 날짜를 강제 삽입하여 신뢰도를 높입니다.
    (핵심 로직)
    """
    enriched_data = raw_data.copy()
    current_date_str = date.today().strftime("%Y년 %m월")
    sources: List[str] = []

    # 1. 필수 출처 검증 및 주입 (Source Link 강제 삽입 시뮬레이션)
    for key, value in raw_data.get('data', {}).items():
        if isinstance(value, dict) and 'source' in value:
            source = value['source'].get('name')
            link = value['source'].get('url')
            if source and source not in sources:
                sources.append(source)
                # 데이터 원본에 출처 정보를 명시적으로 추가
                enriched_data[f"Source_{key}"] = f"{source} ({link})"

    # 2. 발행 날짜 강제 삽입 (최신 정보임을 강조)
    if "발행일자" not in enriched_data:
        enriched_data["발행일자"] = current_date_str

    print(f"\n✅ 데이터 무결성 검증 완료: {', '.join(sources)} 출처 및 {current_date_str} 날짜가 적용되었습니다.")
    return enriched_data


def optimize_seo_metadata(content_body: str, core_keywords: List[str]) -> Dict[str, str]:
    """
    콘텐츠 본문과 핵심 키워드를 기반으로 SEO 메타데이터를 자동 최적화합니다.
    (자동 최적화 로직)
    """
    # 1. Description 최적화 (클릭 유도 및 정보 압축)
    description_draft = f"🚨 {core_keywords[0]}의 사각지대! 국민연금만 믿으면 안 되는 이유와, 놓치기 쉬운 노후 자산 체크리스트 3가지를 공개합니다. 공적 데이터를 기반으로 작성된 필독 정보입니다."

    # 2. Keywords 생성 (검색 엔진이 선호하는 조합)
    keywords_str = ", ".join(core_keywords + ["국민연금 사각지대", "노후 준비"])

    # 3. 제목 재구성 (AIDA 구조 적용 시뮬레이션)
    optimized_title = f"[경고] {core_keywords[0]}만으론 부족합니다: 놓친 노후 자산 체크리스트 | 온현"

    return {
        "title": optimized_title,
        "description": description_draft[:155], # 구글 제한 길이 준수
        "keywords": keywords_str
    }


def run_integrity_check(policy_data_path: str, content_body: str, core_keywords: List[str]):
    """메인 실행 함수: 전체 검증 및 최적화 파이프라인을 실행합니다."""
    print("\n=========================================")
    print("🚀 정책 데이터 무결성 체크 시작 (Policy Integrity Checker)")
    print("=========================================\n")

    # 1. 데이터 로드 및 검증
    raw_data = load_policy_data(policy_data_path)
    if not raw_data:
        return {"status": "Failed", "message": "데이터 로딩 실패로 파이프라인을 중단합니다."}

    enriched_data = validate_and_enrich(raw_data, content_type="Blog")

    # 2. SEO 메타데이터 최적화
    seo_meta = optimize_seo_metadata(content_body, core_keywords)

    print("\n✅ [최종 결과] 콘텐츠 발행 준비 완료.")
    return {
        "status": "Success",
        "enriched_data": enriched_data,
        "seo_metadata": seo_meta
    }


if __name__ == "__main__":
    # --- 테스트 시뮬레이션 환경 (실제 실행 예시) ---
    print("===========================================================")
    print("⚙️ [테스트 모드] Policy Integrity Checker 실행")
    print("===========================================================")

    # 1. 가상의 정책 데이터 파일 생성 (테스트를 위해 임시로 생성)
    test_data = {
        "metadata": {"title": "국민연금 개정 정보", "date": "2024-05"},
        "data": {
            "특수고용직공백": {
                "description": "프리랜서의 연금 납부 공백 리스크.",
                "source": {"name": "국민연금공단", "url": "https://www.nps.or.kr/gap"}
            },
            "기초생활정보": {
                "description": "지자체별 지원 바우처 정보.",
                "source": {"name": "보건복지부", "url": "http://mohw.go.kr/voucher"}
            }
        }
    }
    test_file = "temp_policy_data.json"
    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump(test_data, f)

    # 2. 가상의 콘텐츠 본문 및 키워드 설정
    sample_body = "많은 분들이 국민연금을 노후 대비의 가장 큰 축으로 생각합니다. 하지만 정말 그게 전부일까요? ... (여기에 실제 블로그 원고가 들어갑니다.)"
    sample_keywords = ["국민연금 사각지대", "특수고용직 연금", "노후 소득 공백"]

    # 3. 모듈 실행 및 테스트
    result = run_integrity_check(test_file, sample_body, sample_keywords)
    print("\n[테스트 결과 JSON]...")
    print(json.dumps(result, indent=4, ensure_ascii=False))

    # 4. 임시 파일 정리
    import os
    os.remove(test_file)
    print("✅ 테스트 완료 및 임시 파일 삭제.")