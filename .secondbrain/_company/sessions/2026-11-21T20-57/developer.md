# 💻 코다리 — MiniFunnel의 핵심 전환 로직(API Gateway)에 A/B 테스트 기능을 추가합니다. 최소 두 가지 변수(예: CTA 문구 A vs. B, 혹은 색상 테마 A vs. B)를 실시간으로 배분하고, 각 그룹별 사용자 행동 데이터(클릭 시점, 이탈률 등)가 무결하게 수집 및 기록될 수 있도록 백엔드 로직을 업데이트해주세요. (테스트 환경 분리 필수)

💻 코다리: 작업 시작합니다. ⚙️

CEO님의 지시사항을 확인했습니다. MiniFunnel의 핵심 전환 로직에 A/B 테스트 기능을 통합하는 건 단순한 기능 추가가 아니라, 제품 수익화 파이프라인 전체의 **무결성**과 **분석 가능성**을 근본적으로 강화하는 작업입니다. 🧐

A/B 테스트는 무작위 배분이 핵심이며, 가장 중요한 것은 '누구에게 어떤 변수(Variant)를 노출했는지' 그리고 그 이후 '어떤 행동(Event)'이 발생했는지를 완벽하게 매핑하고 로그에 남기는 것입니다. 이걸 놓치면 데이터가 깨지는 거나 마찬가지예요.

현재 작업 대상은 `miniFunnelApiController.ts`입니다. 이 파일의 구조를 먼저 파악해야 A/B 로직을 가장 적절한 지점(Gateway)에 주입할 수 있습니다. 변수를 CTA 문구와 배경색 테마 두 가지로 설정하고, 테스트 환경 분리까지 고려하겠습니다.

**[작업 계획]**
1.  **현재 상태 파악:** `miniFunnelApiController.ts`의 내용을 읽어 현재 데이터 흐름을 이해합니다.
2.  **A/B 로직 설계 및 구현:** API Gateway 레벨에서 사용자 ID를 기반으로 50:50 무작위 배분(Bucketing) 로직을 추가합니다. (테스트 환경 분리 고려).
3.  **로깅 시스템 통합:** 어떤 변수 조합이 노출되었는지 기록하는 전용 `VariantExposureService`를 만들고, 컨트롤러에서 이를 호출하여 로그에 반영합니다.

먼저 현재 컨트롤러의 구조부터 확인하겠습니다.

<read_file path="C:\Users\USER\Desktop\MiniFunnelAutomation\src\controllers\miniFunnelApiController.ts"/>

📊 평가: 진행중 — 핵심 파일의 기존 로직을 파악해야 A/B 테스트 게이트웨이를 안전하게 설계할 수 있습니다.
📝 다음 단계: `miniFunnelApiController.ts` 내용을 바탕으로, API Gateway에 A/B 로직 및 Variant Exposure Service를 추가 구현합니다.

---
## 📁 파일 액션 결과

📖 읽기: ~\Desktop\MiniFunnelAutomation\src\controllers\miniFunnelApiController.ts (60줄, 2.7KB)
```
 1	/**
 2	 * @module miniFunnelApiController
 3	 * @description MiniFunnel MVP의 모든 클릭/전환 추적 요청을 처리하는 백엔드 컨트롤러입니다.
 4	 * 이 파일은 API 게이트웨이 역할을 하며, 트래픽 부하 및 유효성 검증을 최우선합니다.
 5	 */
 6	
 7	import { TrackingService } from '../services/trackingService';
 8	import { TrackRequestData } from '../types';
 9	
10	// Mock DB Connection (실제 환경에서는 Sequelize, Prisma 등 ORM 연결 필요)
...
```

[시스템: read_file 결과]
파일: ~\Desktop\MiniFunnelAutomation\src\controllers\miniFunnelApiController.ts (60줄)
```
 1	/**
 2	 * @module miniFunnelApiController
 3	 * @description MiniFunnel MVP의 모든 클릭/전환 추적 요청을 처리하는 백엔드 컨트롤러입니다.
 4	 * 이 파일은 API 게이트웨이 역할을 하며, 트래픽 부하 및 유효성 검증을 최우선합니다.
 5	 */
 6	
 7	import { TrackingService } from '../services/trackingService';
 8	import { TrackRequestData } from '../types';
 9	
10	// Mock DB Connection (실제 환경에서는 Sequelize, Prisma 등 ORM 연결 필요)
11	const mockDbLogger = async (data: any): Promise<void> => {
12	    console.log(`[DB LOGGING SUCCESS] Tracking Data Saved to DB:`, JSON.stringify(data));
13	    // 실제로는 await dbConnection.transaction(async trx => { ... }); 구문 사용
14	};
15	
16	/**
17	 * @api/v1/track-funnel 
18	 * MiniFunnel 페이지의 모든 전환 및 클릭 이벤트를 추적합니다.
19	 * POST 요청으로 데이터를 받습니다.
20	 * @param req - HTTP Request 객체 (RequestData 포함)
21	 * @param res - HTTP Response 객체
22	 */
23	export const trackMiniFunnelConversion = async (req: any, res: any): Promise<void> => {
24	    try {
25	        // 1. 입력 데이터 유효성 검사 및 구조화 (가드 로직 최우선)
26	        const requestData: TrackRequestData = req.body;
27	
28	        if (!requestData || !['source', 'defectId', 'funnelStage'].includes(requestData.funnelStage)) {
29	            console.error("Tracking Error: 필수 데이터 누락 또는 유효하지 않은 Funnel Stage입니다.");
30	            return res.status(400).json({ 
31	                success: false, 
32	                message: "Invalid tracking payload received." 
33	            });
34	        }
35	
36	        // 2. 핵심 비즈니스 로직 호출 (TrackingService 사용)
37	        const success = await TrackingService.processConversionEvent(requestData);
38	
39	        if (!success) {
40	             console.error("Tracking Error: 트래킹 서비스에서 처리할 수 없는 이벤트가 감지되었습니다.");
41	            return res.status(422).json({ 
42	                success: false, 
43	                message: "Failed to process conversion event due to internal validation." 
44	            });
45	        }
46	
47	        // 3. DB 기록 (트랜잭션 커밋)
48	        await mockDbLogger(requestData); // 성공적으로 로직을 통과하면 데이터베이스에 저장합니다.
49	
50	        res.status(200).json({ 
51	            success: true, 
52	            message: "Conversion event tracked and logged successfully." 
53	        });
54	
55	    } catch (error) {
56	        console.error("Critical API Error during Funnel Tracking:", error);
57	        // 내부 서버 에러는 500으로 처리하고 디버그 로그를 남깁니다.
58	        res.status(500).json({ success: false, message: "Internal Server Error during tracking process." });
59	    }
60	};
```
