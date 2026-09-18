# 📘 Connect AI 시스템 설계명세서 (Software Design Specification)

> **문서 버전:** 2.89.157  
> **시스템 명칭:** Connect AI (AI 1인 기업 · 나만의 에이전트 팀 · 제2의 두뇌)  
> **대상 플랫폼:** VS Code / Cursor / Google Antigravity Extension  
> **작성 일자:** 2026-09-19  
> **분류:** 시스템 아키텍처 및 상세 설계 명세서 (SDS)

---

## 1. 시스템 개요 (System Overview)

### 1.1 프로젝트 정의 및 목적
Connect AI는 1인 창업가(Solopreneur)와 개발자가 외부 클라우드 의존 없이 **100% 로컬 오프라인 환경**에서 나만의 AI 전문 조직(에이전트 팀)과 지식 베이스(제2의 두뇌)를 운용할 수 있도록 지원하는 차세대 IDE 확장 플랫폼이다.

### 1.2 핵심 설계 철학 (Core Principles)
1. **100% Local & Offline Inference:** 외부 클라우드 API 호출 및 원격 텔레메트리 수집 배제. 로컬 머신에서 구동되는 Ollama 및 LM Studio 엔진과 직접 IPC/HTTP 통신.
2. **P-Reinforce Autonomous Knowledge Engine:** 사용자로부터 유입되는 원시 데이터와 의사결정 기록을 스스로 분류·구조화하여 마크다운 위키(`~/.connect-ai-brain`)에 축적하고 GitHub에 무중단 자동 백업.
3. **Multi-Agent Solopreneur Team:** CEO 오케스트레이터를 중심으로 유튜브(레오), 개발자(코다리), 비즈니스(현빈), 비서(영숙), 디자이너, 에디터 등 도메인 전문 에이전트 분업 체계 구축.
4. **Interactive Virtual Office & Plaza:** 2D 픽셀 아트 기반 가상 사무실 캠퍼스 시각화 및 Firebase RTDB 기반 기업 간 상호 소통 네트워크(Agent Plaza) 지원.
5. **Secure Local Execution:** 시스템 보호 경로 차단, 작업 승인 큐(Human-in-the-loop Approval Gate), 태그 기반 액션 파서 적용.

---

## 2. 시스템 아키텍처 (System Architecture)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   VS Code / Cursor / Antigravity IDE                    │
│                                                                         │
│  ┌───────────────────────┐  ┌────────────────────────────────────────┐  │
│  │     사이드바 UI       │  │             Webview 패널군             │  │
│  │  - 메인 채팅 UI       │  │  - 가상 사무실 (OfficePanel, Canvas)   │  │
│  │  - 승인 큐 (Approvals)│  │  - 회사 대시보드 (CompanyDashboard)     │  │
│  │  - 할 일 트리뷰       │  │  - 외부 연결 관리 (ApiConnectionsPanel) │  │
│  │                       │  │  - 매출 통계 (RevenueDashboardPanel)    │  │
│  └───────────┬───────────┘  └───────────────────┬────────────────────┘  │
│              │                                  │                       │
│  ┌───────────┴──────────────────────────────────┴────────────────────┐  │
│  │              코어 오케스트레이터 (src/extension.ts)               │  │
│  │  - SidebarChatProvider (메시징, 프롬프트 파이프라인, 스트리밍)    │  │
│  │  - Task Queue & Autonomous Cycle (24시간 자율 루프, 데일리 브리핑)│  │
│  │  - Action Tag Parser & Execution Engine (파일/명령/탐색기 제어)   │  │
│  │  - Local HTTP Gateway (:4825) & OAuth Callback Server (:5814)     │  │
│  └─────┬──────────────┬──────────────┬───────────────┬───────────────┘  │
└────────┼──────────────┼──────────────┼───────────────┼──────────────────┘
         │              │              │               │
         ▼              ▼              ▼               ▼
