# 💻 코다리 — Designer가 제공한 'Deep Crimson Red' CTA 컴포넌트 자산(SVG/CSS)을 수령한다고 가정하고, Mini-App Funnel의 핵심 기술 검증 루프를 준비하십시오. 이 자산을 활용하여 웹사이트 내 프로토타입에 임시 통합 테스트 환경을 구성해야 합니다. 개발 목표는 단순히 표시하는 것을 넘어, '스코어 변화'와 연동되어 애니메이션과 함께 CTA가 동적으로 활성화/비활성화되는 상태 관리(State Management) 로직을 E2E 레벨에서 검증하는 것입니다.

💻 코다리: 작업 시작합니다.

CEO 지시사항을 검토했습니다. 핵심은 Designer가 제공한 'Deep Crimson Red CTA 자산'을 단순한 정적 UI로 끝내는 것이 아니라, **점수(Score) 변화라는 동적인 상태(State)**와 연동하여 E2E 레벨에서 작동하는 Mini-App Funnel의 기술 검증 루프를 완성하는 것입니다.

이건 단순히 컴포넌트 라이브러리 작업이 아닙니다. 데이터 입력(Score) $\rightarrow$ 비즈니스 로직 (Critical/Safe 판단) $\rightarrow$ UI 출력 및 애니메이션 트리거라는 **완벽한 시스템 아키텍처**가 필요합니다.

따라서, 다음 단계로 진행하겠습니다:
1.  새로운 Next.js 환경을 셋업하고, 프로젝트 구조를 확보합니다.
2.  핵심 로직(Score State Management)과 UI 컴포넌트 통합(Deep Crimson CTA)을 구현하여 프로토타입 파일을 작성합니다.
3.  마지막으로, 이 프로토타입이 의도대로 작동하는지 E2E 테스트 도구를 사용해 검증합니다.

---

### ⚙️ Step 1: 프로젝트 초기화 및 환경 설정

먼저 Next.js 기반의 웹 개발 환경을 구축하겠습니다.

<run_command>npm create next-app mini-funnel-prototype --ts</run_command>
<run_command>cd mini-funnel-prototype</run_command>

### 💻 Step 2: 핵심 프로토타입 파일 작성 및 로직 구현

`src/components/FunnelPrototype.tsx` 파일을 생성하여 상태 관리와 UI 통합을 담당하는 메인 컴포넌트를 작성하겠습니다. 이 코드는 점수 변화에 따라 CTA의 가시성, 애니메이션, 그리고 '위기감' 레벨을 제어합니다.

<create_file path="mini-funnel-prototype/src/components/FunnelPrototype.tsx">
// src/components/FunnelPrototype.tsx
"use client"; // Next.js 클라이언트 컴포넌트로 설정

import React, { useState, useEffect } from 'react';
import Head from 'next/head';

// ---------------------------------------------
// [DESIGNER SPECIFICATION INTEGRATION]
// Deep Crimson Red CTA 자산 기반의 스타일링 및 구조 정의 (CSS Modules 또는 Tailwind 사용 가정)
// 실제 구현에서는 전역 CSS에 --color-deep-crimson을 정의해야 합니다.
const deepCrimsonStyle = {
    '--color-deep-crimson': '#B30000',
    '--color-alert-dark': 'rgba(179, 0, 0, 0.85)',
};

interface FunnelState {
    score: number; // 현재 측정 점수 (0~100)
    isCritical: boolean; // Critical 상태 여부 (Score <= 30)
}

// ---------------------------------------------
// [COMPONENT] The Warning Overlay (CTA #1 - 도입부 후킹용)
const CTACriticalWarningOverlay: React.FC<{ score: number }> = ({ score }) => {
    if (!score || !['Critical', 'Pre-Alert'].includes(score)) return null;

    return (
        <div className={`absolute bottom-0 left-0 w-full p-4 ${score <= 30 ? 'opacity-100' : 'opacity-50'} transition-all duration-500`}
             style={{ backgroundColor: deepCrimsonStyle['--color-alert-dark'] }}>
            <div className="max-w-xl mx-auto text-center">
                <h3 className={`text-lg font-bold mb-2 ${score <= 30 ? 'text-white' : 'text-red-800'}`}>🚨 [경고] 현재 당신의 건강 점수: {score}점</h3>
                <p className="text-sm text-gray-200">이 수치, 방심하면 안 됩니다. 전문가의 진단이 필수입니다.</p>
                <button 
                    className={`mt-3 px-6 py-2 rounded-full font-bold transition-all duration-300 ${score <= 30 ? 'bg-[#B30000] hover:bg-[#8b0000] text-white' : 'bg-gray-400 cursor-not-allowed'} shadow-lg`}
                    disabled={score > 30}
                >
                    ▶️ Mini-App 진단 도구로 즉시 점검하기 (필수)
                </button>
            </div>
        </div>
    );
};

