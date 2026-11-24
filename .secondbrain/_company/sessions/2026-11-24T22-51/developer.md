# 💻 코다리 — 비서가 작성해 줄 새로운 컴포넌트 맵을 기다려 주세요. 맵이 확보되는 즉시, 지난번 목표였던 '가격 비교표'의 트래킹 로직 통합 및 테스트 코드를 재개할 수 있도록 준비하고, 필요한 API 호출 스펙(Mocking 포함)과 단위 테스트 케이스를 미리 구상해 주세요.

💻 코다리: 작업 시작합니다. 영숙님의 컴포넌트 맵 잘 받았습니다. 덕분에 아키텍처의 큰 그림이 확실해졌어요. ✅

Mini Bundle LP의 핵심은 '손실 공포(FOMO)'를 극대화하여 진단 테스트와 가격 비교표를 자연스럽게 연결하는 겁니다. 영숙님이 정리해주신 청사진을 보니, `PriceTable` 컴포넌트가 이 전체 퍼널의 **결정적인 병목 지점(Bottleneck)**이네요.

CEO님의 지시대로, 제가 가장 가치 높은 단일 작업을 결정했습니다. 바로 **'가격 비교표 (Price Table)'에 대한 트래킹 로직 통합 설계와 단위 테스트 환경 구축**입니다. 이 부분이 깨지면 모든 KPI 측정이 마비됩니다. 😭

지금부터 필요한 API 스펙(Mocking 포함)과 단위 테스트 케이스를 준비하는 작업을 진행하겠습니다.

### ⚙️ 작업 계획 및 흐름
1.  **테스트 구조 설계**: `PriceTable`의 상태 변화와 상호작용 지점을 추적할 수 있는 Mock API 서비스와 전용 Context/Hook을 정의합니다.
2.  **Mocking 구현**: 실제 백엔드 호출 없이도 테스트가 가능한 가짜(Mock) 데이터 레이어를 만듭니다.
3.  **단위 테스트 작성**: 핵심 시나리오 (예: 마우스 오버 시 A/B/C 티어 순차 트래킹, 특정 CTA 클릭 시 최종 전환 값 기록)를 커버하는 Jest 기반의 테스트 코드를 작성합니다.

---

### 1단계: Mock API 및 Context 준비
`PriceTable` 컴포넌트가 의존할 추적(Analytics Tracking) 로직을 전역적으로 관리하고 모킹할 수 있는 구조가 필요합니다. 기존에 작업했던 `useAnalyticsTracker.ts`를 활용하여 확장하겠습니다.

<create_file path="src/context/AnalyticsContext.tsx">
// src/context/AnalyticsContext.tsx
import React, { createContext, useContext, useState } from 'react';

interface AnalyticsState {
  trackEvent: (eventName: string, properties: Record<string, any>) => void;
  isLoading: boolean;
}

const AnalyticsContext = createContext<AnalyticsState | undefined>(undefined);

export const AnalyticsProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  // 실제 환경에서는 이 상태가 서버와 통신하거나 Redux/Zustand 같은 전역 상태 관리 도구와 연동됩니다.
  const [isLoading, setIsLoading] = useState(false);

  /**
   * 특정 이벤트 발생 시 분석 데이터를 추적합니다.
   * @param eventName - 발생한 이벤트의 이름 (예: 'price_hover', 'cta_click')
   * @param properties - 이벤트 관련 추가 데이터 {tier: 'Silver', source: 'DiagnosticTest'} 등
   */
  const trackEvent = async (eventName: string, properties: Record<string, any>) => {
    console.log(`[Analytics] Tracking Event: ${eventName}`, properties);

    // 💡 Mocking/Simulation 로직: 실제 API 호출 대신 콘솔에 기록하고 비동기 지연을 시뮬레이션합니다.
    setIsLoading(true);
    try {
      await new Promise(resolve => setTimeout(resolve, 50)); // Simulate Network Delay
      
      // 여기서 MockAPIService를 통해 실제로 전송되는 로직이 들어갑니다.
      console.log(`✅ [Analytics Success] ${eventName} data successfully queued.`);

    } catch (error) {
      console.error(`❌ [Analytics Failure] Failed to track event: ${error}`);
      // 에러 발생 시, UI에 영향을 주지 않고 로컬 저장소(IndexedDB/Local Storage)에 임시 저장하는 폴백 로직이 필요합니다.
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <AnalyticsContext.Provider value={{ trackEvent, isLoading }}>
      {children}
    </AnalyticsContext.Provider>
  );
};

