# 💻 코다리 — Designer가 확정할 애니메이션 명세서(Animation Specification)를 기반으로, MiniFunnel의 모든 인터랙티브 컴포넌트(시스템 경고 오버레이, Defect ID 코드 노출, 임계점 CTA 배경 등)에 글리치 효과 및 Red/Blue 컬러 로직을 완벽하게 통합하는 바닐라 JS 프로토타입 버전을 완성해주세요. 특히, 사용자가 진단 과정을 진행할 때의 모든 애니메이션 트리거와 상태 변화(State Change)를 코딩하고, 코드 리뷰가 가능한 형태로 정리해야 합니다.

💻 코다리: 작업 시작합니다. 시니어 엔지니어 입장에서 이 지시는 매우 중요합니다. MiniFunnel의 핵심은 '위기감'을 전달하는 애니메이션과 상태 변화 로직입니다. 바닐라 JS 프로토타입으로 구현하라는 것은, 외부 라이브러리에 의존하지 않고 순수한 웹 기술로 시스템적 신뢰도를 확보하겠다는 뜻이므로, 코딩 원칙상 매우 바람직합니다.

다만, 이전에 'Designer'가 확정한 **애니메이션 명세서(Animation Specification)**가 현재 컨텍스트에 직접적으로 보이지 않습니다. 애니메이션 로직은 명세서를 기반으로 해야 하므로, 먼저 해당 스펙을 확보해야 합니다. 만약 스펙이 없다면, 이전의 의사결정 로그와 공학적 위기감 조성 원칙(Deep Crimson Red/Glitch Effect)을 바탕으로 임시 가정을 세우고 진행하겠습니다.

일단 프로젝트 디렉토리를 탐색하여 기존 구조를 파악하고, 프로토타입 구현에 필요한 HTML 및 JS 파일의 위치를 확인하겠습니다.

<list_files path="c:\Data\Project\connect-ai"/>


---
## 📁 파일 액션 결과

📂 목록: c:\Data\Project\connect-ai/
```
📄 01_개발자보고서_E2E_TestPriorityList_[YYYYMMDD].md
📁 ActionItems/
📁 api/
📁 app/
📄 ARCHITECTURE.md
📁 assets/
📁 backend/
📁 business/
📄 connect-ai-lab-2.89.157.vsix
📄 connect-ai-lab-2.89.158.vsix
📄 context_processor.py
📁 data_pipeline/
📄 data_validator.py
📁 design/
📄 DESIGN.md
📁 designs/
📁 design_assets/
📄 DESIGN_SPECIFICATION.md
📁 design_system_spec/
📄 detect_tg.js
📄 EDUCATIONAL_SLIDES.md
📄 final_handoff_briefing_v2.0.md
📄 Funnel_MVP_E2E_Test_Plan_v1.0.md
📄 GapAnalyzerPrototype.html
📄 index.html
📁 KnowledgeBase/
📄 LICENSE
📄 lpo_prototype
📄 MARKDOWN_DOCUMENTATION_MANUAL.md
📁 mini-app/
📄 mini-app-final-prototype.html
📁 mini-app-funnel/
📄 mini-app-funnel-mvp.html
📄 mini-app-risk-score-mockup.html
📄 mini-app_final_prototype_e2e_test_report.md
📄 mini-app_final_prototype_refactor_report.md
📁 mini_funnel_design_specs/
📄 mini_funnel_qa_checklist_handover.md
📄 package-lock.json
📄 package.json
📄 PLAZA_SETUP.md
📄 PRESENTATION.md
📁 prototype/
📄 README.md
📄 README_GapVisualization_Guide.md
📄 renderer_core.py
📁 researcher/
📁 research_output/
📄 risk_gauge_test.html
📁 schemas/
📁 scripts/
📄 secretary_task_briefing_48h.md
📁 services/
📁 sessions/
📄 SHOWCASE_GUIDE.md
📁 src/
📄 Strategic_Monetization_Playbook_v2.0.md
📄 system_schema.json
📁 temp/
📁 tests/
📄 test_client.py
📄 test_context_processor.py
📄 test_dataset.csv
📄 test_gap_pipeline_v1.py
📄 test_renderer.py
📄 test_solution_assets.py
📁 tools/
📄 tsconfig.json
📄 video_renderer.py
📁 writer_output/
📁 _company/
📁 결과물/
📄 튜토리얼_비서_연결.md
```

[시스템: list_files 결과]
디렉토리: c:\Data\Project\connect-ai/
📄 01_개발자보고서_E2E_TestPriorityList_[YYYYMMDD].md
📁 ActionItems/
📁 api/
📁 app/
📄 ARCHITECTURE.md
📁 assets/
📁 backend/
📁 business/
📄 connect-ai-lab-2.89.157.vsix
📄 connect-ai-lab-2.89.158.vsix
📄 context_processor.py
📁 data_pipeline/
📄 data_validator.py
📁 design/
📄 DESIGN.md
📁 designs/
📁 design_assets/
📄 DESIGN_SPECIFICATION.md
📁 design_system_spec/
📄 detect_tg.js
📄 EDUCATIONAL_SLIDES.md
📄 final_handoff_briefing_v2.0.md
📄 Funnel_MVP_E2E_Test_Plan_v1.0.md
📄 GapAnalyzerPrototype.html
📄 index.html
📁 KnowledgeBase/
📄 LICENSE
📄 lpo_prototype
📄 MARKDOWN_DOCUMENTATION_MANUAL.md
📁 mini-app/
📄 mini-app-final-prototype.html
📁 mini-app-funnel/
📄 mini-app-funnel-mvp.html
📄 mini-app-risk-score-mockup.html
📄 mini-app_final_prototype_e2e_test_report.md
📄 mini-app_final_prototype_refactor_report.md
📁 mini_funnel_design_specs/
📄 mini_funnel_qa_checklist_handover.md
📄 package-lock.json
📄 package.json
📄 PLAZA_SETUP.md
📄 PRESENTATION.md
📁 prototype/
📄 README.md
📄 README_GapVisualization_Guide.md
📄 renderer_core.py
📁 researcher/
📁 research_output/
📄 risk_gauge_test.html
📁 schemas/
📁 scripts/
📄 secretary_task_briefing_48h.md
📁 services/
📁 sessions/
📄 SHOWCASE_GUIDE.md
📁 src/
📄 Strategic_Monetization_Playbook_v2.0.md
📄 system_schema.json
📁 temp/
📁 tests/
📄 test_client.py
📄 test_context_processor.py
📄 test_dataset.csv
📄 test_gap_pipeline_v1.py
📄 test_renderer.py
📄 test_solution_assets.py
📁 tools/
📄 tsconfig.json
📄 video_renderer.py
📁 writer_output/
📁 _company/
📁 결과물/
📄 튜토리얼_비서_연결.md
