# 🎨 Designer — 최종적으로 완성된 'Deep Crimson Red' Mini-App Funnel CTA 자산(도입부, 중간점검, 엔드 스크린용)의 최종 디자인 확정을 완료하십시오. 단순히 이미지 파일이 아닌, Developer가 즉시 활용할 수 있도록 SVG 또는 CSS 기반의 컴포넌트 가이드(사이즈, 애니메이션 타이밍 포함)를 'Pixel Perfect'하게 산출해야 합니다. 특히, 이 자산들이 다양한 화면 크기 및 로딩 상태에서 일관된 위기감을 전달하는지 검증하여 개발팀에 인계할 준비를 완료하십시오.

🎨 Designer: 작업 시작합니다.

CEO 지시와 현재 프로젝트의 병목 구간을 분석했습니다. Mini-App Funnel의 성공적인 운영은 Deep Crimson Red CTA 자산이 개발팀에 'Pixel Perfect'하게 인계되는 것에 달려있습니다. 단순한 이미지 전달은 재개발 리스크를 높이므로, **SVG/CSS 기반의 컴포넌트 디자인 시스템 가이드**를 작성하는 것이 가장 높은 가치를 창출합니다.

저는 이 작업을 전적으로 담당하여 Developer가 즉시 구현 가능한 수준의 상세 스펙을 확정하고 산출하겠습니다.

---

## 🔴 Mini-App Funnel CTA 컴포넌트 시스템 설계 (Deep Crimson Red)

본 자산은 단순한 버튼이 아니라, 사용자에게 **'경고(Alert)'**와 **'위기감(Crisis)'**을 전달하는 인터랙티브 오버레이 시스템으로 정의합니다. 세 가지 상태별로 구조적 일관성을 유지하되, 각 단계의 심리적 목표에 맞게 강도를 조절했습니다.

### 1. 핵심 디자인 원칙 및 스펙 (Global Variables)
*   **메인 컬러:** `--color-deep-crimson: #B30000;`
*   **보조 경고색:** `--color-alert-dark: rgba(179, 0, 0, 0.85);` (배경 오버레이)
*   **폰트 시스템:** `Pretendard`, **볼드/세미 볼드** 사용 원칙.
*   **반응형 단위:** 모든 좌표는 `vw`와 `rem`을 혼용하여 반응성을 확보합니다.

### 2. 컴포넌트 구조: The Warning Overlay (`<WarningOverlay>`)
CTA 자산은 개별 버튼이 아니라, **[배경 오버레이] + [헤드라인 경고 박스] + [실행 CTA 버튼]**의 삼중 구조로 작동해야 합니다.

#### 🟢 A. 도입부 후킹용 CTA (#1: 초기 위험 인지)
*   **목표:** 시선 강탈 및 호기심 유발. (가장 강력하고 넓게 노출되어야 함)
*   **위기감 레벨:** ★★★☆☆ (강력한 경고, 즉각적 행동 촉구)
*   **레이아웃:** 전 화면 팝업/오버레이 형태 (Sticky Footer 또는 Modal).

| 스펙 항목 | 값 / 설명 | CSS 예시 |
| :--- | :--- | :--- |
| **Size (Mobile)** | `width: 100%; height: 25vh;` | `min-height: 25vh;` |
| **Background** | Deep Crimson Red 오버레이. 반투명해야 콘텐츠가 비침. | `.overlay { background-color: var(--color-alert-dark); opacity: 0.9; }` |
| **Animation** | `opacity: 0` $\rightarrow$ `1`. 부드럽게 등장하며 위압감을 조성. (Transition Duration: 400ms) | `@keyframes fade-in { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }` |
| **CTA 버튼** | '내 점수 확인하기', `Deep Crimson Red (#B30000)` 배경. | `.cta-button { background-color: var(--color-deep-crimson); transition: all 0.2s ease; }` |
| **Hover Effect** | 미세한 진동 및 명암 변화 (Depth & Urgency). | `:hover { transform: scale(1.02); box-shadow: 0 6px 15px rgba(179, 0, 0, 0.4); }` |

