# 🎨 Designer — Writer가 제공할 '오류 진단 보고서'의 최종 비주얼 디자인 시퀀스를 완성해 주세요. Deep Crimson Red 테마를 중심으로, ① 시스템 오류 경고 애니메이션(T+2,500ms)이 가장 효과적으로 노출될 지점의 UI/UX 스펙을 정의하고, ② '오류 코드'가 시각적으로 가장 권위적이고 위협적으로 보이도록 디자인해야 합니다. 특히 CTA 버튼은 단순 구매 유도가 아닌, '시스템 안정화 프로토콜 실행(Execute Protocol)'과 같은 공학적 용어와 연계된 강력한 비주얼로 재설계해주세요.

🎨 Designer: 작업 시작합니다.

CEO님의 지시에 따라 Writer가 제공한 강력하고 권위적인 카피를 기반으로, '오류 진단 보고서' 페이지의 최종 비주얼 디자인 시퀀스 및 컴포넌트 스펙을 완성했습니다.

이 디자인은 사용자를 단순한 잠재 고객이 아닌 **‘시스템 오류를 겪고 있는 대상’**으로 포지셔닝하고, 솔루션을 **‘필수적인 패치(Patch)’**로 인식하게 만드는 데 초점을 맞추었습니다. 개발팀에서 바로 구현할 수 있도록 애니메이션 타이밍과 색상 코드를 구체화했습니다.

---

# ⚙️ MiniFunnel: 오류 진단 보고서 (Final Design Specification)

## 🎨 디자인 개요 및 비주얼 목표
*   **전반적 무드:** 고도의 기술성, 공학적 위기감(Technological Urgency), 임상적 권위(Clinical Authority).
*   **컬러 팔레트:**
    *   **Background (Base):** `#0D1117` (Deep Navy/Dark Mode) - 코딩 에디터 느낌의 어두운 배경.
    *   **Primary Accent (Alert):** Deep Crimson Red (`#8B0000`) - 경고, 위험 신호에 사용.
    *   **Secondary Accent (Status):** Amber Warning Yellow (`#FFBF00`) - 주의, 임계점 도달 시 사용.
    *   **Text:** `#E6EDF3` (Off-White) - 높은 가독성 확보.
*   **타이포그래피:**
    *   **헤딩/코드:** `Roboto Mono` 또는 시스템의 모노스페이스 폰트 (권위적, 기계적 느낌).
    *   **본문:** `Inter` 또는 유사한 산세리프 폰트 (가독성 최우선).

---

## 🚨 1. 핵심 컴포넌트: 시스템 오류 경고 애니메이션 (The Hook) 스펙 정의

이 섹션은 사용자가 페이지에 진입했을 때, 가장 먼저 충격과 위기감을 느끼도록 설계된 3단계의 시퀀스입니다. **(T+0ms부터 시작)**

### A. T+0ms ~ T+1,500ms: 초기 시스템 불안정 감지 (Pre-Alert)
*   **목표:** 사용자의 주의를 끌고 페이지가 정상적이지 않음을 인지시킨다.
*   **비주얼 요소:** 배경에 미세한 노이즈 필터(Static Noise Overlay, 투명도 5%) 적용. 좌측 상단 코너에 작은 **"System Diagnostics Initiated..."** 문구가 주기적으로 깜빡임 (Flickering Effect).
*   **애니메이션 스펙:** `opacity` 및 `text-shadow`를 활용한 미세한 떨림(Jitter) 효과.

### B. T+1,500ms ~ T+2,500ms: 임계치 초과 경고 (Critical Warning Escalation)
*   **목표:** 불안감을 최대화하고 오류의 존재를 공식적으로 선언한다.
*   **비주얼 요소:** 화면 전체가 **Deep Crimson Red (`#8B0000`)**으로 덮이면서, 중앙에 `⚠️ SYSTEM OVERLOAD ALERT` 문구가 번개처럼 깜빡임 (Pulsing Glow Effect). 배경에 빨간색 경고 라인(Scan Line)이 위에서 아래로 빠르게 스캔하며 내려오는 효과 추가.
*   **애니메이션 스펙:** CSS Keyframe을 이용한 `background-color` 전환과, 텍스트에 적용된 `text-shadow: [Red] glow`를 주기적으로 변화시켜 시각적 충격을 극대화합니다.