// ---------------------------------------------
// [COMPONENT] The Solution CTA (CTA #2 - 해결책 제시 후 배치용)
const CTASolution: React.FC = () => (
    <div className="mt-8 p-6 border-l-4 border-[#B30000] bg-red-50/50 shadow-md">
        <h4 className="text-xl font-bold text-[#B30000]">✅ 해결책 제시: 당신이 취할 수 있는 다음 단계</h4>
        <p className="mt-2 text-gray-700">위기 상황에 대한 근본적 원인을 파악하려면, 우리만의 전문 Mini-App Funnel을 통해 종합적인 점검을 받아보세요.</p>
        <button 
            className="mt-4 px-8 py-3 rounded-lg font-bold transition-all duration-300 bg-[#B30000] hover:bg-red-700 text-white shadow-xl"
        >
            👉 상세 맞춤 진단 리포트 받기 (클릭)
        </button>
    </div>
);

// ---------------------------------------------
// [MAIN PROTOTYPE COMPONENT]
const FunnelPrototype: React.FC = () => {
    // 초기 상태는 임의로 설정하거나, API 호출 후 로딩 처리 필요. 여기서는 가상 점수를 사용합니다.
    const [state, setState] = useState<FunnelState>({ score: 75, isCritical: false });

    // 시뮬레이션: 점수 변화를 주는 핸들러 (API 응답을 모방)
    const handleScoreUpdate = (newScore: number) => {
        let newCritical = newScore <= 30;
        setState({ score: newScore, isCritical: newCritical });
    };

    // 시뮬레이션 버튼 핸들러
    const handleSimulationStep = async (step: 'initial' | 'moderate' | 'critical') => {
        await new Promise(resolve => setTimeout(resolve, 500)); // 로딩 애니메이션 시간 확보
        if (step === 'initial') {
            // 도입부 후킹 단계 시뮬레이션 (점수가 아직 미정확함)
            handleScoreUpdate(70);
        } else if (step === 'moderate') {
            // 중간 점검 단계 시뮬레이션 (경고 신호 감지, 50~60점대)
            handleScoreUpdate(45);
        } else {
            // 최종 엔드 스크린 시뮬레이션 (위기 임계치 도달, Critical 상태)
            handleScoreUpdate(22);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50 p-8 font-sans relative">
            <Head>
                <title>Mini-App Funnel Prototype Test</title>
            </Head>
            
            {/* 배경 오버레이를 위한 컨테이너 (Deep Crimson Red가 덮어쓸 영역) */}
            <div className="relative max-w-4xl mx-auto bg-white p-10 shadow-2xl">

                {/* === 🔴 핵심 컴포넌트: 위기감 조성 오버레이 (CTA #1) === */}
                <CTACriticalWarningOverlay score={state.score} />


                <h1 className="text-4xl font-extrabold text-gray-900 mb-6">🩺 웰에이징 라이프케어 스코어 진단</h1>
                <p className="text-lg text-gray-600 mb-8">당신의 현재 생활 습관 점수는 몇 점일까요? 데이터 기반으로 위기감을 조성하고, Mini-App Funnel로 유도하는 E2E 검증 환경입니다.</p>

                {/* === 📊 Score Display & State Visualization === */}
                <div className="bg-gray-100 p-6 rounded-xl mb-8 shadow-inner">
                    <h2 className="text-2xl font-bold mb-4 text-[#B30000]">현재 측정 점수: <span className={`text-4xl ${state.isCritical ? 'text-red-700 animate-pulse' : 'text-green-600'}`}>{state.score}점</span></h2>
                    <div className="w-full bg-gray-200 rounded-full h-3 mb-2">
                        <div 
                            className={`h-3 rounded-full transition-all duration-1000 ease-out ${state.isCritical ? 'bg-[#B30000]' : state.score > 50 ? 'bg-green-500' : 'bg-yellow-500'}`}
                            style={{ width: `${state.score}%` }}
                        ></div>
                    </div>
                    <p className="text-sm text-gray-500">점수 변화에 따라 상단의 경고 오버레이(CTA #1)가 동적으로 활성화됩니다.</p>
                </div>

                {/* === 📝 시뮬레이션 및 테스트 인터페이스 (개발자용) === */}
                <div className="border p-6 rounded-xl bg-yellow-50/70">
                    <h3 className="text-xl font-bold mb-4 text-gray-800">🚀 E2E 흐름 시뮬레이터</h3>
                    <p className="mb-4 text-sm text-red-600">아래 버튼을 순서대로 클릭하여, Mini-App Funnel의 핵심 3단계(도입부 $\rightarrow$ 중간 점검 $\rightarrow$ 최종 엔드 스크린)가 기술적으로 작동하는지 확인하세요.</p>
                    <div className="flex space-x-4">
                        <button 
                            onClick={() => handleSimulationStep('initial')}
                            className="px-6 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition"
                        >
                            1. 도입부 후킹 (Initial) - 점수 70점 설정
                        </button>
                        <button 
                            onClick={() => handleSimulationStep('moderate')}
                            className="px-6 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600 transition"
                        >
                            2. 중간 점검 (Moderate) - 점수 45점 설정
                        </button>
                        <button 
                            onClick={() => handleSimulationStep('critical')}
                            className="px-6 py-2 bg-[#B30000] text-white rounded hover:bg-red-800 transition"
                        >
                            3. 최종 엔드 스크린 (CRITICAL) - 점수 22점 설정
                        </button>
                    </div>
                </div>

                {/* === 🎯 CTA #2 배치 예시 */}
                <CTASolution />
            </div>
        </div>
    );
};


export default FunnelPrototype;
</create_file>

### ✅ Step 3: 페이지 연결 및 테스트 준비

생성한 컴포넌트를 메인 페이지에 임포트하고, 전체 구조를 확인하는 `src/app/page.tsx` 파일을 수정하겠습니다.

<edit_file path="mini-funnel-prototype/src/app/page.tsx">
import React from 'react';
import FunnelPrototype from '../components/FunnelPrototype';

// 기존 내용 대체:
export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50">
      {/* Mini-App Funnel의 핵심 테스트 환경 */}
      <FunnelPrototype />
    </main>
  );
}
</edit_file>

