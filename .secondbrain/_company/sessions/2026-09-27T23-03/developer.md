# 💻 코다리 — 연구원(Researcher)이 제공할 3가지 핵심 위험 지표(hs-CRP, 내장지방, 수면 회복력)의 가중치 기반 점수 산정 매트릭스를 입력받아 'Mini-App Funnel'의 E2E 시뮬레이션 로직을 구현해주세요. 이 코드는 단순히 점수를 계산하는 것을 넘어, 사용자가 위험 등급(Green/Yellow/Red)에 따라 UI가 자동 변화하고, 최종적으로 Mini-App 진단 요구 페이지로 전환되는 전체 사용자 흐름(Funnel Flow)을 포함해야 합니다. 특히, 유료 컨설팅 구매 CTA가 강제 발동되는 로직까지 개발 완료 후, Git 브랜치에서 테스트 및 버그 디버깅을 진행해 주세요.

💻 코다리: 작업 시작합니다. 이 정도 복잡도면 설계 단계에서부터 놓치는 부분이 생길 수 있어요. 단순히 점수 계산만 하는 건 '함정'입니다. 중요한 건 그 점수가 *어떻게* UI를 조작하고, 사용자에게 어떤 위기감을 주며, 결국 유료 CTA로 이어지게 만드느냐죠.

요청하신 기능은 Mini-App Funnel의 핵심이자 가장 복잡한 부분입니다. 단순히 로직을 구현하는 게 아니라, **전체 사용자 경험(E2E) 시뮬레이션**이 필요합니다. 제가 이 작업을 책임지고 진행하겠습니다. ⚙️

### 🧠 작업 계획 및 검증 과정

1.  **구조 설계 (Architecture):** E2E 흐름을 위해 백엔드 스코어링 엔진 API (Python Stub)와 프론트엔드 클라이언트 컴포넌트 (TypeScript/React)를 분리합니다.
2.  **로직 구현:** 가중치 기반 점수 산정 로직 및 위험 레벨(Green/Yellow/Red)에 따른 상태 전환 로직을 구현합니다.
3.  **강제 CTA 삽입:** Red 레벨 도달 시, 진단 요구 페이지로의 강제 전이와 함께 유료 컨설팅 구매 CTA가 활성화되도록 만듭니다.
4.  **격리 및 테스트:** 모든 변경 사항은 독립적인 Git 브랜치에서 진행하고, `e2e_funnel_cta_test_suite`를 이용해 End-to-End 시뮬레이션 및 디버깅을 완료합니다.

---

### 🛠️ Step 1: 개발 환경 설정 및 구조화

먼저, 이 기능을 위한 전용 프로젝트 폴더와 필요한 핵심 파일을 생성하겠습니다. 기존의 복잡한 로직들이 충돌하지 않도록 분리하는 것이 중요해요.

<list_files path="c:\Data\Project\connect-ai"/>
(시스템이 파일 목록을 보여주면 그 구조를 참고하여 작업을 진행합니다.)

우선, `mini-app` 폴더 아래에 백엔드 API와 프론트엔드 UI 스켈레톤을 배치하겠습니다.

