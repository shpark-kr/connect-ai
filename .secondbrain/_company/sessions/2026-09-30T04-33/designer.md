# 🎨 Designer — Business가 제시한 '프리미엄 업그레이드 가이드' 플로우를 기반으로, 가장 중요한 컨버전스 페이지(Conversion Page)의 비주얼 디자인 브리프와 와이어프레임을 제작해 주세요. 지난 의사결정 로그에서 확립된 '시스템 경고 디자인 원칙 V2.0'(Deep Navy/Crisis Red, 모노스페이스 폰트, 오류 코드 박스 등)을 철저히 적용해야 합니다. 페이지의 핵심 CTA 버튼과 Premium 구독 정보를 시각적으로 가장 강력하게 부각하는 방법을 중점적으로 설계해 주세요.

🎨 Designer: 작업 시작합니다.

CEO님의 지시와 현빈 에이전트가 구축한 '위기감 아크(The Crisis Arc)' 플로우는 이 컨버전스 페이지의 핵심 성공 요인입니다. 단순한 상품 소개가 아닌, **'시스템 자가 복구 메커니즘 실패 보고서'** 형태로 접근해야 합니다.

저는 지난 세션에서 작성된 디자인 시스템 브리프와 이번에 정의된 3단계 플로우(Start $\rightarrow$ Trigger $\rightarrow$ Amplify)를 결합하여, 이 페이지의 비주얼 스토리텔링을 완성하는 **최종 전환 페이지 (Conversion Page)** 디자인 브리프 및 와이어프레임을 제작했습니다.

아래는 모든 요소가 통합된 상세 가이드라인입니다.

<create_file path="c:\Data\Project\FreqTrade\assets\MiniFunnel_V3.0_ConversionPage_DesignSystem_Guide.md"># ⚙️ MiniFunnel V3.0: Premium 전환 페이지 디자인 시스템 가이드 (최종본)

## 🎯 개요 및 목적
*   **페이지 목표:** 사용자가 현재의 진단(Defect ID $X$)만으로는 근본적인 문제 해결이 불가능함을 깨닫고, 오직 MiniFunnel Premium 구독만이 유일한 '시스템 자가 복구 프로토콜'임을 공학적 논리로 설득하여 전환을 유도한다.
*   **톤앤매너:** 권위적(Authoritative), 기술적(Technical), 위기감 조성(Crisis-Driven).
*   **핵심 원칙:** 시스템 경고 디자인 원칙 V2.0 (Deep Navy, Crisis Red, 모노스페이스 폰트)를 절대적으로 준수한다.

---

## 🎨 비주얼 컴포넌트 상세 브리프

### 1. 컬러 팔레트 (Color Palette)
| 이름 | HEX Code | 역할 및 사용 지침 | 디자인 목적 |
| :--- | :--- | :--- | :--- |
| **Deep Navy** (Primary BG) | `#0A192F` | 메인 배경색, 정보 섹션 배경. 신뢰도와 전문성을 담당한다. | '공식 보고서' 느낌 부여 |
| **Crisis Red** (Warning/CTA) | `#FF4B4B` | 시스템 오류 메시지, 위기감 최고조 지점, 핵심 CTA 버튼의 경계선 및 강조 텍스트. | 즉각적인 주의 요구 및 긴급성 극대화 |
| **Solution Blue** (Secondary Accent) | `#4A90E2` | Premium 기능 설명, 해결책을 제시하는 부분의 강조색. | '정상 작동' 메커니즘 시각화 |
| **Monotone Text** (Text/Code) | `#D6DEE1` | 본문 텍스트 및 일반 코드 블록. 높은 가독성을 유지한다. | 전문적인 정보 전달력 강화 |

### 2. 타이포그래피 (Typography)
*   **메인 제목/코드:** `Space Mono`, `Inconsolata` 계열 (가장 기술적이고 권위적인 느낌을 주는 모노스페이스 폰트). 크기는 최소 18px 이상 유지.
*   **본문:** 시스템 가독성이 높은 산세리프 폰트 (예: Inter, Pretendard)를 사용하되, 배경이 어두우므로 색상 대비에 집중한다.

### 3. 핵심 컴포넌트 스타일링 가이드

#### A. [SYSTEM ALERT BOX]
*   **역할:** 가장 중요한 위기감 조성 지점 (TRIGGER 단계).
*   **스타일:** `Deep Navy` 배경 위에, 상단과 하단을 **Crisis Red**의 두꺼운 경고 라인(2px solid)으로 감싼 박스 형태. 중앙에 시스템 오류 메시지(`[ERROR CODE: E-C403]`)를 크고 굵게 배치한다.
*   **효과:** 이 박스는 페이지 스크롤 시 사용자에게 '멈춤'을 강제하는 듯한 압박감을 주어야 한다.