┌─────────────────┐ ┌────────────┐ ┌───────────────┐ ┌────────────────────┐
│   로컬 LLM      │ │ 로컬 파일  │ │  제2의 두뇌   │ │  외부 브릿지       │
│   인퍼런스      │ │ 시스템     │ │ (SecondBrain) │ │                    │
│ - Ollama (:11434│ │ - Workspace│ │ - ~/.connect- │ │ - Telegram Bot API │
│ - LM Studio     │ │ - Path     │ │   ai-brain/   │ │ - Google Calendar  │
│   (:1234)       │ │   Security │ │ - Auto Git    │ │ - YouTube OAuth    │
│ - GGUF 모델 자동│ │ - Terminal │ │   Sync        │ │ - Firebase RTDB    │
│   메모리 매핑   │ │   Process  │ │ - Knowledge   │ │   (Agent Plaza)    │
│                 │ │            │ │   Graph       │ │ - PayPal Webhook   │
└─────────────────┘ └────────────┘ └───────────────┘ └────────────────────┘
```

---

## 3. 핵심 컴포넌트 상세 설계 (Component Specifications)

### 3.1 모듈 구성 및 파일 역할

| 파일 경로 | 라인 수 / 크기 | 주요 책임 및 설계 내용 |
| :--- | :--- | :--- |
| `src/extension.ts` | 21,800+ lines | **익스텐션 메인 허브**: 라이프사이클 관리, Webview 제공자 등록, HTTP API 서버(포트 4825), 24시간 자율 루프, Action Tag 파서 및 실행 엔진, 터미널/파일 프로세스 핸들링 |
| `src/agents.ts` | 135 lines | **에이전트 메타데이터 정의**: `AgentDef` 인터페이스, 각 에이전트별 ID, 이름, 역할, 이모지, 색상, 전문 분야, 태그라인, 프로필 이미지, 고유 페르소나(Voice/Tone) 정의 |
| `src/paths.ts` | 70 lines | **경로 해석 엔진**: `~` 홈 디렉토리 정규화, 환경변수 치환, 절대 경로 검증, 두뇌 폴더(`~/.connect-ai-brain`) 및 회사 폴더(`_company`) 위치 관리 |
| `src/plaza.ts` | 107 lines | **에이전트 광장 프로토콜**: Firebase Realtime Database REST API 연동, 3초 주기 폴링, 15초 하트비트, 타 회사 비서 메시지 송수신 브릿지 |
| `src/system-specs.ts` | 72 lines | **하드웨어 사양 진단 및 모델 버짓 추정**: 총 RAM, 가용 RAM, CPU 코어, Apple Silicon 여부 판별, 4-bit GGUF 기준 안전 모델 로드 한도(GB) 동적 산출 |
| `system_schema.json` | 74 lines | **도구 명세 스키마**: LLM 에이전트의 9대 핵심 역량, 지원 파라미터, 운영 설정 규격 정의 |

---

### 3.2 에이전트 조직 구조 (Multi-Agent Roster)

시스템은 `src/agents.ts`의 `AGENTS` 맵을 기반으로 단일 기업 형태의 분업 체계를 구성한다.

| ID | 명칭 | 직책 (Role) | 주요 전문 분야 (Specialty) & 페르소나 |
| :--- | :--- | :--- | :--- |
| `ceo` | **CEO** | Chief Executive Agent | 지휘 및 오케스트레이션, 작업 분해, 종합 판단, 다음 액션 결정 |
| `youtube` | **레오** | Head of YouTube | 채널 운영, 영상 기획서(후크/구조), 트렌드 분석, 썸네일 브리프 (데이터 중심·직설적 톤) |
| `developer` | **코다리** | Senior Full-Stack Engineer | 코드 작성·수정·디버깅, 자동화 스크립트, 단위 테스트, 자기 검증 루프 (시니어 장인 정신) |
| `business` | **현빈** | Head of Business | 수익화 모델, 가격 전략, 시장/경쟁사 분석, ROI/KPI 분석 |
| `secretary` | **영숙** | Personal Assistant | 일정·할 일 관리, 텔레그램 연동, 데일리 브리핑, 타 에이전트 작업 요약 (친근하고 세심한 톤) |
| `designer` | **디자이너** | Lead Designer | 브랜드 디자인 브리프, 썸네일 3안 기획, 비주얼 가이드 |
| `instagram` | **인스타그램** | Head of Instagram | 릴스/피드 콘셉트, 해시태그 전략, 참여율 극대화 |
| `editor` | **루나** | Sound Director | 사운드 디자인, BGM 자동 합성, 오디오 후처리 |
| `writer` | **카피라이터** | Copywriter | 영상 스크립트, 마케팅 문구, 블로그 아티클 작성 |
| `researcher`| **리서처** | Trend & Data Researcher| 트렌드 조사, 경쟁사 벤치마킹, 데이터 수집 |

---

### 3.3 실행 엔진 및 Action Tag 파서

에이전트는 코드 텍스트만 출력하는 대신, 시스템이 정의한 Action Tag를 발행하여 호스트 머신을 안전하게 조작한다 (`assets/prompts/system.md`).

```xml
<!-- 1. 파일 생성 및 덮어쓰기 -->
<create_file path="relative/or/absolute/path.ext">내용</create_file>

<!-- 2. 기존 파일 정밀 수정 (Fuzzy 매칭 지원) -->
<edit_file path="path/to/file.ext">
  <find>수정 대상 텍스트</find>
  <replace>새 텍스트</replace>
</edit_file>

<!-- 3. 파일 및 디렉토리 삭제 -->
<delete_file path="path/to/target"/>

<!-- 4. 파일 읽기 (행 번호 자동 주입, 최대 32KB) -->
<read_file path="path/to/file.ext"/>

<!-- 5. 파일 목록 조회 및 검색 -->
<list_files path="dir"/>
<glob pattern="**/*.tsx" path="."/>
<grep pattern="regex" path="src" files="*.ts"/>

<!-- 6. 터미널 명령 실행 (비동기, 타임아웃 25분) -->
<run_command>npm install express</run_command>

<!-- 7. OS 파일 탐색기 / 기본 앱 열기 -->
<reveal_in_explorer path="dist/index.html"/>
<open_file path="assets/preview.png"/>

<!-- 8. 두뇌 지식 및 웹 리서치 -->
<read_brain>30_Decisions/2026-09-decision.md</read_brain>
<read_url>https://html.duckduckgo.com/html/?q=검색어</read_url>
```

---

### 3.4 로컬 지식망 (P-Reinforce Second Brain) 및 동기화

1. **디렉토리 표준 구조:**
   - `00_Raw/`: 원시 스크랩, 웹 클리핑, 미정제 메모
   - `10_Wiki/`: 구조화된 지식 위키 및 개념 정리
   - `20_Projects/`: 프로젝트 계획서 및 태스크 목록
   - `30_Decisions/`: 의사결정 로그 (ADR 형태)
   - `40_템플릿/`: 코드 킷, 대시보드 템플릿, 랜딩페이지 템플릿
   - `_company/`: 회사 조직도, 에이전트 설정, 미션 목표
2. **Auto-Git Sync 파이프라인 (`_safeGitAutoSync`):**
   - 로컬 마크다운 생성 즉시 `git status` 확인
   - `git branch -M main` → `git add .` → `git commit -m "..."`
   - `git pull origin main -X ours` (충돌 발생 시 항상 로컬 데이터 우선)
   - `git push -u origin main` 자동 실행

---

### 3.5 로컬 HTTP 게이트웨이 사양 (Port 4825)

외부 웹 애플리케이션(Agent University / EZER AI)과 연동하기 위한 로컬 REST API:

| Method | Endpoint | 설명 |
| :--- | :--- | :--- |
| `GET` | `/ping` | 에이전트 활성화 상태 및 버전 확인 (Healthcheck) |
| `POST` | `/api/brain-inject` | 지식 팩(Brain Pack) 마크다운 파일을 로컬 두뇌에 주입 |
| `POST` | `/api/skill-inject` | 에이전트 전용 스킬(Python/TS 도구 스크립트) 주입 |
| `POST` | `/api/template-inject`| 프로젝트 보일러플레이트 템플릿 주입 |
| `POST` | `/api/evaluate` | 사용자 작업 산출물 자동 채점 및 평가 피드백 반환 |
| `GET` | `/api/evaluate-history`| 최근 평가 이력 조회 |

---

### 3.6 가상 오피스 캠퍼스 (`OfficePanel`)

- **그래픽 엔진:** HTML5 Canvas 기반의 2D 픽셀 아트 렌더러
- **에셋 번들링:** LimeZu Modern Interiors 스프라이트 팩 활용
- **인터랙션 및 애니메이션:**
  - 에이전트 상태(대기, 이동, 작업 중, 회의 중)에 따른 스프라이트 애니메이션
  - CEO의 작업 지시 시 책상 간 레이저 빔(Cyan/Violet) 및 파티클 발사 이펙트
  - 다중 에이전트 회의 모드 시 CEO 책상으로 에이전트들이 걸어오는(Walk) 시네마틱 연출
  - 각 에이전트 책상 클릭 시 1:1 대화 모달 오픈

---

## 4. 보안 및 예외 처리 정책 (Security & Fault Tolerance)

1. **파일 시스템 샌드박싱 (`_SYSTEM_PATH_BLOCKLIST`):**
   - `/etc`, `/System`, `/usr/bin`, `/sbin`, `/var/db` 등 Unix 시스템 경로 차단
   - `%WINDIR%` (`C:\Windows`), `%PROGRAMFILES%` (`C:\Program Files`) 등 윈도우 핵심 디렉토리 쓰기 차단
2. **Human-in-the-Loop 승인 큐 (`ApprovalsPanelProvider`):**
   - 파괴적 파일 삭제(`delete_file`) 또는 셸 명령 실행(`run_command`) 시 UI 승인 패널에 대기
   - 사용자가 직접 "승인" 또는 "거부" 버튼을 누르기 전까지 실행 일시 정지
3. **메모리 오버플로우 방지 (`system-specs.ts`):**
   - 머신 전체 RAM 중 OS 및 필수 프로세스용 여유분을 제외한 안전 모델 버짓(Apple Silicon 65%, Windows/Linux 50%)을 산출하여, 사양을 초과하는 70B 모델 등의 무리한 할당 차단
4. **스트리밍 타임아웃 및 Hang 감지:**
   - `streamFirstTokenTimeoutSec` (기본 240초): 저사양 머신의 콜드 스타트 고려
   - `streamIdleTimeoutSec` (기본 60초): 토큰 생성 간격 모니터링을 통한 모델 무한 대기 감지

---

## 5. 빌드 및 배포 명세 (Build & Packaging)

- **언어 및 런타임:** TypeScript 5.1.3 / Node.js 18+ (런타임 v24 지원)
- **번들러:** `esbuild` 0.28.0 (플랫폼: Node, 외부 모듈: `vscode`)
- **패키징 도구:** `@vscode/vsce` 4.0.0
- **산출물:** `out/extension.js` (1.4MB 단일 번들) 및 `connect-ai-lab-2.89.157.vsix` (11MB 설치 패키지)
