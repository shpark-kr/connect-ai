/**
 * @fileoverview Funnel Tracking Service: MiniFunnel의 모든 핵심 이벤트를 추적하고 전송하는 모듈.
 * 💡 목적: 단순히 클릭을 세는 것이 아니라, '사용자의 의도(Intent)'가 상승하는 순간(Score+5)을 포착하여
 * 재정적 위협 고지 -> CTA 전환까지의 경로를 측정합니다.
 */

// --- 타입 정의 (TypeScript Strictness 유지) ---
export type FunnelStage = "awareness" | "interest" | "consideration" | "action";
export type DefectId = string; // 예: LDL_CHOLESTEROL, ARTERIAL_STIFFENING 등

interface TrackingPayload {
    timestamp: number;
    user_session_id: string;      // 세션 고유 ID (브라우저 로컬 스토리지에서 가져오는 것을 가정)
    funnel_stage: FunnelStage;    // 현재 사용자가 어느 단계에 있는지?
    defect_id: DefectId;          // 어떤 핵심 위험 요인(Defect ID)이 주제인지?
    intent_score_increase: number; // 이 액션으로 인해 점수가 얼마나 올랐는지 (최소 1점 이상)
    source_page: string;          // 트래킹 이벤트가 발생한 페이지 경로
}

/**
 * FunnelTrackingService는 MiniFunnel의 모든 핵심 이벤트를 표준화된 방식으로 추적합니다.
 * @param payload - 전송할 데이터 객체 (필수 매개변수 검증 필수)
 * @returns {Promise<boolean>} API 호출 성공 여부
 */
export async function trackMiniFunnelEvent(payload: TrackingPayload): Promise<boolean> {
    // 🛡️ Guard Clause: 핵심 파라미터가 누락되었는지 먼저 확인합니다.
    if (!payload.defect_id || !payload.funnel_stage || payload.intent_score_increase <= 0) {
        console.error("[Funnel Tracking ERROR] 필수 매개변수 중 하나 이상이 누락되었습니다.");
        // 데이터 유실을 막기 위해 실패 로그만 남기고 호출은 차단합니다.
        return false; 
    }

    const TRACKING_API_ENDPOINT = process.env.TRACKING_API_URL || "https://api.onhyeon.com/v1/funnel/track";

    try {
        console.log(`[Funnel Tracking] -> ${payload.defect_id} (${payload.funnel_stage}) 이벤트 추적 시작...`);
        
        // 🚨 high_intent_action (Score +5) 전용 로직 분리 및 강조
        if (payload.intent_score_increase === 5) {
            console.warn("!!! CRITICAL ALERT: High Intent Action 감지! Score +5 부여 !!!");
            // 이 단계에 도달했다는 것은 사용자가 '재정적 시스템 오류'의 심각성을 인지했음을 의미합니다.
        }

        const response = await fetch(TRACKING_API_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Client-Source': 'OnHyeonFunnelTracker' // 출처 명확히 기록
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log(`[Funnel Tracking SUCCESS] 추적 완료. 서버 응답:`, data);
        return true;

    } catch (error) {
        console.error("[Funnel Tracking FATAL ERROR] 트래킹 API 호출 중 치명적인 오류 발생:", error);
        // 실패 시에도 사용자 경험에 영향을 주지 않도록 silent fail을 수행합니다.
        return false; 
    }
}

/**
 * 예제 사용법: high_intent_action이 발생했을 때의 호출 로직 (실제 웹 환경에서 버튼 클릭 핸들러 등에 연결)
 * const payloadExample = {
 *     timestamp: Date.now(),
 *     user_session_id: localStorage.getItem('sessionId') || 'anonymous',
 *     funnel_stage: "consideration", // 예시: 고려 단계
 *     defect_id: "ARTERIAL_STIFFENING", // 예시: 핵심 Defect ID
 *     intent_score_increase: 5, // High Intent Action! Score +5
 *     source_page: window.location.href
 * };
 * trackMiniFunnelEvent(payloadExample);
 */

// 이 모듈은 별도의 의존성 없이 순수 트래킹 로직만 담당합니다.