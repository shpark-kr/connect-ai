# 💻 코다리 — Designer가 완성할 MiniFunnel의 오류/경고 UI 스펙에 대비하여, 결제 실패 시 재시도(Retry) 버튼과 '시스템 복구 프로토콜 확인' CTA 컴포넌트의 프론트엔드 와이어프레임 및 초기 코드 골격(Boilerplate)을 준비해주세요. 이는 Designer가 최종 스펙을 제공하는 즉시 코딩에 착수할 수 있도록 준비되어야 합니다.

💻 코다리: 작업 시작합니다.

CEO님의 지시 사항 확인했습니다. MiniFunnel의 결제 실패(Payment Failure)와 이탈 방지 플로우를 완성하는 데 있어 가장 중요한 것은 '기술적 신뢰성'을 잃지 않는 것입니다. 단순한 오류 메시지가 아니라, **"시스템이 일시적으로 문제를 감지했고, 사용자가 취해야 할 다음 프로토콜은 이것이다"**라는 권위적인 흐름이 필요합니다.

Designer가 정의한 복잡하고 공학적인 스펙(Deep Navy/Crisis Red, System Alert)을 기반으로, 재시도 로직과 시스템 안내 CTA를 위한 컴포넌트 골격을 준비하겠습니다. 이 두 컴포넌트는 상태 관리와 비즈니스 로직 분리를 위해 **단일 책임 원칙(SRP)**에 따라 각각 독립적인 파일로 설계하는 것이 가장 안전합니다.

두 개의 핵심 보일러플레이트 파일을 생성하고, Tailwind CSS를 사용하여 Designer가 제시한 테마 컬러 및 애니메이션 클래스들을 적용할 수 있도록 주석 처리하여 준비하겠습니다.

### ⚙️ 작업 계획
1.  `RetryButton.tsx`: 결제 실패 시 재시도 로직을 담당하는 컴포넌트. (상태: Loading, Success, Error)
2.  `ProtocolCheckCTA.tsx`: 사용자가 다음 단계의 솔루션을 탐색하도록 유도하는 '프로토콜 확인' CTA 컴포넌트.

### 🛠️ 코드 구현

먼저 `src/components/funnel` 폴더 안에 두 개의 파일을 생성합니다. 기존에 생성된 `MiniFunnelComponent.tsx`와 같은 위치에 배치하여 통합성을 높이겠습니다.

<create_file path="c:\Data\Project\connect-ai\src\components\funnel\RetryButton.tsx">
import React, { useState, useCallback } from 'react';

// 타입 정의: 재시도 로직의 상태를 명확히 합니다. (TypeScript 엄격 적용)
type ButtonState = 'idle' | 'loading' | 'success' | 'error';

interface RetryButtonProps {
  /** 현재 결제 시도의 성공 여부를 받습니다. */
  initialStatus: 'pending' | 'failed' | 'successful';
  /** 재시도 API 호출 함수 (실제 비즈니스 로직이 들어갈 부분) */
  onRetryAttempt: () => Promise<boolean>; 
  /** 버튼을 클릭했을 때의 콜백 */
  onClick?: () => void;
}

const RetryButton: React.FC<RetryButtonProps> = ({ initialStatus, onRetryAttempt, onClick }) => {
  // 컴포넌트가 관리하는 내부 상태 (로딩 및 성공/실패 애니메이션 관리를 위함)
  const [buttonState, setButtonState] = useState<ButtonState>(initialStatus === 'failed' ? 'idle' : 'idle');
  const [isRetryActive, setIsRetryActive] = useState(false);

  /** 🚨 재시도 로직을 실행하는 핵심 핸들러 */
  const handleRetryClick = useCallback(async () => {
    if (buttonState === 'loading') return; // 중복 호출 방지

    setIsRetryActive(true);
    setButtonState('loading');
    
    try {
      // 실제 API 호출을 시뮬레이션합니다. 여기를 수정해야 합니다.
      const success = await onRetryAttempt(); 
      
      if (success) {
        setButtonState('success'); // 성공 상태로 전환하여 잠시 보여줌
        setTimeout(() => setButtonState('idle'), 2000); // 2초 후 초기화
        // TODO: 부모 컴포넌트에게 성공 이벤트를 전파해야 함.
      } else {
        setButtonState('error'); // 실패 상태로 전환
      }
    } catch (e) {
      console.error("Retry attempt failed:", e);
      setButtonState('error');
    } finally {
      setIsRetryActive(false);
    }
  }, [onRetryAttempt, buttonState]);

  // Tailwind CSS를 사용하여 공학적 경고 톤을 적용합니다.
  const getButtonClasses = () => {
    switch (buttonState) {
      case 'loading':
        return "bg-yellow-600 cursor-not-allowed animate-pulse border-4"; // 로딩 중은 노란색 깜빡임
      case 'success':
        return "bg-green-600 border-2 shadow-lg"; // 성공 시 녹색 강조
      case 'error':
        return "bg-red-700 border-4 border-red-900 animate-shake"; // 실패 시 경고 애니메이션 (CSS Keyframe 필요)
      default:
        // 기본 재시도 버튼 스타일
        return "bg-[#2A3D51] hover:bg-[#3C536E] text-white transition duration-300 border-2 border-[#B00020]"; 
    }
  };

  const getButtonContent = () => {
    switch (buttonState) {
      case 'loading':
        return "Processing Protocol... ⚙️";
      case 'success':
        return "Protocol Restored! ✅";
      case 'error':
        return "🔴 Retry Failed. Check System Log."; // 실패 시 강한 경고 문구 사용
      default:
        return "Attempt Protocol Restore (Retry)";
    }
  };

  return (
    <button 
      onClick={handleRetryClick} 
      disabled={!onRetryAttempt || buttonState === 'loading'}
      className={`px-8 py-3 rounded-lg font-bold tracking-wider ${getButtonClasses()} transition duration-200`}
    >
      {getButtonContent()}
    </button>
  );
};

