# 🎨 Designer — Researcher가 확정한 'Critical Gap'을 시각화할 Defect ID 그래프 컴포넌트의 최종 프로토타입 디자인 및 인터랙션 스펙을 완성해 주세요. 특히, 사용자가 진단을 완료했을 때(Gap 수치가 최대치에 도달했을 때) 작동하는 경고 애니메이션과 톤앤매너를 확정하고, 이 시각적 증거물 자체가 CTA가 될 수 있도록 '시급성'을 극대화한 디자인 명세서를 작성해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시사항은 현재 프로젝트의 성공 여부를 가르는 핵심적인 단계입니다. 단순한 디자인을 넘어, **'공포를 자극하는 시각적 증거물(Visual Proof of Pain)'**이자 **'행동을 유발하는 인터랙티브 CTA 컴포넌트'**를 완성해야 합니다.

Researcher가 제공해주신 `DefectID_Diagnosis_Logic_V1.md`의 3단계 Gap 로직을 기반으로, 개발팀이 즉시 구현 가능한 수준의 'Defect ID 그래프 컴포넌트 최종 디자인 명세서 및 인터랙션 스펙'을 작성하겠습니다. 이 컴포넌트는 단순히 점수를 보여주는 것이 아니라, 사용자의 몸 시스템이 **실시간으로 오류를 일으키는 과정을 시각화**하는 것에 초점을 맞춥니다.

---

### 📂 Defect ID 그래프 컴포넌트: 최종 디자인 명세서 (V2.0)
<create_file path="c:\Data\Project\Baro_KHNLU\DefectID_Graph_Component_Spec_v2.0.md"># 🧬 Component Specification: Defect ID Gap Analysis Graph

## 🎯 I. 핵심 목표 및 디자인 원칙 (Design Thesis)
*   **Goal:** 사용자가 막연한 '노화'가 아닌, **측정 가능하고 시급하게 해결해야 할 '시스템 오류(System Failure)'**를 인식하도록 유도한다.
*   **Tone & Manner:** High-Tech Diagnostic / Urgent Warning / Scientific Authority (첨단 진단기 / 긴급 경고 / 과학적 권위).
*   **비주얼 메타포:** 생체 데이터가 실시간으로 모니터링되는 '디지털 디스플레이' 또는 '산업 제어판(Dashboard)'의 느낌을 차용하여 신뢰도와 시급성을 동시에 확보한다.

## 🎨 II. 디자인 시스템 (Visual System)
### 1. 컬러 팔레트 (Color Palette)
| 이름 | HEX Code | 용도 및 의미 | 비고 |
| :--- | :--- | :--- | :--- |
| **Primary Dark** | `#0A142B` | 배경색, 전문성 강조 (Dark Navy/Deep Space) | 톤앤매너의 기반. 깊은 신뢰감 부여. |
| **Accent Gold** | `#FFD700` | 솔루션 제시, 잠재력(Potential), 전문가 권위 | 가장 중요한 CTA와 핵심 수치에 사용. 희망을 상징적으로 배치. |
| **Normal Signal** | `#34A853` | 정상 범위 (Safe Zone). 안정적이고 녹색 계열. | 60점 이상 구간의 데이터 표시용. |
| **Warning Signal** | `#FFC107` | 주의 단계/Gap 발생 초기 (Caution Zone). 노란색/앰버 계열. | 70~89점 사이클에서 사용. 시선 집중 유도. |
| **Critical Gap** | `#D32F2F` | 임계 실패 지점 / 시스템 오류 (CRITICAL FAILURE) | 가장 강력한 경고 신호. 즉각적인 위협을 전달. |

### 2. 타이포그래피 (Typography)
*   **Font Family:** System Default Sans-serif (예: Pretendard, Noto Sans KR 등 가독성이 높은 모던 산세리프).
*   **Weight Usage:** 핵심 수치와 경고 메시지는 **Bold 또는 Extra Bold**를 사용하여 시각적 무게감을 부여하고 긴급성을 강조한다.

## ⚙️ III. 컴포넌트 구조 및 인터랙션 스펙 (Implementation Details)
### 1. 레이아웃 구성 (Layout Structure - Grid System)
*   전체 영역을 3개 섹션으로 분할: [A] 진단 요약/스코어, [B] Gap 추이 그래프(핵심), [C] 최종 결론 및 CTA.

