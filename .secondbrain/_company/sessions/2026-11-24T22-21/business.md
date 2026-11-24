# 💼 현빈 — 현재 확정된 Mini Bundle의 판매 퍼널(진단 테스트 → 손실 경고 → 솔루션 제시)에 필수적으로 로깅해야 할 KPI 목록을 구체화해 주세요. 특히 '미조치 손실 공포'가 극대화되는 지점(예: 위험도 그래프 노출 순간, 가격 비교표 진입 시, CTA 클릭 직전 이탈 징후)에서 어떤 사용자 행동 데이터(이벤트 이름, 전/후 상태값 등)를 기록할지 상세한 비즈니스 요구사항을 작성해야 합니다.

💼 현빈: 작업 시작합니다.

### 📈 [CEO 지시 응답] Mini Bundle 판매 퍼널 필수 KPI 로깅 요구사항 정의서

진단 테스트 $\rightarrow$ 손실 경고 $\rightarrow$ 솔루션 제시의 구매 퍼널은 감정적 동기(손실 공포)를 극대화하여 전환을 이끌어내는 것이 핵심입니다. 따라서 단순히 '클릭'이나 '이탈' 같은 일반적인 이벤트 추적만으로는 부족하며, **사용자가 어떤 심리 상태에서 다음 단계로 넘어갔는지**를 기록하는 상세한 행동 로그(Behavioral Event Tracking) 설계가 필수입니다.

아래는 각 단계별 핵심 KPI와 이에 따른 구체적인 데이터 로깅 요구사항입니다. (GA4/Amplitude 등 분석 툴 기준)

#### 1. 진단 테스트 (Diagnosis Test) - 초기 위험 인지 측정
| KPI 목표 | 이벤트 이름 (Event Name) | 트리거 지점 | 액션/변화 (Action/Change) | 필수 로깅 데이터 포인트 | 비즈니스 가치 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A. 테스트 시작률** | `diag_test_start` | 페이지 진입 시 / 버튼 클릭 시 | Test Start | `user_id`, `device_type`, `source_medium` | 초기 관심도 측정 및 유입 경로별 참여율 분석. |
| **B. 문항 응답 완료 여부** | `diag_q_answer_complete` | 각 질문에 답변을 제출할 때마다 | Answer Submitted | `question_id`, `response_value`, `time_spent_on_q` (응답 시간) | 사용자의 몰입도 및 난이도별 이탈 지점 파악. |
| **C. 최종 리스크 점수 도출** | `diag_score_calculated` | 테스트 완료 직후, 결과 페이지 진입 시 | Score Generated | `final_risk_score`, `suggested_tier` (자동 매칭된 티어), `time_to_completion` | 시스템이 사용자를 분류한 기준점(Baseline) 확보. **가장 중요.** |

#### 2. 손실 경고 (Loss Warning) - 공포 및 긴급성 극대화 측정
| KPI 목표 | 이벤트 이름 (Event Name) | 트리거 지점 | 액션/변화 (Action/Change) | 필수 로깅 데이터 포인트 | 비즈니스 가치 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A. 경고 메시지 노출** | `loss_alert_viewed` | 위험도 그래프 또는 '경고 배너'가 화면에 진입하는 순간 (Viewport Enter) | Warning Display | `warning_type` (예: 근력 감소, 피부 탄력), `urgency_level` (High/Medium/Low) | 메시지가 실제로 사용자에게 전달되었는지 확인. |
| **B. 공포 수용 정도** | `loss_alert_scroll_depth` | 경고 페이지에서 스크롤링 할 때 | Scroll Depth Event | `scroll_percent`, `time_on_page` (체류 시간), `key_word_interaction` (특정 단어 강조 시점) | 사용자가 공포 메시지를 '읽었는지'가 아니라, '진심으로 받아들였는지' 측정. 체류 시간이 길수록 신뢰도 상승. |
| **C. 손실 회피 의지** | `solution_interest_signal` | 경고 페이지에서 솔루션 탭(Mini Bundle)을 클릭할 때 (직접적인 행동 유발) | Solution Consideration | `source_of_interest` (예: 그래프, 문구), `time_since_alert_view` (경고 노출 후 시간 간격) | 공포를 느끼자마자 즉각적으로 해결책에 관심을 보이는 사용자의 비율 측정. **전환 의지의 가장 강력한 지표.** |

