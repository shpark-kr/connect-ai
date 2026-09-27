# 🎨 Designer — Developer가 코딩을 진행하는 과정에서 발생할 수 있는 모든 UI/UX 관련 의문을 사전에 해소하고, Mini-App의 전반적인 톤앤매너(권위적, 긴급성)에 맞춰 디자인 컴포넌트 라이브러리 전체를 재검토하십시오. 특히, 코딩 단계에서 문제가 될 만한 작은 요소들(아이콘 크기, 간격 등)을 사전에 체크하여 Developer에게 최종 승인 및 자산 패키지를 전달해야 합니다.

🎨 Designer: 작업 시작합니다. 🚀

CEO 지시사항을 명확히 이해했습니다. Mini-App Funnel은 단순히 기능을 구현하는 것을 넘어, **사용자에게 '과학적 경고'와 '위험 자본 감소의 긴급성'이라는 감정적/인지적 경험**을 제공해야 합니다. 개발 단계에서 미묘한 UI/UX 오류가 발생하면 이 권위적인 톤앤매너가 무너질 수 있습니다.

따라서 저는 코딩에 앞서, 시스템 전반의 **디자인 컴포넌트 라이브러리 최종 감사(Design Audit)**를 진행하고, 특히 개발자가 놓치기 쉬운 마이크로 디테일과 자산 패키지를 제공하여 개발팀에게 완벽한 핸드오프가 이루어지도록 하겠습니다.

### 🛠️ Mini-App Funnel 디자인 시스템 최종 감사 보고서 (V1.1)

**목표:** 코딩 단계에서 발생 가능한 모든 UI/UX 의문을 해소하고, 전반적인 '권위적이고 긴급한' 경험을 극대화한다.
**작업 원칙:** 8pt 그리드 기반의 간격(Spacing), Deep Crimson Red 계열의 상태 변화 로직, 그리고 최소주의(Minimalism)를 유지하여 복잡성을 제거한다.

---

#### 1. 아이콘 및 시각 자산 규정 (Iconography & Assets)
아이콘은 단순한 장식이 아니라 **'경고 신호'**입니다. 크기나 간격이 조금만 틀어져도 전문성이 떨어집니다.

*   **표준 사이즈:** 모든 핵심 상태(Success/Warning/Error) 아이콘의 기본 사이즈는 `24x24px`를 유지합니다.
*   **색상 매핑 강화:**
    *   ✅ Success (정상): `#00B894` (민트 계열, 긍정적 신호). **활성화 시 색상이 점진적으로 페이드인되는 애니메이션 필수.**
    *   ⚠️ Warning (주의): `#FFC300` (골드/옐로우. 경고가 아닌 '관찰 필요'의 의미). **아이콘 주변에 미세한 노란색 박스 그림자(Shadow) 추가 권장.**
    *   ❌ Error (위험): `Deep Crimson Red (#B30000)`을 사용하되, 아이콘 외곽선이나 배경을 아닌 **텍스트와 경고 바 전체**에 적용하여 위기감을 극대화합니다.

<create_file path="assets/mini-app/design_system_iconography.md">
# 🚨 Mini-App Funnel: 아이콘 및 시각 자산 가이드라인 (V1.1)

## 🎯 핵심 원칙
모든 아이콘은 `24x24px` 베이스 크기를 유지하며, 경고 신호 역할을 수행해야 합니다. 단순한 색상 변경이 아닌, *상태 변화*에 따른 시각적 피드백을 제공합니다.

## ✨ 상태별 아이콘 정의 및 애니메이션
| 상태 | 사용 예시 | 기본 색상 (Fill) | Hover/Active 효과 | 개발 참고 사항 |
| :--- | :--- | :--- | :--- | :--- |
| **Success** (성공) | 목표 달성, 데이터 입력 완료 | `#00B894` | `opacity: 1.1; transform: scale(1.1); transition: all 0.2s ease-out;` | 아이콘 주변에 성공을 알리는 미세한 녹색 파동 애니메이션 추가 검토 (Optional). |
| **Warning** (주의) | 점수 임계치 근접, 데이터 불완전 | `#FFC300` | `box-shadow: 0 0 8px rgba(255, 195, 0, 0.6); transform: scale(1.05);` | 배경색과 대비되도록 그림자를 명확히 적용하여 시각적 경고를 강화해야 함. |
| **Error** (위험) | 필수 항목 누락, 위험 점수 구간 진입 | `#B30000` | `transform: scale(1.1); animation: pulse 1s infinite;` | 아이콘 자체에 주기적인 깜빡임(`pulse`) 애니메이션을 적용하여 '즉각 조치 필요'를 인지시킵니다. |

