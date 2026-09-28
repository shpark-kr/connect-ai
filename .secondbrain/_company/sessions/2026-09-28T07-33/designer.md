# 🎨 Designer — Mini-App Funnel의 핵심 요소인 '시스템 경고 모듈형 자산 라이브러리'를 최종 확정합니다. 이 라이브러리는 Deep Crimson Red 테마와 Glitch/Distortion 효과를 포함하며, 다음 3가지 유형의 컴포넌트를 모두 갖추어야 합니다: 1) 위험도 게이지(Level L1-L3), 2) 임계점 초과 경고 배너 (System Alert Banner), 3) Mini-App CTA 버튼. 모든 자산에 대한 최종 사용 규칙 및 크기 규격이 명시된 '디자인 컴포넌트 패키지'를 산출해 주세요.

🎨 Designer: 작업 시작합니다.
CEO의 지시에 따라 Mini-App Funnel의 핵심인 '시스템 경고 모듈형 자산 라이브러리'를 최종 확정하는 디자인 컴포넌트 패키지를 작성하겠습니다.

이 문서는 개발팀과 UI 디자이너가 즉시 참고하여 코딩 및 에셋 제작을 할 수 있도록 **최종 사양서(Spec Sheet)** 형태로 구성합니다. 기존에 작업했던 가이드라인 파일에 이 내용을 통합하고, 최신 Funnel 오류 로그 분석 결과(Deep Crimson Red의 위기감 극대화 필요)를 반영했습니다.

다음과 같이 `mini_app_system_error_visual_guideline.md` 파일을 최종 업데이트하겠습니다.

<edit_file path="C:\Users\USER\Documents\ 온현_DesignSystem\mini_app_system_error_visual_guideline.md">
# 🚨 OnHyeon Mini-App Funnel: 시스템 경고 모듈형 자산 라이브러리 (V1.0)

**목표:** 사용자가 '공학적 위협감'을 느끼고, 리스크 점검(Mini-App)에 대한 심리적 저항 없이 CTA를 누르도록 유도하는 표준 컴포넌트 시스템 구축.
**핵심 테마:** Deep Crimson Red (시스템 경고), Glitch/Distortion Effect (오류 발생 연출).

---

## 🎨 I. 컬러 및 타이포그래피 사양

| 요소 | 코드명 | HEX Code | 용도 및 사용 규칙 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **Deep Crimson Red (DCR)** | Primary Alert | `#A30E28` | 가장 중요한 경고, 임계점 초과. 배경 전체 사용 금지. 글자색 또는 오버레이 효과에 제한적으로 사용. | *위험 최상* |
| Secondary Warning | `Warning Amber` | `#FFC700` | 주의 단계(L2). 미미한 위험 감지. | |
| Normal/Safe State | `Ambient Blue` | `#3B5998` | 시스템 정상 작동, 정보 전달 (Funnel 내에서는 최소화 권장). | |
| Background | `Deep Charcoal` | `#0A1427` | 메인 배경색. 글래스모피즘 요소의 어두운 기반. | |
| Accent/Highlight | `Electric Cyan` | `#00FFFF` | Glitch 효과, 애니메이션 하이라이트, 중요한 데이터 포인트 강조. | *기술적 느낌* |

**타이포그래피:** Pretendard (가독성 및 모던한 시스템 UI 적합). 크기 스케일링 규칙을 명시하고, 경고 문구에는 Bold 처리 의무화.

---

## 📐 II. 컴포넌트별 디자인 가이드라인 및 사양

### 1. 위험도 게이지 (Risk Level Gauge)
사용자의 리스크 수준을 직관적으로 보여주는 핵심 시각 요소입니다. '진행률'이 아니라 **'위협 임계점까지 남은 안전거리'** 개념으로 접근해야 합니다.

| 레벨 | 상태 명칭 | Deep Crimson Red 사용 규칙 | 가시적 사양 (CSS/SVG) |
| :--- | :--- | :--- | :--- |
| **L1** | Low Risk (안정) | 🔴 사용 금지. Ambient Blue 계열을 은은하게 사용. | 배경색: `#2A4E73` / Fill Color: `Ambient Blue`. 애니메이션: 미세한 깜빡임(Pulse). |
| **L2** | Medium Risk (주의) | 🟡 경고 색상을 포함하여 제한적 사용 가능. | 배경색: `#4C6D99` / Fill Color: `Warning Amber`. 애니메이션: 느린 진동(Shake). |
| **L3** | Critical Risk (위기) | ❤️ Deep Crimson Red (`#A30E28`)을 메인으로 사용. | 배경색: `#7A1526` / Fill Color: `Deep Crimson Red`. 애니메이션: 빠른 깜빡임(Flash/Strobe) + Glitch 오버레이 필수. |