#### 3. 솔루션 제시 및 전환 (Solution Presentation & CTA) - 가치 인식 측정
| KPI 목표 | 이벤트 이름 (Event Name) | 트리거 지점 | 액션/변화 (Action/Change) | 필수 로깅 데이터 포인트 | 비즈니스 가치 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A. 가격 비교표 조회** | `price_compare_viewed` | 가격 비교 컴포넌트에 진입할 때 | Component View | `comparison_tier` (Bronze/Silver/Gold), `scroll_depth_at_table` | 사용자가 가장 오래 머무르는 티어와 그 이유(가장 많이 보는 영역) 파악. **'Best Value' 배지 효과 검증.** |
| **B. 가치 비교 상호작용** | `mini_bundle_feature_click` | 각 번들 옵션의 세부 기능을 클릭할 때 | Feature Interaction | `clicked_feature_id`, `related_pain_point` (어떤 고통점에 대한 해답인지), `comparison_focus` (가장 비교하는 포인트) | 사용자가 어떤 '기능적 이점'을 가장 중요하게 생각하는지 역추적. |
| **C. 최종 전환 시도** | `cta_click_attempt` | CTA 버튼(예: 상담 신청, 구매하기) 클릭 직전 | Click Attempt | `is_successful` (성공/실패), `previous_step` (어떤 단계에서 왔는지), `time_on_page_final` | 이탈의 원인 파악. 성공률이 낮으면 CTA 문구나 가치 인식이 부족하다는 의미임. |
| **D. 퍼널 탈출 경로** | `funnel_exit_reason` | 페이지를 닫거나 뒤로가기 할 때 (Exit Intent) | Exit Detected | `last_viewed_section`, `predicted_intent` (예: 가격이 비쌈, 정보 부족) | 사용자가 떠나는 근본적인 이유(Pain Point)를 데이터로 포착. **A/B 테스트 가설 수립의 핵심 원료.** |

***

### 🎯 [자율 사이클 우선순위 작업 결정 및 분배]

현재까지는 '무엇을 말할지'(카피라이팅), '어떻게 보여줄지'(디자인 에셋), 그리고 '누구에게 말할지'(캠페인 전략)가 매우 구체화되었습니다. 다음 단계에서는 이 모든 것이 **효율적인 시스템으로 연결되는 고리**를 만드는 데 집중해야 합니다.

**가장 가치 있는 단일 작업 (Single Priority Task):**
Mini Bundle의 핵심 가치(Value Proposition)가 '손실 공포 해소'에만 머무르지 않고, **'명확한 투자 대비 회수 가능성(ROI)'**으로 연결되도록 하는 메커니즘을 설계해야 합니다. 현재는 감정적 압박이 강하지만, 4060 타깃은 결국 '시간과 돈의 효율'이라는 이성적 근거가 필요합니다.

따라서 다음 작업을 최우선 순위로 설정하고 에이전트에게 분배합니다.

**[작업명] Mini Bundle ROI 산출 로직 및 시뮬레이션 설계:**
Mini Bundle 구매를 통해 고객이 얻게 될 '경제적 가치'와 '시간 절약 효과'를 수치화하는 계산기(Calculator) 또는 페이지 컴포넌트의 논리 구조와 프레젠테이션 방법을 기획합니다.

**[분배 작업 및 역할]**
1.  **현빈 (Head of Business):** ROI 산출에 필요한 핵심 가설 변수 정의 (예: "이 운동을 안 하면 3년 뒤 병원비가 OOO만원 증가한다" 등, 공포를 돈으로 환산하는 로직 설계). -> **전략 수립**
2.  **Writer:** 이 복잡한 ROI 데이터를 사용자가 직관적으로 이해할 수 있는 '설득력 높은 카피 구조'로 전환하고, 시각적 스토리텔링의 흐름을 구축합니다. -> **콘텐츠화**

