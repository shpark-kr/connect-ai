# 🎨 Designer — 블로그 콘텐츠의 신뢰도를 높이고 CTA 전환율을 극대화하기 위해, 핵심 정보를 요약한 '필수 체크리스트' 형태의 인포그래픽 템플릿 (노랑/흰색 고대비 필수)을 제작하십시오. 이 디자인은 블로그와 랜딩페이지에 삽입되어 독자가 즉시 행동할 수 있도록 유도해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시사항과 현재 블로그 콘텐츠의 흐름(불안감 유발 $\rightarrow$ 문제 제기 $\rightarrow$ 해결책 제시)을 고려했을 때, 가장 중요한 것은 **'정보 전달'에서 '행동 유도'로 전환시키는 브릿지**를 만드는 것입니다. 따라서 단순한 인포그래픽이 아닌, 독자가 자신의 현재 상태를 자가진단하고 다음 행동을 취하도록 설계된 인터랙티브 UI 컴포넌트로서의 '체크리스트 시스템'으로 접근해야 합니다.

아래는 이 핵심 정보를 요약하여 블로그와 랜딩페이지에 즉시 삽입 가능하며, CTA 전환율을 극대화하는 **'노후 자산 사각지대 필수 체크리스트' 디자인 스펙**입니다.

### 📄 [최종 산출물] '사각지대 진단 체크리스트' Design Spec v1.0

이 컴포넌트는 HTML/CSS 키트로 제작되어 개발팀에 전달하며, **노랑(경고) / 흰색(정보) / 검은색(텍스트)**의 고대비 조합을 사용합니다.

#### 🎨 1. 디자인 시스템 정의 (Color & Typography)

| 요소 | 용도 | 컬러 코드 (HEX) | 설명 및 역할 |
| :---: | :---: | :---: | :---: |
| **Primary Warning** | 사각지대 경고, 중요 액션 버튼 배경 | `#FFD700` (골드 톤 노랑) | 사용자에게 '주의'를 환기시키는 핵심 색상. 지나친 채도는 피하고, 신뢰감을 주는 골드 느낌으로 조정. |
| **Background** | 콘텐츠 영역 배경 | `#FFFFFF` | 최대의 가독성을 위한 흰색 바탕. |
| **Text Primary** | 본문 텍스트, 제목 | `#1A1A1A` (거의 검정) | 높은 대비를 유지하여 눈의 피로도를 낮춤. |
| **Accent/Success** | 체크 완료(Good), 안전 지점 표시 | `#4CAF50` (녹색) | 사용자가 이미 통제하고 있는 영역임을 시각적으로 안심시키는 역할. |
| **Typography** | 제목 및 강조 텍스트 | Noto Sans KR Bold | 가독성과 신뢰성을 주는 고딕 계열의 폰트를 최우선으로 지정합니다. |

#### 🧱 2. 컴포넌트 구조 (Component Architecture)

이 체크리스트는 총 3가지 Pain Point를 다루며, 각 항목은 다음 4단계의 논리적 흐름을 가집니다.

1.  **[Pain Point Title]:** 주제 제시
2.  **[Check Item/Question]:** 사용자가 스스로에게 던져야 할 질문 (불안감 유발)
3.  **[Status Indicator]:** 현재 상태를 시각적으로 판단하는 부분 (빨강 $\rightarrow$ 노랑 $\rightarrow$ 녹색)
4.  **[Action Button]:** 다음 행동을 유도하는 CTA (가장 중요)

---
#### 💡 3. 상세 구조 및 내용물 작성 (The Template Content)

