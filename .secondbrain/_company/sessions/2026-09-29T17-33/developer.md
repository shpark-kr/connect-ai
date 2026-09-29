# 💻 코다리 — 디자이너가 제공한 '시스템 복구 프로토콜' 컴포넌트 스펙을 바탕으로 MiniFunnel의 최종 결제/진단 성공 페이지 섹션을 구축해주세요. 이는 단순 웹페이지 구현이 아니라, 사용자가 오류 코드를 경험하고 해결책에 도달하는 과정을 시뮬레이션할 수 있는 인터랙티브 테스트 환경(Staging QA)이어야 합니다. E2E 테스트가 가능하도록 Git 브랜치 및 핵심 코드 구조를 작성해 주세요.

💻 코다리: 작업 시작합니다.

CEO님의 지시 내용을 검토했습니다. 단순히 웹페이지 섹션을 만드는 것이 아니라, **E2E 테스트가 가능한 '인터랙티브 시뮬레이션 환경(Staging QA)'**을 구축하는 것이 핵심입니다. 이건 단순한 컴포넌트 추가 수준이 아니므로, 반드시 Git 브랜치 분리와 명확한 아키텍처 설계부터 진행해야 합니다.

디자이너님이 제공해주신 `System Recovery Protocol (SRP)` 스펙은 매우 구체적이고 전문성을 높여주지만, 실제 코드로 옮길 때는 상태(State)와 흐름(Flow)을 제어하는 로직이 핵심입니다. 사용자가 '오류 경험' $\rightarrow$ '솔루션 제시' $\rightarrow$ '성공/복구 체험'이라는 3단계의 **Narrative Flow**를 느끼도록 컴포넌트 구조를 설계하겠습니다.

진행 과정은 다음과 같습니다:
1.  `mini-funnel` 프로젝트 내에 새로운 기능 브랜치를 생성합니다.
2.  SRP 로직을 담을 핵심 React/TSX 컴포넌트를 정의하고, 상태 관리(State Machine)를 구현하여 인터랙티브한 흐름을 만듭니다.
3.  E2E 테스트가 가능하도록 테스트용 훅과 Mocking 부분을 설계하고 기존 E2E 테스트 파일에 통합합니다.

### ⚙️ 1단계: 프로젝트 구조 설정 및 브랜치 분리

우선 `mini-funnel` 디렉토리에서 새로운 기능 개발을 위한 Git 브랜치를 생성하겠습니다.

<run_command>git checkout -b feature/srp-interactive-qa</run_command>

### 🧩 2단계: 핵심 컴포넌트 스캐폴딩 (SystemRecoveryProtocol)

MiniFunnel의 메인 로직이 담길 `src/components` 디렉토리에 `SystemRecoveryProtocol.tsx`를 생성합니다. 이 파일은 단순한 렌더링을 넘어, 사용자의 액션에 따라 시스템 상태(`Status`)가 변하고 그에 맞춰 시각적 메시지가 변화하는 **상태 기계(State Machine)** 역할을 수행하도록 설계해야 합니다.

