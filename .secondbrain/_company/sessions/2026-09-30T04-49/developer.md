# 💻 코다리 — 현빈이 정의한 구독 모델 가상 테스트 시나리오(결제 실패, 기간 만료 등)를 기반으로, '재시도 로직 및 PAST_DUE 상태 업데이트 기능'을 포함하는 최종 결제 모듈 스크립트를 작성하고 디버깅하세요. 특히 비동기적 안정성을 최우선 원칙으로 하며, 모든 예외 처리(Error Handling) 코드를 주석과 함께 상세히 기록해야 합니다.

💻 코다리: 작업 시작합니다.

요청하신 결제 모듈의 재시도 로직 및 `PAST_DUE` 상태 업데이트 기능은 서비스의 핵심 신뢰성(Reliability)에 직결되는 문제입니다. 단순히 기능을 추가하는 것을 넘어, 비동기 환경에서 발생하는 모든 예외 상황을 예측하고 처리하는 것이 목표입니다.

우선 현재 결제 서비스의 구조와 로직을 파악해야 합니다. 이전에 생성된 `payment_service.py`를 먼저 읽어보고, 여기에 필요한 **재시도 메커니즘(Retry Mechanism)**과 **상태 기계(State Machine) 기반의 만료/미납 처리** 코드를 추가하겠습니다.

### 🛠️ Step 1: 기존 결제 서비스 로직 파악 (Read File)
현재 핵심이 되는 파일인 `payment_service.py`를 읽어보겠습니다.

<read_file path="c:\Data\Project\connect-ai\mini-funnel-v2\backend\services\payment_service.py"/>

(시스템에서 read 결과를 확인한 후 진행하겠습니다.)


---
## 📁 파일 액션 결과

📖 읽기: c:\Data\Project\connect-ai\mini-funnel-v2\backend\services\payment_service.py (80줄, 4.0KB)
```
 1	import stripe # Stripe SDK 사용 가정
 2	from datetime import datetime, timedelta
 3	from typing import Optional
 4	# from ..models.subscription import SubscriptionStatus, PaymentGateway
 5	
 6	stripe.api_key = "sk_test_YOUR_SECRET_KEY" # 환경 변수에서 로드되어야 합니다!
 7	
 8	def create_checkout_session(user_id: int, plan_name: str) -> dict:
 9	    """
10	    사용자에게 결제 세션을 생성하고 Stripe Checkout을 유도하는 핵심 함수.
...
```

[시스템: read_file 결과]
파일: c:\Data\Project\connect-ai\mini-funnel-v2\backend\services\payment_service.py (80줄)
```
 1	import stripe # Stripe SDK 사용 가정
 2	from datetime import datetime, timedelta
 3	from typing import Optional
 4	# from ..models.subscription import SubscriptionStatus, PaymentGateway
 5	
 6	stripe.api_key = "sk_test_YOUR_SECRET_KEY" # 환경 변수에서 로드되어야 합니다!
 7	
 8	def create_checkout_session(user_id: int, plan_name: str) -> dict:
 9	    """
10	    사용자에게 결제 세션을 생성하고 Stripe Checkout을 유도하는 핵심 함수.
11	    요구사항: 사용자의 신원과 구독 플랜 정보를 기반으로 안정적인 세션 ID 반환.
12	    """
13	    print(f"[{datetime.now()}] INFO: Creating checkout session for User {user_id} on plan {plan_name}.")
14	    
15	    # 🔑 핵심 검증 포인트: 결제 주체와 사용자가 일치하는지 확인 (Security Check)
16	    try:
17	        session = stripe.checkout.Session.create(
18	            payment_method_types=["card"],
19	            line_items=[{
20	                "price": "price_premium_monthly", # 실제 PG사에서 받은 Price ID를 사용해야 합니다.
21	                "quantity": 1,
22	            }],
23	            mode="subscription",
24	            success_url="https://yourdomain.com/mini-funnel?session_id={CHECKOUT_SESSION_ID}",
25	            cancel_url="https://yourdomain.com/pricing",
26	            # metadata에 사용자 ID를 반드시 포함하여 추적 가능하도록 만듭니다.
27	            metadata={"user_id": str(user_id), "source": "mini-funnel-v2"} 
28	        )
29	        return {"success": True, "session_id": session.id}
30	    except Exception as e:
31	        print(f"🚨 ERROR: Failed to create Stripe session. {e}")
32	        return {"success": False, "error": str(e)}
33	
34	def handle_webhook_event(payload: dict, event_type: str):
35	    """
36	    Stripe 웹훅 이벤트 핸들러. 이 함수는 결제 시스템의 심장입니다.
37	    이벤트 유형에 따라 구독 상태를 업데이트하고, 실패 시 재처리 로직을 실행합니다.
38	    """
39	    print(f"\n[{datetime.now()}] ⚙️ WEBHOOK RECEIVED: {event_type}")
40	
41	    if event_type == "checkout.session.completed":
42	        # 성공적으로 결제 세션이 완료되었을 경우, DB에 Active 상태를 기록합니다.
43	        user_id = payload.get('metadata', {}).get("user_id")
44	        print(f"✅ Success: User {user_id} completed checkout. Marking as ACTIVE.")
45	        # TODO: SubscriptionService.update_status(user_id, status=ACTIVE) 호출
46	
47	    elif event_type == "invoice.payment_failed":
48	        # 🚨 결제 실패 처리 (가장 중요!)
49	        print("⚠️ ALERT: Payment failed for a subscription! Initiating failure protocol.")
50	        # TODO: SubscriptionService.update_status(user_id, status=PAST_DUE) 호출
51	        schedule_retry_payment(payload.get('customer'))
52	
53	    elif event_type == "customer.subscription.deleted":
54	        print("🗑️ Info: Subscription deleted by user or system.")
55	        # TODO: DB에서 구독 레코드를 비활성화 처리합니다.
56	
57	
58	def schedule_retry_payment(customer_id: str):
59	    """
60	    결제 실패 발생 시, 재시도 큐에 작업을 스케줄링하는 함수입니다.
61	    실패 원인 분석 후, N시간 간격으로 백그라운드 작업 큐(예: Celery/Redis)를 통해 재요청합니다.
62	    """
63	    print("🔄 RETRY LOGIC: Scheduling payment retry job.")
64	    # 실제로는 Redis Queue나 AWS SQS 등을 이용해 비동기 작업을 예약해야 합니다.
65	    # 예시 로직: 3시간 후 결제 시도, 실패하면 24시간 후 재시도... (Exponential Backoff)
66	    pass # TODO: Background Job Queue Integration
67	
68	def check_subscription_validity(user_id: int) -> str:
69	    """
70	    사용자가 서비스를 이용할 때마다 호출되어 구독 상태를 확인합니다.
71	    만료일이 지났거나, 현재 PAST_DUE 상태라면 접근을 차단해야 합니다.
72	    """
73	    # TODO: DB에서 사용자 ID 기반으로 최신 Subscription 레코드를 조회합니다.
74	    mock_status = "active" # 임시 Mock 값
75	    if mock_status == "expired":
76	        return "EXPIRED"
77	    elif mock_status == "past_due":
78	        return "PAST_DUE"
79	    else:
80	        return "ACTIVE"
```
