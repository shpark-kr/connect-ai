# 💻 코다리 — Designer로부터 전달받을 '시스템 오류 보고서' 및 '진단 테스트 페이지'의 프로토타입(Mock-up) 구축을 시작해주세요. React/Tailwind CSS 기반으로, Deep Navy와 Crisis Red를 활용한 핵심 컴포넌트 3가지(1. Defect ID 표시 박스, 2. 증상 데이터 입력 필드, 3. 최종 보고서 출력 영역)의 더미 데이터를 이용한 기능을 구현하고, 개발된 코드 구조를 문서화해주세요.

💻 코다리: 작업 시작합니다.

CEO님의 지시사항을 확인했습니다. '시스템 오류 보고서'와 '진단 테스트 페이지'의 프로토타이핑은 회사 정체성(Deep Navy/Crisis Red 기반의 공학적 권위성)을 구현하는 핵심 단계입니다. 단순히 UI를 나열하는 수준으로는 부족하고, Designer님이 정의한 상태 기계(State Machine)의 **느낌**과 **흐름**을 코드로 구현해야 합니다.

따라서 React와 TypeScript를 사용하여 재사용 가능한 컴포넌트 단위로 구조화하겠습니다. 기존 작업물과의 일관성을 위해 프로젝트 폴더는 `mini-funnel-proto`로 설정하고, 핵심 로직은 다음 3가지 컴포넌트에 집중합니다.

1.  **`DefectIdCard`**: 가장 먼저 사용자의 시선을 붙잡을 '시스템 오류' 표시 장치.
2.  **`SymptomInputForm`**: 전문적인 데이터 입력의 느낌을 주는 폼.
3.  **`ReportOutputArea`**: 최종적으로 시스템이 내리는 권위 있는 진단 보고서.

먼저 프로젝트 폴더를 설정하고 필요한 컴포넌트들을 생성하겠습니다. 모든 코드는 Tailwind CSS와 TypeScript를 사용하며, Deep Navy (`#0A1931`)와 Crisis Red (`#C5222D`)가 메인 컬러로 적용됩니다.

### 🛠️ 파일 구조 및 구현 (React/TypeScript)

<create_file path="mini-funnel-proto/src/components/DefectIdCard.tsx">
import React from 'react';

interface DefectIdCardProps {
  defectId: string;
  description: string;
}

const DefectIdCard: React.FC<DefectIdCardProps> = ({ defectId, description }) => {
  return (
    <div className="p-6 bg-[#1a2d4c] border-l-8 border-red-700 shadow-xl rounded-lg transition duration-300 hover:shadow-[0_0_20px_rgba(197,34,45,0.5)]">
      <div className="flex items-center mb-3">
        {/* 시스템 경고 아이콘 (🚨) */}
        <svg className="w-8 h-8 text-red-500 mr-3 animate-pulse" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.13-.655 1.73-2.182 1.73-3.8l0-3.8c0-1.618-.6-3.145-1.73-3.8z" />
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01" />
        </svg>
        <h2 className="text-xl font-mono text-[#C5222D] tracking-widest uppercase">
          DEFECT ID: {defectId}
        </h2>
      </div>
      <p className="text-sm text-gray-300 mb-4 border-l-2 pl-3 border-[#C5222D]">
        {description}
      </p>
      <div className="mt-4 p-3 bg-black/20 rounded text-xs font-mono">
          [STATUS: CRITICAL - IMMEDIATE INTERVENTION REQUIRED]
      </div>
    </div>
  );
};

export default DefectIdCard;
</create_file>

<create_file path="mini-funnel-proto/src/components/SymptomInputForm.tsx">
import React, { useState } from 'react';

interface SymptomInputFormProps {
    onAnalyze: (data: any) => void;
}