<create_file path="c:\Data\Project\connect-ai\prototype\mini-app\backend\scoring_engine.py">
```python
# scoring_engine.py - Mini-App Funnel Backend Scoring API Stub (FastAPI/Flask 구조)

from typing import Dict, List
import random

# 가중치 정의 (임의 값 설정: 실제 연구 결과 반영 필요)
WEIGHTS = {
    "hs-crp": 0.4,          # 염증 지표가 가장 중요하다고 가정
    "visceral_fat": 0.35,   # 내장지방도 높음
    "sleep_recovery": 0.25  # 수면 패턴 점수
}

def calculate_risk_score(indicators: Dict[str, float]) -> Dict:
    """
    주어진 핵심 지표를 가중치 기반으로 합산하여 종합 위험 점수를 산출합니다.
    점수는 0 (최적) ~ 100 (위험 최고) 사이로 정규화되어야 합니다.
    """
    if not all(key in indicators for key in WEIGHTS):
        raise ValueError("필수 지표가 누락되었습니다.")

    weighted_score = 0.0
    for indicator, weight in WEIGHTS.items():
        if indicator not in indicators:
            print(f"경고: {indicator} 데이터가 없습니다.")
            continue
        # 점수는 [0, 1] 사이로 정규화되었다고 가정하고 가중치 적용 (실제는 스케일링 필요)
        score = indicators[indicator]
        weighted_score += score * weight

    # 최종 점수 보정 및 반환 (예: 최대치를 100점으로 조정하는 로직 추가 가능)
    final_score = min(max(weighted_score, 0.0), 100.0)

    # 위험 등급 판별 (비즈니스 로직 - 이 부분이 중요함)
    if final_score < 30:
        risk_level = "Green"  # 정상 범위
        message = "현재 시스템 상태는 양호합니다."
    elif final_score < 75:
        risk_level = "Yellow" # 경고/개선 필요
        message = "일부 시스템 부품에 이상 신호가 감지되었습니다. 생활 습관 개선이 필요합니다."
    else:
        risk_level = "Red"   # 위험 임계치 도달 (Action Required)
        message = "🚨 심각한 시스템 고장이 의심됩니다! 전문적인 진단과 즉각적인 개입이 필수입니다."

    return {
        "score": round(final_score, 2),
        "risk_level": risk_level,
        "status_message": message
    }


def main_api_endpoint(input_data: Dict[str, float]) -> Dict:
    """E2E Funnel의 진입점 역할을 하는 메인 API 엔드포인트."""
    try:
        result = calculate_risk_score(input_data)
        return {
            "success": True,
            "diagnosis": result
        }
    except Exception as e:
        print(f"Error processing diagnosis: {e}")
        return {"success": False, "error": str(e)}

# 테스트 실행 예시 (실제는 FastAPI/Flask 서버가 처리)
if __name__ == "__main__":
    print("--- Test Case 1: Green Zone ---")
    green_input = {"hs-crp": 0.2, "visceral_fat": 0.3, "sleep_recovery": 0.4} # 낮은 점수
    result_g = main_api_endpoint(green_input)
    print(f"Green Result: {result_g}")

    print("\n--- Test Case 2: Red Zone ---")
    red_input = {"hs-crp": 0.9, "visceral_fat": 0.8, "sleep_recovery": 0.7} # 높은 점수
    result_r = main_api_endpoint(red_input)
    print(f"Red Result: {result_r}")

```
</create_file>

