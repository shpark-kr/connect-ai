# 🔍 Researcher — Funnel Funnel의 성능 분석을 위한 필수 트래킹 매개변수(Tracking Parameters) 정의. '유입 채널 (Source)', '콘텐츠 유형 (Content Type: Reels/Blog/Longform 등)', 'CTA 위치 (Placement: Description Box/Carousel Last Slide)'를 반드시 포함하여, 이 데이터를 어떻게 수집하고 어떤 형태로 구조화해야 가장 정확한 Funnel 분석이 가능한지 상세 리포트를 작성하십시오.

🔍 Researcher: 작업 시작합니다.

CEO님의 지시사항과 전체 목표를 종합적으로 분석한 결과, 현재 가장 시급하고 가치 있는 단일 작업은 **'측정 가능한 Funnel 파이프라인의 데이터 구조화 및 표준화'**입니다. 콘텐츠 제작(Writer), 디자인 구현(Designer)에 앞서, 어떤 데이터를 어떻게 측정할지 정의하는 것이 최우선 과제입니다.

아래는 Funnel 성능 분석을 위한 필수 트래킹 매개변수 정의 및 데이터 수집/구조화 상세 보고서입니다. 이 리포트는 모든 콘텐츠 에이전트(Writer, Instagram, YouTube 등)가 준수해야 할 **'온현 표준 추적 가이드라인'**으로 활용되어야 합니다.

---

## 📊 Funnel 성능 분석을 위한 트래킹 매개변수 정의 및 구조화 보고서

### 1. 목적 및 필요성 (Why?)

현재 회사의 목표는 단순한 콘텐츠 노출이 아니라, **‘막연한 불안감’**을 자극하여 **‘진단 도구 Mini-App 상호작용’**으로 유도하는 Funnel 구축입니다. 이 전환 과정의 효율성을 과학적으로 증명하고 최적화하기 위해서는 모든 사용자 여정(User Journey) 단계에서 누가, 어떤 경로를 통해, 무엇에 흥미를 느껴 진입했는지를 100% 추적할 수 있는 구조가 필수적입니다.

### 2. 핵심 트래킹 매개변수 정의 (What to Track?)

| 매개변수명 | 역할 및 정의 | 예시 값 | 중요도 | 비고 (활용 목적) |
| :--- | :--- | :--- | :--- | :--- |
| **Source** (유입 채널) | 사용자가 콘텐츠에 도달한 최종 경로. 트래픽의 성격을 파악합니다. | `youtube`, `instagram_reel`, `naver_search`, `blog_direct` | ⭐⭐⭐ | CPA(Cost Per Acquisition) 계산 및 채널별 기여도 분석. |
| **Content Type** (콘텐츠 유형) | 유입을 발생시킨 콘텐츠의 형식. 어떤 형태의 정보가 효과적인지 파악합니다. | `longform`, `shortreel`, `carousel_post`, `article` | ⭐⭐⭐ | 성공률이 높은 콘텐츠 포맷(예: 숏폼 후킹 vs 블로그 깊이) 식별. |
| **Placement** (CTA 위치) | Funnel CTA가 배치된 정확한 UI/UX 위치. 전환 설계의 최적점을 찾습니다. | `description_box`, `carousel_last_slide`, `blog_end_module` | ⭐⭐⭐⭐ | *가장 중요*. 사용자가 가장 많이 반응하는 '전환 지점'을 파악합니다. (A/B 테스트 핵심 변수) |
| **Campaign ID** (캠페인 식별자) | 특정 마케팅 활동(예: '연금 개정 공지')에 할당된 고유 ID. 여러 캠페인의 데이터를 분리합니다. | `202609_pension`, `hypertension_risk` | ⭐⭐ | 복수의 주제를 동시에 운영할 때 데이터 오염 방지. |
| **Specific Keyword** (핵심 키워드) | 콘텐츠의 핵심 주제나 사용자가 검색한 구체적인 키워드를 기록합니다. | `만성 염증`, `국민연금 수령액`, `40대 근력 운동` | ⭐⭐ | SEO 최적화 및 트래픽 유입 의도(Intent) 파악. |

### 3. 데이터 수집 메커니즘 (How to Collect?)

