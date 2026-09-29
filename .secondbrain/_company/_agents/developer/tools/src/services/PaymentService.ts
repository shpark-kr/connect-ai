// Payment Service Interface 정의 (핵심 추상화)
export interface IPaymentGateway {
    /** 
     * 결제 시도: 외부 PG사(Stripe, KG이니시스 등)로 실제 결제를 요청합니다.
     * @param amount - 금액 (USD)
     * @param token - 사용자 토큰/결제 수단 ID
     * @returns Promise<TransactionResult>
     */
    processPayment(amount: number, token: string): Promise<{ success: boolean; transactionId: string }>;

    /** 
     * 결제 취소: 환불이 필요한 경우 사용합니다. 
     */
    refund(transactionId: string): Promise<boolean>;
}

// 가짜 구현체 (Mock Implementation) - 테스트용
export class MockPaymentGateway implements IPaymentGateway {
    async processPayment(amount: number, token: string): Promise<{ success: boolean; transactionId: string }> {
        console.log(`[MOCK] ${token}로 $${amount.toFixed(2)} 결제 시도...`);

        // --- 핵심 테스트 로직 추가: Intentional Failure Simulation ---
        if (token.includes('FAIL_CARD')) { 
            return { success: false, transactionId: 'FAIL-123' }; // 카드 거절 시뮬레이션
        }
        if (amount > 500 && token.includes('SERVER_OVERLOAD')) {
             // 서버 과부하를 유도하여 트랜잭션 타임아웃 테스트 유발
            await new Promise(resolve => setTimeout(resolve, 2000)); 
            return { success: false, transactionId: 'TIMEOUT-408' };
        }

        // 기본 성공 케이스
        const mockTxId = `TX-${Date.now()}-${Math.random().toString(36).substring(7).toUpperCase()}`;
        console.log(`[MOCK] 결제 성공! Transaction ID: ${mockTxId}`);
        return { success: true, transactionId: mockTxId };
    }

    async refund(transactionId: string): Promise<boolean> {
        console.warn(`[WARNING] 트랜잭션 ${transactionId}에 대한 환불 처리 시도...`);
        // 실제로는 PG사에 요청해야 함
        return true; 
    }
}

export type TransactionResult = { success: boolean; transactionId: string };