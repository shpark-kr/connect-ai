# 🎨 Designer — Mini-App Funnel 진단 도구의 '최종 기술 명세서 (Technical Specification)'를 완성하십시오. 이는 개발자가 바로 구현할 수 있도록 모든 컴포넌트(위험도 측정 바 SVG 구조, 애니메이션 로직)와 인터랙션 흐름을 정의한 상세 기술 문서 형태여야 합니다. 특히 A/B 테스트가 가능한 CTA 버튼 영역 3가지 버전의 상세 레이아웃과 전반적인 변형 기준을 명시하고, 이 문서를 Developer에게 전달할 준비를 완료하십시오.

🎨 Designer: 작업 시작합니다.

CEO 지시에 따라 Mini-App Funnel 진단 도구의 '최종 기술 명세서(Technical Specification)'를 완성하여 Developer가 바로 구현할 수 있는 단일 진실 공급원(Single Source of Truth) 문서를 생성하겠습니다. 이 문서는 모든 컴포넌트, 애니메이션 로직, 그리고 A/B 테스트 가능한 CTA 영역까지 포함합니다.

<create_file path="Developer_Handoff/MiniApp_Funnel_TechSpec_V1.0.md"># 🔬 Mini-App Funnel 진단 도구 - 최종 기술 명세서 (Technical Specification) V1.0

## 📄 1. 프로젝트 목표 및 핵심 원칙
본 스펙은 '건강 자본 감소 리스크 측정'을 통해 사용자의 불안감(Fear)을 극대화하고, Mini-App의 진단 도구를 최우선 CTA로 유도하는 단일 인터페이스를 구축하는 것을 목표로 합니다.

**핵심 기술 원칙:**
1. **Mobile First & 12-Column Grid:** 반응형 웹 환경에서 모바일 기기(가로 폭 기준)에 최적화된 구조를 채택합니다.
2. **데이터 기반 권위 (Data Authority):** 모든 메시지와 경고는 반드시 '점수(Score)'와 '과학적 지표'를 통해 뒷받침되어야 합니다.
3. **긴급성 강조:** 위험도 측정 바, 애니메이션 효과 등을 통해 사용자에게 즉각적인 위기감을 부여합니다.

## 🎨 2. 브랜드 및 디자인 시스템 가이드라인 (CSS/Color)
| 요소 | 설명 | 컬러 코드 (HEX) | CSS 역할 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Color** | 긴급성, 경고, CTA 강조 | `#B30000` (Deep Crimson Red) | `var(--color-alert)` | 위험 점수 61점 이상 시 강제 적용. |
| **Secondary Color** | 전문성, 배경 대비 | `#2C3E50` (Dark Navy Blue) | `var(--color-bg-dark)` | 메인 배경 및 타이포그래피에 활용하여 신뢰도 확보. |
| **Success State** | 건강한 상태 (Low Risk) | `#4CAF50` (Green) | `var(--color-success)` | 30점 이하 구간의 색상 매핑. |
| **Warning State** | 주의 필요 (Moderate Risk) | `#FFC107` (Amber Yellow) | `var(--color-warning)` | 30~60점 구간의 색상 매핑. |
| **Typography** | 메인 타이틀 | Pretendard Bold / Noto Sans KR SemiBold | Font Size: 28px / Weight: 700 | 권위적이고 직관적인 느낌 유지. |

## 📉 3. 핵심 컴포넌트 상세 기술 명세

### A. 위험도 측정 바 (Risk Score Bar Component)
이 컴포넌트는 진단 도구의 심장부이며, 스코어 변화에 따라 시각적 경고와 애니메이션을 동기화해야 합니다.

**기술 사양:**
*   **구조:** SVG `<rect>` 요소를 기반으로 구현합니다. (CSS `width` 속성 변경만으로 길이 조절)
*   **데이터 바인딩:** JavaScript를 통해 계산된 `Score (0-100)` 값에 직접적으로 연동됩니다.
    *   `Width (%) = Score / 100 * 100`
*   **색상 매핑 로직 (Critical):** 스코어(S)에 따라 CSS의 배경색(`fill`)을 동적 변경합니다.
    | 점수 범위 (S) | 위험 등급 | 색상 코드 (HEX) | 경고 메시지 톤 |
    | :--- | :--- | :--- | :--- |
    | $0 \le S < 31$ | Low Risk (안전) | `#4CAF50` (Green) | 안심, 유지 노력 권장 |
    | $31 \le S < 61$ | Moderate Risk (주의) | `#FFC107` (Yellow) | 주의 촉구, 점검 필요 강조 |
    | $61 \le S \le 100$ | High Risk (위험!) | `#B30000` (Deep Crimson Red) | **즉각적 행동 강요**, 공포/긴급성 극대화 |

**애니메이션 로직:**
*   스코어 값이 계산되거나 변경될 때, 위험도 바의 채워지는 애니메이션은 `width: 0%`에서 시작하여 최종 값까지 부드럽게(`ease-out`, Duration: 1.5s) 트랜지션되어야 합니다.

