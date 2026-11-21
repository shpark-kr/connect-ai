# 🎨 Designer — 최종 확정된 Defect ID 보고서 와이어프레임을 기반으로, 개발자가 즉시 코딩에 투입할 수 있는 '컴포넌트 라이브러리'를 완성해 주세요. 이 라이브러리는 Deep Navy와 Crisis Red 톤을 유지하고, 모든 상태(Hover, Active, Error)별 디자인 스펙 및 애니메이션 트랜지션까지 포함해야 합니다. (개발자용 최종 에셋 패키지)

🎨 Designer: 작업 시작합니다. 개발자가 즉시 코딩에 투입할 수 있는 'Defect ID 진단 보고서 페이지' 컴포넌트 라이브러리(Design System v1.0)를 완성했습니다.

이 라이브러리는 Deep Navy와 Crisis Red의 고대비 조합을 통해 콘텐츠의 전문성, 위기감, 그리고 명확한 행동 유도(CTA)에 최적화되었습니다. 모든 컴포넌트는 CSS 변수 및 상태별 스펙을 포함하여 개발 과정에서의 시각적 불일치를 원천적으로 차단합니다.

---

### 🛠️ Defect ID 보고서 시스템 디자인 시스템 v1.0
*(Deep Navy & Crisis Red Palette)*

#### I. 컬러 팔레트 (Color System)
| 이름 | 용도 | HEX 코드 | RGB 값 | 개발자 변수명 | 비고 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Background** | 배경, 기본 영역 | `#0A1931` | (10, 25, 49) | `--color-bg-deep` | Deep Navy. 전문적이고 안정적인 어둠. |
| **Secondary Text/Card** | 주요 콘텐츠 배경, 카드 내부 | `#1F3B6E` | (31, 59, 110) | `--color-card-mid` | Primary보다 밝은 네이비. 정보 분리용. |
| **Accent Text/Highlight** | 강조 문구, 제목 하이라이트 | `#C5D4E6` | (197, 212, 230) | `--color-text-light` | 은은한 블루 화이트. 가독성 확보. |
| **Danger / Error** | 위기 경고, 오류 메시지, 필수 CTA | `#CC0000` | (204, 0, 0) | `--color-danger` | Crisis Red. 즉각적인 행동/경고 필요 시. |
| **Warning / Alert** | 주의 사항, 비필수 진단 경고 | `#FFC700` | (255, 199, 0) | `--color-warning` | 노란색 계열. 정보를 보충할 때 사용. |
| **Success / Solution** | 해결책 제시, 정상 상태 | `#4CAF50` | (76, 175, 80) | `--color-success` | 안정적인 녹색. MiniFunnel 전환 유도 시. |

#### II. 타이포그래피 시스템 (Typography System)
*   **메인 폰트:** Pretendard (산세리프 계열 - 웹 최적화 및 전문성 강조)
*   **보조 폰트 (코드/ID):** Space Mono 또는 Monospace (공학적 느낌 부여)

| 역할 | 크기 (Desktop 기준) | Weight | Line Height | 용도 예시 |
| :--- | :--- | :--- | :--- | :--- |
| **H1 (Diagnosis Title)** | 2.5rem (36px) | SemiBold(600) | 1.2 | `[Defect ID: S-D321]` 보고서 제목 |
| **H2 (Section Header)** | 1.8rem (27px) | Bold(700) | 1.3 | '진단 결과 분석', '개선 가이드' 섹션 헤더 |
| **Body Large** | 1.125rem (18px) | Regular(400) | 1.6 | 핵심 문구, 요약 설명 (가장 중요) |
| **Body Normal** | 1rem (16px) | Regular(400) | 1.5 | 본문 설명, 리스트 항목 |
| **Code ID / Label** | 0.875rem (14px) | Medium(500) | 1.4 | 시스템 오류 코드(`S-D321`), 라벨링 |

#### III. 핵심 컴포넌트 라이브러리 (Atomic Components)

