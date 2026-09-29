import { useState, useCallback } from 'react';

// 🚨 State Machine Definition: 모든 상태는 명확한 목적을 가져야 합니다.
export enum ProtocolState {
  INITIAL_INPUT = 'INITIAL_INPUT', // 초기 진단 입력 단계
  DIAGNOSIS_PROCESSING = 'DIAGNOSIS_PROCESSING', // 데이터 처리 중 (로딩/애니메이션)
  ERROR_DISPLAY = 'ERROR_DISPLAY', // 공학적 오류 코드 E-XXX 표시 및 경고
  PROTOCOL_SOLUTION = 'PROTOCOL_SOLUTION', // 해결책(프로토콜 단계) 제시 및 CTA 유도
}

export interface DiagnosisResult {
  errorCode: string; // 예: E-M411
  description: string; // 문제 설명 (공학적 용어 사용 필수)
  severityLevel: 'Critical' | 'High' | 'Moderate'; // 심각도에 따른 UI 변수
}

export type RecoveryFlow = {
    currentState: ProtocolState;
    diagnosisResult: DiagnosisResult | null;
    setStep: (state: ProtocolState, result?: DiagnosisResult) => void;
};

// 🧠 State Logic Hook: 상태 변화를 관리하는 핵심 로직입니다.
export const useRecoveryFlow = (): RecoveryFlow => {
  const [currentState, setCurrentState] = useState<ProtocolState>(ProtocolState.INITIAL_INPUT);
  const [diagnosisResult, setDiagnosisResult] = useState<DiagnosisResult | null>(null);

  // 1. 초기 진단 시작 함수 (사용자가 데이터를 입력했을 때 호출)
  const startDiagnosis = useCallback((inputData: string) => {
    console.log(`[Flow Start] Diagnosis triggered with data: ${inputData}`);
    setCurrentState(ProtocolState.DIAGNOSIS_PROCESSING);
    // 실제 환경에서는 여기서 API 호출 및 비동기 처리가 이루어집니다.
  }, []);

  // 2. 진단 완료 및 오류 코드 설정 함수 (API 응답 처리)
  const setDiagnosisResultAndAdvance = useCallback((result: DiagnosisResult) => {
    setDiagnosisResult(result);
    setCurrentState(ProtocolState.ERROR_DISPLAY);
    console.log(`[Flow Advance] Diagnosis complete. Error Code: ${result.errorCode}`);
  }, []);

  // 3. 프로토콜 단계로 이동 및 결과 표시 (진단 후 다음 액션)
  const advanceToSolution = useCallback(() => {
    setCurrentState(ProtocolState.PROTOCOL_SOLUTION);
    console.log('[Flow Advance] Moving to Solution Protocol.');
  }, []);


  const setStep = useCallback((state: ProtocolState, result?: DiagnosisResult) => {
    if (result && state === ProtocolState.ERROR_DISPLAY) {
      setDiagnosisResult(result);
    }
    setCurrentState(state);
  }, []);

  return {
    currentState,
    diagnosisResult,
    setStep: setStep,
  };
};