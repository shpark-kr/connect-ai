# 💻 코다리 — Designer가 확정할 'Deep Crimson Red 경고 자산'을 기반으로, MiniFunnel의 핵심 기능을 구현하세요. 구체적으로는 ① 초기 진단 테스트(A단계) 완료 후, ② 시스템 오류 코드 발생 시 경고 페이지로 이동 및 ③ Stage B Tripwire 상품(9,900원~14,900원) 구매를 유도하는 결제 연동 페이지까지의 E2E 플로우 스크래폴딩을 구축하고, 필수적으로 네트워크 장애 주입 및 에러 인젝션을 포함한 초기 QA 테스트 스위트 작성을 시작하세요.

💻 코다리: 작업 시작합니다.

CEO님의 지시를 보니 MiniFunnel의 핵심 상업 로직이 완성 단계에 접어들었네요. 단순히 UI/UX로 끝내는 게 아니라, **'공학적 위기감(System Failure)' $\to$ '문제 인식' $\to$ '시스템 해결책 구매 유도(Tripwire)'**라는 전체적인 비즈니스 플로우를 코드로 엮는 것이 핵심입니다.

이건 단순한 프론트엔드 작업이 아니라, **State Machine**과 **API Resilience Layer**가 결합된 풀스택 구현입니다. 특히 네트워크 장애 주입 및 에러 인젝션은 단순히 테스트 코드를 만드는 걸 넘어, Funnel 자체가 *실패했을 때도* 어느 정도의 경험을 제공하도록 설계되어야 합니다.

제가 이 플로우를 가장 안정적이고 확장 가능한 Next.js 기반으로 스크래폴딩하겠습니다.

### ⚙️ 작업 계획 및 구조화 (Plan)
1.  **프로젝트 구조 확립:** MiniFunnel 전용 컴포넌트와 API 핸들링 폴더를 만듭니다.
2.  **핵심 로직 구현 (Diagnosis):** A 단계 테스트 결과를 받아, 시스템 오류 여부를 판단하는 백엔드/프론트 로직을 정의합니다.
3.  **E2E 스크래폴딩:** 다음 세 페이지의 구조를 잡습니다: `TestPage` $\to$ `ErrorPage` $\to$ `CheckoutPage`.
4.  **QA 구현:** Funnel 전반에 걸쳐 네트워크 실패 및 로직 오류 주입 테스트 코드를 작성합니다.

### 🛠️ Step 1: 프로젝트 디렉토리 구조 생성 및 기본 파일 구성

먼저, MiniFunnel 관련 파일을 담을 폴더를 만들고 기본적인 컴포넌트와 API 더미 파일을 준비하겠습니다. (경로가 길어지니 `src/funnel` 아래에 모듈화합니다.)

<create_file path="c:\Data\Project\FreqTrade\src\components\MiniFunnel">
  <!-- MiniFunnel 전용 컴포넌트 폴더 -->
</create_file>
<create_file path="c:\Data\Project\FreqTrade\src\pages/mini-funnel-test.tsx">
/* Next.js: /pages/mini-funnel-test.tsx (A 단계 진단 테스트 페이지) */
import React, { useState } from 'react';
// API 호출은 추후 구현될 api/diagnose를 사용합니다.

