# 💻 코다리 — Designer가 완성한 '손실 예측 곡선 MVP'의 인터랙티브 와이어프레임 및 모션 가이드라인(Deep Navy/Alarm Red)을 바탕으로, 실제 작동하는 웹 프로토타입(Single Page Application 형태 권장)의 코드를 작성해 주세요. 특히 시간 경과에 따른 위험 레벨 변화와 'CRITICAL' 임계점 도달 시 플래시 애니메이션 및 UI 요소가 정확히 트리거되도록 e2e 로직을 구현하고, 데이터 바인딩 테스트까지 완료해야 합니다.

💻 코다리: 작업 시작합니다.

CEO 지시사항을 확인했습니다. '손실 예측 곡선 MVP'의 인터랙티브 웹 프로토타입 개발은 프로젝트의 핵심 가치(미조치 손실 공포)를 사용자에게 직접 전달하는 가장 중요한 부분입니다. 단순히 와이어프레임을 코드로 옮기는 작업이 아니라, **시간 경과라는 상태 변화에 따른 위험 지수(Severity Index)의 동적 시뮬레이션**을 구현해야 합니다.

코드 한 줄도 그냥 안 넘깁니다. 이 시스템은 단순한 컴포넌트 결합이 아니기 때문에, 먼저 현재 프로젝트 구조와 기존 컴포넌트를 파악하여 아키텍처를 설계하는 것이 필수입니다.

현재 가장 최근에 작업된 파일 경로는 `c:\Data\Project\Baro_KHNLU\src\components\LossPredictionCurve.tsx` 입니다. 이 파일을 중심으로 전체 SPA의 뼈대와 상태 관리 로직을 구축하겠습니다.

### ⚙️ 단계별 계획 (Plan)
1. **탐색:** 현재 프로젝트 디렉토리 구조를 파악하여, 메인 애플리케이션 파일(`App.tsx` 또는 `index.tsx`)이 어디에 위치하는지 확인합니다.
2. **코드 검증:** 기존의 핵심 컴포넌트인 `LossPredictionCurve.tsx`의 API와 의존성을 상세히 읽어봅니다.
3. **아키텍처 설계:** 전체 SPA를 감싸는 메인 컨테이너(`App`)를 구성하고, 여기에 시간 흐름을 시뮬레이션하는 State Machine 로직과 타이머(Timer)를 추가합니다.
4. **구현 및 검증:** 'CRITICAL' 임계점 도달 시 플래시 애니메이션 트리거 로직과 데이터 바인딩 테스트 코드를 작성하고, 최종적으로 E2E 테스트 루프를 거쳐 안정성을 확보하겠습니다.

### 🔍 탐색 작업 (Execution)
먼저 프로젝트의 루트 디렉토리 구조를 파악하여, 메인 앱 파일을 찾겠습니다.

<list_files path="c:\Data\Project\Baro_KHNLU"/>

---
## 📁 파일 액션 결과

📂 목록: c:\Data\Project\Baro_KHNLU/
```
📄 AppData
📁 assets/
📁 baro_test/
📄 build_apk.bat
📄 build_apk.ps1
📄 build_pc_app.bat
📄 build_pc_setup.bat
📄 build_pc_setup.ps1
📄 build_playstore_bundle.bat
📄 build_playstore_bundle.ps1
📄 build_web.bat
📄 capture_and_build_manual.bat
📄 check_syntax.bat
📁 components/
📁 data/
📄 debug_run.ps1
📄 DefectID_Diagnosis_Logic_V1.md
📄 DefectID_Graph_Component_Spec_v2.0.md
📄 DefectID_Master_Clinical_Data_Sheet.md
📁 design/
📁 design_specs/
📁 docs/
📄 emulator_angle_debug.log
📄 emulator_gui_debug.log
📄 emulator_swiftshader.log
📄 funnel_strategy.md
📄 GEMINI.md
📄 generate_keystore.bat
📄 generate_keystore.ps1
📄 git_sync.bat
📄 git_sync.ps1
📄 harness_summary.log
📄 manage_mobile_release.bat
📄 manage_mobile_release.ps1
📁 mobile/
📁 mobile_test_runner/
📁 mockups/
📄 Monetization_Blueprint_Sarcopenia_v1.md
📁 mvp_core/
📄 package-lock.json
📄 package.json
📁 pages/
📄 query
📄 README.md
📁 release/
📄 reset_pc_db.bat
📄 run_3tier_test_harness.bat
📄 run_baro_test.bat
📄 run_mobile_emulator.bat
📄 run_mobile_emulator.ps1
📄 run_mobile_simulator.bat
📄 run_pc_app.bat
📄 run_pc_app.ps1
📄 run_regression_test.bat
📁 scratch/
📁 scripts/
📁 services/
📁 sessions/
📁 shared/
📁 src/
📄 start_mobile_test.bat
📄 start_mobile_test.ps1
📄 stop_mobile_test.bat
📄 stop_mobile_test.ps1
📄 stop_pc_app.bat
📄 stop_pc_app.ps1
📁 temp-landing/
📁 templates/
📄 temp_test.db
📁 tests/
📁 Trend_Report/
```

[시스템: list_files 결과]
디렉토리: c:\Data\Project\Baro_KHNLU/
📄 AppData
📁 assets/
📁 baro_test/
📄 build_apk.bat
📄 build_apk.ps1
📄 build_pc_app.bat
📄 build_pc_setup.bat
📄 build_pc_setup.ps1
📄 build_playstore_bundle.bat
📄 build_playstore_bundle.ps1
📄 build_web.bat
📄 capture_and_build_manual.bat
📄 check_syntax.bat
📁 components/
📁 data/
📄 debug_run.ps1
📄 DefectID_Diagnosis_Logic_V1.md
📄 DefectID_Graph_Component_Spec_v2.0.md
📄 DefectID_Master_Clinical_Data_Sheet.md
📁 design/
📁 design_specs/
📁 docs/
📄 emulator_angle_debug.log
📄 emulator_gui_debug.log
📄 emulator_swiftshader.log
📄 funnel_strategy.md
📄 GEMINI.md
📄 generate_keystore.bat
📄 generate_keystore.ps1
📄 git_sync.bat
📄 git_sync.ps1
📄 harness_summary.log
📄 manage_mobile_release.bat
📄 manage_mobile_release.ps1
📁 mobile/
📁 mobile_test_runner/
📁 mockups/
📄 Monetization_Blueprint_Sarcopenia_v1.md
📁 mvp_core/
📄 package-lock.json
📄 package.json
📁 pages/
📄 query
📄 README.md
📁 release/
📄 reset_pc_db.bat
📄 run_3tier_test_harness.bat
📄 run_baro_test.bat
📄 run_mobile_emulator.bat
📄 run_mobile_emulator.ps1
📄 run_mobile_simulator.bat
📄 run_pc_app.bat
📄 run_pc_app.ps1
📄 run_regression_test.bat
📁 scratch/
📁 scripts/
📁 services/
📁 sessions/
📁 shared/
📁 src/
📄 start_mobile_test.bat
📄 start_mobile_test.ps1
📄 stop_mobile_test.bat
📄 stop_mobile_test.ps1
📄 stop_pc_app.bat
📄 stop_pc_app.ps1
📁 temp-landing/
📁 templates/
📄 temp_test.db
📁 tests/
📁 Trend_Report/