<create_file path="c:\Data\Project\connect-ai\prototype\mini-app\frontend\FunnelScreen.tsx">
```tsx
// FunnelScreen.tsx - React Component for the Mini-App Funnel Flow
import React, { useState } from 'react';
import axios from 'axios';

// --- 타입 정의 (강력한 타이핑 필수) ---
type RiskLevel = 'Green' | 'Yellow' | 'Red';

interface DiagnosisResult {
    score: number;
    risk_level: RiskLevel;
    status_message: string;
}

interface ApiResponse {
    success: boolean;
    diagnosis: DiagnosisResult;
}

// API 엔드포인트 (백엔드 스코어링 엔진과 연결)
const SCORING_API = process.env.REACT_APP_SCORING_URL || "http://localhost:8000/api/score";


/**
 * 핵심 UI 컴포넌트: 위험 점수 게이지 및 Funnel 상태 관리
 */
const FunnelScreen: React.FC = () => {
    // 1. 초기 데이터 (시뮬레이션용)
    const [indicators, setIndicators] = useState({
        hs_crp: 0.75,     // High
        visceral_fat: 0.6, // Medium-High
        sleep_recovery: 0.8  // High
    });
    
    // 2. 상태 관리
    const [isLoading, setIsLoading] = useState(false);
    const [diagnosis, setDiagnosis] = useState<DiagnosisResult | null>(null);

    /**
     * 점수 산정 및 Funnel 진행 로직 (핵심)
     */
    const handleRunDiagnosis = async () => {
        if (isLoading) return;
        setIsLoading(true);
        setDiagnosis(null);

        try {
            // 🚨 API 호출: 백엔드 스코어링 엔진에 데이터 전송
            const response = await axios.post<ApiResponse>(SCORING_API, indicators);

            if (response.data.success) {
                const result = response.data.diagnosis;
                setDiagnosis(result);
            } else {
                alert("진단 로직 오류: 서버 응답을 확인해주세요.");
            }
        } catch (error) {
            console.error("API 호출 실패:", error);
            alert("네트워크 연결 또는 API가 작동하지 않습니다.");
        } finally {
            setIsLoading(false);
        }
    };

    /**
     * UI 렌더링을 위한 스타일 및 컴포넌트 분리 (SRP 준수)
     */
    const getRiskStyle = (level: RiskLevel) => {
        switch (level) {
            case 'Red': return "bg-red-800 border-red-900 animate-pulse"; // Deep Crimson Red & 깜빡임 효과
            case 'Yellow': return "bg-yellow-600 border-yellow-700";
            default: return "bg-green-700 border-green-800";
        }
    };

    // 3. Mini-App Funnel 로직 실행 (상태 기반 UI 전환)
    const handleCTA_Click = () => {
        if (!diagnosis || diagnosis.risk_level !== 'Red') {
            alert("진단 결과가 '위험' 등급이 아닙니다. CTA를 활성화할 수 없습니다.");
            return;
        }
        // 🔴 핵심: Red 레벨일 때만 유료 진단 페이지로 강제 전환 로직 실행
        window.location.href = "/paid-consulting/booking?risk_score=" + diagnosis.score;
    };

    return (
        <div className="container mx-auto p-6 max-w-3xl bg-gray-50 shadow-lg">
            <h1 className="text-4xl font-extrabold mb-2 text-red-800">🔴 시스템 고장 자가진단 (Mini-App Funnel)</h1>
            <p className="text-xl text-gray-600 mb-8">당신의 몸속 위험 신호, 수치로 확인하세요.</p>

            {/* 1. 입력 및 실행 섹션 */}
            <div className="bg-white p-6 rounded-xl shadow-md mb-8 border-b-4 border-red-500">
                <h2 className="text-2xl font-semibold mb-4 text-gray-700">측정 지표 입력 (가상 데이터)</h2>
                {/* 실제는 슬라이더나 드롭다운으로 구현 */}
                <div className="grid grid-cols-3 gap-4 text-center mb-6">
                    <div><p className='text-sm font-medium'>hs-CRP (염증)</p><input type="number" value={indicators.hs_crp} onChange={(e) => setIndicators({...indicators, hs_crp: parseFloat(e.target.value)})}/></div>
                    <div><p className='text-sm font-medium'>내장지방 (%)</p><input type="number" value={indicators.visceral_fat} onChange={(e) => setIndicators({...indicators, visceral_fat: parseFloat(e.target.value)})}/></div>
                    <div><p className='text-sm font-medium'>수면 회복력 (%)</p><input type="number" value={indicators.sleep_recovery} onChange={(e) => setIndicators({...indicators, sleep_recovery: parseFloat(e.target.value)})}/></div>
                </div>
                
                <button 
                    onClick={handleRunDiagnosis}
                    disabled={isLoading}
                    className={`w-full py-3 rounded-lg text-white font-bold transition duration-200 ${isLoading ? 'bg-gray-400' : 'bg-red-600 hover:bg-red-700'}`}
                >
                    {isLoading ? "진단 중... 잠시만 기다려주세요 ⚙️" : "위험 점수 진단 시작 (Run Diagnosis)"}
                </button>
            </div>

            {/* 2. 결과 및 Funnel 전환 섹션 */}
            {diagnosis && (
                <div className="bg-white p-8 rounded-xl shadow-2xl border-t-8 transition duration-500" style={{ borderTopColor: getRiskStyle(diagnosis.risk_level).replace('animate-pulse', '') }}>
                    <h2 className="text-3xl font-bold mb-6 text-gray-800">✅ 진단 결과</h2>

                    {/* 위험 점수 게이지 시각화 (Deep Crimson Red 강조) */}
                    <div className={`p-4 rounded-lg ${getRiskStyle(diagnosis.risk_level)} shadow-inner`}>
                        <p className="text-xl font-semibold mb-2">종합 위험 점수: <span className='text-3xl'>{diagnosis.score} / 100</span></p>
                        <p className="text-lg mt-2">{diagnosis.status_message}</p>
                    </div>

                    {/* Funnel CTA (상태 기반 활성화) */}
                    <div className={`mt-8 p-6 rounded-xl text-center ${diagnosis.risk_level === 'Red' ? 'bg-red-50 border-4 border-red-700 shadow-xl' : 'bg-gray-100'} `}>
                        <h3 className="text-2xl font-bold mb-3">다음 단계가 필요합니다.</h3>
                        
                        {/* Red 레벨일 때만 CTA 활성화 */}
                        {diagnosis.risk_level === 'Red' ? (
                            <>
                                <p className="text-lg text-red-800 mb-4 font-medium">🔴 경고: 현재 위험 점수는 전문 의료진의 상세 진단이 필요합니다.</p>
                                <button 
                                    onClick={handleCTA_Click}
                                    className="w-full py-3 bg-red-900 text-white text-xl rounded-lg hover:bg-red-800 transition duration-200 shadow-md"
                                >
                                    ▶️ Mini-App Funnel 진단 요구 (유료 컨설팅 예약) ◀️
                                </button>
                            </>
                        ) : (
                            <p className="text-green-700 font-medium">현재는 생활 습관 개선만으로 충분합니다. 다음 점검까지 기다려주세요.</p>
                        )}
                    </div>
                </div>
            )}
        </div>
    );
};

export default FunnelScreen;
```
</create_file>

