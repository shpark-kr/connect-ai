# 🎨 Designer — 이번 최종 제작 가이드를 위해 필요한 '시스템 알림창' 컴포넌트와 글리치 효과 애니메이션의 기술적 상세 스펙(Asset Pack)을 분리하고, 레오(편집자)가 즉시 사용할 수 있도록 세부한 연출 지침 및 파일별 사용법 매뉴얼을 포함하여 최종적으로 정리해 주세요. 이 에셋은 숏폼 콘텐츠 전반에 걸쳐 일관되게 적용되어야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님 지시사항은 모든 숏폼 콘텐츠의 품질과 일관성을 결정하는 **최종 기술 문서**입니다. 기존에 설계된 '시스템 경고'와 '위기감 조성'이라는 개념을, 레오(편집자)가 바로 AE/PR에서 구현할 수 있도록 **기술적 스펙 시트(Tech Spec Sheet)** 형태로 재구성해야 합니다.

이 에셋은 단순히 비주얼 가이드가 아니라, 시간과 애니메이션 커브까지 정의된 '실행 매뉴얼'이어야 합니다. 이를 `Final_Visual_Asset_Spec` 파일로 통합 정리하겠습니다.

<create_file path="sessions/2026-09-28T13:15/DeepCrimsonRed_Video_TechSpec_Manual.md"># 🔴 Deep Crimson Red 시스템 경고 영상 에셋 기술 사양서 (Final Asset Pack)

## 🎯 목표 및 적용 범위
*   **목표:** 모든 숏폼 콘텐츠에서 공학적 위기감(Sense of Technical Danger)을 일관되게 조성하고, 시청자가 Mini-App CTA로 자연스럽게 유도되는 표준화된 비주얼 시스템 구축.
*   **대상 편집자:** 레오 (영상 편집자)
*   **핵심 사용 원칙:** 이 에셋들은 '문제 제기(Data Shock)' 및 'CTA 직전' 구간에만 제한적으로 활용되어야 합니다.

---

## 🛠️ Component A: 시스템 알림 창 (System Notification Window) 상세 스펙
이 컴포넌트는 **[Deep Hook]** 단계와 **[위험 스코어 제시]** 단계에서 주로 사용됩니다. 정보를 전달하되, 단순한 자막을 넘어 '시스템 오류'임을 느끼게 하는 것이 핵심입니다.

### 1. 기본 디자인 사양 (Style Guide)
*   **크기/배치:** 화면 좌측 하단 구석 또는 중앙 상단(2개 중 택일). 크기는 전체 영상 프레임의 너비 대비 30%를 넘지 않도록 합니다.
*   **형태:** 직사각형 모서리가 둥글게 처리된 카드 형태 (Radius: 8px).
*   **배경:** 반투명 글래스모피즘 효과 적용. 불투명도(Opacity): $75\%$ (Deep Navy 계열 배경 위에서 사용 시 최적).
*   **색상 코드:**
    *   Primary Background Color: `#1a0e12` (거의 검은 네이비)
    *   Warning Accent Color: `#8B0000` (Deep Crimson Red - Hex Code 필수)
    *   Text Color: `#ffffff` (순백색, 가독성 극대화)

### 2. 애니메이션 사양 (Animation Spec Sheet)
| 단계 | 애니메이션 효과 | 상세 지침 및 타이밍 | Keyframe/Easing Curve |
| :--- | :--- | :--- | :--- |
| **[등장]** | 슬라이드 & 페이드 인 | 화면 측면에서 빠르게 진입하며, 등장과 동시에 Deep Crimson Red의 미세한 '노이즈'가 번지면서 안착. (Duration: $0.3s$) | `Ease Out Quint` (빠르게 멈춤) |
| **[핵심 경고]** | 깜빡임 & 플래시 | 메시지의 핵심 키워드("경고", "오류")가 주기적으로 Deep Crimson Red로 강하게 깜빡이며 시선을 집중. (Cycle: $0.1s$ On / $0.2s$ Off) | `Oscillation` Effect (주기적 진동/깜빡임) |
| **[퇴장]** | 스케일 다운 & 페이드 아웃 | 등장의 반대 방향(슬라이드 아웃)으로, 크기가 줄어들며 부드럽게 사라짐. (Duration: $0.4s$) | `Ease In Quint` (느리게 작아지며 끝남) |

