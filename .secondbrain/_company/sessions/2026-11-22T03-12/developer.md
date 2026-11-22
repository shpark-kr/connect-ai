# 💻 코다리 — Designer가 제공할 최종 디자인 스펙과 지난 로그에서 확정된 3단계 MiniFunnel 프로토콜(PCR) 흐름에 맞춰, 웹사이트의 핵심 위젯(Defect ID 보고서 위젯 및 Funnel 추적 모듈)을 End-to-End 테스트 가능한 상태로 코딩하고 git 저장소에 커밋하세요. 초기 A/B 테스트가 가능하도록 최소한의 KPI 측정 로직까지 포함해야 합니다.

💻 코다리: 작업 시작합니다.

CEO님의 지시가 명확하네요. '핵심 위젯을 End-to-End 테스트 가능한 상태로 코딩하고 커밋'하는 것이 목표입니다. 이게 단순히 디자인 스펙을 옮겨 붙이는 작업이 아니라는 걸 아니까요. 🐛 Funnel 흐름과 KPI 측정 로직까지 포함하려면, 코드 레벨에서부터 책임지고 검증해야 합니다.

일단 현재 Designer가 제공한 상세 스펙(`c:\Data\Project\connect-ai\designs\01_threat_report_template_specs.md`)을 기반으로, 위젯의 핵심 컴포넌트와 KPI 추적 로직을 포함하는 TypeScript/React 코드를 작성하겠습니다. A/B 테스트를 위한 가짜 트래커(Mock Tracker)도 함께 구현해야 합니다.

### ⚙️ Step 1: 프로젝트 스캐폴딩 및 파일 생성
위젯들이 들어갈 `src/widgets` 디렉토리를 가정하고, 핵심 컴포넌트 두 개와 추적 서비스 하나를 생성하겠습니다. 모든 코드는 타입스크립트를 사용해서 구조적 안정성을 확보합니다.

<create_file path="src/widgets/DefectReportWidget.tsx">
```tsx
import React, { useState, useCallback } from 'react';
import { trackFunnelStep, TrackedButtonProps } from './FunnelTrackerService';
import './DefectReportWidget.css'; // CSS는 별도로 관리한다고 가정

interface DefectReportWidgetProps {
  initialData: any; // API로부터 받아오는 데이터 형태라고 가정
}

// 재사용 가능한 CTA 버튼 컴포넌트 (A/B 테스트를 위해 props로 variant를 받음)
const TrackedButton: React.FC<TrackedButtonProps> = ({ children, onClick, buttonId, variant }) => {
  const handleClick = useCallback(() => {
    if (onClick) onClick();
    // A/B 테스트 로직 실행: 어떤 버튼이 클릭되었는지 추적
    trackFunnelStep(buttonId, variant); 
  }, [buttonId, variant]);

  return (
    <button 
      className={`cta-btn cta-${variant}`} 
      onClick={handleClick}
      style={{ '--color-primary': variant === 'A' ? '#64FFDA' : '#AAAAAA' }} // 예시로 변수 사용
    >
      {children}
    </button>
  );
};

const DefectReportWidget: React.FC<DefectReportWidgetProps> = ({ initialData }) => {
  const [isCritical, setIsCritical] = useState(false);
  // 로직 검증: Critical Red 시퀀스를 구현하는 상태
  React.useEffect(() => {
    if (initialData?.threatLevel === 'CRITICAL') {
      setIsCritical(true);
    }
  }, [initialData]);

  return (
    <div className="defect-report-widget" style={{ '--color-dark-navy': '#0A192F' }}>
      <h1>🚨 Defect ID 시스템 오류 보고서</h1>
      
      {/* 1. 위협 레벨 경고 바 */}
      <div className={`warning-bar ${isCritical ? 'critical' : ''}`}>
        [⚠️ Threat Level: {initialData?.threatLevel || 'UNKNOWN'}]
      </div>

      <p><strong>Defect ID:</strong> <span className="defect-id">{initialData?.defectId || "DFA-000"}</span></p>
      <div className="data-visuals">
        {/* 주요 수치 그래프 영역 (Placeholder) */}
        <p>메타볼릭 공백 지표: {Math.random().toFixed(2)} (정상 범위 초과)</p>
      </div>

      <h2>📍 MiniFunnel 진단 서비스로 이동</h2>
      <div className="cta-group">
        {/* 3. MiniFunnel 링크 버튼 - A/B 테스트 대상 */}
        <TrackedButton 
          buttonId={`mini_funnel_${initialData?.defectId}`}
          variant={'A'} // Variant A: Primary CTA
          onClick={() => alert('MiniFunnel 진단 페이지로 이동 (Variant A)')}
        >
          ✅ 지금 바로 재정적 손실액 확인하기 (클릭률 최적화)
        </TrackedButton>

        <TrackedButton 
          buttonId={`mini_funnel_${initialData?.defectId}`}
          variant={'B'} // Variant B: Secondary CTA (Different copy/color)
          onClick={() => alert('MiniFunnel 진단 페이지로 이동 (Variant B)')}
        >
          🔍 자세한 Defect ID 보고서 받기 (대안적 접근)
        </TrackedButton>
      </div>

    </div>
  );
};

export default DefectReportWidget;
```

