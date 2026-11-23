# 💻 코다리 — Business팀이 확정한 3단계 상품 구조(Basic/Standard/Premium) 기반의 랜딩 페이지 A/B 테스트 환경 구축을 위한 기술 설계도를 작성해 주세요. 특히, 'Gap 수치 입력 → 임계점 비교 → 위험도 출력' 과정에서 필요한 데이터 처리 로직(API endpoint), 사용자 인증/세션 관리 방법, 그리고 결제 시스템 연동(Stripe 또는 국내 PG사)의 기본 구조를 포함해야 합니다.

💻 코다리: 작업 시작합니다.

CEO 지시가 매우 명확하고 핵심적입니다. 랜딩 페이지의 A/B 테스트 환경 구축은 단순한 프론트엔드 개발이 아니라, **사용자 심리를 데이터로 측정하고(Diagnosis), 그 결과를 수익화 구조에 완벽하게 매핑하는 (Funnel Engineering) 백엔드 로직 설계**가 선행되어야 합니다.

저는 이 과정을 '진단 엔진 기반의 3단계 Funnel Architecture'로 정의하고 기술 설계를 진행하겠습니다. 단순히 UI를 만드는 것이 아니라, 데이터 무결성과 확장성(Scalability), 그리고 가장 중요한 **에러 복구 로직(Resilience)**까지 고려한 설계가 필요합니다.

아래는 이 목표를 달성하기 위한 기술 설계도입니다. 모든 부분은 클라이언트-서버 간의 명확한 역할 분리와 테스트 케이스 기반으로 구조화했습니다.

---

# ⚙️ Defect ID 진단 Funnel Architecture Design Spec (v1.0)

## 1. 아키텍처 개요 및 기술 스택 제안
전체 시스템은 **SPA(Single Page Application)** 형태의 랜딩 페이지를 중심으로, 백엔드 API 서버가 모든 로직과 상태 관리를 담당하는 구조가 가장 효율적입니다.

| 레이어 | 역할 (Responsibility) | 권장 기술 스택 | 고려 사항 (Why?) |
| :--- | :--- | :--- | :--- |
| **Frontend (FE)** | 사용자 인터페이스, 데이터 입력, 결과 시각화 (Defect ID 그래프 렌더링), 상태 관리. | Next.js (React) + TypeScript + Tailwind CSS | SEO와 성능(SSR/SSG)을 확보하며, 복잡한 컴포넌트 구조에 유리합니다. |
| **Backend API (BE)** | 핵심 로직 처리, 사용자 인증, 진단 알고리즘 실행, 상품 데이터 조회. | FastAPI (Python) / Node.js (Express) + TypeScript | Python은 통계/데이터 처리에 강점이 있어 `Diagnosis Engine` 구현에 최적입니다. |
| **Database (DB)** | 사용자 정보(Profile), 세션 기록(Funnel State), 진단 점수 매트릭스 저장. | PostgreSQL (Postgres) | 관계형 데이터베이스로 트랜잭션 무결성 및 복잡한 쿼리 처리에 안정적입니다. |

## 2. 핵심 API 엔드포인트 설계 (The Data Pipeline)
진행 과정에서 발생하는 모든 상태 변화와 데이터를 처리할 메인 진단 흐름을 정의합니다.

### A. [Step 1] 사용자 입력 및 초기 진단 요청
*   **Endpoint:** `POST /api/v1/diagnose/initial`
*   **Body (Request):** `{ "user_id": "uuid", "session_token": "jwt_token", "input_data": { "hba1c": 6.5, "blood_pressure": "130/85", "lifestyle_score": 7 } }`
*   **Response:** `{ "status": "SUCCESS", "severity_index": 0.65, "recommended_funnel_state": "Basic" }`

### B. [Step 2] Gap 수치 분석 및 위험도 출력 (Core Logic)
이 부분이 가장 중요합니다. 단순히 점수를 주는 것이 아니라, **'어떤 Gap 때문에 어떤 상품을 써야 하는지'**를 결정해야 합니다.
*   **Endpoint:** `POST /api/v1/diagnose/calculate`
*   **Body (Request):** `{ "user_id": "uuid", "session_token": "jwt_token", "input_data": { ... } }`
*   **Logic Flow:**
    1.  DB에서 `Gap Matrix`를 조회합니다.
    2.  입력 데이터와 매트릭스를 비교하여 **'Critical Gap (임계점 초과)'** 리스트를 추출합니다.
    3.  추출된 Gap들의 심각도(Severity)에 따라 0~1 사이의 단일 `severity_index`를 계산합니다.
    4.  이 인덱스에 따라 Basic/Standard/Premium을 결정하고, 해당 근거 (예: "수면 부족 Gap으로 인해 Standard 패키지가 필요합니다.")를 반환합니다.