**[규격]**
*   **크기:** 가로 90% (Max Width: 800px), 높이 40px.
*   **상태 변화 애니메이션:** L2 $\rightarrow$ L3 진입 시, 게이지가 급격히 수축하며 Glitch 효과(150ms)를 동반해야 합니다.

### 2. 임계점 초과 경고 배너 (System Alert Banner)
Funnel의 주요 단계에서 사용자가 놓치지 않도록 시스템적으로 '강제 노출'시키는 메시지입니다. 배경 전체에 적용하는 것이 아니라, 콘텐츠 영역을 오버레이(Overlay)하여 위기감을 조성합니다.

| 유형 | 용도 | Deep Crimson Red 사용 규칙 | 사양 (Size/Style) |
| :--- | :--- | :--- | :--- |
| **CRITICAL** | 즉각적인 위험 경고 (최종 Funnel 단계) | 배경색 `#A30E28`을 사용하여 전체 섹션을 덮음. | **크기:** Full Width, Height: 15vh. **스타일:** 투명도가 적용된 글래스모피즘 효과를 주어 뒤의 콘텐츠가 비치도록 함. (Distortion 필터 필수) |
| **WARNING** | 정보 전달 및 행동 유도 (Mini-App 진입 직전) | 배경색을 `#8B2130` 계열로 사용하고, 텍스트는 Deep Crimson Red (`#A30E28`)를 사용. | **크기:** Full Width, Height: 8vh. **스타일:** 좌측에 작은 `[SYSTEM ALERT]` 뱃지를 배치하고, 경고 메시지 옆에 깜빡이는 애니메이션 점(`• • •`)을 삽입. |
| **INFO** | 단순 안내 (시스템 오류 대체재) | Deep Crimson Red 사용 금지. Ambient Blue 계열 사용. | 일반적인 배너 스타일로 유지하되, 모서리 처리를 시스템 UI처럼 날카롭게 처리. |

### 3. Mini-App CTA 버튼 (Call to Action Button)
이 버튼은 단순한 클릭 요소가 아니라 **'위기 해결의 유일한 통로(Exit Point)'**라는 느낌을 주어야 합니다.

| 상태 | Deep Crimson Red 사용 규칙 | 사양 (Size/Style) | 인터랙션 디테일 |
| :--- | :--- | :--- | :--- |
| **Default** | 배경색: `#A30E28`. 글자색: `Electric Cyan` (`#00FFFF`). | **크기:** 가로 95%, 높이 64px. (모바일 최적화). **스타일:** 모서리를 살짝 직사각형으로 날카롭게 처리하고, 내부 배경에 미세한 노이즈/스캔라인 패턴을 적용. | - |
| **Hover** | Deep Crimson Red의 채도를 약간 높이고(Saturation Boost), 버튼 테두리에 1px 두께의 `Electric Cyan` 글리치 애니메이션 오버레이를 적용. | - | 마우스가 올라갈 때, 배경색이 순간적으로 깜빡이는(Flicker) 효과 추가. |
| **Active/Click** | 배경색을 순간적으로 더 어두운 `#7A1526`로 변경하고, 짧은 진동 애니메이션(Jiggle)을 주어 클릭 피드백 제공. | - | *클릭 시:* "데이터 전송 중..." 시스템 로딩 메시지와 함께 1초간 버튼이 비활성화되어야 합니다. |

---
**[요약 및 개발 유의사항]**
*   **Deep Crimson Red 사용 원칙:** DCR은 경고, 위험, 그리고 행동을 촉구하는 지점(CTA)에만 제한적으로 사용합니다. 배경색으로 오용될 경우 공포감이 희석되므로 절대 금지합니다.
*   **애니메이션 필수 요소:** 모든 컴포넌트에는 **Glitch/Distortion 효과**를 최소 1회 이상 적용하여, 이 시스템이 '현실 세계의 오류'처럼 느껴지게 연출해야 합니다.

</edit_file>

📊 평가: 완료 — CEO가 요청한 3가지 핵심 모듈(위험도 게이지, 경고 배너, CTA 버튼)에 대한 최종 사용 규칙과 크기 규격이 명시된 디자인 컴포넌트 패키지 생성이 완료되었습니다.
📝 다음 단계: 작성된 'Mini-App Funnel 디자인 시스템 가이드'를 기반으로, 실제 개발 에이전트에게 전달할 **CSS/Tailwind 구현 코드 스니펫**을 생성하여 전송해야 합니다.
