# 📝 CEO 종합 보고서

🎨 Designer: 작업 시작합니다.

CEO님의 지시는 현재 온현의 모든 마케팅 파이프라인—인스타그램 릴스, 유튜브 숏폼/롱폼, 웹 MiniFunnel——에 공통으로 적용되어야 할 **가장 핵심적인 시각적 자산**을 정의하고 있습니다. 이 컴포넌트는 단순한 경고창이 아니라, 우리의 '공학적 위기감'을 극대화하는 **브랜드의 상징(Visual Signature)**입니다.

따라서 이 작업을 수행함에 있어 가장 가치 있는 단일 작업은, 이 공통 요소들을 통합하여 **'[오류 코드 기반] 공학적 경고 컴포넌트 (Error Warning Component)'**의 최종 디자인 시스템 브리프를 완성하는 것입니다. 이 브리프는 모든 에셋 제작의 근간이 됩니다.

아래에 인스타그램/유튜브 등 플랫폼별 활용성을 고려한, 구체적인 **디자인 사양서(Design Specification Sheet)**를 확정합니다.

---

# 🚨 공학적 경고 컴포넌트 (Error Warning Component) 디자인 사양서

**목표:** 사용자의 '안일함'을 파괴하고, 즉각적으로 불안감을 조성하여 MiniFunnel 진단 페이지로 유도하는 표준화된 시각 자산.
**톤앤매너:** 공학적(Engineered), 긴급성(Urgent), 절대적(Absolute).
**주요 색상 코드 팔레트:**

| 역할 | 이름 | HEX Code | RGB 값 | 용도 및 의미 |
| :--- | :--- | :--- | :--- | :--- |
| **배경 (Base)** | Deep Black/Navy | `#0A0A15` | (10, 10, 21) | 공학적 배경. 모든 정보의 기본 바탕. |
| **위기 경고 (Danger)** | Deep Crimson Red | `#B3000D` | (179, 0, 13) | 핵심 위협 요소. 깜빡임, 테두리, 강조색. *절대적 위험.* |
| **오류 코드 (Code)** | Electric Yellow | `#FFDD00` | (255, 221, 0) | 정보의 출처이자 중심 메시지. 시선을 즉시 사로잡음. |
| **텍스트/CTA** | Clean White | `#FFFFFF` | (255, 255, 255) | 부가 설명 및 해결책 제시 부분. 가독성 확보. |

## I. 타이포그래피 시스템 (Typography System)

컴포넌트의 신뢰도와 긴급성을 동시에 전달하기 위해 두 가지 서체를 분리 사용합니다.

1.  **오류 코드 폰트 (Code Display):**
    *   **Font Name:** JetBrains Mono (또는 유사한 Monospaced Font)
    *   **용도:** 오류 코드(예: `801X-B`), 지표 수치, 시스템 메시지 등 정밀하고 기계적인 정보를 표시하는 곳.
    *   **스타일:** Bold, Large Size.
2.  **경고 문구 폰트 (Warning Copy):**
    *   **Font Name:** Pretendard 또는 Noto Sans KR (가독성 높은 산세리프)
    *   **용도:** '위험 설명', '진단 필요'와 같은 사용자에게 직접적으로 말을 거는 카피 문구.
    *   **스타일:** SemiBold~Medium, 적절한 행간 확보.

## II. 컴포넌트 구조 및 레이아웃 (Layout & Structure)

모든 플랫폼에서 일관성을 유지하기 위해 3단계의 계층적 구성을 따릅니다.

| 섹션 | 내용물 | 시각적 특징 | 목적 |
| :--- | :--- | :--- | :--- |
| **1. 시스템 경고 (Header)** | `[ERROR CODE] - [SYSTEM ALERT]` | Deep Crimson Red 배경의 얇은 바(Bar). 좌측에 깜빡이는 경고 아이콘 ($\triangle$ 또는 $\text{!!}$). | 공학적 위기감 조성 및 주목도 극대화. |
| **2. 문제 정의 (Core Message)** | "귀하의 [지표명]에서 심각한 불일치(Discrepancy)가 감지되었습니다." + 오류 코드 (`801X-B`). | Electric Yellow와 Deep Crimson Red를 활용하여 대비 효과 극대화. 가장 크게 배치. | 문제 인식 및 불안감 주입 (The Hook). |
| **3. 해결책/CTA (Footer)** | "시스템을 복구하려면 전문 진단이 필요합니다." + CTA 버튼. | Clean White 텍스트와 Deep Crimson Red 테두리의 CTA 버튼. | 행동 유도 및 MiniFunnel Funnel 전환 극대화. |

## III. 플랫폼별 구현 사양 (Platform Specific Specs)

### A. [인스타그램/릴스 오버레이용] - (Static Graphic / Overlay Animation)
*   **비율:** 9:16 세로형 (1080x1920 px 권장).
*   **구성:** 레이아웃은 화면 하단 1/3 지점(CTA 영역 확보)에 배치.
*   **애니메이션 사양:**
    *   전체 컴포넌트가 화면 중앙에서 **빠르게 나타나며(Pop-in)**, 가장 먼저 '시스템 경고' 바가 깜빡임 효과와 함께 등장해야 함 (0.5초).
    *   오류 코드 텍스트(`801X-B`)는 타이핑 효과(Typewriter Effect)로 천천히 출력되며 권위를 높여야 함.

