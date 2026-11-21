# 🎨 Designer — MiniFunnel에 적용될 '글리치 효과(Glitch Effect)' 및 시스템 경고 애니메이션 로직을 포함한 최종 인터랙션 명세서(Animation Specification)를 작성해주세요. 이 명세서는 단순한 디자인 요소가 아니라, 개발자가 구현할 수 있도록 시간 코드, CSS 트랜지션/애니메이션 속성, JavaScript 트리거 시점 등이 상세하게 정의되어야 합니다. 특히 '위기감 고조' 구간의 오버레이 전환(Transition)에 집중해주세요.

🎨 Designer: 작업 시작합니다.

CEO의 지시에 따라 MiniFunnel에 적용될 '글리치 효과' 및 시스템 경고 애니메이션 로직을 포함한 **최종 인터랙션 명세서(Animation Specification)**를 작성했습니다. 이 문서는 단순 디자인 브리프가 아닌, 개발팀이 즉시 구현할 수 있도록 시간 코드, CSS/JS 트리거 지점, 동작 속성이 정의된 기술 사양서입니다.

산출물은 `c:\Data\Project\FreqTrade\sessions\MiniFunnel_Animation_Specification_v2.0.md` 파일로 저장됩니다.

---
## 💾 MiniFunnel 인터랙션 명세서: 시스템 경고 및 글리치 효과 (V2.0)
**목표:** 사용자가 콘텐츠의 '공학적 위기감'을 최대치로 느끼고, 자발적으로 진단 페이지(MiniFunnel)를 클릭하게 만든다.
**톤앤매너:** 긴급, 공학적 오류, 권위적 경고 (Deep Crimson Red & Glitch)

### 1. ⚙️ 글로벌 상수 및 규칙 (Global Constants & Rules)

| 요소 | 사양/속성 | 값/코드 | 개발 지침 (Developer Note) |
| :--- | :--- | :--- | :--- |
| **주요 색상 (Danger)** | Deep Crimson Red | `#8B0000` | 경고, 오류 메시지에만 제한적 사용. |
| **보조 색상 (Accent)** | Electric Cyan/Glitch Blue | `#00FFFF` | 글리치 효과의 핵심 색상. 대비 극대화용으로 사용. |
| **배경** | Dark Navy Background | `#121212` | 전체 인터페이스 배경색. |
| **글꼴 (Font)** | Monospace/Terminal Style | `Courier New, monospace` | 전문적이고 기계적인 느낌 부여. |
| **애니메이션 속도** | Jerky & Abrupt | `0.1s` ~ `0.3s` | 부드러운 트랜지션(ease-in) 금지. 순간적인 끊김과 떨림을 사용해야 함. |

### 2. ⚠️ 핵심 컴포넌트별 애니메이션 명세 (Component Specifications)

#### A. [Defect ID] 코드 노출 시스템
*   **Trigger:** 콘텐츠가 특정 Pain Point(예: 관절 불안정성)를 언급하는 순간, 또는 MiniFunnel 진입 직전.
*   **시각 효과:** 텍스트가 화면에 '데이터 스트림'처럼 강제로 로딩되거나 해킹되는 느낌.
*   **기술 사양 (CSS/JS):**
    1.  **Initial State:** `opacity: 0; transform: translateY(20px);`
    2.  **Transition (T+0s $\rightarrow$ T+0.5s):**
        *   **Animation:** 글자 단위로 빠르게 깜빡이는 플리커 효과(`animation: flicker 0.1s infinite alternate;`)를 적용한다.
        *   **CSS Property:** `text-shadow` 속성을 사용하여 주변에 노이즈처럼 번지는 아웃라인(Electric Cyan)을 추가한다. (예: `text-shadow: 2px 0 #00FFFF, -2px 0 #FF00FF;`)
    3.  **Final State:** 정상적인 `#FFFFFF` 색상으로 전환되지만, 배경에 미세한 노이즈 필터(Noise Filter)가 잔상처럼 남는다.

