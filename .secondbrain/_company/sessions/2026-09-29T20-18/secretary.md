# 📱 영숙 — 현재까지 확정된 모든 수익화 자산(가격 모델, Funnel 구조, 에러 핸들링)을 통합하여 MiniFunnel 결제 플로우 및 API 명세서 V2.0 초안을 작성해 주세요. 이 문서는 코다리에게 개발 요청을 할 수 있도록 구체적인 End-to-End 시퀀스와 예외 처리(Exception Handling) 로직까지 포함해야 합니다.

📱 영숙: 사장님, 지시사항 확인했습니다! 😊

현재까지 확정된 모든 수익화 자산(가격 모델, Funnel 구조, 에러 핸들링)을 통합하여 MiniFunnel 결제 플로우 및 API 명세서 V2.0 초안 작성이 가장 중요합니다. 개발에 들어가기 전, 이 **명세서가 곧 청사진**이 되거든요.

따라서 오늘 가장 가치 있는 단일 작업은 '통합된 기술 문서 작성'이며, 제가 내용을 정리하여 파일로 만들겠습니다. 이 문서를 바탕으로 코다리 개발자님께 요청하면 됩니다. ✨

아래에 MiniFunnel 결제 플로우 및 API 명세서 V2.0 초안을 생성했습니다. 확인해 주시고 혹시 빠진 부분이 있다면 말씀해주세요! 📝

***

### 📄 MiniFunnel Payment Flow & API Spec V2.0 (초안)

<create_file path="c:\Data\Project\connect-ai\.secondbrain\_company\_agents\secretary\MiniFunnel_Payment_Spec_V2.0.md"># ⚙️ MiniFunnel 결제 플로우 및 API 명세서 V2.0

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

</create_file>

***

📊 평가: 완료 — CEO님의 지시사항에 맞춰 핵심 기술 문서 초안을 완성하여 개발 요청 준비가 완료되었습니다.
📝 다음 단계: 사장님께서 이 명세서를 검토하시고, 혹시 추가하거나 수정할 부분이 있는지 피드백을 주시면 바로 반영하겠습니다! 😊

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\.secondbrain\_company\_agents\secretary\MiniFunnel_Payment_Spec_V2.0.md
