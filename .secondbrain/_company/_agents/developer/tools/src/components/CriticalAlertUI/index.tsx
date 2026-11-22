// Critical Alert UI Component (MVP Boilerplate)
import React from 'react';
import './styles/variables.css';

interface CriticalAlertProps {
  severity: 'low' | 'medium' | 'high'; // Severity determines the visual state
  defectId: string;
  readingValue?: number; // Current measured value (e.g., LDL)
}

/**
 * [MVP Boilerplate] 핵심 경고 UI 컴포넌트. 
 * V4.0 스펙에 따라 CSS 변수와 애니메이션 루프를 적용함.
 * @param {CriticalAlertProps} props - Severity, Defect ID, 측정값 등 속성 전달
 */
const CriticalAlertUI: React.FC<CriticalAlertProps> = ({ severity, defectId, readingValue }) => {
  // CSS 변수를 통해 경고 레벨에 따른 색상 및 애니메이션 로직을 제어합니다.
  const alertClass = `alert-box ${severity}-level`;

  return (
    <div className={alertClass} role="alert" aria-live="assertive">
      <div className="alert-header">
        <span className={`icon-${severity}`}>⚠️</span> 
        <h2 className="defect-id-title">🚨 [DEFECT ID: {defectId}] 측정 오류 감지</h2>
      </div>

      <div className="alert-body">
        <p>현재 생체 신호는 심각한 위험 수준을 나타내고 있습니다. 즉시 검진이 필요합니다.</p>
        {readingValue !== undefined && (
          <div className="value-container">
            <span className="value-label">측정된 수치:</span> 
            <span className={`measured-value ${severity}-flash`}>
              {`${Math.round(readingValue)} mg/dL`}
            </span>
          </div>
        )}
      </div>

      <button className="cta-button">🚨 즉시 검진 예약하기</button>
    </div>
  );
};

export default CriticalAlertUI;