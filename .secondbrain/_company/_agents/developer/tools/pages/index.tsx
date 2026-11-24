import React from 'react';
import Head from 'next/head';
import CTAButtonComponent from '../components/CTAButtonComponent';
import { useTracking } from '../context/TrackingContext';

// --------------------------------------------------------
// [1] 가상의 위험도에 따른 경고 패널 컴포넌트 (Designer 스펙 반영)
// --------------------------------------------------------
interface UrgencyPanelProps {
  riskLevel: 'Low' | 'Moderate' | 'Critical';
}

const UrgencyPanel: React.FC<UrgencyPanelProps> = ({ riskLevel }) => {
  const { trackEvent } = useTracking();
  let title = '';
  let colorClass = '';
  let urgencyMessage = '';

  switch (riskLevel) {
    case 'Low':
      title = "⚠️ 경고: 현재 위험 수준은 안정적입니다.";
      colorClass = "bg-blue-100 border-blue-300 text-blue-800";
      urgencyMessage = "하지만 방심은 금물합니다. 정기적인 관찰과 생활 습관 개선이 필요합니다.";
      break;
    case 'Moderate':
      title = "⚠️ 주의: 일부 항목에서 위험 징후가 발견되었습니다.";
      colorClass = "bg-yellow-100 border-yellow-300 text-yellow-800";
      urgencyMessage = "생활 습관 개선만으로는 부족합니다. 객관적인 데이터 분석이 필요합니다.";
      break;
    case 'Critical':
      title = "🚨 긴급 경고: 생물학적 손실 임계점에 근접했습니다!";
      colorClass = "bg-red-100 border-red-400 text-red-800 animate-pulse"; // Alarm Red 활용
      urgencyMessage = "시간이 없습니다. 지금 바로 객관적인 진단으로 '미래 손실 방어액'을 확보해야 합니다.";
      break;
  }

  return (
    <div className={`p-6 border-l-8 rounded-lg shadow-xl ${colorClass}`} role="alert">
      <h2 className="text-2xl font-extrabold mb-3 flex items-center">🚨 {title}</h2>
      <p className="text-lg mb-4">{urgencyMessage}</p>
    </div>
  );
};

