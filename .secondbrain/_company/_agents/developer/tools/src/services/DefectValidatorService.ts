/**
 * DefectValidatorService.ts
 * @description Master Defect DB 기반의 유효성 검증 및 진단 로직을 담당하는 서비스 계층.
 * 모든 데이터 검증은 이 모듈을 통해 이루어져야 합니다.
 */

import { DiagnosisInputData, DefectCode } from "../types/DiagnosisTypes"; // 가상의 타입 정의 파일

// =========================================================
// ⚠️ WARN: 실제로는 외부 DB (SQL/NoSQL)와 통신해야 하지만, 현재는 Mock 데이터로 대체합니다.
// 이 구조가 반드시 수정되어야 합니다.
// =========================================================
const MASTER_DEFECT_DB: Record<DefectCode, { description: string; severity: 'LOW' | 'MEDIUM' | 'HIGH'; baseRate: number }> = {
    "E-M411": { 
        description: "관절 불안정성(Knee Instability): 무릎 관절 주변 연부 조직의 구조적 약화.", 
        severity: "HIGH", 
        baseRate: 0.25 // 기준 대비 위험 지수 (예시)
    },
    "N-512": { 
        description: "신경 전달 효율 저하(Neurological Efficiency Drop): 중추 신경계의 미세한 전도율 감소.", 
        severity: "MEDIUM", 
        baseRate: 0.15 
    },
    "C-701": { 
        description: "코어 근육 시스템 결함(Core System Failure): 몸통 안정화 근육군의 활성도 저하로 인한 전반적 자세 불안정.", 
        severity: "HIGH", 
        baseRate: 0.30 
    },
};

/**
 * 사용자 입력 데이터를 검증하고, Master Defect DB에 존재 여부를 확인합니다.
 * @param data - 사용자가 제출한 진단 데이터 객체.
 * @returns {Object} 성공 시 유효성 검사된 결과 및 상세 정보.
 * @throws {Error} DefectCode가 DB에 존재하지 않을 경우, 강제 오류를 발생시킵니다.
 */
export const validateDefectData = (data: DiagnosisInputData): { code: DefectCode; details: any } => {
    const { defectId } = data;

    if (!defectId) {
        throw new Error("Validation Failed: 진단 ID(defectId)가 누락되었습니다.");
    }

    const normalizedCode = defectId.toUpperCase().trim();

    // 1. DB 존재 여부 검증 (핵심 로직)
    const masterDefectKey = Object.keys(MASTER_DEFECT_DB).find(key => key === normalizedCode);

    if (!masterDefectKey) {
        // ⚠️ 유효성 검증 실패 시, 강제 에러를 발생시켜 상태 기계를 정지시키고 오류 UI를 표시해야 합니다.
        throw new Error(`SYSTEM ERROR: Defect Code '${defectId}'는 Master Defect DB에 정의되지 않은 비표준 코드입니다. 데이터 유효성을 확인할 수 없습니다.`);
    }

    // 2. 성공적인 검증 로직 실행
    const defectDetails = MASTER_DEFECT_DB[masterDefectKey];

    return { 
        code: masterDefectKey as DefectCode, 
        details: {
            description: defectDetails.description,
            severity: defectDetails.severity,
            baseRate: defectDetails.baseRate,
            // 여기에 추가적인 계산 로직 (예: 사용자 연령에 따른 가중치 적용)을 넣습니다.
        }
    };
};

/**
 * Mock Master Defect DB의 모든 코드를 반환합니다. (UI 선택지 제공용)
 */
export const getAllValidDefectCodes = (): string[] => {
    return Object.keys(MASTER_DEFECT_DB);
}