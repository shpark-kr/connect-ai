# 🎨 Designer — MiniFunnel V2.0의 '시스템 경고' 원칙에 맞춰 모든 콘텐츠(썸네일, 리스/피드, 랜딩 페이지 UI)에 사용될 핵심 비주얼 에셋 패키지를 제작해 주세요. 반드시 다음 요소를 포함해야 합니다: 1. Deep Crimson Red를 활용한 표준 시스템 경고 배너 (System Alert), 2. Researcher가 제공할 'Defect ID'와 공학적 용어를 결합하여 시각화하는 오류 코드/진단 결과 템플릿, 3. CLI(Command Line Interface) 콘솔 스타일의 정보 박스 및 테스트 리포트 프레임워크, 4. 모노스페이스 폰트를 적용한 표준 타이포그래피 세트입니다. 이 모든 에셋은 즉시 재사용 가능해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO님의 지시 사항은 MiniFunnel의 핵심 가치인 '공학적 위기감'을 모든 접점에서 일관되게 유지하는 가장 중요한 기반 작업입니다. 요청하신 대로, 콘텐츠 제작에 즉시 투입 가능한 **MiniFunnel V2.0 디자인 시스템 (Visual Asset Package)**을 구축하고 이를 파일로 제공합니다.

이 브리프는 컬러 팔레트부터 폰트 규격, 그리고 핵심 컴포넌트 3가지(경고 배너, 오류 코드, CLI 리포트)의 상세 스펙까지 담고 있습니다. 모든 에셋은 Dark Mode 기반의 '시스템 UI' 느낌을 유지하도록 설계되었습니다.

<create_file path="assets/MiniFunnel_V2.0_DesignSystem_Brief.md"># ⚙️ MiniFunnel V2.0 디자인 시스템 가이드라인 (Visual Asset Package)

이 문서는 온현의 모든 콘텐츠(썸네일, 리스, 랜딩 페이지 UI)에 공통적으로 적용되는 표준 비주얼 에셋 및 규격집입니다. 목표는 사용자가 '정보 획득'을 넘어 '시스템적 위기 진단 프로토콜 실행'이라는 권위적인 경험을 하게 만드는 것입니다.

---

## 1. 🎨 컬러 팔레트 (Color Palette)

모든 색상 코드는 Hex Code를 기준으로 하며, 대비(Contrast Ratio)와 의미론적 사용처가 명확히 구분됩니다.

| 이름 | 역할 (Role) | HEX 코드 | CMYK/RGB (참고) | 사용 원칙 및 용도 |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Dark** | 메인 배경색 (시스템 배경) | `#0A192F` | R:10 G:25 B:47 | 전체 UI의 기본 배경. 전문성, 깊이감 부여. |
| **Secondary Accent** | 구조적 구분/카드 배경 | `#172B4D` | R:23 G:43 B:77 | 섹션 분리, 카드(Card) 배경, 패널 내부 배경. |
| **Text Primary** | 기본 텍스트 색상 (Body Text) | `#E6E6FA` | 밝은 라벤더 계열 | 본문 및 일반 설명 텍스트. 높은 가독성 유지. |
| **System Alert Red** | **[필수] 시스템 경고/위기** | `#8B0000` | Deep Crimson Red | *오직* 생명이나 건강에 대한 '즉각적인 위협'을 나타낼 때만 사용. (배경, 테두리, 텍스트 강조) |
| **Success Code Green** | 정상 작동/프로토콜 성공 | `#3CB371` | Medium Sea Green | 시스템 상태가 '정상(OK)'일 때의 코드 출력 또는 해결책 제시 부분에 한정. |
| **Warning Yellow** | 잠재적 위험/주의 단계 | `#FFD700` | Gold/Yellow | '주의 깊은 점검 필요'와 같은 2차적인 경고 메시지에 사용. |
| **Code Accent Cyan** | 코드 구문 강조 (Syntax Highlight) | `#64FFDA` | Light Aqua | 명령어, 변수명 등 CLI 스타일의 코드를 시각적으로 구분할 때 사용. |

---

## 2. 🅰️ 타이포그래피 시스템 (Typography System)

전문적이고 기계적인 느낌을 극대화하기 위해 모노스페이스 계열을 메인으로 채택합니다.

*   **메인 폰트:** `Source Code Pro` (또는 `Roboto Mono`)
    *   **사용 이유:** 코딩 환경에서 사용되는 폰트로, 전문적이고 기술적인 신뢰도를 즉각적으로 부여합니다.
    *   **Weight 활용:** Regular(본문), Bold(제목), Italic(코드 예시)를 명확히 구분하여 위계를 만듭니다.