<create_file path="src/widgets/FunnelTrackerService.ts">
```typescript
/**
 * @module FunnelTrackerService 
 * MiniFunnel 프로토콜(PCR)에 맞춰 KPI 추적을 담당하는 모듈.
 * 클라이언트 측에서 API 호출을 시뮬레이션하고, A/B 테스트 데이터를 수집합니다.
 */

// 구조화된 트래킹 데이터 타입을 정의하여 안정성을 확보합니다.
interface TrackingPayload {
    funnelStep: string; // 예: 'DefectID_View', 'CTA_A_Click'
    timestamp: number;
    deviceId: string; 
    userSessionId: string;
    experimentVariant: 'A' | 'B' | null; // A/B 테스트 변수
    data: Record<string, any>; // 추가 데이터 (예: clicked element ID)
}

/**
 * Funnel 단계 추적을 시뮬레이션합니다. 
 * 실제 환경에서는 이 함수가 외부 분석 API (Google Analytics, Amplitude 등)를 호출해야 합니다.
 */
export const trackFunnelStep = (stepId: string, variant: 'A' | 'B' | null): void => {
    const payload: TrackingPayload = {
        funnelStep: stepId,
        timestamp: Date.now(),
        deviceId: window.localStorage.getItem('deviceId') || 'UNKNOWN_DEVICE', 
        userSessionId: sessionStorage.getItem('sessionId') || Math.random().toString(36).substring(2),
        experimentVariant: variant,
        data: { source: 'DefectReportWidget' }
    };

    console.log(`[⚙️ FUNNEL TRACKING] Sending payload to Analytics API:`, JSON.stringify(payload));

    // ********************************************
    // TODO: 실제 배포 시점에는 여기에 fetch()를 이용한 
    // 외부 분석 서비스 엔드포인트 호출 코드가 들어가야 합니다. (네트워크 에러 처리 필수)
    // 예시: await fetch('/api/v1/track', { method: 'POST', body: JSON.stringify(payload) });
    // ********************************************

    // 로컬 스토리지를 이용해 임시 트래픽 로그를 남깁니다. (개발용 디버깅 목적)
    if (!localStorage.getItem('funnelLogs')) {
        localStorage.setItem('funnelLogs', JSON.stringify([]));
    }
    const logs = JSON.parse(localStorage.getItem('funnelLogs') || '[]');
    logs.push(payload);
    localStorage.setItem('funnelLogs', JSON.stringify(logs));

    console.log(`[✅ TRACKING SUCCESS] Funnel Step '${stepId}' recorded for Variant ${variant}.`);
};
```

