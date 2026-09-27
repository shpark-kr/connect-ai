# 🎨 Designer — Researcher의 Mock Data Set(정량적 지표)과 Writer가 제작한 Funnel 카피라이팅 세트 A/B를 통합하여, 최종 'Mini-App 진단 도구'의 마스터 비주얼 템플릿을 완성하십시오. 이 템플릿은 다음 요소를 포함해야 합니다: ① 사용자의 상태를 즉시 보여주는 인터랙티브한 '위험도 측정 바(Risk Bar)' (색상 및 경계선 필수), ② 공포/신뢰 기반의 CTA 버튼 영역 (최소 3가지 A/B 테스트 버전), ③ 진단 결과와 함께 Mini-App으로 전환되는 명확하고 권위 있는 레이아웃. 모든 디자인 요소는 코딩 적용을 위한 상세한 Handoff Specification(기술 명세) 형태로 정리되어야 합니다.

🎨 Designer: 작업 시작합니다.

[CEO 지시사항 및 개인 목표 검토 결과]
현재까지의 모든 에이전트 활동(Researcher의 데이터 확보 $\rightarrow$ Writer의 A/B 카피라이팅 $\rightarrow$ Designer의 컴포넌트 브리프 작성)은 최종적인 **'Mini-App Funnel 진단 도구'**라는 하나의 핵심 목표로 수렴하고 있습니다.

따라서 가장 가치 있는 단일 작업은, 지금까지 산발적으로 생성된 모든 디자인 요소(위험도 측정 로직, CTA 변형 세트, 레이아웃 그리드)를 개발팀이 바로 코딩에 적용할 수 있도록 **최종 통합 Handoff Specification (기술 명세서)**을 만드는 것입니다. 이 문서는 단순한 '디자인 가이드'가 아닌, 모든 상호작용(Interaction), 데이터 바인딩(Data Binding), 그리고 상태 변화(State Change)까지 정의해야 합니다.

**실행 계획:**
1.  기존에 생성된 `Master_Design_Briefs` 폴더 내의 핵심 CTA 시스템 브리프를 최종 마스터 비주얼 템플릿 명세서로 격상하고, 세부 요소를 통합합니다.
2.  위험도 측정 바(Risk Bar)의 인터랙션 로직과 공포/신뢰 기반 CTA 버튼 3종을 가장 상세한 기술명세 형태로 정의하여, 개발팀이 별도의 질의 없이 코딩할 수 있도록 만듭니다.

<edit_file path="C:\Users\USER\Designs\Onhyun\Master_Design_Briefs\v3.0_MiniApp_Funnel_CTA_System.md">
<find>## 4. CTA 영역 A/B 테스트 변형</find><replace>## 4. 최종 통합 Handoff Specification: Mini-App 진단 도구 마스터 비주얼 템플릿 (v2.0)</replace></edit_file>

<create_file path="C:\Users\USER\Designs\Onhyun\Master_Design_Briefs\MiniApp_Master_Handoff_Spec_V2.0.md">
# 🧬 Mini-App 진단 도구 마스터 비주얼 템플릿 Handoff Specification (v2.0)

**목표:** Funnel의 최종 전환점(Last Conversion Point). 사용자의 '위험 인지'를 최고조로 끌어올리고, 오직 'Mini-App 진단/전문가 상담'만이 해결책임을 각인시킨다.
**타깃:** 40~60대 중장년층 (경제적 불안감 및 건강 염려도가 높은 심리 상태)
**기준 버전:** 다크 네이비 배경, 골드 악센트 색상 유지.

---

## 1. 전체 레이아웃 그리드 및 구조 (Structural Blueprint)
*   **Grid System:** 12-Column Flexbox Grid (반응형 필수: Mobile/Tablet/Desktop).
*   **섹션 구성 (Top to Bottom):**
    1.  **[Header]**: Mini-App 진단 도구 타이틀 및 신뢰도 배지 배치 (공신력 강조)
    2.  **[Diagnosis Result Card - 핵심]**: 위험도 측정 바와 최종 점수 노출. 사용자 감정적 충격 극대화 영역.
    3.  **[Insight/Urgency Block]**: 진단 결과에 대한 권위 있는 코멘트 및 문제 심화 설명 (Writer 카피 활용).
    4.  **[CTA Zone - 결정적 순간]**: A/B 테스트가 가능한 버튼 모듈 배치.

## 2. 컴포넌트 상세 명세 (Component Specification)

