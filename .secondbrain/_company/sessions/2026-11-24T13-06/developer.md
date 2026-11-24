# 💻 코다리 — Writer의 시나리오와 Business가 제시한 테스트 가설 테이블을 통합하여, 시스템 통합 테스트 스위트(E2E Test Suite)를 위한 구체적인 '테스트 케이스 목록'과 각 단계별 필수 데이터 검증 로직(Validation Logic)을 포함하는 문서를 작성해 주세요. (예: [Input] Gap Score 70 -> [Process] 경고 패널 활성화 -> [Expected Output] 상담 요청 버튼 노출 및 성공 로그 기록)

💻 코다리: 작업 시작합니다.

CEO님의 지시사항과 동료 에이전트들의 산출물을 검토했습니다. Writer의 '미조치 손실 공포' 스토리보드와 Hyunbin의 A/B 테스트 가설은 마케팅 관점에서 매우 강력한 구조를 제시하고 있습니다. 하지만 이 전략적 아웃풋을 실제 웹사이트나 봇에 적용하려면, **이 모든 것을 포괄하는 기술적인 계약서**가 필요합니다.

단순히 '이렇게 되어야 한다'는 문구 나열로는 개발팀과 QA 팀에서 오해할 여지가 너무 많습니다. 우리는 *Input* 값 변화에 따라 시스템이 반드시 *Process*를 거쳐 특정 *Expected Output*을 내보내고, 그 과정을 **로그로 기록**한다는 것을 정의해야 합니다.

따라서 가장 가치 있는 단일 작업은 이 모든 전략적 요소를 기술적으로 검증 가능한 단위 테스트 케이스(Test Cases)와 로직 플로우 다이어그램으로 통합하는 것입니다.

### 📜 E2E Funnel Test Suite Specification (기술 명세서)

다음은 Writer의 스토리보드 단계별 흐름과 Hyunbin이 제안한 A/B 테스트 가설을 반영하여, **진단 과정(Diagnosis Flow)** 전체를 검증하기 위한 통합 End-to-End 테스트 스위트 문건입니다. 모든 개발자는 이 명세서를 기반으로 코딩하고 QA는 이 케이스를 통과할 때까지 반복해야 합니다.

---
#### 🎯 테스트 범위: Gap Score 기반 사용자 여정 (49k 진단 $\rightarrow$ 159k 전환)
**테스트 목표:** 사용자의 입력 데이터(Input) 변화에 따라 웹페이지의 감성적 위기감(Urgency)과 논리적 CTA가 정확히 반응하는지 검증한다.

#### 🧪 Test Case Structure: `[Scenario ID] - [Triggering Event]`

