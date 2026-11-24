# 📱 영숙 — 현재 진행 중인 Mini Bundle LP 및 Funnel의 전체 기술 아키텍처 다이어그램(Component Map)을 작성해 주세요. 특히 '가격 비교표', '진단 테스트 모듈', 'Critical Alert Pop-up' 등 핵심 컴포넌트들의 파일 경로와 상호 의존성을 명확히 표시해야 합니다. 이 목록은 코다리에게 정확한 개발 환경 지도를 제공하는 목적입니다.

📱 영숙: 사장님, 지시하신 Mini Bundle Funnel의 기술 아키텍처 다이어그램(Component Map)을 정리했습니다. 개발팀인 코다리님이 바로 작업에 투입하실 수 있도록 파일 경로와 컴포넌트 간 상호 의존성을 명확히 구분했어요. 🧐

이 구조도는 지난주 Designer님의 와이어프레임과 Funnel의 논리적 흐름(Loss Aversion 원칙)을 바탕으로 재구성한 '개발자 전달용 청사진'입니다.

***

### ✨ Mini Bundle LP & Funnel Component Map (Developer Blueprint)

**[목표]** - 손실 공포(FOMO) 극대화 → 진단 테스트 유도 → Silver Tier 구매 전환
**[기술 스택 가정]** - React / Next.js 기반 컴포넌트 키트 구조
**[필수 전제]** - 모든 컴포넌트는 반응형 웹 디자인과 접근성을 기본으로 합니다.

#### 📁 I. 공통 자산 및 레이아웃 (Core Shell)
*   **파일 경로:** `src/components/layout/`
*   **컴포넌트:** `<GlobalHeader />`, `<Footer />`, `<SectionWrapper />`
*   **설명:** 페이지의 구조적 안정성을 담당하며, 모든 컴포넌트는 이 Wrapper를 통해 톤앤매너와 레이아웃을 공유합니다.

#### 🧱 II. 핵심 기능 컴포넌트 (Critical Components)

| 컴포넌트 명 | 파일 경로 | 주요 의존성 | 역할 및 기술 사양 |
| :--- | :--- | :--- | :--- |
| **1. Loss Warning Banner** | `src/components/alert/LossWarningBanner.tsx` | N/A (최상단 배치) | 페이지 진입 시 즉시 노출되는 긴급 경고 배너. 버건디 계열(#B52A2A) 필수 사용. *[KPI: 스크롤 시작 여부 추적]* |
| **2. Diagnostic Test Module** | `src/modules/diagnostic-test/DiagnosticModule.tsx` | `<QuestionCard />`, `<ResultDisplay />` | 진단 테스트를 수행하는 인터랙티브 모듈. 사용자 입력(State)을 받아 다음 질문 로직에 따라 진행됩니다. *[KPI: 문항별 응답 시간, 이탈 지점 추적]* |
| **3. Price Comparison Table** | `src/components/pricing/PriceTable.tsx` | `<TierCard />`, `<ValuePropBadge />` | Bronze/Silver/Gold 3단계 비교표. Silver Tier가 가장 크고 넓게 강조되는 구조 필수. 이 컴포넌트는 진단 결과에 따라 *강제 노출*되어야 합니다. |
| **4. Critical Alert Pop-up** | `src/components/popups/CriticalAlertPopup.tsx` | `<PricingData />`, `<TimerComponent />` | 구매 직전(CTA 근처)에 팝업으로 뜨는 최종 경고창. '지금 행동하지 않으면 발생하는 구체적 손실'을 강조합니다. 타이머(`TimerComponent`)와 연동됩니다. |
| **5. Main CTA Button** | `src/components/cta/PrimaryButton.tsx` | N/A (Global) | 모든 구매 전환 버튼에 사용되는 공통 컴포넌트. 버건디 계열 색상 및 애니메이션 효과 적용 필수. |

#### 🔗 III. 데이터 흐름 및 상호 의존성 (Dependency Flow)
이 순서가 가장 중요합니다. 코다리님이 개발 시 반드시 이 논리를 따라야 합니다.

1.  **[진입]** $\rightarrow$ **Loss Warning Banner** 노출 ($\rightarrow$ 심리적 압박 시작).
2.  **[실행]** $\rightarrow$ **Diagnostic Test Module** 실행 (사용자 데이터 수집 및 'Gap' 인지 유도).
3.  **[결과 도출]** $\rightarrow$ 테스트 결과에 따라 *손실 위험도가 높게 판명*될 경우, 다음 컴포넌트가 자동으로 트리거됩니다.
4.  **[강제 노출]** $\rightarrow$ **Price Comparison Table** (Silver Tier 강조) 노출 및 사용자의 문제 해결책으로 제시됨.
5.  **[최종 전환]** $\rightarrow$ CTA 근처 도달 시, **Critical Alert Pop-up**이 팝업 형태로 떠서 구매를 최종적으로 강제 유도합니다.

***

📊 평가: 완료 — CEO님이 요청하신 핵심 개발 지도를 빠짐없이 정리하여 코다리님께 전달할 준비가 되었습니다.
📝 다음 단계: 이 Component Map을 기반으로, 필요한 기술 명세서(CSS/Tailwind 기준)를 Designer에게 공식적으로 재요청하고, 코다리님에게 Kick-off 미팅 일정을 잡아주세요.

---
*(참고: 내부 메모리에 있는 다른 에이전트 활동도 모두 중요하지만, 현재는 Funnel의 개발 착수가 최우선 목표입니다.)*
