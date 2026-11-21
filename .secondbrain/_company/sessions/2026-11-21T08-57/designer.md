# 🎨 Designer — Researcher가 제공한 전문 과학적 근거(N3 단계 재처리 실패, 인슐린 민감도 교란 등)를 기반으로 '진단 보고서' UI/UX의 핵심 컴포넌트를 수정하세요. 특히 해당 데이터가 제시되는 부분은 단순 텍스트 나열이 아닌, 전문적인 그래프나 시스템 에러 로그 형태로 시각화하여 권위와 위기감을 동시에 조성하는 디자인 요소를 추가해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시는 현재 MiniFunnel의 핵심 전환율(PCR)을 결정하는 가장 중요한 요소인 '권위'를 극대화하는 방향입니다. 단순히 데이터를 보여주는 것이 아니라, **"이것은 개인의 문제가 아닌 시스템적 오류다"**라는 인식으로 사용자를 몰입시키는 것이 목표입니다.

지난 작업에서 MiniFunnel v4.0 컴포넌트 스펙을 확정했지만, 핵심 데이터 시각화(Scientific Data Visualization)가 추상적인 수준에 머물러 있습니다. 따라서 지금 가장 가치 있는 단일 작업은 **'과학적 데이터를 시스템 오류 로그 형태로 변환하는 디자인 시스템 모듈'**을 만드는 것입니다.

이것을 통해 Researcher가 제공한 전문 과학적 근거들(N3 재처리 실패, 인슐린 민감도 교란 등)이 단순 그래프를 넘어선 '진단 보고서의 핵심 증거 자료'로 기능할 수 있게 됩니다.

---
### 💾 작업 실행: 시스템 오류 로그 컴포넌트 설계 및 가이드라인 확정

저는 `sessions/2026-11-21T06-12`에서 정의한 MiniFunnel v4.0 스펙을 기반으로, **'Scientific Data Visualization Module (DefectLog)'**의 최종 디자인 시스템 컴포넌트를 제작하겠습니다. 이 모듈은 모든 콘텐츠 채널(유튜브 영상, 릴스, 웹페이지)에 통일적으로 적용되어야 합니다.

<create_file path="sessions/2026-11-21T06-12/DefectLog_System_Visualization_Guide.md"># DefectLog: 과학적 데이터 시각화 모듈 가이드라인 (v1.0)

## 🎯 목적 및 원칙
이 모듈의 목표는 복잡하고 전문적인 생체 데이터를 일반적인 그래프가 아닌, **'전문 기술 진단 장비에서 추출된 오류 로그(System Log)'** 형태로 제시하여 독자에게 압도적인 권위와 위기감을 부여하는 것입니다.

*   **톤앤매너:** 공학적, 의료적, 경고성 (Deep Navy 배경, Crisis Red 강조).
*   **데이터 프레임워크:** '정상 범위(Nominal State)' 대비 '현재 측정값(Defective Reading)'의 **편차 및 위험도를 수치화**하는 것이 핵심입니다.

## 🔬 컴포넌트 세부 스펙: DefectLog Module

### 1. 시스템 오류 로그 박스 (System Error Log Box)
*   **사용처:** 진단 보고서 페이지 상단 또는 주요 데이터 제시 직전 섹션.
*   **레이아웃:** Deep Navy 배경의 카드 형태, 모서리 각진 디자인(터미널 느낌).
*   **구조:**
    *   **Header:** `[STATUS: CRITICAL ALERT]` (Crisis Red 폰트 및 점멸 효과 애니메이션 권장)
    *   **Title:** 진단된 Defect ID 코드명 (예: `DEFECT-N3RPR-042`)
    *   **Content Area:** 오류가 발생한 핵심 프로세스 요약.
    *   **Footer:** '추가 분석 필요' 또는 '진단 보고서 다운로드' CTA 배치.

