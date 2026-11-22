# 🎨 Designer — 코다리가 정의한 Data Contract (특히 애니메이션 로직 및 상태 변화에 따른 시각적 피드백)를 100% 반영하여, 'CriticalAlert UI'의 최종 개발용 디자인 에셋을 완성하십시오. 이는 단순 스케치가 아닌, CSS 변수와 React 컴포넌트 단위로 재현 가능한 Hi-Fi Mockup 형태여야 하며, Hero 섹션과 결합된 사용자 경험(UX) 흐름이 매끄럽게 보이도록 디자인해야 합니다.

🎨 Designer: 작업 시작합니다. CEO님의 지시를 최우선으로 반영하여, 지금까지의 모든 사양(API Spec V4.0 및 Data Contract)을 통합한 최종 개발용 디자인 에셋을 완성하겠습니다. 이 결과물은 단순 스케치가 아닌, 개발자가 즉시 React 컴포넌트와 CSS 변수를 통해 구현할 수 있도록 '디자인 토큰'과 '상태 변화 로직'이 결합된 Hi-Fi Mockup 명세서입니다.

이번 작업의 목표는 **Critical Alert UI**를 Hero 섹션에 통합하고, 사용자의 불안감(Panic)을 시간 경과에 따라 점진적으로 고조시키는 사용자 경험 흐름(UX Flow)을 정의하는 것입니다.

### 🛠️ 최종 산출물: CriticalAlert 컴포넌트 디자인 명세서 (Dev Ready)

다음 파일은 `CriticalAlert_Component_Def.md`로 생성되며, 이 파일을 개발팀에 전달하면 바로 코딩이 가능하도록 토큰 및 로직 레벨에서 완성됩니다.

<create_file path="C:\Users\USER\Design\CriticalAlert_Component_Def.md"># 🚨 Critical Alert Component Definition (V5.0 - Production Ready)

**[목표]**
*   사용자가 인지하는 재정적 리스크(The Gap)를 애니메이션과 시각적 위협을 통해 극대화한다.
*   Hero 섹션의 핵심 메시지 흐름에 맞춰, 낮은 긴급성 $\rightarrow$ 경고 $\rightarrow$ 임계점 도달로 이어지는 3단계 UX 전환을 구현한다.

**[기술 스택 가정]**
*   프레임워크: React (Component-based)
*   스타일링: CSS Variables & Tailwind CSS (최소한의 커스터마이징 필요)
*   애니메이션 로직: Framer Motion 또는 GSAP 기반, 상태(State)에 따라 속성 변경.

---

### 🎨 1. 디자인 토큰 및 컬러 팔레트 정의

| Token | Value | Description | Usage Context |
| :--- | :--- | :--- | :--- |
| `--color-primary` | `#FFD700` (골드) | 핵심 메시지, 액션 유도 (CTA). 전문성과 희망. | 그래프 라인, 강조 텍스트, 성공적 해결책 부분. |
| `--color-secondary` | `#192A56` (딥 네이비) | 배경색, 신뢰성 기반 색상. 공신력 부여. | 전체 배경, 헤더/푸터, 기본 UI 요소. |
| `--color-warning` | `#FF8C00` (진한 오렌지) | 주의 단계, 리스크 인지 시작점. | 중간 경고 메시지, 임계치 초과 직전의 데이터 변화. |
| `--color-danger` | `#B22222` (짙은 벽돌 레드) | **최종 공포/위기 상태**. 즉각적인 행동 요구. | Critical Alert 배경색, 애니메이션 최대값 도달 시. |
| `--font-family-main` | 'Noto Sans KR', serif | 헤드라인 및 강조 텍스트에 무게감 부여. | 제목 태그 (H1, H2). |
| `--font-size-alert` | 3rem / 5rem | 위험 수치를 시각적으로 압도하는 사이즈. | 애니메이션되는 핵심 숫자(Metric). |

---

### ⚛️ 2. CriticalAlert Component 구조 및 상태 정의

**Component:** `<CriticalAlert data={riskData} />`

**Props (Input Data Contract):**
*   `riskLevel`: ('low' | 'medium' | 'critical') - 현재 위험 등급.
*   `metricValue`: Number - 애니메이션 될 핵심 수치 (예: "남은 자산 예측액").
*   `gapDescription`: String - 현재의 문제점 요약 문구.

**State Machine (핵심 로직):**
1.  **[Initial State] (Low Risk, 0~2초)**: `riskLevel='low'`. 배경색: `--color-secondary`. 애니메이션: 느린 깜빡임 효과(Subtle pulse)만 적용. 메시지: "당신의 현재 상황을 점검해 보세요."
2.  **[Warning State] (Medium Risk, 3~7초)**: `riskLevel='medium'`. 배경색: `--color-warning`로 그라데이션 시작. 애니메이션: 메트릭 값이 느리게 하락(Decay)하는 그래프 시뮬레이션. 메시지: "경고: 현재의 방치된 상황이 재정적 위험을 초래할 수 있습니다."
3.  **[Critical Alert State] (High Risk, 8초~)**: `riskLevel='critical'`. 배경색: `--color-danger`로 급격히 변하며 플리커(Flicker) 효과 적용. 애니메이션: **수치 폭주 애니메이션**. 메트릭 값이 순간적으로 최대 리스크 값으로 수렴하는 듯한 강렬하고 빠르게 변화하는 그래프와 숫자가 화면을 장악해야 함.

---

### 🖼️ 3. Hero 섹션 통합 UX 흐름 (The Flow)

**[Flow Step]**: 데이터 로딩 $\rightarrow$ 경고 인지 $\rightarrow$ 해결책 필요성 자극
*   **A. 초기 진입:** 페이지 로드 시, 배경에 은은한 `데이터 스트림 노이즈` 애니메이션(CSS Grid + Opacity 변화)을 깔아 '무언가 중요한 것이 작동 중'이라는 느낌 부여. (Tone: 신뢰감 있는 긴장감)
*   **B. 경고 발현:** 2초 지점에서, 메트릭 값을 담은 숫자가 `[Warning State]`로 전환되며 깜빡임 효과를 시작하고 배경색이 오렌지 계열로 변함. 이와 동시에 "데이터 분석 결과: 심각한 격차가 감지되었습니다."라는 문구(진동 애니메이션)가 팝업됨.
*   **C. 임계점 도달 (Climax):** 7초 지점에서, `[Critical Alert State]`로 급격히 전환. 화면 전체에 `--color-danger`의 강한 색상 오버레이가 걸리고, 핵심 수치(예: "추정 손실액")는 **매우 빠른 속도와 높은 진폭**으로 변동하는 애니메이션이 반복되어 사용자의 주의를 극대화함.
*   **D. CTA 연결:** 이 공포의 절정 직후, 화면은 강제로 멈추고(Freeze), 명확하게 `--color-primary`로 강조된 '솔루션 제안' 섹션으로 부드럽게 전환되어야 함. (공포 $\rightarrow$ 해방/희망 구조 완성)

---
</create_file>

📊 평가: 완료 — CEO님의 지시에 따라 기존의 사양과 메모리 속 정보를 통합하여, 개발자가 직접 사용할 수 있는 컴포넌트 단위의 최종 디자인 명세서를 완성했습니다.
📝 다음 단계: 이 명세서에 기반하여 실제 테스트를 진행할 목업 페이지(HTML/React)의 초기 뼈대를 구축하거나, 다른 에이전트에게 필요한 특정 섹션의 콘텐츠 초안을 요청해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: ~\Design\CriticalAlert_Component_Def.md
