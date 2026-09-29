import React from 'react';
import { DiagnosisProvider, useMiniFunnelState } from '../context/DiagnosisContext';
// ✅ 기존에 개발된 컴포넌트들 (가정)
import RecoveryProtocol from '../components/RecoveryProtocol/RecoveryProtocol'; 
import './styles/PageStyles.module.css'; // 전역 페이지 스타일

/**
 * MiniFunnel Landing Page의 Hero 섹션
 */
const FunnelHeroSection: React.FC = () => {
  return (
    <section className="hero-section">
      <h1>🚨 [시스템 경고] 당신의 신체 시스템에 오류가 감지되었습니다.</h1>
      <p>40대 이상이라면, 노화라는 단어로 덮어두기 쉬운 공학적 결함(Defect)이 이미 시작되었습니다.</p>
      <p className="sub-text">MiniFunnel 진단 과정을 통해 당신의 정확한 시스템 오류 코드를 확인하고 복구 계획을 세우세요.</p>
    </section>
  );
};

/**
 * MiniFunnel Landing Page 전체 구조 (Provider로 감싸서 상태 제공)
 */
const MiniFunnelLandingPageContent: React.FC = () => {
  const { currentStep, finalResult } = useMiniFunnelState();

  return (
    <div className="funnel-container">
      {/* 1. Hero Section - Hook & 위기감 조성 */}
      <FunnelHeroSection />
      
      <main className={`content-area ${currentStep === 'result' ? 'result-view' : ''}`}>
        {/* 2. 진단 Form 및 로직 처리 (핵심) */}
        <section className="diagnosis-section">
          <h2>✅ 시스템 진단 시작: 주요 Defect ID 점검</h2>
          {/* DiagnosisForm은 RecoveryProtocol 컴포넌트 내부에서 사용한다고 가정합니다. */}
          <RecoveryProtocol /> 
          <button 
            onClick={() => { /* 실제 Context의 runDiagnosis() 호출 */ }} 
            disabled={currentStep === 'result' || currentStep === 'hero'}
            className="diagnosis-button"
          >
             {/* 로딩 상태와 버튼 텍스트를 동적으로 변경해야 합니다. */}
            진단 결과 분석 및 시스템 보고서 받기 ⚙️
          </button>
        </section>

        {/* 3. 최종 결과 CTA Section (State 기반 렌더링) */}
        {finalResult && currentStep === 'result' && (
          <section className="result-cta-section">
            <h2>🚨 진단 완료: 당신의 시스템 오류 코드</h2>
            <div className={`defect-display ${finalResult.severity.toLowerCase()}`}>
              <h1>Defect ID: {finalResult.defectId}</h1>
              <p>{finalResult.message}</p>
              {/* 🎯 Funnel 최종 목표 CTA */}
              <button className="cta-primary">
                [복구 프로토콜 시작] 상세 진단 및 솔루션 보기 → (MiniFunnel)
              </button>
            </div>
          </section>
        )}
      </main>
    </div>
  );
};

/**
 * 최종 Export 구조: Context Provider로 감싸서 사용성을 보장
 */
const MiniFunnelLandingPage: React.FC = () => (
    <DiagnosisProvider>
        <MiniFunnelLandingPageContent />
    </DiagnosisProvider>
);

export default MiniFunnelLandingPage;