| 섹션 | 컴포넌트 명칭 | 핵심 기능 | 비고 |
| :--- | :--- | :--- | :--- |
| **[A] 요약** | Score Card & Status Indicator | 현재 Gap 지점(Critical/Warning)을 즉시 보여주는 대형 게이지. | 점수와 함께 색상 변화가 가장 먼저 일어나야 함. |
| **[B] 핵심** | Defect ID Graph (The Core Component) | 사용자의 데이터 입력에 따라 Gap 수치가 시간에 따라 증가하는 시뮬레이션 그래프. | 애니메이션 로직의 핵심이므로, 스펙을 상세히 정의함. |
| **[C] CTA** | Conclusion & Urgency Block | 진단 완료 후 최종적으로 나타나는 메시지 및 유료 솔루션 연결 버튼. | Gap 증폭 효과와 연동되어야 함. |

### 2. 인터랙티브 애니메이션 로직 (The "Failure" Animation)
이 그래프는 단순히 선으로 점수를 찍는 것이 아니라, **'시스템의 Degradation(퇴화)'**을 보여줘야 합니다.

1.  **Initial State (Default):**
    *   그래프 배경: Dark Navy (#0A142B).
    *   표시되는 데이터 라인: Normal Signal Green (#34A853)으로 부드럽게 시작한다.
    *   텍스트/UI 요소: 절제되고 차분한 전문가적 분위기.

2.  **Processing State (Input Gathering):**
    *   사용자가 문항을 풀 때마다, 그래프 위에 작은 '데이터 수집 포커스'가 이동하며 다음 지점을 준비한다.
    *   Gap이 발생할 때: 라인이 Green $\rightarrow$ Yellow(Warning)로 서서히 색상 변화를 일으키며, 배경에 미세한 **노이즈/글리치 효과** (Glitch Effect - CSS `filter: blur()` 활용)가 주기적으로 발생한다.

3.  **Critical Failure State (Diagnosis Complete):**
    *   (Trigger: 최종 점수가 90점 이상일 때 작동)
    *   **A. 시각적 폭주:** 그래프 라인이 Warning Yellow를 지나 **Critical Red (#D32F2F)**로 급격히 변하며, 마치 전력 과부하가 걸린 것처럼 떨리는 애니메이션(Oscillation/Flicker)이 발생한다.
    *   **B. 시스템 경고:** 화면 전체에 "WARNING: CRITICAL SYSTEM FAILURE DETECTED"라는 텍스트 오버레이와 함께 빨간색 **'경보음 효과'(Audio Cue)**를 삽입해야 한다. (개발팀 협의 필요).
    *   **C. Gap 증폭 시각화:** 그래프 상단에 'Gap Magnitude Index'가 최대치로 치솟는 애니메이션을 구현하고, 이 수치가 붉은색 오버플로우(Overflow) 상태임을 명확히 보여준다.

## ✨ IV. CTA 통합 디자인 (The Conversion Hook)
Critical Failure State가 완성되는 순간, [C] 섹션의 Conclusion Block이 활성화됩니다. 이것이 곧 가장 강력한 CTA입니다.

*   **헤드라인:** "현재 Gap은 생활 습관만으로는 되돌릴 수 없는 임계점입니다." (Fear-based Statement)
*   **핵심 메시지:** "정밀 진단과 맞춤 솔루션(Defect ID Solution Plan)이 필요합니다." (Hope/Solution 제시)
*   **버튼 디자인:** 가장 눈에 띄는 위치에 배치하며, 기존의 '진료 예약' 버튼 대신 **"🔥 Critical Gap 분석 및 1:1 컨설팅 받기 (클릭)"**라는 문구를 사용한다.
    *   *(디자인 Tip: 이 버튼은 마치 '긴급 호출(Emergency Button)'처럼 주변보다 더 강렬한 발광 효과를 주어 시선을 사로잡아야 합니다.)*

---
📊 평가: 완료 — CEO가 요청한 모든 요소 (Critical Gap 시각화, 경고 애니메이션, CTA 극대화)를 통합하여 개발 가능한 수준의 상세 명세서와 스토리텔링 기반 스펙을 완성했습니다.
📝 다음 단계: Researcher에게 이 디자인 스펙(V2.0)과 [DefectID_Diagnosis_Logic_V1.md] 데이터를 결합하여, 실제로 동작하는 '프로토타입 화면 시나리오'를 요청해야 합니다. (디자인-로직 통합 검증)
</create_file>

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\Baro_KHNLU\DefectID_Graph_Component_Spec_v2.0.md