// --------------------------------------------------------
// [2] 메인 랜딩 페이지 컴포넌트 (Funnel 구조)
// --------------------------------------------------------
const HomePage = () => {
  const { setABTestGroup } = useTracking();
  React.useEffect(() => {
    // 마운트 시점에 A/B 테스트 그룹을 설정하여 트래킹 시작
    setABTestGroup('A'); // 초기화
  }, [setABTestGroup]);

  // 🚨 핵심 액션 핸들러: 진단 패키지 구매 시도 (가장 높은 우선순위)
  const handlePurchaseAttempt = async () => {
    await useTracking().trackEvent('Funnel_Step', { step: 'Purchase_Click' });
    alert("✅ [시뮬레이션] 49,000원 진단 패키지 구매 플로우로 이동합니다. (실제 결제 API 호출 예정)");
    // TODO: 실제 결제 게이트웨이(Stripe/PG) 연동 로직 구현
  };

  return (
    <div className="min-h-screen bg-gray-50 font-sans">
      <Head>
        <title>온현 | 미래 손실 방어 시스템</title>
        {/* 🚨 Deep Navy와 Alarm Red를 위한 커스텀 CSS 정의가 필요합니다. */}
        <style>{`
          :root {
            --deep-navy: #0A183D; /* 깊은 네이비 */
            --darker-navy: #07122a;
            --alarm-red: #CC3333; /* 경고 빨강 */
            --darker-red: #9e2525;
          }
          .bg-deep-navy { background-color: var(--deep-navy); }
          .hover\\:bg-darker-navy:hover { background-color: var(--darker-navy); }
          .bg-alarm-red { background-color: var(--alarm-red); }
          .hover\\:bg-darker-red:hover { background-color: var(--darker-red); }
        `}</style>
      </Head>

      {/* 🚀 HERO SECTION (불안감 유발 & 문제 제기) */}
      <header className="bg-deep-navy text-white py-24">
        <div className="max-w-6xl mx-auto px-4 text-center">
          <h1 className="text-5xl md:text-6xl font-extrabold mb-4 tracking-tight">
            지금, 당신의 건강은 '비용'이 아닌 <span className="text-yellow-400">미래 손실</span>입니다.
          </h1>
          <p className="text-xl text-gray-300 max-w-3xl mx-auto mb-8">
            막연한 노화가 아닙니다. 측정 가능한 생물학적 메커니즘의 '파괴 지점'을 찾아야 합니다.
          </p>
          {/* 첫 번째 CTA: 진단 시작 유도 */}
          <div className="mt-10">
             <CTAButtonComponent 
                label="🚨 49,000원으로 손실 예측 리포트 받기"
                onClickAction={handlePurchaseAttempt}
                variant="AlarmRed"
            />
          </div>
        </div>
      </header>

      {/* 🔥 URGENCY ALERT PANEL (핵심 심리적 트리거) */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-4xl mx-auto px-4">
          <UrgencyPanel riskLevel="Critical" /> {/* 가장 위험한 시나리오를 노출하여 공포 유발 */}
          <p className="text-center mt-8 text-lg text-gray-600">
            👉 경고: 이 데이터는 본인만 가지고 계셔야 할 '개인화된 손실 예측 지표'입니다.
          </p>
        </div>
      </section>

      {/* 🎯 FUNNEL CORE SECTION (구매 유도) */}
      <section className="py-20 bg-white">
        <div className="max-w-6xl mx-auto px-4 text-center">
          <h2 className="text-4xl font-bold mb-12 text-deep-navy">
            [Step 1] 객관적 진단을 통한 손실 방어 시스템 구축 (필수 과정)
          </h2>
          
          {/* 🚨 가장 중요한 구매 섹션 - Deep Navy 배경으로 무게감 부여 */}
          <div className="bg-gray-100 p-8 rounded-xl shadow-2xl border border-deep-navy/20">
            <h3 className="text-3xl font-extrabold text-alarm-red mb-4">
              최소 투자액: 49,000원 <span className="text-gray-600">(지금 무시하면 생길 손실 방어 비용)</span>
            </h3>
            <p className="text-xl mb-8 text-deep-navy">
              단순 검사가 아닙니다. 당신의 '미래 재정적/신체적 손실'을 계량화하는 최초의 시스템입니다.
            </p>

            {/* A/B 테스트용 3가지 CTA 버튼 배치 */}
            <div className="flex justify-center space-x-6 mt-8">
                <CTAButtonComponent 
                    label="지금 진단 리포트 받기 (A)"
                    onClickAction={handlePurchaseAttempt}
                    variant="AlarmRed"
                    abTestVariant="A"
                />
                 <CTAButtonComponent 
                    label="진단 패키지 구매하기 (B)"
                    onClickAction={handlePurchaseAttempt}
                    variant="DeepNavy"
                    abTestVariant="B"
                />
            </div>
             <p className="mt-6 text-sm text-gray-500">
                * CTA 클릭 시 A/B 테스트 및 구매 추적 로직이 자동 실행됩니다. ⚙️
            </p>
          </div>
        </div>
      </section>

      {/* 📚 CLOSING SECTION (신뢰도 확보) */}
      <section className="py-16 bg-deep-navy text-white">
          <div className="max-w-4xl mx-auto px-4 text-center">
            <h2 className="text-3xl font-bold mb-4">검증된 솔루션으로 불안감을 해결하세요.</h2>
            <p className="text-lg mb-8 text-gray-300">
                온현은 웰에이징 라이프케어 분야에서 쌓아온 데이터를 바탕으로, 고객님의 건강 여정을 Systematically 관리합니다.
            </p>
          </div>
      </section>
    </div>
  );
};

export default HomePage;