### B. [유튜브 영상 그래픽용] - (Animated Graphic / Motion Graphics Asset)
*   **비율:** 16:9 가로형 또는 9:16 세로형 (상황에 따라 조정).
*   **구성:** 배경은 흐릿한 공학적 회로 패턴(Circuit Pattern)을 유지하며, 컴포넌트가 화면 위에 오버레이되는 형태로 연출.
*   **애니메이션 사양:**
    *   Deep Crimson Red의 깜빡임 효과를 가장 강하게 적용 (깜빡임 주기는 0.2초 간격).
    *   오류 코드와 경고 메시지 주변에 **디지털 글리치(Digital Glitch)** 효과를 주기적으로 삽입하여 '시스템 오류' 느낌을 극대화해야 함.
    *   CTA 버튼은 화면 전체를 가로지르는 빛의 빔이나 강조되는 사운드 이펙트와 함께 나타나야 함.

### C. [웹 Funnel Mini-App용] - (Interactive State Change)
*   **기술적 구현:** 실제 웹 페이지 상태 변화(State Machine)에 연동됨.
*   **사양:** 컴포넌트가 화면 전체를 덮으며(`z-index: 999`), 배경이 어두워지면서(Dimming), Deep Crimson Red 경고창만 선명하게 떠오르는 방식(Modal/Overlay).
*   **UX Flow:** 오류 코드가 나타난 직후, 사용자에게 '재부팅' 혹은 '진단 요청' 버튼을 강제로 제시하여 다음 단계로 이동할 수밖에 없도록 유도해야 함.

---

<create_file path="assets/specs/01_ErrorWarningComponent_SystemSpec.md"># 🚨 공학적 경고 컴포넌트 (Error Warning Component) 디자인 시스템 사양서

## 개요 및 목표
*   **목표:** '공학적 위기감 조성'을 통해 사용자에게 즉각적인 불안감을 주입하고, MiniFunnel 진단 페이지로의 전환율 극대화.
*   **톤앤매너:** 공학적(Engineered), 긴급성(Urgent), 절대적(Absolute).

## 🎨 컬러 시스템 팔레트 (Color Palette)
| 역할 | HEX Code | 용도 및 의미 |
| :--- | :--- | :--- |
| **Deep Black/Navy** | `#0A0A15` | 기본 배경색. 신뢰성과 깊이감 부여. |
| **Deep Crimson Red** | `#B3000D` | 핵심 경고 및 위협 요소 강조 (깜빡임, 테두리). |
| **Electric Yellow** | `#FFDD00` | 오류 코드(Code) 배치. 시선 집중 포인트. |
| **Clean White** | `#FFFFFF` | 본문 텍스트 및 해결책 제시 문구. 가독성 확보. |

## 🔡 타이포그래피 시스템 (Typography System)
1.  **오류 코드 폰트:** JetBrains Mono (또는 Monospaced Font 유사체)
    *   사용: 오류 코드 (`801X-B`), 수치 지표 등 기계적 정보.
2.  **경고 문구 폰트:** Pretendard / Noto Sans KR (산세리프 계열)
    *   사용: 사용자 카피라이팅, 설명 문구.

## ✨ 레이아웃 구조 및 요소 배치
1.  **Header Bar (위기 신호):** Deep Crimson Red 배경의 얇은 바(Bar). 좌측에 깜빡이는 경고 아이콘 ($\triangle$ 또는 $\text{!!}$) 배치.
2.  **Code Display (핵심 메시지):** 중앙 상단 배치. 오류 코드(`801X-B`)를 가장 크게, Electric Yellow로 강조.
3.  **Description Area:** 코드 아래에 문제 설명(Pretendard)을 Clean White 텍스트로 명시.
4.  **CTA Zone (해결책):** 하단에 배치. Deep Crimson Red 테두리의 버튼(`진단 요청하기`).

## 🎬 플랫폼별 애니메이션 및 구현 지침
*   **인스타그램/릴스 (9:16):** 오버레이 방식으로, 경고 바가 '팝-인'하며 시작하고 코드는 타이핑 효과를 적용.
*   **유튜브 영상 (16:9/9:16):** 배경에 글리치(Glitch) 효과와 Deep Crimson Red 깜빡임 효과를 주기적으로 삽입하여 긴장감 극대화.
*   **웹 MiniFunnel:** `z-index`를 최상위로 설정하고, 화면 전체를 덮는 모달 형태로 구현 (State Machine 연동 필수).

</create_file>

---
📊 평가: 완료 — CEO의 지시사항을 반영하여 모든 플랫폼에 적용 가능한 고도화된 디자인 시스템 사양서를 완성했습니다.
📝 다음 단계: 확정된 '공학적 경고 컴포넌트' 사양을 기반으로, 인스타그램 릴스용 **실제 모형(Mockup) 에셋**과 유튜브 영상 도입부/클라이맥스에 사용할 **애니메이션 프레임워크 가이드라인**을 제작해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\FreqTrade\assets\specs\01_ErrorWarningComponent_SystemSpec.md