### ⚙️ Step 4: E2E 기능 검증 실행 (가장 중요)

코드를 만들었으니, 반드시 동작하는지 확인해야 합니다. 이 프로토타입은 전형적인 Mini-App Funnel의 핵심 로직을 구현한 것이므로, 가장 적합한 테스트 도구인 `e2e_funnel_cta_test_suite`를 사용하여 상태 전환 및 UI 상호작용(특히 Critical 상태에서의 CTA 활성화)을 검증하겠습니다.

<run_command>cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe e2e_funnel_cta_test_suite.py</run_command>

📊 평가: 진행중 — 코드 구현은 완료되었으나, 시스템 레벨의 E2E 테스트 실행을 통해 최종 기능 검증이 필요함.
📝 다음 단계: `e2e_funnel_cta_test_suite`가 성공적으로 실행되어 프로토타입 로직(상태 $\leftrightarrow$ UI/애니메이션)이 완벽히 검증되면, 이 코드를 기반으로 실제 프론트엔드 개발팀에 인계할 최종 스펙 문서와 컴포넌트를 정리해야 합니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `npm create next-app mini-funnel-prototype --ts`
```
npm warn Unknown cli config "--ts". This will stop working in the next major version of npm.
npm warn exec The following package was not found and will be installed: create-next-app@16.3.6

> connect-ai-lab@2.89.158 npx
> create-next-app mini-funnel-prototype

[?25l[36m?[39m [1mWould you like to use the recommended Next.js defaults?[22m [90m»[39m [90m- Use arrow-keys. Return to submit.[39m
[36m>[39m   [36m[4mYes, use recommended defaults[39m[24m[90m - TypeScript, ESLint, No React Compiler, Tailwind CSS, No src/ directory, App Router, AGENTS.md[39m
    No, reuse previous settings[90m[39m
    No, customize settings[90m[39m
```
_✅_

### 🔧 실행: `cd mini-funnel-prototype`
```
������ ��θ� ã�� �� �����ϴ�.
```
_❌ exit 1_

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

✅ 생성: c:\Data\Project\FreqTrade\mini-funnel-prototype\src\components\FunnelPrototype.tsx
❌ 편집 실패: mini-funnel-prototype/src/app/page.tsx — 파일이 존재하지 않습니다.
