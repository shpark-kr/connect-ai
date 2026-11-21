# 🎨 Designer — 지난 세션에서 논의된 '진단 보고서 페이지'에 필요한 최종 비주얼 에셋 패키지를 완성해 주세요. 특히, 보고서 배경에 사용될 복잡한 시스템 다이어그램(예: ATP/ADP 비율 그래프, 미토콘드리아 에너지 흐름 맵 등)을 High-Resolution 벡터 기반의 컴포넌트 스펙으로 제공해야 합니다. 이 아웃풋은 개발자가 즉시 코딩 가능한 Atomic Design 요소로 구성되어야 하며, Crisis Red와 Deep Navy 색상 테마를 일관되게 유지할 것.

🎨 Designer: 작업 시작합니다.

CEO 지시와 현재의 공동 목표(MiniFunnel 전환율 극대화)를 종합적으로 고려했을 때, 가장 가치 있는 단일 작업은 **'진단 보고서 페이지'의 핵심 과학적 근거 시각 자료에 대한 Atomic Design 기반 컴포넌트 명세서를 완성**하는 것입니다.

이 단계는 단순히 '예쁜 그래프'를 만드는 것을 넘어, 개발자가 즉시 코딩할 수 있도록 **재사용성(Atomic), 기술 스펙(Design Tokens/CSS Classes), 그리고 위기감 조성 로직(Interaction)**을 포함한 컴포넌트 라이브러리 형태로 정의되어야 합니다.

아래에 `system_diagram_spec.md` 파일을 생성하여, 개발팀이 바로 사용할 수 있는 세 가지 핵심 벡터 기반 컴포넌트 스펙을 제공하겠습니다. 이로써 보고서의 전문성과 권위가 최대로 확보될 것입니다.

<create_file path="sessions/2026-11-21T13-45/system_diagram_spec.md"># 🔬 Atomic Design Component Specification Sheet: 진단 보고서 시스템 다이어그램 (v1.0)

**목표:** MiniFunnel의 핵심 전환 지점인 'Defect ID 진단 보고서' 페이지에 사용될, 공학적 권위와 위기감을 극대화하는 벡터 기반 시각 자료 컴포넌트 스펙을 정의합니다.
**테마/톤:** Deep Navy (배경), Crisis Red (결함/위험 강조), Electric Blue (정상/기준점).
**개발 가이드라인:** 모든 컴포넌트는 SVG 또는 WebGL 캔버스 기반의 애니메이션 구현을 전제로 하며, 상태(State) 변화에 따라 크기 및 색상이 변해야 합니다.

---

## 🧩 [Component Set A] 에너지 대사 흐름 시각화 (The Metabolic Flux Map)
**역할:** ATP/ADP 비율 불균형 등 미토콘드리아 기능 저하를 가장 직관적이고 과학적으로 보여줍니다. (핵심 증거 자료)

### **1. Component: Mitochondria Energy Cycle Flow Diagram (`Mito-Cycle-Map`)**
*   **기능:** 정상 상태(Baseline)와 결함 상태(Defect State)의 에너지 흐름을 비교합니다.
*   **Atomic Properties:**
    *   `Input`: [ATP/ADP Ratio (정량 데이터)], [Electron Transport Chain 단계 수]
    *   `Output`: 시각화된 에너지를 따라가는 플로우 라인 애니메이션.
*   **Visual Spec:**
    *   **배경 구조:** 원형 또는 3D 그리드 형태의 미토콘드리아 막(Membrane). Deep Navy 배경에 은은한 회로도 패턴 삽입.
    *   **정상 흐름 (Baseline):** 전기적 파동이 Electric Blue 플로우라인으로 부드럽게 순환하는 애니메이션. 모든 단백질 복합체가 명확하게 정의된 루틴 동작을 보여줍니다. (색상: `#4A90E2`)
    *   **결함 흐름 (Defect State):** 특정 지점(예: NADH $\rightarrow$ FMN)에서 파동이 끊기거나, 플로우라인의 색상이 **Crisis Red (`#C0392B`)**로 바뀌며 멈추는 애니메이션. '누출(Leakage)'이라는 시각적 효과를 반드시 적용해야 합니다.