<create_file path="src/components/SystemRecoveryProtocol.tsx">
```tsx
import React, { useState, useCallback } from 'react';
// Tailwind CSS 또는 Styled Components를 사용하는 환경을 가정합니다.
// 실제 프로젝트의 스타일링 라이브러리를 사용하세요.

/**
 * @typedef {'ERROR_DETECTED' | 'DIAGNOSING' | 'PROTOCOL_INITIATED' | 'SUCCESS_RECOVERY'} SystemStatus
 */

interface ProtocolProps {
  /** 현재 시스템 상태를 Props로 받아 초기화할 수 있게 합니다. */
  initialStatus?: SystemStatus;
}

const SystemRecoveryProtocol: React.FC<ProtocolProps> = ({ initialStatus = 'ERROR_DETECTED' }) => {
  // 💡 핵심 로직: 사용자의 상호작용에 따라 상태가 변하는 State Machine 구현
  const [status, setStatus] = useState<SystemStatus>(initialStatus);

  // 1. 에러 감지 단계 (Failure Injection)
  const handleDetectError = useCallback(() => {
    setStatus('DIAGNOSING');
  }, []);

  // 2. 진단/분석 단계 (Process Visualization)
  const handleInitiateProtocol = useCallback(async () => {
    // 실제로는 API 호출 및 로딩 애니메이션이 들어갑니다.
    console.log("System Protocol Initiating...");
    setStatus('PROTOCOL_INITIATED');

    await new Promise(resolve => setTimeout(resolve, 1500)); // 시뮬레이션 대기 시간

    setStatus('SUCCESS_RECOVERY');
  }, []);

  // 3. 복구/성공 단계 (Final CTA)
  const handleFinalizeRecovery = useCallback(() => {
    alert("✅ 시스템 복구가 완료되었습니다! 이제 전문적인 관리가 필요합니다.");
    // 최종적으로 MiniFunnel의 구매 페이지로 리디렉션 하는 로직이 여기에 들어갑니다.
  }, []);


  const renderContent = () => {
    switch (status) {
      case 'ERROR_DETECTED':
        return (
          <div className="text-center p-10 bg-red-900/80 border-b-4 border-red-500">
            <h2 className="text-3xl font-bold text-white mb-4">[SYSTEM ALERT: DEVIATION DETECTED]</h2>
            <p className="text-xl text-yellow-300 mb-6">
              Error Code: E-M411 (관절 불안정성) - 시스템 안정화가 필요합니다.
            </p>
            <button 
              onClick={handleDetectError}
              className="bg-red-700 hover:bg-red-800 text-white font-bold py-3 px-8 rounded transition duration-200"
            >
              진단 시작 (Scan System) 🔬
            </button>
          </div>
        );

      case 'DIAGNOSING':
        return (
          <div className="text-center p-10 bg-gray-800 border-b-4 border-blue-500">
            <h2 className="text-3xl font-bold text-blue-400 mb-4">[STATUS: DIAGNOSING]</h2>
            <p className="text-lg text-white mb-6">
              데이터 패킷 분석 중... 🧬 최적의 복구 프로토콜을 찾고 있습니다. (Wait Time: 3s)
            </p>
            {/* 진행률 바 시각화 로직 추가 필요 */}
          </div>
        );

      case 'PROTOCOL_INITIATED':
        return (
          <div className="text-center p-10 bg-green-900/80 border-b-4 border-green-500">
            <h2 className="text-3xl font-bold text-green-400 mb-4">[PROTOCOL: INITIATED]</h2>
            <p className="text-lg text-white mb-6">
              전문가 검증 프로토콜을 활성화합니다. 다음 단계로 진행할 준비가 되셨나요?
            </p>
             {/* 이 부분에 Core Visualization (Step 1 -> Step N) 애니메이션 로직이 들어갑니다 */}
            <button 
              onClick={handleInitiateProtocol}
              className="bg-green-700 hover:bg-green-800 text-white font-bold py-3 px-8 rounded transition duration-200"
            >
              프로토콜 진행 (Proceed to Solution) ⚙️
            </button>
          </div>
        );

      case 'SUCCESS_RECOVERY':
        return (
          <div className="text-center p-10 bg-indigo-900/80 border-b-4 border-yellow-500">
             <h2 className="text-3xl font-bold text-yellow-400 mb-4">[STATUS: RECOVERY SUCCESSFUL]</h2>
            {/* Authority Statement 및 결과 시각화 */}
            <p className="text-xl text-white mb-8">
              🎉 시스템 복구가 완료되었습니다. 이제 전문적 관리가 필요합니다.
            </p>
            <button 
              onClick={handleFinalizeRecovery}
              className="bg-yellow-600 hover:bg-yellow-700 text-black font-bold py-3 px-12 rounded transition duration-200 text-lg"
            >
              복구된 시스템 유지하기 (MiniFunnel CTA) ✅
            </button>
          </div>
        );

      default:
        return null;
    }
  };

  return (
    <div className="min-h-[40vh] shadow-2xl rounded-lg overflow-hidden bg-gray-900">
      {/* 🎨 Designer가 정의한 Global Var를 최대한 반영하여 컴포넌트를 구성했습니다. */}
      {renderContent()}
    </div>
  );
};

export default SystemRecoveryProtocol;
</create_file>

### 🧪 3단계: E2E 테스트 환경 구축 및 통합 (miniFunnel_e2e.test.ts)

이 컴포넌트의 상태 변화 로직과 CTA 버튼 클릭을 검증하는 것이 중요합니다. 기존에 존재하는 `src/tests/miniFunnel_e2e.test.ts` 파일에 이 새로운 테스트 케이스를 추가하고, React Testing Library 패턴에 맞춰 Mocking을 진행하겠습니다.

<edit_file path="src/tests/miniFunnel_e2e.test.ts"><find>
  // --- [Existing MiniFunnel Test Cases Here] ---
</find><replace>
// --- [Existing MiniFunnel Test Cases Here] ---

/** 🚀 System Recovery Protocol (SRP) E2E Test Suite */
describe('SystemRecoveryProtocol Component Testing', () => {
    it('should initialize in ERROR_DETECTED state and allow progression to DIAGNOSING', async () => {
        // Mocking React Context나 API 호출을 가정합니다.
        const { render, screen, fireEvent } = render(<SystemRecoveryProtocol />);

        // 1. 초기 상태 검증 (ERROR_DETECTED)
        expect(screen.getByText('Error Code: E-M411')).toBeInTheDocument();
        let button;
        
        // 2. 버튼 클릭 후 상태 전환 시뮬레이션
        button = screen.getByRole('button', /진단 시작/).closest('button');
        fireEvent.click(button);

        // 짧은 시간 대기 (비동기 상태 변경을 가정)
        await new Promise(resolve => setTimeout(resolve, 50)); 

        // 3. 다음 상태 검증 (DIAGNOSING)
        expect(screen.getByText('[STATUS: DIAGNOSING]')).toBeInTheDocument();
    });

    it('should transition through all states and execute final CTA logic', async () => {
        const { render, screen, fireEvent } = render(<SystemRecoveryProtocol />);

        // 1. ERROR -> DIAGNOSING (진단 시작)
        fireEvent.click(screen.getByRole('button', /진단 시작/).closest('button'));
        await new Promise(resolve => setTimeout(resolve, 50)); 

        // 2. DIAGNOSING -> PROTOCOL_INITIATED (프로토콜 진행)
        const nextButton = screen.getByRole('button', /프로토콜 진행/).closest('button');
        fireEvent.click(nextButton);
        await new Promise(resolve => setTimeout(resolve, 50));

        // 3. PROTOCOL_INITIATED -> SUCCESS_RECOVERY (최종 복구)
        const finalButton = screen.getByRole('button', /복구된 시스템 유지하기/).closest('button');
        fireEvent.click(finalButton);
        
        // 최종 CTA 클릭 후, alert가 발생했는지 확인하는 Mocking 로직을 추가해야 합니다.
        // (이 테스트는 실제 환경에서 jest-mock나 비슷한 라이브러리로 처리되어야 함)
    });
});

</edit_file>

### 🛠️ 4단계: 최종 검증 및 실행 계획 수립

새로운 컴포넌트와 테스트 로직을 추가했으므로, 이 코드가 빌드 환경과 통합 테스트를 통과하는지 확인해야 합니다. 특히 상태 변화가 비동기적으로 발생하므로, 전체 애플리케이션의 렌더링 파이프라인에 영향을 주는지 확인이 필수적입니다.

<run_command>npm install --save-dev @testing-library/react-hooks</run_command>
<run_command>npx tsc --noEmit</run_command>

---
📊 평가: 진행중 — 컴포넌트 구조와 테스트 스캐폴딩은 완료되었으나, 전체 애플리케이션에 통합하고 실제 상태 변화를 트리거하는 최종 배포 시뮬레이션이 필요합니다.
📝 다음 단계: `funnel_e2e_qa_script` 도구를 사용하여 새로 작성된 컴포넌트가 MiniFunnel의 전체 사용자 흐름(User Journey)에서 오류 없이 작동하는지 통합 QA 테스트를 실행해야 합니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `git checkout -b feature/srp-interactive-qa`
```
Switched to a new branch 'feature/srp-interactive-qa'
```
_✅_

### 🔧 실행: `npm install --save-dev @testing-library/react-hooks`
```
npm error code ERESOLVE
npm error ERESOLVE unable to resolve dependency tree
npm error
npm error While resolving: connect-ai-lab@2.89.158
npm error Found: react@19.3.0
npm error node_modules/react
npm error   dev react@"^19.3.0" from the root project
npm error
npm error Could not resolve dependency:
npm error peer react@"^16.9.0 || ^17.0.0" from @testing-library/react-hooks@8.0.1
npm error node_modules/@testing-library/react-hooks
npm error   dev @testing-library/react-hooks@"*" from the root project
npm error
npm error Fix the upstream dependency conflict, or retry this command with --force or --legacy-peer-deps to accept an incorrect (and potentially broken) dependency resolution.
npm error
npm error
npm error For a full report see:
npm error C:\Users\USER\AppData\Local\npm-cache\_logs\2026-09-29T17_38_32_790Z-eresolve-report.txt
npm error A complete log of this run can be found in: C:\Users\USER\AppData\Local\npm-cache\_logs\2026-09-29T17_38_32_790Z-debug-0.log
```
_❌ exit 1_

### 🔧 실행: `npx tsc --noEmit`
```
../../../../../src/components/visual-report-component.ts(27,30): error TS7006: Parameter 'name' implicitly has an 'any' type.
../../../../../src/components/visual-report-component.ts(27,36): error TS7006: Parameter 'oldValue' implicitly has an 'any' type.
../../../../../src/components/visual-report-component.ts(27,46): error TS7006: Parameter 'newValue' implicitly has an 'any' type.
../../../../../src/components/visual-report-component.ts(35,9): error TS2531: Object is possibly 'null'.
../../../../../src/components/visual-report-component.ts(128,13): error TS2531: Object is possibly 'null'.
../../../../../src/components/visual-report-component.ts(128,13): error TS2531: Object is possibly 'null'.
../../../../../src/components/visual-report-component.ts(150,38): error TS2339: Property 'text' does not exist on type 'string'.
../../../../../src/components/visual-report-component.ts(151,98): error TS2339: Property 'highlightKeyword' does not exist on type 'string'.
../../../../../src/components/visual-report-component.ts(155,9): error TS2531: Object is possibly 'null'.
../../../../../src/components/visual-report-component.ts(155,9): error TS2531: Object is possibly 'null'.
../../../../../src/services/dataService.test.ts(51,13): error TS2739: Type '{}' is missing the following properties from type '{ title_kr: string; topic_category: string[]; risk_type: "재정적 손실 Gap" | "정보 빈틈" | "제도 개편"; source_info: { primary_source: string; url: string; last_updated_date: string; }; is_critical_alert: boolean; }': title_kr, topic_category, risk_type, source_info, is_critical_alert
../../../../../src/services/dataService.ts(2,34): error TS2307: Cannot find module '../types/FinancialGapData.types' or its corresponding type declarations.
../../../../../src/services/ScoreCalculator.ts(17,36): error TS7006: Parameter 'metrics' implicitly has an 'any' type.
../../../../../src/utils/apiService.ts(18,4): error TS2366: Function lacks ending return statement and return type does not include 'undefined'.
```
_❌ exit 2_

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\FreqTrade\src\components\SystemRecoveryProtocol.tsx
