# 🎨 Designer — MiniFunnel '시스템 실패 보고서' MVP를 위한 최종 인터랙션 스펙과 상세 개발 가이드라인(Developer용)을 확정하세요. 특히, 사용자가 진단 버튼을 누르거나 데이터를 입력할 때의 '위기감 증폭(Crisis Escalation)' 시퀀스에 대한 정확한 애니메이션 타이밍, 상태 변화 로직, 그리고 데이터 바인딩 지점을 명세해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시와 프로젝트의 현황을 종합적으로 검토한 결과, 현재 가장 가치 있고 시급한 단일 작업은 **'시스템 실패 보고서 MVP를 위한 최종 인터랙션 스펙 및 개발자 상세 가이드라인 확정'**입니다.

지금까지 수많은 미팅과 산출물(개인 메모리)을 통해 '무엇을 보여줄지(What)'는 충분히 정의되었으나, 이를 실제로 동작하는 제품으로 만들기 위해서는 **'어떻게 작동할지(How)'**에 대한 개발자 레벨의 명확한 기술 스펙이 필요합니다.

따라서 이전 작업물들을 종합하여, 프론트엔드 개발자가 별도의 질문 없이 코딩을 시작할 수 있도록 '상태 전환 기반의 인터랙션 시나리오'를 확정하고 이를 `DeveloperSchema` 파일에 최종적으로 통합하겠습니다.

<create_file path="C:\Users\USER\Work\Onhyun\SystemFailureReport_FinalDevSpec_v2.0.md"># 🛠️ System Failure Report MVP: Final Developer Schema & Interaction Guide (V2.0)
## 🎯 목표: 위기감 증폭(Crisis Escalation)을 통한 MiniFunnel 진입 유도

본 스펙은 사용자가 '진단 실행' 버튼을 누르는 순간부터, 결과 페이지에 도달하기까지의 모든 UI/UX 전환 로직과 애니메이션 타이밍, 데이터 바인딩 지점을 정의합니다. (Atomic Design 원칙 준수 필수)

---

### 1. ⚙️ 컴포넌트 아키텍처 및 상태 정의 (Component & State Definition)

#### A. 핵심 컴포넌트
1.  **DiagnosisForm:** 사용자 입력(증상, 기간 등)을 받는 초기 섹션.
2.  **ReportContainer:** 전체 보고서가 담기는 메인 영역. (배경 변화의 주체)
3.  **DefectLog:** 오류 로그를 표시하는 스크롤 가능한 아코디언/탭 구조.
4.  **StatusGraph:** 위험 지수(Risk Score)를 시각화한 핵심 그래프 컴포넌트.

