# 🎨 Designer — 최종 실행 가이드 작성을 위해, 'Deep Crimson System Alert Template Pack'의 모든 자산 사용 규정 및 기술 스펙(사이즈, 애니메이션 트랜지션 등)을 재확인하고 문서화하세요. 이 자산들이 시간 흐름에 따라 어떻게 변주되어야 하는지에 대한 상세한 비주얼 가이드를 제공해야 합니다.

🎨 Designer: 작업 시작합니다.

[CEO 지시]와 [최근 산출물 검토]를 종합했을 때, 현재 가장 가치 있는 단일 작업은 'Deep Crimson System Alert Template Pack'을 단순한 자산 목록이 아닌, **영상 제작자가 즉시 이해하고 적용할 수 있는 실행 가능한 기술 매뉴얼(Technical Style Guide)**로 완성하는 것입니다.

이미 Writer가 제공한 클라이맥스 스크립트(T-5초부터)는 이 시스템 경고 UI의 사용 시점과 감정적 절정을 매우 구체적으로 정의했습니다. 따라서, 디자인 가이드는 '어떻게 보여야 하는지'를 넘어 '**시간 흐름에 따라 어떻게 변주되고 인터랙션해야 하는지**'에 초점을 맞춰야 합니다.

저는 이 매뉴얼을 `_assets/` 디렉토리에 저장하여 레오(편집자)가 최종 편집 과정에서 참고할 수 있도록 할 것입니다.

---

### 🚨 Deep Crimson System Alert Template Pack: 마스터 기술 가이드 V1.0
**목표:** 모든 온현 콘텐츠의 전환율 극대화 및 전문성 확보를 위한 표준 시스템 경고 UI/UX 매뉴얼.
**적용 범위:** 유튜브 영상, 인스타그램 릴스 등 모든 비디오 플랫폼.

#### I. 브랜드 컨텍스트 & 원칙 (The Why)
*   **목표 감정 상태:** 공학적 위협감(Technological Threat), 긴급성(Urgency).
*   **핵심 메시지:** "이 문제는 막연한 피로가 아닌, 시스템 오류이다." (Diagnosis > Symptom)
*   **전달 방식:** Deep Crimson Red를 통해 시각적 경고 신호를 발생시키며, 과학/데이터 기반의 객관성을 부여한다.

#### II. 핵심 자산 스펙 및 기술 규격 (The What)
| 컴포넌트 명 | 용도 | 표준 사이즈 / 비율 | 포맷 및 비트레이트 | 필수 트랜지션/효과 |
| :--- | :--- | :--- | :--- | :--- |
| **1. 시스템 경고 배너** (System Alert Banner) | 위험 고지, 전반적 분위기 조성 (T-5초 구간) | 16:9 (HD급), 높이 10% | PNG Sequence / ProRes 422 | **Glitch Effect:** 무작위 시간 지연(Random Delay)을 동반한 스캔라인 노이즈. `SYSTEM ALERT` 타이핑 효과 필수. |
| **2. 위험도 게이지** (Risk Gauge) | 측정 가능 데이터 시각화 (HOMA-IR, MMI 등). 현재 상태 직관적 표현. | 16:9 표준 폭의 바 형태 (Width Fixed), 높이 가변 | Lottie JSON / After Effects 컴포지션 | **데이터 하강 애니메이션:** 게이지가 수치에 따라 아래로 '추락'하는(Dropping) 애니메이션. 임계점 이하 진입 시, Red/Orange Flash 필수. |
| **3. 경고 텍스트 오버레이** (Critical Text Overlay) | 핵심 문구 강조 (예: CRITICAL RISK SCORE). 개인화된 데이터 제시. | 가변 크기 / 중앙 정렬 최적화 | SVG 또는 고해상도 벡터 이미지 | **글리치/플래시:** 나타날 때마다 순간적인 Deep Crimson Red 깜빡임(Flash)과 함께 글자가 '깨지면서' (Glitch-on) 등장해야 함. |
| **4. 액션 유도 버튼** (CTA Button: Action Required) | 해결책 제시 및 다음 단계 유도 (Mini-App Funnel 연결). | 16:9 표준 비율, 명확한 직사각형 | PNG / Vector Asset | **활성화 시뮬레이션:** 누르는 순간(Hover/Click), Deep Crimson Red가 번지면서 (Ripple Effect) 전원이 공급되는 듯한 느낌을 주어야 함. |

