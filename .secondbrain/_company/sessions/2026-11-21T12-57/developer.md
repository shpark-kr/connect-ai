# 💻 코다리 — Designer가 완성한 '진단 보고서 페이지'의 최종 와이어프레임을 검토하여, 이를 실제로 동작 가능한 Atomic Design 기반의 컴포넌트 스펙 시트로 변환해 주세요. 모든 인터랙션(버튼 클릭, 상태 변화, 패키지 선택)에 대한 코드 레벨의 명세와 의존성 주입 컨테이너 패턴을 적용할 수 있도록 구조를 설계하고, 주요 기능별 API 통합 및 E2E 테스트 루프 구축 계획까지 포함한 개발 가이드라인을 작성해 주세요.

💻 코다리: 작업 시작합니다.

CEO 지시사항을 받았습니다. Designer가 완성한 '진단 보고서 페이지' 와이어프레임은 훌륭하지만, 이것만으로는 프로덕션 레벨의 코드베이스로 간주할 수 없습니다. "어떻게" 이 위기감이 코드로 구현되고, 클릭 한 번에 전체 시스템이 무너지지 않을지에 대한 설계가 필요합니다.

저는 시니어 풀스택 엔지니어로서, 단순한 와이어프레임 변환을 거부합니다. 이것은 **Atomic Design 기반의 컴포넌트 아키텍처**로 재구성되어야 하며, 모든 상호작용은 *예측 가능하고* *테스트 가능하게* 설계되어야 합니다.

요청하신 대로, 'S-D740 진단 보고서 페이지'를 위한 최종 개발 가이드라인을 작성하겠습니다.

---

### ⚙️ MiniFunnel: S-D740 진단 보고서 컴포넌트 스펙 시트 (Atomic Design v1.0)

#### 🎯 아키텍처 목표
*   **패턴:** 의존성 주입(Dependency Injection, DI) 컨테이너 패턴 적용. 각 기능(진단 엔진, 결제 모듈, UI 로직)은 독립된 서비스 레이어로 분리되어야 합니다.
*   **원칙:** 단일 책임 원칙 (Single Responsibility Principle, SRP) 준수. 컴포넌트는 상태 관리만 담당하고, 비즈니스 로직은 외부 `Service Layer`에 위임합니다.
*   **프레임워크 가정:** Next.js/React + TypeScript (가장 효율적인 현대 웹 아키텍처로 가정).

#### 🧱 I. 컴포넌트 정의 및 API 명세 (Code-Level Specs)

| 컴포넌트 이름 | 책임(Responsibility) | Props (입력) | State 관리 (내부) | 필수 의존성/API 호출 |
| :--- | :--- | :--- | :--- | :--- |
| **`DiagnosticHeader`** | 시스템 위기감 조성 및 핵심 정보 표시. (Deep Navy, Crisis Red) | `defectId: string`, `status: 'CRITICAL' \| 'DEGRADED'`, `urgencyLevel: number` | None | N/A (순수 UI 렌더링). 애니메이션은 CSS/Tailwind로 처리. |
| **`ErrorLogVisualizer`** | 기술적 권위를 부여하는 오류 로그 시각화. | `logData: string[]`, `sourceModule: string` | None | API 호출 필요 없음. 외부 데이터를 받아 포맷팅만 담당. |
| **`DiagnosisInsightCard`** | 핵심 진단 결과를 강조. (Gold Accent) | `keyFinding: string`, `severityImpact: number` | None | N/A. 렌더링 로직에 집중. |
| **`PackageSelectorContainer`** | 단계별(L1 $\rightarrow$ L2 $\rightarrow$ L3) 제품 구매 유도 및 상태 관리. | `currentDiagnosis: object[]`, `initialStep: 'Bronze' \| 'Silver' \| 'Gold'` | `selectedTier: string`, `isPaid: boolean` | 🟢 **`[Service] DiagnosisEngineAPI`**: 진단 결과에 따른 최적 패키지 계산. <br> 🟡 **`[Service] PaymentGatewayAPI`**: 결제 상태 확인 및 처리 (결제 성공/실패). |
| **`CTAButton_Buy`** | 구매 액션 트리거. | `tierName: string`, `price: number`, `onPurchaseClick: (tier: string) => Promise<void>` | Disabled 여부 (`isLoading`) | 🟢 **`[Service] PaymentGatewayAPI`**: 결제 요청을 비동기적으로 처리하고, 성공/실패 상태를 반환. |

