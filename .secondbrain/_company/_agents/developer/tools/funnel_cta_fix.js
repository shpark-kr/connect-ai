/**
 * funnel_cta_fix.js
 * ---------------------------------------------------------------------
 * A/B Test 변수 누락 방지 및 Exit Intent 트래킹 보강 스크립트 (V1.1)
 * NOTE: 이 스크립트는 기존 <script> 태그의 추적 로직 앞에 삽입되어야 합니다.
 */

(function() {
    const trackFunnelEvent = (eventName, dataParams = {}) => {
        // 기본 데이터 파라미터 정의 (강제 값 설정)
        let mergedData = {
            ...dataParams,
            source_platform: window.devicePixelRatio > 1 ? 'mobile' : 'desktop', // 디바이스 체크 기반 플랫폼 추정
            timestamp: new Date().toISOString(),
            // A/B 테스트 변수가 누락된 경우 기본값을 주입하여 데이터 무결성을 확보함
            ab_test_group: localStorage.getItem('ab_test_group') || 'default' 
        };

        console.log(`[Funnel Tracker] Sending event: ${eventName}`, mergedData);

        // 실제 API 호출 로직 (여기에 기존 추적 스크립트를 통합/호출)
        // 예시: fetch('/api/track', { method: 'POST', body: JSON.stringify({event: eventName, data: mergedData}) });
    };

    // 1. Exit Intent Listener 추가 (페이지 이탈 직전 감지)
    let isExitIntent = false;
    window.addEventListener('mouseout', function(e) {
        // 마우스가 창 바깥으로 나갈 때만 발동하도록 조건을 걸어 오작동 방지
        if (!e.relatedTarget && !isExitIntent) { 
            trackFunnelEvent("exit_intent", { reason: "mouse_out" });
            isExitIntent = true;
        }
    }, false);

    // 2. 핵심 CTA 클릭 시 자동 실행 로직 (기존 추적 스크립트를 감싸는 역할)
    document.addEventListener('click', function(e) {
        const target = e.target;
        if (target.closest('[data-cta="solution"]')) {
            trackFunnelEvent("cta_clicked", { cta_type: "Solution Presentation" });
        } else if (target.closest('[data-cta="download"]')) {
             // 다운로드 CTA는 핵심 전환점이므로, 성공 여부까지 기록하는 것이 좋음
             trackFunnelEvent("cta_clicked", { cta_type: "Lead Magnet Download Start" }); 
        }
    }, true);

})();