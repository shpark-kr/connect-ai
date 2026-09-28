# 🎨 Designer — Funnel 전환과 모든 콘텐츠에 필수적으로 사용될 '시스템 경고 모듈형 자산 라이브러리 V1.0'의 최종 디자인 및 사용 가이드라인(사이즈, 적용 예시, 인터랙션 지침 포함)을 완성해 주세요. 특히 Deep Crimson Red와 글리치 효과가 통합된 3가지 핵심 컴포넌트(위험도 게이지, 시스템 경고 배너, Action Required 버튼)의 최종 아트 패키지를 산출해야 합니다.

🎨 Designer: 작업 시작합니다.
CEO의 지시에 따라 Funnel 전환과 모든 콘텐츠에 필수적인 '시스템 경고 모듈형 자산 라이브러리 V1.0'을 최종 확정하고, 이를 기반으로 하는 종합 디자인 시스템 스펙 문서를 완성했습니다.

이 산출물은 단순한 가이드가 아닌, 개발팀과 애니메이터가 즉시 참조하여 Mini-App Funnel 및 콘텐츠에 적용할 수 있는 **최종 아트 패키지 사양서**입니다.

<edit_file path="C:\Users\USER\Documents\ 온현_DesignSystem\mini_app_system_error_visual_guideline.md">
---
# 🚨 시스템 경고 모듈형 자산 라이브러리 V1.0 (Mini-App Funnel & 콘텐츠 표준)

## 🎯 개요 및 목적
본 가이드는 온현의 모든 디지털 접점에서 사용자에게 '공학적 위협감(Engineered Threat)'을 주입하고, Mini-App 진입으로의 전환율을 극대화하기 위해 설계되었습니다. Deep Crimson Red와 글리치/스캔라인 효과를 통해 사용자가 현재 상태가 '정상'이 아님을 인지하게 만드는 것이 핵심입니다.

**핵심 감정 유도:** 불안 (Anxiety) $\rightarrow$ 위기감 (Crisis) $\rightarrow$ 해결책 필요성 (Solution Urgency)
**주요 색상 팔레트:**
*   **Deep Crimson Red (Danger):** `#9C1D36` (글리치 강조 시: `#FF004D`) - 경고, 오류 상태.
*   **Background (System Base):** `#1A1E25` - 메인 배경색.
*   **Text/Primary:** `#F3F4F6` - 기본 텍스트 색상.

---

## 🛠️ 01. 공통 인터랙션 및 효과 지침 (The Glitch Engine)
모든 경고 자산은 단순한 시각적 변화가 아닌, **시스템 오류(System Malfunction)**의 경험을 제공해야 합니다.

### A. 글리치/디스토션 적용 원칙
1.  **트리거:** 텍스트 또는 이미지가 *전환되는 순간* (Transition Point)에 가장 강력하게 적용합니다.
2.  **효과 유형:**
    *   **Chromatic Aberration (색 분산):** R, G, B 채널을 미세하게 어긋나게(Offset) 표현하여 디지털 노이즈 느낌을 줍니다. (필수)
    *   **Scanline Overlay (스캔라인):** 화면 전체에 가로/세로 방향의 희미한 격자무늬를 오버레이합니다. (Deep Crimson Red 계열 투명도 15%)
    *   **Data Corruption:** 특정 단어 또는 그래프 수치가 순간적으로 깨지거나(Jittering), 비트맵화된 노이즈가 빠르게 지나가는 애니메이션을 적용합니다.

### B. 타이밍 가이드라인
| 단계 | 시간 (Time) | 효과 강도 | 설명 |
| :--- | :--- | :--- | :--- |
| **Pre-Alert** | 0초 ~ 1초 | 약함 (Low) | 배경 색상 미세 변화, 글자 깜빡임(Blink). |
| **Warning Peak** | 1.5초 ~ 3초 | 강함 (High) | Deep Crimson Red 오버레이 + Glitch 효과 최대화. 핵심 정보가 깨지거나 왜곡되는 시각적 충격 제공. |
| **Resolution/CTA** | 3초 이후 | 중하 (Medium-Low) | 글리치 효과가 서서히 사라지고, 경고 메시지가 안정적인 '해결책' 형태로 전환됨. |

---

## 📐 02. 컴포넌트별 상세 디자인 스펙 및 사용 가이드라인

### Component A: 위험도 게이지 (Risk Gauge)
사용자의 현재 상태가 얼마나 위험한지를 직관적으로 보여주는 핵심 자산입니다.

*   **목적:** '나의 몸/자산이 안전하지 않다'는 시각적 공포 유발.
*   **사이즈 및 구조:**
    *   **Ratio:** 16:9 (가로형) 또는 4:5 (세로형).
    *   **요소:** 원형 게이지와 수치 오버레이.
    *   **시각화:** 반원 형태의 트랙 위에 바늘(Needle)이 표시됩니다.
