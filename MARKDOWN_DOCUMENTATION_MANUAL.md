# 📚 Connect AI 프로젝트 마크다운(.md) 전수 분석 및 상세 가이드북
# (Comprehensive Markdown Documentation & Specifications Manual)

> **문서 버전:** 2.89.157  
> **분석 대상:** Connect AI 프로젝트 내 45개 마크다운 파일 전체  
> **작성 일자:** 2026-09-19  
> **목적:** 프로젝트에 포함된 모든 마크다운 문서의 핵심 내용, 구조, 상호 연관성 및 실전 활용법 총정리  

---

## 📑 목차 (Table of Contents)

1. [개요 및 마크다운 파일 분류 체계](#1-개요-및-마크다운-파일-분류-체계)
2. [루트 핵심 가이드 & 아키텍처 문서 (8종)](#2-루트-핵심-가이드--아키텍처-문서-8종)
3. [지식 베이스 & 브레인 팩 (Brain Pack) 문서 (2종)](#3-지식-베이스--브레인-팩-brain-pack-문서-2종)
4. [프롬프트 엔지니어링 & 에이전트 페르소나 규격 (10종)](#4-프롬프트-엔지니어링--에이전트-페르소나-규격-10종)
5. [에이전트 전문 도구 스펙 (Tool Seeds, 20종)](#5-에이전트-전문-도구-스펙-tool-seeds-20종)
6. [개발자 스타터 킷 템플릿 문서 (Brain Seeds, 4종)](#6-개발자-스타터-킷-템플릿-문서-brain-seeds-4종)
7. [에셋 라이선스 명세 (1종)](#7-에셋-라이선스-명세-1종)
8. [문서 간 상호작용 매트릭스 & 실전 활용 로드맵](#8-문서-간-상호작용-매트릭스--실전-활용-로드맵)

---

## 1. 개요 및 마크다운 파일 분류 체계

Connect AI 프로젝트는 단순한 코드 저장소가 아니라, 에이전트의 지식, 프롬프트, 도구 명세, 시연 시나리오, 학술 교육 자료가 마크다운(.md) 형식으로 표준화된 **자율 지식 생태계**로 구축되어 있습니다. 총 45개의 마크다운 파일은 다음과 같이 6개 그룹으로 분류됩니다.

```
Connect AI 마크다운 체계 (45개)
├── 1. 루트 핵심 가이드 (8) ── README, ARCHITECTURE, DESIGN_SPEC, SHOWCASE, PLAZA, PRESENTATION, SLIDES, 튜토리얼
├── 2. 브레인 팩/지식 (2) ──── MrBeast_Premium_10, MrBeast_Data_Brain
├── 3. 프롬프트 규격 (10) ──── system, ceo-*, confer, decisions-extract, secretary-*, skill-distill
├── 4. 도구 명세 (20) ─────── business(1), developer(5), editor(3), secretary(3), youtube(8)
├── 5. 템플릿 킷 (4) ──────── dashboard-kit, landing-kit, mobile-kit, portfolio-kit
└── 6. 에셋 라이선스 (1) ──── LICENSE-ASSETS
```

---

## 2. 루트 핵심 가이드 & 아키텍처 문서 (8종)

### 2.1 `README.md`
- **목적:** 프로젝트의 공식 대표 소개 문서.
- **핵심 내용:**
  - Connect AI v2 (P-Reinforce)의 정체성: 100% 로컬, 100% 오프라인 자율 지식 엔진.
  - 4대 코어 기능: Agent University(A.U) 지식 주입 연동, 제로 인터랙션 지식 구조화, Auto-Git Sync 100%, 설치형 모델 자동 감지(Ollama/LM Studio).
  - 설치 및 빌드 방법(`npm install`, `npm run compile`, `vsce package`).
  - LM Studio 및 Ollama 로컬 엔진 구동 가이드.

### 2.2 `ARCHITECTURE.md`
- **목적:** Brain-GitHub 자동 동기화 및 설정 아키텍처 레퍼런스.
- **핵심 내용:**
  - VS Code 전역 설정 키 명세(`localBrainPath`, `secondBrainRepo`, `ollamaUrl`, `defaultModel` 등).
  - 동기화 핵심 함수: `_safeGitAutoSync` (지식 주입 후 자동 백업), `_syncSecondBrain` (수동 동기화 트리거).
  - 지식 주입(`4825/api/brain-inject`)부터 GitHub `git pull/push`까지의 데이터 흐름도.

### 2.3 `DESIGN_SPECIFICATION.md`
- **목적:** 정식 소프트웨어 시스템 설계명세서 (Software Design Specification).
- **핵심 내용:**
  - 시스템 5대 설계 철학, 전체 블록 다이어그램.
  - 21,800줄의 `src/extension.ts` 및 하위 모듈(`agents.ts`, `paths.ts`, `plaza.ts`, `system-specs.ts`)의 상세 스펙.
  - Action Tag 파서 규칙, 승인 큐(Human-in-the-loop) 보안 정책, 로컬 HTTP 엔드포인트 명세.

### 2.4 `SHOWCASE_GUIDE.md`
- **목적:** 7분 완결형 라이브 시연 시나리오 풀 가이드.
- **핵심 내용:**
  - **시연 전 체크리스트:** VSIX 설치, Window Reload, `curl http://127.0.0.1:4825/ping` 검증.
  - **ACT 1 (오프라인 충격):** 와이파이를 물리적으로 끄고도 로컬 LLM이 즉시 응답하는 순간.
  - **ACT 2 (비코더의 게임 제작):** "코다리야 병아리 게임 만들어줘" → 30초 만에 브라우저에 다마고치 웹게임 실행.
  - **ACT 3 (회의 시네마틱):** CEO 책상으로 레오와 현빈이 걸어와 전략 회의를 수행하는 가상 오피스 연출.
  - **ACT 4 (매출 대시보드):** 카운트업 애니메이션과 도넛 차트를 통한 실시간 PayPal 매출 확인.
  - **ACT 5 (네온 서바이버):** Vampire Survivors 풍의 고급 웹게임을 자동 스캐폴딩하고 실행.

### 2.5 `PLAZA_SETUP.md`
- **목적:** 다중 사용자 회사 간 네트워킹 공간인 "에이전트 광장(Agent Plaza)" 셋업 가이드.
- **핵심 내용:**
  - GCP Firebase Realtime Database를 중앙 통신 버스로 활용하는 Layer 2 연동 아키텍처.
  - "비서 = 단일 브릿지" 원칙: 전문가는 로컬에 머물고, 비서(영숙)가 회사를 대표하여 타 회사 비서와 대화.
  - 3초 주기 폴링 및 15초 주기 프레즌스 하트비트 전송 구조.

### 2.6 `PRESENTATION.md`
- **목적:** 키노트 및 학술/투자 발표용 슬라이드 콘텐츠.
- **핵심 내용:**
  - 클라우드 AI의 3대 한계(비용, 프라이버시, 인터넷 의존) 극복 방안.
  - Multi-Agent System (MAS)의 학술적 배경: 분산 인지(Decentralized Cognition), 계층적 오케스트레이션.
  - 실시간 데이터 프리페치(Prefetch)를 통한 환각(Hallucination) 원천 차단 기법.

### 2.7 `EDUCATIONAL_SLIDES.md`
- **목적:** 대학 학부 AI/SW 강의 수준의 심층 교육 슬라이드 세트.
- **핵심 내용:**
  - **Group A (LLM 기본 원리):** 토큰화(Tokenization), Transformer Self-Attention 메커니즘, 4-bit 양자화(Quantization) 수학적 원리.
  - **Group B (에이전틱 엔지니어링):** ReAct 루프, 도구 호출(Tool Calling)과 정규식 기반 태그 파싱, 로컬 파일 시스템 샌드박싱.
  - **Group C (멀티에이전트 설계):** 작업 분해(Task Decomposition), 비동기 회의(Deliberation), 24시간 자율 사이클 구조.

### 2.8 `튜토리얼_비서_연결.md`
- **목적:** 비전문가도 10분 만에 완료하는 텔레그램 봇 및 구글 캘린더 연동 튜토리얼.
- **핵심 내용:**
  - BotFather를 통한 텔레그램 봇 생성 및 Connect AI 마법사 연결 (Chat ID 자동 감지).
  - Google Calendar OAuth 2.0 권한 획득 절차.
  - 자연어 명령 예시집: "내일 3시 광고주 미팅 잡아줘", "오늘 일정 뭐야?", "할 일 목록 확인해줘".

---

## 3. 지식 베이스 & 브레인 팩 (Brain Pack) 문서 (2종)

### 3.1 `src/MrBeast_Premium_10.md`
- **규모:** 158KB 대형 데이터셋
- **내용:** 세계 1위 유튜버 MrBeast의 최신 10개 영상에 대한 초정밀 리버스 엔지니어링 데이터.
- **구성 요소:** 영상별 고유 ID, 썸네일 URL, 게시일, 조회수/좋아요/댓글 수 지표, 전체 음성 전사 스크립트(Transcript), 후크(Hook) 문장 분석.
- **역할:** 유튜브 전문 에이전트(레오)가 콘텐츠 기획 및 제목/썸네일 도출 시 벤치마킹하는 최상위 골드 스탠다드 지식 베이스.

### 3.2 `.secondbrain/00_Raw/2026-04-16/MrBeast_Data_Brain.md`
- **내용:** 로컬 두뇌(`00_Raw`)에 적재된 MrBeast 영상 데이터의 초기 원시 인텔리전스 파일.
- **역할:** P-Reinforce 엔진이 원시 데이터를 읽어 `10_Wiki`와 `🚀 Skills`로 지식을 추출·정제하는 입력 소스로 활용.

---

## 4. 프롬프트 엔지니어링 & 에이전트 페르소나 규격 (10종)

`assets/prompts/` 디렉토리에 위치하며, LLM에게 행동 지침과 출력 스키마를 부여합니다.

| 파일명 | 대상 역할 | 핵심 지침 및 입출력 규격 |
| :--- | :--- | :--- |
| `system.md` | **전체 시스템** | 10대 Action Tag(`<create_file>`, `<edit_file>`, `<run_command>` 등) 선언 및 경로 보안 규칙 |
| `ceo-chat.md` | **CEO** | 사장님에 대한 보고 톤, 간결한 요약, 선제적 액션 제안 지침 |
| `ceo-classifier.md` | **CEO 라우터** | 사용자 입력의 의도(단순 대화, 코딩, 기획, 데이터 분석 등)를 초고속 분류 |
| `ceo-planner.md` | **CEO 플래너** | **최소 동원 원칙** 적용. 작업에 필요한 에이전트만 정밀 선별하여 Strict JSON 형식으로 출력 |
| `ceo-report.md` | **CEO 리포터** | 24시간 자율 사이클 또는 프로젝트 완료 시 최종 성과 브리핑 템플릿 |
| `confer.md` | **다중 에이전트** | 에이전트 간 1:1 또는 다자간 상호 검토, 피드백, 협업 회의 프로토콜 |
| `decisions-extract.md` | **지식 정원사** | 대화 및 작업 로그에서 핵심 비즈니스·기술 의사결정(ADR)을 자동 추출 |
| `secretary-telegram.md` | **비서 (영숙)** | 텔레그램 모바일 환경에 최적화된 친근한 어조, 불릿 포인트 기반 요약, 일정 관리 응답 |
| `secretary-triage.md` | **비서 트리거** | 외부 알림 및 인바운드 메시지의 긴급도(긴급/통상/무시) 자동 분류 |
| `skill-distill.md` | **스킬 추출기** | 방금 수행한 성공적인 작업 결과물을 영구 재사용 가능한 스킬 템플릿으로 변환 |

---

## 5. 에이전트 전문 도구 스펙 (Tool Seeds, 20종)

`assets/tool-seeds/` 디렉토리에 위치하며, 각 에이전트가 실제로 실행하는 Python/Node 스크립트와 실행 가이드입니다.

### 5.1 Business (비즈니스 - 현빈)
- `paypal_revenue.md`: PayPal REST API를 호출하여 최근 30일간의 트랜잭션, 누적 매출, 환불율을 집계하고 대시보드 데이터 포맷으로 정제.

### 5.2 Developer (개발자 - 코다리)
- `lint_test.md`: ESLint 및 단위 테스트를 백그라운드에서 실행하고 실패 지점을 코다리에게 피드백하는 자기 검증 루프 도구.
- `pack_apply.md`: 압축된 프로젝트 보일러플레이트 팩을 지정된 디렉토리에 자동 압축 해제 및 의존성 구성.
- `pwa_setup.md`: 웹 애플리케이션에 매니페스트(`manifest.json`)와 서비스 워커를 주입하여 오프라인 PWA로 변환.
- `web_init.md`: Vite + React + TypeScript 기반의 초경량 웹 프로젝트 즉시 스캐폴딩.
- `web_preview.md`: 로컬 개발 서버를 가동하고 브라우저를 자동 오픈하여 결과를 사용자에게 시각적으로 제시.

### 5.3 Editor (사운드/영상 - 루나)
- `music_generate.md`: 로컬 MusicGen 또는 ACE-Step AI 모델을 구동하여 분위기별 맞춤형 BGM 자동 작곡.
- `music_studio_setup.md`: 로컬 머신에 오디오 합성 라이브러리(PyTorch, Torchaudio, SoundFile) 자동 세팅.
- `music_to_video.md`: FFmpeg를 사용하여 생성된 BGM을 영상 소스와 완벽한 볼륨 밸런스로 자동 합성.

### 5.4 Secretary (비서 - 영숙)
- `google_calendar.md`: Google Calendar API를 통해 오늘의 일정 목록과 비는 시간대를 파악.
- `google_calendar_write.md`: 자연어로 요청된 미팅을 Google Calendar에 신규 등록하거나 기존 일정 변경/삭제.
- `telegram_setup.md`: 텔레그램 봇 토큰 유효성 검사 및 웹훅/폴링 파이프라인 개설.

### 5.5 YouTube (유튜브 - 레오)
- `auto_planner.md`: 채널 컨셉과 최신 트렌드를 결합하여 월간 콘텐츠 발행 캘린더 자동 수립.
- `channel_full_analysis.md`: YouTube Analytics API를 통해 시청 시간, 평균 조회율(AVD), 구독자 전환율 정밀 진단.
- `comment_harvester.md`: 최근 영상의 시청자 댓글을 수집하여 감성 분석 및 차기 콘텐츠 아이디어 도출.
- `competitor_brief.md`: 지정한 경쟁 채널의 최근 업로드 목록과 이상 급등(Outlier) 영상을 감지하여 요약.
- `my_videos_check.md`: 업로드된 영상들의 썸네일, 제목, 태그, 디스크립션 완성도를 SEO 관점에서 검사.
- `telegram_notify.md`: 유튜브 채널의 주요 마일스톤(조회수 10만 돌파 등) 달성 시 텔레그램으로 축하 알림 발송.
- `trend_sniper.md`: 특정 키워드의 검색 급상승 트렌드를 포착하여 선제적 영상 기획 제안.
- `youtube_account.md`: YouTube Data API v3 연동을 위한 OAuth 인증 토큰 발급 및 갱신.

---

## 6. 개발자 스타터 킷 템플릿 문서 (Brain Seeds, 4종)

`assets/brain-seeds/40_템플릿/developer/`에 위치하며, 코다리가 사용자 요청 시 단 몇 초 만에 실제 앱으로 조립해내는 완성형 템플릿 명세입니다.

| 템플릿 명칭 | 문서 파일 | 제공 컴포넌트 및 용도 |
| :--- | :--- | :--- |
| **Dashboard Kit** | `dashboard-kit/README.md` | 사이드바, 상단 바, 통계 카드(`StatsCards`), 최근 내역 테이블(`RecentTable`)을 갖춘 관리자 대시보드 |
| **Landing Kit** | `landing-kit/README.md` | 히어로 섹션, 특장점, 요금제 테이블(`Pricing`), FAQ, CTA, 푸터를 갖춘 고전환율 랜딩페이지 |
| **Mobile Kit** | `mobile-kit/README.md` | 홈 스크린, 프로필 스크린, 세팅 스크린 및 탭 네비게이션을 포함한 모바일 웹/PWA 킷 |
| **Portfolio Kit** | `portfolio-kit/README.md` | 소개, 보유 기술 스택 태그, 프로젝트 갤러리, 문의 폼을 갖춘 1인 개발자 쇼케이스 웹사이트 |

---

## 7. 에셋 라이선스 명세 (1종)

### 7.1 `assets/pixel/LICENSE-ASSETS.md`
- **저작권자:** LimeZu (Modern Interiors / Modern Office Revamped Pack)
- **내용:** Connect AI 가상 사무실(OfficePanel)에 탑재된 픽셀 아트 타일셋 및 캐릭터 스프라이트의 정식 상업용/비상업용 이용 허가 조건 명시.
- **조건:** 재배포 금지, 프로젝트 내 번들 형태의 합법적 사용 보장.

---

## 8. 문서 간 상호작용 매트릭스 & 실전 활용 로드맵

### 8.1 런타임 데이터 및 프롬프트 흐름도

```
[사용자 입력] 
     │
     ▼
[assets/prompts/system.md] (기본 액션 태그 규칙 주입)
     │
     ▼
[assets/prompts/ceo-planner.md] (의도 분석 및 에이전트 선별)
     │
     ├─▶ 유튜브 작업: [assets/tool-seeds/youtube/*.md] + [MrBeast_Premium_10.md 지식]
     ├─▶ 코딩 작업:   [assets/tool-seeds/developer/*.md] + [assets/brain-seeds/40_템플릿/*]
     ├─▶ 일정 작업:   [assets/tool-seeds/secretary/*.md] + [assets/prompts/secretary-*.md]
     └─▶ 비즈니스:   [assets/tool-seeds/business/*.md]
     │
     ▼
[src/extension.ts 액션 파서] (실제 터미널 명령 및 파일 쓰기 실행)
     │
     ▼
[ARCHITECTURE.md의 _safeGitAutoSync] (SecondBrain 폴더에 영구 보관 & GitHub 백업)
```

### 8.2 사용자 실전 활용 가이드
1. **처음 사용하는 경우:** [`README.md`](file:///c:/Data/Project/connect-ai/README.md) 및 [`튜토리얼_비서_연결.md`](file:///c:/Data/Project/connect-ai/튜토리얼_비서_연결.md)를 먼저 확인하여 기본 환경을 구성합니다.
2. **시연 및 데모를 준비하는 경우:** [`SHOWCASE_GUIDE.md`](file:///c:/Data/Project/connect-ai/SHOWCASE_GUIDE.md)의 5개 Act 동선을 따라 리허설합니다.
3. **내부 아키텍처 및 시스템 확장을 개발하는 경우:** [`DESIGN_SPECIFICATION.md`](file:///c:/Data/Project/connect-ai/DESIGN_SPECIFICATION.md)와 [`ARCHITECTURE.md`](file:///c:/Data/Project/connect-ai/ARCHITECTURE.md)를 참고하여 모듈을 확장합니다.
4. **강의나 발표를 진행하는 경우:** [`PRESENTATION.md`](file:///c:/Data/Project/connect-ai/PRESENTATION.md) 및 [`EDUCATIONAL_SLIDES.md`](file:///c:/Data/Project/connect-ai/EDUCATIONAL_SLIDES.md)의 슬라이드 마크다운을 복사하여 발표 자료로 활용합니다.