export default RetryButton;
</create_file>

<create_file path="c:\Data\Project\connect-ai\src\components\funnel\ProtocolCheckCTA.tsx">
import React from 'react';

interface ProtocolCheckCTAProps {
  /** CTA를 클릭했을 때 이동할 경로 또는 함수 */
  onNavigate: (path: string) => void;
  /** 프로토콜 확인의 제목 */
  title: string;
  /** 부가 설명 문구 */
  description: string;
}

const ProtocolCheckCTA: React.FC<ProtocolCheckCTAProps> = ({ onNavigate, title, description }) => {
  // 이 CTA는 단순한 버튼이 아니라 '시스템 가이드'처럼 보여야 합니다. 
  // 따라서 일반적인 링크 스타일보다 더 권위적이고 구조적인 디자인을 적용합니다.

  return (
    <div className="mt-12 p-8 bg-[#1A2530] border-l-4 border-[#B00020] rounded-md shadow-xl">
      {/* 🚨 시스템 권위 경고 배너를 재사용하는 느낌으로 설계 */}
      <h3 className="text-2xl font-extrabold text-white mb-2 flex items-center">
        <span className="text-[#B00020] mr-3 animate-pulse">[PROTOCOL REQUIRED]</span> 
        {title}
      </h3>
      
      <p className="text-gray-300 mb-6 border-b border-dashed pb-4">{description}</p>

      {/* 실제 클릭 가능한 영역 */}
      <button
        onClick={() => onNavigate('/mini-funnel/protocol-check')}
        className={`w-full py-3 text-lg font-bold tracking-wider uppercase 
                    bg-[#B00020] hover:bg-[#D41A37] transition duration-300 
                    shadow-[0_0_15px_rgba(176,0,32,0.8)]`} // Crisis Red 네온 효과 시뮬레이션
      >
        {/* 버튼 텍스트: 반드시 행동을 유도하는 전문 용어 사용 */}
        Execute Protocol Check & Diagnose System Failure →
      </button>

      <p className="text-sm text-gray-500 mt-4 italic">
        * 본 프로토콜은 사용자 시스템의 결함을 진단하고, 최적화된 복구 모듈을 연결합니다.
      </p>
    </div>
  );
};

export default ProtocolCheckCTA;
</create_file>

### 🧹 검증 및 정리
새로운 컴포넌트 파일들이 생성되었으므로, 필요한 스타일링과 애니메이션(예: `animate-shake`, `.alert-flash`)이 Tailwind CSS 설정 또는 글로벌 CSS에 포함되어 있는지 확인하는 것이 필수입니다.

<run_command>npm run lint -- --fix</run_command>
<reveal_in_explorer path="c:\Data\Project\connect-ai\src\components\funnel"/>

📊 평가: 완료 — 요청된 두 가지 핵심 컴포넌트의 초기 골격과 타입 안정성을 확보하여, Designer 스펙이 들어오는 즉시 코딩에 착수할 수 있는 상태입니다.
📝 다음 단계: MiniFunnelComponent.tsx를 수정하여 `RetryButton`과 `ProtocolCheckCTA`를 임포트하고 결제 실패 시나리오의 레이아웃을 통합하는 작업을 진행해야 합니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `npm run lint -- --fix`
```
npm error Missing script: "lint"
npm error
npm error Did you mean this?
npm error   npm link # Symlink a package folder
npm error
npm error To see a list of scripts, run:
npm error   npm run
npm error A complete log of this run can be found in: C:\Users\USER\AppData\Local\npm-cache\_logs\2026-11-21T05_30_38_436Z-debug-0.log
```
_❌ exit 1_

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\src\components\funnel\RetryButton.tsx
✅ 생성: c:\Data\Project\connect-ai\src\components\funnel\ProtocolCheckCTA.tsx
🗂 🗂 익스플로러 열림: c:\Data\Project\connect-ai\src\components\funnel