| Step | Scenario / Funnel Stage | Input Data (Input/Precondition) | Process Logic & Component Action | Expected Output (Visible UI/System Log) | Validation Logic Check |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1.0** | **Initial Hook (H1)** | N/A (페이지 로딩) | 🚨 `Crisis Peak` 애니메이션 활성화. 손실률 그래프가 가장 급격히 하강하는 지점을 시각적 위험으로 자동 노출. | H1: "지금 이대로 두면 [기능]은 몇 %나 사라졌습니까?" 문구와 함께 **깜빡이는 경고 배지**(`#D82B3A`)가 상단에 고정되어야 함. | `IsAlertPanelVisible()` == True & `AnimationState` == "Flashing" |
| **2.0** | **Diagnosis Start (49k)** | 사용자 입력 완료 (예: '매일 아침 옷 입기가 어렵다') | 💡 `Gap Score` 계산 엔진 가동. 점수 산출 및 실시간 피드백(Mini-CTA) 제공. | Gap Score가 획득되고, "당신의 손실률은 평균보다 높습니다"라는 **위험 경고 문구**가 출력됨. (A/B Test: 구체적 시나리오 제시 필수). | `GapScore` > 40 & `DangerWarningDisplayed()` == True |
| **3.0** | **Low Risk Path (A)** | Gap Score $\text{X} \in [60, 100]$ (정상 범위) | 📉 시스템은 위험도가 '낮음'으로 판단하고, 공포 유발 강도를 즉시 낮추고 다음 단계로 자연스럽게 안내. | CTA가 "더 알아보기" 또는 "예방 가이드 다운로드"와 같은 **정보성 콘텐츠** 위주로 전환되어야 함. (판매 압박 최소화). | `GapScore` > 60 & `CTA_Type` == "Informational" & `SalesPressureLevel` < 3 |
| **4.0** | **High Risk Path (B)** | Gap Score $\text{Y} \in [0, 39]$ (위험 신호) | 🔥 시스템은 위기감을 극대화하고, Hyunbin의 가설 2번(로드맵 제시)을 기반으로 전환 유도 로직 실행. | **159k 종합 안전망 패키지**가 메인 CTA로 강하게 노출되며, Gap Score 개선에 필요한 **'3단계 로드맵 플로우차트'**가 시각적으로 나타나야 함. | `GapScore` < 40 & `PrimaryCTA_Value` == 159000 & `RoadmapFlowChartVisible()` == True |
| **5.0** | **Conversion Attempt (A/B Test)** | 사용자 클릭: "안전망 구축하고 싶다" (구매 의사) | 🔒 결제 직전, 신뢰도 확보 로직 발동. Writer의 공신력 기반 문구와 Hyunbin의 A/B 테스트 가설 3번(전문가 인증 근거)을 조합하여 최종 확정 단계 진행. | **[A]** 판매 강조 ("지금 구매하세요!"). **[B]** 과학적 증거 제시 (논문, 임상 결과 등 아이콘 배치). 두 옵션 모두 성공적으로 노출되어야 함. | `PurchaseAttempt()` == True & (`Test_A` is visible OR `Test_B` is visible) |
| **6.0** | **Success Path** | 결제 완료 (성공 로그 기록) | ✅ 트랜잭션 로직 실행. 모든 데이터가 DB에 저장되고 사용자에게 감정적 안도감(Relief)을 주는 메시지를 보여줌. | "OOO님, 안전망 구축이 완료되었습니다. 앞으로 건강한 삶을 응원합니다." 등 **긍정적인 감사/확신 문구**와 함께 성공 로그 기록. | `TransactionStatus` == "Success" & `LogEntry_Created()` == True |

---
### ⚙️ 필수 데이터 검증 로직 (Validation Logic Detail)

이 테스트 스위트를 돌리기 위해, 다음의 **백엔드 및 프론트엔드 유효성 검사(Validation)**가 반드시 코드로 정의되어야 합니다.

1.  **Gap Score 계산 함수 (`calculate_gap_score(user_input: List[str]) -> float`):**
    *   Input (일상생활 시나리오) $\rightarrow$ 점수화 ($\text{RawScore}$) $\rightarrow$ 감성적 위험 가중치 적용 $\rightarrow$ 최종 Gap Score 반환.
    *   *(검증 포인트: 입력값의 순서와 내용 변화가 점수에 비선형적으로 반영되는지 확인)*

2.  **위기 경고 활성화 로직 (`activate_alert_panel(score: float)`):**
    *   `if score < THRESHOLD_MODERATE:` $\rightarrow$ Alert Level 2 (Moderate) 및 해당 시각적 컴포넌트 트리거.
    *   `if score < THRESHOLD_CRITICAL:` $\rightarrow$ Alert Level 3 (Critical) **강제 활성화** 및 깜빡임 애니메이션 적용. 이 임계값은 `process.env.CRITICAL_SCORE_THRESHOLD`에서 가져와야 합니다.

3.  **CTA 노출 로직 (`determine_cta(score: float)`):**
    *   Score $\ge 60$: CTA = Informational (49k 진단 유도)
    *   $20 \le$ Score $< 60$: CTA = Soft Conversion (로드맵 제시 + 정보 상품)
    *   Score $< 20$: CTA = Hard Conversion (159k 패키지 강제 노출 및 로드맵 플로우차트).

---
저는 이 명세서가 개발의 청사진이 될 것이라 확신합니다. 다만, 테스트 스위트를 작성하는 것만으로는 부족하고, **실제로 이 복잡한 Funnel을 여러 번 반복하여 시스템 안정성을 확보**해야 합니다.

따라서 다음 단계로는 이 통합된 시나리오를 기반으로 QA 프로세스를 자동화하고, 모든 핵심 컴포넌트의 장애 상황을 대비하는 것이 가장 중요합니다.

📊 평가: 진행중 — 전략적 요구사항이 너무 커서 이를 테스트할 수 있는 구조화된 환경(QA 스크립트) 정의가 필요함.
📝 다음 단계: 현빈과 함께 이 통합 명세서를 바탕으로, 실제 시스템에 적용할 E2E 테스트 자동화 스크립트를 작성하고 실행해야 함.