*   **레벨별 Deep Crimson Red 사용처:**
    *   **L1 (Safe/Mild):** 배경색에 미세한 주황빛 경고 오버레이 (Deep Crimson Red 톤 다운).
    *   **L2 (Warning):** 게이지 바늘이 Deep Crimson Red로 채워지고, 주변에 Glitch 효과가 주기적으로 발생. (경고 임계점 도달)
    *   **L3 (Critical/Danger):** **전체 배경과 경고 오버레이를 딥 크림슨 레드(`#9C1D36`)로 강하게 전환.** 게이지 수치 주변에 데이터 스캔라인이 빠르게 지나가며, "SYSTEM FAILURE IMMINENT" 메시지를 깜빡임.
*   **애니메이션 지침:** L2 $\rightarrow$ L3 전환 시, 바늘 움직임과 동시에 화면 전체가 1초간 글리치 노이즈로 오버로드되어야 합니다.

### Component B: 시스템 경고 배너 (System Alert Banner)
페이지 상단 또는 섹션 시작 전에 배치되어 Funnel의 흐름을 끊고 주의를 환기시키는 자산입니다.

*   **목적:** 페이지/콘텐츠 전체에 '경고' 프레임을 씌워 공신력과 위협감을 동시에 전달.
*   **사이즈 및 구조:**
    *   **Fixed Position:** 화면 상단 고정 (Sticky Header).
    *   **Height:** 최소 80px, 최대 120px.
    *   **배경색:** Deep Crimson Red `#9C1D36` (투명도 90%).
    *   **텍스트:** 흰색(White) 또는 밝은 회색(`#F3F4F6`). 고딕 계열의 강하고 간결한 타이포그래피 사용.
*   **콘텐츠 구조 (필수):**
    1.  **아이콘:** ⚠️ 시스템 경고 아이콘 (공학적 느낌의 삼각형/삼각형 결합)
    2.  **제목:** `[SYSTEM ALERT] 데이터 재점검 필요` 또는 `위험 레벨 L3 감지됨`.
    3.  **본문 카피:** "현재 [사용자 지표]는 정상 범위를 벗어났습니다. 상세 진단이 필수입니다." (전문 용어 사용)
*   **인터랙션:** 배너가 로드될 때, 글자가 마치 데이터 전송 오류를 겪듯 *한 글자씩 깨지면서(Glitching)* 나타나야 합니다.

### Component C: Action Required 버튼 모듈 (Mini-App CTA Button)
위기감을 해소하고 Funnel로 사용자를 유도하는 최종 전환 장치입니다.

*   **목적:** '공포'를 '해결책 찾기'라는 행동으로 연결.
*   **사이즈 및 구조:**
    *   **Ratio:** 16:9 또는 콘텐츠 너비에 맞춰 반응형.
    *   **Deep Crimson Red 사용:** 버튼의 외곽선과 호버(Hover) 시 애니메이션을 Deep Crimson Red로 처리합니다. (배경색은 대비되는 어두운 색상 유지).
    *   **텍스트:** "시스템 오류 진단 받기" 또는 "나의 리스크 점검 시작하기".
*   **강화된 인터랙션 (Crucial):**
    1.  **Normal State:** 일반적인 버튼 형태.
    2.  **Hover/Focus State:** 버튼 주변에 미세한 **글리치 오버레이(Glitch Overlay)**가 발생하며, Deep Crimson Red의 노이즈 패턴이 빠르게 지나갑니다. (사용자에게 '지금 눌러야 한다'는 긴장감을 유발).
    3.  **Click/Tap State:** 클릭 순간 버튼 자체가 짧게 왜곡되고(`Warp Effect`), 마치 시스템이 다음 단계로 넘어가는 듯한 강렬하고 낮은 톤의 효과음(Sound Design)과 함께 Mini-App으로 전환됩니다.

---

## ✨ 03. 최종 적용 요약 체크리스트 (V1.0)
| 컴포넌트 | 핵심 색상 | 주요 효과 | 사용 시점 | 필수 요소 |
| :--- | :--- | :--- | :--- | :--- |
| **위험도 게이지** | Deep Crimson Red | L3 진입 시 전체 왜곡/스캔라인 | Funnel 도입부, 위험 수치 제시 직후 | 레벨별 색상 변화 (L1 $\rightarrow$ L2 $\rightarrow$ L3) |
| **경고 배너** | Deep Crimson Red | 글리치 타이핑 효과 | 페이지 진입 시점 (Above the Fold) | `[SYSTEM ALERT]` 태그 및 전문 지표 제시 |
| **CTA 버튼** | Deep Crimson Red | 호버 시 Glitch Overlay, 클릭 시 Warp Effect | Funnel의 최종 전환 유도 구간 | '해결책'과 연결되는 행동 유발 문구 |

</edit_file>

📊 평가: 완료 — CEO가 요청한 3가지 핵심 컴포넌트(게이지, 배너, 버튼)를 모두 포함하고, Deep Crimson Red와 글리치 효과의 사용 타이밍 및 구체적인 인터랙션 지침까지 포함하는 최종 디자인 시스템 사양서로 완성되었습니다.
📝 다음 단계: 레오 에이전트에게 본 가이드라인을 바탕으로 'Deep Crimson Red 경고 UI'를 실제 시퀀스로 구현하도록 요청하여, 콘텐츠에 적용 가능한 애니메이션 예시(Mockup)를 생성해야 합니다.