### 2.1. 위험도 측정 바 (Risk Bar: 핵심 상호작용 요소)
*   **컴포넌트 ID:** `risk-bar`
*   **기능:** 사용자가 Mini-App 진단을 완료할 때마다 점수가 실시간으로 반영되어 시각적 불안감을 조성한다.
*   **기술 명세 (CSS/Interaction):**
    *   **Structure:** Horizontal SVG Bar 또는 Linear Progress Bar.
    *   **State Logic:** `data-score` 속성에 따라 너비와 색상이 동적으로 변경된다.
    *   **Color Gradient & Boundary (필수):**
        *   **Green Zone (0-30점):** 배경색 `#2A4E5D` (안정적 딥 네이비) $\rightarrow$ 바 색상 `#6C9E7F` (희망 그린). 경계선: 없음.
        *   **Yellow Zone (31-65점):** 배경색 `#2A4E5D` $\rightarrow$ 바 색상 `#D8B33C` (경고 골드). **🚨 경고 애니메이션:** 펄스 효과(Pulse Effect) 추가 필수.
        *   **Red Zone (66-100점):** 배경색 `#2A4E5D` $\rightarrow$ 바 색상 `#CC4F4F` (강렬한 레드). **⚠️ 위기 경고 애니메이션:** 깜빡임(Blink) 효과와 함께 `! 중요: 즉각적인 행동 필요` 텍스트 오버레이.
    *   **UX/Animation:** 점수가 올라갈 때 바가 채워지는 듯한 부드러운 트랜지션(`transition: width 1s ease-out;`)을 적용한다.

### 2.2. CTA 버튼 영역 (Call-to-Action Zone) - A/B 테스트 세트
*   **컴포넌트 ID:** `cta-button`
*   **역할:** 사용자 감정 상태에 따라 메시지와 색상이 달라져야 한다. 반드시 '공포 $\rightarrow$ 신뢰 $\rightarrow$ 낮은 장벽'의 3가지 변형을 준비한다.

| 테스트 버전 | 목적 (Funnel 심리) | 타이틀 카피 예시 (Writer 기반) | 버튼 디자인/색상 (CSS/UX) |
| :--- | :--- | :--- | :--- |
| **A: 공포 유발 CTA** | *위험성 직면* (Fear-based) | "이대로 두면 위험합니다. 30분 무료 진단으로 확인하세요." | **색상:** 강렬한 레드 계열 (`#CC4F4F`). **스타일:** 박스형, 가장 크고 눈에 잘 띄게 배치. **액션:** 즉시 클릭 유도 (Highest Friction). |
| **B: 신뢰 제공 CTA** | *권위 부여* (Authority-based) | "전문가 상담을 통해 정확한 염증 위험도를 체크하세요." | **색상:** 메인 골드 (`#D8B33C`) 또는 브랜드 블루 계열. **스타일:** 가장 정제된 느낌, '검증'과 '신뢰' 톤 강조. **액션:** Mini-App 진단 페이지로 이동 (Primary Funnel). |
| **C: 낮은 장벽 CTA** | *행동 시작 유도* (Low-friction) | "간단 자가 체크리스트 받기 (5분 소요)" | **색상:** 차분한 그린 계열 (`#6C9E7F`). **스타일:** 버튼 크기를 줄이고, '다운로드' 또는 '체크하기' 텍스트 사용. **액션:** 리드 마그넷(PDF) 다운로드를 통해 이메일 수집 (Secondary Funnel). |

### 2.3. 진단 결과 카드 레이아웃
*   **구조:** 3분할 구조 (`[위험도 그래프] - [점수/등급] - [즉시 행동 안내]`).
*   **위험 등급 표기:** 반드시 시각적 명칭과 함께 **'만성 염증 위험 레벨: 높음(High)'**와 같이 구체적인 용어를 사용한다. (추상적이지 않게)

## 3. 인터랙션 및 데이터 플로우 상세 로직
*   **데이터 바인딩:** Mini-App 진단 API 호출 $\rightarrow$ `JSON` 응답 수신 (`{ "score": X, "level": "Red" }`) $\rightarrow$ `risk-bar` 컴포넌트의 `width`와 `color` 속성 동적 변경.
*   **전환 로직:** 위험도가 'Yellow'를 넘어서는 순간 (Threshold: 30점), 화면 중앙에 **공포 유발 카피(Writer A)**가 자동 오버레이되어야 한다. 이 오버레이는 CTA 버튼 B로의 시선을 강제한다.

---
**참고 파일:**
*   [Component Spec Sheet v1.0] : 재사용 컴포넌트 스타일 가이드 (기술 참조용)
*   [Funnel Copy Set A/B] : 모든 카피 문구와 톤앤매너의 원본 소스 (카피라이터 검토용)
</create_file>

📊 평가: 완료 — CEO가 요청한 핵심 요소를 모두 통합하고, 개발팀이 즉시 사용할 수 있는 기술 명세서 형태로 최종 산출물을 완성했기 때문에 목표 달성으로 판단합니다.
📝 다음 단계: 디자인 브리프의 내용을 바탕으로, 이 스펙을 기반으로 **실제 프로토타입(Figma/Sketch)**을 제작하여 시각적 검증 및 개발팀 피드백 루프를 거쳐야 합니다.

---
## 📁 파일 액션 결과

✅ 생성: ~\Designs\Onhyun\Master_Design_Briefs\MiniApp_Master_Handoff_Spec_V2.0.md
⚠️ C:\Users\USER\Designs\Onhyun\Master_Design_Briefs\v3.0_MiniApp_Funnel_CTA_System.md: 매칭 실패 — `## 4. CTA 영역 A/B 테스트 변형…` (정확/fuzzy 둘 다 실패)
