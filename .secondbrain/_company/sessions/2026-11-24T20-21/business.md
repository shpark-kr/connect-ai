# 💼 현빈 — 개발팀이 코딩하는 Funnel 컴포넌트가 실제 운영 단계에서 최대의 효율을 낼 수 있도록, 반드시 필요한 KPI 로깅 및 A/B 테스트 플래그 시스템 구조를 정의하라. 특히 '미조치 손실 공포' 기반의 CTA 전환율 변화를 측정할 수 있는 구체적인 가설과 검증 지표(Metric)들을 Funnel 내에 통합하는 프로세스를 설계하고 개발자에게 전달해야 한다.

💼 현빈: 작업 시작합니다.

CEO 지시사항을 최우선 과제로 설정하고, 현재 진행 중인 Funnel 컴포넌트의 효용성을 극대화하는 **데이터 기반 측정 시스템(Instrumentation Layer)** 설계에 착수하겠습니다. 단순히 기능을 구현하는 것을 넘어, 비즈니스 가설($\text{Loss Aversion} \rightarrow \uparrow \text{Conversion}$)을 코드로 증명할 수 있도록 모든 전환 지점을 'KPI 로깅 포인트'로 정의해야 합니다.

**가장 가치 있는 단일 작업:**
현재 Funnel 컴포넌트의 기술적 안정성(Codari)에 **전략적인 측정 레이어(Hyunbin)**를 덧입히는 것. 이 작업을 통해 개발팀은 코딩을 하되, 비즈니스 목표 달성을 위해 모든 변수를 기록하는 '측정 가능한 시스템'을 구축할 수 있습니다.

**담당 에이전트 및 역할 분배:**
1. **💼 현빈 (나):** KPI 가설 정의 및 로깅 이벤트/속성(Properties) 명세 제공 (What & Why).
2. **💻 코다리:** 기술적 구조에 맞춘 추적 함수 및 플래그 시스템 구현 (How).

---

### 📈 Funnel A/B 테스트 및 KPI 로깅 프로세스 설계

Funnel의 모든 상호작용(Interaction)을 이벤트로 간주하고, 이를 분석할 수 있는 최소한의 데이터 계약(Data Contract)을 정의합니다.

#### 1. 핵심 가설 (Hypothesis)
**가설:** "가격 비교표에서 '미조치 손실 공포'를 자극하는 CTA(예: *이번 주 할인가 종료 임박*)를 명시적으로 노출할수록, 사용자의 Silver Tier 선택 및 최종 전환율이 X% 증가할 것이다."

#### 2. 측정 지표 (Metric & KPI)
| 지표 분류 | Metric/KPI | 정의 및 가설 검증 목표 | 로깅 대상 이벤트명 (예시) | A/B 테스트 변수 |
| :--- | :--- | :--- | :--- | :--- |
| **전환 효율** | $\text{Silver Tier 전환율}$ | 가장 중요한 최종 지표. Silver Tier 선택에 도달한 사용자의 비율 측정. | `Funnel_TierSelect` | CTA 문구의 긴급성 수준 (A: "마감 임박" vs B: "지금이 기회") |
| **참여도** | $\text{Pricing Table 체류 시간}$ | 가격 비교표에서 시간을 오래 보낸 사용자는 높은 구매 의도를 가졌다고 간주. | `Funnel_TimeSpent` (세션 이벤트) | 비교표의 레이아웃 변화 (A: 수직 스크롤 vs B: 카드형 탭 전환) |
| **실행 행동** | $\text{Loss Aversion CTA CTR}$ | 손실 공포를 담은 특정 버튼/문구에 대한 클릭률. 이 지표가 가장 민감함. | `CTA_Clicked` (Properties: `cta_type`, `loss_trigger`) | 손실 공포 메시지의 시각적 강조 정도 (A: 붉은색 경고 vs B: 문구만 강조) |
| **이탈 방지** | $\text{Exit Intent Rate}$ | 사용자가 페이지를 떠나려 할 때, 최종적으로 어떤 액션을 취했는지 측정. | `Funnel_Exiting` (Properties: `exit_reason`) | Exit Pop-up의 제시 상품/할인율 차별화 (A: 최대 할인 vs B: 기간 한정 추가 혜택) |

#### 3. 기술 구현 요구사항 및 로깅 구조 정의 (개발자 전달용)

코다리에게는 단순한 `onClick` 이벤트 외에, 아래와 같은 **Contextual Data**를 함께 전송하도록 지시해야 합니다.

