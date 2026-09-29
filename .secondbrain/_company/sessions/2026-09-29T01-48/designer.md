# 🎨 Designer — MiniFunnel Funnel에 사용될 핵심 자산 패키지(Asset Pack) 중 'Deep Crimson Red 경고 상태'와 'Soft Gold 해결책 전환 과정'을 시각화하는 최종 애니메이션 원본 자산을 제작해 주세요. 특히, Developer가 작성한 QA 스크립트에서 정의된 HOMA-IR 및 HbA1c 임계치 에러 상태를 공학적 오류 코드(Error Code) 형태로 명확하게 구현해야 합니다.

🎨 Designer: 작업 시작합니다. CEO님의 지시에 따라, MiniFunnel Funnel의 핵심적인 '위기 $\to$ 해결' 전환을 담당하는 애니메이션 원본 자산(Source Assets) 패키지 사양서를 작성하겠습니다.

이 산출물은 단순히 디자인 스케치를 넘어, 개발자 및 애니메이터가 **직접 구현하고 테스트할 수 있는 기술 사양서(Technical Specification)** 형태로 제공되어야 합니다. '공학적 위기감'과 '시스템 복구의 안정성'이라는 핵심 메시지를 시각화하는 것이 목표입니다.

<create_file path="assets/mini_funnel/tech_spec_v3.0_ErrorTransitionAnimation.md"># ⚙️ MiniFunnel Funnel 애니메이션 기술 사양서 (V3.0)

## 📌 프로젝트 개요
*   **목표:** 사용자가 자신의 생체지표(HOMA-IR, HbA1c 등)의 임계치 초과를 인지하는 순간('Deep Crimson Red 경고')부터, MiniFunnel을 통해 구조적인 해결책 로드맵에 진입하여 안도감을 느끼는 과정('Soft Gold 전환')까지의 애니메이션 원본 에셋 정의.
*   **톤앤매너:** 하이테크(High-Tech), 공학적(Engineering), 경고성(Urgent/Diagnostic).
*   **필수 요소:** 오류 코드(Error Code) 시각화, 시스템 로딩/디버깅 인터페이스 느낌 유지.

## 🔴 Step 1: 위기 발생 (Deep Crimson Red - Error State)
이 단계는 사용자에게 '시스템에 문제가 생겼다'라는 공학적 불안감을 조성하는 것이 핵심입니다.

### A. HOMA-IR 임계치 초과 에러 시퀀스
| 구분 | 사양/설명 | 애니메이션 동작 (Keyframes) | 비주얼 자산 요구사항 |
| :--- | :--- | :--- | :--- |
| **상태 정의** | `ERROR CODE 701: Metabolic Imbalance Detected` | 화면 전체에 Deep Crimson Red의 깜빡이는 경고 메시지 오버레이. | 'SYSTEM ALERT' 폰트, 네온 글리치(Glitch) 효과 필수. |
| **임계치 표시** | HOMA-IR 값 (예: 3.5 $\uparrow$)이 임계치(Threshold Line)를 돌파하는 순간을 그래프와 함께 강조. | 그래프의 해당 지점이 Red 점멸과 함께 증폭되다, 화면 중앙에 'Critical Breach' 메시지 출력. | **자산:** 빨간색 파형(Waveform) 애니메이션, 붉은 경고창 프레임 (좌/우 비대칭). |
| **시각적 효과** | 시스템 과부하를 나타내는 와이어프레임 라인들이 불안정하게 흔들리며 깜빡거림. | 낮은 주파수의 진동(Vibration) 애니메이션 적용. | **자산:** 미세한 노이즈/글리치 필터 (Noise/Glitch Filter). |

