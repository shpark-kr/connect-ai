import { validateDefectData } from './DefectValidatorService';
import { DiagnosisInputData } from '../types/DiagnosisTypes';

describe('DefectValidatorService Integration Test Suite', () => {
    // 🟢 테스트 케이스 1: 유효한 Master Defect Code 입력 (Success Path)
    test('should successfully validate a known defect code (E-M411)', () => {
        const mockData: DiagnosisInputData = { defectId: 'e-m411' }; // 소문자 테스트 포함
        expect(() => validateDefectData(mockData)).not.toThrow();

        try {
            const result = validateDefectData(mockData);
            expect(result.code).toBe('E-M411');
            expect(result.details.severity).toBe('HIGH');
        } catch (e) {
            fail('Expected successful validation but an error was thrown.');
        }
    });

    // 🟢 테스트 케이스 2: 다른 유효한 Master Defect Code 입력 (Success Path - Corner Case)
    test('should successfully validate another known defect code (N-512)', () => {
        const mockData: DiagnosisInputData = { defectId: ' N-512 ' }; // 공백 포함 테스트
        expect(() => validateDefectData(mockData)).not.toThrow();

        try {
            const result = validateDefectData(mockData);
            expect(result.code).toBe('N-512');
            expect(result.details.severity).toBe('MEDIUM');
        } catch (e) {
            fail('Expected successful validation but an error was thrown for N-512.');
        }
    });

    // 🔴 테스트 케이스 3: 존재하지 않는 임의의 코드 입력 (Failure Path - CRITICAL)
    test('should throw a specific SYSTEM ERROR when the defect code is unknown', () => {
        const mockData: DiagnosisInputData = { defectId: 'ZZ-999' }; // 가짜 코드
        
        // 에러가 발생하는지 확인하는 것이 핵심입니다.
        expect(() => validateDefectData(mockData)).toThrow('SYSTEM ERROR'); 
    });

    // 🔴 테스트 케이스 4: 필수 필드 누락 (Failure Path - Input Validation)
    test('should throw an error when the defectId field is missing', () => {
        const mockData: DiagnosisInputData = { defectId: '' }; // 빈 값 입력
        expect(() => validateDefectData(mockData)).toThrow("진단 ID(defectId)가 누락되었습니다.");
    });

});