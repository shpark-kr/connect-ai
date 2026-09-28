# 🎨 Designer — Deep Crimson Red 시스템 경고 UI와 글리치 효과를 활용한 'Instagram Reels 전용 템플릿 패키지 V3.0'을 최종 구현하세요. 이 버전은 모바일 환경에 최적화되어야 하며, 사용자가 즉시 문구(Placeholder)만 변경하여 사용할 수 있도록 Figma 또는 PSD 기반으로 제공되어야 합니다. (필수 포함 요소: 위험 스코어 표시 영역, 공학적 경고 메시지 프레임, Mini-App CTA 버튼 표준 모듈)

🎨 Designer: 작업 시작합니다. CEO 지시에 따라 'Instagram Reels 전용 템플릿 패키지 V3.0'의 최종 디자인 시스템 스펙을 작성합니다. 이전 버전에서 부족했던 모바일 최적화와 즉시 사용 가능성을 극대화하는 데 중점을 두었습니다. 이 산출물은 Figma/PSD 빌더가 참조할 수 있는 '최종 실행 가이드(Final Execution Guide)' 역할을 합니다.

이 작업의 목표는 **'Deep Crimson Red 시스템 경고'라는 공학적 위기감**을 통해 시청자가 콘텐츠를 끝까지 보도록 유도하고, 마지막 3초에 Mini-App CTA 버튼으로 자연스럽게 몰입시키는 것입니다.

---

### 💾 최종 산출물: `sessions/2026-09-28T10-00/Instagram_Reels_Template_Kit_V3.0.md`

**파일명:** Instagram Reels Template Kit V3.0 - Final Specification
**사용 포맷:** Figma (또는 Adobe XD) 기반, After Effects 애니메이션 가이드 포함
**비율:** 9:16 (1080px x 1920px)
**톤앤매너:** 공학적 위협감 (Techno-Alarm), Deep Crimson Red, 글리치/데이터 스캔 효과

#### 1. 전체 레이아웃 및 컴포넌트 구조 (The Anatomy)

템플릿은 **[A] 후크 영역 $\rightarrow$ [B] 문제 제기/데이터 쇼크 $\rightarrow$ [C] 솔루션 제시 & CTA**의 3단계 Funnel에 맞춰 세 가지 주요 섹션으로 분할됩니다. 각 섹션별로 레이아웃을 고정합니다.

| 요소 | 위치 및 크기 (Pixel) | 목적 | 필수 적용 효과 |
| :--- | :--- | :--- | :--- |
| **배경 그리드** | 1080x1920 전체 | 통일감 유지 | 미세한 데이터 스캔라인(Opacity: 5%) 오버레이. |
| **헤더 (A)** | 상단 30% (약 600px) | 시선 강탈, 문제 정의 | 타이포그래피 글리치 애니메이션 필수. |
| **메인 콘텐츠/데이터 (B)** | 중단 45% (약 900px) | 신뢰성 확보, 위협감 극대화 | 경고창(Warning Box), 데이터 스코어 모듈 삽입. |
| **CTA & 결론 (C)** | 하단 25% (약 500px) | 전환 유도 (Call to Action) | 가장 강렬한 Deep Crimson Red 배경, 시스템 오류 메시지 활용. |

#### 2. 핵심 컬러 팔레트 및 타이포그래피 가이드

| 요소 | HEX 코드 | 역할/적용 방식 | 비고 |
| :--- | :--- | :--- | :--- |
| **Deep Crimson Red (Primary)** | `#8B0000` | 경고, 임팩트, CTA 배경. 가장 중요한 시각적 자극제. | 글리치 및 시스템 오류 프레임에 사용. |
| **Dark Slate Blue (Secondary)** | `#1F2A37` | 메인 배경색 (다크 모드). 전문성/안정감 부여. | 전체 화면의 기본 컬러. |
| **Accent Teal/Cyan** | `#00FFFF` | 데이터 포인트 강조, 시스템 메시지(텍스트). 기술적 느낌 극대화. | 경고문 텍스트 또는 그래프 선 색상으로 제한 사용. |
| **White/Light Gray** | `#FFFFFF`/`#CCCCCC` | 본문 가독성 확보용 (Placeholder 텍스트). | 주된 내용은 절대로 순백색을 쓰지 말 것. |

