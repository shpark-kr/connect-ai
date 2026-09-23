// /pages/api/v2/calculate_gap.ts
import { NextApiRequest, NextApiResponse } from 'next';

/**
 * Gap 계산 API Stub 엔드포인트 (V2.0)
 * 실제 로직은 GapCalculation_API_Spec_V2.0.md를 기반으로 구현되어야 합니다.
 * 여기서는 클라이언트-서버 통신 흐름 검증을 위해 Mock 데이터를 사용합니다.
 */
export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  // 1. 요청 유효성 검사 (Validation Check) - 필수 단계입니다.
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed. Only POST is allowed.' });
  }

  const { assessmentData } = req.body;

  // 2. 데이터 무결성 검증 (Input Validation)
  if (!assessmentData || typeof assessmentData !== 'object') {
    return res.status(400).json({ error: 'Invalid request body. Must contain valid assessmentData.' });
  }

  console.log('Received Assessment Data:', assessmentData);

  // 3. 핵심 로직 (Stub Implementation)
  // 실제로는 이 부분에 복잡한 GapCalculation_API_Spec_V2.0의 모든 가중치 계산이 들어가야 합니다.
  let totalGapAmount: number;
  let riskLevel: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';

  try {
    // Mock 로직 1: 특정 핵심 항목 존재 유무에 따라 Gap을 조작합니다. (테스트 용이성 확보)
    const hasLongTermCareRisk = assessmentData['long_term_care']?.includes('YES') ?? false;
    const isHousingGap = assessmentData['housing']?.includes('NO') ?? false;

    if (hasLongTermCareRisk && isHousingGap) {
        // 최대 리스크 조합 시뮬레이션: 가장 높은 Gap 금액을 반환하여 Critical 경고를 유도합니다.
        totalGapAmount = 4500000; // 예시: 450만원
        riskLevel = 'CRITICAL';
    } else if (hasLongTermCareRisk) {
        // 중급 리스크 시뮬레이션
        totalGapAmount = 1200000; // 예시: 120만원
        riskLevel = 'HIGH';
    } else {
        // 낮은 리스크 시뮬레이션 (혹은 Gap 없음)
        totalGapAmount = Math.floor(Math.random() * 50000); // 최대 5만 원의 작은 Gap
        riskLevel = 'LOW';
    }

  } catch (error) {
    console.error("Error during gap calculation stub:", error);
    return res.status(500).json({ error: 'Internal server error during Gap computation.' });
  }


  // 4. 응답 구조화 및 전송
  const result = {
    success: true,
    timestamp: new Date().toISOString(),
    gapDetails: {
      calculatedAmountKRW: totalGapAmount, // 원 단위로 반환
      description: `사용자님의 현재 상황을 진단한 결과, 공적 지원만으로는 ${totalGapAmount.toLocaleString()}원 상당의 생활/돌봄 사각지대가 예상됩니다.`,
    },
    riskAssessment: {
      level: riskLevel, // CRITICAL, HIGH, MEDIUM, LOW
      displayMessage: getRiskDisplayMessage(riskLevel),
      colorClass: getRiskColorClass(riskLevel) // Tailwind CSS 클래스를 반환하여 프론트가 바로 사용 가능하도록 함.
    }
  };

  res.status(200).json(result);
}


/**
 * 위험 레벨별 메시지 및 색상 매핑 (유지보수성을 위해 함수로 분리)
 */
function getRiskDisplayMessage(level: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL'): string {
    switch (level) {
        case 'CRITICAL': return "🚨 경고: 치명적 재정 사각지대 감지. 즉각적인 보완책 마련이 필요합니다.";
        case 'HIGH': return "⚠️ 위험 수준: 중요한 영역에서 Gap이 발생했습니다. 세부 체크가 필요합니다.";
        case 'MEDIUM': return "🟡 주의: 일부 항목에서 추가 점검이 필요한 부분이 확인되었습니다.";
        case 'LOW': return "🟢 안정적: 현재까지는 큰 구조적 리스크가 감지되지 않았습니다. (하지만 꼼꼼한 재확인이 필수입니다.)";
    }
}

function getRiskColorClass(level: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL'): string {
    switch (level) {
        case 'CRITICAL': return 'text-red-700 bg-red-100 border-red-700'; // Critical Red! (지난 의사결정 로그 반영)
        case 'HIGH': return 'text-orange-600 bg-orange-50 border-orange-600';
        case 'MEDIUM': return 'text-yellow-800 bg-yellow-50 border-yellow-700';
        case 'LOW': return 'text-green-700 bg-green-50 border-green-700';
    }
}

export { getRiskDisplayMessage, getRiskColorClass };