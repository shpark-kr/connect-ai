/**
 * @module apiService
 * Defect ID 진단 API를 모킹하여 비동기 데이터 흐름을 시뮬레이션합니다.
 * 실제 백엔드(POST /api/v1/diagnose/calculate)와 통신하는 로직을 대체합니다.
 */

import { DiagnosticResult } from '../types'; // 추후 생성될 타입 정의를 가정합니다.

// [Mock Data Definition] - 임상 데이터 매트릭스 기반의 가짜 결과 세트
const MOCK_DATA = {
    initial: { 
        HbA1c: 5.2,     // 정상 범위 (기준값)
        systolicBP: 118, // 정상 범위
        waistCircumference: 90, // 정상 범위
        activityLevelScore: 75, // 높은 점수 (정상)
    },
    critical_gap: {
        HbA1c: 6.8,     // Critical! 당뇨 전 단계 이상 수치 (Gap 발생)
        systolicBP: 145, // 고혈압 위험 수준
        waistCircumference: 105, // 복부 비만 임계점 초과
        activityLevelScore: 30, // 매우 낮은 활동 점수
    }
};

/**
 * 모킹된 진단 API 호출 함수. 
 * 시뮬레이션 지연 시간을 포함하여 실제 네트워크 지연을 모방합니다.
 * @param initialData 초기 입력 데이터 (사용자 측정값)
 * @returns Promise<DiagnosticResult> - 가짜 진단 결과
 */
export const calculateDefectDiagnosis = async (initialData: any): Promise<DiagnosticResult> => {
    console.log("⏳ API 호출 시뮬레이션 시작: Defect ID 진단을 계산합니다...");

    // 1. 초기 로딩 및 지연 시간 모방 (API가 작동하는 느낌 주기)
    await new Promise(resolve => setTimeout(resolve, 1500));

    // 2. 데이터 처리 단계 모방 (진단 모델이 돌고 있는 느낌)
    console.log("⚙️ 진단 엔진 구동 중... 생체 지표 간의 상관관계 분석...");
    await new Promise(resolve => setTimeout(resolve, 1000));


    // --- [핵심: Critical Gap 상태로 강제 전환 시뮬레이션] ---
    // 실제로는 사용자 입력 데이터에 따라 결정되어야 하지만, MVP 구축을 위해 가장 극적인 Case를 모킹합니다.

    const result = {
        date: new Date().toISOString(),
        diagnosisName: "Defect ID 종합 위험 지수",
        isCriticalGap: true, // ★★★ Critical Gap 강제 플래그 설정 ★★★
        dataPoints: [
            { 
                name: "혈당 (HbA1c)", 
                currentValue: MOCK_DATA.critical_gap.HbA1c, 
                threshold: 5.7, // 정상 임계치 (mg/dL)
                unit: "mmol/mol",
                defectGap: Math.round(MOCK_DATA.critical_gap.HbA1c - 5.7) * 10, // Gap 수치를 크게 모킹
            },
            { 
                name: "혈압 (Systolic BP)", 
                currentValue: MOCK_DATA.critical_gap.systolicBP, 
                threshold: 120,
                unit: "mmHg",
                defectGap: Math.round(MOCK_DATA.critical_gap.systolicBP - 120) * 5,
            },
            { 
                name: "복부둘레 (Waist)", 
                currentValue: MOCK_DATA.critical_gap.waistCircumference, 
                threshold: 90,
                unit: "cm",
                defectGap: Math.round(MOCK_DATA.critical_gap.waistCircumference - 90) * 2,
            },
        ]
    };

    console.log("✅ 진단 완료. Critical Gap 상태 데이터 반환.");
    return result;
}
export type MockApiResponse = typeof calculateDefectDiagnosis;