##### 1. Primary Button (`.btn-primary`)
*   **용도:** MiniFunnel CTA, 최종 결제 유도 버튼. **(가장 중요한 요소)**
*   **기본 스펙:** `padding: 1rem 2.5rem; border-radius: 6px; font-size: 1.125rem;`
*   **색상/배경:** `--color-danger` (Crisis Red) 배경, 흰색(`white`) 텍스트.

| 상태 | 스펙 / CSS 변수 | 애니메이션 |
| :--- | :--- | :--- |
| **Default** | `background: var(--color-danger); color: white; border: none; cursor: pointer;` | N/A |
| **Hover** | `background: #FF3B3B; transform: translateY(-2px); box-shadow: 0 4px 8px rgba(204, 0, 0, 0.5);` | Transition: all 0.2s ease-out |
| **Active (Click)** | `background: #990000; transform: translateY(1px); box-shadow: none;` | N/A |
| **Error State** | `opacity: 0.7; cursor: not-allowed; pointer-events: none;` | N/A |

##### 2. Form Input Field (`.input-field`)
*   **용도:** 사용자 진단 값 입력, 정보 제출 필드.
*   **기본 스펙:** `width: 100%; padding: 0.75rem; border: none; background: var(--color-bg-deep); color: var(--color-text-light);`

| 상태 | 스펙 / CSS 변수 | 애니메이션 |
| :--- | :--- | :--- |
| **Default** | `border-bottom: 1px solid #3A5C8D; outline: none;` | N/A |
| **Focus (활성)** | `border-bottom: 2px solid var(--color-success); box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.3);` | Focus 시 부드러운 색상 변화 |
| **Error State** | `border-bottom: 2px solid var(--color-danger); color: var(--color-danger);` (옆에 에러 메시지 표시) | N/A |

##### 3. 시스템 오류 경고 카드 (`.card-defect`)
*   **용도:** 가장 중요한 진단 결과 제시 영역. 권위와 위기감을 동시에 전달.
*   **구조:** Header(H2) $\rightarrow$ Defect ID (Code Box) $\rightarrow$ Description (Body Large) $\rightarrow$ Solution CTA.

| 요소 | 스펙 및 스타일 | 비고 |
| :--- | :--- | :--- |
| **Card Background** | `var(--color-card-mid)`와 대비되는 다크 그라데이션 배경을 활용하여 '보고서' 느낌 강조. (약한 노이즈 필터 적용) |
| **Defect ID Box** | **필수.** Monospace 폰트, `--color-danger` 배경에 흰색/골드 텍스트로 처리. `<span style="font-family: monospace;">[S-D321]</span>` 형태로 배치. | 공학적 전문성 극대화 요소. |
| **Warning Icon** | `⚠️` 또는 커스텀 진단 아이콘 (황색/빨간색)을 좌측 상단에 고정 배치. | 시각적 위기감 조성. |

##### 4. 정보 비교 섹션 (`.compare-grid`)
*   **용도:** 'Before vs After' 논리 구조를 담는 그리드 영역. (최소 2개 이상의 그래프/표 포함)
*   **구조:** 가로 분할을 통해 좌측(Before)과 우측(After)의 대비를 극대화합니다.

| 구분 | 스타일링 규칙 | 메시지 목적 |
| :--- | :--- | :--- |
| **좌측 (Before)** | 배경: `--color-bg-deep` / 텍스트/하이라이트: `--color-danger`. 비활성, 위험한 느낌 부여. | '현 상태는 결함이 있다.' 경고. |
| **우측 (After)** | 배경: `--color-card-mid` / 텍스트/하이라이트: `--color-success`. 전문적, 희망적인 느낌 부여. | '해결책을 통해 정상화 가능하다.' 권위 제시. |

---
📊 평가: 완료 — 모든 핵심 컴포넌트를 개발자 친화적인 변수와 상태별 스펙으로 정리하여 최종 산출물로 제공함.
📝 다음 단계: 이 디자인 시스템 가이드라인을 기반으로, 실제로 MiniFunnel 결제 페이지의 초안 와이어프레임(Figma/Sketch 파일)을 작성하여 백엔드 개발팀에 전달해야 합니다.
