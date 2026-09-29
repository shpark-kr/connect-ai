# 💻 코다리 — secretary가 정리한 통합 브리핑 문서를 기반으로, E-M411 시스템 복구 프로토콜 MiniFunnel UI의 인터랙티브 목업(Mockup)을 구현하세요. 이는 단순한 디자인 구현이 아닌, '진단 → 위기감 고조 → 솔루션 제시'로 이어지는 논리적 흐름과 상태 변화(State Change)가 작동하는 수준이어야 합니다. 사용자가 실제 웹사이트에서 경험할 수 있는 테스트 가능한 형태로 완성하고 git에 커밋하세요.

💻 코다리: 작업 시작합니다.

CEO 지시사항을 확인했습니다. '단순한 디자인 구현'이 아니라, **상태 변화(State Change)가 작동하는 수준의 인터랙티브 목업**을 요구하셨습니다. 이건 단순 컴포넌트 개발로 끝나지 않습니다. MiniFunnel의 핵심은 *사용자 심리*를 조작하는 논리적 플로우에 있기 때문에, 프론트엔드 상태 관리(State Management)와 UI/UX 로직이 완벽하게 결합되어야 합니다.

영숙님이 정리해주신 통합 브리핑 문서를 기반으로, 이 복잡한 인터랙티브 경험을 담는 `MiniFunnelMockup` 컴포넌트를 구축하겠습니다. React와 TypeScript를 사용하여 상태 기계(State Machine) 패턴을 적용할 것이며, Deep Crimson 테마의 시각적 권위를 확보하는 게 최우선 목표입니다.

**[작업 계획]**
1.  프로젝트 내 `src/components` 디렉토리에 MiniFunnel 관련 파일을 생성합니다.
2.  TypeScript와 React를 사용하여 상태 기계를 구현하고, 5단계 User Flow (Alert $\rightarrow$ Question $\rightarrow$ Protocol $\rightarrow$ CTA)가 순차적으로 작동하도록 코드를 작성합니다.
3.  작성 후에는 반드시 컴포넌트 테스트 및 타입 안정성을 검증하는 과정을 거칩니다.

먼저 필요한 파일 구조를 잡겠습니다. 현재 작업 환경에 `src/components` 디렉토리가 있는지 확인하겠습니다. (없으면 생성해야 합니다.)

<list_files path="src/components"/>


---
## 📁 파일 액션 결과

📂 목록: c:\Data\Project\connect-ai\src\components/
```
📁 ArticleBuilder/
📄 authority-link-box.html
📄 ChecklistDownloadForm.jsx
📁 DiagnosticChecklist/
📄 FormModule.tsx
📄 FunnelCTA.tsx
📁 FunnelPage/
📄 GapAreaChartComponent.types.ts
📄 GapAreaChartModule.tsx
📄 GapContrastWidget.tsx
📁 GapRiskVisualizer/
📄 GapWidget.js
📄 InteractiveGapAreaChart.tsx
📄 master-cta-module.css
📁 MiniApp/
📁 MiniFunnel/
📄 MiniFunnelCore.tsx
📄 RiskScoreCalculator.tsx
📄 RiskScoreModule.tsx
📁 StatusIndicator/
📁 text/
📁 ui/
📄 visual-report-component.ts
📁 visualization/
📁 visualizations/
📁 welfare-flowchart/
📁 __tests__/
```

[시스템: list_files 결과]
디렉토리: c:\Data\Project\connect-ai\src\components/
📁 ArticleBuilder/
📄 authority-link-box.html
📄 ChecklistDownloadForm.jsx
📁 DiagnosticChecklist/
📄 FormModule.tsx
📄 FunnelCTA.tsx
📁 FunnelPage/
📄 GapAreaChartComponent.types.ts
📄 GapAreaChartModule.tsx
📄 GapContrastWidget.tsx
📁 GapRiskVisualizer/
📄 GapWidget.js
📄 InteractiveGapAreaChart.tsx
📄 master-cta-module.css
📁 MiniApp/
📁 MiniFunnel/
📄 MiniFunnelCore.tsx
📄 RiskScoreCalculator.tsx
📄 RiskScoreModule.tsx
📁 StatusIndicator/
📁 text/
📁 ui/
📄 visual-report-component.ts
📁 visualization/
📁 visualizations/
📁 welfare-flowchart/
📁 __tests__/