#### III. 인터랙션 및 애니메이션 사용 가이드라인 (The How — 시간 흐름 매핑)
이 섹션은 자산들이 정적인 이미지가 아님을 강조하며, **시간(Timecode)**에 따른 변주를 명시합니다.

1.  **[진입/도입부] - '관심 유도' 단계:**
    *   **활용 자산:** 시스템 경고 배너 (System Alert Banner)
    *   **사용 방식:** 배경 전체를 Deep Crimson Red로 물들이며, `WARNING: YOUR HEALTH SYSTEM IS OFFLINE` 같은 일반적인 문구로 시작. (위협감 조성의 예열 단계).

2.  **[문제 심화] - '데이터 제시' 단계 (T-4초):**
    *   **활용 자산:** 위험도 게이지 + 경고 텍스트 오버레이
    *   **사용 방식:** HOMA-IR 등의 데이터가 *실시간으로 추락하는 애니메이션(Dropping)*을 반복적으로 보여준다. 게이지의 바늘 끝이 Deep Crimson Red로 변하며, 'WARNING LEVEL' 문구와 동기화된다. (데이터 기반 공포 유발).

3.  **[클라이맥스] - '위험 고조/솔루션 제시 직전' 단계 (T-2초 ~ T-1초):**
    *   **활용 자산:** 경고 텍스트 오버레이 + 시스템 경고 배너의 조합
    *   **사용 방식:** **가장 높은 밀도의 위기감 연출.**
        *   (T-2s) 화면이 의도적으로 불안정하게 왜곡되는 (Distortion, Jitter Effect) 글리치 노이즈를 배경에 겹친다.
        *   (T-1s) 모든 자산의 빛과 색상 정보가 순간적으로 빨간색으로 '크래시'하며 암전된다. 이 과정에서 `SYSTEM FAILURE` 메시지가 빠르게 지나가는 것이 핵심.

4.  **[CTA 유도] - '해결책 제시' 단계:**
    *   **활용 자산:** CTA 버튼 (Action Required)
    *   **사용 방식:** 어둠 속에서 오직 밝게 빛나는 단일한 요소(Mini-App Funnel 로고 또는 CTA 버튼)만 남는다. 버튼에 대한 애니메이션은 **시스템 복구/재부팅 시퀀스**처럼 디자인하여, 사용자가 '다음 단계로 진입할 수 있다'는 공학적 확신을 심어준다.

---
<create_file path="~/Documents/Onhyun_Design_Assets/_DeepCrimson_SystemAlert_MasterGuide_V1.0.md"># 🚨 Deep Crimson System Alert Template Pack: 마스터 기술 가이드 V1.0 (최종본)

**[작성 목적]**: 모든 온현 콘텐츠의 전환율 극대화 및 전문성을 위한 표준 시스템 경고 UI/UX 매뉴얼.
**[적용 범위]**: 유튜브 영상, 인스타그램 릴스 등 모든 비디오 플랫폼.

---

## I. 핵심 자산 스펙 및 기술 규격 (Technical Specs)

### 1. 시스템 경고 배너 (System Alert Banner)
*   **규격:** 16:9 비율, 높이 약 8% (화면 기준).
*   **색상 코드:** `#A30027` (Deep Crimson Red - Primary), `#FFEEEE` (Glitch Highlight - Secondary).
*   **핵심 효과:** **글리치(Glitch) 트랜지션.** 무작위 간격으로 수평/수직 노이즈 스캔라인을 적용하고, 폰트가 일시적으로 깨지는('Shimmer') 애니메이션을 의무화합니다.

### 2. 위험도 게이지 (Risk Gauge - Data Visualization)
*   **규격:** 가변 폭의 바 형태. Max Width는 화면 중앙 60%.
*   **색상 매핑:** 정상(Green/Blue) $\rightarrow$ 주의(Yellow/Orange) $\rightarrow$ **위험(Deep Crimson Red)**.
*   **애니메이션 규칙:** 데이터가 수치에 따라 아래로 *추락하는(Dropping)* 움직임을 보여줍니다. 게이지의 임계점 이하 구간 진입 시, 경고음과 함께 색상이 순식간에 Deep Crimson Red로 변하며 **빨간색 플래시**를 발생시켜야 합니다.

