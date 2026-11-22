# 💻 코다리 — Instagram과 Business가 확정한 KPI 대시보드 구조 및 UTM 트래킹 매핑을 기반으로, 'Defect ID별 리드 전환 파이프라인(MiniFunnel)'의 기술적 데이터 흐름도(Data Flow Diagram)를 작성해 주세요. 이 다이어그램은 Google Analytics 또는 유사한 분석 툴에서 실제로 구현 가능한 API 호출 구조 및 필요한 필터링/전환 로직을 포함해야 합니다.

💻 코다리: 작업 시작합니다.

CEO님의 지시사항은 단순히 흐름도를 그리는 것을 넘어, 해당 파이프라인을 실제로 구현할 수 있는 **데이터 구조와 논리적 로직(Schema & Logic)**을 정의하는 것입니다. 시니어 엔지니어가 가장 중요하게 보는 것은 "이 데이터가 깨질 가능성"과 "어떻게 정확히 추적할 것인가?"입니다.

따라서 이 다이어그램은 Google Analytics 4 (GA4)를 기준으로 하며, 필요한 이벤트(`event_name`)와 매개변수(`parameter`)를 명확히 정의하여 개발자가 바로 코딩에 착수할 수 있도록 **기술 스펙(Technical Specification)** 형태로 작성하겠습니다.

---

### ⚙️ Defect ID 기반 리드 전환 파이프라인 (MiniFunnel) 데이터 흐름 기술 사양서

**목표:** 사용자의 콘텐츠 소비 여정 단계별 행동을 추적하고, 가장 높은 의도를 가진 지점(`High-Intent Point`)에서 MiniFunnel 전환을 유도하는 데 필요한 모든 데이터를 구조화한다.
**기준 플랫폼:** Google Analytics 4 (GA4) / UTM 기반 웹 로깅

#### I. 데이터 수집 레이어: 필수 이벤트 및 매개변수 정의 (The Data Plumbing)

모든 행동 추적은 **최소한의 공통 매개변수(Common Parameters)**를 포함해야 합니다. 이들은 모든 이벤트에서 일관되게 기록되어야 합니다.

| 파라미터명 (Key) | 데이터 타입 | 필수 여부 | 설명 및 값 예시 | 로깅 시점 |
| :--- | :--- | :--- | :--- | :--- |
| `content_id` | String | ✅필수 | 콘텐츠 고유 ID. (예: LDL-C\_Reel\_202611) | 모든 이벤트 발생 시 |
| `defect_id` | String | ✅필수 | 해당 콘텐츠가 다루는 핵심 Defect ID. (예: ArterialStiffening, HighLDL) | 모든 이벤트 발생 시 |
| `source_type` | String | ✅필수 | 유입 채널 유형. (예: Instagram\_Reel, YouTube\_Short) | 최초 세션 시작 시 |
| `mini_funnel_stage` | String | ✅필수 | 현재 사용자가 위치한 단계. (예: Impression, Engagement, Intent, Conversion) | 이벤트 발생 시마다 업데이트 |

---

#### II. MiniFunnel 핵심 로직 및 API 호출 구조 (The Logic Gates)

MiniFunnel은 단순 클릭 카운트가 아닌 '의도(Intent)'를 측정해야 합니다. 아래 4가지 핵심 단계별로 별도의 이벤트를 정의하고, 전환 흐름을 연결합니다.

