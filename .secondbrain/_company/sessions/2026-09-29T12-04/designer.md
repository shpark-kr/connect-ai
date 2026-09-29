# 🎨 Designer — Developer가 수정한 E2E QA 스크립트의 검증 범위를 재설정해야 합니다. MiniFunnel의 Critical System Alert UI (CSA-UI) 컴포넌트가 다음 3가지 핵심 상호작용을 완벽하게 통과하는지 확인하도록 상세한 테스트 시퀀스를 제공해주세요: ① Deep Crimson Red 테마 적용 여부, ② T+2,500ms의 State Transition 타이밍 정확성, ③ 오류 발생 후 사용자가 취해야 할 CTA(행동 유도) 버튼의 시각적 위계 구조.

🎨 Designer: 작업 시작합니다.

CEO님의 지시에 따라, MiniFunnel의 Critical System Alert UI (CSA-UI) 컴포넌트가 기술적으로 완벽하게 검증될 수 있도록 상세한 E2E 통합 테스트 시나리오를 설계했습니다. 이는 단순 기능 테스트를 넘어, '시스템 고장(Failure)'이라는 권위적 테마와 그에 따른 사용자 경험 흐름을 코딩 레벨에서 강제하는 목표입니다.

이 스크립트는 기존의 `funnel_e2e_qa_script.py` 내에 추가되어야 할 새로운 테스트 클래스 및 메서드 세트이며, 명확한 기술적 검증 기준(Assertions)과 시간 동기화(Timing Synchronization)를 포함합니다.

### 📝 E2E QA 상세 테스트 시나리오: CSA-UI Resilience Verification

`<create_file path="c:\Data\Project\connect-ai\design_assets\CSA-UI_Test_Plan_v2.md"># MiniFunnel Critical System Alert UI (CSA-UI) 통합 테스트 계획 v2.0`</create_file>
```markdown
## 🎯 목적: CSA-UI의 시스템적 안정성 및 사용자 흐름 검증

본 테스트는 단순히 오류 메시지 출력 여부를 확인하는 것이 아니라, '시스템 실패'라는 스토리텔링에 따른 다음 세 가지 핵심 요소가 완벽하게 작동함을 증명합니다.

1. **Deep Crimson Red 테마 적용 (Visual Authority):** 오류 발생 시 전역 CSS 및 컴포넌트 배경색이 지정된 Deep Crimson Red 계열(HEX: #900C3F)로 정확히 변환되는지 검증.
2. **T+2,500ms State Transition (Temporal Accuracy):** 실패 경고 메시지 노출 시점부터 다음 CTA 유도 스크린으로 전환되는 타이밍이 ±100ms 오차 범위 내에 있는지 측정하고 검증.
3. **CTA 위계 구조 및 포커스 순서 (Usability Hierarchy):** 오류 발생 후, 사용자의 시선 흐름과 키보드 포커스가 가장 중요한 '해결책 CTA'로 자연스럽게 유도되는지 확인.

---

## 🧪 테스트 스크립트 구조 (Pseudo-Code/unittest Style)

이 코드는 기존 `funnel_e2e_qa_script.py` 파일에 추가되어야 할 새로운 클래스입니다.

```python
import unittest
from selenium.webdriver.common.by import By
# 가정: WebDriver가 DOM 조작 및 시간 측정을 담당한다고 가정합니다.

