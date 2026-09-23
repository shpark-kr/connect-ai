import os
from datetime import date
from typing import Dict, List

# --- [설정 및 상수] ---
TARGET_DIR = r"C:\Data\Project\connect-ai\결과물\01_블로그_콘텐츠"
CURRENT_DATE_STR = date.today().strftime("%Y-%m-%d") # 오늘 날짜로 고정
HEADER_HTML = """
<div class="blog-header">
    <h1 data-role="main-title">[긴급 경고] {topic_title}</h1>
    <p class="author-info">작성: 온현 에이전트 | 업데이트: {}</p>
</div>
"""

def generate_html_content(
    topic_title: str, 
    raw_writer_html: str, 
    design_assets: Dict[str, str], 
    data_points: List[str]
) -> str:
    """
    주제별 콘텐츠를 조합하여 최종 HTML 본문을 생성하는 핵심 함수.
    (실제로는 이 부분에 복잡한 파싱 및 스타일링 로직이 들어갑니다.)
    """
    # 1. 헤더와 메타 정보를 조합합니다.
    header = HEADER_HTML.format(topic_title=topic_title, date_str=CURRENT_DATE_STR)

    # 2. 본문 내용을 받습니다 (Writer의 원고를 사용).
    body_content = raw_writer_html
    
    # 3. 에셋 삽입 지점 자동화 (가정): Designer와 Researcher의 데이터를 기반으로 차트/이미지 태그를 주입합니다.
    asset_insertion = ""
    if design_assets:
        asset_insertion += "\n<!-- [Designer Asset Placeholder] -->\n"
        for key, asset in design_assets.items():
             asset_insertion += f'<div class="chart-component {key}">[자동 삽입 에셋]: {asset}</div>'
    
    # 4. 최종 HTML 구조를 만듭니다.
    final_html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{topic_title}</title>
</head>
<body>
{header}

<!-- [Start Blog Content] -->
{body_content}{asset_insertion}
<!-- [End Blog Content] -->

</body>
</html>
"""
    return final_html


def render_blog_post(
    file_name: str, 
    topic_title: str, 
    raw_writer_html: str, 
    design_assets: Dict[str, str], 
    data_points: List[str]
):
    """
    단일 블로그 포스팅을 생성하고 지정된 경로에 저장합니다.
    """
    print(f"-> Processing: {topic_title}...")
    final_html = generate_html_content(
        topic_title=topic_title, 
        raw_writer_html=raw_writer_html, 
        design_assets=design_assets, 
        data_points=data_points
    )

    # 파일명 규칙 준수: YYYY-MM-DD_[파일명]_[글주제].html
    file_name_safe = "".join(c for c in topic_title if c.isalnum() or c in ('-', '_')).lower()[:30]
    final_path = os.path.join(TARGET_DIR, f"{CURRENT_DATE_STR}_{file_name}_{file_name_safe}.html")

    try:
        with open(final_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"✅ Success: {final_path} 파일 저장 완료.")
        return True
    except Exception as e:
        print(f"❌ Error saving file {file_name}: {e}")
        return False

# --- [가상의 데이터베이스 시뮬레이션] ---
# 실제로는 이 데이터를 외부 JSON/DB에서 불러와야 함.
BLOG_DATA = [
    {
        "title": "국민연금만으론 부족합니다: 노후 '생활비' Gap 분석",
        "html": """
            <p>🚨 **핵심 메시지:** 지금부터 본 내용을 집중해서 읽어주십시오. 당신이 생각하는 은퇴 자금과 실제 필요한 돈 사이에는 엄청난 간극(Gap)이 존재합니다.</p>
            <h2>1. 국민연금이 예측하지 못한 '숨겨진 비용'</h2>
            <p>우리는 연금 액수만 봐서 안심하지만, 문제는 물가 상승률과 의료비 증가에 있습니다. 특히 70대 이후의 간병 및 비급여 항목은 공적 시스템이 커버하기 어렵습니다.</p>
            <h3>[Data Point: 생활비 Gap]</h3>
            <p class="warning-box">💡 **팩트 체크:** 보건복지부 통계에 따르면, 2035년 기준 예상 은퇴 가구의 월 필수 지출액은 약 XXX만원이지만, 국민연금 추정 수령액으로는 YYY만원이 부족합니다. (Gap: ZZZ만원)</p>
            <p class="cta-section">📌 **Action:** '나만의 노후 Gap 진단표'를 다운로드하고 정확한 격차 금액을 확인하세요! [CTA 버튼]</p>
        """, # Writer가 완성했다고 가정한 HTML 내용
        "assets": {
            "생활비_갭": "2035년 예상 필수 지출 vs 국민연금 추정 수령액 비교 차트",
            "물가상승_커브": "지난 10년간 CPI와 연금 지급률 격차 그래프"
        },
        "data": ["보건복지부/기획재정부 공표 은퇴 생활비 통계", "한국은행 (CPI 통계)"]
    },
    # 나머지 9개 주제에 대한 더미 데이터가 여기에 추가되어야 함.
]


def main():
    """메인 실행 함수: 모든 블로그 포스팅을 순차적으로 생성합니다."""
    print("=============================================================")
    print("✨ 온현 콘텐츠 렌더링 엔진 (content_renderer) 작동 시작 ✨")
    print(f"대상 디렉토리: {TARGET_DIR}")
    
    success_count = 0
    for data in BLOG_DATA:
        if render_blog_post(
            file_name=data["title"],
            topic_title=data["title"],
            raw_writer_html=data["html"],
            design_assets=data["assets"],
            data_points=data["data"]
        ):
            success_count += 1

    print("=============================================================")
    print(f"✅ 모든 블로그 포스팅 렌더링 완료. 총 {success_count}/{len(BLOG_DATA)}개 파일 저장 성공.")


if __name__ == "__main__":
    main()
# END OF FILE