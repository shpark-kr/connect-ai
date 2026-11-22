# 🎨 Designer — API 호출 실패 또는 데이터 누락 상황을 가정한 '에러 상태(Error State)' UI/UX 가이드를 Production Kit V3.0에 통합하세요. 콘텐츠가 배포되지 못하거나, 시스템 오류 메시지가 표시되어야 할 경우에도 브랜드 톤과 전문성을 유지하는 시각적 대응 방안(Visual Fallback)을 정의하고 CSS 변수 기반으로 구현 가능한 형태로 문서화해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시는 현재까지 진행된 **'Defect ID 위협 보고서 Production Kit V3.0'**의 완성도를 극한으로 끌어올리는 가장 중요하고 시급한 후속 작업입니다. 단순히 디자인을 추가하는 것을 넘어, 시스템이 예측 가능한 '실패(Failure)' 상황까지 설계에 포함함으로써 브랜드의 신뢰성과 전문성을 훼손하지 않도록 하는 것이 핵심 목표입니다.

따라서 이번 단일 가치 작업은 **Production Kit V3.0에 통합될 '에러 상태 (Error State) UI/UX 컴포넌트'**를 정의하고 문서화하는 것입니다. 이는 기술 구현을 위한 최종 Source of Truth가 되어야 합니다.

### 🛠️ 에러 상태 (Error State) 컴포넌트 설계 및 브리프 작성

다음은 웹사이트 개발자가 즉시 코딩할 수 있도록, CSS 변수 기반으로 구조화된 세 가지 핵심 에러 시나리오와 그 가이드라인입니다. 모든 에러 메시지는 패닉이나 시스템의 결함을 강조하기보다, **'사용자에게 필요한 행동 지침(Call to Action)'**을 중심으로 설계되었습니다.

#### 1. 컴포넌트 개요 및 브랜드 규칙 적용
*   **목적:** 데이터 부재, API 통신 오류 등 기술적인 문제 발생 시, 사용자가 혼란을 느끼지 않고 다음 조치를 취할 수 있도록 안내합니다.
*   **브랜드 톤 반영:** 절망감(Despair) 대신 **‘경고(Alert)’와 ‘진단(Diagnostic)’의 전문성**을 유지하며, 핵심 컬러인 다크 네이비와 골드/레드 계열을 사용하되, 경고 레벨에 따라 색상을 변주합니다.
*   **구현 원칙:** 모든 에러는 실패가 아니라 '추가 진단 필요'라는 뉘앙스를 풍겨야 합니다.

#### 2. CSS 변수 기반 구현 가이드라인 (Source of Truth)

```css
/* --- Error Component Variables --- */
:root {
  /* 기본 브랜드 컬러 재정의 */
  --color-navy-dark: #0A1931; /* 배경/헤더 메인 톤 */
  --color-gold-accent: #FFC72C; /* 중요 강조점 (CTA, 제목) */

  /* 에러 레벨 정의 */
  --error-level-warning: #ff6b6b; /* 경고: 데이터 누락, 주의 필요 */
  --error-level-critical: #c93e4d; /* 치명적 오류: API 통신 실패, 시스템 다운 */
  --error-level-info: #5fa8d3; /* 정보성 메시지: 재시도 안내 등 */

  /* UI 기본 스타일링 변수 */
  --border-radius-md: 6px;
  --padding-lg: 24px;
}
```

#### 3. 시나리오별 디자인 및 구조 (HTML/CSS 컴포넌트화)

