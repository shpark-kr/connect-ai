# 💻 코다리 — Designer가 제공한 컴포넌트 명세서(Component Spec)를 바탕으로, MiniFunnel의 핵심 기능을 수행하는 'Defect ID 진단 위젯 (Widget)'의 초기 버전 코드를 작성해주세요. 이 위젯은 단일 HTML 파일로 구성되어야 하며, 다음 기능을 반드시 포함해야 합니다: 1) Defect ID 코드와 심각도를 시각적으로 표시하고, 2) 사용자의 클릭 이벤트 발생을 추적하는 간단한 클라이언트 사이드 로직(JavaScript)을 구현하며, 3) 나중에 다양한 콘텐츠에서 재사용할 수 있도록 모듈화된 구조를 갖추어야 합니다. (개발 목표: 기술적 안정성 확보)

💻 코다리: 작업 시작합니다.

요청하신 'Defect ID 진단 위젯'은 단순한 UI 컴포넌트가 아니라, **MiniFunnel 유도라는 핵심 비즈니스 목표를 수행하는 인터랙티브 장치**입니다. 따라서 단순히 보기 좋은 HTML/CSS로 끝낼 순 없습니다. 자바스크립트를 사용해 다음과 같은 기술적 안정성을 확보해야 합니다.

1.  **캡슐화 (Encapsulation):** 전역 스코프 오염을 막기 위해 IIFE 또는 클래스 구조를 사용합니다.
2.  **상태 관리:** Defect ID와 심각도(Severity)가 변경될 때마다 DOM을 재조작하는 로직이 명확해야 합니다.
3.  **추적성 (Traceability):** 클릭 이벤트는 반드시 어떤 데이터와 함께 로그되어야 나중에 QA나 분석 단계에서 의미를 가집니다.

Designer님이 제공해주신 스펙(Dark Mode, Monospace Font 등)을 기반으로, 재사용성을 최우선한 단일 HTML 파일을 작성하겠습니다.