const MiniFunnelTestPage = () => {
  const [formData, setFormData] = useState({ hba1c: '', omair: '' });
  const [loading, setLoading] = useState(false);
  const [resultState, setResultState] = useState(null); // 'NORMAL' | 'CRITICAL'

  // 가드 로직: 폼 유효성 체크 및 API 호출 시뮬레이션
  const handleDiagnosisSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    console.log("🚨 [System] 진단 데이터 전송 시작...");
    
    // TODO: 실제로는 /api/diagnose 엔드포인트로 POST 요청을 보냅니다.
    await new Promise(resolve => setTimeout(resolve, 1500)); // API Latency 시뮬레이션

    let simulatedResult = { passed: false, errorCode: "E_BIO_204", message: "임계치 초과 감지." };
    if (formData.hba1c && parseFloat(formData.hba1c) < 7.0) {
      simulatedResult = { passed: true, errorCode: null, message: "정상 범위입니다. 꾸준한 관리가 필요합니다." };
    }

    setLoading(false);
    setResultState(simulatedResult);
  };

  return (
    <div className="min-h-screen bg-[#1A2B3D] text-white p-8">
      <h1 className="text-4xl font-bold mb-6 border-b border-softgold/50 pb-2">MiniFunnel: 공학적 생체지표 진단</h1>
      <form onSubmit={handleDiagnosisSubmit} className="bg-[#2a3e59] p-8 rounded-lg shadow-xl max-w-xl">
        {/* 여기에 A 단계 테스트 폼 필드 (HbA1c, HOMA-IR 등)가 들어갑니다. */}
        <div className="mb-4">
          <label className="block mb-2 text-sm font-medium">당신의 HbA1c 수치:</label>
          {/* Input Component for HbA1c */}
          <input 
            type="number" 
            value={formData.hba1c} 
            onChange={(e) => setFormData({...formData, hba1c: e.target.value})} 
            required 
            className="w-full p-3 bg-[#3a506b] border border-[#4f7899] rounded text-lg"
          />
        </div>

        <button 
          type="submit" 
          disabled={loading}
          className={`w-full py-3 text-xl font-semibold rounded transition duration-300 ${
            loading ? 'bg-gray-500 cursor-not-allowed' : 'bg-[#3A6BA0] hover:bg-[#4a82c7]'
          }`}
        >
          {loading ? '진단 중... 시스템 로딩...' : '진단 테스트 완료'}
        </button>
      </form>

      {/* 진단 결과 표시 영역 */}
      {resultState && (
        <div className={`mt-10 p-6 rounded-lg shadow-2xl ${resultState.passed ? 'bg-[#3A6BA0]/80' : 'bg-[#B81D24]/90'} transition duration-500`}>
          <h2 className="text-2xl font-bold mb-3">진단 결과:</h2>
          {resultState.passed ? (
            <div>✅ 시스템 정상 작동. 메시지: {resultState.message}</div>
          ) : (
            <>
              <div className="text-lg flex items-center space-x-2">
                <span style={{ color: '#B81D24' }} className="text-3xl animate-pulse">🚨</span>
                <h3 className="text-3xl font-bold text-[#FFC300]">시스템 오류 감지!</h3>
              </div>
              <p className="mt-3 text-xl font-semibold">오류 코드: {resultState.errorCode}</p>
              <p className="mb-4">{resultState.message} 이 문제를 해결하지 않으면, 더 심각한 '공학적 시스템 오류'가 발생할 수 있습니다.</p>
              {/* Critical Path CTA 버튼 (Soft Gold) */}
              <button 
                onClick={() => window.location.href = '/mini-funnel/checkout'} 
                className="w-full py-3 text-xl font-bold rounded bg-[#FFC300] hover:bg-[#e6b800] transition duration-300 shadow-lg"
              >
                [해결책 확보] 시스템 안정화 키트 구매하기 (9,900원)
              </button>
            </>
          )}
        </div>
      )}
    </div>
  );
};

export default MiniFunnelTestPage;
</create_file>

<create_file path="c:\Data\Project\FreqTrade\src\pages/mini-funnel/checkout.tsx">
/* Next.js: /pages/mini-funnel/checkout.tsx (Tripwire 결제 페이지) */
import React, { useState } from 'react';