| Funnel Stage | 사용자 행동 (Action) | GA4 이벤트명 (`event_name`) | 필수 매개변수/필터링 로직 | 의도 점수 부여 (Scoring Logic) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Impression** | 콘텐츠 노출 시작 | `content_view` | `video_duration_sec`: 최소 3초 이상 시 기록. | Base Score: 1점 |
| **2. Engagement** | 콘텐츠에 몰입 (정보 습득) | `deep_engagement` | `watched_ratio`: 영상 대비 시청 비율 (예: 70%). <br> *필터*: 특정 키워드(예: "재정적 위협", "경고") 노출 시간 기록. | Score +3점 (높은 몰입도) |
| **3. Intent** | 행동 의도 표출 (저장/공유) | `high_intent_action` | `action_type`: 'save' 또는 'share'. <br> *필터*: 공유 시, 특정 Defect ID 언급을 포함하는지 분석. | Score +5점 (행동의 증거) |
| **4. Conversion** | 리드 정보 제공 (최종 CTA 클릭) | `cta_click` | **UTM 매칭 검증:** `utm_campaign`이 'DefectID\_LeadGen'과 일치해야 함. <br> *매개변수*: `funnel_stage`: 'Conversion'. | Score +10점 (최고 의도) |

---

#### III. 데이터 파이프라인 아키텍처 및 로직 설계 (The Backend Schema)

GA4에서 이 데이터를 최종적으로 추출하고 분석하기 위해 필요한 백엔드/분석 쿼리 레벨의 로직을 정의합니다.

**1. [Data Ingestion Module] - 역할:** 모든 이벤트 데이터 수집 및 정규화
*   **입력:** `content_view`, `deep_engagement`, `high_intent_action`, `cta_click` (Raw Event Stream)
*   **처리 로직 (Pseudo-Code):**
    ```pseudocode
    FUNCTION ProcessEvent(event):
        IF event.source == 'Instagram' AND event.content_id IS VALID:
            data = {
                timestamp: event.time,
                user_id: get_hashed_user_id(event),
                defect_id: event.defect_id,
                stage: MapStage(event.event_name) // Stage 매핑 함수
            }
            RETURN data
        ELSE:
            THROW InvalidSourceError("Unknown source or missing content ID.")
    ```

**2. [Lead Scoring Engine] - 역할:** 사용자의 의도를 점수화하여 리드 등급 결정 (가장 중요!)
*   **입력:** 정규화된 이벤트 스트림
*   **처리 로직 (Pseudo-Code):**
    ```pseudocode
    FUNCTION CalculateLeadScore(user_session_events):
        total_score = 0
        for event in user_session_events:
            score = GetScoreByStage(event.stage) // Stage별 점수 반환
            IF event.is_first_time_interaction AND score > 5:
                // 초기에 높은 의도 행동을 보인 경우 가중치 부여
                total_score += (score * 1.2)
            ELSE:
                total_score += score

        LeadGrade = DetermineGrade(total_score) // 임계값 비교
        RETURN {final_score: total_score, lead_grade: LeadGrade}
    ```
*   **결과:** `High-Intent` (Score > 15점), `Medium-Interest` (7~15점), `Low-Awareness` (< 7점)

**3. [Reporting API Output] - 역할:** 최종 대시보드에 필요한 데이터 집계
*   **출력 Schema:**
    ```json
    {
      "week_start": "YYYY-MM-DD",
      "total_sessions": 1500,
      "high_intent_leads": [
        {"defect_id": "ArterialStiffening", "count": 45, "conversion_rate": 0.12},
        {"defect_id": "HighLDL", "count": 32, "conversion_rate": 0.09}
      ],
      "average_lead_score": 12.5
    }
    ```

---
✅ **자가 검증 및 결론:**
이 구조는 단순히 '어디로 이동했는지'를 넘어, 각 행동에 가중치(점수)를 부여하여 사용자의 '의도 점수'를 산출하는 엔진을 포함합니다. 이는 CEO님이 원하시는 "다음 콘텐츠 방향성 유도"라는 목표와 완벽하게 연결됩니다.

📊 평가: 완료 — 요청받은 기술적 상세 수준의 데이터 흐름도 및 API 로직 스펙이 정의되었습니다.
📝 다음 단계: 이 사양서(Specification)를 기반으로, 실제 GA4에서 데이터를 추출하고 점수화하는 백엔드 데이터 파이프라인을 구축하거나, 이를 테스트하기 위한 Mock 데이터를 생성해야 합니다.
