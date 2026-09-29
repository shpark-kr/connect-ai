# 📝 CEO 종합 보고서

🎨 Designer: 작업 시작합니다.

[CEO의 지시]는 MiniFunnel 결제 경험의 가장 중요한 전환점(Critical Moment)에 대한 UX/UI 완성도를 극한으로 끌어올리는 매우 가치 높은 요청입니다. 단순히 색상 변경을 넘어, '위기감 완화'라는 심리적 목표를 달성하는 애니메이션 매뉴얼이 필요합니다.

이는 **[c:\Data\Project\FreqTrade\DesignSystem\MiniFunnel_QA_Mockup_Spec_V3.md]**에 정의된 QA Mockup을 기반으로, 개발자가 바로 구현할 수 있도록 **'Interaction Sequence Spec Sheet'** 형태로 재정립하겠습니다.

---

# 🛠️ MiniFunnel 결제 게이트웨이 전환 애니메이션 매뉴얼 (v1.0)
**제목:** Deep Crimson Alert $\rightarrow$ System Recovery Protocol Transition
**목표:** 사용자에게 '시스템 실패(Failure)'의 충격을 준 뒤, 다음 단계로의 논리적이고 심리적으로 수용 가능한 진입 경로를 제공한다. 위기감을 급격히 낮추지 않고, *다음 행동*으로 초점을 전환시킨다.

## 🎨 핵심 컬러 정의 (Color Palette)
| 상태 | 색상명 | Hex Code | 사용 목적 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **Critical Alert** (Start) | Deep Crimson Red | `#A30012` | 최고 위기감, 시스템 오류 경고. | 충격 및 공포 유발. |
| **Transition Mid-State** | Glitch Magenta | `#B8496D` | 시스템 불안정 상태 시각화. | 색상 간의 혼란과 떨림 표현. |
| **Recovery Protocol** (End) | Soft Amber Yellow | `#FFC700` | 경고 해제, 다음 단계 유도, 안내. | '안심'이 아닌 '주의 환기' 톤 유지. |
| **Success/Action** | Deep Navy Blue | `#1A237E` | 브랜드 신뢰도 및 CTA 영역. | 안정적인 배경색 역할. |

## ⏳ 애니메이션 타이밍 및 가이드 (Interaction Sequence Spec)
**총 예상 시간:** $5,000\text{ms}$ (Start: $\text{T}=0$)

### Phase 1: 시스템 충격 발생 (Deep Crimson Alert)
**(Time Span: T=0ms to T+2,000ms)**

| 요소 | 애니메이션 동작 | 타이밍 및 이징(Easing) | 개발 가이드라인 |
| :--- | :--- | :--- | :--- |
| **UI 배경/프레임** | Deep Crimson Red로 강하게 플래시 (Flash). 전체 화면에 얇은 노이즈 오버레이 (`Noise Overlay`)를 적용. | $\text{T}=0\text{ms}$에서 $100\%$ 투명도까지 급격히 변함. **반복:** $50\text{ms}$ 간격으로 플래시 반복 (최대 3회). | `opacity` 속성을 활용하여 짧고 강한 깜빡임을 구현. 배경 전체에 적용. |
| **오류 메시지** | `[ERROR CODE: XXX]`가 화면 중앙에서 나타남. 글자가 떨리며(Shake) 불안정하게 표시됨. | $\text{T}=0\text{ms}$에 팝인(Pop-in). 이후 $2,000\text{ms}$ 동안 지속적인 미세한 `Vibration` 효과 적용. | CSS Transform을 이용해 축 방향으로 무작위 진동(`translateX`/`translateY`) 부여. |
| **CTA 영역** | 버튼이 완전히 비활성화(Disabled)되며, Deep Crimson Red의 낮은 광원 효과만 유지됨. 클릭 이벤트는 완전히 막힘 (Event Listener: `none`). | $\text{T}=0\text{ms}$에 즉시 적용. | 사용자에게 어떠한 액션도 불가능함을 시각적으로 강제해야 함. |

