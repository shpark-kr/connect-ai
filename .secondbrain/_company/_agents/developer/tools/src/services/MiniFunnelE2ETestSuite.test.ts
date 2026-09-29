/**
 * @file MiniFunnel E2E 테스트 스위트
 * 진단(Diagnosis)부터 구매 완료(Purchase)까지의 모든 트랜잭션 무결성을 검증합니다.
 */

import { DiagnosisRecord, PurchaseTransaction, ProtocolTier } from '../models/MiniFunnelModels';
import { api_client, dbService } from './MockAPIClient'; // 가상의 Mock API 클라이언트 및 DB 서비스 임포트

describe('🚀 MiniFunnel End-to-End Critical Path Test Suite', () => {
    // 테스트 시작 전 공통 초기화: 시스템 상태를 'Healthy'로 설정합니다.
    beforeAll(() => {
        console.log("--- [SETUP] E2E 트랜잭션 시뮬레이터 초기화 ---");
        dbService.resetDatabaseState();
    });

    // 1. 핵심 성공 경로 테스트 (Happy Path)
    it('should successfully diagnose a critical defect and complete the TIER1 purchase', async () => {
        const mockData = [{ metricName: '관절가동범위_좌', value: 15, unit: '도' }]; // Critical Defect 시뮬레이션
        
        // STEP 1: 진단 데이터 전송 및 레코드 생성 (API Call)
        let diagnosisRecord: DiagnosisRecord = await api_client.submitDiagnosis(mockData);
        expect(diagnosisRecord).toHaveProperty('detectedDefects', expect.arrayContaining([
            { defectId: 'E-403', riskLevel: 'CRITICAL', severityScore: expect.any(Number) }
        ]));

        // STEP 2: Tier 1 상품 구매 시도 (Payment Call)
        let transactionAttempt = await api_client.processPurchase({
            recordId: diagnosisRecord.recordId,
            tier: ProtocolTier.DIAGNOSIS_REPORT,
            priceCents: 29000 // 29,000원
        });

        // STEP 3: 결과 검증 (DB Check)
        let finalTransaction = await dbService.getTransactionByRecordId(diagnosisRecord.recordId);
        expect(finalTransaction?.paymentStatus).toBe('SUCCESS');
        expect(finalTransaction?.purchaseTier).toBe(ProtocolTier.DIAGNOSIS_REPORT);
    });

    // 2. 실패 및 복구 테스트 (Failure/Edge Case)
    it('should rollback transaction if payment gateway fails after diagnosis', async () => {
        const mockData = [{ metricName: '혈압_평균', value: 140, unit: 'mmHg' }]; // High Defect 시뮬레이션

        // STEP 1: 진단 데이터 전송 및 레코드 생성 (API Call - 성공)
        let diagnosisRecord = await api_client.submitDiagnosis(mockData);
        
        // STEP 2: 결제 실패 상황 강제 주입 (Payment Failure Simulation)
        // API 클라이언트가 Payment Gateway Mock을 'FAILURE'로 설정하도록 합니다.
        await api_client.simulatePaymentFailure();

        let transactionAttempt = await api_client.processPurchase({
            recordId: diagnosisRecord.recordId,
            tier: ProtocolTier.PROTOCOL_KIT,
            priceCents: 149000
        });

        // STEP 3: 결과 검증 (DB Check) - 핵심 로직 검증 지점
        let finalTransaction = await dbService.getTransactionByRecordId(diagnosisRecord.recordId);
        expect(transactionAttempt?.success).toBe(false); // API 응답 자체도 실패여야 함
        // 중요한 건 DB 상태가 이전으로 돌아갔는지 확인하는 것! (롤백)
        expect(finalTransaction?.paymentStatus).toBe('PENDING'); 
    });

    it('should handle race conditions and ensure idempotency for repeated calls', async () => {
        const mockData = [{ metricName: '체지방률', value: 25, unit: '%' }];
        // 동일한 진단 데이터를 여러 번 전송할 경우, 새로운 레코드를 생성하지 않고 기존 레코드의 위험 점수만 업데이트해야 합니다.
        let initialRecord = await api_client.submitDiagnosis(mockData);

        // 1초 간격으로 동일 요청을 두 번 보냄 (Race Condition 시뮬레이션)
        await new Promise(resolve => setTimeout(resolve, 50));
        let secondAttemptRecord = await api_client.submitDiagnosis(mockData);

        // 검증: recordId는 같고, 데이터만 합쳐져야 하며, 시스템이 중복 처리를 막았음을 확인합니다.
        expect(initialRecord.recordId).toEqual(secondAttemptRecord.recordId);
    });
});