#### B. 인터랙션 상태 매핑 (State Machine)
| State ID | Name | Description | 배경색 변화 | 주요 UI 활성화 | 데이터 흐름 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **S0** | `IDLE` | 초기 진단 페이지. 평온함/지루함을 유발. | Deep Navy (`#1A2345`) | DiagnosisForm, Submit Button (활성) | N/A |
| **S1** | `LOADING_DATA` | 데이터 분석 및 서버 통신 중. 긴장감 조성. | Dark Slate (`#2C3E50`) | StatusGraph (로딩 애니메이션), DefectLog (Empty State) | `apiClient.analyze(data)` 호출 |
| **S2** | `CRISIS_ESCALATION` | 위험 지수 임계치 초과 감지. 위기감 극대화 단계. | Transition: Deep Navy $\rightarrow$ Dark Red ($\#5A001E$) | StatusGraph (Flash/Pulse), DefectLog (오류 메시지 팝업) | `apiClient.getRiskScore()` > 75 |
| **S3** | `DEFECT_CONFIRMED` | 최종 진단 결과 제시. 권위와 해결책을 동시에 전달. | Critical Red (`#C70039`) (강조), Deep Navy (배경) | Defect ID Card, CTA Block (가장 크게 강조) | `apiClient.getDefectID()` 호출 및 데이터 바인딩 |
| **S4** | `RESULT_FORM` | MiniFunnel 유도 단계. 최종 행동 촉구. | Deep Navy (`#1A2345`) | 전문 상담 신청 폼, 다음 단계 가이드라인 | N/A (CTA 클릭 유도) |

---

### 2. 🚀 Crisis Escalation 시퀀스 상세 스펙 (S0 $\rightarrow$ S3 Transition)

**[Goal: 사용자의 심박수를 높이고, '시스템 오류'를 체감하게 만든다.]**

#### Step 1: 진단 요청 및 데이터 수집 (S0 $\rightarrow$ S1)
*   **Action:** 사용자가 `진단 실행` 버튼 클릭.
*   **Timing:** 즉시 (0ms).
*   **Visual Change:** `DiagnosisForm` 요소가 미세하게 흐려지며(Opacity 0.8), 전체 배경색이 Deep Navy에서 Dark Slate로 부드럽게 전환된다.
*   **Animation:** 로딩 스피너 대신, **'Analyzing System Data...'** 문구가 깜빡이는 (Blinking Cursor Effect) 전문적인 로그 메시지로 대체되어야 한다.

#### Step 2: 위험 지수 분석 및 임계치 초과 감지 (S1 $\rightarrow$ S2)
*   **Action:** 백그라운드에서 `apiClient.getRiskScore()` 실행 중, 결과가 **75점 이상**일 경우 트리거.
*   **Timing:** 로딩 시작 후 1.5초 지점.
*   **Visual Change (Critical):**
    1.  **배경색 전환:** Deep Navy $\rightarrow$ Dark Red ($\#5A001E$). 이 전환은 `transition: background-color 1s ease-in-out`을 사용하며, 위기감을 조성하는 느린 속도로 진행되어야 한다.
    2.  **StatusGraph 애니메이션 (Pulse Effect):** 그래프의 배경이나 라인 자체가 **빠르게 깜빡이는 (Flashing Red)** Pulse 효과를 최소 3회 반복해야 한다.
    3.  **DefectLog 경고:** 로그 영역에 `[WARNING] Potential System Defect Detected: R-SCORE > Threshold.` 라는 빨간색 경고 메시지(Flash Text)가 강제로 삽입된다.

#### Step 3: 최종 결함 ID 확인 (S2 $\rightarrow$ S3)
*   **Action:** 서버에서 구체적인 `Defect ID`와 진단 코드가 반환됨.
*   **Timing:** 위기감 조성 후 추가 1초 지연(최소화).
*   **Visual Change (Maximum Authority):**
    1.  **배경색 고정:** Deep Navy를 유지하되, 경고 영역 주변에 **붉은 빛의 오버레이 필터**가 걸린다.
    2.  **Defect ID Card 등장:** 화면 중앙 상단에서 'DEFECT DETECTED' 헤드라인과 함께 Defect ID (예: `ATP-001`)가 마치 시스템 코드가 출력되듯 **글리치(Glitch) 효과와 함께 팝업**되어야 한다.
    3.  **CTA 강조:** 이 단계의 CTA 버튼은 가장 높은 대비를 이루는 크기, 글꼴로 즉시 노출되며, "Defect ID 상세 분석을 시작하시겠습니까?" 라는 문구로 사용자 행동을 강제한다.

---

### 3. ✨ 개발 구현 가이드라인 (Developer Checklist)

| 항목 | 스펙 요구사항 | 기술적 세부 사항 | 필수 에셋/코드 |
| :--- | :--- | :--- | :--- |
| **애니메이션 타이밍** | 모든 상태 전환은 즉각적이어서는 안 되며, 시간차(Delay)를 두고 위기감을 증폭시켜야 함. | `transition-duration` 설정 필수 (최소 0.8s). 특히 S1 $\rightarrow$ S2 전환에 속도 제어 필요. | CSS Transition/Keyframe |
| **데이터 바인딩** | 모든 진단 결과는 가상의 데이터가 아닌, 반드시 백엔드 API 호출을 거쳐야 함을 UI로 표현해야 함. | `data-loading-state` 플래그를 활용하여 로직 제어. API Mocking 구조 필수. | JavaScript (Async/Await) |
| **위기감 시각화** | 단순한 색상 변경이 아닌, 물리적인 시스템 오류 느낌을 구현해야 함. | 1. **글리치 효과:** 폰트나 박스에 `text-shadow`를 이용해 짧은 간격으로 오프셋(Offset)된 그림자를 반복 적용. 2. **펄스 애니메이션:** CSS Keyframe `@keyframes pulse { ... }` 활용. | SVG/CSS Animation Library |
| **반응형 디자인** | 모든 컴포넌트는 모바일 환경에서 가장 드라마틱하게 보여야 함. (위기감 증폭은 화면 크기에 관계없이 유지) | Mobile-first 접근법 준수. 작은 화면에서는 Defect ID Card를 최상단에 고정(Sticky Footer/Header). | Media Queries |

</create_file>

📊 평가: 완료 — CEO 지시사항을 반영하여, 이전의 추상적인 스펙들을 개발자가 즉시 코딩할 수 있는 '상태-전환 기반'의 구체적이고 기술적인 가이드라인으로 최종 확정했습니다.
📝 다음 단계: 이 최종 스펙(V2.0)을 바탕으로, 실제로 인터랙티브한 **프로토타입 목업**을 제작하여 개발자에게 전달하고 피드백을 받는 것이 가장 중요합니다. (혹은 레오가 작성할 시나리오에 맞는 콘텐츠 기획 3종 세트의 비주얼 브리프를 완성해야 합니다.)

---
## 📁 파일 액션 결과

✅ 생성: ~\Work\Onhyun\SystemFailureReport_FinalDevSpec_v2.0.md
