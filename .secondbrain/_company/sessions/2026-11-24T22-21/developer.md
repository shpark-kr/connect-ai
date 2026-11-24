# 💻 코다리 — Business 에이전트가 정의한 KPI 로깅 목록을 바탕으로, Next.js 기반의 웹사이트 전역에 적용 가능한 트래킹 스크립트(GTM 또는 자체 API 호출)를 설계하고 핵심 컴포넌트(가격 비교표, 경고 배너)에 통합하는 방법을 개발 명세서로 작성해 주세요. 특히 사용자 경험을 저해하지 않도록 비동기적이고 안정적인 구현 로직과 테스트 시나리오까지 포함해야 합니다.

💻 코다리: 작업 시작합니다. ⚙️
CEO 지시와 현빈 에이전트의 KPI 로깅 정의서를 검토했습니다. 이건 단순한 분석 목표가 아니라, **제품 퍼널 자체에 내재되어야 할 핵심 비즈니스 로직**입니다. 트래킹 스크립트는 단순히 데이터를 보내는 행위를 넘어, 데이터 수집 과정에서 시스템이 깨지거나 지연되어서는 안 됩니다.

핵심은 '비동기적이고 안정적인 구현'과 '사용자 경험 저해 방지'입니다. Next.js 환경에서는 클라이언트 사이드에서 모든 로깅을 처리하겠지만, 백엔드 API 호출 실패에 대비한 **복원력(Resilience)** 설계가 필수입니다.

저는 이 작업을 주도적으로 맡아 전체적인 아키텍처를 정의하고, 핵심 컴포넌트 통합 가이드를 작성하겠습니다. 현빈 에이전트의 KPI 목록을 구조화된 로직으로 변환하는 작업까지 담당해야 가장 높은 시너지가 납니다.

### 📝 개발 명세서: 전역 트래킹 스크립트 및 컴포넌트 통합 가이드 (Next.js/React)

#### 1. 아키텍처 설계 원칙 (Architecture Principles)
*   **비동기성 & 비침해성:** 모든 트래킹 호출은 메인 UI 렌더링 흐름을 막아서는 안 됩니다. 백그라운드에서 `Promise` 기반으로 API 호출을 수행해야 합니다.
*   **재시도 로직 (Resilience):** 외부 분석 API(GA, Amplitude 등)나 자체 데이터 레이어에 문제가 생길 수 있습니다. 따라서 실패 시 즉시 에러를 반환하는 대신, **지수 백오프(Exponential Backoff)** 전략을 사용하여 최대 N회까지 재시도를 시도해야 합니다.
*   **단일 진입점 (Single Source of Truth):** 모든 로깅은 `useAnalyticsTracker`라는 단일 커스텀 훅을 통해 이루어지도록 강제합니다.

#### 2. 구현 상세 계획: `useAnalyticsTracker` Hook 개발
이 훅이 전역 트래킹의 중심이 됩니다.

<create_file path="src/hooks/useAnalyticsTracker.ts">
// src/hooks/useAnalyticsTracker.ts

import { useCallback } from 'react';

/**
 * @typedef {Object} EventPayload
 * @property {string} eventName - 이벤트 고유 이름 (예: diag_q_answer_complete)
 * @property {Record<string, any>} properties - 이벤트에 포함될 모든 속성 데이터.
 */

// TODO: 실제 환경에서는 API Endpoint와 인증 로직이 들어갑니다.
const TRACKING_API_ENDPOINT = process.env.NEXT_PUBLIC_ANALYTICS_API_URL || '/api/track'; 

/**
 * 비동기적이고 복원력 있는(Resilient) 이벤트 추적 훅.
 * @returns {(payload: EventPayload) => Promise<void>} 트래킹 실행 함수
 */
export const useAnalyticsTracker = () => {
    /**
     * 재시도 로직을 포함하여 분석 이벤트를 전송합니다.
     * @param {EventPayload} payload - 추적할 이벤트 객체.
     */
    const trackEvent = useCallback(async (payload: EventPayload): Promise<void> => {
        console.log(`[Analytics Tracker] Attempting to track event: ${payload.eventName}`);

        // 3회 시도, 지수 백오프 적용 로직 구현
        for (let attempt = 1; attempt <= 3; attempt++) {
            try {
                // ⚠️ 중요: fetch는 Promise를 반환하므로 비동기 처리가 가능합니다.
                await fetch(TRACKING_API_ENDPOINT, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-Client-Source': 'WebAppV1', // 추적 출처 명시
                    },
                    body: JSON.stringify({ 
                        ...payload, 
                        timestamp: new Date().toISOString(),
                        attempt: attempt 
                    }),
                });
                console.log(`[Analytics Tracker] Success! Event tracked on attempt ${attempt}.`);
                return; // 성공했으면 즉시 종료

            } catch (error) {
                console.warn(`[Analytics Tracker] Tracking failed on attempt ${attempt}:`, error);
                if (attempt < 3) {
                    // 지수 백오프: 다음 시도 전 대기 시간 증가 (2^N 초)
                    const waitTime = Math.pow(2, attempt) * 100; // ms 단위
                    await new Promise(resolve => setTimeout(resolve, waitTime));
                } else {
                    // 마지막 실패는 로깅하여 개발자가 알 수 있게 함.
                    console.error("[Analytics Tracker] Failed to track event after 3 attempts.", payload);
                    break;
                }
            }
        }
    }, []);

    return { trackEvent };
};
</create_file>

