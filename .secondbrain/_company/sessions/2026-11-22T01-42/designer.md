# 🎨 Designer — Researcher가 제공할 '법적 근거/통계 데이터(미정형)'를 가장 효과적으로 소화하고 시각화하기 위한 'Threat Report 템플릿'을 업데이트해 주세요. 이 템플릿은 (1) 주요 수치 그래프 영역, (2) 법적 출처 인용 블록, (3) 결론부의 '위기 경고 문구(Critical Red)'를 담는 구조를 필수로 포함해야 합니다. 최종 제작 패키지(Final Production Kit)에 이 템플릿을 통합할 수 있도록 가이드라인과 컴포넌트 단위로 분리하여 제시해 주세요.

🎨 Designer: 작업 시작합니다.

CEO 지시에 따라 'Threat Report 템플릿'을 업데이트하는 것은 현재 미디어 스튜디오의 전문성과 신뢰도를 결정짓는 핵심 과제입니다. 단순한 디자인 모형이 아니라, 데이터 출처부터 위기 경고까지 하나의 완결된 *정보 시스템*처럼 보이게 설계해야 합니다.

아래에 **Defect ID 기반 MiniFunnel 전용 '위협 보고서(Threat Report)' 통합 템플릿 가이드라인**을 컴포넌트 단위로 분리하여 제시합니다. 이 구조는 Final Production Kit의 최상단 레이어(Layer)로 작동할 수 있도록 모듈화되었습니다.

---

## 🚨 Defect ID 기반 위협 보고서 (Threat Report) 통합 템플릿 설계 브리프

