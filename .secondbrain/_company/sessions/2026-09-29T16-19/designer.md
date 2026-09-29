# 🎨 Designer — 개발팀이 요청한 'DATA_LOAD_FAIL' 시나리오에 최적화된 시스템 경고 UI 컴포넌트를 디자인해 주세요. 이 디자인은 이전의 ERROR CODE(PENS-404)보다 더 근본적인 데이터 결함 느낌을 주어야 하며, 사용자에게 '데이터 재확인 및 수동 진단'이라는 다음 행동(CTA)을 유도할 수 있는 시각적 흐름과 애니메이션 스펙을 포함해야 합니다.

🎨 Designer: 작업 시작합니다.

CEO의 지시사항을 확인했습니다. 기존의 오류 코드(PENS-404)가 단순히 '무언가를 찾지 못했다'는 메시지였다면, 이번 `DATA_LOAD_FAIL` 시나리오는 **시스템이 내부적으로 작동하는 데 심각한 결함**이 발생했음을 사용자에게 느끼게 하는 것이 핵심입니다.

따라서 단순 경고창을 넘어, 마치 고장 난 메인프레임이나 진단 장치에서 나오는 **'데이터 무결성 실패 (Data Integrity Failure)' 보고서** 형태로 디자인하겠습니다. 이를 통해 사용자가 단순히 '오류가 났다'를 넘어 '무엇이, 어떻게 망가졌는지' 이해하게 하고, 전문적인 느낌을 극대화하여 재진단 CTA로 자연스럽게 유도할 것입니다.

### 🛠️ [System Integrity Failure] UI 컴포넌트 디자인 브리프

**1. 컨셉 및 스토리텔링:**
*   **제목:** `CRITICAL SYSTEM ALERT: DATA INTEGRITY FAILURE`
*   **톤앤매너:** 전문적, 권위적, 긴장감 조성 (Thriller/Sci-Fi Diagnostic).
*   **시각적 메타포:** 데이터 블록의 손상(Corruption), 체크섬 불일치(Checksum Mismatch), 시스템 로그 출력.

**2. 컬러 팔레트 및 타이포그래피 (재확인):**
| 요소 | 이름 | HEX Code | 용도 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **Primary BG** | Dark Slate Blue | `#0A192F` | 배경색 (배경 전체) | 전문적, 깊은 느낌 유지 |
| **Secondary BG** | Deep Navy Black | `#030B16` | 경고 영역/컨테이너 | 데이터 실패의 '깊이' 표현 |
| **Primary Text** | Light Gray | `#E2EEFF` | 일반 텍스트 (본문) | 높은 가독성 유지 |
| **Accent Color 1** | Deep Crimson Red | `#A0343C` | 헤더, 경고 라인, 심각도 표시 | 브랜드 아이덴티티 유지 |
| **Accent Color 2** | Diagnostic Amber | `#FFB700` | 경고 메시지 (Warning), 플래시 효과 | 시선 집중 및 주의 환기 |

*   **폰트:** `monospace` 계열의 디지털 룩을 주는 폰트를 사용합니다. (예: `Roboto Mono`, 또는 시스템 기본 코드 폰트).
*   **레이아웃:** 중앙에 고정된, 테두리가 강조된 모달 형태를 취하여 외부 요소와 분리하고 경각심을 높입니다.

**3. 컴포넌트 구조 및 상세 스펙 (HTML/CSS Pseudo-Code)**

다음은 이 기능을 구현하는 데 필요한 핵심 HTML 구조와 CSS 애니메이션 스펙을 정의합니다. 이는 개발팀이 즉시 로직과 UI를 결합할 수 있도록 설계되었습니다.