const SymptomInputForm: React.FC<SymptomInputFormProps> = ({ onAnalyze }) => {
    const [symptoms, setSymptoms] = useState({
        bodyPainLevel: 3, // 1-5 scale
        sleepQualityScore: 60, // %
        digestionIssueDays: 7,
        recentDietChange: false,
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        const { name, value, type, checked } = e.target;
        setSymptoms(prev => ({
            ...prev,
            [name]: type === 'checkbox' ? checked : (type === 'number' ? parseFloat(value) : value),
        }));
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        console.log("Sending analysis data:", symptoms);
        onAnalyze(symptoms);
    };

    return (
        <div className="p-8 bg-[#0A1931] border border-[#C5222D]/50 rounded-xl shadow-inner max-w-md">
            <h3 className="text-lg font-mono mb-6 text-gray-200 border-b border-[#C5222D]/30 pb-2">
                [DATA INGESTION MODULE] - 증상 데이터 입력
            </h3>

            <form onSubmit={handleSubmit} className="space-y-6">
                {/* 1. 통증 레벨 */}
                <div>
                    <label htmlFor="bodyPainLevel" className="block text-sm font-mono mb-2 text-[#C5222D] tracking-wider">
                        Body Pain Index (BPI) [1-5]:
                    </label>
                    <input 
                        id="bodyPainLevel" 
                        name="bodyPainLevel" 
                        type="range" 
                        min="1" max="5" step="1" 
                        value={symptoms.bodyPainLevel} 
                        onChange={handleChange} 
                        className="w-full h-2 bg-[#1a2d4c] rounded-lg appearance-none cursor-pointer range-lg [&::-webkit-slider-thumb]:bg-[#C5222D]"
                    />
                    <div className="flex justify-between text-xs text-gray-400 mt-1"><span>1 (Mild)</span><span>5 (Severe)</span></div>
                </div>

                {/* 2. 수면 품질 */}
                 <div>
                    <label htmlFor="sleepQualityScore" className="block text-sm font-mono mb-2 text-[#C5222D] tracking-wider">
                        Sleep Quality Score (%) [0-100]:
                    </label>
                    <input 
                        id="sleepQualityScore" 
                        name="sleepQualityScore" 
                        type="number" 
                        min="0" max="100" 
                        value={symptoms.sleepQualityScore} 
                        onChange={handleChange} 
                        className="w-full p-3 bg-[#1a2d4c] border border-gray-700 rounded text-white focus:ring-[#C5222D] focus:border-[#C5222D]"
                    />
                </div>

                {/* 3. 식단 변화 여부 */}
                 <div className="flex items-center justify-between">
                    <input 
                        id="recentDietChange" 
                        name="recentDietChange" 
                        type="checkbox" 
                        checked={symptoms.recentDietChange} 
                        onChange={handleChange} 
                        className="h-5 w-5 text-[#C5222D] bg-[#1a2d4c] border-gray-600 focus:ring-[#C5222D]"
                    />
                    <label htmlFor="recentDietChange" className="text-sm font-mono text-gray-300">
                        최근 식단 변화 감지 (Y/N)
                    </label>
                </div>

                {/* Submit Button */}
                <button 
                    type="submit" 
                    className="w-full py-3 mt-8 bg-[#C5222D] hover:bg-red-700 text-white font-bold uppercase tracking-widest transition duration-150 shadow-lg shadow-red-900/50"
                >
                    진단 분석 요청 (Run Analysis)
                </button>
            </form>
        </div>
    );
};

export default SymptomInputForm;
</create_file>

<create_file path="mini-funnel-proto/src/components/ReportOutputArea.tsx">
import React from 'react';

interface ReportOutputAreaProps {
  reportData: any; // Mock data structure
}

const ReportOutputArea: React.FC<ReportOutputAreaProps> = ({ reportData }) => {
  return (
    <div className="p-8 bg-[#0A1931] border-4 border-[#C5222D]/80 rounded-xl shadow-[0_0_30px_rgba(197,34,45,0.3)]">
      <h3 className="text-2xl font-mono mb-6 text-white uppercase tracking-widest border-b pb-2 border-[#C5222D]/50">
        [SYSTEM ANALYSIS COMPLETE] - 최종 보고서 출력 영역
      </h3>

      {/* 핵심 진단 결과 (가장 중요한 부분) */}
      <div className="mb-8 p-6 bg-[#1a2d4c] rounded-lg border-l-8 border-green-500/90">
        <h4 className="text-xl font-mono mb-2 text-green-400 tracking-wider">✅ DIAGNOSIS SUMMARY:</h4>
        <p className="text-gray-300 leading-relaxed">{reportData.summary}</p>
      </div>

      {/* 상세 결과 섹션 */}
      <div className="space-y-6 text-sm text-gray-200">
        <h4 className="text-lg font-mono text-[#C5222D] border-b border-[#C5222D]/30 pb-1">
          > [CORE DEFECT PROFILE] (Priority: High)
        </h4>
        <div className="bg-black/20 p-4 rounded-md font-mono text-xs whitespace-pre-wrap">
            {`Defect ID: ${reportData.defectId}
Source Module: Metabolism_Audit V3.1
Severity Rating: ${reportData.severity} (CRITICAL)
Root Cause Hypothesis: ${reportData.rootCause}`}
        </div>

        <h4 className="text-lg font-mono text-[#C5222D] border-b border-[#C5222D]/30 pb-1 pt-6">
          > [RECOMMENDED PROTOCOL] (Action Required)
        </h4>
        <p className="mb-4 text-gray-300">{reportData.protocol}</p>

        {/* CTA 구역 */}
        <div className="text-center p-6 bg-[#1a2d4c] border border-dashed border-red-500 rounded-lg">
            <p className="text-xl font-bold mb-3 text-[#C5222D]">
                🔒 Premium Protocol Access Required
            </p>
            <button 
                className="px-8 py-3 bg-[#C5222D] hover:bg-red-700 text-white font-extrabold uppercase tracking-widest transition duration-150 shadow-lg"
            >
                Full System Report & Protocol Unlock
            </button>
        </div>
      </div>
    </div>
  );
};

export default ReportOutputArea;
</create_file>

<create_file path="mini-funnel-proto/src/App.tsx">
import React, { useState } from 'react';
import DefectIdCard from './components/DefectIdCard';
import SymptomInputForm from './components/SymptomInputForm';
import ReportOutputArea from './components/ReportOutputArea';

// Mock Data Definitions (Dummy data for the prototype)
const MOCK_DEFECT = {
    id: 'E-C403',
    description: '만성적 염증 수치 상승 및 대사 효율 저하. 신체 활동과 영양소 흡수 경로에 심각한 병목 현상이 감지되었습니다.',
};

const INITIAL_REPORT_DATA = {
    defectId: MOCK_DEFECT.id,
    summary: "현재 패턴 분석 결과, 신체의 에너지 대사 효율성이 임계점 이하로 떨어져 있습니다. 이는 단순 피로가 아닌, 시스템적인 '만성적 염증'에 기인한 구조적 문제입니다. 즉각적인 개입이 필요합니다.",
    severity: "CRITICAL",
    rootCause: "주요 영양소 흡수 경로의 미세 균열 및 운동 부족으로 인한 대사 불균형 가속화.",
    protocol: "최적의 결과를 위해서는 '개인 맞춤형 3단계 프로토콜 번들'을 통한 전문 지식과 관리 시스템이 필수적으로 요구됩니다. 이 보고서만으로는 근본적인 해결책 제시가 어렵습니다.",
};

const App: React.FC = () => {
    // State to manage the report data after form submission
    const [reportData, setReportData] = useState<typeof INITIAL_REPORT_DATA>(INITIAL_REPORT_DATA);
    const [loading, setLoading] = useState(false);

    /**
     * 시뮬레이션: 증상 데이터를 받아 최종 보고서를 생성하는 함수 (API 호출 시뮬)
     */
    const handleAnalyzeSymptoms = async (symptoms: any) => {
        setLoading(true);
        // API Latency Simulation
        await new Promise(resolve => setTimeout(resolve, 1500));

        // Simulate successful data processing and report generation
        const newReportData = {
            defectId: MOCK_DEFECT.id, // Keep the ID consistent for the prototype
            summary: "입력된 데이터를 바탕으로 재분석한 결과, 초기 예측이 맞습니다. '대사 효율성 저하'가 핵심 문제이며, 특히 수면 패턴과 미세 영양소 결핍 간의 상관관계가 높게 감지되었습니다.",
            severity: Math.random() > 0.7 ? "CRITICAL" : "HIGH",
            rootCause: `BPI ${symptoms.bodyPainLevel}와 Sleep Score ${symptoms.sleepQualityScore}%의 불일치 패턴이 주요 원인으로 추정됩니다.`,
            protocol: "가장 효과적인 개입은 수면 주기 최적화(Circadian Rhythm Optimization)와 미세 영양소 보강을 결합한 '통합 관리 시스템'입니다. 이는 오직 유료 프로토콜 번들을 통해서만 접근 가능합니다.",
        };

        setReportData(newReportData);
        setLoading(false);
    };


  return (
    <div className="min-h-screen p-8 bg-[#0A1931] text-gray-200 font-sans">
      <header className="mb-12 border-b border-red-700/50 pb-4">
        <h1 className="text-4xl font-mono uppercase tracking-widest flex items-center">
            <span className="text-[#C5222D] mr-3 animate-pulse">[SYSTEM ALERT]</span> 
            Health Protocol Validator <span className='ml-4 text-sm font-normal text-gray-400'>(Beta v1.0)</span>
        </h1>
        <p className="mt-2 text-lg text-[#C5222D]/70">
            공학적 위기감 기반의 신체 진단 및 문제 해결 프로세스 시뮬레이터 💻
        </p>
      </header>

      {/* 1. 핵심 Defect ID 표시 */}
      <div className="mb-16 max-w-3xl mx-auto">
        <DefectIdCard defectId={MOCK_DEFECT.id} description={MOCK_DEFECT.description} />
      </div>

      {/* 2. 증상 입력 및 분석 */}
      <div className="max-w-4xl mx-auto mb-16">
        <SymptomInputForm onAnalyze={handleAnalyzeSymptoms} />
      </div>

      {/* 3. 최종 보고서 출력 영역 */}
      <div className="max-w-5xl mx-auto">
        <ReportOutputArea reportData={reportData} />
      </div>
    </div>
  );
};

export default App;
</create_file>

### ✨ 코드 구조화 및 문서화

위와 같이 3개의 핵심 컴포넌트와 메인 `App.tsx`를 구성했습니다. 이 코드는 Designer님이 정의한 '공학적 위기감'과 '권위성'을 시각적으로 재현하는 데 초점을 맞췄습니다.

#### 구현된 구조의 장점 (Self-Correction Check)
1.  **전문성/권위성 강화:** `font-mono`, 대문자 사용, `#C5222D`와 `Deep Navy` 배경색을 통해 일반적인 건강 앱이 아닌 '시스템 진단' 도구라는 느낌을 강하게 부여했습니다.
2.  **상태 기계 반영:** `SymptomInputForm`에서 데이터를 입력하고 버튼을 누르면, `handleAnalyzeSymptoms` 함수가 실행되어 *비동기적 지연*(`await new Promise(...)`)과 함께 **결과 보고서 컴포넌트의 내용이 변경(State Update)**됩니다. 이는 실제 '처리 중' 상태를 거쳐 결과를 받는 과정을 모방합니다.
3.  **재사용성:** 각 컴포넌트는 독립적으로 동작하며, 필요에 따라 `DefectIdCard`만 팝업하거나 `SymptomInputForm`을 분리하여 다른 페이지에서도 활용 가능합니다.

#### 다음 단계 제언 (Next Step Engineering)
이 프로토타입은 **프론트엔드 시각화**가 완성되었지만, 핵심적인 *데이터 로직*과 *서비스 플로우*가 아직 빠져 있습니다.

1.  **백엔드 API 연동:** `handleAnalyzeSymptoms` 함수 내부의 가짜 로직(Mocking)을 실제 백엔드 엔드포인트(`POST /api/v1/diagnosis`) 호출로 대체해야 합니다.
2.  **유효성 검증 (V&V):** 폼 입력 값에 대한 경계값 검사 및 필수 필드 체크 등 클라이언트 측 유효성 검사(Client-side Validation)를 추가하여 사용자 경험을 개선해야 합니다.

<reveal_in_explorer path="mini-funnel-proto/src"/>
<run_command>npm install react typescript tailwindcss</run_command>

📊 평가: 진행중 — 핵심 컴포넌트와 구조는 완성되었으나, 실제 API 호출 및 유효성 검증 로직이 필요하여 다음 스텝의 백엔드 연동 작업이 남아있습니다.
📝 다음 단계: `handleAnalyzeSymptoms` 함수를 실제 백엔드 API 엔드포인트(`POST /api/v1/diagnosis`)와 연결하고, 클라이언트 측 데이터 유효성 검사(Validation) 로직을 추가해야 합니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `npm install react typescript tailwindcss`
```
up to date, audited 584 packages in 4s

105 packages are looking for funding
  run `npm fund` for details

2 vulnerabilities (1 low, 1 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
npm warn install-scripts 4 packages have install scripts not yet covered by allowScripts:
npm warn install-scripts   @parcel/watcher@2.6.0 (install: node-gyp rebuild)
npm warn install-scripts   @vscode/vsce-sign@2.1.0 (postinstall: node ./src/postinstall.js)
npm warn install-scripts   esbuild@0.28.0 (postinstall: node install.js)
npm warn install-scripts   unrs-resolver@1.12.2 (postinstall: node postinstall.js)
npm warn install-scripts
npm warn install-scripts Run `npm install-scripts ls` to review, or `npm install-scripts approve <pkg>` to allow.
```
_✅_

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\FreqTrade\mini-funnel-proto\src\components\DefectIdCard.tsx
✅ 생성: c:\Data\Project\FreqTrade\mini-funnel-proto\src\components\SymptomInputForm.tsx
✅ 생성: c:\Data\Project\FreqTrade\mini-funnel-proto\src\components\ReportOutputArea.tsx
✅ 생성: c:\Data\Project\FreqTrade\mini-funnel-proto\src\App.tsx
🗂 🗂 익스플로러 열림: c:\Data\Project\FreqTrade\mini-funnel-proto\src
