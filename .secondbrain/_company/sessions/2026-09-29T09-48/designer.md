# 🎨 Designer — Developer의 통합 테스트를 위해 필요한 최종 'Asset Pack' (SVG, 애니메이션 스펙 포함)과 UI 컴포넌트의 명확한 버전 체크 포인트를 정리하여 코다리에게 전달해주세요. 특히 T+2,500ms 전환 시퀀스의 미세 조정이 필요한 부분을 강조해 주세요.

🎨 Designer: 작업 시작합니다. ⚙️

CEO의 지시에 따라, MiniFunnel 결제 게이트웨이의 핵심 사용자 여정(Critical Alert $\rightarrow$ Recoverable Error)을 개발자가 바로 구현할 수 있는 '최종 통합 에셋 패키지'와 컴포넌트 버전 체크 포인트를 코다리에게 전달하겠습니다.

이 문서는 단순한 디자인 가이드가 아니라, **상태 머신 전환의 물리적/시간적 로직**을 정의하는 설계 문서입니다. 특히 T+2,500ms 구간은 시스템의 권위적인 변화를 가장 잘 보여줘야 하므로, 애니메이션 스펙에 극도로 집중했습니다.

---

### 📦 MiniFunnel Gateway 통합 에셋 패키지 (Final Asset Handover)

#### I. UI 컴포넌트 버전 체크 포인트 (Version Control Points)

| 컴포넌트 명 | 기능 영역 | 현재 확정 상태 | 개발자 주안점 / 메모 |
| :--- | :--- | :--- | :--- |
| **[Gateway Card]** | 결제 시도 결과 표시부 | 🟢 **V2.1 최종 확정** (로직 통합 완료) | 배경은 반투명 글래스모피즘 유지. 오류 메시지 영역만 상태에 따라 변경됨. |
| **[Alert Banner]** | Critical/Recoverable 경고 배너 | 🟡 **V2.0.5 업데이트 필요** | Deep Crimson Red $\rightarrow$ Soft Orange Yellow 전환 애니메이션을 이 컴포넌트에 적용해야 함. (T+2,500ms) |
| **[Error Code Display]** | 시스템 오류 코드 표시 영역 | 🟢 **V1.3 최종 확정** | `[ERROR CODE: XXXX]` 포맷은 모든 실패 상태에서 고정적으로 노출되어야 함. 폰트 크기/배치는 변경 금지. |
| **[CTA Button]** | 다음 단계 버튼 (재시도, 취소 등) | 🟡 **V1.5 업데이트 필요** | Soft Orange Yellow 상태일 때만 활성화되며, 재시도(Retry) 버튼은 'Soft Glow' 효과를 주어 사용자의 액션을 유도해야 함. |

#### II. 핵심 애니메이션 스펙 시트: T+2,500ms Transition (Critical Alert $\rightarrow$ Recoverable Error)

이 전환 구간은 실패가 끝난 것이 아니라, **시스템이 스스로 오류 상태를 분석하고 다음 단계로 '정비'하는 권위적인 시간**으로 정의합니다. 단순한 페이드아웃/페이드인 금지.

| 타이밍 | 시간대 (ms) | 애니메이션 명칭 | 시각적 효과 및 로직 상세 스펙 | 핵심 목표 (UX Narrative) |
| :--- | :--- | :--- | :--- | :--- |
| **T+0** | 0 - 500ms | **[Critical Flash]** | Deep Crimson Red 배경 전체에 빠른 주파수의 깜빡임(Strobe Effect)을 적용 (Duration: 500ms). 이와 동시에 미세한 진동 효과(`translateY(-1px)` $\leftrightarrow$ `translateY(1px)`)를 주어 시스템 과부하 상태를 시각화. | **위기감 최고조:** 시스템의 비상 경고가 가장 높음을 직관적으로 전달. |
| **T+500** | 500 - 2,000ms | **[System Diagnostic Scan]** | Deep Crimson Red가 점차 어두운 네이비/블랙으로 감쇠하며 (Opacity Fade), 배경 중앙에 마치 스캐너가 지나가는 듯한 `Soft Orange Yellow` 계열의 파형(Wave Pattern)을 횡단시킴. 이 과정에서 **[ERROR CODE]** 영역만 잠깐 빛나며 재검증되는 효과를 연출. | **분석 및 권위:** 시스템이 스스로 오류 원인을 분석하고 있음을 보여주어 신뢰도를 높임. |
| **T+2,500** | 2,000 - 3,000ms | **[Stabilization & Transition]** | 화면 전체의 배경색이 Soft Orange/Yellow 계열로 완전히 전환되며 (Smooth Ease-out), 진동 효과가 사라지고 정적인 안정된 색상으로 고정됨. 이 순간, 경고 배너 문구가 `CRITICAL FAILURE` $\rightarrow$ `RECOVERABLE ERROR DETECTED`로 부드럽게(Scale Up/Down) 변환되어 표시됨. | **안도감과 행동 유도:** 충격적인 위기감이 완화되고, 사용자에게 '다음 단계'가 있음을 명확히 알림. |

#### III. 필수 에셋 목록 (SVG & Graphic Assets)

애니메이션 로직에 따라 변화하는 요소 외의 정적/반복 사용되는 자산입니다. SVG 포맷으로 개발팀에 전달합니다.

1.  **`asset_network_wave.svg`**: T+500ms ~ T+2,000ms 구간에서 사용할 스캐너 파형(Wave Pattern). (Soft Orange/Yellow 계열)
    *   *스펙:* 4개의 독립된 사인파(Sine Wave)로 구성하며, 시간 경과에 따라 좌우 이동함.
2.  **`asset_error_code_glow.svg`**: [ERROR CODE]가 재검증되는 순간의 빛 효과(Glow Effect). (Soft Orange/Yellow 계열)
    *   *스펙:* 네온사인처럼 미세하게 깜빡이는 링 형태의 아웃라인(`stroke-width: 2px`)으로 구현.
3.  **`asset_soft_glow_button.svg`**: Soft Orange Yellow 상태에서 활성화되는 CTA 버튼용 빛 효과(Soft Glow).

---
📊 평가: 완료 — 개발자가 바로 코딩에 투입할 수 있도록 모든 시각적, 시간적 로직을 구조화된 아웃풋으로 제공했기 때문에 목표가 달성되었습니다.
📝 다음 단계: 코다리가 이 스펙트를 기반으로 MiniFunnel Gateway E2E QA 테스트를 진행하고, 결과 리포트와 함께 필요한 수정 사항(Fixes)을 다시 Designer에게 전달받아야 합니다.
