import unittest
from utils.cta_injector import FunnelCTAMasterInjector, CTAInjectionError

# 가상의 최종 확정된 CTA 에셋을 사용합니다. (실제로는 Designer가 제공한 값)
MOCK_CTA = "🚨 무료 전문가 진단 받기: 5060 맞춤 지원금 체크리스트 다운로드"

class TestFunnelCTAINjectionE2E(unittest.TestCase):
    """
    전체 콘텐츠 파이프라인에서 Funnel CTA가 누락 없이 강제 주입되는지 검증하는 E2E 테스트 스위트.
    """
    @classmethod
    def setUpClass(cls):
        """테스트 클래스 시작 시, Injector 객체를 초기화합니다."""
        print("--- 🛠️ FunnelCTA MasterInjector 초기화 중 ---")
        try:
            cls.injector = FunnelCTAMasterInjector(MOCK_CTA)
        except ValueError as e:
            raise Exception(f"테스트 설정 오류: {e}")

    def test_1_html_injection_blog(self):
        """[Blog HTML] 일반적인 블로그 본문 콘텐츠에 CTA가 정상적으로 주입되는지 검증."""
        print("\n--- 🧪 테스트 1/3: Blog HTML Injection ---")
        mock_content = """
        <h1>국민연금 사각지대 점검 방법</h1>
        <p>최근 공공데이터를 분석한 결과, 많은 분들이 놓치고 계신 중요한 지원금 리스크가 존재합니다.</p>
        <h2>핵심 체크포인트</h2>
        <ul><li>1. 소득 기준 재점검</li><li>2. 가입 기간 증빙 서류 준비</li></ul>
        <p>따라서 이 내용을 꼼꼼히 확인하는 것이 중요하며, 전문가의 도움이 필요합니다.</p>
        """
        expected_cta_fragment = "🚨 무료 전문가 진단 받기: 5060 맞춤 지원금 체크리스트 다운로드"
        
        # 실행 및 검증
        result = self.injector.inject_html(mock_content)
        self.assertIn(expected_cta_fragment, result, f"HTML에 CTA가 삽입되지 않았습니다. 결과: {result}")
        print("✅ HTML 테스트 통과.")

    def test_2_markdown_injection_youtube(self):
        """[YouTube Description Markdown] 롱폼 스크립트의 설명란 본문에 CTA가 정상적으로 주입되는지 검증."""
        print("\n--- 🧪 테스트 2/3: YouTube Markdown Injection ---")
        mock_content = """
        오늘 영상에서는 공공데이터 기반으로 놓치기 쉬운 세 가지 지원금을 분석했습니다. 
        이 내용만 알아도 최소 몇십만원을 절약할 수 있습니다!
        시간 순서대로 잘 시청해주세요. 👍
        """
        expected_cta_fragment = "🚨 무료 전문가 진단 받기: 5060 맞춤 지원금 체크리스트 다운로드"

        # 실행 및 검증
        result = self.injector.inject_markdown(mock_content)
        self.assertIn(expected_cta_fragment, result, f"Markdown에 CTA가 삽입되지 않았습니다. 결과: {result}")
        print("✅ Markdown 테스트 통과.")

    def test_3_plain_text_injection_instagram(self):
        """[Instagram Plain Text] 숏폼/릴스 캡션 등 단순 텍스트에 CTA가 정상적으로 주입되는지 검증."""
        print("\n--- 🧪 테스트 3/3: Plain Text Injection ---")
        mock_content = """
        #5060 #지원금 #국민연금
        이번 이슈를 놓치면 정말 큰일납니다. 오늘 내용 꼭 저장해두세요! 💾
        """
        expected_cta_fragment = "🚨 무료 전문가 진단 받기: 5060 맞춤 지원금 체크리스트 다운로드"

        # 실행 및 검증
        result = self.injector.inject_plain_text(mock_content)
        self.assertIn(expected_cta_fragment, result, f"Plain Text에 CTA가 삽입되지 않았습니다. 결과: {result}")
        print("✅ Plain Text 테스트 통과.")

    def test_4_mandatory_validation_and_no_duplicates(self):
        """[Validation] 콘텐츠에 이미 CTA가 포함되어 있을 경우 중복 주입을 방지하는지 검증."""
        print("\n--- 🧪 테스트 4/3: Duplicate Prevention (Critical) ---")
        # 기존 콘텐츠 자체가 CTA를 포함하고 있음
        mock_content = "최근 분석 결과입니다. 🚨 무료 전문가 진단 받기: 5060 맞춤 지원금 체크리스트 다운로드를 꼭 하세요."
        expected_output = mock_content # 내용 변화가 없어야 함

        # 실행 및 검증 (HTML 형식으로 테스트)
        result = self.injector.inject_html(mock_content)
        self.assertEqual(result, expected_output, "이미 CTA가 있는 경우 원본 콘텐츠가 변형되어서는 안 됩니다.")
        print("✅ 중복 방지 로직 통과.")


if __name__ == '__main__':
    # unittest 실행을 위해 임시로 경로를 설정합니다.
    import os; os.chdir(r"c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\tests\unit")
    unittest.main()