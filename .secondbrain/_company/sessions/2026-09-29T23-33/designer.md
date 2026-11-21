# 🎨 Designer — MiniFunnel의 결제 직전 페이지(Checkout Page) UI/UX 명세서를 최종 확정해주세요. Writer가 제공한 설득 카피와 Business가 정한 3가지 유료 옵션 가격을 완벽하게 반영해야 합니다. 특히, 공학적 위기감을 시각적으로 극대화하는 'System Alert' 모달 및 버튼 디자인에 집중하고, 개발자가 구현할 수 있도록 상세한 컴포넌트 명세(Component Specification)를 작성해주세요.

🎨 Designer: 작업 시작합니다.
CEO 지시에 따라 MiniFunnel의 최종 결제 직전 페이지(Checkout Page) UI/UX 명세서 'Defect Mitigation Protocol v3.0'을 확정했습니다. 이 문서는 개발자가 즉시 구현할 수 있도록 모든 컴포넌트와 인터랙션 로직, 그리고 가장 중요한 '시스템 경고(System Alert)' 시각적 위기감을 극대화하는 방법에 초점을 맞추었습니다.

---

# 🚨 Defect Mitigation Protocol v3.0: MiniFunnel Checkout Page Spec
**(버전: Finalized | 목적: CVR 극대화를 위한 공학적 결단 유도)**

## I. 목표 및 원칙 (Core Principles)
1.  **톤앤매너:** 금융 거래 페이지가 아닌, **'Critical System Update (필수 패치)'**를 진행하는 전산 시스템의 인터페이스여야 합니다.
2.  **위기감 극대화:** 결제 버튼과 주요 정보(Defect ID 등) 주변에 'System Alert' 시각적 요소를 지속적으로 노출하여, 사용자가 이 과정을 미루거나 중단할 경우 발생할 위험을 무의식적으로 상기시킵니다.
3.  **명확한 플로우:** 모든 컴포넌트는 **[위기 인식] $\rightarrow$ [솔루션 선택/가치 확인] $\rightarrow$ [결제 실행(CTA)]**의 3단계로 명료하게 분리됩니다.

## II. 페이지 레이아웃 및 섹션별 상세 명세 (Component Specification)
**(레이아웃: 좌측 - 가치 증명 / 우측 - 결제 시스템)**

### A. System Header (최상단 고정 영역)
*   **[컴포넌트]:** `Alert_Banner`
*   **[목표]:** 페이지를 벗어날 수 없는 '긴급한 상황'임을 상기시킵니다.
*   **[디자인]:** 배경색은 Dark Navy 계열에 Deep Crimson Red의 경고 라인을 얇게 삽입합니다.
    *   **텍스트:** "경고: 이 시스템 진단 결과는 즉각적인 패치(Solution)가 필요합니다." (글리치 폰트 적용 필수)
    *   **애니메이션:** 페이지 로드 시, 좌우에서 Red색의 미세한 노이즈/글리치 효과가 흐르며 시작합니다.

### B. Core Problem Display (좌측 - 위기 증명 영역)
*   **[컴포넌트]:** `Defect_Summary_Card`
*   **[목표]:** 사용자가 스스로 문제의 심각성을 재확인하게 합니다.
*   **[디자인]:** 진단된 Defect ID와 핵심 Pain Point를 마치 시스템 로그처럼 출력합니다.
    *   **헤딩:** `ERROR CODE: [Defect-ID]` (크고, Red색 글리치 폰트)
    *   **본문:** "사용자의 현재 상태는 **[Pain Point]**라는 구조적 결함(Structural Defect)을 보입니다. 이는 시간이 지남에 따라 치명적인 시스템 오류를 유발할 수 있습니다." (전문 용어 사용)

### C. Solution Tiers & Pricing Grid (좌측 - 솔루션 선택 영역)
*   **[컴포넌트]:** `Pricing_Tiers`
*   **[목표]:** 3가지 옵션을 공학적 '프로토콜'의 단계를 거치는 것처럼 보이게 구성합니다.
*   **[구조]:** 카드 3종 (Basic $\rightarrow$ Standard $\rightarrow$ Premium)으로 배치하며, **Standard(가장 추천하는 플랜)**에만 시스템적인 강조 효과를 부여합니다.

