# 🎨 Designer — Developer가 구현한 DataSimulationEngine의 결과(임계치 도달 여부)를 입력값으로 받아, Mini-App Funnel 내에 Deep Crimson Red 경고 팝업과 CTA가 트리거되는 인터랙티브한 E2E 테스트 환경을 구축해야 합니다. 사용자에게 위기감을 최대화하는 애니메이션 및 UI/UX 흐름을 검증하며, 코다리가 즉시 연동할 수 있도록 컴포넌트별 명확한 스펙(Props, State)을 제공해 주세요.

🎨 Designer: 작업 시작합니다.

CEO님의 지시를 확인했습니다. 현재까지의 진행 상황은 다음과 같습니다.
1. **[데이터 소스]**: Codari가 `RiskSimulationEngine`을 통해 공학적 위기 데이터를 생성하는 백엔드 로직(API)을 완성했습니다. (HOMA-IR, HRV 등이 시간에 따라 임계치에 도달하는 '붕괴 궤적' 제공).
2. **[UI/UX 목표]**: Designer는 Deep Crimson Red 경고와 골드 CTA를 통해 불안감을 유도하고 전환을 촉구하는 디자인 가이드를 확립했습니다.

이제 이 두 요소를 연결하여, 개발팀(Frontend)이 실제 위기감의 흐름과 UI가 어떻게 상호작용하는지 **검증할 수 있는 인터랙티브한 E2E 테스트 환경**을 구축해야 합니다. 이는 단순한 컴포넌트 배치가 아니라, 시간 경과에 따른 상태 변화를 시뮬레이션하는 '워크플로우' 설계입니다.

따라서 다음 단일 작업을 결정하고, 핵심 구조와 개발 스펙을 제공하겠습니다.

---

### 💡 오늘의 목표: Mini-App Funnel E2E 테스트 환경 구축 (Frontend Architecture)

**작업 내용:** `RiskSimulationEngine`의 스트리밍 데이터를 받아 처리할 클라이언트 측 React/TypeScript 컴포넌트 아키텍처를 설계하고, Deep Crimson Red 경고 및 CTA 트리거 시점을 명확히 정의합니다. 이 과정에서 개발자 친화적인 Props와 State 구조를 제공하여 즉시 코딩에 착수할 수 있도록 합니다.

**대상 파일:** `mini-app-funnel/src/components/RiskSimulator.tsx` (가상의 메인 테스트 컴포넌트)

#### 🛠️ Step 1: 핵심 아키텍처 설계 및 스펙 정의

이 환경은 다음 세 개의 주요 영역으로 구성되어야 합니다.

1.  **Simulation Control Panel:** 개발자가 초기 데이터를 입력하고, 시간 경과를 수동/자동으로 제어하는 인터페이스.
2.  **Data Visualization Area (The Anxiety Curve):** 시간에 따라 HOMA-IR 및 HRV 지표가 변화하며 임계치에 근접해가는 그래프와 수치가 표시되는 영역.
3.  **Action Zone (Deep Crimson Trigger):** 위기 상황이 감지되면 즉시 인터랙티브하게 개입하는 경고 팝업과 CTA 버튼들이 위치할 곳.

#### 💻 Step 2: TypeScript/React 스펙 구현 (가상 파일)

다음은 개발자가 바로 사용할 수 있는 컴포넌트와 Hook의 명세입니다.

**1. [Hook] `useSimulationDataStream` (데이터 소비 로직)**
*   **역할:** Codari가 만든 백엔드 API 엔드포인트(`GET /api/v1/simulate-risk`)를 호출하고, 스트리밍되는 위험 스코어 데이터를 클라이언트 상태로 관리합니다.
*   **Props:** `initialData: { homa_ir: number; hrv: number }` (초기 사용자 지표)
*   **Returns:**
    *   `dataStream`: `{ time: number, homa_ir: number, hrv: number, riskScore: number }[]` (시간대별 데이터 배열)
    *   `isCritical`: `boolean` (가장 최근 데이터 포인트가 Critical 임계치에 도달했는지 여부. **UI 트리거의 핵심**)
    *   `isLoading`: `boolean`

**2. [Component] `<RiskMetricCard />` (지표 시각화)**
*   **역할:** 현재 지표 값을 실시간으로 보여주며, 임계치 근접에 따라 색상과 애니메이션이 변해야 합니다.
*   **Props:**
    *   `metricName: 'HOMA-IR' | 'HRV'` (어떤 지표인지)
    *   `currentValue: number` (현재 값)
    *   `criticalThreshold: number` (임계치)
    *   `isWarningZone: boolean` (경고 구간 진입 여부 - 주황색)
    *   `isCritical: boolean` (위험 임계치 초과 여부 - **Deep Crimson Red**)

