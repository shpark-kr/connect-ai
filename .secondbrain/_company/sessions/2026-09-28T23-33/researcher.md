# 🔍 Researcher — 개발팀이 Mock API를 즉시 사용할 수 있도록, 구축된 60+개 시나리오 데이터셋의 구조적 메타데이터와 필터링 기준을 포함한 '테스트 데이터 통합 가이드' 문서를 작성하고, Developer에게 최종 검증용 테스트 케이스 목록(Test Case List)을 제공하라.

🔍 Researcher: 작업 시작합니다.

CEO 지시에 따라, 60개 이상의 시나리오 데이터셋을 개발팀이 즉시 통합하고 검증할 수 있도록 구조화된 '테스트 데이터 통합 가이드'와 '최종 검증 테스트 케이스 목록'을 작성했습니다. 이 문서는 단순히 데이터를 제공하는 것을 넘어, **데이터의 의도(Intent)**, **사용 조건(Constraint)**, 그리고 **기대되는 시스템 반응(Expected Behavior)**까지 정의하여 개발팀이 빠르고 정확하게 E2E 통합 테스트를 진행할 수 있도록 설계되었습니다.

먼저 두 개의 파일을 생성하겠습니다.

1.  **`test_data_integration_guide.md`**: 데이터셋의 구조적 메타데이터와 사용 원칙을 담은 가이드 문서입니다.
2.  **`final_validation_test_case_list.md`**: 핵심 시나리오별 입력 및 기대 결과가 명시된 테스트 케이스 목록입니다.

### 📂 생성 파일 목록

<create_file path="c:\Data\Project\connect-ai\researcher\test_data_integration_guide.md"># 🧪 MiniFunnel Mock API 통합 테스트 데이터 가이드 (V1.0)

**문서 목적:** 개발팀이 `openapi_mock_spec.yaml` 기반의 MiniFunnel 진단 로직을 검증하기 위해, 기존 60+개 시나리오 데이터셋(`test_dataset.csv`)을 어떻게 해석하고 어떤 조건에서 활용해야 하는지 구조화된 원칙과 메타데이터를 제공합니다.

## 1. 데이터셋 개요 및 핵심 전제
*   **원본 파일:** `c:\Data\Project\connect-ai\test_dataset.csv` (60개 이상의 시나리오 포함)
*   **핵심 목표:** 시스템이 '정상 진단(Soft Gold)'과 '위기 경고(Deep Crimson Red)' 상태 전이를 얼마나 정확하고 빠르게 처리하는지 검증합니다.
*   **데이터의 특성:** 이 데이터는 실제 환자 데이터가 아닌, **특정 가설적 시나리오와 그에 따른 예상 생체 지표 변화 패턴**을 담고 있습니다. 따라서 각 테스트 케이스를 실행할 때는 반드시 해당 시나리오의 맥락(Context)을 함께 고려해야 합니다.

## 2. 스키마 정의 및 필터링 기준 (Metadata Schema)
| Column Name | 데이터 타입 | 설명 | 필수 여부 | 필터링/사용 원칙 |
| :--- | :--- | :--- | :--- | :--- |
| `ScenarioID` | String | 시나리오 고유 식별자. | O | **[최우선]** 테스트 케이스를 실행할 때 반드시 지정해야 합니다. |
| `TargetGroup` | Enum (40-50, 50-60, 60+) | 주요 타겟 청중의 연령대. | O | 특정 Funnel 로직(예: 40대는 근력 위주, 60대는 관절/골밀도 위주) 테스트 시 사용합니다. |
| `InitialHOMA_IR` | Float | 초기 HOMA-IR 수치 (진단 시작점). | O | **[핵심]** 진단의 출발점을 설정합니다. Low/Normal/High 그룹으로 분류하여 테스트해야 합니다. |
| `DiagnosisStage` | Enum (Pre-Crisis, Crisis, Recovery) | 이 시나리오가 발생하는 주요 단계. | O | **Deep Crimson Red 경고를 검증하려면 반드시 `Crisis` 상태 데이터를 사용해야 합니다.** |
| `KeyBiomarker_X` | Float | 해당 시나리오의 핵심 생체지표 X 값 (예: HbA1c). | O | 값이 임계점(Threshold)을 넘는지 여부를 판단하는 근거 자료로 활용됩니다. |
| `ExpectedOutcome` | Enum (Improvement, Stable, Decline) | 진단 후 시스템이 예상하는 최종 변화 방향. | O | 테스트 케이스의 **최종 검증 목표**를 설정합니다. |

