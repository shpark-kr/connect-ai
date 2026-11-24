import React, { createContext, useContext, useState } from 'react';

// 🚨 추적 로직 인터페이스 정의: 모든 행동은 반드시 어떤 변수에 의해 트리거되어야 함.
interface TrackingContextType {
  trackEvent: (eventName: string, properties: Record<string, any>) => Promise<void>;
  setABTestGroup: (group: 'A' | 'B') => void;
}

// 초기 상태 설정
const defaultContext: TrackingContextType = {
  trackEvent: async (eventName: string, properties: Record<string, any>) => {
    console.log(`[Analytics] Event Tracked: ${eventName}`, properties);
    // TODO: 실제 Google Analytics/Firebase API 호출 로직 구현 필요
    await new Promise(resolve => setTimeout(resolve, 50)); // Simulate network delay
  },
  setABTestGroup: (group: 'A' | 'B') => {
    console.log(`[A/B Test] Group set to ${group}.`);
    // TODO: Local Storage 또는 Context에 A/B 그룹 저장 로직 구현 필요
  }
};

export const TrackingContext = createContext<TrackingContextType>(defaultContext);

export const TrackingProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [abTestGroup, setABTestGroupState] = useState<'A' | 'B'>('A'); // 기본 그룹 A로 설정

  // 🚨 트래킹 로직: 모든 중요한 액션은 이 함수를 거쳐야 함.
  const trackEvent = async (eventName: string, properties: Record<string, any>) => {
    await defaultContext.trackEvent(eventName, {...properties, abTestGroup});
  };

  // 🚨 A/B 테스트 그룹 설정 로직
  const setABTestGroup = (group: 'A' | 'B') => {
    setABTestGroupState(group);
    // 실제 배포 시에는 서버 측에서 할당하거나, 쿠키를 사용해야 함.
  };

  return (
    <TrackingContext.Provider value={{ trackEvent, setABTestGroup }}>
      {children}
    </TrackingContext.Provider>
  );
};

export const useTracking = () => useContext(TrackingContext);