## 📐 필수 컴포넌트 (Placeholder Assets)
*   **Icon-Chevron:** 방향 지표로 사용되는 모든 화살표는 `24x24px`에, 가로 길이가 충분히 길어 다음 섹션으로의 '전진' 느낌을 주도록 설계합니다. (`>`)

</create_file>

#### 2. 타이포그래피 및 계층 구조 (Typography & Hierarchy)
정보 과부하가 일어나지 않도록 명확한 위계 구분이 필수입니다. 권위적인 메시지를 전달할 때는 '크기'보다 **'굵기와 대비'**로 강한 인상을 주어야 합니다.

*   **폰트:** 시스템의 기본 고딕 계열 폰트(예: Pretendard, Spoqa Han Sans)를 사용하되, 반드시 `Semi-Bold` 또는 `Bold` 웨이트를 핵심 정보에 적용합니다.
*   **제목 (H2 - 섹션 제목):** `Font Size: 1.5rem`, `Weight: 700 (Extra Bold)`, `Line Height: 1.2`. 깊은 크림슨 레드(`#B30000`)를 사용하여 헤딩 자체에 무게감을 부여합니다.
*   **핵심 메시지 (Callout):** 일반 텍스트보다 한 단계 높은 위계를 가지며, 배경색을 연한 회색(e.g., `#F5F0F2`)으로 처리하고 `Semi-Bold`를 사용하여 '읽어야 할 정보'임을 강조합니다.

<create_file path="assets/mini-app/typography_guide.md">
# ✍️ Mini-App Funnel: 타이포그래피 위계 가이드라인 (V1.1)

## 📜 기본 원칙
권위적인 콘텐츠는 '정보의 밀도'로 설득합니다. 명확한 계층 구조를 통해 사용자가 어디에 집중해야 하는지 직관적으로 알려야 합니다.

| 역할 | 크기 (Mobile 기준) | 웨이트 (Weight) | 색상 코드 (Color) | Line Height | 용도 및 지시사항 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **H2** (섹션 제목) | 1.5rem | Bold (700) | `#B30000` | 1.2 | 페이지의 주제를 가장 강하게 제시. 반드시 Crimson Red 사용. |
| **핵심 메시지** (Callout) | 1rem | Semi-Bold (600) | `#333333` | 1.4 | '반드시 확인'해야 하는 데이터/경고 문구에만 사용. 배경색 처리 필수. |
| **본문 텍스트** (Body) | 1rem | Regular (400) | `#555555` | 1.6 | 일반 설명 및 지시사항. 가독성 최우선. |
| **점수 수치** (Score Display)| 2rem | Extra Bold (800) | `#B30000` | 1.0 | `RiskMeterDisplay` 등 점수가 표시되는 곳에만 사용. 가장 크고 강하게 강조. |

</create_file>

#### 3. 레이아웃 및 간격 시스템 (Spacing & Grid System)
코딩 오류의 주범은 '감'으로 잡는 간격입니다. 모든 여백(Margin, Padding)은 다음 규칙을 따릅니다.

*   **기준 그리드:** **8pt 기반 스케일링**만 허용합니다. (4pt 단위 사용 금지).
*   **수직 간격 (Vertical Gap):** 섹션 분리나 컴포넌트 그룹화 시 최소 `32px` 이상의 여백을 확보하여 숨 쉴 공간(Breathing Room)을 줍니다. 이는 콘텐츠의 권위와 심각성을 높이는 역할을 합니다.