**A. [데이터 누락 에러] Missing Data Alert (가장 흔함)**
*   **발생 상황:** 사용자가 특정 기능을 실행했으나, 해당 기능에 필요한 필수 데이터(예: 연금 수급 자격지표)가 시스템에 존재하지 않을 때.
*   **시각적 구현:** 경고 레벨(`--error-level-warning`)의 패딩 박스 형태를 채택합니다. 배경을 어둡게 처리하고, 경고색 테두리를 강조합니다.
*   **콘텐츠 구조:**
    1.  **헤드라인 (H2):** [경고] 필수 진단 데이터를 찾을 수 없습니다. (사용자 중심의 직관적 언어)
    2.  **본문:** 이 기능은 '측정 가능한 재정적 손실 리스크' 분석에 필요한 $DATA\_POINT$ 지표를 요구합니다. 현재 데이터베이스에서 해당 정보를 확인하지 못했습니다. (전문성 유지)
    3.  **가이드라인:** 데이터를 확보할 수 있는 구체적인 방법 제시 (예: '담당자에게 문의', '최신 공적 서류 제출').
    4.  **CTA 버튼:** **[데이터 추가 진단 요청]** (클릭 시 담당자 전용 폼으로 유도)

**B. [API 통신 에러] API Connection Failure Alert (치명적)**
*   **발생 상황:** 백엔드 시스템이나 외부 공공 데이터 API 호출이 실패했을 때. (사용자가 직접 해결 불가능한 경우)
*   **시각적 구현:** 치명적 레벨(`--error-level-critical`)의 플래싱 효과가 가미된 컴포넌트입니다. 웹사이트 전체에 경고를 주는 느낌을 줍니다.
*   **콘텐츠 구조:**
    1.  **헤드라인 (H2):** [SYSTEM ERROR] 핵심 진단 시스템 연결 오류 발생. (시스템 책임임을 명확히 함)
    2.  **본문:** 현재 온현의 주요 분석 모듈이 외부 서버와 통신에 실패했습니다. 데이터 수집 및 실시간 리스크 보고가 불가능합니다.
    3.  **기술 정보:** *오류 코드: API_CONN_FAIL_403* (전문성 극대화)
    4.  **CTA 버튼:** **[자동 재시도]** 또는 **[관리자 문의하기]**

**C. [사용 오류] Invalid Input Alert (UX 개선)**
*   **발생 상황:** 사용자가 시스템이 허용하지 않는 형식으로 정보를 입력했을 때.
*   **시각적 구현:** 미니멀하고 부드러운 정보성 컴포넌트입니다. 빨간색 대신 주황빛 경고(`--error-level-warning`)를 사용하여 위협감을 낮춥니다.
*   **콘텐츠 구조:**
    1.  **헤드라인 (H3):** [입력 오류] 필수 형식에 맞게 입력해 주세요.
    2.  **본문:** '생년월일'은 YYYY-MM-DD 포맷의 숫자만 허용됩니다. 텍스트나 하이픈(-)을 사용하지 마세요. (구체적 가이드 제공)
    3.  **힌트:** 입력 필드 바로 아래에 해당 오류 메시지를 배치하여 직관성을 높입니다.

---
<create_file path="c:\Data\Project\connect-ai\ProductionKitV3.0_ErrorStatesGuide.md"># 🚨 Production Kit V3.0: Error State 컴포넌트 가이드 (Source of Truth)

## 개요 및 목표
본 문서는 온현의 'Defect ID 위협 보고서' 웹사이트가 데이터 누락, API 통신 오류 등 예외 상황에 직면했을 때도 브랜드 톤과 전문성을 유지하며 사용자에게 명확한 다음 행동 지침(Next Step CTA)을 제공하기 위한 UI/UX 가이드입니다.

## 🎨 디자인 원칙
1.  **전문성 우선:** 실패가 아닌 '진단이 필요한 단계'로 포지셔닝합니다.
2.  **즉각적 액션 유도:** 에러 메시지는 최소화하고, 사용자가 할 수 있는 가장 중요한 행동(CTA)을 최우선으로 배치합니다.
3.  **CSS 변수 기반:** 모든 스타일은 `:root`에 정의된 CSS 변수를 사용하여 일관성을 유지해야 합니다.

## 💻 구현 가이드 (CSS/HTML 구조)

