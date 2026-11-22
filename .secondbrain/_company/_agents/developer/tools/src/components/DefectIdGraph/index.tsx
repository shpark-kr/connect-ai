// Defect ID 변화 그래프 컴포넌트 (MVP Boilerplate)
import React from 'react';
import './styles/variables.css';

interface GraphDataPoint {
  time: string; // 시간 축 레이블
  value: number; // 측정값
}

/**
 * [MVP Boilerplate] Defect ID 변화 추이 그래프 컴포넌트. 
 * SVG와 CSS 변수를 사용하여 애니메이션 루프 기반의 시각화를 구현합니다.
 * @param {GraphDataPoint[]} data - 시간별 데이터 포인트 배열
 */
const DefectIdGraph: React.FC<{ data: GraphDataPoint[] }> = ({ data }) => {
  if (!data || data.length === 0) {
    return <div className="graph-container">데이터를 로드할 수 없습니다.</div>;
  }

  // SVG Path 데이터 생성 로직 (MVP 단계이므로 단순 연결만 구현)
  const points = data.map((point, index) => `${index * 100}% ${point.value}`).join(' ');

  return (
    <div className="graph-container">
      <h3>📈 {data[0].time} 기준 Defect ID 추이 분석</h3>
      <svg viewBox="0 0 100 100" preserveAspectRatio="none" width="100%" height="250px">
        {/* Axes & Grid (Simplification for MVP) */}
        <rect x="0" y="0" width="100%" height="100%" fill="none" /> 

        {/* The core animated path line. Stroke-dasharray/offset을 이용한 애니메이션 루프를 가정합니다. */}
        <path 
          d={`M 0 100 C ${data[0].time} 50, ${data[1].time} 50, ${data[2].time} 100`} // 가상의 곡선 경로 (실제 구현 시 데이터 매핑 필요)
          stroke="var(--defect-gradient)" 
          strokeWidth="3" 
          fill="none"
          className="animated-path" 
        />

        {/* Data Points */}
        {data.map((point, index) => (
            <circle 
                key={index} 
                cx={(index / (data.length - 1)) * 90 + 5} // 가상의 X 위치 계산
                cy={`${(point.value / Math.max(...data.map(d => d.value))) * 120}`} // Y축 스케일링 가정
                r="3" 
                fill="#ff4757" 
                style={{ opacity: `${0.5 + index * 0.1}` }}
            />
        ))}

      </svg>
      <div className="graph-x-labels">
          {data.map((point, index) => (
              <span key={index} style={{ left: `${(index / (data.length - 1)) * 90 + 5}%` }}>{point.time}</span>
          ))}
      </div>
    </div>
  );
};

export default DefectIdGraph;