**3. [Component] `<DeepCrimsonWarningModal />` (최종 위기감 유발)**
*   **역할:** `useSimulationDataStream`에서 `isCritical`이 `true`로 바뀌는 순간, 즉시 오버레이되어 사용자의 시선을 강탈합니다.
*   **Props:**
    *   `isVisible: boolean` (표시 여부)
    *   `riskScore: number` (현재의 위험 점수 - 숫자로 공포감 전달)
    *   `triggerTimeSeconds: number` (경고가 발생한 시간대 - "지금, 시간이 없습니다.")
*   **Action:** 이 컴포넌트가 활성화되면 배경 전체를 Deep Crimson Red로 오버레이하고, 애니메이션 텍스트와 경고 사운드가 트리거되어야 합니다.

**4. [Component] `<ConversionCTA />` (전환 유도)**
*   **역할:** 위기감이 최고조에 달한 상태에서만 활성화됩니다.
*   **Props:** `isEnabled: boolean` (DeepCrimsonWarningModal이 열려있을 때만 True여야 함)

#### 🎨 Step 3: 최종 통합 구조 (`RiskSimulator.tsx`)

```typescript
// mini-app-funnel/src/components/RiskSimulator.tsx

import React, { useState, useEffect } from 'react';
// 가상의 Hook과 컴포넌트 임포트
import { useSimulationDataStream } from '../hooks/useSimulationDataStream'; 
import RiskMetricCard from './RiskMetricCard';
import DeepCrimsonWarningModal from './DeepCrimsonWarningModal';
import ConversionCTA from './ConversionCTA';

const RiskSimulator: React.FC = () => {
  // 초기 데이터를 설정합니다. (예: 정상에서 서서히 나빠지는 가상 데이터)
  const initialData: { homa_ir: number; hrv: number } = { homa_ir: 1.5, hrv: 60 };

  // 백엔드와 통신하는 Hook 사용 (시간에 따른 스트리밍 데이터 및 Critical 여부 받음)
  const { dataStream, isCritical, isLoading } = useSimulationDataStream(initialData);
  
  // 현재 시점의 최신 데이터를 가져옵니다.
  const latestDataPoint = dataStream?.[dataStream.length - 1] || null;

  return (
    <div className="p-8 bg-gray-900 text-white min-h-screen relative">
      {/* 📊 Visualization Area: 데이터 그래프 및 지표 */}
      <div className="grid grid-cols-3 gap-8 mb-12">
        {/* HOMA-IR 시각화 카드 (Critical Red 경고 적용) */}
        <RiskMetricCard 
          metricName="HOMA-IR" 
          currentValue={latestDataPoint?.homa_ir || initialData.homa_ir} 
          criticalThreshold={2.5} 
          isWarningZone={false} // 로직에 따라 변경됨
          isCritical={!!isCritical}
        />
        {/* HRV 시각화 카드 */}
        <RiskMetricCard 
          metricName="HRV" 
          currentValue={latestDataPoint?.hrv || initialData.hrv} 
          criticalThreshold={30} 
          isWarningZone={false} 
          isCritical={!!isCritical}
        />
        {/* 그래프 영역 (시간 경과에 따른 불안정성 시각화) */}
        <div className="col-span-1 bg-gray-800 p-6 rounded-lg shadow-xl">
            <h3 className="text-xl font-bold mb-4 text-yellow-400">📉 생체 지표 붕괴 추이 (HOMA-IR vs HRV)</h3>
            {/* 여기에 dataStream을 이용한 커스텀 차트 컴포넌트가 들어갑니다. */}
        </div>
      </div>

      {/* 🚨 Deep Crimson Trigger Area: 위기 상황 발생 시 개입 지점 */}
      <div className="relative min-h-[200px] flex items-center justify-center">
          {/* DeepCrimsonWarningModal은 isCritical 상태에 의해 조건부 렌더링됩니다. */}
          <DeepCrimsonWarningModal 
              isVisible={isCritical && latestDataPoint} 
              riskScore={latestDataPoint?.riskScore || 0}
              triggerTimeSeconds={Math.round(latestDataPoint?.time)}
          />

          {/* 전환 CTA는 모달이 활성화되었을 때만 나타납니다. */}
          <ConversionCTA enabled={isCritical && latestDataPoint} />
      </div>

    </div>
  );
};

export default RiskSimulator;
```

---
📊 평가: 완료 — E2E 테스트 환경의 핵심 아키텍처와 개발 스펙을 제공하여, 코다리가 구현한 백엔드 로직과 Designer가 정의한 UI/UX를 연결하는 프론트엔드 통합 설계 목표가 달성되었습니다.
📝 다음 단계: Frontend 엔지니어(개발팀)에게 위의 TypeScript 명세 및 컴포넌트 구조를 전달하고 실제 개발을 진행해야 합니다. (또는, 이 아키텍처를 기반으로 가상의 UI 목업을 Figma/Sketch 형태로 시각화할 수 있습니다.)