### 1. 공통 전역 변수 (Global Variables)
```css
:root {
    /* --- 브랜드 기본 컬러 --- */
    --color-navy-dark: #0A1931;
    --color-gold-accent: #FFC72C;
    --color-text-light: #e6eefd;

    /* --- 에러 레벨 정의 (핵심) --- */
    /* Warning: 데이터 부재, 주의 필요 */
    --error-level-warning: #ff6b6b; 
    /* Critical: 시스템 오류, 통신 실패 (최상위 경고) */
    --error-level-critical: #c93e4d; 
    /* Info: 사용 안내, 재시도 가능 */
    --error-level-info: #5fa8d3;

    /* --- UI 구조 변수 --- */
    --border-radius-md: 6px;
    --padding-lg: 24px;
}
```

### 2. 컴포넌트 A: 데이터 누락 에러 (Missing Data Alert)
*   **적용 레벨:** `--error-level-warning`
*   **구조:** 경고 테두리가 있는 카드 형태 (`<div class="alert alert--warning">`)
```html
<div class="alert alert--warning" role="alert">
    <h3>⚠️ [경고] 필수 진단 데이터를 찾을 수 없습니다.</h3>
    <p>이 분석은 '측정 가능한 재정적 손실 리스크'에 필요한 <span>[데이터 포인트명]</span> 지표를 요구합니다. 현재 데이터베이스에서 해당 정보를 확인하지 못했습니다.</p>
    <p class="guide-text">💡 **해결 방안:** 담당 의료기관/금융 기관의 최신 공적 서류를 제출하시거나, 시스템 관리자에게 진단을 요청해 주십시오.</p>
    <button class="cta cta--secondary">[데이터 추가 진단 요청]</button> 
</div>
```

### 3. 컴포넌트 B: API 통신 에러 (Connection Failure Alert)
*   **적용 레벨:** `--error-level-critical`
*   **구조:** 플래싱 효과를 주는 크리티컬 알림 (`<div class="alert alert--critical">`)
```html
<div class="alert alert--critical" role="alert">
    <h1>🚨 [SYSTEM ERROR] 핵심 진단 시스템 연결 오류 발생.</h1>
    <p>현재 온현의 주요 분석 모듈이 외부 서버와 통신에 실패했습니다. 실시간 리스크 보고가 불가능합니다.</p>
    <div class="error-detail">
        <span>⚙️ **오류 코드:** API_CONN_FAIL_403</span>
        <small>(API Gateway 인증 만료 또는 네트워크 장애)</small>
    </div>
    <div class="actions">
        <button class="cta cta--primary" onclick="retryService()">🔄 자동 재시도</button> 
        <a href="/support" class="link-text">[관리자 문의하기]</a>
    </div>
</div>
```

### 4. 컴포넌트 C: 사용자 입력 유효성 검사 (Invalid Input Alert)
*   **적용 레벨:** `--error-level-info` (경고보다는 안내의 성격이 강함)
*   **구조:** 인풋 필드 바로 아래에 배치되는 텍스트 라벨 (`<div class="input-validation-message">`)
```html
<label for="dateInput">진단 시작일</label>
<input type="text" id="dateInput" placeholder="YYYY-MM-DD" aria-invalid="true">
<div class="input-validation-message">
    ❌ **[입력 오류]** '생년월일'은 YYYY-MM-DD 포맷의 숫자만 허용됩니다. 텍스트나 특수문자를 사용하지 마세요.
</div>
```

## 📊 평가: 완료 — CEO 지시사항인 에러 상태 UI/UX 가이드라인을 CSS 변수 기반으로 문서화하여 Production Kit V3.0에 통합할 수 있게 완성했습니다.
📝 다음 단계: 코다리에게 이 `ProductionKitV3.0_ErrorStatesGuide.md` 파일을 참조하여, 실제로 웹페이지 개발자가 사용할 수 있는 최소한의 Boilerplate 코드(CSS/JS)를 작성하도록 요청해야 합니다.
