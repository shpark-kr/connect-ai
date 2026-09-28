# 💻 코다리 — Developer는 Designer가 제작할 최종 애니메이션 에셋을 전제로, MiniFunnel.tsx 모듈의 E2E 테스트 환경 구축을 최우선 과제로 삼으세요. 핵심은 '네트워크 불안정성 시뮬레이션'과 'Designer가 제공할 애니메이션 컴포넌트와의 통합(Integration)'입니다. API 호출 실패, 재시도 로직, 그리고 최종 애니메이션 트랜지션이 모두 결합된 종합적인 검증 테스트 스크립트를 작성하고, 테스트 케이스 매트릭스를 완성하여 다음 개발 사이클에 대비해야 합니다.

💻 코다리: 작업 시작합니다.

CEO님의 지시를 받았습니다. MiniFunnel의 E2E 테스트 환경 구축은 단순히 버그를 찾는 것을 넘어, **시스템 복원력(Resilience)**과 **경험적 완성도(Experiential Fidelity)**를 확보하는 핵심 단계입니다. 특히 '네트워크 불안정성' 시뮬레이션과 Designer가 만든 '애니메이션 트랜지션' 결합 검증은 일반적인 단위 테스트 스코프를 벗어납니다.

테스트 케이스 매트릭스와 함께, 이 복잡한 로직을 통합하기 위한 개념적인 테스트 환경 구조(Mocking + State Control)를 먼저 설계하겠습니다. 실제 코드는 다음 사이클에 작성하되, 지금은 **검증 가능한 아키텍처 정의**가 우선입니다.

---

### ⚙️ MiniFunnel E2E Test Harness 설계 및 검증 계획

MiniFunnel 테스트는 단일 모듈 단위 테스트로 접근할 수 없습니다. 데이터 흐름(API $\to$ State Change $\to$ UI Render $\to$ Animation) 전반에 걸친 **통합 시퀀스 테스트**가 필수입니다. 이를 위해 React Testing Library와 Jest의 `mocking` 기능을 최대한 활용하여, 네트워크 요청과 상태 변화를 강제할 수 있는 환경을 구축해야 합니다.

#### 1. 핵심 테스트 모듈 구조 (`MiniFunnelTestHarness.tsx`)
실제 개발 시 이 파일이 기준이 됩니다. 우리는 API 호출 자체를 Mock 처리하고, 성공/실패 여부와 애니메이션의 상태 변수(e.g., `isCrisisMode`, `isLoading`)를 직접 주입하며 테스트해야 합니다.

```typescript
// src/components/MiniFunnelTestHarness.tsx (Conceptual File)
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import MiniFunnel from './MiniFunnel'; // 실제 Funnel 컴포넌트 경로

// 🚨 Mocking 설정: 모든 API 호출을 가로채서 제어합니다.
jest.mock('../api/diagnosisEngine', () => ({
  runDiagnosis: jest.fn(),
}));

describe('E2E MiniFunnel Resilience and Animation Test Suite', () => {
  const mockRunDiagnosis = require('../api/diagnosisEngine').runDiagnosis;

  // ----------------------------------------------------
  // [Test Group 1] Network Resilience Testing (API Failure)
  // ----------------------------------------------------
  test('should handle API failure and display graceful fallback state', async () => {
    // Arrange: 최초 호출 시 네트워크 에러 강제 발생 Mocking
    mockRunDiagnosis.mockRejectedValue(new Error("Network Timeout or Service Unavailable"));

    render(<MiniFunnel initialData={null} />);

    // Act & Assert: 로딩 상태 확인 후, 실패 메시지와 재시도 버튼이 보이는지 검증
    expect(screen.getByText(/네트워크 연결에 문제가 발생했습니다/i)).toBeInTheDocument();
    await waitFor(() => expect(screen.getByRole('button', { name: /다시 시도/i })).toBeInTheDocument());
  });

  test('should successfully retry after initial failure (Circuit Breaker logic)', async () => {
    // Arrange: 1회차는 실패, 2회차는 성공하도록 Mocking 설정
    mockRunDiagnosis.mockRejectedValueOnce(new Error("Temporary API Failure"));
    mockRunDiagnosis.mockResolvedValueOnce({ homaIr: 'Normal', status: 'Safe' });

    render(<MiniFunnel initialData={null} />);

    // Act & Assert: 실패 후 재시도 로직이 발동하고, 최종적으로 성공 상태를 보여주는지 확인
    await waitFor(() => {
      expect(screen.getByText(/정상 범위입니다/i)).toBeInTheDocument();
    });
  });

  // ----------------------------------------------------
  // [Test Group 2] Animation & State Transition Testing (Designer Integration)
  // ----------------------------------------------------
  test('should trigger Deep Crimson Red warning on crisis state and maintain animation integrity', async () => {
    // Arrange: 위험 수치 데이터 주입 Mocking
    mockRunDiagnosis.mockResolvedValueOnce({ homaIr: 'HighRisk', status: 'Crisis' });

    render(<MiniFunnel initialData={null} />);

    // Act & Assert 1: Deep Crimson Red 경고 UI가 정확히 나타나는지 확인 (CSS/SVG 기반)
    await waitFor(() => {
      const crisisIndicator = screen.getByTestId('crisis-indicator'); // Test ID 사용 가정
      expect(crisisIndicator).toHaveStyle('background-color: #B92F2F;'); 
      // 추가 검증: A-01 Pulse Effect가 적용되었는지 (CSS Keyframes 확인)
    });

    // Act & Assert 2: Soft Gold 전환 시 애니메이션이 부드럽게 해제되는지 확인
    // 이 부분은 상태 변화 핸들러를 강제로 호출하여 테스트해야 함.
    // 예시: setAnimationState('SoftGold'); -> UI가 재렌더링될 때만 검증 가능
  });

  // ----------------------------------------------------
  // [Test Group 3] Comprehensive E2E Funnel Flow Test
  // ----------------------------------------------------
  test('should complete the full funnel flow: Crisis detection -> Solution display -> CTA engagement', async () => {
    // Mocking으로 모든 단계 통과 시나리오 설정
    mockRunDiagnosis.mockResolvedValueOnce({ homaIr: 'HighRisk', status: 'Crisis' });

    render(<MiniFunnel initialData={null} />);

    // 1. Crisis State 확인 (Deep Crimson Red)
    await waitFor(() => expect(screen.getByTestId('crisis-indicator')).toBeVisible());

    // 2. 해결책 버튼 클릭 시뮬레이션 (Soft Gold 전환 트리거)
    const solutionButton = screen.getByRole('button', { name: /해결책 알아보기/i });
    solutionButton.click();

    // 3. 최종 CTA 유도 상태 확인
    await waitFor(() => expect(screen.getByText(/솔루션 패키지 구매하기/i)).toBeVisible());
  });
});
```