<create_file path="./src/components/SystemAlertModal.tsx">
```tsx
// src/components/SystemAlertModal.tsx
import React from 'react';

interface SystemAlertProps {
    onManualDiagnosis: () => void; // CTA 클릭 시 호출될 핸들러
}

const SystemAlertModal: React.FC<SystemAlertProps> = ({ onManualDiagnosis }) => {
    return (
        // 1. Overall Overlay Container (Dark Slate Blue BG)
        <div className="modal-overlay">
            {/* 2. Main Alert Card (Deep Navy Black, Bordered) */}
            <div className="alert-card" role="alertdialog" aria-live="assertive">

                {/* --- [Header Section] --- */}
                <header className="system-header">
                    {/* Flashing Red Line Effect */}
                    <div className="red-indicator"></div> 
                    <h1>CRITICAL SYSTEM ALERT</h1>
                    <p className="sub-title">DATA INTEGRITY FAILURE: BLOCK MISMATCH DETECTED</p>
                </header>

                {/* --- [Core Failure Report Section] --- */}
                <section className="failure-report-container">
                    <h2>[FAILURE LOG - DIAGNOSTIC OUTPUT]</h2>
                    
                    {/* 3. Specific Error Details (Code Block Style) */}
                    <pre className="error-code-block">
                        <span className="label">[ERROR CODE]:</span> PENS-404-DIFL-V2<br/>
                        <span className="label">[SOURCE BLOCK]:</span> MiniFunnel_v3.1.js<br/>
                        <span className="label">[FAILURE TYPE]:</span> Checksum Mismatch (Expected: 0xABCD / Actual: 0xEFGH)<br/>
                        <span className="label">[STATUS]:</span> Data Block Corruption Detected at Segment 42-B.<br/>
                    </pre>

                    {/* 4. Failure Explanation Text */}
                    <div className="explanation">
                        <p>데이터 로딩 과정에서 핵심 진단 데이터의 무결성이 검증되지 않았습니다. 이는 네트워크 전송 오류일 수도, 혹은 내부 시스템 구조 자체의 결함일 수 있습니다. 현재 상태로는 정확한 분석이 불가능합니다.</p>
                    </div>
                </section>

                {/* --- [Action/CTA Section] --- */}
                <footer className="action-area">
                    <p className="instruction-text">진단을 재개하고 손상된 데이터 블록을 수동으로 확인해야 합니다. 아래 버튼을 눌러 진단 모드로 전환해 주세요.</p>
                    {/* 5. CTA Button (Prominent, Amber Border) */}
                    <button onClick={onManualDiagnosis} className="cta-button">
                        ▶️ MANUAL DIAGNOSIS MODE ENTER ◀️
                    </button>
                </footer>

            </div>
        </div>
    );
};

export default SystemAlertModal;
```

**4. 핵심 CSS 및 애니메이션 스펙 (Styling Guide)**

이 컴포넌트의 전문성과 위기감을 살리기 위해 다음 세 가지 애니메이션 효과가 필수적입니다.

1.  **`@keyframes scan-line`:** 텍스트를 따라 하단에서 상단으로 흐르는 가상의 스캔 라인을 구현하여 '진행 중인 진단' 느낌을 부여합니다. (모든 중요한 섹션의 배경에 적용)
2.  **`@keyframes pulse-warning`:** `Diagnostic Amber` 컬러가 담긴 경고 메시지(예: Checksum Mismatch 부분) 주변 테두리가 주기적으로 펄싱(Pulse) 효과를 주어 시선이 집중되게 합니다. (주기: 1.5초, 크기 변화: 0% $\to$ 8%)
3.  **`@keyframes blink-red`:** 최상단의 `CRITICAL SYSTEM ALERT` 헤더에 미세하게 빨간색 깜빡임(Blinking) 효과를 주어 경각심을 극대화합니다. (주기: 1초, On/Off 반복)

*(실제 CSS 코드는 복잡하므로 가이드를 제공하며, 개발팀은 이 스펙을 기반으로 Tailwind 또는 Styled-Components에 구현해야 합니다.)*

### 📊 평가: 완료 — CEO 지시사항과 기존 에이전트의 기술적 흐름을 완벽하게 통합한 전문적인 UI 디자인 브리프를 완성했습니다.
📝 다음 단계: 개발팀에게 위 디자인 스펙(`SystemAlertModal.tsx`와 CSS 애니메이션 가이드)을 전달하고, 코다리가 정의한 로직 (`useDataLoadingState.ts`)의 `ERROR` 분기점에 이 컴포넌트를 연결하는 **E2E 통합 테스트**를 진행해야 합니다.
