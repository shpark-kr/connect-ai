# 💻 코다리 — MiniFunnel Funnel('national_pension')의 e2e 테스트 결과를 바탕으로, 외부 제휴 링크를 안정적으로 삽입할 수 있는 전용 컴포넌트(SRP: System Recommendation Panel)의 최종 마크업과 JavaScript 로직을 구현하고 디버깅하십시오. 이 컴포넌트는 Deep Navy와 Crisis Red 톤을 유지하며, 사용자에게 위기감을 조성하는 '공식 프로토콜 인증' 요소를 포함해야 합니다. 완성 후에는 A/B 테스트 설정을 위한 코드 기반 준비도 완료해야 합니다.

💻 코다리: 작업 시작합니다.

CEO 지시사항은 이 프로젝트의 핵심 전환 경로(Conversion Path)에 직접 영향을 미치는 매우 중요한 요구사항입니다. MiniFunnel Funnel(`national_pension`)에서 가장 결정적인 순간, 즉 사용자가 위기감을 느끼고 솔루션 구매를 결심하는 '마찰 지점'을 책임지는 컴포넌트이기 때문에, 단순한 프론트엔드 구현 수준으로는 안 됩니다.

이 SRP (System Recommendation Panel)는 다음 3가지 요구사항을 완벽히 충족해야 합니다:
1.  **기술적 안정성:** 모든 외부 링크 클릭은 반드시 추적 로직(Tracking API Call)을 거쳐야 하며, 실패 시 백오프/재시도 메커니즘이 작동해야 합니다.
2.  **심리적 설득력:** Deep Navy와 Crisis Red를 사용한 '공식 프로토콜 인증' 요소를 통해 권위적인 신뢰감을 조성해야 합니다.
3.  **개발 유연성:** A/B 테스트 로직을 JS 레벨에서 분리하여, 콘텐츠만 변경하고 전체 컴포넌트 구조는 유지할 수 있도록 설계되어야 합니다 (SRP 원칙 준수).

따라서, 저는 이 작업을 **[탐색 → 구현(Markup & Logic) → 통합 및 검증]**의 3단계로 진행하겠습니다. 먼저 현재 프로젝트 파일 구조를 파악하여 기존 MiniFunnel 컴포넌트나 공통 UI 라이브러리 위치를 찾아야 합니다.

<list_files path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools"/>
<glob pattern="**/*MiniFunnel*.tsx" files="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools"/>

---
## 📁 파일 액션 결과

📂 목록: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools/
```
📁 api_modules/
📄 api_resilience_module.py
📄 circuit_breaker.py
📁 client/
📁 components/
📁 connect-ai/
📁 connect-ai-prototype/
📄 content_master_tester.py
📄 content_orchestrator.py
📄 data_ingestion_module.py
📁 data_pipeline/
📄 e2e_deployment_simulator.py
📄 e2e_funnel_cta_test_suite.py
📄 e2e_publishing_orchestrator.py
📄 E2E_Stability_Checklist_v1.md
📄 final_publishing_test_harness.py
📄 funnel_e2e_qa_script.py
📄 jest.config.js
📁 landing-kit/
📄 lint_test.json
📄 lint_test.md
📄 lint_test.py
📁 mini-app-funnel/
📁 mini-app-prototype/
📄 mini-app_funnel_api_contract.md
📁 mini-funnel-poc/
📁 mini-funnel-v2/
📄 MiniApp_Funnel_v1.0_DesignSpec_FIXED.md
📄 MockAPIService.py
📁 modules/
📁 module_source/
📁 nextjs-gap-prototype/
📄 openapi_mock_spec.yaml
📄 pack_apply.json
📄 pack_apply.md
📄 pack_apply.py
📄 policy_integrity_checker.py
📄 publishing_test_orchestrator.py
📄 pwa_setup.json
📄 pwa_setup.md
📄 pwa_setup.py
📁 react_components/
📄 resilience_publisher_tester.py
📁 schemas/
📁 scripts/
📁 services/
📁 src/
📁 stress_test/
📄 stress_test_posting_orchestrator.py
📁 tests/
📄 test_component_injector_resilience.py
📄 test_diagnosis_engine.py
📄 test_e2e_data_pipeline.py
📄 test_renderer_pipeline.py
📄 test_rollback_logic.py
📄 test_video_pipeline.py
📁 utils/
📄 video_auto_converter.py
📁 video_pipeline/
📄 video_renderer_core.py
📄 visual_qa_module.py
📄 web_init.json
📄 web_init.md
📄 web_init.py
📄 web_preview.json
📄 web_preview.md
📄 web_preview.py
📄 wordpress_publisher_tester.py
```
🔎 glob `**/*MiniFunnel*.tsx` (c:\Data\Project\connect-ai): 6개
```
.secondbrain/_company/_agents/developer/tools/components/MiniFunnel.tsx
.secondbrain/_company/_agents/developer/tools/src/pages/MiniFunnelLandingPage.tsx
src/components/mini-funnel/MiniFunnelPage.tsx
src/components/mini-funnel/MiniFunnelStateProvider.tsx
src/components/MiniFunnelCore.tsx
src/context/MiniFunnelContext.tsx
```

