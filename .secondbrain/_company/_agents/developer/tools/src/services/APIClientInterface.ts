// DefectValidatorService가 외부 API에 의존하는 추상화 계층(Interface)을 정의합니다.
import { DefectID, DiagnosisResult } from '../types/DiagnosisTypes';

/**
 * @interface APIClientInterface
 * 실제 데이터베이스 또는 API 게이트웨이와 통신하는 모든 로직의 계약(Contract).
 * 이를 통해 서비스 레이어는 '데이터 출처'에 대해 알 필요가 없습니다.
 */
export interface APIClient {
    /**
     * 특정 DefectID를 기반으로 실시간 측정 데이터를 비동기적으로 패칭합니다.
     * @param defectId 검증하려는 결함의 고유 ID (예: E-M411).
     * @returns Promise<DiagnosisResult> - API 응답 지연 시간을 시뮬레이션한 최종 진단 결과 객체.
     * @throws Error - 네트워크 오류나 4xx/5xx 에러가 발생했을 때 던져지는 표준화된 에러입니다.
     */
    getDefectData(defectId: DefectID): Promise<DiagnosisResult>;

    /**
     * 여러 결함 ID의 데이터 패칭을 병렬로 처리합니다 (Race Condition 및 Latency 시뮬레이션).
     * @param defectIds 요청할 결함 ID들의 배열.
     * @returns Promise<Map<DefectID, DiagnosisResult>> - 모든 데이터를 성공적으로 가져온 맵 객체.
     */
    getMultipleDefectData(defectIds: DefectID[]): Promise<Map<DefectID, DiagnosisResult>>;
}

/**
 * 실제 외부 API와의 연결을 시뮬레이션하는 Mock 구현체 (Test용).
 * 실제 운영 환경에서는 Firebase SDK 또는 Axios/Fetch Wrapper로 대체됩니다.
 */
export class MockAPIClient implements APIClient {
    private readonly MOCK_DELAY_MS: number = 50; // 데이터 패칭 지연 시간 시뮬레이션 (50ms)

    /**
     * 가짜 데이터를 생성하여 비동기적으로 반환합니다.
     */
    public async getDefectData(defectId: DefectID): Promise<DiagnosisResult> {
        console.log(`[API Client] Fetching data for ${defectId}... (Simulating delay)`);
        // 네트워크 지연 시간 시뮬레이션
        await new Promise(resolve => setTimeout(resolve, this.MOCK_DELAY_MS));

        if (!['E-M411', 'N-512'].includes(defectId)) {
            throw new Error(`API_ERROR: Invalid Defect ID format or not found in mock DB.`);
        }

        // 가짜 데이터 로직 (실제로는 API 응답 본문 구조를 따름)
        const isCritical = defectId === 'E-M411';
        return {
            defectID: defectId,
            name: `공학적 시스템 결함 (${defectId})`,
            severityLevel: isCritical ? 'CRITICAL' : 'WARNING',
            measuredValue: Math.random() * (isCritical ? 50 + Math.random() * 20 : 10), // 위기감 유발 값 생성
            threshold: isCritical ? 70 : 30, // 기준치 대비 낮은 측정값 강조
            description: `${defectId}은(는) 현재 ${Math.round((Math.random()* (isCritical? 50+Math.random() * 20) / 10): 1)}의 위험도를 보이며, 임계점(${this.getThreshold(defectId)}) 대비 낮은 측정값으로 진단되었습니다.`,
        };
    }

    /**
     * 여러 데이터를 병렬로 가져오는 것을 시뮬레이션합니다. (Promise.all 활용)
     */
    public async getMultipleDefectData(defectIds: DefectID[]): Promise<Map<DefectID, DiagnosisResult>> {
        console.log(`[API Client] Fetching multiple data for ${defectIds.length} defects...`);

        // 각 요청에 대해 지연 시간을 부여하고 병렬로 처리하는 것을 시뮬레이션
        const promises = defectIds.map(id => this.getDefectData(id).catch(e => ({ error: (e as Error).message })));
        
        const resultsArray = await Promise.allSettled(promises);
        const resultMap = new Map<DefectID, DiagnosisResult>();

        resultsArray.forEach((result, index) => {
            const defectId = defectIds[index];
            if (result.status === 'fulfilled' && typeof result.value !== 'object' || result.value === null || 'error' in result.value) {
                 // 에러가 포함되거나 유효하지 않은 경우, 오류 객체를 저장합니다.
                resultMap.set(defectId, result.value); 
            } else if (typeof result.value === 'object' && !('error' in result.value)) {
                // 성공적으로 데이터를 가져온 경우
                resultMap.set(defectId, result.value as DiagnosisResult);
            }
        });

        return resultMap;
    }

    private getThreshold(defectId: DefectID): number {
        if (defectId === 'E-M411') return 70;
        if (defectId === 'N-512') return 30;
        return 50; // 기본값
    }
}