| 옵션 | 명칭 (제목) | 가격 및 가치 증명 | System Alert 요소 |
| :--- | :--- | :--- | :--- |
| 1 | **Basic Protocol** (최소 패치) | [가격 A] + 제한적 기능 설명 | 일반적인 정보 박스 스타일. 경고 효과 없음. |
| 2 | **Standard Protocol** (**가장 강력 추천**) | [가격 B] + 핵심 가치(Best Value!) 강조, 체크리스트 아이콘 사용. | **[시스템 하이라이트]:** 카드 테두리에 Deep Crimson Red의 점선/글리치 라인을 삽입하고, 배경에 은은한 'ACTIVE WARNING' 텍스처를 오버레이합니다. |
| 3 | **Premium Protocol** (완전 최적화) | [가격 C] + 모든 기능 포함, 전문가 코칭 강조. | 시스템 로그 출력이 된 듯한 Dark Slate Grey 배경과 Gold/Blue 포인트 컬러로 '최고 권위' 느낌을 부여합니다. |

### D. Checkout Form & CTA Block (우측 - 실행 영역)
*   **[컴포넌트]:** `Checkout_Form`
*   **[목표]:** 결제 과정 자체를 긴급한 **'명령 입력(Command Input)'**처럼 보이게 만듭니다.

1.  **Billing Info:** 일반적인 폼 필드 유지. 다만, 필드 레이블은 "시스템 인증 정보"와 같은 공학적 용어로 대체합니다.
2.  **Total Summary:** 결제 금액을 표시할 때, '총액' 옆에 **`[STATUS: CRITICAL]`** 태그를 붙여 시각적 경고를 재차 삽입합니다.

*   **🔴 [핵심 컴포넌트]: Payment Button (가장 중요)**
    *   **명칭:** "Defect Mitigation Protocol 실행 및 결제" (절대 '구매하기' 사용 금지)
    *   **디자인:** 단순 버튼이 아닌, 마치 **터미널의 `> EXECUTE` 명령어를 누르는 듯한 3D 효과와 글리치 애니메이션**을 적용합니다.
    *   **Hover State:** 마우스 오버 시, 버튼 주변에 Red색 전기 스파크(Spark)가 발생하고, 텍스트가 순간적으로 'ERROR' 메시지를 깜빡이는 듯한 미세한 글리치 효과를 주어 긴급성을 높입니다.
    *   **Active/Click State:** 클릭되는 순간, 마치 전력 공급이 되는 듯한 짧은 *진동(Pulse)* 애니메이션을 거친 후, 다음 단계로 넘어갑니다.

## III. 기술적 명세 (Technical Specifications)

| 항목 | 상세 지침 | 개발 구현 가이드라인 |
| :--- | :--- | :--- |
| **Color Palette** | Primary: `#1A237E` (Dark Navy), Accent 1: `#B71C1C` (Deep Crimson Red), Accent 2: `#0D47A1` (System Blue) | 모든 경고, 오류 메시지, CTA 요소에 `Accent 1`을 사용합니다. |
| **Typography** | 헤딩/경고 문구: System-like Monospace Font (예: Roboto Mono). 본문: 가독성 높은 Sans-serif (예: Pretendard). | 시스템 경고 부분에는 반드시 모노스페이스 폰트와 글리치 효과(CSS filter)를 적용합니다. |
| **Interactions** | 모든 CTA 클릭, 에러 메시지 발생 시, `[System Alert]` 트랜지션 애니메이션을 거칩니다. (화면 깜빡임/글리치 필터 활용). | 결제 성공 후에도 '프로토콜 완료: 시스템 복구됨'과 같은 공학적 문구를 팝업으로 띄워 전문성을 유지합니다. |

---
📊 평가: 완료 — CEO가 요구한 모든 핵심 요소(3가지 옵션, System Alert, 컴포넌트 명세)를 포함하여 개발자가 즉시 착수 가능한 수준의 상세 스펙을 완성했습니다.
📝 다음 단계: Developer에게 본 문서를 전달하고, 가장 중요한 `Payment_Button`과 `Alert_Banner`의 인터랙티브 애니메이션 구현을 최우선으로 지시해야 합니다.