#### 🧪 II. 로직 흐름 및 의존성 주입(DI) 설계

1.  **데이터 플로우:**
    *   `DiagnosisPageContainer` (Root Component)가 `[Service] DiagnosisEngineAPI`에 요청 (`defectId: S-D740`).
    *   `DiagnosisEngineAPI`는 백엔드에서 진단 결과를 받아 **최적화된 패키지 순서와 가격 구조**를 결정합니다.
    *   결정된 데이터는 `PackageSelectorContainer`의 Props로 주입됩니다. (DI 원칙 준수)
2.  **상태 변화 관리:**
    *   사용자가 `CTAButton_Buy` 클릭 $\rightarrow$ `DiagnosisPageContainer`가 **`[Service] PaymentGatewayAPI`**를 호출하며, 로딩 상태(`isLoading`)를 true로 변경합니다.
    *   결제 성공 시: `PackageSelectorContainer`의 내부 상태 (`selectedTier`, `isPaid`)를 업데이트하고, 감사 페이지(Thank You Page)로 라우팅을 지시합니다.
    *   결제 실패 시: 사용자에게 구체적인 에러 메시지(예: "카드 정보가 유효하지 않습니다")를 팝업으로 보여주며, 상태만 `isLoading`을 false로 되돌립니다.

#### ✅ III. E2E 통합 테스트 루프 구축 계획 (테스트 가능성 검증)

이 복잡한 Funnel은 단일 단위 테스트(Unit Test)로는 커버가 불가능합니다. 반드시 **End-to-End (E2E)** 테스트를 통해 전체 사용자 흐름을 검증해야 합니다.

**필수 E2E 시나리오:**
1.  **Scenario 1: 성공적인 Funnel 완료 (Happy Path):**
    *   [Test Action] 페이지 진입 $\rightarrow$ `DiagnosisHeader`가 'CRITICAL' 상태를 정확히 표시하는지 검증.
    *   [Test Action] L1 패키지를 선택하고, 가짜 결제 정보를 입력하여 구매 버튼 클릭.
    *   [Expected Result] PaymentGatewayAPI 호출이 성공적으로 완료되고, 다음 페이지로의 라우팅이 트리거되는지 확인.
2.  **Scenario 2: 재시도 및 실패 처리 (Negative Path):**
    *   [Test Action] L3 패키지를 선택하고, 유효하지 않은 결제 정보를 입력하여 구매 버튼 클릭.
    *   [Expected Result] `CTAButton_Buy`가 오류 상태로 전환되고, 컴포넌트가 **사용자 친화적인 에러 메시지**를 정확히 표시하는지 확인 (페이지 이탈 방지).
3.  **Scenario 3: 데이터 무결성 검사:**
    *   [Test Action] 진단 보고서의 특정 지표(예: ATP/ADP Ratio)가 변경될 때, `DiagnosisInsightCard`의 텍스트와 색상이 비례적으로 업데이트되는지 확인. (데이터 변화에 따른 UI 반영 검증).

---
### 🚀 최종 과제 결정 및 에이전트 분배

**[최적화된 단일 작업]**: 현재 디자인 명세는 완벽하지만, 이는 아직 가짜 코드(Mock)입니다. 가장 중요한 것은 이 복잡한 Funnel의 **예측 가능성 및 결제 과정의 안정성**을 확보하는 것입니다.
**→ 과제: MiniFunnel Funnel의 E2E 테스트 환경 구축 및 주요 API 통합 시뮬레이션.**