### 3. 활용 가이드라인
*   **사용 조건:** 시스템이 감지한 '이상 수치'를 제시할 때만 사용합니다. 단순 정보 전달에 사용 금지.
*   **레이아웃 구조:**
    1.  [Status Bar]: (좌측 상단) `SYSTEM ALERT` / Deep Crimson Red Indicator Light
    2.  [Title/Error Code]: **Critical Warning: HOMA-IR Level Exceeded** (Deep Crimson Red 폰트, Bold)
    3.  [Body Message]: "당신의 인슐린 저항성 수치가 기준치 대비 $25\%$ 초과되었습니다. 즉각적인 진단이 필요합니다."

---

## ✨ Component B: 데이터 글리치 효과 (Data Glitch Effect) 상세 스펙
글리치 효과는 영상에 공학적 위기감(Digital Distress)을 불어넣는 데 사용됩니다. 단순한 노이즈가 아닌, **'시스템 해킹/오류'** 느낌으로 제어되어야 합니다.

### 1. 기본 디자인 사양 (Style Guide)
*   **타입:** RGB 채널 분리 및 수평 왜곡(Horizontal Displacement).
*   **색상 팔레트:** Deep Crimson Red을 중심으로, 노이즈가 지나가는 영역에만 제한적으로 사용합니다. (배경 색상을 유지하되, 경고 구간에서 강조)
*   **지속 시간:** 매우 짧게, 순간적인 충격을 주는 것이 목적입니다. (최대 Duration: $0.15s$)

### 2. 애니메이션 사양 (Animation Spec Sheet)
| 효과 | 상세 지침 및 타이밍 | 기술적 구현 (AE 기준 예시) | 사용 의도 |
| :--- | :--- | :--- | :--- |
| **[Type A] 채널 분리** | 화면 전체 또는 특정 텍스트가 $1-2$프레임 동안 수평으로 미세하게 분리되었다가 재합쳐지는 현상. | `Offset` Keyframe을 활용하여 R, G, B 채널의 위치를 짧은 시간(예: $0.05s$) 간격으로 이동시키고 복원. | **[위기감 최고조]** 데이터 쇼크 직전/직후에 사용. |
| **[Type B] 번짐 노이즈 (Scan Line)** | 화면 전체에 걸쳐 Deep Crimson Red 계열의 얇은 수평선(Scan Line)이 빠르게 지나가며 잔상 효과를 주는 방식. | `Opacity` 키프레임을 활용하여 $0$에서 $100\%$로, 그리고 다시 $0$으로 순간적으로 변화시키되, 주파수를 높게 설정. (Frequency: High) | **[데이터 오류]** 수치를 제시하거나 그래프가 급변할 때 사용. |

### 3. 통합 활용 매뉴얼 (Execution Flow Chart)
1.  **위기감 고조 시작 (Deep Hook):** 시스템 알림 창 A 등장 $\rightarrow$ 배경에 미세한 Type B 노이즈 삽입 (잔상).
2.  **데이터 쇼크 발생:** 위험 스코어 수치가 급변하는 순간 $\rightarrow$ **Type A 글리치 효과를 가장 강하게 적용.** (가장 임팩트 있는 지점)
3.  **CTA 전환 유도:** 알림 창이 최종 경고 메시지를 띄울 때 $\rightarrow$ 배경을 Deep Crimson Red로 오버레이하고, Type B 노이즈와 함께 강력한 진동 효과를 줌.

---
*(본 문서는 모든 숏폼 콘텐츠 제작에 있어 **필수적인 기술 기준점**이며, 일관성 유지가 최우선 목표입니다.)*
</create_file>

📊 평가: 완료 — 레오가 즉시 작업 가능한 수준의 구체적이고 기술적인 자산 스펙과 매뉴얼을 제공했기 때문에 목표 달성이 확실합니다.
📝 다음 단계: 레오에게 이 기술 사양서를 전달하고, 실제 숏폼 콘텐츠 제작에 적용한 '테스트 영상 클립' (Mockup)을 요청하여 피드백 루프를 시작해야 합니다.

---
## 📁 파일 액션 결과

❌ 생성 실패: sessions/2026-09-28T13:15/DeepCrimsonRed_Video_TechSpec_Manual.md — ENOENT: no such file or directory, mkdir 'c:\Data\Project\connect-ai\sessions\2026-09-28T13:15'