<create_file path="C:\Data\Project\connect-ai\결과물\03_기획_디자인\Gap_Checklist_DesignSpec_v1.0.html">
<!-- Gap Warning Module Checklist -->
<style>
    /* TailwindCSS 또는 CSS 변수 사용 권장 */
    :root {
        --color-warning: #FFD700; 
        --color-text: #1A1A1A;
        --color-background: #FFFFFF;
        --font-family: 'Noto Sans KR', sans-serif;
    }

    .checklist-container {
        max-width: 850px;
        margin: 40px auto;
        padding: 30px;
        border: 2px solid var(--color-warning); /* 경고 테두리 */
        background-color: #FFFDE7; /* 미세한 노랑 배경으로 주목도 높임 */
        border-radius: 15px;
    }

    .checklist-item {
        display: flex;
        align-items: center;
        margin-bottom: 25px;
        padding: 15px;
        background-color: #FFFFFF;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

    /* 상태별 색상 */
    .status-risk { color: #D32F2F; font-weight: bold; } /* 빨간색 (위험) */
    .status-caution { color: #FFA000; font-weight: bold; } /* 주황색 (주의) */
    .status-safe { color: #4CAF50; font-weight: bold; } /* 녹색 (안전) */

    /* CTA 버튼 스타일링 - 가장 크고 눈에 띄게 */
    .cta-button {
        display: block;
        width: 100%;
        padding: 20px;
        background-color: #FFD700; /* Warning Primary Color 사용 */
        color: var(--color-text);
        font-size: 1.4rem;
        font-weight: bold;
        text-align: center;
        border: none;
        cursor: pointer;
        margin-top: 30px;
        transition: background-color 0.3s;
    }
</style>

<div class="checklist-container">
    <h1>🚨 노후 자산 사각지대 필수 진단 체크리스트 (5060 필독)</h1>
    <p style="font-size: 1.1rem; margin-bottom: 30px;">아래 질문에 답하며, 당신의 은퇴 준비 상태를 객관적으로 점검해 보세요. 놓친 단 하나의 사각지대가 큰 위협이 될 수 있습니다.</p>

    <!-- ==================== 항목 1: 국민연금 리스크 ==================== -->
    <div class="checklist-item">
        <span style="flex: 3; font-size: 1.2rem;"><strong>💰 1. 은퇴 후 소득 빈틈 점검 (국민연금)</strong></span>
        <span style="flex: 4; text-align: right; color: #D32F2F;">⚠️ 사각지대 의심</span>
    </div>
    <div class="checklist-item">
        <p style="flex: 3; font-size: 1rem; margin-bottom: 5px;">✅ **질문:** 직장 은퇴 후, 연금 외의 추가 소득 흐름(임대, 재취업 등)을 확보할 구체적 계획이 있습니까?</p>
        <span style="flex: 4; text-align: right;"><strong class="status-risk">❌ 위험! (점검 필요)</strong></span>
    </div>

    <!-- ==================== 항목 2: 장기요양보험 리스크 ==================== -->
    <div class="checklist-item">
        <span style="flex: 3; font-size: 1.2rem;"><strong>🏥 2. 돌봄 비용의 숨겨진 지출 점검 (장기요양)</strong></span>
        <span style="flex: 4; text-align: right; color: #D32F2F;">⚠️ 사각지대 의심</span>
    </div>
    <div class="checklist-item">
        <p style="flex: 3; font-size: 1rem; margin-bottom: 5px;">✅ **질문:** 본인 부담금 외, 간병/특수 재활 등 비급여 영역에 대한 대비 예산과 플랜이 수립되어 있습니까?</p>
        <span style="flex: 4; text-align: right;"><strong class="status-risk">❌ 위험! (점검 필요)</strong></span>
    </div>

    <!-- ==================== 항목 3: 상속 및 자산 리스크 ==================== -->
    <div class="checklist-item">
        <span style="flex: 3; font-size: 1.2rem;"><strong>💰 3. 미래 재산 이전 구조 점검 (상속세/증여)</strong></span>
        <span style="flex: 4; text-align: right; color: #D32F2F;">⚠️ 사각지대 의심</span>
    </div>
    <div class="checklist-item">
        <p style="flex: 3; font-size: 1rem; margin-bottom: 5px;">✅ **질문:** 현재 보유 자산에 대해 법적/세무적으로 최적화된 이전 계획(사전 증여, 신탁 등)이 마련되어 있습니까?</p>
        <span style="flex: 4; text-align: right;"><strong class="status-risk">❌ 위험! (점검 필요)</strong></span>
    </div>

    <!-- ==================== 최종 CTA 섹션 (핵심 전환 구간) ==================== -->
    <div style="margin-top: 50px;">
        <h3>📌 당신의 현재 점수는?</h3>
        <p>위 세 가지 항목 중 **하나라도 '❌ 위험!'** 에 해당한다면, 지금 바로 전문가 진단이 필요합니다. 사각지대는 스스로 파악하기 가장 어렵습니다.</p>

        <!-- 최종 CTA 버튼 -->
        <button class="cta-button" onclick="window.location.href='[랜딩페이지 URL]'">
            👉 [무료] 3가지 사각지대 완벽 진단 체크리스트 다운로드 받기 (클릭)
        </button>
        <p style="font-size: 0.9rem; color: #666; margin-top: 15px;">*진단 리포트에서는 개인별 맞춤형 해결책을 제시합니다.</p>

</div>
</create_file>

#### 📝 4. 개발팀 전달 가이드라인 (Implementation Notes)

| 영역 | 요구사항 | 비고 |
| :---: | :---: | :---: |
| **반응성(Responsiveness)** | 모바일 환경에서 체크리스트 항목이 한 줄로 깔끔하게 재배치되어야 함. 폰트 크기 조정 필수. | `flex-basis` 또는 Grid 시스템 활용 권장. |
| **상태 로직** | '위험' 상태는 단순 텍스트가 아닌, 경고 아이콘(⚠️)과 함께 노란색 배경의 하이라이팅을 적용해야 함. | CSS 애니메이션: 마우스 오버 시 미세한 그림자 변화 유도 (Depth감). |
| **CTA 최적화** | CTA 버튼 클릭 시, 사용자 경험 측면에서 '페이지 스크롤'보다는 즉시 랜딩 페이지로 이동하도록 설정할 것. (직접적인 트래픽 전환 목표) | A/B 테스트용 카피: "무료 진단 체크리스트 다운로드"와 "맞춤형 노후 계획 상담받기" 두 가지 버전 준비 필수. |

---
📊 평가: 완료 — 사용자가 요구한 고대비의 행동 유도 중심의 인포그래픽 템플릿 스펙을 구체적인 HTML/CSS 구조로 제공하여 블로그에 즉시 적용 가능하게 함.
📝 다음 단계: 코다리에게 이 `Gap_Checklist_DesignSpec_v1.0.html` 파일을 기반으로, 실제 웹페이지 삽입 가능한 반응형 CSS 컴포넌트 키트를 요청하고, 랜딩 페이지의 CTA 버튼과 연동할 수 있는 초기 개발 테스트를 진행해야 함.

---
## 📁 파일 액션 결과

✅ 생성: C:\Data\Project\connect-ai\결과물\03_기획_디자인\Gap_Checklist_DesignSpec_v1.0.html
