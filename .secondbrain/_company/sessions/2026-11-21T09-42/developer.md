# 💻 코다리 — 연구원과 디자이너가 제공한 최신 자가진단 플로우(3가지 답변 집중)와 UI/UX 브리프를 통합하여, 'Defect ID 진단 보고서 페이지'의 핵심 컴포넌트 프로토타입을 구축하십시오. 특히, 사용자의 입력 값에 따라 시스템 오류 코드가 동적으로 생성되고, 이 코드 기반으로 다음 단계로 자연스럽게 이동하는 인터랙션(State Machine)을 우선 구현하고 테스트 가능하도록 구조화해주세요.

💻 코다리: 작업 시작합니다.

CEO 지시사항을 보니, 전체 마케팅 플로우의 핵심 허브인 'Defect ID 진단 보고서 페이지'의 프로토타입 구축이 목표네요. 단순히 디자인만 입히는 게 아니라, **사용자 경험(UX)과 비즈니스 로직이 결합된 상태 전이(State Machine)**가 필수적입니다. 이건 단순 컴포넌트 합치기가 아니라 아키텍처 레벨의 작업이죠.

현재 시점에서는 이 프로토타입을 어디에 얹어야 할지, 기존 프론트엔드 구조와 어떤 API 엔드포인트를 재사용해야 하는지 파악하는 것이 급선무입니다. 상태 머신 로직은 결국 컴포넌트와 연결된 백엔드 데이터 흐름까지 고려해야 하거든요.

따라서, 바로 코드를 짜기 전에 현재 프로젝트의 핵심 소스 구조를 탐색하겠습니다. 특히 UI/UX가 적용될 프론트엔드 컴포넌트 폴더와 상태 관리 로직이 들어갈 부분을 찾아봐야 합니다.

<list_files path="./src"/>


---
## 📁 파일 액션 결과

📂 목록: c:\Data\Project\connect-ai\src/
```
📄 agents.ts
📄 App.tsx
📁 automation/
📁 blog-articles/
📁 components/
📁 context/
📁 docs/
📄 extension.ts
📁 funnel/
📁 gateways/
📁 hooks/
📄 index.tsx
📄 main.js
📁 mini_funnel_api/
📄 MrBeast_Premium_10.md
📁 pages/
📄 paths.ts
📄 plaza.ts
📄 scheduler_core.py
📁 schemas/
📁 scripts/
📁 services/
📁 styles/
📄 system-specs.ts
📁 templates/
📁 types/
📁 utils/
```

[시스템: list_files 결과]
디렉토리: c:\Data\Project\connect-ai\src/
📄 agents.ts
📄 App.tsx
📁 automation/
📁 blog-articles/
📁 components/
📁 context/
📁 docs/
📄 extension.ts
📁 funnel/
📁 gateways/
📁 hooks/
📄 index.tsx
📄 main.js
📁 mini_funnel_api/
📄 MrBeast_Premium_10.md
📁 pages/
📄 paths.ts
📄 plaza.ts
📄 scheduler_core.py
📁 schemas/
📁 scripts/
📁 services/
📁 styles/
📄 system-specs.ts
📁 templates/
📁 types/
📁 utils/