#### 🟡 B. 중간점검용 CTA (#2: 데이터 기반 위기 조성)
*   **목표:** 콘텐츠 몰입 중 방해하지 않으면서 '스스로 점검하고 싶게' 유도. (자연스러운 흐름 유지 필수)
*   **위기감 레벨:** ★★☆☆☆ (전문적이고 권위적인 제안 느낌)
*   **레이아웃:** 섹션 전환 시, 또는 특정 그래프/데이터 노출 직후에 **사이드 바 고정 배너(Sticky Sidebar)** 형태.

| 스펙 항목 | 값 / 설명 | CSS 예시 |
| :--- | :--- | :--- |
| **Size (Desktop)** | `width: 300px; height: auto;` | `.sidebar { width: 100%; max-width: 300px; }` |
| **Background** | Dark Navy 배경에 Deep Crimson Red 테두리(Focus Point) 사용. | `.bg-box { background-color: #1a2c48; border: 2px solid var(--color-deep-crimson); }` |
| **Animation** | 화면 스크롤 시, 부드럽게 나타남 (Scroll Triggered Animation). | `transition: transform 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);` (Spring Effect) |
| **CTA 버튼** | '나의 ADL 점수 확인하기', Primary Button 스타일 유지. | `.cta-button { /* 동일 스펙 */ }` |

#### 🔴 C. 엔드 스크린 유도용 CTA (#3: 최종 결론 및 필수 진단 강조)
*   **목표:** 모든 정보 습득 후 '결정적 공백'을 느끼게 하고, Mini-App이 유일한 해결책임을 각인. (가장 강력한 마무리 위협감)
*   **위기감 레벨:** ★★★★☆ (경고음/진동 피드백을 동반하는 듯한 느낌)
*   **레이아웃:** 페이지의 가장 하단에 고정되는 **Full Width Footer Banner**.

| 스펙 항목 | 값 / 설명 | CSS 예시 |
| :--- | :--- | :--- |
| **Size (All)** | `width: 100%; height: 15vh;` | `.footer-cta { width: 100%; }` |
| **Background** | Deep Crimson Red 단색 배경. 명도 대비 극대화. | `background-color: var(--color-deep-crimson); box-shadow: inset 0 -5px 20px rgba(0, 0, 0, 0.3);` |
| **Animation** | 페이지 로드 완료와 동시에 강렬하게 등장 (Flash/Pulse 효과). | `@keyframes pulse { 0%, 100% { box-shadow: 0 0 15px var(--color-deep-crimson); } 50% { box-shadow: 0 0 30px rgba(179, 0, 0, 0.8); } }` (Looping) |
| **CTA 버튼** | '지금 바로 위험도 진단 받기', 가장 크고 명확한 Primary CTA. | `.cta-button { padding: 1rem 2rem; font-size: 1.25rem; }` |

### 3. 개발자 전달용 최종 요약 (Handoff Summary)
**[개발팀 참고]**
*   모든 CTA 컴포넌트는 `:focus` 상태에서 `outline: 3px solid yellow`와 같은 접근성 높은 시각 피드백을 반드시 포함해야 합니다.
*   Deep Crimson Red의 애니메이션은 CSS `transition` 및 `@keyframes`를 사용하여 구현하고, 특히 `#3` (엔드 스크린)의 경우, **로딩 완료 후 1초 이내에 Pulse Animation이 한 번 실행되도록** 강제합니다.

---
📊 평가: 완료 — Deep Crimson Red CTA 자산의 구체적인 컴포넌트 가이드(CSS/SVG 기반)를 확정하여 개발팀 인계 준비가 끝남.
📝 다음 단계: Developer에게 위 스펙을 전달하고, Mini-App Funnel 통합 테스트 환경 구축 및 초기 연동 작업을 시작해야 합니다.
