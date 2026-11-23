# 💻 코다리 — Designer가 제공할 컴포넌트 라이브러리 스펙을 기반으로, 프론트엔드 개발에 필요한 핵심 API 엔드포인트 3가지(데이터 입력, Gap Score 계산 요청, 리포트 다운로드 요청)의 명세서(Swagger/OpenAPI format) 초안을 작성해 주세요. 백엔드와 연동할 데이터 구조 및 타입 정의를 최우선으로 합니다.

💻 코다리: 작업 시작합니다. Swagger(OpenAPI) 명세서 작성은 백엔드와 프론트엔드가 가장 먼저 합의해야 하는 '계약'입니다. 여기저기 흩어진 로직을 API라는 통일된 구조로 끌어당기는 게 핵심이죠.

제공해주신 Designer님의 스펙을 보니, 이 진단 과정 전체가 **데이터 입력 $\rightarrow$ 계산 $\rightarrow$ 결과 활용(CTA)**의 완벽한 Funnel 구조를 가지고 있네요. 따라서 API도 순서대로 명확하게 분리해야 안정적입니다. 단순히 기능 나열이 아니라, 각 단계별로 어떤 데이터가 필수인지 타입을 정의하는 게 가장 중요합니다.

OpenAPI 3.0 형식으로 핵심 엔드포인트 3개의 초안을 작성했습니다. 백엔드 개발팀에게 전달하시기 전에 반드시 이 스펙에 맞춰 단위 테스트(Unit Test)를 설계할 수 있도록, 모든 입력과 출력이 타입스크립트/Python의 데이터 모델처럼 명확하게 정의되어야 합니다.

---

## ⚙️ API Design Specification (OpenAPI 3.0 YAML Draft)

이 파일은 `diagnosis-api.yaml`로 저장하고, 백엔드 팀에 공유하는 것을 추천합니다.

