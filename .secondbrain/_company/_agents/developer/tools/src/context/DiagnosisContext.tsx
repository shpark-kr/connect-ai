import React, { createContext, useContext, useState, useCallback } from 'react';
import { DiagnosisResult, DiagnosticInput } from '../types/index';

// 🚨 타입 정의 (실제 프로젝트 구조에 맞춰 조정 필요)
interface MiniFunnelState {
  currentStep: 'hero' | 'diagnosis' | 'result';
  diagnosticData: DiagnosticInput | null;
  isLoadingDiagnosis: boolean;
  finalResult: DiagnosisResult | null;
}

const DiagnosisContext = createContext<MiniFunnelState & { updateDiagnosticData: (data: Partial<DiagnosticInput>) => void, runDiagnosis: () => Promise<void>>();

export const useDiagnosisContext = () => useContext(DiagnosisContext);

/**
 * Mock API 호출 함수: 실제 백엔드 엔드포인트와 대체 가능하도록 설계.
 * @param data - 사용자가 입력한 진단 데이터
 */
const mockApiCallForDiagnosis = async (data: DiagnosticInput): Promise<DiagnosisResult> => {
  console.log("API Call: Running diagnostic check with:", data);
  // ⚡️ 실제 환경에서는 useQuery를 통해 fetcher 함수로 대체됨.
  await new Promise(resolve => setTimeout(resolve, 1500)); // 네트워크 지연 시뮬레이션

  if (data.bloodPressure && data.bloodPressure.systolic < 100) {
    return { defectId: "E-M411", severity: "Critical", message: "관절 시스템의 심각한 불안정성 감지. 즉각적인 복구 프로토콜이 필요합니다." };
  } else if (data.sugarLevel && data.sugarLevel < 90) {
    return { defectId: "E-N512", severity: "Warning", message: "에너지 시스템의 저하가 확인되었습니다. 영양 보충이 시급합니다." };
  } else {
    return { defectId: "OK-000", severity: "Normal", message: "현재 측정된 수치로는 큰 문제가 감지되지 않았습니다. 정기 점검을 권장합니다." };
  }
};

export const DiagnosisProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [state, setState] = useState<MiniFunnelState>({
    currentStep: 'hero',
    diagnosticData: null,
    isLoadingDiagnosis: false,
    finalResult: null,
  });

  /** 전역 상태 업데이트 로직 */
  const updateDiagnosticData = useCallback((dataUpdate: Partial<DiagnosticInput>) => {
    setState(prev => ({
      ...prev,
      diagnosticData: { ...prev.diagnosticData, ...dataUpdate }
    }));
  }, []);

  /** 진단 프로세스 실행 (핵심 로직) */
  const runDiagnosis = useCallback(async () => {
    if (!state.diagnosticData) {
        alert("진단을 진행하려면 모든 필수 항목을 입력해 주세요.");
        return;
    }
    setState(prev => ({ ...prev, isLoadingDiagnosis: true }));

    try {
      // ⭐️ useQuery 패턴의 핵심 로직 시뮬레이션 (API 호출)
      const result = await mockApiCallForDiagnosis(state.diagnosticData);
      console.log("Diagnostic Success:", result);

      setState(prev => ({
        ...prev,
        isLoadingDiagnosis: false,
        finalResult: result,
        currentStep: 'result', // 진단 완료 후 결과 페이지로 전환
      }));

    } catch (error) {
      console.error("Diagnostic Failure:", error);
      setState(prev => ({
        ...prev,
        isLoadingDiagnosis: false,
        finalResult: null,
        currentStep: 'diagnosis', // 오류 발생 시 진단 페이지에 머무름
      }));
    }
  }, [state.diagnosticData]);

  const contextValue = {
    ...state,
    updateDiagnosticData,
    runDiagnosis,
  };

  return (
    <DiagnosisContext.Provider value={contextValue}>
      {children}
    </DiagnosisContext.Provider>
  );
};

export const useMiniFunnelState = () => useDiagnosisContext();