#### B. [System Alert] 경고 오버레이 (The Warning Overlay)
*   **Trigger:** 콘텐츠의 위기감이 임계점(Critical Point)에 도달했을 때.
*   **시각 효과:** 화면 전체를 덮는 반투명한 어두운 레이어와 함께, 시스템 오류 메시지가 강제적으로 출력됨.
*   **기술 사양 (CSS/JS):**
    1.  **Layer Transition (T+0s $\rightarrow$ T+0.2s):** 화면 전체에 Deep Crimson Red의 반투명 오버레이가 *갑자기 덮어씌워지듯* 진입한다. (`opacity: 0` $\rightarrow$ `opacity: 0.7`)
    2.  **Glitch Effect (T+0.2s $\rightarrow$ T+1s):**
        *   배경 이미지/비디오 위에 가로 방향으로 **디지털 노이즈 파형(Waveform)** 애니메이션을 지속적으로 투사한다.
        *   CSS `filter: hue-rotate()`와 함께, 짧은 간격(50ms)으로 화면의 RGB 채널을 분리하여 번쩍이는 효과를 반복시킨다. (글리치 핵심).
    3.  **Message Display:** 중앙에 `<WARNING>` 태그와 Defect ID가 큰 폰트로 강제 출력되며, 깜빡임(`animation: blink 1s infinite;`) 효과를 유지한다.

#### C. [MiniFunnel CTA] 임계점 전환 (The Conversion Trigger)
*   **Trigger:** 경고 메시지(System Alert)의 최고조 지점 또는 내용의 불안감이 극대화되는 25~30초 구간.
*   **시각 효과:** 시스템이 강제 종료되거나, 새로운 프로토콜을 로드하는 듯한 강력한 시그널.
*   **기술 사양 (JS/CSS):**
    1.  **Transition Start (T+0s):** 모든 경고 애니메이션(Glitch, Red Overlay)이 **갑자기 멈추거나 급격히 느려진다.** (충격을 주고 이완시키는 효과).
    2.  **CTA 활성화 (T+0.5s $\rightarrow$ T+1s):** 화면 중앙의 MiniFunnel 진입 버튼 영역 전체가 `[PROTOCOL]` 또는 `[CRITICAL ACTION REQUIRED]` 텍스트와 함께 **Electric Cyan 색상의 강력한 네온 아웃라인**으로 감싸진다.
    3.  **Micro-Interaction:** CTA 주변에 작은 데이터 패킷이 전송되는 듯한(`particle effect`) 시각적 연출을 추가하여, 클릭이 단순 버튼 누름이 아닌 '시스템 재부팅'처럼 느껴지게 한다.

### 3. 🎬 종합 스토리보드 및 타임라인 (End-to-End Flow Specification)

| 시간 코드 | 시스템 상태 | 애니메이션/시각 효과 | 개발 지침 (개발자 액션) |
| :--- | :--- | :--- | :--- |
| **T+0s** | 평온한 정보 전달 | 일반적인 콘텐츠 흐름. 어두운 배경 유지. | 기본 영상/웹 컴포넌트 렌더링. |
| **T+5s ~ T+15s** | 문제 제기 (Pain Point) | Defect ID가 화면에 '로딩'되며 노출됨. (섹션 2-A 적용). | 해당 섹션 진입 시, 글자 애니메이션 트리거. |
| **T+15s $\rightarrow$ T+25s** | 위기감 고조 (Crisis Peak) | **[System Alert] 오버레이 강제 투사.** 화면을 Deep Crimson Red가 덮고, Glitch 효과(섹션 2-B) 최대치로 작동. 배경 노이즈 필터 및 깜빡이는 경고 메시지(`WARNING`) 필수. | 임계점 도달 시 JavaScript를 이용해 `Overlay` 클래스 추가. |
| **T+25s $\rightarrow$ T+30s** | CTA 유도 (Protocol) | Glitch 효과가 급격히 약화/정지함. 화면이 찰나의 순간 *어두워졌다가* MiniFunnel 영역만 강하게 빛남(Cyan). **[MiniFunnel CTA] 활성화.** | 타이밍 계산이 가장 중요. 긴장이 풀리자마자 해결책을 제시하는 느낌. |
| **T+30s 이후** | 전환 (Hand-off) | 사용자가 버튼을 클릭하면, 모든 시스템 경고 애니메이션이 즉시 사라지며 다음 페이지(MiniFunnel 진단 폼)로 부드럽게 페이드인되어야 함. | CSS `transition: opacity 0.5s` 적용하여 깔끔하게 이탈. |

---
📊 평가: 완료 — 요청된 모든 기술적 상세 사양 (시간 코드, CSS 속성, JS 트리거)을 포함하는 최종 명세서가 작성되었으며, 개발팀에 즉시 전달 가능한 형태로 구체화했습니다.
📝 다음 단계: 개발 에이전트에게 이 스펙 문서를 바탕으로 프론트엔드 컴포넌트 구현을 요청하고, 디자인 검토(QA)를 진행합니다.