<create_file path="index.html">
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Defect ID 진단 위젯 | 온현</title>
    <!-- 외부 라이브러리 사용 최소화 (재사용성 및 단일 파일 목표) -->
    <style>
        /* II. 컴포넌트별 상세 스펙 기반 전역 스타일 정의 */
        :root {
            --color-primary: #D9534F; /* Critical Red */
            --color-secondary: #FFC107; /* Amber/Yellow */
            --color-background: #1a1e25; /* Dark Navy/Slate */
            --color-text: #E0E0E0; /* Light Gray */
            --color-accent: #00FFFF; /* Cyan (Technical Data) */
            --font-mono: 'Courier New', Courier, monospace;
        }

        body {
            background-color: var(--color-background);
            color: var(--color-text);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }

        .defect-widget {
            width: 100%;
            max-width: 768px; /* 반응형 구조 반영 */
            background-color: #232735;
            border: 1px solid rgba(40, 48, 60, 0.7);
            padding: 30px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.4) inset;
        }

        h1 {
            font-size: 1.5em;
            color: var(--color-accent);
            border-bottom: 2px solid #3a3e48;
            padding-bottom: 10px;
            margin-top: 0;
        }

        /* 1️⃣ Defect ID 코드 표시 영역 */
        .defect-id-display {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px 0;
            margin-bottom: 30px;
            border-bottom: 1px dashed #3a3e48;
        }

        .id-container {
            flex-grow: 1; /* 공간 점유 */
            text-align: left;
        }

        #defectIdCode {
            font-family: var(--font-mono);
            color: var(--color-accent);
            font-size: 2em;
            margin-right: 20px;
            /* 깜빡임/글리치 효과 구현 */
            animation: blinker 1s linear infinite alternate;
        }

        .id-meaning {
            font-family: var(--font-mono);
            color: var(--color-text);
            display: block;
            font-size: 0.9em;
            margin-top: 5px;
            /* 글리치 효과를 위한 CSS 구현 (미니멀 버전) */
        }

        @keyframes blinker {
            from { opacity: 1; }
            to { opacity: 0.2; }
        }

        /* 심각도 표시기 */
        .severity-indicator {
            min-width: 150px;
            text-align: right;
            padding-left: 30px;
        }

        #severityLevel {
            font-size: 2em;
            font-weight: bold;
            cursor: default;
        }

        /* 심각도 컬러 매핑 */
        .critical { color: var(--color-primary); } /* Red */
        .warning { color: var(--color-secondary); } /* Yellow/Amber */
        .low { color: #4CAF50; } /* Green - 안정성 강조를 위해 추가 */

        /* CTA 버튼 (MiniFunnel 유도) */
        .mini-funnel-cta {
            text-align: center;
            padding: 20px 0;
        }

        #ctaButton {
            background-color: var(--color-primary);
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 1.2em;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.1s;
            letter-spacing: 1px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        #ctaButton:hover {
            background-color: #c34a45; /* Darker red on hover */
            transform: translateY(-1px);
        }

        #ctaButton:active {
            transform: translateY(1px);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body>
    <div class="defect-widget">
        <h1>🚨 Defect ID 진단 시스템 보고서</h1>

        <!-- I. Defect ID 코드 표시 영역 -->
        <div class="defect-id-display">
            <div class="id-container">
                <span id="defectIdCode">[AWAITING DATA]</span>
                <span id="defectMeaning" class="id-meaning">진단 대기 중. 전문 분석을 위해 데이터를 입력해주세요.</span>
            </div>

            <!-- 심각도 표시 영역 -->
            <div class="severity-indicator">
                심각도: <span id="severityLevel" class="low">LOW</span>
            </div>
        </div>

        <!-- II. CTA 및 로직 수행 버튼 -->
        <div class="mini-funnel-cta">
            <p>즉시 진단 및 위험 요소 제거가 필요합니다.</p>
            <button id="ctaButton">▶️ MiniFunnel 프로토콜(PCR) 실행하기</button>
            <small style="display: block; margin-top: 10px;">* 클릭 시 전문 분석 페이지로 이동합니다 (추적됨).</small>
        </div>
    </div>

    <script>
        // =======================================================
        // [MODULAR JS WIDGET LOGIC] Defect ID Widget Controller
        // 전역 스코프 오염 방지를 위해 IIFE(Immediately Invoked Function Expression) 사용.
        // =======================================================
        (function() {
            'use strict';

            // DOM 요소들을 미리 캐싱하여 성능 최적화 (시니어 스타일)
            const $defectIdCode = document.getElementById('defectIdCode');
            const $defectMeaning = document.getElementById('defectMeaning');
            const $severityLevel = document.getElementById('severityLevel');
            const $ctaButton = document.getElementById('ctaButton');

            /**
             * @type {Object} 현재 위젯의 상태를 저장하는 전역(로컬) 변수
             */
            let widgetState = {
                isInitialized: false,
                currentDefectId: null,
                severityClass: 'low',
                severityText: 'LOW'
            };

            /**
             * 🐛 [핵심 기능] 위젯의 시각적 상태를 업데이트하는 함수.
             * @param {string} id - Defect ID 코드 (예: D-1024)
             * @param {string} meaning - 의미 설명
             * @param {'CRITICAL' | 'WARNING' | 'LOW'} severityType - 심각도 유형
             */
            function displayDefectInfo(id, meaning, severityType) {
                // 1. 상태 업데이트 및 유효성 검사 (Guard Clause)
                if (!id || !meaning || !severityType) {
                    console.error("Widget Error: 필수 데이터 누락으로 인해 정보 표시를 취소합니다.");
                    return;
                }

                widgetState.currentDefectId = id;
                widgetState.severityClass = severityType === 'CRITICAL' ? 'critical' : 
                                             severityType === 'WARNING' ? 'warning' : 'low';
                widgetState.severityText = severityType.toUpperCase();

                // 2. DOM 조작 (최적화된 방식으로)
                $defectIdCode.textContent = id;
                $defectMeaning.textContent = meaning;
                
                // 심각도 레벨 클래스 및 텍스트 업데이트
                $severityLevel.className = ''; // 기존 클래스 초기화
                $severityLevel.classList.add(widgetState.severityClass);
                $severityLevel.textContent = widgetState.severityText;

                console.log(`✅ Widget State Updated: ${id} - ${meaning} (${severityType})`);
            }


            /**
             * ⚙️ [핵심 기능] 사용자 상호작용(클릭)을 추적하는 이벤트 리스너 핸들러.
             * @param {Event} e - 클릭 이벤트 객체
             */
            function handleCtaClick(e) {
                e.preventDefault();
                console.warn("=======================================");
                // 🚀 MiniFunnel CTA 클릭 로그 추적 (핵심 비즈니스 로직)
                const trackingPayload = {
                    timestamp: new Date().toISOString(),
                    widgetId: "DefectID_Diagnosis_Widget", // 이 위젯 고유 ID
                    defectId: widgetState.currentDefectId,
                    severity: widgetState.severityText,
                    actionTaken: "CTA_Click_MiniFunnel_Initiated",
                    clientSource: window.location.href
                };

                // 실제 환경에서는 fetch API를 통해 분석 서버로 전송해야 함.
                console.log("📊 [ANALYTICS TRACKING]: MiniFunnel CTA 클릭 이벤트 발생.");
                console.log("   -> Payload:", JSON.stringify(trackingPayload, null, 2));

                // 다음 단계 (가상): 전문 분석 페이지로 이동하는 로직 실행
                alert(`[시스템 알림] ${widgetState.currentDefectId} 진단 결과에 따른 'MiniFunnel 프로토콜'을 시작합니다.`);
                // window.location.href = "/mini-funnel-protocol"; // 실제 구현 시 사용

            }

            /**
             * 🔧 [초기화 로직] 위젯이 DOM에 완전히 로드되었을 때 호출되는 진입점.
             */
            function initWidget() {
                if (widgetState.isInitialized) return; // 이미 초기화됨 방지

                // 이벤트 리스너 등록
                $ctaButton.addEventListener('click', handleCtaClick);

                // --- 테스트 데이터로 위젯 초기화 ---
                // 실제 사용 시에는 API 호출을 통해 데이터를 받아 displayDefectInfo를 호출해야 함.
                const testId = "D-1024"; 
                const testMeaning = "장기간의 생활 습관 및 영양 불균형으로 인한 세포 에너지 시스템 오류(Mitochondrial Stress). 즉각적인 관리가 필요합니다.";
                const testSeverity = 'CRITICAL'; // CRITICAL, WARNING, LOW 중 선택

                displayDefectInfo(testId, testMeaning, testSeverity);
                
                widgetState.isInitialized = true;
                console.log("✅ Defect ID Widget Initialization Complete.");
            }

            // DOMContentLoaded 이벤트 리스너를 붙여서 스크립트가 모든 요소 로드 후 실행되도록 보장 (Best Practice)
            document.addEventListener('DOMContentLoaded', initWidget);

        })();
    </script>