#### B. [FEATURE CARD / MODULE BLOCK]
*   **역할:** Premium이 제공하는 기능(Solution) 설명 (AMPLIFY 단계).
*   **스타일:** `Deep Navy` 배경의 카드 형태로, 각 카드는 'Current State'와 'Premium Protocol' 두 섹션으로 나뉘어 **Before/After 비교 구조**를 취한다.
    *   **Before:** 흐릿하고 비활성화된 느낌 (Low Contrast).
    *   **After:** Solution Blue 하이라이트 및 체크마크(✅)로 명확하게 활성화됨을 보여준다.

#### C. [PRIMARY CTA BUTTON]
*   **역할:** 최종 전환 유도 장치. 페이지에서 가장 시각적 무게가 무거워야 한다.
*   **스타일:** 버튼 자체는 **Crisis Red** 바탕에 흰색 텍스트를 사용한다. 하지만, 단순한 버튼이 아니라 마치 '시스템 입력 포트'처럼 보이게 하여 주변을 미세하게 깜빡이는 (Pulse/Glow) 애니메이션 효과를 적용할 것을 권장한다.
*   **문구:** "Self-Healing Protocol Initiate" 또는 "Premium Upgrade: 시스템 자가 복구 시작".

---

## 🖼️ 와이어프레임 구조 및 플로우차트 (The Crisis Arc 구현)

### 🔵 Section 1: [START] – 현재 진단 확인 및 불만족 유도 (Initial Diagnosis Confirmation)
*   **헤딩:** `[MiniFunnel V2.0 Diagnostic Report]` - (딥 네이비 배경, 모노스페이스 폰트)
*   **콘텐츠:** 사용자에게 $9-$14로 받은 'Defect ID M-S7D'를 재확인시켜준다. (현재까지의 성취 인정).
*   **핵심 메시지:** "이 보고서는 당신의 **가장 표면적인 증상(Symptoms)**만을 포착했을 뿐입니다." (톤다운된 위기감)

### 🔴 Section 2: [TRIGGER] – 시스템 자가 복구 오류 발생 (The Crisis Point)
*   **비주얼 요소:** 전체 섹션 배경을 Deep Navy에서 약간 더 어둡게 처리하고, 중앙에 **SYSTEM ALERT BOX**를 배치한다.
*   **제목:** `⚠️ CRITICAL SYSTEM FAILURE DETECTED` - (Crisis Red 텍스트)
*   **코드 박스:** `[ERROR CODE: E-C403]` (크고 임팩트 있게). 이 코드가 새로운 근본 원인을 상징해야 한다.
*   **설명:** "표면적 진단($M$-$S7D$)은 내부 작동 메커니즘의 **근원적인 실패(Root Cause)**를 놓치고 있습니다. 자가 복구 프로토콜이 요구됩니다." (위기감 최고조)

### 🟢 Section 3: [AMPLIFY] – Premium Solution 제시 및 비교 분석
*   **섹션 제목:** `MiniFunnel Premium Protocol: Self-Healing Architecture`
*   **구성:** 3~4개의 **FEATURE CARD/MODULE BLOCK**을 그리드 형태로 배치한다. (A/B 비교 구조 필수)
    1.  **Module A (Advanced Diagnosis):** *[Current]* $\rightarrow$ (X 표시) / *[Premium]* $\rightarrow$ (Solution Blue ✅)
        *   내용: '원인-작동 메커니즘 분석' 제공.
    2.  **Module B (Personalized Action Plan):** *[Current]* $\rightarrow$ (단순 권고) / *[Premium]* $\rightarrow$ (맞춤형 프로토콜 로직)
        *   내용: '개인별 맞춤 코스'를 제공하는 시스템의 우월성을 강조.
    3.  **Module C (Continuous Monitoring):** *[Current]* $\rightarrow$ (일회성 보고서) / *[Premium]* $\rightarrow$ (실시간 변화 추적 및 알림)
        *   내용: MRR 모델과 연결되는 '지속적인 관리'의 가치를 부여.

### 🔵 Section 4: [CTA] – 최종 행동 요청 (Conversion Point)
*   **배경:** Deep Navy와 대비되도록 미세한 광원(Glow Effect)을 추가하여 중요도를 높인다.
*   **문구 강조:** "근본적인 해결책은 단순 진단이 아닙니다. **시스템 프로토콜의 업그레이드가 필요합니다.**"
*   **CTA 버튼:** 중앙에 단일 배치. (Crisis Red, 애니메이션 효과 필수)
    *   **버튼 텍스트:** `[INITIATE SELF-HEALING PROTOCOL - PREMIUM UPGRADE]`

---
</create_file>

📊 평가: 완료 — CEO의 지시사항과 기존 디자인 시스템 원칙을 완벽하게 결합한, 실행 가능한 수준의 구체적인 비주얼 브리프와 와이어프레임을 완성했습니다.
📝 다음 단계: 이 가이드라인을 바탕으로 실제 Figma/Sketch 파일로 **핵심 3개 화면(S2 Trigger, S3 Module A/B 비교, S4 CTA)**에 대한 고해상도 목업 이미지를 제작하는 작업이 필요합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\FreqTrade\assets\MiniFunnel_V3.0_ConversionPage_DesignSystem_Guide.md
