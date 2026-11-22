# 💻 코다리 — 최근 정의된 MiniFunnel 로직(특히 `high_intent_action` 이벤트 및 Score +5점 부여)을 실제 웹/랜딩 페이지 환경에 적용할 트래킹 코드 스크립트를 완성하고, 테스트 가능한 Boilerplate 코드로 분리하여 작성하십시오. 이 과정에서 모든 매개변수(`defect_id`, `mini_funnel_stage`)가 정확히 수집되는지 검증하는 로직을 포함해야 합니다.

💻 코다리: 작업 시작합니다.

CEO 지시사항을 검토했습니다. MiniFunnel 로직의 핵심은 단순히 트래픽을 측정하는 것이 아니라, **사용자의 의도 점수(Intent Score)**가 상승하는 '고급 전환 신호'를 포착하여 유료 상담 예약이라는 최종 목표에 연결시키는 것입니다. 이 `high_intent_action` 이벤트 추적 코드는 전체 데이터 파이프라인에서 가장 중요한 민감 정보입니다.

단순히 함수 하나를 만드는 것으로 끝내면 안 됩니다. 어떤 상황(어떤 페이지, 어느 단계)에서 호출되든 매개변수가 누락되지 않도록 엄격한 **타입 시스템과 기본값 체크**가 필수입니다. 따라서 `FunnelTrackingService`라는 모듈화된 서비스로 분리하고, 이를 검증하는 테스트 케이스를 함께 작성하겠습니다.

---

### ⚙️ 작업 계획 및 실행 (MiniFunnel Tracking Service 구축)

1.  **트래킹 서비스 파일 생성:** 재사용 가능한 TypeScript 기반의 `FunnelTrackingService` 모듈을 만듭니다. 이 서비스는 모든 Funnel 이벤트(Stage, Defect ID, Score 등)를 받아 표준화된 JSON 형태로 전송하는 책임을 가집니다.
2.  **핵심 로직 구현:** `high_intent_action`에 대한 5점 점수 부여 로직을 포함하고, 필수 매개변수 검증(Guard Clause)을 적용합니다.
3.  **테스트 스위트 실행:** 방금 만든 서비스가 실제 MiniFunnel 구조에서 예상대로 동작하는지, 그리고 모든 파라미터가 누락 없이 전송되는지 `e2e_funnel_cta_test_suite`를 이용해 검증하겠습니다.

<create_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\src\services\FunnelTrackingService.ts">
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
</create_file>

<run_command>cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe e2e_funnel_cta_test_suite.py</run_command>

---
📊 평가: 진행중 — 핵심 로직은 완성되었으나, 이 코드가 실제 웹/LP 환경에서 오류 없이 작동하는지 최종 검증이 필요합니다.
📝 다음 단계: 테스트 결과를 분석하여 (1) 트래킹 코드의 전역 배치 및 초기화 과정을 확정하거나, (2) 백엔드 스키마에 필요한 새 필드(e.g., `intent_score_increase`)를 반영하도록 데이터 파이프라인을 업데이트해야 합니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppDa`
```
=============================================

--- [🌐 Web Test] Funnel 'national_pension' 테스트 시작 ---
[✅ Data Injection]: 데이터 성공적으로 주입됨: 월 평균 150만원 부족
[❌ Web Flow ERROR]: 네트워크/요청 실패: HTTPSConnectionPool(host='www.onhyeon-site.com', port=443): Max retries exceeded with url: /signup/submit (Caused by NameResolutionError("HTTPSConnection(host='www.onhyeon-site.com', port=443): Failed to resolve 'www.onhyeon-site.com' ([Errno 11001] getaddrinfo failed)"))

--- [▶️ YouTube Test] Funnel 'national_pension' 테스트 시작 ---
[✅ Data Injection]: 링크 내부에 위험액 정보가 안전하게 포함됨.
[✅ Tracking Link Structure]: 예상 URL 생성 완료: https://analytics.example.com/track/?utm_source=youtube&funnel=national_pension&campaign=gap_cta&content=gap_cta
[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.


=============================================

--- [🌐 Web Test] Funnel 'health_insurance' 테스트 시작 ---
[⚠️ Data Injection WARN]: 데이터가 누락되었으나, CTA는 대체 텍스트를 안전하게 표시함.
[❌ Web Flow ERROR]: 네트워크/요청 실패: HTTPSConnectionPool(host='www.onhyeon-site.com', port=443): Max retries exceeded with url: /signup/submit (Caused by NameResolutionError("HTTPSConnection(host='www.onhyeon-site.com', port=443): Failed to resolve 'www.onhyeon-site.com' ([Errno 11001] getaddrinfo failed)"))

--- [▶️ YouTube Test] Funnel 'health_insurance' 테스트 시작 ---
[⚠️ Data Injection WARN]: 링크에 데이터 누락 대비 로직이 필요합니다.
[✅ Tracking Link Structure]: 예상 URL 생성 완료: https://analytics.example.com/track/?utm_source=youtube&funnel=health_insurance&campaign=gap_cta&content=gap_cta
[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.


=============================================

--- [🌐 Web Test] Funnel 'inheritance' 테스트 시작 ---
[✅ Data Injection]: 데이터 성공적으로 주입됨: 최소 3천만원 손실 우려
[❌ Web Flow ERROR]: 네트워크/요청 실패: HTTPSConnectionPool(host='www.onhyeon-site.com', port=443): Max retries exceeded with url: /signup/submit (Caused by NameResolutionError("HTTPSConnection(host='www.onhyeon-site.com', port=443): Failed to resolve 'www.onhyeon-site.com' ([Errno 11001] getaddrinfo failed)"))

--- [▶️ YouTube Test] Funnel 'inheritance' 테스트 시작 ---
[✅ Data Injection]: 링크 내부에 위험액 정보가 안전하게 포함됨.
[✅ Tracking Link Structure]: 예상 URL 생성 완료: https://analytics.example.com/track/?utm_source=youtube&funnel=inheritance&campaign=gap_cta&content=gap_cta
[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.

=============================================

[🚨 E2E 테스트 실패] 일부 필수 기능에서 오류가 감지되었습니다. 코드를 수정하고 재검증해야 합니다.
```
_✅_

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools\src\services\FunnelTrackingService.ts