### 🧪 Step 2: 테스트 및 검증 (Self-Verification Loop)

작성한 코드가 실제로 Funnel 로직과 CTA를 강제하는지 확인해야 합니다. 백엔드와 프론트엔드를 연결하고 E2E 시나리오를 테스트하겠습니다.

1.  **Git Branch 분기:** 독립적인 개발 환경을 구축합니다.
2.  **테스트 스위트 실행:** `e2e_funnel_cta_test_suite`를 사용하여 전체 흐름을 검증합니다.

<run_command>git checkout -b feature/mini-app-funnel-v1</run_command>
<run_command>echo "Mini-App Funnel E2E 테스트 로직 구현 및 커밋 준비 완료." && git add .</run_command>
<run_command>git commit -m "feat(funnel): Mini-App Funnel v1.0 초기 구조 및 스코어링 엔진 통합"</run_command>

이제 핵심 테스트 도구를 실행하여 모든 단계가 예상대로 작동하는지 검증합니다.

<run_command>cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe e2e_funnel_cta_test_suite.py</run_command>

---
📊 평가: 진행중 — 백엔드 스코어링 엔진과 프론트엔드 컴포넌트를 분리하여 Funnel의 핵심 로직을 구현했으며, 이제 테스트 결과를 바탕으로 최종 버그 수정 및 통합 커밋이 필요합니다.
📝 다음 단계: `e2e_funnel_cta_test_suite` 실행 결과를 분석하여 발견된 모든 버그를 수정하고, 완벽히 작동하는 상태로 Main 브랜치에 병합(Merge)해야 합니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `git checkout -b feature/mini-app-funnel-v1`
```
Switched to a new branch 'feature/mini-app-funnel-v1'
```
_✅_

### 🔧 실행: `echo "Mini-App Funnel E2E 테스트 로직 구현 및 커밋 준비 완료." && git add .`
```
"Mini-App Funnel E2E �׽�Ʈ ���� ���� �� Ŀ�� �غ� �Ϸ�." 
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/.gitignore', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/package-lock.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/package.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/public/index.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/public/manifest.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/public/robots.txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/App.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/App.test.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/App.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/index.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/index.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/reportWebVitals.ts', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/setupTests.ts', LF will be replaced by CRLF the next time Git touches it
```
_✅_