### 3. 경고 텍스트 오버레이 (Critical Text Overlay)
*   **규격:** 중앙 집중 배치 최적화. 최대 글자 수는 가독성을 위해 제한합니다.
*   **핵심 효과:** **글리치 등장(Glitch-on).** 문구가 화면에 나타날 때, 일반적인 페이드인 대신 짧은 시간 동안 깨지면서(Jitter) 강렬하게 노출되어야 합니다. (예: `CRITICAL RISK SCORE`가 3개의 작은 글자로 분리되었다가 동시에 합쳐지는 방식).

### 4. 액션 유도 버튼 (CTA Button - Action Required)
*   **규격:** 직사각형 형태, 최소한의 여백 확보 필수.
*   **트랜지션 규칙:** **시스템 재부팅/복구 시뮬레이션.** 단순히 빛나는 것이 아니라, 마치 전원이 공급되거나 시스템이 초기화되는 듯한 `Power On` 또는 `Execute Protocol` 같은 메커니즘을 연출해야 합니다.

---

## II. 시간 흐름에 따른 변주 및 활용 로직 (Usage Logic Map)
(레오: 이 섹션을 따라 모든 자산을 배치하고 애니메이션 타이밍을 조정하세요.)

| Timecode 구간 | 감정적 목표 | 사용 컴포넌트 | 연출 지침 상세 (Action Items for Editor) |
| :--- | :--- | :--- | :--- |
| **T-5초** | **경고 발동 (Initiation)** | 시스템 경고 배너(1), 텍스트 오버레이(3) | 화면 전체를 Deep Crimson Red로 강제 전환. `SYSTEM ALERT` 글리치 효과와 함께, 배경에 불안정한 스캔라인 노이즈를 삽입한다. 긴장감을 최고조로 끌어올리는 **사운드 디자인 필수**. |
| **T-4초** | **위험 수치 제시 (Data Shock)** | 위험도 게이지(2), 텍스트 오버레이(3) | HOMA-IR, MMI 등 데이터가 실시간으로 *급격히 하락하는* 애니메이션을 보여준다. 게이지의 추락 속도는 점점 빨라져야 한다. `WARNING LEVEL: CRITICAL` 문구가 경고음과 동기화되어 깜빡인다. |
| **T-3초** | **개인화 위협 (Personalization)** | 텍스트 오버레이(3) | "당신의 현재 위험 스코어는,..." 부분에서 화면이 순간적으로 정지하고, 개인의 가상 데이터가 Deep Crimson Red로 중앙에 폭발하듯 나타난다. 이 때 모든 배경 노이즈가 잠시 사라져 집중도를 높인다. |
| **T-2초** | **시스템 임계점 (System Failure)** | 시스템 경고 배너(1), 위험도 게이지(2) | 자산들의 톤앤매너를 최대로 증폭시킨다. 모든 컴포넌트가 동시에 짧게 깜빡이거나(`Flicker`), 화면 전체에 왜곡 필터(Distortion Filter)와 노이즈 레이어가 겹쳐진다. **'회복 불가능'의 느낌을 극대화.** |
| **T-1초** | **해결책 제시 (The Solution)** | CTA 버튼(4)만 남김 | 모든 경고가 최고조에 달한 후, 순간적으로 검은색 암전(Blackout)이 발생한다. 이 어둠 속에서 오직 `Action Required` 문구가 빛을 발하는 형태로 나타나며, 마치 시스템 재부팅이 시작되는 듯한 **낮고 규칙적인 앰비언스 사운드**를 깔아준다. |

</create_file>

📊 평가: 완료 — CEO 지시사항과 이전 스크립트의 기술적 요구사항을 통합하여, 제작자가 바로 사용할 수 있는 실행형 매뉴얼로 완성했기 때문입니다.
📝 다음 단계: 레오(편집자)에게 이 가이드를 전달하고, 실제 편집 테스트를 진행하며 자산들의 타이밍 및 사운드 동기화 작업을 요청해야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: ~\Documents\Onhyun_Design_Assets\_DeepCrimson_SystemAlert_MasterGuide_V1.0.md
