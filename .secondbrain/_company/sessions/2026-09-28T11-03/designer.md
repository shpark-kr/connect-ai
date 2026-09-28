# 🎨 Designer — Researcher가 제시한 HOMA-IR Index, ASMI 등 과학 기반 위험 지표를 직관적으로 보여줄 수 있는 '시스템 알림창(System Alert UI)' 컴포넌트 디자인을 완성하세요. 이 컴포넌트는 Deep Crimson Red 경고 톤앤매너와 글리치 효과를 기본으로 하며, 측정 가능한 데이터 그래프(예: 정상 범위 vs 위험 스코어)가 삽입 가능하도록 모바일 최적화된 Figma 파일로 제공되어야 합니다. CTA 직전에 최대의 위기감을 줄 수 있는 '임계점 도달' 시각 연출 요소를 반드시 포함하세요.

🎨 Designer: 작업 시작합니다.

CEO 지시사항은 현재 모든 콘텐츠 제작의 핵심 전제이자, 가장 시급하고 가치가 높은 단일 작업입니다. 이 '시스템 알림창(System Alert UI)' 컴포넌트가 완성되어야만 Writer와 레오 에이전트가 다음 단계로 나아갈 수 있습니다.

저는 디자인 시스템을 담당하는 Lead Designer로서, 단순히 이미지를 만드는 것을 넘어, **'공학적 위기감(Engineered Urgency)'** 이라는 브랜드의 핵심 감정을 담은 재사용 가능한 모듈화된 컴포넌트를 제작하겠습니다.

제작할 산출물은 Figma 파일 그 자체를 직접 제공하기 어렵기 때문에, 해당 디자인 시스템을 완벽하게 구현하고 개발팀이 즉시 사용할 수 있도록 **디자인 스펙 및 구조 정의서 (Tech Spec)** 파일을 생성하는 방식으로 접근하겠습니다. 이 파일에는 색상 코드, 레이아웃 좌표(Grid System), 애니메이션 로직까지 포함됩니다.

### 🛠️ 산출물: 시스템 알림창 컴포넌트 설계 명세 (System Alert UI Tech Spec)

다음 경로에 Figma 기반의 기술 사양서와 디자인 시스템 가이드를 생성합니다.

<create_file path="sessions/2026-09-28T11-30/Designer_Asset_Guide_V4.0_SystemAlertUI.md"># 🚨 온현(Onhyun) - Critical Alert System UI Component V4.0 (Figma Tech Spec)

## 📌 개요 및 목적
본 컴포넌트는 시청자에게 과학적, 공학적 위협을 즉각적으로 인지시키는 인터페이스입니다. HOMA-IR Index 등 생체 지표를 측정 가능한 수치로 제시하며, Mini-App 진단 유도 직전 CTA 영역에서 위기감(Urgency)을 극대화하는 것이 주 목적입니다.

**톤앤매너:** Deep Crimson Red (DCR), 글리치/시스템 에러 효과, 다크 모드 기반의 공학적 경고.
**최적 해상도:** 1080x1920 (모바일 세로 비율)
**재사용성:** 모든 콘텐츠 제작 시 표준 컴포넌트로 활용되어야 합니다.

---

## 📐 시스템 구조 정의 및 그리드 (Grid System)
*   **컨테이너 크기:** 1080px(W) x 1920px(H)
*   **그리드 설정:** 12컬럼 시스템 (Column Grid, 100px 간격)을 기반으로 모든 요소를 배치하여 모듈화합니다.

## 🎨 컬러 팔레트 및 타이포그래피
### 1. 핵심 색상 코드
| 역할 | 이름 | HEX Code | 용도 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **배경 (Default)** | Deep Dark Gray | `#0A0F13` | 기본 배경색 (어두운 밤하늘 느낌) | 위기감 유지에 최적화된 무채색 |
| **Primary Alert** | Deep Crimson Red | `#B72429` | 경고 메시지, 임계점 표시, CTA 버튼 | 브랜드 핵심 경고 톤앤매너 (DCR) |
| **Secondary Warning** | Amber Failure | `#FFC300` | 경계선, 점멸 효과, 데이터 플래그 | 위험도 상승 직전의 시각적 불안정성 표현 |
| **Normal/Safe Zone** | Muted Teal | `#4A90E2` | 정상 범위 표시, 기준점 그래프 라인 | 심리적 안정감을 주기 위한 대비 색상 (Min.) |
| **텍스트 (Primary)** | Light Gray | `#DDE3EB` | 본문 텍스트, 레이블 | 높은 가독성 확보 |