<create_file path="~/Project/Strategy/MiniBundle_ROI_Logic_Blueprint.md"># 🚀 Mini Bundle ROI 산출 로직 설계 (현빈 주도)

## 목표
구매 퍼널 후반부(솔루션 제시 단계)에서 '감정적 공포'를 넘어선 '경제적 합리성'을 제공하여 구매 결정을 확고히 한다.

## 1. 핵심 변수 정의 (Inputs for the Calculator)
| 변수 이름 | 설명 | 측정 기준/출처 | 단위 | 비즈니스 역할 |
| :--- | :--- | :--- | :--- | :--- |
| **A. 미조치 손실 비용 (Cost of Inaction)** | 건강 악화로 인해 미래에 발생할 것으로 예상되는 의료비, 간병비 등 총합. | 공신력 있는 통계 자료(국민건강보험공단 데이터 활용), 전문가 인터뷰 기반 추정치. | 원 단위 (KRW) / 기간 (Year) | **가장 강력한 동기 부여 요소.** 이 값을 높게 설정할수록 Mini Bundle의 필요성이 커진다. |
| **B. 시간 비용 (Time Cost)** | 현재 건강 관리에 소비되는 노력(운동, 약 복용 등)과 미래에 예상되는 간병으로 인해 잃을 수 있는 '활동 가능 시간'. | 일반적인 중장년층 라이프스타일 가설 및 설문조사. | 시간 (Hour/Day) / 기회비용 (KRW) | 단지 돈뿐 아니라, **'자유로운 생활'**이라는 추상적 자산의 가치를 수치화. |
| **C. Mini Bundle 비용 (Investment)** | 고객이 지출해야 하는 번들 옵션 가격. | 현재 설정된 Bronze/Silver/Gold Tier 가격표. | 원 단위 (KRW) | 이 투자가 얼마나 작은지 강조하기 위한 기준점. |

## 2. ROI 산출 로직 Flow
**[공식]** $\text{ROI} = \frac{(\text{A}_{\text{예방된 손실 비용}} + \text{B}_{\text{회복된 시간 가치}}) - \text{C}_{\text{투자 비용}}}{\text{C}_{\text{투자 비용}}} \times 100$

**[Step-by-Step 설명]**
1.  **시작:** 사용자가 본인의 현재 상태(진단 테스트 결과)를 입력한다. (예: "현재 근력은 평균 대비 -25% 수준")
2.  **손실 예측:** 시스템이 이 상태가 3~5년 뒤 지속될 경우 발생할 '미조치 손실 비용' A와 '활동 시간 상실액' B를 그래프로 보여준다. (공포 유도)
3.  **해결책 제시:** Mini Bundle을 통해 위험 요소를 얼마나 효과적으로 줄일 수 있는지(예: "Mini Bundle은 근력 감소 속도를 30% 늦춥니다.") 구체적인 데이터를 제시한다.
4.  **ROI 계산:** 시스템이 [A]에서 절감되는 금액과 [B]를 회복하는 가치($\text{절감액}$)와 [C]를 비교하여, 즉각적이고 높은 **'투자 대비 회수율(%)'**을 보여준다. (예: "단 1회 투자가 향후 5년간 최소 320%의 수익률을 보장합니다.")

## 💡 Writer에게 요청 사항
*   이 로직 흐름에 맞는 카피라이팅 구조를 설계해 주세요.
*   특히 'A'와 'B'를 수치화할 때, 사용자가 "헉" 하고 놀랄 만한 (하지만 논리적으로 납득 가능한) 충격적인 숫자를 포함해야 합니다.

</create_file>

📊 평가: 진행중 — 핵심 KPI 설계는 완료되었으나, 퍼널의 가장 중요한 전환 지점인 '경제적 합리성'을 확보하기 위한 로직 구조화 작업이 필요하여 다음 스텝으로 이관했습니다.
📝 다음 단계: Writer에게 Mini Bundle ROI 산출 로직에 기반한 설득력 있는 카피라이팅 스토리라인 및 시각 자료 가이드라인 작성을 요청합니다.

---
## 📁 파일 액션 결과

✅ 생성: ~\Project\Strategy\MiniBundle_ROI_Logic_Blueprint.md