*   **담당 에이전트:** 💻 코다리 (시니어 풀스택 엔지니어) — 아키텍처 설계와 테스트 코드 작성에 가장 적합.
*   **필요 도구 사용:** `e2e_funnel_cta_test_suite`를 활용하여 가이드라인에서 제시한 E2E 시나리오 1, 2, 3을 코드로 구현하고 실행해야 합니다.

<run_command>cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe e2e_funnel_cta_test_suite.py</run_command>

📊 평가: 진행중 — 상세한 아키텍처 명세가 완료되었으며, 다음 스텝은 이 설계에 기반하여 실제 테스트 환경을 구축하는 것입니다.
📝 다음 단계: `e2e_funnel_cta_test_suite`를 실행하여 MiniFunnel Funnel의 핵심 사용자 여정(Happy/Negative Path) 안정성을 검증할 코드 레벨의 결과를 받습니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppDa`
```
=============================================

--- [🌐 Web Test] Funnel 'national_pension' 테스트 시작 ---
[✅ Data Injection]: 데이터 성공적으로 주입됨: 월 평균 150만원 부족
[❌ Web Flow ERROR]: 네트워크/요청 실패: HTTPSConnectionPool(host='www.onhyeon-site.com', port=443): Max retries exceeded with url: /signup/submit (Caused by NameResolutionError("HTTPSConnection(host='www.onhyeon-site.com', port=443): Failed to resolve 'www.onhyeon-site.com' ([Errno 11001] getaddrinfo failed)"))

--- [▶️ YouTube Test] Funnel 'national_pension' 테스트 시작 ---
[✅ Data Injection]: 링크 내부에 위험액 정보가 안전하게 포함됨.
[✅ Tracking Link Structure]: 예상 URL 생성 완료: https://analytics.example.com/track/?utm_source=youtube&funnel=national_pension&campaign=gap_cta&content=gap_cta
[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.


=============================================

--- [🌐 Web Test] Funnel 'health_insurance' 테스트 시작 ---
[⚠️ Data Injection WARN]: 데이터가 누락되었으나, CTA는 대체 텍스트를 안전하게 표시함.
[❌ Web Flow ERROR]: 네트워크/요청 실패: HTTPSConnectionPool(host='www.onhyeon-site.com', port=443): Max retries exceeded with url: /signup/submit (Caused by NameResolutionError("HTTPSConnection(host='www.onhyeon-site.com', port=443): Failed to resolve 'www.onhyeon-site.com' ([Errno 11001] getaddrinfo failed)"))

--- [▶️ YouTube Test] Funnel 'health_insurance' 테스트 시작 ---
[⚠️ Data Injection WARN]: 링크에 데이터 누락 대비 로직이 필요합니다.
[✅ Tracking Link Structure]: 예상 URL 생성 완료: https://analytics.example.com/track/?utm_source=youtube&funnel=health_insurance&campaign=gap_cta&content=gap_cta
[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.


=============================================

--- [🌐 Web Test] Funnel 'inheritance' 테스트 시작 ---
[✅ Data Injection]: 데이터 성공적으로 주입됨: 최소 3천만원 손실 우려
[❌ Web Flow ERROR]: 네트워크/요청 실패: HTTPSConnectionPool(host='www.onhyeon-site.com', port=443): Max retries exceeded with url: /signup/submit (Caused by NameResolutionError("HTTPSConnection(host='www.onhyeon-site.com', port=443): Failed to resolve 'www.onhyeon-site.com' ([Errno 11001] getaddrinfo failed)"))

--- [▶️ YouTube Test] Funnel 'inheritance' 테스트 시작 ---
[✅ Data Injection]: 링크 내부에 위험액 정보가 안전하게 포함됨.
[✅ Tracking Link Structure]: 예상 URL 생성 완료: https://analytics.example.com/track/?utm_source=youtube&funnel=inheritance&campaign=gap_cta&content=gap_cta
[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.

=============================================

[🚨 E2E 테스트 실패] 일부 필수 기능에서 오류가 감지되었습니다. 코드를 수정하고 재검증해야 합니다.
```
_✅_