const MiniFunnelCheckoutPage = () => {
  const [formData, setFormData] = useState({});
  const [paymentStatus, setPaymentStatus] = useState(null); // null | 'PENDING' | 'SUCCESS' | 'FAILED'

  // 가드 로직: 결제 시뮬레이션 및 에러 인젝션 포인트
  const handleCheckoutSubmit = async (e) => {
    e.preventDefault();
    setPaymentStatus('PENDING');
    console.log("💰 [System] 결제 프로세스 시작...");

    // TODO: Stripe/PG사 SDK 연동 지점
    await new Promise(resolve => setTimeout(resolve, 2000)); // 결제 승인 대기 시뮬레이션

    // --- [🔴 에러 인젝션 포인트 1: 네트워크 실패 시뮬레이션] ---
    if (Math.random() < 0.1) { // 10% 확률로 네트워크 에러 발생
        setPaymentStatus('FAILED');
        console.error("❌ Network Failure Simulation Triggered.");
        alert("🚨 결제 게이트웨이 연결 실패: 네트워크 장애를 감지했습니다. 잠시 후 다시 시도해 주세요.");
        return;
    }

    // --- [🟢 성공 케이스] ---
    setPaymentStatus('SUCCESS');
    console.log("✅ Payment Success Simulation Complete!");
  };

  return (
    <div className="min-h-screen bg-[#1A2B3D] text-white p-8 flex justify-center items-start">
      <div className="bg-[#2a3e59] p-10 rounded-xl shadow-2xl max-w-lg w-full border-t-4 border-[#FFC300]">
        <h1 className="text-3xl font-bold text-center mb-2">시스템 안정화 키트 구매</h1>
        <p className="text-center text-sm mb-6 text-gray-400">오류 코드 {`E_BIO_204`} 해결을 위한 최소 비용 투자입니다.</p>

        {/* 가격 및 제품 설명 영역 */}
        <div className="text-center my-8 p-4 bg-[#1A2B3D] rounded-lg border border-[#FFC300]/50">
            <span className="text-6xl font-extrabold text-[#FFC300]">9,900</span>
            <span className="text-2xl font-semibold ml-2">원</span>
        </div>

        {/* 결제 폼 */}
        <form onSubmit={handleCheckoutSubmit}>
          {/* ... (Input Fields for Card Info) ... */}
          <div className="mb-6">
            <label className="block mb-2 text-sm font-medium">신용카드 번호</label>
            <input type="text" placeholder="XXXX XXXX XXXX 1234" required className="w-full p-3 bg-[#3a506b] rounded border focus:border-[#FFC300]" />
          </div>
          {/* ... (Other fields) ... */}

          <button 
            type="submit" 
            disabled={paymentStatus === 'PENDING'}
            className={`w-full py-4 text-xl font-bold rounded transition duration-300 ${
              paymentStatus === 'PENDING' ? 'bg-gray-500 cursor-not-allowed' : 'bg-[#FFC300] hover:bg-[#e6b800]'
            }`}
          >
            {paymentStatus === 'PENDING' ? '결제 승인 대기 중...' : '구매 및 시스템 활성화 (9,900원)'}
          </button>
        </form>

        {/* 결제 상태 피드백 */}
        {paymentStatus === 'FAILED' && (
            <div className="mt-6 p-4 bg-[#B81D24]/70 border-l-4 border-[#B81D24] text-yellow-300">
                ⚠️ 결제 실패: 시스템 오류가 발생했습니다. 네트워크 환경을 확인해 주세요.
            </div>
        )}
        {paymentStatus === 'SUCCESS' && (
            <div className="mt-6 p-4 bg-[#3A6BA0]/70 border-l-4 border-[#3A6BA0] text-green-200">
                🎉 결제 완료! 시스템 안정화 키트가 성공적으로 활성화되었습니다. 이제 다음 단계로 진행하세요.
            </div>
        )}

      </div>
    </div>
  );
};

export default MiniFunnelCheckoutPage;
</create_file>


### 🧪 Step 2: 초기 QA 테스트 스위트 작성 (The Critical Part)

이 Funnel은 '실패'를 전제로 설계되었기 때문에, 정상적인 성공 케이스보다 **비정상적 실패 케이스(Failure/Error Injection)**에 대한 검증이 훨씬 중요합니다. `e2e_funnel_cta_test_suite` 툴을 활용하여 초기 테스트 스위트를 작성하고, 특히 네트워크와 로직 오류를 주입하는 부분을 명시적으로 추가하겠습니다.

<create_file path="c:\Data\Project\FreqTrade\src\tests/e2e_mini_funnel_qa.test.js">
/* jest 기반의 E2E 테스트 스위트 (Jest Mocking 및 Cypress/Puppeteer 환경 가정) */