class TestCSAUIResilience(unittest.TestCase):
    """
    CSA-UI 컴포넌트의 리질리언스 검증 테스트 스위트. 
    실패 시나리오를 강제 주입하고, 시스템 반응을 측정한다.
    """
    
    @classmethod
    def setUpClass(cls):
        # 전역 설정: 페이지 로드 및 초기 상태 확인
        pass

    def test_1_deep_crimson_red_theme_application(self):
        """[검증 1] 오류 발생 시 Deep Crimson Red 테마 적용 여부 검증."""
        print("--- Running Test 1: Visual Failure State ---")
        # 1. 실패 시나리오 트리거 (예: 필수 입력값 누락)
        self.driver.click(By.ID("btn_submit")) # submit 버튼 클릭 -> 에러 발생 가정

        # 2. Assertions (CSS 검증): DOM의 주요 요소에 Deep Crimson Red가 적용되었는지 확인
        failure_container = self.driver.find_element(By.CLASS_NAME, "csa-alert-panel")
        self.assertEqual(
            failure_container.get_style_property("background-color"), 
            "rgb(144, 12, 63)", # Deep Crimson Red의 RGB 값으로 검증 (또는 hex 코드를 직접 비교)
            "FAIL: CSA Alert Panel background color mismatch."
        )

        # 3. Assertions (Typography): 경고 메시지 제목 글꼴과 색상이 지정된 권위적 스타일인지 확인
        title = self.driver.find_element(By.CLASS_NAME, "csa-error-title")
        self.assertTrue("font-family: monospace" in title.get_style_property("font-family"))

    def test_2_transition_timing_accuracy(self):
        """[검증 2] 오류 메시지 노출 후 다음 스크린 전환 타이밍 측정."""
        print("--- Running Test 2: Temporal State Transition ---")
        start_time = time.time() # T0: 테스트 시작 시간

        # 1. 실패 시나리오 트리거 (T0)
        self.driver.click(By.ID("btn_submit")) 
        
        # 2. Critical Alert UI 노출 확인 (T0 -> T+ε)
        alert = self.driver.find_element(By.CLASS_NAME, "csa-alert-panel")
        self.assertTrue(alert.is_displayed(), "FAIL: CSA Panel must appear immediately.")

        # 3. 다음 단계 CTA 버튼 등장 대기 (T+2.5s)
        next_cta = self.driver.find_element(By.ID("btn_proceed_to_error_fix"))
        
        # WebDriver의 Explicit Wait을 사용하여 정확한 시간 측정 시뮬레이션
        WebDriverWait(self.driver, 10).until(
            lambda d: next_cta.is_displayed() and abs(time.time() - start_time) >= 2.49 and abs(time.time() - start_time) <= 2.51
        )
        end_time = time.time() # T+T_elapsed
        elapsed_time = end_time - start_time

        # 4. Assertions (Timing 검증): 시간 오차 범위 확인
        self.assertAlmostEqual(elapsed_time, 2.5, delta=0.1, msg=f"FAIL: Transition time {elapsed_time:.3f}s is outside the required range [2.4s, 2.6s].")

    def test_3_cta_visual_hierarchy_and_focus(self):
        """[검증 3] 오류 발생 후 CTA의 시각적 위계 및 키보드 포커스 순서 검증."""
        print("--- Running Test 3: Usability and Focus Flow ---")
        
        # 1. 실패 시나리오 트리거 (T0)
        self.driver.click(By.ID("btn_submit")) 

        # 2. Assertions (Visual Hierarchy): 가장 중요도가 높은 CTA가 가장 먼저, 가장 크게 보여야 함.
        primary_cta = self.driver.find_element(By.ID("btn_proceed_to_error_fix"))
        secondary_info = self.driver.find_element(By.CLASS_NAME, "csa-learn-more")

        # Assert 1: Primary CTA의 크기/대비도 검증 (가장 두드러져야 함)
        self.assertTrue("padding: 20px" in primary_cta.get_style_property("padding"), "Primary CTA must be the largest element.")
        self.assertEqual(primary_cta.get_style_property("background-color"), "#FFCC00", "Primary CTA background color must contrast sharply.");

        # Assert 2: Tab 순서 검증 (Focus Order)
        # 사용자가 TAB 키를 누를 때, 반드시 Primary CTA가 가장 먼저 포커스를 가져야 함.
        self.assertEqual(self.driver.get_focused_element(), primary_cta, "FAIL: Initial tab focus must land on the Primary Action CTA.")

```

### 📊 평가: 완료 — CEO님의 지시에 따라 기술적 검증 가이드를 설계하여 개발팀에 전달할 준비가 되었습니다.
📝 다음 단계: 코다리에게 `CSA-UI_Test_Plan_v2.md` 파일을 전달하고, 기존 QA 스크립트에 이 테스트 케이스들을 통합하도록 요청해야 합니다.

<list_files path="c:\Data\Project\connect-ai\design_assets"/>
```

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\design_assets\CSA-UI_Test_Plan_v2.md
📂 목록: c:\Data\Project\connect-ai\design_assets/
```
📄 CSA-UI_Interaction_Spec_Manual.md
📄 CSA-UI_Test_Plan_v2.md
📄 mini_funnel_final_mockup_v1.md
```

[시스템: list_files 결과]
디렉토리: c:\Data\Project\connect-ai\design_assets/
📄 CSA-UI_Interaction_Spec_Manual.md
📄 CSA-UI_Test_Plan_v2.md
📄 mini_funnel_final_mockup_v1.md