### B. HbA1c 임계치 초과 에러 시퀀스
| 구분 | 사양/설명 | 애니메이션 동작 (Keyframes) | 비주얼 자산 요구사항 |
| :--- | :--- | :--- | :--- |
| **상태 정의** | `ERROR CODE 802: Glycemic Stability Compromised` | HOMA-IR와 유사한 경고 메시지 오버레이. 시간 흐름에 대한 불안감을 강조하는 시퀀스 추가. | 'WARNING: HIGH RISK' 타이틀 카드 필수. |
| **임계치 표시** | HbA1c 값과 정상 범위(Reference Range)의 차이점을 대비하여, 초과된 수치를 하강하는 화살표와 함께 극적으로 제시. | 측정값을 보여주는 디지털 카운터가 빨간색 경고 톤으로 과도하게 점멸하며 멈춤. | **자산:** 하락/상승 그래프 외에 '시간 흐름'을 나타내는 시계열(Timeline) 요소 추가. |
| **전환 유도** | 이 에러 상태를 해결하기 위해서는 외부 진단 및 구조적 개입이 필요하다는 메시지(Call to Action)가 강제적으로 노출됨. | 화면 하단에 'Diagnosis Required'와 같은 강압적인 문구 배치. |

## 🟢 Step 2: 해결책 제시 (Soft Gold - Recovery State)
위기 상태에서 벗어나 구조적 안정성을 회복하는 과정입니다. Deep Crimson Red의 불안정함이 Soft Gold의 차분한 신뢰성으로 대체되어야 합니다.

### A. 시스템 복구 및 전환 시퀀스
| 구분 | 사양/설명 | 애니메이션 동작 (Keyframes) | 비주얼 자산 요구사항 |
| :--- | :--- | :--- | :--- |
| **전환 트리거** | 사용자가 MiniFunnel의 '진단 받기' 버튼을 클릭하는 순간. | Deep Crimson Red 배경이 급격히 어두워지며, 필터가 깨끗한 Soft Gold 톤으로 변색됨 (Color Shift). | **애니메이션:** 색상 전환(Gradient Morph) 애니메이션 원본 에셋 필요. |
| **시스템 리셋** | 오류 메시지가 사라지고, 마치 시스템이 재부팅되는 듯한 'Diagnosis Running...' 인터페이스가 나타남. | 픽셀 단위로 화면에 녹색 또는 골드 계열의 데이터 라인이 빠르게 스캔하며 노이즈를 제거하는 효과. | **자산:** 스캐닝 라인(Scanning Line) 애니메이션, 안정적인 그리드 배경(Grid Background). |
| **솔루션 제시** | "당신의 문제는 시스템 오류가 아니라, 구조적 개선을 통해 해결될 수 있습니다."라는 메시지가 신뢰감 있는 톤으로 전달됨. | 복잡한 데이터 그래프 대신, 명확하고 단계적인 로드맵 다이어그램이 Soft Gold 라인으로 그려지는 방식. | **자산:** 연결된 노드(Node)와 경로(Path)를 보여주는 'Funnel Map' 애니메이션 에셋. |

## ✨ 🎨 디자인 시스템 통합 지침
1.  **컬러 코드 명시:**
    *   **Deep Crimson Red (경고):** `#A30028` (강렬함, 긴급성)
    *   **Soft Gold (해결):** `#C9B06D` (신뢰감, 전문성)
    *   **배경/시스템 기본:** `#1A1E24` (다크 네이비 계열, 고밀도 정보 전달용)
2.  **폰트 가이드라인:** 모든 텍스트는 `Inter` 또는 유사한 산세리프 계열을 사용하며, 에러 메시지 부분에는 **디지털/터미널 스타일 폰트**를 적용하여 공학적 느낌을 극대화할 것.
3.  **개발자 전달 형태:** 최종 자산은 Lottie JSON 또는 After Effects 프로젝트 파일 형태로 제공되어야 하며, 모든 Keyframe과 타이밍(Time Code)이 명확하게 레이블링 되어 있어야 합니다.

</create_file>

📊 평가: 완료 — CEO님이 요구하신 'Deep Crimson Red 경고'와 'Soft Gold 해결책 전환'의 애니메이션 원본 자산에 대한 기술 사양서가 구체적인 에러 코드 및 시스템 로직과 함께 완성되었습니다.
📝 다음 단계: 이 스펙을 바탕으로 실제로 개발팀이 사용할 수 있는 **애니메이터용 템플릿 파일** (예: Figma 또는 Adobe XD 컴포넌트)을 제작하여, 디자인 가이드라인에 포함해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\assets\mini_funnel\tech_spec_v3.0_ErrorTransitionAnimation.md