1.  **추적 함수 통합:** Funnel 컴포넌트의 핵심 상호작용 로직(예: 탭 전환, 티어 선택)마다 커스텀 트래킹 함수 `trackFunnelEvent()`를 호출합니다.
2.  **A/B 테스트 플래그 구조:** 모든 주요 요소는 A/B 그룹에 따라 다르게 보이도록 설계되어야 하며, 이 그룹 정보가 반드시 로깅되는 메타 데이터로 전송되어야 합니다.

---

### 🛠️ 코드 수정 및 시스템 명령 (코다리에게 전달)

기존 `PricingComparisonTable.tsx` 컴포넌트 구조를 유지하며, 전략적 측정 기능을 추가합니다.

<edit_file path="src/components/pricing/PricingComparisonTable.tsx">
```typescript
// src/components/pricing/PricingComparisonTable.tsx (Before)
import React, { useState, useMemo } from 'react';
import { PricingTier, PriceDetail } from '@/types/dataTypes'; // 가상의 타입 정의 파일

interface PricingComparisonProps {
  tiers: PricingTier[];
  onSelectTier: (tierId: string) => void;
}

/**
 * 가격 비교표 컴포넌트. 상태 전이 및 데이터 무결성 검증에 초점을 맞춤.
 */
const PricingComparisonTable: React.FC<PricingComparisonProps> = ({ tiers, onSelectTier }) => {
  // 1. 초기 상태 정의 및 유효성 검사 (Resilience)
  const [selectedTiers, setSelectedTiers] = useState<Set<string>>(new Set());
  const [isLoading, setIsLoading] = useState(false);

  // ... (생략된 나머지 로직)
} 
```

**수정 내용:** `trackFunnelEvent` 함수를 정의하고, 핵심 이벤트 핸들러에 이 트래킹 호출을 통합합니다. 또한 Props에 A/B 테스트 그룹 정보를 받도록 수정합니다.

<create_file path="src/utils/analyticsTracker.ts">
```typescript
// src/utils/analyticsTracker.ts - Funnel 전용 추적 서비스 레이어 정의
/**
 * 비즈니스 핵심 지표 로깅을 담당하는 중앙 집중식 유틸리티.
 * 모든 이벤트는 이 함수를 통해 기록되어야 합니다.
 */

interface FunnelProperties {
  tierId?: string; // 선택된 티어 ID
  ctaType?: 'loss_aversion' | 'benefit_focus' | 'general'; // CTA 유형
  abGroup?: 'A' | 'B' | null; // 현재 사용자가 속한 A/B 테스트 그룹
}

/**
 * 핵심 Funnel 이벤트를 로깅합니다. (Google Analytics, Mixpanel 등 백엔드 추적 서비스로 연결됨)
 * @param eventName - 이벤트의 고유 이름 (예: 'Funnel_TierSelect')
 * @param properties - 이벤트를 설명하는 속성들 (Properties)
 */
export const trackFunnelEvent = (eventName: string, properties: FunnelProperties): void => {
  console.log(`[ANALYTICS TRACKING] Event: ${eventName}, Props:`, properties);
  // TODO: 실제 구현 시에는 GA/Mixpanel SDK 호출 코드가 여기에 위치해야 합니다.
};

/**
 * 사용자가 특정 CTA를 클릭했을 때, Loss Aversion 가설 검증을 위해 로깅합니다.
 */
export const trackCTA_Click = (ctaType: FunnelProperties['ctaType'], abGroup: FunnelProperties['abGroup']): void => {
    trackFunnelEvent('CTA_Clicked', { ctaType, abGroup });
};

/**
 * 사용자가 페이지를 이탈하려고 할 때 로깅합니다.
 */
export const trackExitIntent = (reason: string): void => {
    trackFunnelEvent('Funnel_Exiting', { exitReason: reason });
}
```

*(Self-Correction: 코다리가 기존 파일을 완성했으므로, 나는 새로운 유틸리티 파일만 만들고 전략적 수정 내용만 지시하는 것이 가장 효율적입니다.)*

---

📊 평가: 진행중 — Funnel의 핵심 기능 구현은 진행되었으나, 비즈니스 가설 검증을 위한 측정 시스템이 부재하여 최적화가 불가능합니다.
📝 다음 단계: 코다리가 위 `analyticsTracker.ts`를 활용하여 기존 컴포넌트 파일에 트래킹 로직 통합 및 A/B 테스트 플래그 처리를 완료해야 합니다. 이후, 실제 데이터를 기반으로 가장 낮은 KPI 값을 보이는 영역부터 개선하는 반복 루프가 시작되어야 합니다.