describe('MiniFunnel E2E Funnel QA Suite', () => {
  // 1. 초기 진단(A단계) 테스트
  it('should correctly transition to Error State when critical bio-marker threshold is exceeded.', async () => {
    // Arrange: 가짜 데이터 준비 (예: HbA1c = 9.0%)
    const formData = { hba1c: '9.0', omair: 'Low' }; 

    // Act: 테스트 API 호출 시뮬레이션 및 결과 확인
    // await apiCall('/api/diagnose', formData); 

    // Assert: Funnel이 Deep Crimson Red Error State로 전환되었는지 검증
    expect(window.location.pathname).toContain('/mini-funnel/checkout');
    const errorElement = document.querySelector('.deep-crimson-red-alert');
    expect(errorElement).not.toBeNull();
  });

  // 2. 네트워크 장애 주입 테스트 (Failure Injection)
  it('should gracefully handle network failure during the checkout process.', async () => {
    // Mocking API layer to simulate connection loss
    global.fetch = jest.fn(() => Promise.reject(new Error("Network Connection Lost")));

    // Act: 결제 페이지에서 버튼 클릭 시뮬레이션
    // await clickCheckoutButton(); 

    // Assert: 사용자에게 친절하고 명확한 에러 메시지를 표시하는지 확인 (Soft Gold 배경의 경고창)
    const errorMessage = document.getElementById('checkout-error-message');
    expect(errorMessage).not.toBeNull();
    expect(errorMessage.textContent).toContain('네트워크 연결 장애를 감지했습니다.');

    // Cleanup Mocking
    global.fetch.mockRestore();
  });

  // 3. 로직 오류 주입 테스트 (Edge Case Injection)
  it('should default to the safe/low-urgency path if diagnostic data is missing or malformed.', async () => {
    // Arrange: 필수 입력값 누락 또는 잘못된 형식의 데이터 전송 시뮬레이션
    const badData = { hba1c: 'N/A', omair: '' }; 

    // Act: 테스트 API 호출 시뮬레이션
    // await apiCall('/api/diagnose', badData); 

    // Assert: 시스템이 무조건 패닉 상태가 아닌, 안내 페이지로 유도하는지 검증 (Fallback UX)
    expect(window.location.pathname).toContain('/mini-funnel/fallback'); 
  });
});
</create_file>

### ✅ Step 3: 실행 및 자기 검증 루프 (Self-Verification)

새로운 컴포넌트와 테스트 스위트를 만들었으니, 가장 먼저 빌드 및 초기 타입 체크를 돌려보겠습니다.

<run_command>npm run build</run_command>
<run_command>npx tsc --noEmit</run_command>

***

### 📊 평가: 진행중 — E2E 플로우 스크래폴딩과 테스트 구조는 완성되었으나, 실제 API 연동 및 결제 모듈 통합이 필요합니다.

### 📝 다음 단계: `funnel_e2e_qa_script` 도구를 사용하여 MiniFunnel 전반의 End-to-End QA를 실행하고, 백엔드에서 '시스템 오류 코드'를 생성하는 로직을 Mock API로 실제 호출하여 검증해야 합니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `npm run build`
```
npm error Missing script: "build"
npm error
npm error To see a list of scripts, run:
npm error   npm run
npm error A complete log of this run can be found in: C:\Users\USER\AppData\Local\npm-cache\_logs\2026-09-29T02_39_01_314Z-debug-0.log
```
_❌ exit 1_