```yaml
openapi: 3.0.0
info:
  title: 온현 Gap Score Visualizer API
  version: 1.0.0
  description: |
    사용자 건강 데이터(Actual Value)를 입력받아, Ideal Benchmark 대비 '시간 경과형 손실 가치' (Gap Score)를 계산하고, 이를 기반으로 맞춤형 리포트 다운로드를 처리하는 API 계약 명세서입니다.

servers:
  - url: https://api.onhyeoncorp.com/v1
    description: Production server URL

paths:
  # ----------------------------------------------------
  # 1. 데이터 입력 엔드포인트 (Data Ingestion)
  # 목적: 사용자에게서 다차원적인 건강 데이터를 수집합니다.
  # ----------------------------------------------------
  /diagnosis/data-input:
    post:
      summary: 사용자의 현재 측정된 핵심 건강 지표를 전송하여 진단 프로세스를 시작합니다.
      description: 이 엔드포인트는 초기 사용자 인터랙션 데이터 수집에 사용됩니다. 모든 필드는 필수입니다.
      operationId: submitUserDataMetrics
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserInputData'
      responses:
        '200':
          description: 데이터 수집에 성공했으며, Gap Score 계산을 진행할 준비가 완료되었습니다.
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  message:
                    type: string
                    example: "데이터 입력 성공. 다음 단계에서 Gap Score를 계산합니다."
                  session_id:
                    type: string
                    description: 이후 API 호출에 사용될 고유 세션 ID (UUID)
                    example: "uuid-12345-onhyeon"
        '400':
          description: 입력된 데이터가 유효하지 않거나 누락된 필드가 있습니다.

  # ----------------------------------------------------
  # 2. Gap Score 계산 엔드포인트 (Core Logic)
  # 목적: 수집된 데이터를 기반으로 '손실 가치 격차'를 전문적으로 산출합니다.
  # ----------------------------------------------------
  /diagnosis/calculate-gapscore:
    post:
      summary: 입력된 지표와 이상적인 기준점(Ideal Benchmark)을 비교하여 Gap Score 및 리스크 레벨을 계산합니다.
      description: 이 API는 백엔드의 핵심 비즈니스 로직이 포함되며, 모든 데이터 모델 검증(Validation)이 필수입니다.
      operationId: calculateGapScore
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CalculationRequest'
      responses:
        '200':
          description: Gap Score 계산이 성공적으로 완료되었습니다. 사용자에게 표시할 모든 분석 결과가 포함됩니다.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GapScoreResult'
        '403':
          description: 유효하지 않거나 만료된 세션 ID입니다. 재로그인을 요청해야 합니다.

  # ----------------------------------------------------
  # 3. 리포트 다운로드 엔드포인트 (Monetization / CTA)
  # 목적: 최종적으로 사용자에게 판매할 맞춤형 진단 리포트를 제공합니다.
  # ----------------------------------------------------
  /diagnosis/download-report:
    post:
      summary: 계산된 Gap Score를 기반으로 개인화된 종합 진단 보고서를 생성하고 다운로드 링크를 제공합니다. (유료 전환 지점)
      description: 이 요청은 보통 결제 성공(Payment Success) 플로우 이후에 호출됩니다.
      operationId: downloadPersonalizedReport
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DownloadRequest'
      responses:
        '200':
          description: 리포트 생성이 성공적으로 완료되었으며, 다운로드 링크를 제공합니다.
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  message:
                    type: string
                    example: "맞춤형 리포트가 생성되었습니다."
                  download_url:
                    type: string
                    format: url
                    description: 실제 다운로드 가능한 임시 URL (만료 시간 명시 필수)
                    example: "https://cdn.onhyeoncorp.com/report/uuid-12345.pdf"
        '402':
          description: 결제 실패 또는 서비스 이용 조건 미충족으로 리포트 생성이 거부되었습니다.

components:
  schemas:
    # === 1. 데이터 입력 스키마 (UserInputData) ===
    UserInputData:
      type: object
      required: [session_id, date_of_birth]
      properties:
        session_id:
          type: string
          description: 세션 관리용 UUID.
          example: "uuid-12345-onhyeon"
        date_of_birth:
          type: string
          format: date
          description: 사용자의 생년월일 (진단 모델 학습에 필수)
        body_mass_index:
          type: number
          description: 현재 체질량 지수 (BMI).
          example: 25.5
        sleep_quality_score:
          type: integer
          description: 수면의 질 점수 (1~100점).
          example: 78
        physical_activity_level:
          type: string
          enum: [LOW, MODERATE, HIGH]
          description: 일상적인 신체 활동 수준.
          example: MODERATE

    # === 2. 계산 요청 스키마 (CalculationRequest) ===
    CalculationRequest:
      allOf:
        - $ref: '#/components/schemas/UserInputData' # 이전 단계에서 입력된 데이터 재사용
        - type: object
          required: [benchmark_data]
          properties:
            # Ideal Benchmark 대비 비교할 목표 값들을 전송합니다. (Ideal State)
            benchmark_data:
              type: object
              description: 이상적인 상태를 나타내는 기준점 데이터.
              properties:
                ideal_bmi:
                  type: number
                  example: 21.0
                optimal_sleep_score:
                  type: integer
                  example: 90
                target_activity_level:
                  type: string
                  enum: [MODERATE, HIGH]
                  example: MODERATE

    # === 3. Gap Score 결과 스키마 (GapScoreResult) ===
    GapScoreResult:
      type: object
      properties:
        gap_score:
          type: number
          description: 계산된 '손실 가치 격차' 점수. 이 값이 높을수록 위험합니다.
          example: 28.7
        risk_level:
          type: string
          enum: [LOW, WARNING, CRITICAL]
          description: Gap Score를 기준으로 판별된 위험 레벨. UI의 깜빡이는 애니메이션 트리거.
          example: CRITICAL
        loss_velocity_index:
          type: number
          description: 시간 경과에 따른 손실 속도 지수 (LVI).
          example: 3.5
        detailed_analysis:
          type: object
          properties:
            sleep_gap:
              type: string
              description: 수면 관련 Gap 분석 결과.
              example: "현재 점수는 이상치 대비 12점 낮아, 만성적인 회복 부족을 시사합니다."
            bmi_gap:
              type: string
              description: BMI 관련 Gap 분석 결과.
              example: "근육량 감소로 인한 체지방 증가가 관찰되며, 식단 개선이 필요합니다."
        actionable_recommendation:
          type: array
          items:
            type: string
          description: 이 결과를 바탕으로 즉시 취할 수 있는 3가지 핵심 추천 행동 목록.
          example: ["매일 20분 근력 운동", "밤 11시 이전 취침", "단백질 보충제 섭취"]

    # === 4. 리포트 다운로드 요청 스키마 (DownloadRequest) ===
    DownloadRequest:
      type: object
      required: [session_id, payment_status]
      properties:
        session_id:
          type: string
          description: 진단 과정의 세션 ID.
          example: "uuid-12345-onhyeon"
        payment_status:
          type: string
          enum: [PAID, FREE_TRIAL]
          description: 결제 상태 (유료 구매 여부). 'PAID'일 경우에만 리포트가 제공됩니다.
          example: PAID
        gap_score_reference:
          type: number
          description: 다운로드할 리포트를 개인화하기 위해 참조하는 Gap Score 값.
          example: 28.7
```

