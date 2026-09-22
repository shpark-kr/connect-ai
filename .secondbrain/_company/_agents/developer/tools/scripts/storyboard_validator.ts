import * as fs from 'fs';
import * as path from 'path';
import { JSONSchema, validate } from 'ajv';

// [절대 경로] - 1단계에서 생성한 스토리보드 파일 참조
const STORYBOARD_PATH = "c:\\Data\\Project\\connect-ai\\결과물\\05_동영상\\storyboard_v3_1_prototype.json";

/**
 * JSON 스키마 정의: 전체 구조와 타입 체크 (Schema Validation)
 */
const schema = {
    type: "object",
    properties: {
        metadata: { type: "object", properties: { version: { type: "string" }, description: { type: "string" } }, required: ["version"] },
        content_scripts: { 
            type: "array", 
            items: {
                type: "object",
                properties: {
                    script_id: { type: "string" },
                    title: { type: "string" },
                    duration_sec: { type: "number" },
                    scenes: { 
                        type: "array", 
                        items: {
                            type: "object",
                            properties: {
                                scene_id: { type: "string" },
                                time_start: { type: "number" }, // 필수: 시간 시작점 (초)
                                time_end: { type: "number" },   // 필수: 시간 종료점 (초)
                                visual_instruction: { type: "string" },
                                audio_script: { type: "string" },
                                text_overlays: { 
                                    type: "array", 
                                    items: { properties: { text: { type: "string" }, color: { type: "string" } } } 
                                },
                                transition_effect: { type: "string" }
                            },
                            required: ["scene_id", "time_start", "time_end"] // 핵심 필드 강제
                        }
                    }
                },
                required: ["script_id", "scenes"]
            }
        }
    },
    required: ["metadata", "content_scripts"]
};

/**
 * 1. JSON 유효성 검사 (Syntax & Schema Check)
 */
function validateStoryboard(data: any): boolean {
    try {
        const ajv = new JSONSchema();
        ajv.addSchema(schema);
        const validateFn = ajv.compile(schema);
        const isValid = validateFn(data);
        if (!isValid) {
            console.error("❌ [SCHEMA ERROR] 스토리보드가 정의된 스키마를 따르지 않습니다:", validateFn.errors);
            return false;
        }
        console.log("✅ [SUCCESS] JSON 스키마 검증 통과.");
        return true;
    } catch (e) {
        console.error(`❌ [PARSING ERROR] 파일 읽기 또는 파싱 오류:`, e);
        return false;
    }
}

/**
 * 2. 시간 논리 검사 (Chronological & Overlap Check)
 */
function validateTiming(contentScripts: any[]): boolean {
    console.log("\n⚙️ [TIMING CHECK] 콘텐츠의 시간적 순서와 중첩을 확인합니다...");
    let allScenes: any[] = [];

    // 모든 스크립트의 모든 씬 데이터를 취합
    for (const script of contentScripts) {
        script.scenes.forEach(scene => {
            allScenes.push({
                script_id: script.script_id,
                scene_id: scene.scene_id,
                start: scene.time_start,
                end: scene.time_end
            });
        });
    }

    // 시간 순서로 정렬 (가장 중요한 검증)
    allScenes.sort((a, b) => a.start - b.start);

    for (let i = 0; i < allScenes.length - 1; i++) {
        const current = allScenes[i];
        const next = allScenes[i + 1];

        // 논리 검증: 현재 씬의 끝 시간이 다음 씬의 시작 시간보다 커야 함 (중첩 금지)
        if (current.end > next.start) {
            console.error(`🚨 [TIMING ERROR] 중첩 발견! ${current.scene_id} (${current.start}-${current.end})이 ${next.scene_id} (${next.start}-${next.end})와 시간적으로 겹칩니다.`);
            return false;
        }

        // 논리 검증: 다음 씬 시작 시간이 현재 씬 끝 시간보다 너무 작으면 안됨 (간격 최소화)
        if ((next.start - current.end) < 0.1 && i > 0) {
             console.warn(`⚠️ [WARNING] ${current.scene_id}와 ${next.scene_id} 간의 전환 시간이 매우 짧습니다 (${next.start - current.end}초). 부드러운 트랜지션이 필요합니다.`);
        }
    }

    console.log("✅ [SUCCESS] 모든 씬이 시간 순서대로 논리적으로 배치되었으며 중첩된 구간은 없습니다.");
    return true;
}


/**
 * 메인 실행 함수
 */
function runValidator() {
    console.log("================================================");
    console.log("🎬 스토리보드 통합 유효성 검사기 (Storyboarding Validator) 시작");
    console.log("================================================\n");

    const rawData = fs.readFileSync(STORYBOARD_PATH, 'utf8');
    let storyboard: any;
    try {
        storyboard = JSON.parse(rawData);
    } catch (e) {
        console.error(`Fatal Error: JSON 파싱 실패! 파일이 유효한 JSON 형태인지 확인해주세요.`);
        return;
    }

    // 1. Schema 검증 실행
    if (!validateStoryboard(storyboard)) {
        return;
    }

    // 2. Timing 논리 검증 실행
    if (validateTiming(storyboard.content_scripts)) {
        console.log("\n✨ 최종 검증 완료: 스토리보드 JSON은 완벽하며, 자동 비디오 파이프라인에 투입할 준비가 되었습니다.");
    } else {
        console.error("\n❌ 치명적 오류: 시간 논리 오류로 인해 렌더링을 보류합니다. 스크립트를 수정해야 합니다.");
    }
}

runValidator();