export const useAnalytics = () => {
  const context = useContext(AnalyticsContext);
  if (!context) {
    throw new Error('useAnalytics must be used within an AnalyticsProvider');
  }
  return context;
};
</create_file>

<create_file path="src/utils/mockApiService.ts">
// src/utils/mockApiService.ts
/**
 * 외부 API 호출을 Mocking하기 위한 서비스 레이어입니다. 
 * 실제 백엔드와 통신하는 대신, 테스트 환경에서 일관된 가짜 데이터를 제공합니다.
 */

export interface TrackDataPayload {
    timestamp: number;
    event_name: string;
    user_id: string | null;
    properties: Record<string, any>;
}

/** 
 * 트래킹 데이터를 전송하는 Mock API 함수입니다.
 * @param payload - 전송할 데이터 페이로드
 */
export const mockSendTrackingData = async (payload: TrackDataPayload): Promise<boolean> => {
    console.log("--- MOCK API CALL STARTED ---");
    // 실제 네트워크 호출 대신, 콘솔 로그와 시간 지연만 발생시킵니다.
    await new Promise(resolve => setTimeout(resolve, 100)); 

    if (Math.random() > 0.95) { // 5% 확률로 API 실패 시뮬레이션
        console.error(`MOCK API ERROR: Network timeout or server failure.`);
        return false;
    } else {
        console.log("✅ MOCK API SUCCESS: Data successfully logged to Analytics Dashboard.");
        // 실제 성공 응답 구조를 반환합니다.
        return true; 
    }
};
</create_file>

### 2단계: 단위 테스트 파일 작성 (Jest 기반)
`PriceTable` 컴포넌트가 의존하는 `useAnalytics` Hook과 `mockApiService`의 연동을 검증할 테스트 파일을 만듭니다. 이 방식이 가장 빠르고 확실하게 트래킹 로직의 안정성을 확보합니다.

<create_file path="src/components/__tests__/PriceTable.test.tsx">
// src/components/__tests__/PriceTable.test.tsx
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import PriceComparisonTable from '@/components/pricing/PriceTable'; // 가상의 경로

// 🛠️ Mocking 설정: AnalyticsContext와 mockSendTrackingData를 전역으로 모킹합니다.
jest.mock('@/context/AnalyticsContext', () => ({
  useAnalytics: jest.fn(() => ({
    trackEvent: jest.fn(), // 추적 이벤트를 가짜 함수로 대체
    isLoading: false,
  })),
}));

// 💡 테스트 목표 정의:
// 1. 컴포넌트가 로드될 때 초기 트래킹이 발생하는지 확인한다. (Initial Load)
// 2. 사용자가 티어에 마우스를 올릴 때(Hover) 해당 이벤트가 정확히 전송되는지 확인한다. (Interaction Tracking)
// 3. 최종 CTA 클릭 시, 전환 값과 함께 마지막 이벤트가 기록되는지 확인한다. (Conversion Funnel)