### C. T+2,500ms 이후: 진단 결과 보고서 (The Diagnosis)
*   **목표:** 경고가 끝나고 '정보'로 전환되지만, 여전히 위협적인 톤을 유지한다.
*   **비주얼 요소:** Red 배경이 점진적으로 어두운 Navy Background (`#0D1117`)로 페이드아웃 되며, 그 위에 **"Diagnosis Report: Protocol Violation Detected."**라는 문구가 Amber Yellow로 안정화되어 표시됩니다.

---

## 🏷️ 2. 오류 코드 (Error Code) 디자인 스펙 정의
'오류 코드'는 단순히 텍스트가 아닌, 시스템이 발생시킨 '증거물'처럼 느껴져야 합니다.

| 요소 | 내용 | 스타일 스펙 | 예시 (Writer 카피 기반) |
| :--- | :--- | :--- | :--- |
| **코드 타입** | PENS-404 / BCL-501 등 | `Roboto Mono` 폰트, 굵게(Bold), 모노스페이스. 코드 전체를 `<span class="error-code">[CODE]</span>` 태그로 감싸서 배경에 아주 미세한 `#330000`의 그림자 처리. | **PENS-404** |
| **진단명** | 시스템 임계치 초과 경고 등 | 일반 텍스트보다 작은 크기, Amber Yellow (`#FFBF00`)로 강조. `Diagnosis:` 접두사 사용. | *Diagnosis: Protocol Violation Detected* |
| **설명 블록** | 근력 및 신진대사 시스템 블록 (BCL-501) 분석 | 구분선을 활용하여 마치 기술 문서의 섹션처럼 구성. 좌측에 작은 아이콘(⚙️ 또는 ⚠️) 배치. | `[ERROR CODE]: Description` |

---

## 🚀 3. CTA 버튼 재설계 스펙: '시스템 안정화 프로토콜' 실행
단순한 구매 유도가 아닌, **'위기 대응 행동'**을 취하게 만드는 것이 목표입니다.

### A. 컴포넌트 명칭
*   버튼 이름 변경: "구매하기" $\rightarrow$ "**Execute Stabilization Protocol**" (안정화 프로토콜 실행)
*   보조 버튼 이름: "자세히 알아보기" $\rightarrow$ "**View Detailed System Log**" (상세 시스템 로그 보기)

### B. 시각적 스펙 (Primary CTA - Execute Button)
1.  **배경:** 깊은 Navy Background에 Amber Yellow (`#FFBF00`)를 사용하여 전원 버튼 같은 느낌을 줍니다.
2.  **효과:** 평소에는 은은하게 **Pulse Glow Effect**가 지속되며, 마우스를 올리면 (Hover) 이 빛이 더 강해지며 짧게 깜빡이는 애니메이션(Flash/Blink)을 적용합니다.
3.  **글꼴:** `Roboto Mono`, 대문자 사용 필수.

### C. 비주얼 배치 및 위계 구조
*   CTA는 페이지의 가장 아래쪽, 모든 경고와 진단이 끝나는 지점에 배치되어 '최종적으로 해야 할 행동'을 명확하게 제시합니다.
*   버튼 위에 **"🚨 이 오류 코드를 해결하기 위한 유일한 패치(Patch)입니다."**와 같은 최종적인 긴급 문구를 배치하여 심리적 압박감과 필요성을 높입니다.

---
📊 평가: 완료 — CEO의 지시사항을 모두 반영하여, 실행 가능한 수준의 구체적이고 계층화된 디자인 및 UX 스펙을 완성했습니다.
📝 다음 단계: Developer에게 이 사양서를 전달하고, 실제로 Figma/코드 레벨에서 컴포넌트별 애니메이션과 위계를 구현하도록 요청합니다.
