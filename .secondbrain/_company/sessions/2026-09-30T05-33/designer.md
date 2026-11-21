# 🎨 Designer — MiniFunnel V1.0의 '시스템 오류 보고서' 및 '진단 테스트 결과 페이지'에 필요한 최종 상호작용(Interaction) 스펙을 정리해주세요. 특히, Defect ID가 입력되었을 때, 사용자가 다음 단계로 넘어갈 때 발생하는 상태 변화(State Change)와 애니메이션 효과 등, 개발자가 코드로 구현할 수 있는 구체적인 명세가 필요합니다.

🎨 Designer: 작업 시작합니다.

요청하신 MiniFunnel V1.0의 핵심 상호작용(Interaction) 스펙은 단순한 디자인 가이드라인을 넘어, **개발자가 코드로 구현할 수 있는 상태 기계(State Machine)** 정의가 되어야 합니다. 이 스펙은 '공학적 위기감'과 '권위성'이라는 회사 정체성을 가장 직접적으로 체험하게 하는 핵심 로직이므로, 이전 단계에서 작성된 시각적 명세와 통합하여 최상위 레벨로 확정합니다.

아래는 개발팀(Front-end/UX Engineering)을 위한 **MiniFunnel V1.0 Interaction Spec (V2.0)**입니다. 이 스펙은 `MiniFunnel_SystemFailureReport_Spec_V1.0.md`를 상위 개념으로 확장하고, 실제 사용자 흐름에 따른 애니메이션 및 상태 변화(State Change) 로직을 추가합니다.

---

## ⚙️ MiniFunnel V1.0: 인터랙션 시스템 스펙 (Interaction Spec v2.0)
**목표:** 사용자가 '진단' 과정을 거치며 자신의 문제 인식을 극대화하고, '시스템 오류 해결'이라는 전문적인 프로세스를 통해 Premium 구독 모델로 자연스럽게 유도하는 경험을 설계한다.

### 1. 시스템 컬러 및 타이포그래피 규칙 재확인
*   **Deep Navy (Primary Background):** `#0A1931` - 기본 배경색, 신뢰성 확보.
*   **Crisis Red (Alert/Error):** `#C5222D` - 위험 경고, 시스템 오류 강조.
*   **Text Color:** `Light Gray` (`#E8EBF3`) - 가독성을 위한 주 텍스트 색상.
*   **Font Family:** Monospace 계열 (예: Fira Code, Source Code Pro) - 전문성과 코딩 환경 재현.

### 2. 핵심 로직 흐름 및 상태 변화 정의 (State Machine Flow)

| 단계 | 사용자 액션 | 시스템 상태 (State) | 목표 경험 (Emotion) | 애니메이션/트랜지션 효과 |
| :--- | :--- | :--- | :--- | :--- |
| **A. 진단 시작** | Defect ID 입력 및 '진단 실행' 버튼 클릭 | `STATE_PROCESSING` | 기대감, 긴장감 (What happens next?) | 1초간 로딩 화면/시스템 분석 애니메이션 |
| **B. 보고서 조회** | 시스템이 결과를 표시함 | `STATE_REPORTING` | 권위성, 문제 인지(Shock) | 텍스트가 한 줄씩 출력되는 '타자기 효과' (Typewriter Effect)로 점진적 정보 공개. |
| **C. 핵심 발견** | 주요 Defect ID 및 위험 요소 강조 영역 노출 | `STATE_CRITICAL` | 공포감, 위기감(Fear) | 배경에 미세한 깜빡임(Subtle Glitch/Flicker) 효과 적용. 경고 박스가 강렬하게 팝업됨. |
| **D. 해결책 제시** | '프로토콜 다운로드' 또는 CTA 버튼 클릭 (유료 전환 유도) | `STATE_ACTION` | 안심감, 전문성(Solution) | Transition: 보고서 모드 $\rightarrow$ Solution Guide 모드로 부드럽게 전환 (Deep Navy 유지). |
| **E. 오류 발생** | 필수 입력값 누락 또는 시스템 불가 상태 | `STATE_ERROR` | 재경고, 좌절감 | 전 화면에 Crisis Red 경고 오버레이. 공학적 에러 코드(`Error Code: X-YZZ`)와 함께 전문적인 설명 제시. |

### 3. 컴포넌트별 상세 스펙 (Dev Specs)

