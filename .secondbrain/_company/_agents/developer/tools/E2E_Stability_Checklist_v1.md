# ✅ E2E 통합 테스트 안정화 검증 체크리스트 (Ver 1.0)

## 📌 목표: 회복 탄력성(Resilience) 및 의존성 무결성 확보
이 체크리스트는 `final_publishing_test_harness` 실행 전, 시스템 전체의 의존성이 완벽한지 확인하는 '최종 검증 리포트'로 활용되어야 합니다.

### 🛠️ 1. 의존성(Dependency) 매핑 및 초기화 점검
*   [ ] **모든 핵심 모듈 식별:** `content_master_tester`, `api_resilience_module`, `e2e_funnel_cta_test_suite` 등 모든 서비스 컴포넌트의 정확한 위치와 인터페이스(입력/출력)를 정의했는가?
*   [ ] **Service Locator 패턴 적용:** 하네스 내부에서 `import` 대신 동적 로딩 함수 (`load_module`)를 사용하여 의존성 경로 오류에 대비했는가? (✅ 리팩토링 완료)
*   [ ] **Mocking 전략 검증:** 외부 API 호출(예: YouTube Upload, Wordpress Post) 시 실제 호출을 막고 Mock 객체로 대체하는 로직이 모든 테스트 케이스에 적용되었는가?

### 💣 2. 에러 핸들링 및 회복 탄력성 (Failure Handling & Resilience)
*   [ ] **ImportError 방어:** 모듈 임포트 실패 시(`try-except` 블록), 프로그램 전체가 크래시되는 것이 아니라 해당 컴포넌트만 '건너뛰기'하고 테스트를 계속할 수 있는 메커니즘이 작동하는가? (✅ `load_module` 구현)
*   [ ] **Input Data Validation:** 모든 테스트 입력 데이터(예: 스크립트, 제목, 썸네일 에셋)는 Null/Empty 값에 대한 예외 처리를 포함하는가?
*   [ ] **Setup/Teardown 격리:** 각 테스트 케이스(`test_X`) 실행 전후로 반드시 필요한 자원(DB 연결, 파일 임시 생성)을 설정하고 제거하는 `setUp`/`tearDown` 훅이 완벽하게 작동하는가?

### 🚀 3. 핵심 로직 검증 (Core Logic Validation)
*   [ ] **데이터 무결성:** 콘텐츠 생산 파이프라인의 모든 단계(리서치 $\rightarrow$ 스크립트 $\rightarrow$ 자막/비주얼 $\rightarrow$ 업로드 메타데이터)에서 데이터가 누락되거나 형식 오류 없이 전달되는지 End-to-End로 검증했는가?
*   [ ] **Funnel CTA 테스트:** `e2e_funnel_cta_test_suite`를 통해 Funnel CTA (리드 마그넷 다운로드, 제휴 링크)가 실제로 클릭 가능한 형태로 변환되어 최종 발행물에 포함되는지 확인하는 시뮬레이션이 추가되었는가?