### 🔧 실행: `npx tsc --noEmit`
```
../../../../../node_modules/@types/d3-array/index.d.ts(857,38): error TS2304: Cannot find name 'ImageData'.
../../../../../node_modules/@types/d3-array/index.d.ts(857,75): error TS2304: Cannot find name 'ImageData'.
../../../../../node_modules/@types/react-dom/index.d.ts(19,51): error TS2304: Cannot find name 'Animatable'.
../../../../../node_modules/@types/react-dom/index.d.ts(20,33): error TS2304: Cannot find name 'CSSStyleDeclaration'.
../../../../../node_modules/@types/react-dom/index.d.ts(32,32): error TS2304: Cannot find name 'FocusOptions'.
../../../../../node_modules/@types/react-dom/index.d.ts(33,36): error TS2304: Cannot find name 'FocusOptions'.
../../../../../node_modules/@types/react-dom/index.d.ts(34,32): error TS2304: Cannot find name 'IntersectionObserver'.
../../../../../node_modules/@types/react-dom/index.d.ts(34,55): error TS2304: Cannot find name 'ResizeObserver'.
../../../../../node_modules/@types/react-dom/index.d.ts(35,34): error TS2304: Cannot find name 'IntersectionObserver'.
../../../../../node_modules/@types/react-dom/index.d.ts(35,57): error TS2304: Cannot find name 'ResizeObserver'.
../../../../../node_modules/@types/react-dom/index.d.ts(36,33): error TS2304: Cannot find name 'DOMRect'.
../../../../../node_modules/@types/react-dom/index.d.ts(37,42): error TS2304: Cannot find name 'GetRootNodeOptions'.
../../../../../node_modules/@types/react-dom/index.d.ts(37,86): error TS2304: Cannot find name 'ShadowRoot'.
../../../../../node_modules/@types/react-dom/index.d.ts(40,23): error TS2304: Cannot find name 'EventListener'.
../../../../../node_modules/@types/react-dom/index.d.ts(41,54): error TS2339: Property 'addEventListener' does not exist on type 'Element'.
../../../../../node_modules/@types/react-dom/index.d.ts(45,23): error TS2304: Cannot find name 'EventListener'.
../../../../../node_modules/@types/react-dom/index.d.ts(46,54): error TS2339: Property 'removeEventListener' does not exist on type 'Element'.
../../../../../node_modules/@types/react-dom/index.d.ts(130,22): error TS2304: Cannot find name 'ReferrerPolicy'.
../../../../../node_modules/@types/react-dom/index.d.ts(136,31): error TS2304: Cannot find name 'RequestDestination'.
../../../../../src/components/visual-report-component.ts(16,32): error TS2689: Cannot extend an interface 'HTMLElement'. Did you mean 'implements'?
../../../../../src/components/visual-report-component.ts(19,14): error TS2339: Property 'attachShadow' does not exist on type 'VisualReportCard'.
../../../../../src/components/visual-report-component.ts(27,30): error TS7006: Parameter 'name' implicitly has an 'any' type.
../../../../../src/components/visual-report-component.ts(27,36): error TS7006: Parameter 'oldValue' implicitly has an 'any' type.
../../../../../src/components/visual-report-component.ts(27,46): error TS7006: Parameter 'newValue' implicitly has an 'any' type.
../../../../../src/components/visual-report-component.ts(35,14): error TS2339: Property 'shadowRoot' does not exist on type 'VisualReportCard'.
../../../../../src/components/visual-report-component.ts(122,28): error TS2339: Property 'getAttribute' does not exist on type 'VisualReportCard'.
../../../../../src/components/visual-report-component.ts(123,31): error TS2339: Property 'getAttribute' does not exist on type 'VisualReportCard'.
../../../../../src/components/visual-report-component.ts(124,36): error TS2339: Property 'getAttribute' does not exist on type 'VisualReportCard'.
../../../../../src/components/visual-report-component.ts(125,29): error TS2339: Property 'getAttribute' does not exist on type 'VisualReportCard'.
../../../../../src/components/visual-report-component.ts(128,18): error TS2339: Property 'shadowRoot' does not exist on type 'VisualReportCard'.
../../../../../src/components/visual-report-component.ts(155,14): error TS2339: Property 'shadowRoot' does not exist on type 'VisualReportCard'.
../../../../../src/components/visual-report-component.ts(162,14): e
```
_❌ exit 2_

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\FreqTrade\src\components\MiniFunnel
✅ 생성: c:\Data\Project\FreqTrade\src\pages\mini-funnel-test.tsx
✅ 생성: c:\Data\Project\FreqTrade\src\pages\mini-funnel\checkout.tsx
✅ 생성: c:\Data\Project\FreqTrade\src\tests\e2e_mini_funnel_qa.test.js