### Phase 2: 전환 및 시스템 불안정화 (Glitch Transition)
**(Time Span: T+2,000ms to T+3,500ms)**

| 요소 | 애니메이션 동작 | 타이밍 및 이징(Easing) | 개발 가이드라인 |
| :--- | :--- | :--- | :--- |
| **전체 UI/색상** | Deep Crimson Red가 빠르게 `Glitch Magenta` 계열로 색상이 스며들기 시작함. 화면에 수평선 형태의 왜곡(Chromatic Aberration) 효과를 노이즈와 함께 삽입. | $\text{T}=2,000\text{ms}$부터 $1,500\text{ms}$ 동안 진행. **Easing:** `ease-in-out` (불안정한 느낌). | 색상 변화가 갑작스럽기보다 '스며드는' 듯한(Diffusion) 효과를 우선 구현. |
| **오류 메시지** | 오류 코드가 깜빡이던 노이즈와 함께 *데이터 스트리밍*처럼 흐릿해지고, 글자가 깨지는(`Pixelation`) 시각적 처리가 동반됨. | $\text{T}=2,000\text{ms}$부터 $1,500\text{ms}$. | `filter: blur()`와 `clip-path`를 조합하여 데이터가 붕괴되는 느낌을 연출. |
| **사용자 심리 유도** | 화면 하단에 작은 글씨로 "잠시만 기다려 주십시오..." 메시지를 아주 희미하게 표시하기 시작함. (이것이 다음 단계의 예고임) | $\text{T}=2,500\text{ms}$ 지점부터 점진적 노출. | 텍스트 투명도를 $10\%$에서 $30\%$로 서서히 증가시킴. |

### Phase 3: 회복 프로토콜 및 행동 유도 (Soft Amber Yellow Recovery)
**(Time Span: T+3,500ms to T+5,000ms)**

| 요소 | 애니메이션 동작 | 타이밍 및 이징(Easing) | 개발 가이드라인 |
| :--- | :--- | :--- | :--- |
| **UI 배경/색상** | 전체 색상이 `Soft Amber Yellow` 계열로 안정화됨. 노이즈와 플래시 효과가 완전히 사라지고, 차분하지만 주의를 요하는 광원(Ambient Glow)만 남음. | $\text{T}=3,500\text{ms}$에 $100\%$ 완료. **Easing:** `ease-out` (안정화). | 색상 전환 시 부드러운 곡선(`Cubic Bézier`)을 사용하되, 여전히 '경고'의 느낌은 유지해야 함. |
| **메인 메시지** | "데이터 처리 중입니다. 다음 단계 확인 필요." 또는 "시스템 재점검: [다음 체크리스트 항목]" 등의 명확한 가이드 메시지가 등장함. | $\text{T}=3,500\text{ms}$에 팝업되어 높은 대비(Contrast)로 강조됨. | 단순 알림이 아닌, *진행 중인 프로세스*임을 암시하는 문구를 사용해야 함. |
| **CTA 영역 (Recovery CTA)** | Deep Crimson Red 경고는 사라지고, Soft Amber Yellow를 배경으로 한 새로운 버튼(`Next Step Check`)이 나타남. 이 버튼은 활성화(Active)되어 마우스를 올릴 때 미세하게 빛나거나 떨리는 효과가 있어야 함. | $\text{T}=4,500\text{ms}$에 등장하여 사용자 행동을 유도함. | **핵심:** 사용자가 '위기 해소'의 기분을 느끼는 순간, 다음 단계로 넘어갈 수 있다는 희망(Hope)을 시각적으로 제공해야 합니다. |

---
📊 평가: 완료 — CEO의 지시에 따라 개발자 친화적인 상세 타이밍 및 인터랙션 시퀀스를 완성했으므로, 이 산출물만으로 목표가 달성됩니다.
📝 다음 단계: Codari에게 본 매뉴얼을 전달하고, 특히 $\text{T}=2,000\text{ms}$ 지점의 색상 전환(Phase 2) 구현에 집중하도록 요청하십시오.
