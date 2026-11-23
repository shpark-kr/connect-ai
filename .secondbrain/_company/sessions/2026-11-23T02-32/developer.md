# 💻 코다리 — Designer가 제공할 '데이터 교란' 애니메이션 스펙(Glitch Effect/Noise Overlay)을 수용하여, React 컴포넌트에서 State Change에 연동되는 로직 구조를 설계해 주세요. 특히, 데이터 값이 임계치를 넘는 순간(`Critical Gap` 상태 진입)의 시각적 전환(Transition)과 그 전후의 애니메이션이 끊김 없이 유기적으로 연결되도록 Pseudo-Code 및 컴포넌트 아키텍처 초안을 작성해야 합니다.

💻 코다리: 작업 시작합니다.

CEO 지시사항 확인했습니다. Designer가 정의한 'Critical Failure' 스펙은 단순한 애니메이션이 아니라, 사용자에게 심리적 압박을 가하는 핵심 *UX 장치*입니다. 이 효과를 React State Change에 유기적으로 연결하려면, 단순히 CSS 클래스를 토글하는 것을 넘어선 **상태 머신(State Machine)** 기반의 로직 설계가 필수입니다.

어떤 데이터 값이 들어오느냐에 따라 시각적 상태(`Normal`, `Warning`, `Critical`)가 결정되고, 이 상태 변화에 맞춰 애니메이션 타이밍과 강도가 조절되어야 합니다. 제가 `DefectIdGraph.tsx` 컴포넌트의 아키텍처를 재설계하고 Pseudo-Code 및 Type Definition을 제시하겠습니다.

### ⚙️ Defect ID Graph Component Architecture 설계

핵심은 다음과 같습니다:
1.  **State Determinism:** 그래프에 표시되는 핵심 수치(`DefectID_Gap_Score`)가 주입되면, 이 값 하나로 모든 시각적 상태를 결정합니다.
2.  **Transition Logic:** 상태 변화는 즉시 일어나지 않고, `Warning` $\rightarrow$ `Critical`과 같이 임계점을 넘을 때 **강도 증가(Amplitude Increase)**의 형태로 연출되어야 합니다.

#### 1. TypeScript Type 정의 (DefectIdGraph.tsx 내부에 추가)

먼저 명확한 타입을 정의하여 상태 간의 불필요한 혼선을 방지해야 합니다.

```typescript
// c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\components\DefectIdGraph.tsx 파일 내부
export type GapStatus = 'NORMAL' | 'WARNING' | 'CRITICAL';

interface DefectIDGraphProps {
  /** 측정된 핵심 지표 값 (0 ~ 100) */
  score: number;
  /* 상태 변화를 감지하기 위한 이전 스코어 (선택 사항, 부드러운 전환에 사용) */
  previousScore?: number;
}

interface StatusMapping {
  status: GapStatus;
  threshold: [number, number]; // [Min, Max] 범위
  animationClass: string; // CSS Class Name
  message: string;
}
```

#### 2. 상태 결정 로직 (State Determination Hook/Function)

데이터 기반으로 상태를 계산하는 전용 함수를 구현합니다. 이 함수가 컴포넌트의 핵심 브레인입니다.

```typescript
// Pseudo-Code: useDefectStatus.ts (또는 DefectIdGraph.tsx 상단에 위치)

const calculateGapStatus = (score: number, previousScore?: number): { status: GapStatus; animationClass: string; message: string } => {
  let currentStatus: GapStatus;
  let statusMessage: string;
  let animationClass: string;

  // 1. Critical Failure 판단 (가장 우선순위 높음)
  if (score >= 85) { // 임계점 초과 가정
    currentStatus = 'CRITICAL';
    statusMessage = "🔴 시스템 오류 감지! 즉각적인 정밀 진단이 필요합니다.";
    animationClass = "glitch-critical";

  // 2. Warning 판단 (주의 단계)
  } else if (score >= 60) { // 경고 범위 가정
    currentStatus = 'WARNING';
    statusMessage = "🟡 위험 신호 감지. 현재 상태 유지를 위해 관리가 필요합니다.";
    animationClass = "glitch-warning";

  // 3. Normal 판단
  } else {
    currentStatus = 'NORMAL';
    statusMessage = "🟢 안정 범위 내에 있습니다. 지속적인 모니터링이 권장됩니다.";
    animationClass = "glitch-normal";
  }

  // * Transition Enhancement Logic (핵심 개선 부분):
  // 만약 이전 상태가 WARNING이었는데 이번에 CRITICAL로 진입했다면, 
  // 단순히 클래스만 바꾸는 것이 아니라 '강도 증가' 로직을 추가해야 합니다.
  if (previousScore && currentStatus === 'CRITICAL' && previousScore < 85) {
    // 강제 트랜지션 효과를 부여하는 특수 플래그 반환
    console.log("🚨 CRITICAL Transition Detected: Triggering amplitude boost!");
    return { status: 'TRANSITION_ACTIVE', animationClass: "transition-boost", message: statusMessage }; 
  }


  return { status: currentStatus, animationClass: animationClass, message: statusMessage };
};
```

#### 3. 컴포넌트 구조 초안 (DefectIdGraph.tsx)

이 로직을 React Hook으로 감싸서 사용성을 높입니다.

```typescript
// Pseudo-Code: DefectIdGraph.tsx
import React, { useMemo } from 'react';
// ... 필요한 타입 및 함수 import ...

const DefectIdGraph: React.FC<DefectIDGraphProps> = ({ score, previousScore }) => {
  // 1. 상태 계산 (useMemo를 사용하여 스코어가 변경될 때만 재계산)
  const statusInfo = useMemo(() => calculateGapStatus(score, previousScore), [score, previousScore]);

  // 2. 스타일 및 핸들러 정의
  const containerClasses = `${statusInfo.animationClass} transition-all duration-300 ease-in-out`;
  
  // Critical 상태일 때만 진단 버튼을 활성화하고, 애니메이션이 적용된 CTA를 보여줌.
  const isCritical = statusInfo.status === 'CRITICAL' || statusInfo.status === 'TRANSITION_ACTIVE';

  return (
    <div className="defect-graph">
      {/* A. 핵심 그래프 시각화 영역 */}
      <div className={`score-display ${containerClasses}`}>
        <h1>{score}</h1> {/* 스코어 값 자체에 애니메이션 클래스 적용 */}
        <p>{statusInfo.message}</p>
      </div>

      {/* B. CTA 및 액션 유도 (Critical일 때 가장 강력해야 함) */}
      <div className="cta-section">
        {isCritical && (
          // Critical 상태 시, 배경까지 Glitch 효과를 적용하여 위협감을 높임.
          <button className="glitch-cta-button" onClick={handleDiagnosisClick}>
            ⚠️ 지금 무료 진단 받기 ({statusInfo.message})
          </button>
        )}
      </div>
    </div>
  );
};

export default DefectIdGraph;
```

### 📊 평가: 진행중 — 컴포넌트 아키텍처와 로직 흐름을 설계했으나, 실제 CSS 애니메이션 (Keyframe) 구현은 아직 코드로 옮기지 않았습니다.

📝 다음 단계: Designer가 제시한 Glitch Effect와 Noise Overlay의 세부 CSS Keyframe 코드를 `DefectIdGraph` 컴포넌트의 스타일 시트로 적용하고, React Transition Hook을 이용하여 상태 변화에 따른 부드러운 애니메이션 흐름을 테스트해야 합니다.
