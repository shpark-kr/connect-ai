/**
 * MiniFunnel E2E Test Schema: 모든 핵심 비즈니스 엔티티 정의
 * 이 모델들은 진단(Diagnosis)부터 구매(Purchase)까지의 데이터 무결성을 보장하는 역할을 합니다.
 */

// --- 1. Defect ID 및 진단 결과 타입 (기존 DiagnosisTypes와 연동)
export type DefectId = string; // 예: E-403, M-512
export interface MeasuredValue {
    metricName: string;
    value: number;
    unit: string;
}

// --- 2. 진단 기록 (DiagnosisRecord): 사용자의 공학적 취약점 로그
export interface DiagnosisRecord {
    recordId: string; // UUID (시스템에서 생성)
    userId: string | null; // 인증된 경우 User ID, 비인증 시 null
    timestamp: Date;
    isCompleted: boolean; // 진단 완료 여부 플래그
    inputData: MeasuredValue[]; // 사용자가 입력한 측정 데이터 배열
    detectedDefects: {
        defectId: DefectId;
        riskLevel: 'CRITICAL' | 'HIGH' | 'MODERATE';
        severityScore: number; // 0.0 ~ 1.0 사이의 공학적 위험 점수
        suggestedIntervention: string; // 초기 권고 사항 요약
    }[];
}

// --- 3. 구매 거래 기록 (PurchaseTransaction): 수익화 흐름 추적
export enum ProtocolTier {
    DIAGNOSIS_REPORT = 'TIER1', // 정밀 리포트 구매
    PROTOCOL_KIT = 'TIER2',   // 생활 습관 가이드/영양제 조합 키트 구매
    FULL_MAINTENANCE = 'TIER3'  // 최종 컨설팅 및 유지관리 프로그램 구매 (ASP)
}

export interface PurchaseTransaction {
    transactionId: string; // 결제 게이트웨이 트랜잭션 ID
    recordId: string;       // 연결된 DiagnosisRecord ID
    purchaseTier: ProtocolTier;
    productName: string;    // 예: "E-403 관절 불안정성 복구 프로토콜"
    priceAmountCents: number; // 가격 (최소 단위인 센트/원 단위로 저장)
    paymentStatus: 'PENDING' | 'SUCCESS' | 'FAILED';
    purchasedAt: Date;
    userToken: string | null; // 결제에 사용된 토큰 (보안 처리 필요)
}

// --- 4. 백엔드 API 요청 및 응답 스키마 (예시)
export interface DiagnosisSubmissionPayload {
    data: MeasuredValue[];
    sessionId: string;
}

export interface ApiResponse<T> {
    success: boolean;
    statusCode: number; // HTTP Status Code 매핑
    message: string;
    data?: T;
}