**폰트 계층:**
1.  **Headline/Warning Text:** `Mono` (Monospace, 예: SF Mono 또는 시스템 글꼴) — 공학적, 데이터 느낌 강조.
2.  **Body Text:** `Noto Sans KR` (Semi-Bold 이상 권장) — 가독성이 높은 본문용.

#### 3. 필수 컴포넌트 상세 스펙 및 애니메이션 지침

##### 🔴 Component A: 위험 스코어 표시 모듈 (The Risk Score Gauge)
*   **위치:** 섹션 B 중앙 좌측 또는 우측 상단 고정 위치.
*   **구조:** 'Risk Score:' 레이블(Accent Teal) $\rightarrow$ 숫자 값 Placeholder (Mono, 4자리) $\rightarrow$ 게이지 바/미터기 형태의 시각화 요소.
*   **애니메이션 지침:**
    1.  **Load-in:** 스코어 숫자가 깜빡이며 카운트업(0부터 시작하여 목표 수치까지 빠르게 도달).
    2.  **Danger State:** 만약 점수가 높을 경우 (예: 75점 이상), 게이지 바 전체가 **Deep Crimson Red**로 즉시 변하고, 주변에 `[WARNING]` 배지가 깜빡이며 나타나야 함.

##### ⚠️ Component B: 공학적 경고 메시지 프레임 (The Glitch Box)
*   **위치:** 섹션 A/B 경계면 또는 내용 전환 시점.
*   **구조:** 직사각형 박스 형태. 배경은 Deep Crimson Red와 Dark Slate Blue의 반투명 그라데이션 조합.
*   **Placeholder 텍스트:** `[SYSTEM ALERT: 생체 데이터 오류 감지]` / `[[CRITICAL WARNING LEVEL]]`
*   **애니메이션 지침 (필수):**
    1.  **진입:** 화면 전체에 걸쳐 **글리치(Glitch)** 효과와 함께 나타나야 합니다. (색상 분산, 수평 노이즈/디스토션 발생 후 원래 이미지로 복구).
    2.  **지속:** 경고 메시지가 표시되는 동안 1~2초 간격으로 미세한 `[ERROR]` 코드가 배경에 랜덤하게 흘러내리는 효과를 유지합니다.

##### 🚀 Component C: Mini-App CTA 버튼 모듈 (The Conversion Point)
*   **위치:** 섹션 C 중앙, 화면의 시선이 가장 많이 머무는 곳.
*   **버튼 스펙:** 너비 70% / 높이 80px. 배경색은 **Deep Crimson Red**.
*   **Placeholder Text:** `[지금 내 몸의 위험 스코어 점검하기]` (폰트: Mono, 볼드)
*   **애니메이션 지침 (최고 중요):**
    1.  CTA가 화면에 나타나기 0.5초 전부터 배경이 빠르게 깜빡이는(Flashing/Strobe Effect) 경고 효과를 주어 긴장감을 최고조로 만듭니다.
    2.  버튼을 누르는 시늉(Press Down)의 트랜지션과 함께, 버튼 주변에 **[SYSTEM CONNECTION ESTABLISHED]**와 같은 성공 신호가 짧게 번쩍이며 애니메이션이 종료되어야 합니다.

#### 4. 최종 제작 체크리스트 (To be used by Editor/Designer)
1.  ✅ 모든 Placeholder 텍스트는 `{{Placeholder_Text}}` 형식으로 통일하여 관리한다.
2.  ✅ Deep Crimson Red의 사용은 **오직 위기감과 CTA에 국한**하고, 다른 곳에는 최소화하여 임팩트를 유지한다.
3.  ✅ 전체 영상은 빠른 컷 전환(Jump Cut)을 사용하여 지루할 틈이 없게 연출해야 한다 (평균 1~2초 이내의 시각 정보 변화).

---
📊 평가: 완료 — CEO가 요구한 모든 필수 요소와 모바일 최적화, 공학적 위기감 요소를 포함하는 V3.0 최종 스펙을 구체적인 디자인 시스템 가이드 형태로 구현했습니다.
📝 다음 단계: 레오(영상 편집자)에게 이 최종 실행 기술 매뉴얼을 전달하고, 실제 애니메이션 테스트를 시작해야 합니다.
