export type DefectCode = "E-M411" | "N-512" | "C-701"; // DB에 정의된 코드만 타입으로 사용

export interface DiagnosisInputData {
    defectId: string; // 사용자 입력 (검증 필요)
    // 기타 진단 데이터 필드...
}

export interface ValidationResult {
    code: DefectCode;
    details: {
        description: string;
        severity: "LOW" | "MEDIUM" | "HIGH";
        baseRate: number;
    };
}