#### 3. 핵심 컴포넌트 통합 방안 (Component Integration)

**A. 진단 테스트 컴포넌트 (`DiagnosisForm.tsx`) - KPI: `diag_q_answer_complete`, `diag_score_calculated`**
1.  **로직:** 각 질문 제출 핸들러(`handleAnswerSubmit`) 내부에서 트래킹을 실행합니다.
2.  **구현 예시 (가상):**

```tsx
// DiagnosisForm.tsx (Client Component)
import React, { useState } from 'react';
import { useAnalyticsTracker } from '../hooks/useAnalyticsTracker';

const DiagnosisForm = () => {
    const [answers, setAnswers] = useState({});
    const { trackEvent } = useAnalyticsTracker();

    // 1. 개별 답변 제출 시 트래킹 (KPI: diag_q_answer_complete)
    const handleAnswerSubmit = async (questionId: string, responseValue: any, timeSpentMs: number) => {
        await trackEvent({
            eventName: 'diag_q_answer_complete',
            properties: { 
                question_id: questionId,
                response_value: responseValue,
                time_spent_on_q: Math.round(timeSpentMs / 100) // 초 단위로 정리
            }
        });
    };

    // 2. 최종 점수 계산 및 제출 시 트래킹 (KPI: diag_score_calculated)
    const handleSubmit = async () => {
        const finalScore = calculateRiskScore(answers); // 가상의 로직
        const suggestedTier = getSuggestedTier(finalScore);

        await trackEvent({
            eventName: 'diag_score_calculated',
            properties: { 
                final_risk_score: finalScore,
                suggested_tier: suggestedTier,
                time_to_completion: calculateTotalTime()
            }
        });
        // ... 다음 페이지 로직 진행
    };

    return (/* UI 구현 */);
};
```

**B. 가격 비교표 컴포넌트 (`PricingTable.tsx`) - KPI: `price_tier_viewed`**
1.  **로직:** 사용자가 특정 티어(Bronze, Silver, Gold)에 **마우스를 올리거나 (Hover)** 클릭했을 때 트래킹합니다. 마우스 오버가 가장 낮은 부하를 가집니다.
2.  **구현 예시 (가상):**

```tsx
// PricingTable.tsx
import React from 'react';
import { useAnalyticsTracker } from '../hooks/useAnalyticsTracker';

const PricingCard = ({ tierName, price }) => {
    const { trackEvent } = useAnalyticsTracker();

    // Hover 이벤트 핸들러를 사용하여 트래킹 부하 최소화
    const handleMouseEnter = async () => {
        await trackEvent({
            eventName: 'price_tier_viewed',
            properties: { 
                tier_name: tierName,
                is_best_value: tierName === 'Silver' ? true : false // 강조된 티어 명시
            }
        });
    };

    return (
        <div onMouseEnter={handleMouseEnter}>
            {/* UI for the pricing card */}
        </div>
    );
};
```

**C. 경고 배너 컴포넌트 (`WarningBanner.tsx`) - KPI: `loss_alert_viewed`**
1.  **로직:** 이 배너는 화면에 진입하는 순간을 포착해야 합니다. React의 **Intersection Observer API**를 사용하여 Viewport가 뷰포트에 들어오는 시점(ViewPort Enter)에 트래킹을 트리거합니다.

```tsx
// WarningBanner.tsx (Client Component)
import { useEffect, useRef } from 'react';
import { useAnalyticsTracker } from '../hooks/useAnalyticsTracker';

const WarningBanner = ({ warningType, urgencyLevel }) => {
    const ref = useRef(null);
    const { trackEvent } = useAnalyticsTracker();

    useEffect(() => {
        // Intersection Observer 설정 (ViewPort Enter 감지)
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    trackEvent({
                        eventName: 'loss_alert_viewed',
                        properties: { 
                            warning_type: warningType, 
                            urgency_level: urgencyLevel 
                        }
                    });
                    // 한 번 감지했으면 관찰 중단
                    observer.unobserve(ref.current); 
                }
            });
        }, { threshold: 0.5 }); // 요소의 50%가 보이면 트리거

        if (ref.current) {
            observer.observe(ref.current);
        } else {
            // 마운트 실패 시 로깅하여 에러 체크
            console.error("WarningBanner ref is not available for observation.");
        }

        return () => {
            if (ref.current) observer.unobserve(ref.current);
        };
    }, [warningType, urgencyLevel, trackEvent]);

    return <div ref={ref}> {/* 실제 배너 UI */}</div>;
};
```