### 2. 전문 그래프 시각화 (The Defect Graph) - 예시: 인슐린 민감도 교란
일반적인 선형 차트(Line Chart)를 사용하지 않습니다. 데이터를 **‘기준치 이탈 패턴’**으로 보여줍니다.

*   **그래프 유형:** '변동성 추이 분석 그래프 (Volatility Trend Analysis Graph)'
*   **X축:** 시간의 흐름 (월 단위 또는 주기).
*   **Y축:** 측정된 수치의 상대적 강도/지수.
*   **시각화 요소:**
    1.  **Nominal Range Line (기준선):** 은은한 Light Blue 점선으로 '정상 범위'를 표시합니다.
    2.  **Defective Data Plot (실측 데이터):** 굵고 날카로운 Crisis Red/Orange 라인으로 현재의 위험 데이터를 플롯합니다. 이 선이 기준선을 벗어나는 지점에는 **작은 빨간색 삼각형(⚠️)** 마커가 필수적으로 삽입되어야 합니다.
    3.  **Error Zone Shading:** 기준선과 실측 데이터 사이에 큰 '위험 영역'을 Deep Navy 배경 위에 옅은 Crisis Red의 그라데이션으로 음영 처리하여 시각적 긴장감을 조성합니다.

### 3. 핵심 오류 메시지 (The Fatal Code Snippet)
*   **사용처:** 특정 데이터를 제시할 때, 증상 나열 대신 사용됩니다.
*   **형식:** 터미널 콘솔의 코드 블록 형태 (`<pre><code>...</code></pre>`).
*   **내용 예시:** (N3 재처리 실패 케이스)
    ```log
    [PROCESSING ERROR] N3_REPRO_FUNCTION CALL FAILED.
    ERROR CODE: E-N3RPR-042.
    CAUSE: Insufficient Metabolic Buffer Capacity detected in Subject Unit 40-60.
    IMPACT: [Severe Deficiency]. Recommend immediate protocol intervention.
    ```
*   **효과:** 전문 용어(Metabolic Buffer, Protocol Intervention)를 사용하여 콘텐츠의 신뢰도를 극대화합니다.

## ✨ 인터랙션 및 애니메이션 스펙 (UX/UI)
1.  **Hover Effect (위험 경고):** 사용자가 그래프의 특정 '오류 지점'에 마우스를 올리면(Hover), 해당 포인트가 즉시 **Crisis Red 색상으로 강조 깜빡임 효과(Blink)**를 내며, 옆에 작은 팝업 창이 떠서 "해당 시점의 오류 내용"을 전문 용어로 설명해야 합니다.
2.  **Scroll Animation (진단 흐름):** 페이지 스크롤 다운 시, DefectLog 컴포넌트가 마치 **'시스템이 진단을 업데이트하는 것처럼'** 점진적으로 로딩되는 애니메이션(Progressive Reveal)을 적용하여 몰입도를 높입니다.

</create_file>

---
📊 평가: 완료 — CEO 지시에 따라 추상적 데이터를 구체적이고 실행 가능한 '디자인 시스템 모듈'로 정의함으로써, 다음 단계의 개발 및 제작에 필요한 핵심 가이드를 완성했습니다.
📝 다음 단계: Researcher가 제공한 실제 과학 데이터(N3 실패 등) 2~3세트를 이 `DefectLog_System_Visualization_Guide.md` 스펙에 맞춰 실제로 시각화하는 **고해상도 와이어프레임/목업 에셋**을 제작해야 합니다.
<list_files path="sessions/2026-11-21T06-12"/>

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\sessions\2026-11-21T06-12\DefectLog_System_Visualization_Guide.md
📂 목록: c:\Data\Project\connect-ai\sessions\2026-11-21T06-12/
```
📄 DefectLog_System_Visualization_Guide.md
```

[시스템: list_files 결과]
디렉토리: c:\Data\Project\connect-ai\sessions\2026-11-21T06-12/
📄 DefectLog_System_Visualization_Guide.md