[시스템: list_files 결과]
디렉토리: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools/
📁 api_modules/
📄 api_resilience_module.py
📄 circuit_breaker.py
📁 client/
📁 components/
📁 connect-ai/
📁 connect-ai-prototype/
📄 content_master_tester.py
📄 content_orchestrator.py
📄 data_ingestion_module.py
📁 data_pipeline/
📄 e2e_deployment_simulator.py
📄 e2e_funnel_cta_test_suite.py
📄 e2e_publishing_orchestrator.py
📄 E2E_Stability_Checklist_v1.md
📄 final_publishing_test_harness.py
📄 funnel_e2e_qa_script.py
📄 jest.config.js
📁 landing-kit/
📄 lint_test.json
📄 lint_test.md
📄 lint_test.py
📁 mini-app-funnel/
📁 mini-app-prototype/
📄 mini-app_funnel_api_contract.md
📁 mini-funnel-poc/
📁 mini-funnel-v2/
📄 MiniApp_Funnel_v1.0_DesignSpec_FIXED.md
📄 MockAPIService.py
📁 modules/
📁 module_source/
📁 nextjs-gap-prototype/
📄 openapi_mock_spec.yaml
📄 pack_apply.json
📄 pack_apply.md
📄 pack_apply.py
📄 policy_integrity_checker.py
📄 publishing_test_orchestrator.py
📄 pwa_setup.json
📄 pwa_setup.md
📄 pwa_setup.py
📁 react_components/
📄 resilience_publisher_tester.py
📁 schemas/
📁 scripts/
📁 services/
📁 src/
📁 stress_test/
📄 stress_test_posting_orchestrator.py
📁 tests/
📄 test_component_injector_resilience.py
📄 test_diagnosis_engine.py
📄 test_e2e_data_pipeline.py
📄 test_renderer_pipeline.py
📄 test_rollback_logic.py
📄 test_video_pipeline.py
📁 utils/
📄 video_auto_converter.py
📁 video_pipeline/
📄 video_renderer_core.py
📄 visual_qa_module.py
📄 web_init.json
📄 web_init.md
📄 web_init.py
📄 web_preview.json
📄 web_preview.md
📄 web_preview.py
📄 wordpress_publisher_tester.py

[시스템: glob 결과]
패턴: **/*MiniFunnel*.tsx
루트: c:\Data\Project\connect-ai
매치 6개:
.secondbrain/_company/_agents/developer/tools/components/MiniFunnel.tsx
.secondbrain/_company/_agents/developer/tools/src/pages/MiniFunnelLandingPage.tsx
src/components/mini-funnel/MiniFunnelPage.tsx
src/components/mini-funnel/MiniFunnelStateProvider.tsx
src/components/MiniFunnelCore.tsx
src/context/MiniFunnelContext.tsx
