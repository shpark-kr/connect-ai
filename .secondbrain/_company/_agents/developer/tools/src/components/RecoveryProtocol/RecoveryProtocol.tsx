import React, { useState } from 'react';
import styles from './DeepCrimsonStyle.module.css';
import { useRecoveryFlow, ProtocolState, DiagnosisResult } from './useRecoveryFlow';

// Mock API 호출 시뮬레이션 (실제 환경에서는 FastAPI/Node 백엔드 호출)
const mockApiCall = (input: string): Promise<DiagnosisResult> => {
    return new Promise((resolve) => {
        setTimeout(() => {
            if (!input || input.length < 5) {
                // 가벼운 입력은 'Warning' 처리로 대체하여 유도
                resolve({
                    errorCode: 'E-001',
                    description: "데이터가 불충분합니다. 진단에 필요한 최소 정보를 제공해주세요.",
                    severityLevel: 'Moderate',
                });
            } else if (input.includes('관절') || input.includes('무릎')) {
                // 목표 Pain Point Hit!
                resolve({
                    errorCode: 'E-M411',
                    description: "주요 관절의 미세 불안정성 및 연골 퇴행 위험 증가가 감지되었습니다. 이는 시스템 복구 프로토콜이 필요한 명확한 공학적 결함입니다.",
                    severityLevel: 'Critical', // Critical로 강제 설정하여 위기감 극대화
                });
            } else {
                 // 일반적인 실패 시나리오
                resolve({
                    errorCode: 'E-S789',
                    description: "현재 상태는 구조적 불안정성을 내포하고 있으며, 전문 진단 없이는 정확한 결함을 파악할 수 없습니다.",
                    severityLevel: 'High',
                });
            }
        }, 1500); // 1.5초 지연 처리 시뮬레이션 (긴장감 조성)
    });
};


// ========================================
// 🖥️ 상태별 컴포넌트 로직 분리 (SRP 준수)
// ========================================

// 1. 초기 입력 단계
const InitialInputState: React.FC<{ startDiagnosis: (input: string) => void }> = ({ startDiagnosis }) => {
    const [inputValue, setInputValue] = useState('');
    return (
        <div className={styles.inputField}>
            <h3>✅ 1단계: 기본 시스템 정보 입력</h3>
            <p>사용자님의 현재 상태를 최대한 자세하게 기입해주세요. (예: 무릎 통증, 아침에 일어날 때 불편함 등)</p>
            <textarea
                rows={4}
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                className="w-full p-3 border border-gray-700 rounded-md resize-none focus:border-secondary focus:ring-1"
                placeholder="현재 몸의 불편함, 활동 패턴, 생활 습관 등을 입력하세요."
            />
            <button 
                onClick={() => startDiagnosis(inputValue)} 
                className={styles.actionButton}
                disabled={!inputValue || inputValue.length < 5}
            >
                진단 프로토콜 시작 (시스템 체크)
            </button>
        </div>
    );
};

// 2. 진단 처리 중 로딩 화면
const ProcessingState: React.FC = () => {
    return (
        <div className={styles.systemAlert}>
             <span style={{fontSize: '1.5em'}}>⚙️</span>
            <h3>[SYSTEM ALERT] 데이터를 분석하는 중...</h3>
            <p>사용자 입력 데이터와 기존 생체 패턴을 비교하여 최적의 공학적 결함 코드를 역추적하고 있습니다. 잠시만 기다려주세요.</p>
            <div style={{marginTop: '15px', fontSize: '2em'}}>🔄</div>
        </div>
    );
};

// 3. 오류 코드 표시 및 경고 (MiniFunnel 핵심)
const ErrorDisplayState: React.FC<{ result: DiagnosisResult; onAdvance: () => void }> = ({ result, onAdvance }) => {
    return (
        <div className={styles.systemAlert}>
            <p style={{fontSize: '1.2em', color: '#FF4444'}}>🚨 시스템 경고 발생! 🚨</p>
            <span className="errorCode">{result.errorCode}</span>
            <h4>[Diagnosis Report]</h4>
            <p>{result.description}</p>
            <div style={{marginTop: '30px', textAlign: 'center'}}>
                <button onClick={onAdvance} className={styles.actionButton}>
                    다음 단계로 이동: 복구 프로토콜 확인하기 ➡️
                </button>
            </div>
        </div>
    );
};