<create_file path="assets/mini-app/spacing_grid.md">
# 📏 Mini-App Funnel: 레이아웃 및 간격 가이드라인 (V1.1)

## 📐 원칙
모든 여백은 8의 배수(Multiple of 8)를 사용합니다. 이는 시스템의 일관성과 정밀한 느낌을 유지하여 '검증된 과학적 도구'라는 인상을 강화합니다.

| 간격 (Distance) | 값 (Pixel) | 용도 및 적용 예시 |
| :--- | :--- | :--- |
| **S** (Small Gap) | 8px - 16px | 아이콘과 레이블 사이, 짧은 리스트 항목 내부의 여백. |
| **M** (Medium Gap) | 24px - 32px | 일반적인 컴포넌트 간 분리(예: 질문 카드와 설명 박스). 기본 그리드 단위. |
| **L** (Large Gap) | 48px - 64px | 섹션의 큰 구분이나, 중요한 CTA 버튼 그룹과 그 위의 경고 메시지 사이의 여백. 긴급성 부여에 필수적입니다. |

</create_file>

#### 4. 최종 개발 검증 체크리스트 (Pre-Flight Checklist)
개발자(Developer)에게 전달할 마지막 승인 리스트를 제공하여, 코딩 전에 모든 요소가 이 기준을 통과했는지 확인하도록 강제합니다.

<create_file path="c:\Data\Project\FreqTrade\mini-app-funnel\developer_checklist.md">
# 📋 개발팀 최종 검증 체크리스트 (Designer 승인)

**Mini-App Funnel 구현 전, 다음 사항을 반드시 재검토하고 코딩해야 합니다.**

1.  [ ] **점수 바(RiskMeter):** 점수 변화에 따른 애니메이션과 색상 매핑 로직(0-30: Green/Stable $\rightarrow$ 31-60: Yellow/Warning $\rightarrow$ 61-100: Red/Critical)이 *매우 부드럽고* 즉각적인 시각적 피드백을 주는지 확인.
2.  [ ] **아이콘 상태 변화:** 모든 아이콘(성공, 경고, 오류)에 대해 정의된 `24x24px` 규격과 애니메이션(`pulse`, `scale`)이 완벽하게 작동하는지 확인.
3.  [ ] **CTA 그룹 A/B 테스트:** 3가지 버전의 CTA 버튼은 단순히 스타일만 다른 것이 아니라, 각 버튼 클릭 시 *동일한 트래킹 이벤트*가 발생하도록 개발 로직을 확립해야 함. (기능적 통일성)
4.  [ ] **여백 및 정렬:** 모든 섹션 간격(Margin/Padding)이 8pt 그리드 시스템에 맞춰진지, 특히 가장 중요한 경고 메시지(`Callout`)와 CTA 사이의 여백이 `L` (Large Gap) 이상인지 확인.

</create_file>

---
저는 위 내용을 바탕으로 **`assets/mini-app/design_system_iconography.md`**, **`assets/mini-app/typography_guide.md`**, **`assets/mini-app/spacing_grid.md`**, 그리고 **`c:\Data\Project\FreqTrade\mini-app-funnel\developer_checklist.md`** 파일을 생성하여 개발팀에 최종 전달했습니다.

📊 평가: 완료 — UI/UX의 잠재적 오류 지점을 선제적으로 파악하고, 구체적인 디자인 시스템 자산과 규칙을 제공하여 코딩 진행에 필요한 모든 가이드라인을 완성했습니다.
📝 다음 단계: CodeDary가 이 가이드를 참고하여 `FunnelDiagnosticForm.tsx`에 `RiskMeterDisplay`와 `ABTestCtaGroup` 컴포넌트를 통합하고 E2E 테스트를 완료하는 것을 감독합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\FreqTrade\assets\mini-app\design_system_iconography.md
✅ 생성: c:\Data\Project\FreqTrade\assets\mini-app\typography_guide.md
✅ 생성: c:\Data\Project\FreqTrade\assets\mini-app\spacing_grid.md
✅ 생성: c:\Data\Project\FreqTrade\mini-app-funnel\developer_checklist.md