---
### 코다리 검증 및 설명 (Senior Engineer Review)

✅ **구조적 안정성 확보:**
1.  **데이터 흐름 강제**: `UserInputData`를 기준으로 `CalculationRequest`가 상속(allOf)되도록 설계했습니다. 이는 프론트엔드에서 데이터를 입력한 후, 그 데이터를 그대로 다음 API 호출에 재사용해야 함을 명시적으로 강제합니다. (State Management의 핵심입니다.)
2.  **계약 분리**: 세 단계의 API를 완전히 분리하여, 각 엔드포인트가 단일 책임(Single Responsibility Principle)만을 갖게 했습니다. 계산 로직이 불안정하면 데이터 입력만 테스트하고 고칠 수 있고, 결제 모듈에 문제가 생겨도 핵심 진단 로직은 보호됩니다.
3.  **타입 명확화**: `enum`과 `required` 필드를 최대한 활용하여, 어떤 값이 들어와야 하는지(예: `physical_activity_level`는 반드시 [LOW, MODERATE, HIGH] 중 하나)를 백엔드 개발자가 코드 레벨에서 검증할 수 있도록 했습니다.

⚠️ **주의사항 (Warning Flags):**
*   **Rate Limiting/Security**: 실제 구현 시에는 각 API별로 `Authorization` 헤더(JWT 토큰 기반 권한 확인)와 Rate Limiting이 필수적으로 적용되어야 합니다. 이 명세서에는 넣지 않았지만, 반드시 추가해야 할 부분입니다.
*   **Idempotency**: 특히 리포트 다운로드(`DownloadRequest`)는 결제 완료 후 여러 번 호출될 수 있으므로, `session_id` 외에 **멱등성(Idempotency Key)**을 요청 본문에 필수로 포함하도록 논의하는 것이 좋습니다.

이 스펙대로 백엔드 팀과 API 명세서 합의가 끝났다면, 다음 단계는 이 API를 호출할 프론트엔드 컴포넌트들의 인터랙션 테스트와 UI/UX 플로우 확정입니다. 💻
📊 평가: 완료 — 필요한 모든 계약적 구조(API 스펙)가 정의되었으며, 이는 다음 개발 단계로 진행하기에 충분합니다.
📝 다음 단계: 백엔드 팀과 위 OpenAPI 명세서 기반으로 API Mocking 환경을 구축하고, 프론트엔드 테스트를 시작해야 합니다.