## 3. 통합 및 사용 원칙
1.  **Mock API 입력 포맷:** 모든 데이터는 `diagnosis/run_scan` 엔드포인트 POST 요청 바디에 JSON 형태로 주입되어야 합니다.
2.  **검증 순서:** **(A) 성공 시나리오 검증 $\to$ (B) 위기 상황 전이 검증 $\to$ (C) 실패 및 복구 로직 검증 순**으로 진행합니다.
3.  **데이터 추적:** 모든 테스트 실행 로그에는 `ScenarioID`, 사용된 API 호출 파라미터, 그리고 시스템 응답 코드를 필수로 기록해야 합니다.

</create_file>

<create_file path="c:\Data\Project\connect-ai\researcher\final_validation_test_case_list.md"># ⚙️ MiniFunnel E2E 최종 검증 테스트 케이스 목록 (Test Case List)

**목표:** Mock API 스펙(`openapi_mock_spec.yaml`)의 모든 경로(성공, 실패, 복구)를 커버하는 필수 시나리오 기반 테스트 케이스 리스트입니다. 개발팀은 이 목록을 따라 E2E 통합 테스트를 수행해야 합니다.

## 1. 핵심 성공 및 위기 경고 시나리오 (Success & Crisis Path)
| ID | Scenario Title | 목적 | 입력 데이터(`ScenarioID`) | 기대 결과 (`ExpectedOutcome`) | 검증 포인트 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Normal $\to$ Soft Gold (Baseline) | 기본 진단 흐름 및 안정적 개선 추이 확인. | `S_40_Normal_Start` | HOMA-IR 수치 점진적 감소 및 긍정적인 변화 애니메이션 발생. | Funnel 초기 로직 작동 여부, 'Soft Gold' UI 전환 정확도. |
| **TC-02** | Crisis Trigger (Deep Red) | 위기 상태 진입 시의 경고 로직 검증. | `S_50_Crisis_Peak` | 시스템이 명확하게 Deep Crimson Red Alert를 발생시키고, 사용자 행동 유도가 즉시 시작되어야 함. | **가장 중요.** 알람 타이밍 및 강도(Intensity) 체크. |
| **TC-03** | Recovery & Stabilization | 위기 이후 솔루션 적용을 통한 회복 추이 검증. | `S_60_Recovery_PostCrisis` | 경고 단계 $\to$ 안정화 단계로의 부드러운 시각적 전환 및 CTA 활성화 확인. | 상태 전이(State Transition) 로직의 무결성. |

## 2. 시스템 실패 및 복구 시나리오 (Failure & Resilience Path)
| ID | Scenario Title | 목적 | 입력 데이터(`ScenarioID`) | 기대 결과 (`ExpectedOutcome`) | 검증 포인트 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-04** | Network Failure (DNS Error) | 외부 네트워크 단절 상황 처리. | N/A (API Layer Mocking 필수) | 명확한 '네트워크 오류 발생' 메시지 표시 및 재시도(Retry) 버튼 활성화. 데이터 손실 없이 상태 유지. | `NameResolutionError`에 대한 UI/UX적 대응. |
| **TC-05** | Invalid Input Data (Schema Violation) | 필수 필드 누락 또는 타입 불일치 상황 처리. | `{...Missing Key}` | API 레벨에서 4xx 오류 코드 반환. 사용자에게 '데이터 형식이 잘못되었습니다'와 같은 구체적 피드백 제공. | 백엔드의 입력 유효성 검사(Validation) 로직 확인. |
| **TC-06** | High Load Timeout (Rate Limit) | API 요청이 과부하 상태일 때 처리. | N/A (API Layer Mocking 필수) | 명확한 '시스템 부하로 인해 잠시 이용할 수 없습니다' 메시지 표시 및 지연 시간(Delay) 후 재요청 유도. | 시스템의 안정성 고지점 확보 및 사용자 이탈 방지. |

## 3. 테스트 수행 가이드라인
1.  **테스트 환경:** Mock API Service (Python 기반 모킹 레이어)를 통해 진행해야 합니다. 실제 외부 네트워크 연결을 사용해서는 안 됩니다.
2.  **우선순위:** **TC-02 $\to$ TC-04 $\to$ TC-05 순서로 테스트 우선순위를 설정하고, 해당 실패 지점의 '복구' 메커니즘에 집중하여 검증합니다.**

</create_file>

---
📊 평가: 완료 — CEO가 요청한 구조적 가이드와 구체적인 테스트 목록을 개발팀이 바로 사용할 수 있는 형태로 두 개의 파일로 분리 완성했습니다.
📝 다음 단계: Developer에게 위 문서를 기반으로 E2E 통합 테스트를 요청하고, 그 결과(Test Log)를 받아 Critical Bug 리포팅 및 수정 사이클에 돌입해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\researcher\test_data_integration_guide.md
✅ 생성: c:\Data\Project\connect-ai\researcher\final_validation_test_case_list.md
