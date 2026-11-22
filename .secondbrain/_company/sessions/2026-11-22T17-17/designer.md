# 🎨 Designer — Developer의 테스트에 필요한 최종 디자인 명세서를 제공하십시오. 특히, 재정적 리스크 보고서 내 그래프 및 애니메이션 요소들이 기술적으로 구현 가능한 '변수 기반(Variable-based)' 컴포넌트 스펙으로 최종 확정되어야 합니다. 모든 에셋과 인터랙션은 React State 로직이 읽어들일 수 있도록 CSS 변수와 명확하게 연결된 형태로 정리하여 전달하세요.

🎨 Designer: 작업 시작합니다.

CEO 지시사항에 따라, 개발팀이 즉각적으로 통합 및 테스트할 수 있도록 '재정적 리스크 보고서'의 디자인 명세를 **변수 기반(Variable-based) 컴포넌트 스펙**으로 최종 확정하여 전달하겠습니다. 이 문서는 React State 로직과 직접 연동되는 CSS 변수를 중심으로 작성되었으며, 개발자에게 전달하는 모든 에셋 및 인터랙션은 이 가이드라인을 따릅니다.

<create_file path="c:\Data\Project\Baro_KHNLU\assets\Final_Dev_Handover_Design_System.md"># 🚀 최종 디자인 시스템 핸드오버 명세서 (V1.0)
**대상:** 개발팀 (React/CSS Variable 기반 통합 테스트용)
**주제:** 재정적 리스크 보고서, Critical Alert UI 컴포넌트

## 🎯 1. 핵심 변수 정의 (CSS Variables Definition)

모든 디자인 요소는 다음의 CSS 변수를 참조합니다. State 로직은 이 변수들을 업데이트하는 것이 핵심입니다.

| 변수명 | 용도 | 기본값(Default) | 상태별 오버라이드 예시 |
| :--- | :--- | :--- | :--- |
| `--color-primary` | 주 강조색 (CTA, 그래프 주요 선) | `#0B3D4C` (딥 네이비) | N/A |
| `--color-secondary` | 보조 요소 (배경, 텍스트 구분선) | `#E5EFEF` (라이트 그레이) | N/A |
| `--color-text` | 기본 본문 텍스트 | `#333333` | N/A |
| `--color-danger` | 위험 경고색 (Critical Alert) | `#D93025` (강한 빨간색) | `State.RiskLevel == 'High'` 시 필수 적용 |
| `--color-warning` | 주의 경고색 (Attention) | `#FFC107` (골드/옐로우) | `State.RiskLevel == 'Medium'` 시 적용 |
| `--color-success` | 안정/긍정 요소 | `#28A745` (녹색) | N/A |
| `--bg-card` | 데이터 카드 배경색 | `rgba(10, 20, 30, 0.6)` (글래스모피즘 기반 어두운 반투명) | N/A |

## 📐 2. 타이포그래피 변수 및 계층 구조 (Typography Variables)

폰트는 'Noto Sans KR'을 메인으로 사용하며, 크기(Size)와 두께(Weight)를 변수로 정의합니다.

| 요소 | CSS 변수 | 기본값 (px) | State 의존성 |
| :--- | :--- | :--- | :--- |
| H1 (섹션 제목) | `--text-h1` | `2rem` | N/A |
| H2 (보고서 소제목) | `--text-h2` | `1.5rem` | 위험도에 따라 굵기(`--font-weight`)가 `700`에서 `900`으로 강제 변경됨. |
| Body Text (본문) | `--text-body` | `1rem` | N/A |
| Caption / Label | `--text-caption` | `0.85rem` | 위험도에 따라 색상(`--color-danger`)이 적용될 수 있음. |

## 📊 3. 컴포넌트별 변수 기반 스펙 (Variable Component Specs)

### A. Critical Alert UI (위험 경고 컴포넌트)
*   **목표:** 리스크 레벨(Low/Medium/High)에 따라 색상, 애니메이션 강도, 레이아웃이 즉각적으로 변화해야 함.
*   **입력 State:** `State.RiskLevel` (`'Low'`, `'Medium'`, `'High'`), `State.Message` (경고 메시지 텍스트).
*   **변수 적용 로직:**
    1.  **배경색 설정:** `background-color: var(--color-danger)`를 사용하며, `RiskLevel='High'`일 때만 **글래스모피즘 배경 투명도를 최소화**하여 강한 존재감을 줍니다.
    2.  **애니메이션 (깜빡임):** 리스크 레벨이 'High'인 경우, 경고창 전체에 1초 주기(Frequency: 0.5Hz)로 `--opacity` 변수를 `0.9`에서 `1.0`으로 변화시키는 **Pulse Effect**를 적용합니다.
    3.  **텍스트 강조:** 위험 메시지(`State.Message`)는 반드시 H2 변수와 `--color-danger`를 사용하여 표시하고, 이 텍스트에만 **굵게(Font Weight: 900)** 처리해야 합니다.

### B. 데이터 그래프 (Line/Bar Chart)
*   **목표:** 수치 변화의 '위험' 또는 '기회'를 시각적으로 과장하여 전달합니다.
*   **변수 적용 로직:**
    1.  **색상 변환:** 비교되는 지표(A vs B)에서, A가 B보다 **절대적인 차이가 20% 이상 클 경우**, 해당 선/바의 색상은 `--color-danger`를 사용합니다. (차이 자체가 위협임을 의미).
    2.  **애니메이션 (진행):** 그래프 데이터 로드 시, 단순히 채워지는 것이 아니라, Y축 값이 증가함에 따라 바가 **밑에서부터 팝업(Pop-up)** 되는 듯한 애니메이션을 적용합니다. 이는 `transform: translateY()`와 결합된 CSS Transition으로 구현되어야 합니다.
    3.  **툴팁 (Hover):** 마우스 오버 시, 단순 수치 표시를 넘어, 해당 데이터 포인트가 전체 평균 대비 **몇 %의 편차**를 보이는지(예: "+15% High Risk")를 `--text-caption` 변수로 강조하여 보여줍니다.

### C. Callout Box (핵심 요약 박스)
*   **목표:** 가장 중요한 '결론'을 제시하며, 시선이 자연스럽게 집중되도록 유도합니다.
*   **변수 적용 로직:**
    1.  **경계 강조:** 이 박스는 모든 섹션에서 **최소 4px 두께의 `--color-primary` 테두리**를 가져야 합니다.
    2.  **내부 시각화:** 내부에는 반드시 `State.KeyTakeaway`라는 변수에 담긴 핵심 문구와, 이를 보조하는 작은 아이콘 세트가 포함되어야 하며, 이 구조는 모든 섹션에서 재사용 가능한 컴포넌트로 정의됩니다.

---
📊 평가: 완료 — CEO의 지시사항을 모두 반영하여 기술적으로 구현 가능한 '변수 기반' 최종 디자인 시스템 명세서를 작성했습니다.
📝 다음 단계: 개발팀에게 본 문서를 전달하고, 실제 `e2e_deployment_simulator.py` 테스트 환경에서 이 변수 로직들이 정상 작동하는지 검증합니다.