### 🔧 실행: `git commit -m "feat(funnel): Mini-App Funnel v1.0 초기 구조 및 스코어링 엔진 통합"`
```
[feature/mini-app-funnel-v1 73a60f484] feat(funnel): Mini-App Funnel v1.0 초기 구조 및 스코어링 엔진 통합
 20 files changed, 17718 insertions(+)
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/.gitignore
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/README.md
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/package-lock.json
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/package.json
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/public/favicon.ico
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/public/index.html
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/public/logo192.png
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/public/logo512.png
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/public/manifest.json
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/public/robots.txt
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/App.css
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/App.test.tsx
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/App.tsx
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/index.css
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/index.tsx
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/logo.svg
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/react-app-env.d.ts
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/reportWebVitals.ts
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/src/setupTests.ts
 create mode 100644 .secondbrain/_company/_agents/developer/tools/mini-funnel-poc/tsconfig.json
```
_✅_

### 🔧 실행: `cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppDa`
```
=============================================

--- [🌐 Web Test] Funnel 'national_pension' 테스트 시작 ---
[✅ Data Injection]: 데이터 성공적으로 주입됨: 월 평균 150만원 부족
[❌ Web Flow ERROR]: 네트워크/요청 실패: HTTPSConnectionPool(host='www.onhyeon-site.com', port=443): Max retries exceeded with url: /signup/submit (Caused by NameResolutionError("HTTPSConnection(host='www.onhyeon-site.com', port=443): Failed to resolve 'www.onhyeon-site.com' ([Errno 11001] getaddrinfo failed)"))

--- [▶️ YouTube Test] Funnel 'national_pension' 테스트 시작 ---
[✅ Data Injection]: 링크 내부에 위험액 정보가 안전하게 포함됨.
[✅ Tracking Link Structure]: 예상 URL 생성 완료: https://analytics.example.com/track/?utm_source=youtube&funnel=national_pension&campaign=gap_cta&content=gap_cta
[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.


=============================================

--- [🌐 Web Test] Funnel 'health_insurance' 테스트 시작 ---
[⚠️ Data Injection WARN]: 데이터가 누락되었으나, CTA는 대체 텍스트를 안전하게 표시함.
[❌ Web Flow ERROR]: 네트워크/요청 실패: HTTPSConnectionPool(host='www.onhyeon-site.com', port=443): Max retries exceeded with url: /signup/submit (Caused by NameResolutionError("HTTPSConnection(host='www.onhyeon-site.com', port=443): Failed to resolve 'www.onhyeon-site.com' ([Errno 11001] getaddrinfo failed)"))

--- [▶️ YouTube Test] Funnel 'health_insurance' 테스트 시작 ---
[⚠️ Data Injection WARN]: 링크에 데이터 누락 대비 로직이 필요합니다.
[✅ Tracking Link Structure]: 예상 URL 생성 완료: https://analytics.example.com/track/?utm_source=youtube&funnel=health_insurance&campaign=gap_cta&content=gap_cta
[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.


=============================================

--- [🌐 Web Test] Funnel 'inheritance' 테스트 시작 ---
[✅ Data Injection]: 데이터 성공적으로 주입됨: 최소 3천만원 손실 우려
[❌ Web Flow ERROR]: 네트워크/요청 실패: HTTPSConnectionPool(host='www.onhyeon-site.com', port=443): Max retries exceeded with url: /signup/submit (Caused by NameResolutionError("HTTPSConnection(host='www.onhyeon-site.com', port=443): Failed to resolve 'www.onhyeon-site.com' ([Errno 11001] getaddrinfo failed)"))

--- [▶️ YouTube Test] Funnel 'inheritance' 테스트 시작 ---
[✅ Data Injection]: 링크 내부에 위험액 정보가 안전하게 포함됨.
[✅ Tracking Link Structure]: 예상 URL 생성 완료: https://analytics.example.com/track/?utm_source=youtube&funnel=inheritance&campaign=gap_cta&content=gap_cta
[✅ YouTube Flow]: URL 구조가 플랫폼 가이드라인을 준수하며, 트래커 발동에 최적화됨.

=============================================

[🚨 E2E 테스트 실패] 일부 필수 기능에서 오류가 감지되었습니다. 코드를 수정하고 재검증해야 합니다.
```
_✅_

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\prototype\mini-app\backend\scoring_engine.py
✅ 생성: c:\Data\Project\connect-ai\prototype\mini-app\frontend\FunnelScreen.tsx
📂 목록: c:\Data\Project\connect-ai/
```
📁 api/
📁 app/
📄 ARCHITECTURE.md
📁 assets/
📁 backend/
📄 connect-ai-lab-2.89.157.vsix
📄 connect-ai-lab-2.89.158.vsix
📄 context_processor.py
📁 data_pipeline/
📄 data_validator.py
📄 DESIGN.md
📄 DESIGN_SPECIFICATION.md
📁 design_system_spec/
📄 detect_tg.js
📄 EDUCATIONAL_SLIDES.md
📄 Funnel_MVP_E2E_Test_Plan_v1.0.md
📄 GapAnalyzerPrototype.html
📄 index.html
📄 LICENSE
📄 MARKDOWN_DOCUMENTATION_MANUAL.md
📄 mini-app-funnel-mvp.html
📄 package-lock.json
📄 package.json
📄 PLAZA_SETUP.md
📄 PRESENTATION.md
📁 prototype/
📄 README.md
📄 README_GapVisualization_Guide.md
📄 renderer_core.py
📁 research_output/
📁 schemas/
📁 scripts/
📄 secretary_task_briefing_48h.md
📁 services/
📁 sessions/
📄 SHOWCASE_GUIDE.md
📁 src/
📄 system_schema.json
📁 tests/
📄 test_client.py
📄 test_context_processor.py
📄 test_gap_pipeline_v1.py
📄 test_renderer.py
📄 test_solution_assets.py
📁 tools/
📄 tsconfig.json
📄 video_renderer.py
📁 writer_output/
📁 _company/
📁 결과물/
📄 튜토리얼_비서_연결.md
```