#### 2. MiniFunnel E2E 테스트 케이스 매트릭스 (Test Case Matrix)

이 표는 우리가 개발 사이클에서 반드시 커버해야 할 **최소한의 검증 범위를 정의**합니다. 이 매트릭스가 곧 우리의 요구사항 명세서입니다.

| No. | Test Scope | Pre-Condition / Input State | Expected Action Triggered | Validation Criteria (Success/Failure) | Priority |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **[A]** | **API Failure & Retry** | Initial state, API Mock = Timeout | Funnel 1단계 로딩 $\to$ 에러 UI 표시 | 1. 실패 메시지 노출 (Deep Crimson Red 배경). <br>2. '재시도' 버튼 활성화 및 클릭 가능 여부 확인. | P1 (Critical) |
| **[B]** | **API Resilience** | Initial state, API Mock = Fail $\to$ Success | Funnel 1단계 로딩 $\to$ 실패 $\to$ 재시도 $\to$ 성공 | 1. 최대 시도 횟수(N회) 초과 시 폴백 메시지 노출 (Timeout/Circuit Breaker). <br>2. N회차에 성공하면 Soft Gold 상태로 정상 진입. | P1 (Critical) |
| **[C]** | **Crisis Animation Trigger** | Input Data = HOMA-IR > Threshold | Funnel 2단계: 위험 경고 활성화 | 1. A-01 Pulse Effect가 정확히 작동하는지 (CSS Keyframes). <br>2. A-02 Glitch/Shake Effect가 위기감 최고조에 도달하도록 연출되는지. | P1 (Critical) |
| **[D]** | **State Transition Animation** | Funnel 2단계 $\to$ Soft Gold Solution Click | Funnel 3단계: 해결책 제시 | 1. Deep Crimson Red $\to$ Soft Gold 전환이 끊김 없이 부드럽게 이루어지는지 (Keyframe Interpolation). <br>2. 애니메이션 트랜지션 시간(Time duration) 준수 여부. | P1 (Critical) |
| **[E]** | **Empty/Normal State Flow** | Input Data = HOMA-IR $\le$ Threshold | Funnel 2단계: 정상 정보 제공 | 1. 위기 경고 UI가 전혀 노출되지 않아야 함. <br>2. 콘텐츠 흐름이 매끄럽게 진행되며 CTA로 자연스럽게 유도되는지. | P2 (High) |
| **[F]** | **Device Viewport Check** | Mobile/Tablet Emulator 환경 | 전체 Funnel Flow | 1. 모든 애니메이션과 UI 요소가 반응형으로 깨지지 않고 정상적으로 스케일링 되는지. <br>2. CTA 버튼이 화면 하단에 항상 고정(Sticky)되는지. | P2 (High) |

---
### ✅ 결론 및 다음 단계 조치

테스트 코드는 상기 매트릭스를 기반으로 작성되어야 하며, 특히 **[B] API Resilience**와 **[D] State Transition Animation** 부분이 가장 까다롭습니다. 이 두 가지를 통합적으로 검증하기 위해 기존에 준비된 전문 테스트 도구를 한 번 실행하여 시스템이 요구되는 모듈 구조를 갖추고 있는지 확인하는 것이 안전합니다.

<run_command>cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe e2e_funnel_cta_test_suite.py</run_command>

📊 평가: 진행중 — E2E 테스트 스크립트 구조 정의와 필수 검증 매트릭스 작성이 완료되었으며, 실제 구현을 위한 초기 도구 실행이 필요합니다.
📝 다음 단계: `e2e_funnel_cta_test_suite` 실행 결과를 분석하여, 현재 Funnel의 어떤 부분이 가장 큰 테스트 공백(Gap)인지 파악하고, 해당 부분에 초점을 맞춰 MiniFunnel 컴포넌트의 로직을 수정/보강해야 합니다.

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