| 용도 | 크기 (Desktop/Mobile 비율) | Weight | 스타일 및 역할 | 예시 텍스트 |
| :--- | :--- | :--- | :--- | :--- |
| **H1 (System Title)** | 36px / 28px | Bold | 가장 중요하고 임팩트가 큰 제목. [시스템 경고]와 결합 사용. | `CRITICAL ALERT: Defect ID E-C403` |
| **H2 (Section Header)** | 24px / 20px | SemiBold | 섹션 구분 및 핵심 원리 제시. | `Defect Analysis Protocol` |
| **Body Text** | 16px / 14px | Regular | 일반적인 설명 텍스트. 가장 높은 가독성 유지. | `...이러한 오류는 시스템의 근본적 결함을 의미합니다.` |
| **Code/ID Tag** | 14px / 12px | Regular | Defect ID, 명령어, 에러 코드 등 전문 용어에 사용. (Monospace) | `[ERR-C403]` 또는 `$ diagnose --check` |

---

## 3. 🧩 표준 컴포넌트 라이브러리 (Standard Components)

### 3.1. [System Alert Banner] - Deep Crimson Red 활용
가장 시급하고 위협적인 메시지를 전달하는 핵심 UI 요소입니다. 모든 콘텐츠의 최상단이나 결론 직전에 배치됩니다.

*   **디자인 규격:**
    *   `Width`: 100% (반응형)
    *   `Height`: 60px - 80px (필요에 따라 조정)
    *   `Background Color`: `#8B0000` (Deep Crimson Red)
    *   `Text Color`: `#FFFFFF` (White)
    *   `Border Radius`: 3px (미세한 각진 느낌 유지)
*   **구조:** `[Severity Level] | [Defect ID/Alert Title]` <br> *Body Text: System Critical Message. Immediate action required.*
*   **사용 원칙:** 이 경고가 표시되는 순간, 시청자(독자)는 현재의 '일상'이 아닌 '위기 상황'에 놓여있다고 무의식적으로 인식해야 합니다.

### 3.2. [Error Code/Diagnosis Template] - 공학적 위기감 극대화
단순한 정보 전달을 넘어, 분석 결과임을 강조하는 전문적인 프레임워크입니다.

*   **디자인 규격:**
    *   `Shape`: 직사각형 패널 (패딩 20px)
    *   `Background Color`: `#172B4D` (Secondary Accent - 미세한 어두운 배경)
    *   `Border`: 좌측 또는 상단에 `Deep Crimson Red`의 두꺼운 세로 라인 (`3px solid #8B0000`)을 필수 적용.
    *   `Typography`: Defect ID와 Error Code는 Cyan Accent를 사용하여 강조합니다.
*   **구조 예시:**
    ```
    ╔════════════════════════════════╗
    ║ [SYSTEM DIAGNOSTICS REPORT]     ║
    ╠════════════════════════════════╣
    ║ DEFECT ID: E-C403 (Cardiac Function) ║
    ║ STATUS CODE: ERROR (Code 7A2F)  ║
    ║ MESSAGE: 근육 세포의 미세 구조적 파괴가 확인되었습니다. ║
    ╚════════════════════════════════╝
    ```

### 3.3. [CLI Console Style Info Box] - 테스트 결과/보고서 프레임워크
데이터 분석 과정이나, '전문가의 진단 결과'를 제시할 때 사용합니다. 마치 컴퓨터가 스스로 계산하고 결과를 출력하는 느낌을 줍니다.

*   **디자인 규격:**
    *   `Shape`: 직사각형 패널 (패딩 15px)
    *   `Background Color`: `#0A192F` (Primary Dark - 배경과 동일하게 하여 몰입감 극대화)
    *   `Border`: 미세한 테두리만 사용하거나, 아예 경계 없이 내부 레이아웃으로 분리.
    *   `Typography`: 모든 텍스트를 코딩된 것처럼 보입니다. `Code Accent Cyan`과 `Text Primary`의 대비가 중요합니다.
*   **구조 예시:**
    ```bash
    user@onhyeon-diagnose:~/$ run_protocol --target=metabolism
    [PROCESSING...] Analyzing metabolic flux rates...
    [STATUS] -> SUCCESS: Baseline within tolerance. (Code 200)
    >>> RECOMMENDATION: Consider supplementing CoQ10. [ACTION REQUIRED]
    ```

---
**✅ 요약 및 재사용 가이드라인:**
*   **Red (`#8B0000`)**: 위기감 = 위험성 인지 (System Alert만 사용).
*   **Dark Navy (`#0A192F`)**: 전문성/신뢰도 구축 (배경, CLI 배경).
*   **Monospace:** 모든 기술적 용어와 결과물에 적용하여 권위적인 톤 유지.

</create_file>

📊 평가: 완료 — CEO님의 요청사항을 완벽하게 반영한 재사용 가능한 디자인 시스템 브리프를 성공적으로 제작했습니다.
📝 다음 단계: 이 브리프를 기반으로 실제 콘텐츠 유형(썸네일, 리스)에 적용된 **3가지 컨셉 시각화 결과물**을 즉시 제시해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\FreqTrade\assets\MiniFunnel_V2.0_DesignSystem_Brief.md