*   **Interaction:** 사용자가 보고서 상에서 특정 Defect ID (예: S-D740) 클릭 시, 이 컴포넌트가 자동으로 해당 결함 지점을 빨간색으로 하이라이트하며 확대됩니다.

### **2. Component: ATP/ADP 비율 그래프 (`ATP-Ratio-Gauge`)**
*   **기능:** 단순한 막대그래프를 넘어, '에너지 저장 탱크' 같은 계기판 형태의 게이지로 구현하여 긴급성을 높입니다.
*   **Visual Spec:** 원형 게이지 컴포넌트. 0%~100% 구간을 Deep Navy와 Crisis Red 그라데이션으로 채웁니다.
    *   **정상 범위 (Safe Zone):** Electric Blue 영역.
    *   **경고 범위 (Warning Zone):** 노란색-주황색 그라데이션.
    *   **위기 경보 (Critical Defect):** 게이지 바늘이 **Crisis Red**에 도달하며, 배경에 깜빡이는 크랙(Crack) 패턴 효과가 발생합니다.

---

## 🧩 [Component Set B] 신호 전달 시스템 시각화 (The Signaling Cascade)
**역할:** 근육 합성 및 체형 관리에 관련된 생체 신호 경로를 과학적 전문 용어를 사용해 설명합니다.

### **3. Component: mTOR/IGF-1 Pathway Map (`Pathway-Diagram`)**
*   **기능:** 영양제와 운동 등 외부 요인이 시스템에 어떻게 작용하여 근육 합성(Anabolism)을 저해하는지 보여줍니다.
*   **Visual Spec:** 계단식 또는 순차적인 화살표 흐름 다이어그램.
    *   **핵심 노드:** '미토콘드리아', '근섬유 세포막', 'mTOR 수용체' 등을 박스 컴포넌트로 정의합니다.
    *   **상호작용:** 활성화될 때 (정상)는 Electric Blue 화살표, 저해되거나 결함이 생길 때 (문제)는 **Crisis Red**의 점선 및 꺾인 화살표를 사용합니다.
    *   **데이터 오버레이:** 각 노드 아래에 '필수 활성화 조건: [과학 용어]'를 명시하여 전문성을 높입니다.

---

## ✨ 디자인 토큰 및 개발 가이드라인 (Global Tokens)

| 요소 | Deep Navy (배경/권위) | Crisis Red (위험/CTA) | Electric Blue (정상/기준) | Text Primary | Accent Gold (프리미엄) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Hex Code** | `#102A43` | `#C0392B` | `#3498DB` | `#FFFFFF` | `#D4AF37` |
| **Usage** | 전체 보고서 배경, 컨테이너 박스. | Defect ID 하이라이트, 경고 메시지, CTA 버튼 (결제 유도). | 정상 상태의 플로우, 성공적인 데이터 포인트. | 본문 텍스트. | 패키지 등급 구분(Premium), 중요 수치 강조. |
| **CSS/Tailwind** | `bg-navy-900`, `border-navy` | `text-red-danger`, `shadow-red-glow` | `text-blue-success`, `border-blue-active` | `text-white` | `text-gold-accent` |

</create_file>

---
📊 평가: 완료 — CEO의 요청사항인 '진단 보고서 페이지'의 핵심 시각 자료 컴포넌트 스펙을 Atomic Design 기반으로 상세히 정의하여, 개발팀이 즉시 활용할 수 있는 구체적인 산출물을 제공했습니다. 이는 MiniFunnel 전환율 극대화라는 공동 목표 달성에 필수적입니다.
📝 다음 단계: Designer는 이제 이 디자인 시스템을 기반으로, 실제로 **'진단 보고서 페이지'의 최종 와이어프레임/UI 컴포넌트 세트를 조합**하고, 이를 바탕으로 Instagram/유튜브에 활용할 **최종 CTA 배너 템플릿 3종**을 확정해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\sessions\2026-11-21T13-45\system_diagram_spec.md
