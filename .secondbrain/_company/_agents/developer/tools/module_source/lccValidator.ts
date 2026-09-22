// src/utils/lccValidator.ts

/**
 * @typedef {Object} DataPoint
 * @property {number} year - 연도 (필수, 정수)
 * @property {number} value - 해당 연도의 재정적 값 (필수, 숫자)
 * @property {string} unit - 단위 (예: "만원")
 */

/**
 * @typedef {Object} DataSets
 * @property {string} id - 데이터셋 ID (고유 식별자)
 * @property {string} label - 그래프 레이블명
 * @property {string} colorCode - 색상 코드 (HEX)
 * @property {DataPoint[]} dataPoints - 연도별 데이터 포인트 배열
 */

/**
 * @typedef {Object} LCCInputData
 * @property {string} chartId - 콘텐츠 고유 ID
 * @property {{primary: string, secondary: string}} title - 그래프 제목 (객체)
 * @property {DataSets[]} dataSets - 모든 데이터셋 배열
 */

/**
 * 입력된 데이터를 검증하고 표준화하여 렌더링 가능한 객체를 반환합니다.
 * 이 함수는 Unit Test의 핵심입니다.
 * @param {LCCInputData} rawData - 전처리할 원본 LCC 데이터 구조체.
 * @returns {{validatedData: LCCInputData, errors: string[]}} 검증된 데이터와 발생한 오류 목록.
 */
export function validateAndNormalizeLccData(rawData) {
    const errors = [];
    let validatedData;

    // 1. 기본 구조 유효성 검사
    if (!rawData || typeof rawData !== 'object') {
        errors.push("❌ 필수 입력 데이터입니다. 객체 형태로 제공되어야 합니다.");
        return { validatedData: null, errors };
    }

    const { chartId, title, dataSets } = rawData;

    // 2. 제목 검증
    if (!title || typeof title !== 'object' || !title.primary) {
        errors.push("❌ 그래프의 주요(Primary) 제목이 누락되었습니다.");
    }

    // 3. 데이터셋 배열 및 개별 포인트 유효성 검사 (가장 중요)
    const validDataSets = [];
    for (let i = 0; i < dataSets.length; i++) {
        const dataset = dataSets[i];
        if (!dataset || !dataset.id || typeof dataset.label !== 'string' || !dataset.colorCode) {
            errors.push(`❌ 데이터셋 ${i}의 필수 속성 (ID, Label, ColorCode)이 누락되었습니다.`);
            continue; // 이 데이터셋은 스킵하고 다음으로 넘어갑니다.
        }

        const validPoints = [];
        for (const point of dataset.dataPoints) {
            // Year: 정수 여부 및 양수 검증
            if (!Number.isInteger(point.year) || point.year < 2000) {
                errors.push(`   - 데이터셋 ${dataset.id}: 유효하지 않은 연도(${point.year})가 발견되었습니다.`);
                continue;
            }
            // Value: 숫자인지 검증
            if (typeof point.value !== 'number' || isNaN(point.value)) {
                errors.push(`   - 데이터셋 ${dataset.id}: 유효하지 않은 값(${point.value})이 발견되었습니다.`);
                continue;
            }
            // Unit: 문자열 여부 검증 (Optional)
            if (typeof point.unit !== 'string' && point.unit !== '') {
                 errors.push(`   - 데이터셋 ${dataset.id}: 유효하지 않은 단위(${point.unit})가 발견되었습니다.`);
            }

            // 모든 검증 통과 시 포인트 추가
            validPoints.push(point);
        }

        if (validPoints.length > 0) {
            validDataSets.push({ ...dataset, dataPoints: validPoints });
        } else {
             errors.push(`⚠️ 데이터셋 ${dataset.id}: 유효한 데이터 포인트가 하나도 없어 그래프에 표시할 수 없습니다.`);
        }
    }

    if (errors.length > 0) {
        return { validatedData: null, errors };
    }

    // 모든 검증 통과 시 최종 구조체 반환
    validatedData = { chartId, title: { primary: title.primary, secondary: title.secondary }, dataSets: validDataSets };
    return { validatedData, errors: [] };
}
export type LccValidatedData = typeof validateAndNormalizeLccData;