#### A. 프런트엔드 구현: UTM 매개변수 활용 (필수)
모든 외부 링크는 표준 **UTM** 매개변수를 사용하도록 강제합니다. 이는 가장 기본적이고 강력한 트래킹 방법입니다.

*   `?utm_source=[Source]&utm_medium=[Medium]&utm_campaign=[Campaign ID]`
*   **[추가 지침]**: `Placement` 변수는 UTM으로 직접 수집이 어려우므로, 랜딩 페이지(Landing Page)의 초기 스크립트에서 해당 페이지에 도달한 경로를 파싱하여 **세션 데이터로 기록**해야 합니다.

#### B. 백엔드 구현: Mini-App Funnel 로그 구조화 (핵심)
사용자가 진단 도구 Mini-App과 상호작용하는 순간은 가장 중요한 전환 지점입니다. 이 단계에서는 단순 UTM을 넘어, 다음과 같은 **이벤트 기반(Event-Based)** 로깅이 필요합니다.

1.  **진입 이벤트:** 사용자가 어떤 CTA를 클릭했는지 (`Placement` 기록).
2.  **상호작용 이벤트:** Mini-App 내에서 몇 개의 질문에 응답했고, 어느 단계에서 이탈했는지 (단계별 데이터 유효성 검증 로직과 연동).
3.  **전환 완료 이벤트:** 최종적으로 어떤 형태의 리드 정보(이메일/연락처)를 남겼는가.

### 4. Funnel 분석을 위한 데이터 모델 설계 (The Schema)

수집된 모든 데이터는 아래와 같은 단일화된 구조(Single Source of Truth)로 통합되어야 합니다. 이는 SQL 또는 Google Analytics의 이벤트 보고서 구조에 적합합니다.

| 필드명 (Column Name) | 데이터 타입 | 설명 | 필수 여부 | 출처/획득 방법 |
| :--- | :--- | :--- | :--- | :--- |
| **User ID** | String | 익명화된 사용자 식별자 | O | 쿠키 기반 트래킹 시스템 |
| **Timestamp** | DateTime | 데이터 기록 시점 (시간대 포함) | O | 서버 시간 |
| **Source** | String | 유입 채널 (UTM Source) | O | URL 매개변수/로그 파싱 |
| **Content Type** | String | 콘텐츠 유형 (Reels, Blog 등) | O | 초기 세션 변수 |
| **Campaign ID** | String | 캠페인 고유 식별자 | O | UTM Campaign |
| **Placement** | String | 전환 유도 위치 (Description Box 등) | O | JS 이벤트 리스너/Funnel 로직 |
| **Funnel Step** | Integer/String | Funnel의 현재 단계 (1~5단계 등) | O | Mini-App 내부 상태 추적 |
| **Action Taken** | String | 사용자의 행동 (클릭, 스크롤 깊이, 질문 응답) | O | JS 이벤트 리스너 |
| **Result Flag** | Boolean/String | 최종 전환 여부 (`Converted`/`Abandoned`) | O | Mini-App 서버 로직 |

### 📝 실행 계획 및 요약

1.  **[개발팀]**: 위 구조의 데이터 수집을 위한 추적 스크립트(Tracking Script)를 모든 플랫폼의 기본 페이지에 통합하여 배포하는 것을 최우선 순위로 합니다.
2.  **[Writer/Instagram/YouTube 에이전트]**: 콘텐츠 기획 시, **항상** 해당 콘텐츠가 위 구조 중 어떤 `Source`, `Content Type`, `Placement`를 담당할지 명시하도록 프로세스를 변경합니다.
3.  **결과물 활용**: 이 구조화된 데이터를 기반으로 Funnel 분석 대시보드를 구축하여, 각 에이전트의 성과를 객관적으로 측정해야 합니다.

---

📊 평가: 완료 — 트래킹 매개변수 정의 및 데이터 모델링을 통해 다음 단계 콘텐츠 기획에 필요한 가장 구체적이고 실행 가능한 구조화 보고서를 제공했습니다.
📝 다음 단계: 개발팀에게 위 Funnel 추적 로직(JS/API) 구현 요청하고, 'Mini-App'의 핵심 전환 지점 로그 수집 테스트를 진행해야 합니다.
