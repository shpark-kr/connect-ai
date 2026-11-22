/**
 * @fileoverview Core Component API V5.0 - Data Contract Definition.
 * This file defines the TypeScript interfaces for all data flowing into and out of 
 * the CI-Score and Risk-Fit Score calculation service. Consistency is critical.
 */

// --- INPUT CONTRACTS ---
export interface UserInteractionEvent {
    type: 'view' | 'click' | 'scroll_depth'; // 사용자 행동 유형
    elementId: string; // 상호작용한 요소의 고유 ID (예: #cta-download)
    timestamp: number; // UTC 시간 (밀리초)
    value?: number; // 스크롤 깊이 등 수치적 값
}

export interface ContentMetadata {
    defectId: string; // 핵심 Defect ID (예: ArterialStiffening)
    severityLevel: 'Low' | 'Medium' | 'High'; // 콘텐츠의 위험도 분류
    targetAudienceGroup: '40-50s' | '50-60s';
    ctaType: 'Download' | 'ConsultationBooking' | 'ViewMoreContent';
}

export interface ApiInputPayload {
    userId: string;
    interactions: UserInteractionEvent[];
    contentMeta: ContentMetadata;
}


// --- OUTPUT CONTRACTS ---
/**
 * The result of the V5.0 Scoring Engine. 
 */
export interface ScoreResult {
    ciScore: number; // Content Intent Score (0.0 to 1.0) - 콘텐츠에 대한 사용자의 의도 점수
    riskFitScore: number; // Risk-Fit Score (0.0 to 1.0) - 사용자에게 노출된 위험 적합성 점수
    isCriticalAlert: boolean; // 최종적으로 Critical Alert 상태인지 여부
    suggestedAction: string; // 시스템이 추천하는 다음 액션 (예: 'Booking CTA 강조')
}

// --- MOCKUP UTILS ---
/**
 * Mock function to simulate API latency and successful data fetching.
 */
export const mockApiCall = async <T>(data: T, delayMs: number = 300): Promise<T> => {
    console.log(`[MockAPI] Simulating network delay of ${delayMs}ms...`);
    return new Promise(resolve => setTimeout(() => resolve(data), delayMs));
};

export type DashboardSchema = {
    input: ApiInputPayload;
    output: ScoreResult;
};