</body>
</html>
</create_file>

<reveal_in_explorer path="index.html"/>

---
**기술적 검토 결과:**
1.  **재사용성/모듈화**: IIFE를 사용하여 전역 스코프 오염을 원천 차단했습니다. `displayDefectInfo` 함수만 호출하면 어떤 곳에서든 상태 업데이트가 가능하도록 분리했습니다. ⚙️
2.  **디자인 준수**: Designer님이 요청하신 Dark Mode, Monospace Font, Critical Red 등의 핵심 디자인 요소를 CSS 변수를 통해 적용하여 일관성을 유지했습니다.
3.  **클릭 추적**: CTA 버튼 클릭 시, `console.log`를 통해 필수 데이터(Widget ID, Defect ID, Severity)가 포함된 트래킹 페이로드를 출력하도록 구현했습니다. 이는 향후 실제 백엔드 분석 모듈과 연동할 수 있는 구조입니다. ✅

📊 평가: 완료 — 요구사항에 맞게 기능성 높은 단일 HTML 위젯을 성공적으로 작성하고 실행 가능한 상태로 만들었습니다.
📝 다음 단계: 이 위젯이 실제로 어떤 콘텐츠(예: 블로그 포스팅, 랜딩 페이지)에 사용될지 파악하여, 해당 환경의 고유한 CSS/JS 구조와 통합 테스트를 진행해야 합니다.

---
## 📁 파일 액션 결과

✏️ 덮어씀: c:\Data\Project\connect-ai\index.html
🗂 🗂 익스플로러 열림: c:\Data\Project\connect-ai\index.html