### C. [Step 3] 상품 정보 조회 및 최종 CTA 요청
*   **Endpoint:** `GET /api/v1/product/{tier}`
*   **Parameters:** `{ tier: "Standard" }`
*   **Response:** 해당 티어의 상세 구성, 가격, 기대 효능 등의 정적(Static) 데이터를 반환합니다.

## 3. 사용자 인증 및 세션 관리 (Authentication & Resilience)
진단 과정은 여러 단계에 걸치므로, 사용자가 이탈했다가 돌아와도 **'현재까지 진단된 Gap 수치'**를 기억해야 합니다.

1.  **인증 방식:** JWT(JSON Web Token) 기반의 Stateless 인증을 채택합니다. (매 요청마다 토큰 검증).
2.  **세션 관리:** `Funnel State` 테이블 (DB에 신설): 사용자 ID, 마지막 진단 시점, **현재 Gap Score Snapshot**, 현재 Funnel Step(0~4), 그리고 다음 예상 CTA를 저장합니다.
3.  **Gap 처리 로직의 안정성:** 모든 API 호출은 트랜잭션으로 묶여야 합니다. 만약 결제 실패 등으로 인해 세션이 끊기더라도, `Funnel State`에 기록된 정보를 통해 **'어디까지 진행했는지'를 보여주며 재진입(Re-entry)** 할 수 있도록 설계합니다.

## 4. 결제 시스템 연동 구조 (Payment Integration)
결제는 가장 오류가 많이 발생하는 지점이므로, '최소한의 시도'와 '자동 복구 로직'에 집중해야 합니다.

*   **PG사 선택:** 초기 테스트 단계에서는 **Stripe Checkout Session**을 활용하는 것이 가장 빠르고 글로벌 표준화되어 있습니다. (국내 PG사는 별도의 웹훅(Webhook) 처리가 필수적입니다.)
*   **핵심 구조: Webhook 기반 트랜잭션 검증:**
    1.  사용자가 결제 버튼 클릭 $\rightarrow$ FE가 Stripe Checkout URL로 리다이렉트.
    2.  Stripe는 PG사 게이트웨이를 통해 결제를 처리하고, **성공/실패 상태를 다시 Backend API의 Webhook 엔드포인트(`POST /api/v1/webhooks/payment`)로 전송**합니다. (클라이언트 측 실패에 의존하지 않음).
    3.  Backend는 이 웹훅을 받아 DB의 해당 `Funnel State`와 연동하여 **'구매 완료 플래그(Purchased Flag)'**를 업데이트하고, 상품 활성화 로직을 트리거 합니다.

---
### 📝 요약 및 다음 단계 Action Plan

| 항목 | 기술적 요구사항 | 비고 (Why?) |
| :--- | :--- | :--- |
| **데이터 처리** | `POST /api/v1/diagnose/calculate` 로직 구현 및 단위 테스트 필수. | Gap 수치 $\rightarrow$ Severity Index $\rightarrow$ Tier 매핑의 핵심 근거가 됨. |
| **State 관리** | `Funnel State` 테이블 설계 및 JWT를 활용한 세션 보존 메커니즘 구축. | 이탈 방지 및 재진입(Re-entry) 기능 확보. |
| **결제 연동** | Webhook 기반의 트랜잭션 검증 로직 (Stripe/PG사). | 결제 성공 여부를 클라이언트가 아닌 서버가 최종 결정하도록 강제함. |

---
📊 평가: 진행중 — 아키텍처와 데이터 흐름은 설계되었으나, 실제 코드로 구현하고 테스트해야 합니다.
📝 다음 단계: 백엔드(FastAPI)를 사용하여 `Diagnosis Engine`의 핵심 API 엔드포인트 (특히 `/diagnose/calculate`) 골격과 단위 테스트 케이스를 먼저 구축하겠습니다.
