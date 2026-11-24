import React from 'react';
import { useTracking } from '../context/TrackingContext';

interface CTAProps {
  label: string; // 버튼에 표시될 텍스트 (e.g., "49,000원으로 진단 받기")
  onClickAction: () => Promise<void>; // 실제 비즈니스 로직 실행 함수
  variant: 'DeepNavy' | 'AlarmRed'; // 색상 변형
  abTestVariant?: 'A' | 'B'; // A/B 테스트 변종 (없으면 기본)
}

const getStyles = (variant: 'DeepNavy' | 'AlarmRed', abTestVariant: 'A' | 'B'): { base: string; hover: string } => {
  // 🚨 코딩 원칙 적용: 색상 정의는 단순 클래스 조합이 아님. 의미를 담아야 함.
  if (variant === 'DeepNavy') {
    return abTestVariant === 'A' 
      ? { base: "bg-deep-navy hover:bg-darker-navy", hover: "hover:bg-darker-navy" } // A: 표준 신뢰감 유도
      : { base: "bg-sky-900 hover:bg-sky-800", hover: "hover:bg-sky-700" };     // B: 유사하지만 다른 톤으로 테스트
  } else if (variant === 'AlarmRed') {
    return abTestVariant === 'A' 
      ? { base: "bg-alarm-red hover:bg-darker-red", hover: "hover:bg-darker-red" } // A: 최대 경고 유도
      : { base: "bg-orange-600 hover:bg-orange-500", hover: "hover:bg-orange-400" };// B: 긴급하지만 덜 위협적인 색상으로 테스트
  }
  return { base: 'bg-gray-500', hover: 'hover:bg-gray-600' };
};

const CTAButtonComponent: React.FC<CTAProps> = ({ label, onClickAction, variant, abTestVariant = 'A' }) => {
  const { trackEvent } = useTracking();
  const styles = getStyles(variant, abTestVariant);

  const handleClick = async () => {
    // 1. 클릭 시도 추적 (가장 먼저 일어나야 함)
    await trackEvent('CTA_Click', { label: label, variant: variant, group: abTestVariant });
    
    try {
      // 2. 비즈니스 로직 실행 (실제 결제/폼 제출)
      await onClickAction();
    } catch (error) {
      console.error("CTA Action Failed:", error);
      // 에러 발생 시 사용자 피드백 및 로그 남기기
    }
  };

  return (
    <button 
      className={`py-3 px-8 rounded-xl text-white font-bold transition-all duration-200 ${styles.base} ${styles.hover}`}
      onClick={handleClick}
      aria-label={`Click button: ${label}`}
    >
      {label}
    </button>
  );
};

export default CTAButtonComponent;