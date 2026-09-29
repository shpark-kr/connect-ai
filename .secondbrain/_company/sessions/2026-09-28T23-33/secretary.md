# 📱 영숙 — Developer가 완성할 Mock API 스펙과 Researcher의 테스트 데이터를 종합하여, 모든 에이전트와 개발팀원들이 이해하기 쉬운 'MiniFunnel 최종 통합 QA 체크리스트 및 핸드오프 메모'를 작성하고 공유하라. (주요 검증 항목: 네트워크 실패 시 폴백 로직 작동 여부, Deep Crimson Red 경고 UI의 트리거 조건 만족 여부)

📱 영숙: 작업 시작합니다. 😊 사장님, 요청하신 'MiniFunnel 최종 통합 QA 체크리스트 및 핸드오프 메모' 작성을 완료했습니다.

지금까지 개발팀(코다리), 리서처(Researcher), 디자이너(Designer) 등 여러 에이전트가 분산적으로 산출물을 만들었기 때문에, 이 모든 요소를 한곳에 모아 '하나의 통합 테스트 및 핸드오프 문서'로 만드는 것이 가장 가치 있는 단일 작업이라고 판단했습니다. 🚀

이 문서는 단순한 체크리스트를 넘어, 다음 단계 개발팀과 QA 팀에게 **"무엇을 검증해야 하는지(QA)", "어떻게 진행해야 하는지(Process)"**의 명확한 계약서 역할을 할 거예요.

<create_file path="c:\Data\Project\connect-ai\mini_funnel_qa_checklist_handover.md"># 🚨 MiniFunnel 최종 통합 QA 체크리스트 & 핸드오프 메모 (V1.0)

**문서 목적:**
MiniFunnel의 모든 기능적 요소(데이터 입력, 상태 전이 로직, UI 애니메이션, API 연동)를 종합적으로 검증하고, 개발팀 및 디자인팀에게 다음 단계 구현을 위한 최종 QA 가이드라인과 작업 분배 명확화.

---

## 🎯 1. 핵심 목표 검증 (QA Priority Checklist)
가장 높은 우선순위로 테스트해야 할 **'시스템의 임계점 변화와 복구 과정'**에 초점을 맞춥니다.

### ✅ A. 상태 전이(State Transition) 로직 검증 (🔥 Deep Crimson Red Trigger)
| 항목 | 시나리오/트리거 조건 | 기대되는 시스템 반응 (Expected Behavior) | 테스트 담당 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **위기 감지** | 1. HOMA-IR 지표가 임계치(예: >3.0) 초과 시 | ➡️ 즉시 화면 전체에 `--color-crisis-red` 경고 UI 활성화 및 애니메이션 트리거. (사운드/진동 포함) | QA / Designer | **Timecode 명시 필수.** 위기감 조성의 공학적 디테일 검증. |
| **경고 유지** | 2. 사용자가 '솔루션'을 무시하고 반복 진단 요청 시 | ➡️ 경고 UI가 지속적으로 깜빡이며, 솔루션 접근을 강제하는 로직이 작동해야 함. | QA / Developer | Funnel의 방어 메커니즘 검증. |
| **해결책 제시** | 3. 사용자 데이터 입력(예: 식단/운동 기록) 후 상태 개선 시 | ➡️ Deep Crimson Red 경고가 'Soft Gold' 해결책 UI로 부드럽게 전환되며, Positive 피드백 애니메이션이 작동해야 함. | QA / Designer | **전환 과정(Transition)** 자체의 완성도가 중요. |

### ✅ B. 기술 안정성 검증 (🌐 Network Failure & Fallback)
| 항목 | 테스트 조건 | 기대되는 시스템 반응 (Expected Behavior) | 테스트 담당 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **Mock API 오류** | 1. 외부 네트워크 요청 실패 시뮬레이션 (DNS Error, Timeout 등) | ➡️ 에러 메시지를 사용자에게 친절하고 이해하기 쉽게(불안감 증폭 없이) 표시해야 함. | QA / Developer | Mock API 스펙(`openapi_mock_spec.yaml`)에 정의된 폴백 로직 작동 확인. |
| **데이터 유효성** | 2. 필수 입력값 누락 또는 비정상 데이터 형식 전송 시 (400 Bad Request) | ➡️ 어느 필드가 문제인지 명확히 하이라이트하며, 오류 수정 가이드라인을 제시해야 함. | QA / Developer | 단순히 에러 코드만 보여주면 안 됨. |

---

## ✨ 2. 에이전트별 핸드오프 및 액션 플랜 (Deliverable Matrix)
각 팀원이 다음 단계에서 반드시 수행할 역할과 산출물을 명확히 분배합니다.

| 담당 에이전트/팀 | 현재 산출물 (Input) | 최종 검토 대상 (Focus Area) | 다음 액션 아이템 (Next Action) | 목표 KPI |
| :--- | :--- | :--- | :--- | :--- |
| **Developer** | `openapi_mock_spec.yaml` | 폴백 로직 통합 및 에러 핸들링 코드 구현. | 🛠️ Mock API Service와 E2E 테스트 환경 연동 완료. (코드 커밋) | 네트워크 실패 시나리오에서 100% 정상 복구. |
| **Designer** | 애니메이션 원본 에셋 팩, UI 목업 | Deep Crimson Red $\to$ Soft Gold 전환의 타이밍 및 시각적 완성도 검증. | 🎨 최종 사용 환경(Mockup)에 맞춰 인터랙티브 프로토타입을 업데이트하고 QA 팀과 테스트 진행. | 사용자 이탈 방지 (Transition 매끄러움). |
| **Researcher** | 테스트 데이터 통합 가이드, 케이스 목록 | *없음* (본 작업에서 완벽히 활용됨) | 💡 Funnel 외부 콘텐츠 기획 단계로 복귀하여, MiniFunnel에 대한 'Hooks'를 강화할 신규 Pain Point 발굴. | Funnel 유입율 최적화. |
| **QA/PM** | *전체 문서* | 모든 QA 체크리스트 항목을 따라 실제 End-to-End 테스트 수행 및 버그 리포팅. | 📝 통합 테스트 보고서(Test Report) 작성 후, 발견된 버그 목록을 개발팀에 전달. | 시스템 안정성 확보 (Defect Zero). |

---
**📌 최종 점검 사항:**
*   MiniFunnel 진단 과정에서 얻은 **'경고 지표'와 '솔루션 가이드'가 항상 연결되어야 합니다.** 경고만 보여주고 해결책이 없으면 안 됩니다.
*   모든 단계별 데이터 전송(State)에 대한 로그 기록이 가능해야, 추후 A/B 테스트 및 서비스 개선의 근거로 활용됩니다.

</create_file>

📊 평가: 완료 — 모든 핵심 산출물과 지시사항을 종합하여 실행 가능한 최종 QA 문서를 작성했기 때문에 목표가 달성되었습니다.
📝 다음 단계: Developer에게 이 체크리스트를 기반으로 Mock API 연동 및 E2E 테스트 환경 구축 작업을 공식적으로 요청해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\mini_funnel_qa_checklist_handover.md