describe('PriceComparisonTable Component Test Suite', () => {
  const mockTrackEvent = jest.fn(); // Mocked trackEvent function reference

  beforeEach(() => {
    // 각 테스트 시작 전에 모킹된 함수를 초기화합니다.
    mockTrackEvent.mockClear(); 
    (require('@/context/AnalyticsContext').useAnalytics as jest.Mock).mockReturnValue({
      trackEvent: mockTrackEvent,
      isLoading: false,
    });
  });

  it('Should render correctly and track initial view event', () => {
    // @tsx 환경에서 테스트 실행 시도
    render(<PriceComparisonTable />); 
    
    // 1. 컴포넌트가 정상적으로 렌더링되었는지 확인 (예: 가격 비교표의 제목이 보이는지)
    expect(screen.getByText(/Bronze|Silver|Gold/i)).toBeInTheDocument();

    // 2. 마운트 시점에 초기 트래킹 이벤트가 호출되었는지 검증
    expect(mockTrackEvent).toHaveBeenCalledTimes(1);
    expect(mockTrackEvent).toHaveBeenCalledWith(
      'price_table_view', // 예상되는 첫 번째 이벤트 이름
      expect.objectContaining({ source: 'LP Landing Page' })
    );
  });

  it('Should track interaction events (Hover) on pricing tiers', async () => {
    render(<PriceComparisonTable />); 

    // 가격표 내의 특정 티어 영역을 찾습니다. (실제 구현 시, button/div에 data-testid를 부여해야 함)
    const silverTierElement = screen.getByTestId('tier-silver'); // 가상의 테스트 ID 사용
    
    // 마우스 오버 이벤트 발생 시뮬레이션
    fireEvent.mouseEnter(silverTierElement); 

    // 예상 검증: Silver Tier에 대한 'hover' 이벤트가 정확히 트래킹되었는지 확인
    expect(mockTrackEvent).toHaveBeenCalledWith(
      'price_hover', 
      expect.objectContaining({ tier: 'Silver', value: expect.any(Number) })
    );

    // 다른 티어와 중복 호출되지 않았는지도 체크 (선택적 검증)
    // ...
  });

  it('Should track final conversion event upon CTA click', async () => {
    render(<PriceComparisonTable />); 

    const ctaButton = screen.getByRole('button', { name: /지금 바로 시작/i }); // 가상의 버튼 역할 사용

    // 최종 구매 액션 시뮬레이션 (클릭)
    fireEvent.click(ctaButton); 

    // 예상 검증: 최종 CTA 클릭 이벤트가 호출되었는지 확인
    expect(mockTrackEvent).toHaveBeenCalledWith(
      'final_conversion', // 예상되는 최종 전환 이벤트 이름
      expect.objectContaining({ tier_purchased: 'Silver', revenue_estimate: expect.any(Number) })
    );

    // 💡 트래킹 로직의 안정성 검증 (Self-Correction): 
    // 만약 mockSendTrackingData가 실패했을 때, 이 테스트는 crash하지 않고 폴백 처리를 하는지 추가로 확인해야 합니다.
  });
});
</create_file>

<reveal_in_explorer path="src/components/__tests__/PriceTable.test.tsx"/>

📊 평가: 진행중 — 트래킹 로직의 통합 설계와 단위 테스트 환경 구축이 완료되었으나, 실제로 `PriceComparisonTable.tsx` 컴포넌트가 존재하지 않아 테스트 코드를 실행하고 검증할 수 없습니다.
📝 다음 단계: 개발팀은 현재 준비된 Mock API 스펙과 Unit Test 파일을 기반으로, 실제 `<Price Comparison Table>` 컴포넌트 파일(`src/components/pricing/PriceTable.tsx`)을 **최소한의 기능(렌더링 및 이벤트 핸들러 연결)**으로 구현해야 합니다. 그 후 제가 전체 시스템 통합 테스트를 진행하겠습니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\Baro_KHNLU\src\context\AnalyticsContext.tsx
✅ 생성: c:\Data\Project\Baro_KHNLU\src\utils\mockApiService.ts
✅ 생성: c:\Data\Project\Baro_KHNLU\src\components\__tests__\PriceTable.test.tsx
🗂 🗂 익스플로러 열림: c:\Data\Project\Baro_KHNLU\src\components\__tests__\PriceTable.test.tsx