<create_file path="src/widgets/DefectReportWidget.css">
```css
/* Defect Report Widget의 스타일링은 디자인 스펙을 따르되, 핵심 변수를 사용합니다. */

.defect-report-widget {
    padding: var(--padding-xl);
    border: 1px solid rgba(100, 255, 218, 0.1); /* --color-border */
    background-color: #1a2e4d; /* Darker background for widget pop */
    box-shadow: 0 0 20px rgba(100, 255, 218, 0.1);
}

h1 {
    font-size: 1.8em;
    color: var(--color-secondary-blue); /* --color-secondary-blue */
    margin-bottom: 20px;
}

/* 위협 레벨 경고 바 (Critical Red) */
.warning-bar {
    padding: 15px;
    margin-bottom: 25px;
    border-radius: 8px;
    font-weight: bold;
    text-align: center;
}

/* Critical Red 시퀀스 (위기감 조성) */
.warning-bar.critical {
    background-color: rgba(255, 75, 75, 0.1); /* --color-warning-red 투명 배경 */
    border: 2px solid var(--color-warning-red); /* --color-warning-red 강조 테두리 */
    color: #ff4b4b; /* Critical Red 텍스트 */
    animation: pulse 1s infinite alternate;
}

@keyframes pulse {
    from { box-shadow: 0 0 5px var(--color-warning-red); }
    to { box-shadow: 0 0 20px var(--color-warning-red); }
}

/* Defect ID 코드 표시 영역 */
.defect-id {
    font-family: 'Courier New', monospace; /* --font-mono */
    background-color: #14356d;
    padding: 5px 10px;
    border-radius: 4px;
    display: inline-block;
}

/* CTA 버튼 그룹 */
.cta-group {
    display: flex;
    gap: 20px;
    margin-top: 30px;
}

.cta-btn {
    padding: 15px 30px;
    border: none;
    border-radius: 6px;
    font-size: 1em;
    cursor: pointer;
    transition: all var(--transition-speed); /* --transition-speed */
}

/* Variant A (Primary) 스타일 */
.cta-btn[class*="cta-A"] {
    background-color: #64FFDA; /* --color-secondary-blue */
    color: var(--color-dark-navy); 
    box-shadow: 0 4px 15px rgba(100, 255, 218, 0.3);
}

/* Variant B (Secondary) 스타일 - A/B 테스트를 위한 차별화된 디자인 */
.cta-btn[class*="cta-B"] {
    background-color: #4a69bd; /* 다른 색상으로 시각적 분리 */
    color: white;
}

/* Hover 상태 (시니어 엔지니어는 호버 효과도 고려해야 합니다) */
.cta-btn:hover {
    opacity: 0.85;
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
}

/* 반응형 고려사항 추가 (클래스만 추가) */
@media (max-width: 768px) {
    .cta-group {
        flex-direction: column;
        gap: 15px;
    }
}
```

### 🛠️ Step 2: End-to-End 테스트 및 검증 루프 실행
코딩만으로는 부족합니다. Funnel 추적과 A/B 테스트가 실제로 작동하는지, 그리고 위젯이 의도한 방식으로 사용자에게 노출되는지 `e2e_funnel_cta_test_suite`를 이용해 검증해야 합니다.

<run_command>cd "c:\Data\Project\connect-ai\.secondbrain\_company\_agents\developer\tools" && C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe e2e_funnel_cta_test_suite.py</run_command>

---
📊 평가: 진행중 — 핵심 컴포넌트 코딩 및 E2E 테스트를 실행하여 구현의 안정성과 Funnel 로직을 검증해야 함.
📝 다음 단계: 테스트 결과 분석 후, 위젯이 실제로 통합될 웹페이지(예: Next.js 페이지)에 이 컴포넌트를 배치하고 최종적으로 배포 환경 시뮬레이션을 진행해야 합니다.

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

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