#### 🔴 3.1. [STATE_PROCESSING] - 로딩 및 데이터 분석 모듈
*   **구현 방식:** Full-screen overlay (Deep Navy 배경).
*   **애니메이션:** 시뮬레이션된 시스템 부팅/처리 과정 구현.
    *   `[0s - 0.5s]` Initial: "Initializing MiniFunnel System..." 메시지 출력.
    *   `[0.5s - 2.0s]` Processing: 중앙에 커서가 깜빡이는 형태의 **"Analyzing Bio-Data Streams... [::]"** 로딩 바를 구현하고, 좌우로 'Processing Data Stream...'과 같은 전문 용어가 스크롤 되게 만듭니다.
    *   `[2.0s - 2.5s]` Completion: "Analysis Complete. Retrieving System Report..." 메시지 출력 후, 다음 페이지(보고서)가 **Fade-In** 됩니다.

#### 🚨 3.2. [STATE_REPORTING] - 시스템 오류 보고서 (System Failure Report)
*   **구현 방식:** 모노스페이스 기반의 로그/콘솔 UI.
*   **애니메이션:** 모든 핵심 정보(Defect ID, 원인 분석 등)는 **타자기 효과(Typewriter Effect)**로 텍스트가 스트리밍 되듯이 나타나야 합니다. (갑작스러운 노출 금지).
*   **구조적 명세:**
    1.  **Header Module:** `[SYSTEM REPORT v2.0]` 및 현재 시간/날짜를 크고 전문적인 폰트로 배치합니다.
    2.  **Defect ID Display:** 최초 발견된 Defect ID는 가장 크게, Crisis Red로 강조하며 **`CRITICAL ALERT: [XXXX-YYYY]`** 형태로 출력됩니다. (이 부분이 시각적 충격의 중심).
    3.  **Analysis Log Module:** 본문 내용은 마치 로그 파일처럼 `[Timestamp] [LEVEL] [Component]: Message` 형식으로 구성하고, Depth에 따라 글자 크기와 배경색을 변화시켜 위계적으로 보이게 합니다.

#### ⚠️ 3.3. [STATE_CRITICAL] - 전환 유도 지점 (The Conversion Trigger)
*   **배치:** 보고서 본문 내용 중 가장 심각한 결론(예: "현재 상태 유지 시, X년 내 Y% 확률로 시스템 오류 발생")을 제시한 직후에 배치합니다.
*   **디자인 스펙:** 메인 콘텐츠를 가리는 오버레이 형태로 구현하며, 배경은 Deep Navy와 Crisis Red가 지배적이어야 합니다.
*   **텍스트 예시 (Tone):**
    > 🚨 **[SYSTEM CRITICAL FAILURE IMMINENT]**
    > 현재의 데이터 흐름(Status Quo)은 지속 불가능한 임계점에 도달했습니다. 추가적인 시스템 실패를 방지하려면, 전문 프로토콜 번들(`Protocol Bundle`) 적용이 *필수*합니다.
*   **상호작용:** 이 경고 박스는 단순 정보 제공을 넘어 **'사용자가 해결해야 할 미해결 과제(Unresolved Task)'**처럼 느껴지도록 디자인되어야 합니다.

#### 💰 3.4. [STATE_ACTION] - CTA 버튼 및 상호작용
*   **버튼 스펙:** 일반적인 Primary Button이 아닌, **`[EXECUTE PROTOCOL X]`** 와 같은 명령 프롬프트 스타일로 디자인합니다. (예: `> EXECUTE PROTOCOL BUNDLE? [Y/N]`)
*   **Hover State:** 버튼에 마우스를 올리면 Crisis Red의 플래시 효과와 함께 '접속 중...' 메시지가 잠시 나타나야 합니다.
*   **Click State:** 클릭 시, 즉각적인 페이지 이동이 아닌 `[Initiating Payment Handshake...]` 와 같은 **새로운 로딩 모듈(Mini-Loading)**을 띄우고, 결제 시스템의 전문성을 강조합니다.

### 4. 개발팀 체크리스트 (Developer Checklist)
*   **✅ State Management:** 모든 페이지 전환은 명시된 상태 기계에 따라 진행되며, 중간 단계가 생략되어서는 안 됩니다.
*   **✅ Animation Consistency:** '타자기 효과'와 '시스템 로딩 애니메이션'의 속도(Speed Curve)를 전체 콘텐츠에 통일하여 적용합니다. (너무 빠르거나 느리지 않게).
*   **✅ Responsiveness:** 모든 컴포넌트는 모바일 환경에서도 Deep Navy/Crisis Red 테마가 유지되도록 반응형으로 설계되어야 합니다.

---
📊 평가: 완료 — 개발자가 즉시 코드로 구현할 수 있도록 상태 변화, 애니메이션, 상호작용을 구체적인 명세로 정의했습니다.
📝 다음 단계: Business와 협의하여 이 '상태 기계'를 기반으로 한 **실제 와이어프레임/프로토타입**을 제작하고, A/B 테스트에 사용할 CTA 문구 및 플로우를 확정해야 합니다.