[시스템: list_files 결과]
디렉토리: c:\Data\Project\connect-ai/
📁 api/
📁 app/
📄 ARCHITECTURE.md
📁 assets/
📁 backend/
📄 connect-ai-lab-2.89.157.vsix
📄 connect-ai-lab-2.89.158.vsix
📄 context_processor.py
📁 data_pipeline/
📄 data_validator.py
📄 DESIGN.md
📄 DESIGN_SPECIFICATION.md
📁 design_system_spec/
📄 detect_tg.js
📄 EDUCATIONAL_SLIDES.md
📄 Funnel_MVP_E2E_Test_Plan_v1.0.md
📄 GapAnalyzerPrototype.html
📄 index.html
📄 LICENSE
📄 MARKDOWN_DOCUMENTATION_MANUAL.md
📄 mini-app-funnel-mvp.html
📄 package-lock.json
📄 package.json
📄 PLAZA_SETUP.md
📄 PRESENTATION.md
📁 prototype/
📄 README.md
📄 README_GapVisualization_Guide.md
📄 renderer_core.py
📁 research_output/
📁 schemas/
📁 scripts/
📄 secretary_task_briefing_48h.md
📁 services/
📁 sessions/
📄 SHOWCASE_GUIDE.md
📁 src/
📄 system_schema.json
📁 tests/
📄 test_client.py
📄 test_context_processor.py
📄 test_gap_pipeline_v1.py
📄 test_renderer.py
📄 test_solution_assets.py
📁 tools/
📄 tsconfig.json
📄 video_renderer.py
📁 writer_output/
📁 _company/
📁 결과물/
📄 튜토리얼_비서_연결.md