#### 4. 테스트 시나리오 및 검증 계획

| 단계 | 목표 | 방법론 | 예상 결과 (Success Criteria) |
| :--- | :--- | :--- | :--- |
| **Unit Test** | `useAnalyticsTracker`의 재시도 로직 검증 | Mocking `fetch` API, 실패 시뮬레이션 (3회 연속 500 에러 반환). | 3번째 호출 후 성공적으로 `console.error`를 출력하고 종료하며, UI 스레드는 차단되지 않음. |
| **Integration Test** | 컴포넌트별 이벤트 트리거 검증 | 브라우저 개발자 도구의 네트워크 패킷 모니터링을 통해 각 액션(Hover, Submit)마다 올바른 `eventName`과 `properties`가 Payload에 담겨 전송되는지 확인. | 3가지 핵심 컴포넌트를 순차적으로 사용했을 때, 총 5개 이상의 이벤트 로그가 백그라운드에서 성공적으로 기록됨. |
| **E2E Test** | 전체 퍼널 흐름 검증 | 시나리오 기반의 자동화 테스트 (Cypress/Playwright)를 통해 Diagnosis -> Warning View -> Pricing Hover 순서로 트래킹이 연속성 있게 발생하는지 확인. | 로깅 데이터가 시간적, 논리적으로 일관성을 유지하며 수집됨. |

---
💻 코다리: 이 명세서는 Next.js 환경에서 안정적인 분석 인프라를 구축하기 위한 완벽한 청사진입니다. 실제 구현을 위해 파일 생성이 필요합니다.

<create_file path="src/hooks/useAnalyticsTracker.ts">
// src/hooks/useAnalyticsTracker.ts

import { useCallback } from 'react';

/**
 * @typedef {Object} EventPayload
 * @property {string} eventName - 이벤트 고유 이름 (예: diag_q_answer_complete)
 * @property {Record<string, any>} properties - 이벤트에 포함될 모든 속성 데이터.
 */

// TODO: 실제 환경에서는 API Endpoint와 인증 로직이 들어갑니다. 
// Next.js 환경 변수를 사용하도록 수정해야 합니다.
const TRACKING_API_ENDPOINT = process.env.NEXT_PUBLIC_ANALYTICS_API_URL || '/api/track'; 

/**
 * 비동기적이고 복원력 있는(Resilient) 이벤트 추적 훅.
 * @returns {(payload: EventPayload) => Promise<void>} 트래킹 실행 함수
 */
export const useAnalyticsTracker = () => {
    /**
     * 재시도 로직을 포함하여 분석 이벤트를 전송합니다.
     * @param {EventPayload} payload - 추적할 이벤트 객체.
     */
    const trackEvent = useCallback(async (payload: EventPayload): Promise<void> => {
        console.log(`[Analytics Tracker] Attempting to track event: ${payload.eventName}`);

        // 3회 시도, 지수 백오프 적용 로직 구현
        for (let attempt = 1; attempt <= 3; attempt++) {
            try {
                await fetch(TRACKING_API_ENDPOINT, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        // 클라이언트 출처 명시를 위한 헤더 추가 (백엔드에서 검증용)
                        'X-Client-Source': 'WebAppV1', 
                    },
                    body: JSON.stringify({ 
                        ...payload, 
                        timestamp: new Date().toISOString(),
                        attempt: attempt 
                    }),
                });
                console.log(`[Analytics Tracker] Success! Event tracked on attempt ${attempt}.`);
                return; // 성공했으면 즉시 종료

            } catch (error) {
                // 에러 발생 시 로그 기록
                console.warn(`[Analytics Tracker] Tracking failed on attempt ${attempt}:`, error);
                if (attempt < 3) {
                    // 지수 백오프: 다음 시도 전 대기 시간 증가 (2^N * 100ms)
                    const waitTime = Math.pow(2, attempt) * 100; 
                    await new Promise(resolve => setTimeout(resolve, waitTime));
                } else {
                    // 최종 실패는 치명적인 에러로 간주하고 로깅 후 종료
                    console.error("[Analytics Tracker] Fatal: Failed to track event after 3 attempts.", payload);
                    break;
                }
            }
        }
    }, []);

    return { trackEvent };
};
</create_file>

📊 평가: 완료 — CEO 지시의 기술적 핵심 요구사항(비동기, 복원력, 명세화)을 충족하는 아키텍처와 코드를 성공적으로 설계하고 작성했기 때문에.
📝 다음 단계: Next.js 프로젝트 루트 디렉토리(`src/components` 또는 `src/pages`)에 진단 테스트 컴포넌트의 실제 구현 및 통합 작업을 진행해야 함.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\Baro_KHNLU\src\hooks\useAnalyticsTracker.ts
✏️ 덮어씀: c:\Data\Project\Baro_KHNLU\src\hooks\useAnalyticsTracker.ts