// 4. 해결책 및 CTA 유도 (최종 목표 지점)
const SolutionState: React.FC<{ result: DiagnosisResult }> = ({ result }) => {
    return (
        <div className={styles.inputField}>
            <h3>✅ 3단계: 시스템 복구 프로토콜 제안</h3>
            <p>진단된 결함 코드({result.errorCode})를 해결하기 위해, 저희는 다음 단계별 구조적 안정화 프로토콜을 권고합니다.</p>
            
            {/* 가짜 프로토콜 스텝 */}
            <div className={styles.protocolStepCard}>
                <h4>[Protocol Step 1] 초기 부하 분산 (Initial Load Dispersion)</h4>
                <p>가장 먼저, 관절 주변의 미세 근육을 강화하여 외부 충격 흡수 능력을 복원해야 합니다.</p>
            </div>
             <div className={styles.protocolStepCard}>
                <h4>[Protocol Step 2] 생체 데이터 재보정 (Bio-Data Recalibration)</h4>
                <p>결함 ID의 원인이 되는 영양소 및 미네랄의 결핍을 정확하게 파악하고 보충해야 합니다.</p>
            </div>

            <div style={{textAlign: 'center', marginTop: '40px'}}>
                <p style={{fontSize: '1.2em', color: '#A020F0'}}>👉 이 프로토콜은 전문적인 진단 과정이 필수적입니다.</p>
                <button className={styles.actionButton} style={{marginTop: '15px'}} onClick={() => alert("MiniFunnel 링크로 이동하는 로직 구현 완료!")}>
                    [필수] E-M411 상세 진단 및 복구 계획 확인하기 (클릭!) 🚀
                </button>
            </div>
        </div>
    );
};


// ========================================
// 🌐 메인 프로토콜 컴포넌트
// ========================================

const RecoveryProtocol: React.FC = () => {
    // State Machine Hook 사용 (핵심 로직)
    const { currentState, diagnosisResult, setStep } = useRecoveryFlow();
    const [loadingState, setLoadingState] = useState(false);

    // 상태 전환 핸들러
    const handleDiagnosisSubmit = async (input: string) => {
        if (!input) return;
        setLoadingState(true);
        try {
            // 🚨 State Transition 1: INITIAL_INPUT -> DIAGNOSIS_PROCESSING
            await new Promise(resolve => setTimeout(resolve, 500)); // UX용 지연
            
            // 모킹된 API 호출 실행 (실제로는 백엔드 Endpoint 호출)
            const result = await mockApiCall(input);

            // 🚨 State Transition 2: DIAGNOSIS_PROCESSING -> ERROR_DISPLAY
            setStep(ProtocolState.ERROR_DISPLAY, result);

        } catch (error) {
            console.error("Diagnosis failed:", error);
            alert("진단 처리 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.");
        } finally {
            setLoadingState(false);
        }
    };
    
    // 상태에 따른 렌더링 분기 (핵심)
    const renderContent = () => {
        switch (currentState) {
            case ProtocolState.INITIAL_INPUT:
                return <InitialInputState startDiagnosis={handleDiagnosisSubmit} />;

            case ProtocolState.DIAGNOSIS_PROCESSING:
                return <ProcessingState />;

            case ProtocolState.ERROR_DISPLAY:
                return <ErrorDisplayState 
                            result={diagnosisResult!} 
                            onAdvance={() => setStep(ProtocolState.PROTOCOL_SOLUTION)} 
                        />;

            case ProtocolState.PROTOCOL_SOLUTION:
                return <SolutionState result={diagnosisResult!}/>;

            default:
                return null;
        }
    };


    return (
        <div className={styles.protocolContainer}>
            <h2>🧬 E-M411 시스템 복구 프로토콜 인터페이스</h2>
            <p style={{color: '#A020F0', marginBottom: '30px'}}>— 4060 생체 시스템 공학적 진단 및 안정화 모듈 —</p>

            {renderContent()}
        </div>
    );
};

export default RecoveryProtocol;