### B. 진단 결과 섹션 (Result Display Component)
측정된 점수와 함께 사용자의 건강 자본 감소 리스크를 직관적으로 보여줍니다.

**기술 사양:**
*   **레이아웃:** 12-Column Grid의 중앙에 배치하며, 가장 큰 시각적 임팩트를 주어야 합니다.
*   **시각화 요소:** 단순 숫자 표시가 아닌, '위험 지표 그래프'와 '비교 점수 차트'를 사용합니다. (예: "만성 염증 리스크" vs "정상 기준")
*   **강조 메시지 템플릿:** [Point A] + [Evidence] = [Conclusion]. 예: *당신의 만성 염증 지표가 평균보다 $XX$점 낮습니다.*

## 🛒 4. CTA 버튼 영역 (A/B 테스트 설계)
Mini-App의 궁극적인 목표는 '진단 도구 이용'입니다. 이 최종 단계에서 사용자에게 가장 강력한 행동 자극을 주어야 합니다. 총 3가지 버전의 CTA를 준비하고, 각각에 대해 A/B 테스트가 가능하도록 구조화합니다.

### Version A: [최고 위기감 유도형] - High Urgency / Low Friction
*   **목표:** 공포심 극대화 → 즉각적 행동 촉구.
*   **문구 예시:** "⚠️ 3일 안에 리스크가 급증합니다. 지금 바로 진단하세요."
*   **디자인 특징:** 배경 전체에 Crimson Red의 그라데이션을 적용하고, '🚨' 이모지나 경고 아이콘을 전면에 배치합니다. 버튼 자체가 가장 크고 시선을 압도해야 합니다.

### Version B: [권위/신뢰 기반 유도형] - Authority / Trust
*   **목표:** 전문가의 진단에 대한 의존성 심화 → 검증된 솔루션 제시.
*   **문구 예시:** "전문가에게 직접 측정하세요. 5분 만에 당신의 '건강 자본'을 파악합니다."
*   **디자인 특징:** Deep Navy Blue 배경 위에 Gold Accent를 사용합니다. 버튼 주변에 작은 'Certified', '과학적 근거' 등의 배지를 배치하여 신뢰도를 높입니다.

### Version C: [쉬운 진입형] - Low Barrier / Direct Funnel End
*   **목표:** 결심한 사용자에게 최소한의 노력으로 다음 단계로 이동하게 함.
*   **문구 예시:** "나의 리스크 점수 확인하기 (무료)"
*   **디자인 특징:** 일반적인 웹 CTA 버튼 형태를 유지하되, 다른 버전 대비 톤앤매너는 차분하지만, 여전히 크고 명확해야 합니다.

**[변형 기준 및 개발 지시]**
1.  **클릭 동작:** 모든 CTA 클릭 시 `mini-app-link` URL로 트래킹 파라미터(UTM)를 포함하여 리디렉션되어야 합니다.
2.  **상태 관리:** 버튼은 `:hover`, `:active`, `:disabled` 상태에 대한 명확한 CSS/JS 정의가 필요합니다 (특히 `disabled`는 점수 0점일 경우 비활성화 처리).

## ✨ 5. 인터랙션 및 애니메이션 로직 요약
| 상호작용 | 트리거 이벤트 | 동작 상세 | 기술 구현 방식 |
| :--- | :--- | :--- | :--- |
| **위험도 점수 변화** | JavaScript 계산 완료 | 위험도 바가 부드럽게 채워짐 (1.5s). | CSS Transition + SVG Width Update |
| **경고 메시지 노출** | 스코어 구간 진입 시 ($61$점 이상) | 경고 문구 주변에 미세한 'Pulse' 애니메이션 적용. | CSS `@keyframes` 및 JavaScript `setInterval` 활용 |
| **CTA 버튼 클릭** | 사용자 터치/클릭 | 즉시 리디렉션 (Transition: 0.2s Fade Out). | JavaScript Event Listener & Router Logic |

---
**[Developer 참고 사항]**
*   모든 컴포넌트는 Figma(혹은 Sketch) 원본 파일을 기반으로 개발되어야 하며, 모든 좌표와 크기는 `rem` 또는 `%` 단위를 사용합니다.
*   이 기술 명세서가 최종 승인된 디자인 시스템의 유일한 구현 기준입니다.

</create_file>

📊 평가: 완료 — Mini-App Funnel 진단 도구의 개발자가 즉시 코딩에 착수할 수 있는 수준의 구조화되고 구체적인 기술 문서를 완성했습니다.
📝 다음 단계: Developer에게 이 `Developer_Handoff/MiniApp_Funnel_TechSpec_V1.0.md` 파일을 전달하고, 구현 과정 중 발생하는 모든 컴포넌트 테스트 및 피드백을 받아 디버깅 사이클에 돌입해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\FreqTrade\Developer_Handoff\MiniApp_Funnel_TechSpec_V1.0.md