### 2. 타이포그래피
*   **폰트:** Pretendard 또는 Inter (시스템 고딕체 사용 권장)
*   **스타일:** Sans-serif 계열의 모던하고 기계적인 느낌을 주는 서체를 채택합니다.
*   **강조:** 위험 스코어 수치는 Bold 900, 크기 72pt 이상으로 매우 크게 배치하여 공학적 데이터가 화면을 지배한다는 느낌을 줘야 합니다.

---

## ⚙️ 컴포넌트 상세 설계 (Component Breakdown)

### 1. [CORE] 위험 스코어 게이지 (Risk Score Gauge Module)
*   **기능:** 현재 측정된 수치(HOMA-IR 등)를 시각화하여 즉각적인 위협감을 전달합니다.
*   **구조:** 가로형 원형 또는 막대 그래프 형태의 게이지를 사용합니다.
*   **상태별 변화 (필수 로직):**
    1.  **Safe State (녹색/파랑 영역):** 게이지가 Muted Teal 라인 내에 머무름.
    2.  **Pre-Alert State (노란색/앰버 영역):** 데이터가 Amber Failure 구간 진입 시, 게이지 주변에 미세한 노이즈(Noise)와 깜빡임(Flicker) 효과를 추가합니다.
    3.  **Critical State (빨간색/DCR 영역):** 임계점 도달 시, **게이지 전체가 DCR로 오버레이되며 글리치 애니메이션이 최대화됩니다.** 수치 주변에 'SYSTEM FAILURE' 등의 경고 텍스트가 깜빡입니다.

### 2. [MODULE] 시스템 알림창 (System Alert Panel)
*   **배치:** 화면 상단 또는 하단을 가로지르는 고정 UI 영역으로 구현합니다.
*   **내용:** `[🚨 CRITICAL WARNING: HOMA-IR INDEX]` 와 같이 공학적/시스템적인 톤의 헤드라인을 사용합니다.
*   **애니메이션:** 진입 시 글리치(Glitch) 효과와 함께 나타나야 하며, 경고 메시지가 변경될 때마다 시스템 에러 사운드와 함께 패널이 순간적으로 흔들리는(Jitter/Shake) 효과를 적용하여 생동감을 부여합니다.

### 3. [CLI] 임계점 도달 시각 연출 (Threshold Reached Visualizer - The Climax)
*   **발생 타이밍:** Mini-App CTA 버튼 직전, 영상 시간 기준으로 **최소 5초간의 집중 배치.**
*   **효과:** 단순한 빨간색 경고를 넘어선 '시스템 강제 종료' 느낌을 연출합니다.
    1.  화면 전체가 DCR 색상의 노이즈와 함께 순간적으로 왜곡(Distortion)됩니다.
    2.  HOMA-IR 수치 옆에 **`[ERROR: THRESHOLD EXCEEDED]`** 라는 메시지가 반복적으로, 그리고 크고 강력하게 플래싱 됩니다.
    3.  배경 이미지/영상은 일시적으로 깨진 데이터 스트림(Data Stream Glitch)처럼 처리되며, 청각적 요소와 결합하여 심리적 압박을 최대화합니다.

---

## 📝 개발 및 구현 가이드라인 (Developer Notes)
*   **Interactivity:** 모든 컴포넌트는 React/Vue 기반의 상태 변화(State Change)에 따라 애니메이션이 트리거되도록 설계해야 합니다. (예: `isCritical: true` → DCR + Glitch On).
*   **Responsiveness:** 16:9 비율의 유튜브 콘텐츠에도 활용 가능하도록, 그리드 시스템을 통해 좌우 여백을 조절할 수 있는 유연성을 확보합니다.

</create_file>

### ✨ 주요 결과물 요약 및 의미
본 'System Alert UI Tech Spec'은 향후 모든 콘텐츠 제작에 필요한 **디자인의 언어(Language of Design)** 그 자체를 확립했습니다. 이는 단순히 템플릿을 제공하는 것을 넘어, 위기감을 조성하는 방식과 시각적 규칙까지 정의한 것이므로, 다음 단계 에이전트들이 이 가이드라인 내에서만 움직일 수 있도록 강력하게 제어합니다.

---
📊 평가: 완료 — CEO 지시사항에 맞춰 모든 콘텐츠 제작의 기반이 되는 핵심 시스템 UI 컴포넌트를 기술 사양서 형태로 완성했습니다.
📝 다음 단계: Writer에게 이 'System Alert UI Tech Spec'을 전달하여, 숏폼 스크립트 내의 **위험 스코어 제시 구간**과 **Mini-App CTA 직전 5초**에 정확히 매핑할 수 있도록 시간대별(Timecode) 디테일한 연출 지문 업데이트를 요청해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\sessions\2026-09-28T11-30\Designer_Asset_Guide_V4.0_SystemAlertUI.md
