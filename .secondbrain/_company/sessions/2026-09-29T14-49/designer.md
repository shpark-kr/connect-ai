# 🎨 Designer — Researcher가 제공한 기술적 블로커 리스트와 '공학적 위기감' 콘셉트를 기반으로, Deep Crimson Red 테마의 오류 코드(Error Code) 및 시스템 경고 UI 컴포넌트 팩을 디자인하세요. 특히, 진단 단계와 해결책 제시 단계에 필요한 시각적 흐름(Visual Flow)과 애니메이션 스펙을 포함해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시 사항을 최우선 목표로 설정하고, Researcher가 제공한 '공학적 위기감' 매트릭스를 기반으로 MiniFunnel 전환율 극대화를 위한 **[Critical System Alert UI 컴포넌트 패키지]**를 설계하겠습니다.

이 디자인은 단순한 경고창(Alert)을 넘어, 시청자에게 **①문제 인식 $\rightarrow$ ②진단 수용 $\rightarrow$ ③솔루션 행동 유도**라는 3단계의 공학적 설득 흐름(Visual Funnel)을 강제하는 것을 목표로 합니다.

---

### 🖥️ [Component Pack] 시스템 오류 시각화 스펙 (V1.0)

#### 1. 브랜드 및 스타일 가이드라인 재정립
*   **주요 컬러 팔레트:** Deep Crimson Red (`#8B0000` - 경고/위기), Technical Black (`#1A1A2E` - 배경), System Gold (`#FFD700` - 중요 정보 강조).
*   **타이포그래피:** 시스템 글꼴 (예: `SF Mono`, `Consolas`)를 사용하여 코딩 콘솔 같은 느낌을 주어 전문성을 극대화합니다.
*   **핵심 디자인 언어:** 다크 모드 기반, 글래스모피즘/네온 효과의 '디지털 오류' 텍스처 오버레이.

#### 2. 핵심 컴포넌트 및 구조 (Layout Structure)

| Component | 역할 | 내용물 예시 | 개발 스펙 가이드 |
| :--- | :--- | :--- | :--- |
| **`System-Container`** | 전체 컨테이너/배경 | 오류 발생 시 화면 전체를 덮는 어두운 오버레이. | 배경에 미세한 노이즈(Grain)와 Red Glitch 효과 (CSS Keyframe: `glitch-effect`) 적용. 크기: `w-full h-screen` |
| **`Alert-Header`** | 위기감 조성 시작점 | 오류 코드(`[PROCESS_TIMEOUT_E-301]`) 및 긴급 경고 타이틀. | 글자색은 금색(Gold), 배경은 Crimson Red의 반투명 오버레이. 가장 먼저, 강하게 눈에 띄어야 함. |
| **`Diagnosis-Module`** | 문제 정의/설득 | Researcher가 제시한 '시스템 실패 진단명' 및 스토리텔링 Hook 문구. | Structured Box 형태로 배치. 일반 설명 대신 '분석 보고서(Analysis Report)' 느낌으로 구성 (좌측: 코드, 우측: 해석). |
| **`Solution-Panel`** | 해결책/CTA 유도 | MiniFunnel 가입 유도, 다음 단계 안내. | 가장 안정적인 색상 (Dark Navy 또는 블랙)을 사용하여 '안정화'를 시각적으로 전달하고 CTA 버튼에만 Crimson Red 사용. |

#### 3. 필수 애니메이션 및 상태 전이 로직 (The Visual Flow)
가장 중요한 것은 **단순한 전환이 아니라, 단계별 위기감 고조**입니다. 아래는 MiniFunnel 진입 경로를 가정한 시간 기반(Time-Based) State Machine 스펙입니다.

| Step | 동작/상태 변화 | 시간 타이밍 (Timing) | 애니메이션 스펙 / CSS 지시 | 개발 로직 구현 포인트 |
| :---: | :--- | :--- | :--- | :--- |
| **A. 초기 진입** | 시스템 오류 발생 (`[SYSTEM_RESOURCE_404]`) | T+0ms (즉각적) | `Alert-Header`가 강렬한 플래시(Flash)와 함께 화면을 덮음. 모든 텍스트에 글리치 효과(`text-shadow: 2px 0 red, -2px 0 blue;`). 배경에서 날카로운 경고음 오버레이. | `useEffect` 후 즉각적인 DOM 업데이트 및 CSS 애니메이션 트리거. |
| **B. 진단 메시지** | 문제의 본질 설명 (Diagnosis-Module) | T+1,500ms (약 1.5초 지연) | Red 플래시가 약해지고(Fade Out), `Diagnosis-Module`이 부드럽게 나타남(`opacity: 0` $\rightarrow$ `opacity: 1`). 코드가 박스 안에 '타자기'처럼 한 글자씩 입력되는 효과 (`typing-effect` keyframe). | 지연 로직 구현. 이 단계에서 사용자에게 충분한 시간(3초)을 주어 공감대를 형성해야 함. |
| **C. 해결책 제시** | 시스템 안정화 및 CTA 유도 (Solution-Panel) | T+3,500ms (약 2초 지연) | `Diagnosis-Module`의 경고 색상이 점차 금색(Gold)으로 변하며 '진단 완료' 느낌을 줌. 배경 노이즈가 줄어들며 안정화된 듯한 미세한 빛(Glow) 효과 추가. CTA 버튼에만 Crimson Red로 긴장감 유지. | 가장 중요한 전환 타이밍. 이 지점에서 **불안감 $\rightarrow$ 희망/해결책**으로의 감정적 반전을 극대화해야 함. |

#### 4. 구현 상세 스펙 (Code Snippet Concept - Tailwind/React)
```jsx
// Deep Crimson Red 테마 기반 Alert Header 컴포넌트 구조 예시
const ErrorAlertHeader = ({ code, title }) => {
  return (
    <div className="absolute inset-0 flex items-center justify-center z-50 bg-[#8B0000]/90 animate-pulse">
      <div className="p-8 rounded-xl shadow-2xl text-center max-w-3xl border-4 border-red-700 backdrop-blur-[1px] bg-black/60">
        {/* 오류 코드 Display */}
        <h1 className={`text-5xl font-mono tracking-widest mb-2 animate-typing`}>
          ERROR: {code} 
        </h1>
        {/* 긴급 메시지 */}
        <p className="text-3xl text-red-300 font-bold mt-4">
          ⚠️ CRITICAL SYSTEM ALERT: {title}
        </p>
      </div>
    </div>
  );
};

// (추가 개발 가이드) Transition Logic 예시
/* 
   useEffect(() => {
     // T+1500ms 후, AlertHeader를 fadeOut하고 DiagnosisModule을 fadeIn 하는 로직 필요.
     setTimeout(() => {
        setIsAlertActive(false); // Header 사라짐 (Red Glitch -> Black/Navy)
        setDiagnosisData(researcherData); // 다음 콘텐츠 모듈 표시 시작
     }, 1500);
  }, []);
*/
```

---
📊 평가: 완료 — CEO 지시에 맞춰 기술적 블로커를 활용한, 개발 가능한 수준의 UI 컴포넌트 패키지와 애니메이션 스펙을 구체적으로 제시했습니다. 이 산출물만으로 MiniFunnel 전환 퍼널의 디자인 기반이 완성되었습니다.
📝 다음 단계: Developer에게 위 스펙과 구조화된 에셋(폰트, 컬러 코드)을 전달하고, 실제 코딩 및 인터랙티브 테스트를 진행해야 합니다.
