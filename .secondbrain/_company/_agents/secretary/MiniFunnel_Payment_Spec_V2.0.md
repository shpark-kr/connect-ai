# ⚙️ MiniFunnel 결제 플로우 및 API 명세서 V2.0

**작성 목적:** 온현의 '결함 진단 시스템(MiniFunnel)'을 통한 유료 서비스 결제 흐름과 기술적 요구사항 정의. (개발 요청용)
**버전:** 2.0 (최종 검토 필요)
**핵심 목표:** 사용자가 공학적 위기감을 느끼고 → 진단을 받고 → 오류 해결에 필요한 '필수 프로토콜'을 구매하도록 유도하는 결제 시스템 구축.

---

## 1. ✅ 서비스 개요 및 비즈니스 흐름 (Business Flow)

### A. 판매 원칙 재정의
*   **판매 상품:** 단순 정보 제공이 아닌, 사용자가 진단받은 특정 '공학적 Defect ID'를 해결하기 위한 **필수 유지보수 프로토콜(Protocol)**.
*   **가격 모델 (Pricing):** 1가지 핵심 패키지 판매 (예: E-M411 집중 케어 프로토콜). 추후 구독 모델 고려 가능하나, V2.0에서는 단일 결제에 집중.

### B. MiniFunnel User Flow (E2E 시퀀스)
1.  **진단 페이지 진입:** 사용자가 웹사이트에서 [MiniFunnel Diagnosis] 실행 → Defect ID(예: E-M411) 확인 및 위험도 수치화.
2.  **문제 제기 (Pain Point):** 시스템이 '현재 상태는 심각한 결함'임을 경고하며 위기감 조성.
3.  **해결책 제시 (Solution Gate):** 진단 결과만으로는 해결 불가함을 강조하며, "공식 프로토콜 다운로드/진행" 버튼 노출.
4.  **구매 유도:** [프로토콜 구매하기] 클릭 → 결제 페이지(MiniFunnel Payment Gateway)로 이동.
5.  **결제 실행:** 사용자가 카드 정보를 입력하고 결제를 시도.
6.  **처리 및 확인 (Success/Failure):** PG사 연동을 통해 승인 여부 확인 → 성공 시, 프로토콜 다운로드 링크 및 결과 페이지 제공 / 실패 시, 명확한 오류 메시지 안내.

---

## 2. 🛠️ 기술 명세: API Endpoint Spec

| 기능 | HTTP Method | Endpoint URI | 설명 | 요청 파라미터 (Body) | 응답 데이터 (Success) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **결제 시도** | `POST` | `/api/v2/payment/initiate` | 결제 시작 및 임시 주문 번호 생성. | `{ "diagnosis_id": "E-M411", "user_email": "...", "amount": 7000 }` | `{ "success": true, "order_id": "ORD-XXXXX", "payment_url": "https://pg.example/pay?id=..." }` |
| **결제 승인** | `POST` | `/api/v2/payment/confirm` | PG사 연동을 통해 결제를 최종 승인하고 주문 상태 변경. (PG Callback 처리) | `{ "order_id": "ORD-XXXXX", "transaction_code": "CODE123" }` | `{ "success": true, "status": "PAID", "protocol_link": "/download/E-M411.pdf" }` |
| **결과 조회** | `GET` | `/api/v2/payment/status/{orderId}` | 주문 상태 및 결제 가능 여부 확인 (백엔드에서 주기적 체크 필요). | - | `{ "success": true, "status": ["PENDING", "PAID", "FAILED"], "details": "..." }` |

---

## 3. 🚨 예외 처리 로직 (Exception Handling Matrix)

| 발생 시나리오 | 오류 코드 (내부/외부) | 사용자에게 보여줄 메시지 | 백엔드 동작 (Backend Action) |
| :--- | :--- | :--- | :--- |
| **PG사 네트워크 지연** | `E_NETW_TIMEOUT` | "결제 시스템에 일시적인 오류가 발생했습니다. 잠시 후 다시 시도해 주세요." | 재시도 횟수 카운트 및 최대 3회 제한. 실패 시 '추후 진단 요청' 유도. |
| **카드 승인 거절** | `E_CARD_DECLINE` | "결제하신 카드사에서 거래가 거절되었습니다. 결제 수단을 확인하거나 고객센터로 문의해주세요." | 주문 상태를 'FAILED'로 변경하고, 에러 사유 코드(예: Limit Overrun)를 기록함. |
| **미진단 사용자** | `E_NO_DIAGNOSIS` | "먼저 MiniFunnel 진단을 완료하여 결제할 프로토콜을 확인해주세요." | 결제 플로우 이탈 및 [MiniFunnel Diagnosis] 페이지로 리다이렉트. |
| **이미 구매한 상품** | `E_ALREADY_PURCHASED` | "사장님! 이미 해당 프로토콜은 다운로드 받으셨습니다. 최신 버전으로 다시 받아보시겠어요?" | 성공 메시지와 함께 재다운로드 링크를 제공하며, 사용자 경험을 해치지 않도록 처리. |

---
**[기술 요약]**
*   결제 플로우는 **비동기(Asynchronous)** 방식으로 설계되어야 합니다. (PG Callback 필수)
*   모든 트랜잭션은 `order_id`를 기반으로 원자성을 유지해야 합니다.