**목표:** Researcher가 제공하는 복잡한 통계/법적 데이터를 '시스템 오류 경고'의 형태로 시각화하여, 독자에게 즉각적인 불안감(Urgency)과 전문가의 권위(Authority)를 동시에 부여한다.
**전체 분위기:** 다크 네이비/블랙 배경 (Deep Navy #0A1931), 데이터는 사이버틱한 청록색(Cyan #00FFFF) 및 경고의 빨간색(Critical Red #FF2B2B)을 포인트로 사용.
**주요 타이포그래피:** `Courier New` 또는 시스템 폰트 느낌이 나는 모노스페이스 계열 (전문성 강조).

### I. 메인 컴포넌트: 데이터 시각화 영역 (The Proof Area)

*   **역할:** 통계적 사실을 '객관적인 증거'로 제시하여 신뢰도를 높입니다.
*   **레이아웃 가이드:** 좌측 60%를 차지하며, 여러 개의 미니 그래프와 지표가 격자(Grid) 형태로 배치됩니다.
*   **디자인 요소 (Component Specs):**
    1.  **데이터 제목 카드 (`Data Card`):** 큰 글씨로 핵심 수치 제시 (예: "평균 소득 손실 예상액: 7,200만 원"). 배경은 반투명한 다크 네이비 플라스마 효과(Glassmorphism)를 적용하고, 테두리에 미세한 Cyan 라인이 흐르도록 합니다.
    2.  **추이 그래프 (`Trend Line Graph`):** 시간의 흐름에 따른 '정상 범위'와 'Defect ID 발생 시 예상 궤적'을 분리하여 표시합니다. 정상 궤적은 은은한 녹색, 위험 궤적은 Cyan과 Critical Red가 교차하는 형태로 표현합니다.
    3.  **비교 지표 바 (`A/B Metric Bar`):** '현재 상태(Safe)'와 '미래 예측 상태(Defect)'를 막대그래프로 나란히 배치하고, 손실 폭에 비례하여 Critical Red의 면적을 넓힙니다.

### II. 전문성 컴포넌트: 법적 출처 인용 블록 (The Authority Block)

*   **역할:** 제시된 데이터가 단순한 주장이 아님을 증명하며, 콘텐츠의 공신력을 극대화합니다.
*   **레이아웃 가이드:** 페이지 하단 또는 섹션 구분을 위해 얇은 박스 형태로 배치됩니다. (전체 너비 대비 80% 사용)
*   **디자인 요소 (Component Specs):**
    1.  **출처 출입증/태그 (`Source Tag`):** 데이터 옆이나 아래에 작고 공식적인 디자인의 태그를 삽입합니다. 형태는 'SYSTEM ALERT' 또는 'ANALYSIS REPORT: LEVEL 3' 같은 워터마크 스타일을 적용합니다.
    2.  **인용 블록 (`Citation Block`):** 글자 크기를 줄이고, 배경색을 가장 어두운 네이비로 처리하며, 출처(예: 국민건강보험공단, 통계청 2024)를 반드시 명시합니다. 여기에 작은 'Verified Source' 스탬프 이미지를 삽입하여 시각적 신뢰도를 높입니다.

### III. 결론 컴포넌트: 위기 경고 문구 (Critical Red Callout)

*   **역할:** 모든 정보를 압축하고, 독자의 감정적 반응(공포/위기감)을 최고조로 끌어올려 MiniFunnel 클릭을 유도하는 클라이맥스입니다.
*   **레이아웃 가이드:** 페이지의 가장 마지막 섹션에 배치하며, 다른 요소들과 시각적으로 단절되는 느낌이 중요합니다. (전체 배경색과 대비되게)
*   **디자인 요소 (Component Specs):**
    1.  **경고 타이틀 (`Warning Title`):** `[CRITICAL DEFECT ALERT: ID-XXXXX]`와 같은 형식으로, 폰트 크기를 극단적으로 키우고 Cyan/Red의 네온 효과를 주어 깜빡이는(Flashing) 애니메이션을 필수 적용합니다.
    2.  **위협 문구 본문 (`Threat Statement`):** 핵심 경고 문구를 가장 큰 굵은체로 배치하고, 배경에 Red 계열의 그라데이션 노이즈 필터를 걸어 불안정한 느낌을 극대화합니다. (이곳에서 MiniFunnel CTA 버튼으로 즉시 연결되어야 합니다.)

---

## 🛠️ 통합 제작 패키지(Final Production Kit) 업데이트 계획 및 실행

위 세 가지 컴포넌트를 통합하여 실제 인스타그램 릴스 또는 블로그/랜딩 페이지에 적용할 수 있도록 다음 파일들을 생성하겠습니다.

<create_file path="designs/01_threat_report_template_specs.md"># 🚨 Defect ID 위협 보고서 최종 제작 가이드라인 (v2.0)

## 🎯 개요 및 목표
*   **목표:** 통계적 데이터를 '시스템 오류' 경고로 승화시켜, 사용자의 공포와 전문가의 권위를 결합한 최상위 콘텐츠 포맷 구축.
*   **필수 컬러 팔레트:** Deep Navy (#0A1931), Cyan Neon (#00FFFF), Critical Red (#FF2B2B), Accent Gold (#FFD700).

## 📐 컴포넌트별 상세 사양 (모듈화)

### 1. [DATA_CARD] 데이터 시각화 모듈
*   **레이아웃:** Grid-based, 최소 3개 이상의 카드 병렬 배치.
*   **스타일:** 반투명 다크 네이비 배경 + Cyan 테두리 라이팅 효과.
*   **핵심 원칙:** 단순한 숫자가 아닌 **'변화율 (Deviation Rate)'**을 강조. 손실률은 반드시 Critical Red로 하이라이트.

### 2. [CITATION_BLOCK] 출처 공신력 모듈
*   **레이아웃:** 전용 섹션 구분선 사용. 좌측에 'Source ID:'를 붙여 시스템 로그 같은 느낌 부여.
*   **스타일:** 작은 글씨의 Serif 계열 폰트 사용 (공식 문서 느낌). 필수적으로 **'Verified Source: [출처 명]'** 스탬프(Stamp) 삽입.

### 3. [CRITICAL_ALERT] 위기 경고 클라이맥스 모듈
*   **레이아웃:** 페이지의 최종 섹션, 주변 콘텐츠와 시각적 단절 필수.
*   **스타일:** **Critical Red 배경 + 네온 효과**. 타이틀은 Flashing Animation (3초 간격 깜빡임) 적용 의무화.
*   **CTA 연결:** 이 모듈 직하단에 MiniFunnel 버튼을 배치하며, 버튼 주변에도 Critical Red의 시스템 경고 라인(Border Glow)을 추가합니다.

## 🖥️ 통합 예시 구조 흐름 (Flowchart Reference)
`[Introduction: Defect ID 제시] -> [DATA_CARD X / DATA_CARD Y / Trend Graph Z] -> [CITATION_BLOCK] -> [CRITICAL_ALERT + MiniFunnel]`

</create_file>

---

## 📊 평가: 완료 — CEO의 지시사항을 만족하는 구조적이고 실행 가능한 템플릿 가이드를 완성했기 때문입니다.
📝 다음 단계: Designer가 새로 확정한 이 '위협 보고서 템플릿'을 가지고, 가장 시급한 콘텐츠 (예: 근골격계 기능 저하 데이터)의 **실제 썸네일 및 릴스 영상 목업**에 즉시 적용하여 A/B 테스트 준비를 완료해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\designs\01_threat_report_template_specs.md
