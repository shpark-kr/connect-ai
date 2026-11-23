/**
 * @module types
 * Defect ID 그래프 관련 타입 정의 파일. 모든 컴포넌트에서 사용될 핵심 계약입니다.
 */

export interface DataPoint {
    name: string; // 예: 혈당 (HbA1c)
    currentValue: number; // 현재 측정된 값
    threshold: number;   // 정상 범위 임계치 (Critical Threshold)
    unit: string;        // 단위
    defectGap: number;   // Gap 수치 (Current - Threshold). 이 값이 시각적 강조의 핵심입니다.
}

export interface DiagnosticResult {
    date: string;
    diagnosisName: string; // 예: Defect ID 종합 위험 지수
    isCriticalGap: boolean; // 가장 중요한 플래그! True면 경고 애니메이션 발동.
    dataPoints: DataPoint[];
}