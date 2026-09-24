import re
from typing import Tuple, Dict

class CTAInjectionError(Exception):
    """CTA 주입 실패 시 발생하는 커스텀 예외."""
    pass

class FunnelCTAMasterInjector:
    """
    Funnel CTA Master Component를 다양한 콘텐츠 형식에 자동으로 강제 주입하고 검증하는 모듈.
    모든 콘텐츠 파이프라인의 공통 게이트 역할을 수행해야 합니다.
    """
    def __init__(self, cta_asset: str):
        """
        Args:
            cta_asset (str): 최종 확정된 CTA 마스터 컴포넌트 문자열. 
                              (예: '지금 전문가 진단 받기 > [링크]')
        """
        if not cta_asset or not isinstance(cta_asset, str):
             raise ValueError("CTA Asset은 필수이며 유효한 문자열이어야 합니다.")
        self.cta_asset = cta_asset

    def _validate_injection(self, content: str) -> bool:
        """
        콘텐츠에 CTA가 이미 존재하는지 확인하여 중복 삽입을 방지하는 내부 검증 로직.
        실제 운영 환경에서는 이 패턴 매칭이 매우 정교해야 합니다.
        """
        # 간단한 예시로, CTA 에셋의 핵심 키워드가 포함되어 있는지 확인합니다.
        return self.cta_asset.lower() in content.lower()

    def inject_html(self, content: str) -> str:
        """
        블로그 HTML 형식에 Funnel CTA를 삽입합니다. 
        일반적으로 본문 마지막 섹션이나 결론 직전에 배치하는 것이 효과적입니다.
        """
        if self._validate_injection(content):
            print("⚠️ [HTML] 경고: CTA가 이미 감지되어 중복 주입을 건너뜁니다.")
            return content

        # HTML 구조상 가장 안전하고 눈에 띄는 위치를 찾습니다. (e.g., </p> 또는 </div> 태그 직전)
        injection_point = "</body>" # 임시로 바디 끝에 강제 삽입한다고 가정합니다.
        if injection_point in content:
             return f"{content[:-len(injection_point)]}<div class='cta-master-component'>{self.cta_asset}</div>{injection_point}"
        else:
            # Fallback: 본문 끝에 <div>로 감싸서 강제 삽입
            return f"{content} <div class='cta-master-component' style='margin-top: 30px; padding: 20px; border: 2px solid #FF6B3D;'>{self.cta_asset}</div>"


    def inject_markdown(self, content: str) -> str:
        """
        유튜브 설명란 본문 (마크다운)에 Funnel CTA를 삽입합니다.
        보통 '---' 구분선이나 마지막 문단 직후가 적절합니다.
        """
        if self._validate_injection(content):
            print("⚠️ [Markdown] 경고: CTA가 이미 감지되어 중복 주입을 건너뜁니다.")
            return content

        # 마크다운 구조에 맞게 강조하는 것이 중요합니다.
        cta_formatted = f"\n\n***\n**🚨 필수 확인:** {self.cta_asset} (클릭하여 진단받으세요)\n***"
        
        # 마지막 문단 끝에 추가한다고 가정하고, 가장 간단하게 내용을 뒤에 붙입니다.
        return f"{content}{cta_formatted}\n"


    def inject_plain_text(self, content: str) -> str:
        """
        인스타그램 캡션이나 단순 API 전송용 Plain Text에 Funnel CTA를 삽입합니다.
        가장 간결하고 강력한 형태로 포맷팅 합니다.
        """
        if self._validate_injection(content):
            print("⚠️ [Plain Text] 경고: CTA가 이미 감지되어 중복 주입을 건너뜁니다.")
            return content

        # 텍스트에서는 이모지와 대문자로 긴급성을 부여합니다.
        cta_formatted = f"\n\n⚡️ 더 많은 정보는 필수 진단 가이드를 확인하세요! {self.cta_asset} ✨"
        return f"{content}{cta_formatted}"

    def process(self, content: str, format_type: str) -> str:
        """다양한 형식에 맞춰 CTA를 처리하는 메인 인터페이스."""
        format_map = {
            'html': self.inject_html,
            'markdown': self.inject_markdown,
            'plain': self.inject_plain_text
        }
        injector_func = format_map.get(format_type.lower())
        if not injector_func:
            raise ValueError("지원하지 않는 형식입니다. ('html', 'markdown', 'plain'만 지원)")

        return injector_func(content)

# 예시 사용법 (테스트 코드에서 활용)
# cta = "지금 전문가 진단 받기 > [링크]"
# injector = FunnelCTAMasterInjector(cta)
# html_output = injector.inject_html("...")
print("✅ CTA Injection Module 설계 완료.")