# 🔍 Researcher — 개발자가 E2E 테스트에 즉시 사용할 수 있도록, MiniFunnel의 핵심 지표(HOMA-IR, hs-CRP 등)를 아우르는 다양한 시나리오 기반의 '테스트 데이터셋'을 50개 이상 준비해주세요. 이 데이터셋에는 임계치 경계를 넘나드는 노이즈성 데이터와, 급격한 상태 변화가 발생하는 극단적인 값들이 포함되어야 합니다.

🔍 Researcher: 작업 시작합니다.

CEO 지시사항과 현재 개발팀의 테스트 진행 상황을 종합했을 때, 가장 시급하고 가치가 높은 단일 작업은 **MiniFunnel이 예상치 못한 입력값이나 임계치를 넘나드는 극단적인 상태 변화에서도 시스템이 붕괴하지 않고 '위기 $\to$ 해결' 로직을 안정적으로 수행할 수 있도록 하는 방대한 테스트 데이터셋 구축**입니다.

현재 코다리 에이전트가 E2E 테스트를 실행했으므로, 이 테스트들이 성공적이든 실패적이든 관계없이, 그 결과를 분석하고 리팩토링하기 위한 '실탄' 역할을 할 대규모의 고난도 시나리오 데이터를 지금 당장 준비하는 것이 가장 가치 높은 다음 스텝입니다.

---

### 🔬 [CEO 지시] MiniFunnel E2E 테스트 데이터셋 (50+개 시나리오)

개발팀이 즉시 사용할 수 있도록, 핵심 생체지표(HOMA-IR, hs-CRP 등)를 아우르는 **고난도 임계치 경계 및 극단적 변화 시나리오** 60개 이상의 테스트 데이터셋을 구조화하여 제공합니다. 이 데이터는 단순한 정상/이상 판별을 넘어, 시스템이 '경고 $\to$ 위기 $\to$ 해결'의 상태 전이를 성공적으로 유도할 수 있는지 검증하는 데 중점을 두었습니다.

**📊 데이터 구성 지표 (Variables):**
*   `ID`: 테스트 케이스 식별자
*   `HOMA-IR`: 인슐린 저항성 지수 (Insulin Resistance)
*   `hs-CRP`: 고감도 C-반응성 단백질 (염증 수치)
*   `Blood_Glucose`: 혈당 수치 (mg/dL)
*   `BMI`: 체질량지수
*   `Sleep_Score`: 수면의 질 점수 (100점 만점, 낮을수록 나쁨)
*   `Expected_State`: 시스템이 감지해야 할 예상 상태 (Normal / Mild Risk / Crisis / Ambiguous)
*   `Target_Funnel_Trigger`: Funnel Mini-App이 작동해야 하는 핵심 트리거

**📋 테스트 시나리오 60+개 데이터셋 (CSV 형식)**

```csv
ID,HOMA-IR,hs-CRP,Blood_Glucose,BMI,Sleep_Score,Expected_State,Target_Funnel_Trigger
# =======================================================
# SECTION 1: 정상 범위 및 안정화 시나리오 (Normal Baseline - ID 001~005)
# 목표: Funnel이 작동할 필요가 없는 최적의 상태를 인식하는지 확인.
001,1.8,0.5,95,23.0,85,Normal,None
002,1.6,0.4,100,22.5,78,Normal,None
003,2.0,0.6,90,24.0,88,Normal,None
004,1.9,0.5,105,23.5,82,Normal,None
005,1.7,0.5,100,23.0,85,Normal,None

# =======================================================
# SECTION 2: 초기 경고/저위험군 시나리오 (Mild Risk - ID 006~015)
# 목표: Deep Crimson Red가 아닌 '주의' 단계의 콘텐츠를 노출하는지 확인. 임계치 근접 테스트.
006,2.3,0.7,110,24.5,75,Mild Risk,Dietary Guidance
007,2.8,0.9,115,25.0,70,Mild Risk,Stress Management
008,2.1,0.65,108,23.8,78,Mild Risk,Exercise Routine
009,2.4,0.8,112,24.2,72,Mild Risk,Supplement Check (Low Dose)
010,2.6,1.0,120,25.5,65,Mild Risk,Lifestyle Change Recommendation
011,3.0,1.2,125,26.0,60,Mild Risk,Initial Warning (Pre-Crisis)
012,2.7,1.1,118,24.8,68,Mild Risk,Monitoring Plan CTA
013,2.9,1.3,130,25.8,55,Mild Risk,Lifestyle Change Recommendation
014,2.2,0.7,115,24.0,70,Mild Risk,Dietary Guidance
015,2.5,0.9,120,25.2,68,Mild Risk,Supplement Check (Moderate Dose)

# =======================================================
# SECTION 3: 임계치 돌파/위기 감지 시나리오 (Crisis Detection - ID 016~025)
# 목표: Deep Crimson Red 경고 UI가 강제적으로 발동되어야 하는 핵심 구간 테스트.
016,4.5,1.8,150,27.0,30,Crisis,Deep Intervention (High Dose/Test Product X)
017,5.0,2.0,180,28.0,15,Crisis,Immediate Action Required (System Failure Alert)
018,6.2,2.5,200,30.0,5,Crisis,Emergency Consultation CTA
019,4.8,2.2,175,29.5,20,Crisis,Deep Intervention (High Dose/Test Product Y)
020,5.5,2.8,160,31.0,10,Crisis,Immediate Action Required (System Failure Alert)
021,4.1,1.9,145,27.5,35,Crisis,Deep Intervention (Product A Focus)
022,5.8,3.0,185,32.0,5,Crisis,Emergency Consultation CTA
023,6.5,3.5,210,33.0,1,Crisis,Highest Priority Alert Level
024,4.9,2.3,170,28.5,18,Crisis,Deep Intervention (Product B Focus)
025,5.2,2.6,165,30.5,12,Crisis,Immediate Action Required (System Failure Alert)

# =======================================================
# SECTION 4: 극단적/노이즈성 데이터 시나리오 (Edge Case & Noise - ID 026~040)
# 목표: 시스템의 안정성과 복원력(Resilience)을 극한으로 테스트. 현실적으로 발생하기 어려운 값 포함.
026,1.5,0.3,98,23.1,90,Normal,None (Noise Check 1 - Near Zero)
027,8.0,0.1,90,20.0,95,Ambiguous,None (Noise Check 2 - Low Biomarkers/High Score)
028,6.8,3.2,205,31.5,2,Crisis,Deep Intervention (Extreme combination)
029,7.5,3.5,215,32.5,0,Crisis,Highest Priority Alert Level (Worst Case)
030,4.0,1.5,130,26.0,N/A,Mild Risk,Error Handling Test (Missing Sleep Score)
031,2.9,0.7,118,24.0,70,Mild Risk,Boundary Check 1 (HOMA-IR 상한 경계)
032,5.1,1.9,165,29.0,25,Crisis,Boundary Check 2 (hs-CRP 임계치 돌파)
033,4.7,2.1,170,28.8,22,Crisis,Boundary Check 3 (HOMA+CRP 동시 상승)
034,6.0,2.5,190,30.0,15,Crisis,System Overload Test (Multiple High Values)
035,7.0,3.0,180,31.0,10,Crisis,Extreme Failure Simulation
036,2.0,0.4,95,23.0,80,Normal,None (Control Check - Perfect Normal)
037,1.8,0.5,98,23.5,85,Normal,None (Control Check 2)
038,3.5,1.0,120,25.0,60,Mild Risk,Boundary Check 4 (Glucose 상승 경계)
039,5.5,2.5,170,29.5,20,Crisis,Combined Failure Simulation
040,3.8,1.7,140,27.0,30,Mild Risk,Boundary Check 5 (Moderate Warning)

# =======================================================
# SECTION 5: 추가 테스트 및 예외 처리 시나리오 (Extended Testing - ID 041~065)
# 목표: 데이터 타입 오류, 누락 값, 복합적인 위기 상황을 다각도로 검증.
041,NULL,0.5,100,23.0,85,Normal,None (Missing HOMA-IR)
042,2.5,NULL,110,24.0,75,Mild Risk,Error Handling Test (Missing CRP)
043,3.0,1.0,120,25.0,60,Mild Risk,Boundary Check 6
044,6.1,2.9,188,30.8,18,Crisis,Near Peak Crisis (시스템 경고 임계치)
045,7.2,3.3,202,32.8,5,Crisis,Peak Crisis Simulation 1
046,6.9,3.6,215,33.2,3,Crisis,Peak Crisis Simulation 2 (Worst Case)
047,4.5,1.5,140,27.5,40,Mild Risk,Sleep Score Normalization Test (낮은 위험도에도 불구하고 수면 문제가 있는 경우)
048,2.0,0.5,90,22.0,85,Normal,None (Low BMI/Optimal)
049,1.7,0.3,95,21.5,90,Normal,None (Best Case Scenario)
050,3.3,1.2,135,26.5,50,Mild Risk,Combination Warning (High BMI + Medium HOMA)
051,4.8,2.2,170,29.0,15,Crisis,Deep Crimson Trigger Test 1
052,5.3,2.8,160,30.0,10,Crisis,Deep Crimson Trigger Test 2
053,4.0,1.8,145,27.0,25,Mild Risk,Pre-Intervention Warning
054,6.5,3.5,210,33.0,1,Crisis,Peak Crisis Simulation (Re-check)
055,5.0,2.0,180,28.0,15,Crisis,Deep Crimson Trigger Test 3
056,7.8,3.4,208,32.9,4,Crisis,Highest Priority Alert Level (Final Check)
057,2.1,0.6,105,23.5,80,Normal,None (Mid-Range Normal)
058,3.5,1.1,130,25.0,60,Mild Risk,Boundary Test 7
059,4.2,1.7,150,28.0,30,Crisis,Transition Warning (Mid-Level Crisis)
060,5.5,2.6,175,29.8,18,Crisis,Final Test Set - Comprehensive Failure

```

---

### 📝 다음 단계: 실행 계획 및 에이전트 분배

**가장 가치 있는 단일 작업:** MiniFunnel의 '상태 전이 로직'과 '예외 처리(Error Handling)'를 위한 E2E 테스트 환경 구축. (CEO 지시 이행)

**에이전트 분배:**
1. **Developer (코다리):** 위 데이터셋(`test_dataset.csv`로 저장 권장)을 즉시 받아, `MiniFunnel.tsx`의 상태 관리 및 에러 핸들링 로직을 리팩토링하고, 특히 4번 섹션(Edge Case)과 5번 섹션(예외 처리)에 대한 방어 코드를 추가해야 합니다.
2. **Researcher (나):** 데이터셋이 잘 사용될 수 있도록, 이 테스트 데이터를 기반으로 'MiniFunnel Mini-App의 핵심 가설'을 정의하고 이를 문서화하여 개발팀과 기획팀에게 공유하겠습니다.

<create_file path="test_dataset.csv">ID,HOMA-IR,hs-CRP,Blood_Glucose,BMI,Sleep_Score,Expected_State,Target_Funnel_Trigger
# =======================================================
# SECTION 1: 정상 범위 및 안정화 시나리오 (Normal Baseline - ID 001~005)
001,1.8,0.5,95,23.0,85,Normal,None
002,1.6,0.4,100,22.5,78,Normal,None
003,2.0,0.6,90,24.0,88,Normal,None
004,1.9,0.5,105,23.5,82,Normal,None
005,1.7,0.5,100,23.0,85,Normal,None

# =======================================================
# SECTION 2: 초기 경고/저위험군 시나리오 (Mild Risk - ID 006~015)
006,2.3,0.7,110,24.5,75,Mild Risk,Dietary Guidance
007,2.8,0.9,115,25.0,70,Mild Risk,Stress Management
008,2.1,0.65,108,23.8,78,Mild Risk,Exercise Routine
009,2.4,0.8,112,24.2,72,Mild Risk,Supplement Check (Low Dose)
010,2.6,1.0,120,25.5,65,Mild Risk,Lifestyle Change Recommendation
011,3.0,1.2,125,26.0,60,Mild Risk,Initial Warning (Pre-Crisis)
012,2.7,1.1,118,24.8,68,Mild Risk,Monitoring Plan CTA
013,2.9,1.3,130,25.8,55,Mild Risk,Lifestyle Change Recommendation
014,2.2,0.7,115,24.0,70,Mild Risk,Dietary Guidance
015,2.5,0.9,120,25.2,68,Mild Risk,Supplement Check (Moderate Dose)

# =======================================================
# SECTION 3: 임계치 돌파/위기 감지 시나리오 (Crisis Detection - ID 016~025)
016,4.5,1.8,150,27.0,30,Crisis,Deep Intervention (High Dose/Test Product X)
017,5.0,2.0,180,28.0,15,Crisis,Immediate Action Required (System Failure Alert)
018,6.2,2.5,200,30.0,5,Crisis,Emergency Consultation CTA
019,4.8,2.2,175,29.5,20,Crisis,Deep Intervention (High Dose/Test Product Y)
020,5.5,2.8,160,31.0,10,Crisis,Immediate Action Required (System Failure Alert)
021,4.1,1.9,145,27.5,35,Crisis,Deep Intervention (Product A Focus)
022,5.8,3.0,185,32.0,5,Crisis,Emergency Consultation CTA
023,6.5,3.5,210,33.0,1,Crisis,Highest Priority Alert Level
024,4.9,2.3,170,28.5,18,Crisis,Deep Intervention (Product B Focus)
025,5.2,2.6,165,30.5,12,Crisis,Immediate Action Required (System Failure Alert)

# =======================================================
# SECTION 4: 극단적/노이즈성 데이터 시나리오 (Edge Case & Noise - ID 026~040)
026,1.5,0.3,98,23.1,90,Normal,None
027,8.0,0.1,90,20.0,95,Ambiguous,None
028,6.8,3.2,205,31.5,2,Crisis,Deep Intervention (Extreme combination)
029,7.5,3.5,215,32.5,0,Crisis,Highest Priority Alert Level (Worst Case)
030,4.0,1.5,130,26.0,N/A,Mild Risk,Error Handling Test (Missing Sleep Score)
031,2.9,0.7,118,24.0,70,Mild Risk,Boundary Check 1 (HOMA-IR 상한 경계)
032,5.1,1.9,165,29.0,25,Crisis,Boundary Check 2 (hs-CRP 임계치 돌파)
033,4.7,2.1,170,28.8,22,Crisis,Boundary Check 3 (HOMA+CRP 동시 상승)
034,6.0,2.5,190,30.0,15,Crisis,System Overload Test (Multiple High Values)
035,7.0,3.0,180,31.0,10,Crisis,Extreme Failure Simulation
036,2.0,0.4,95,23.0,80,Normal,None
037,1.8,0.5,98,23.5,85,Normal,None
038,3.5,1.0,120,25.0,60,Mild Risk,Boundary Check 4 (Glucose 상승 경계)
039,5.5,2.5,170,29.5,20,Crisis,Combined Failure Simulation
040,3.8,1.7,140,27.0,30,Mild Risk,Boundary Check 5 (Moderate Warning)

# =======================================================
# SECTION 5: 추가 테스트 및 예외 처리 시나리오 (Extended Testing - ID 041~065)
041,NULL,0.5,100,23.0,85,Normal,None
042,2.5,NULL,110,24.0,75,Mild Risk,Error Handling Test (Missing CRP)
043,3.0,1.0,120,25.0,60,Mild Risk,Boundary Check 6
044,6.1,2.9,188,30.8,18,Crisis,Near Peak Crisis (시스템 경고 임계치)
045,7.2,3.3,202,32.8,5,Crisis,Peak Crisis Simulation 1
046,6.9,3.6,215,33.2,3,Crisis,Peak Crisis Simulation 2 (Worst Case)
047,4.5,1.5,140,27.5,40,Mild Risk,Sleep Score Normalization Test (낮은 위험도에도 불구하고 수면 문제가 있는 경우)
048,2.0,0.5,90,22.0,85,Normal,None
049,1.7,0.3,95,21.5,90,Normal,None
050,3.3,1.2,135,26.5,50,Mild Risk,Combination Warning (High BMI + Medium HOMA)
051,4.8,2.2,170,29.0,15,Crisis,Deep Crimson Trigger Test 1
052,5.3,2.8,160,30.0,10,Crisis,Deep Crimson Trigger Test 2
053,4.0,1.8,145,27.0,25,Mild Risk,Pre-Intervention Warning
054,6.5,3.5,210,33.0,1,Crisis,Peak Crisis Simulation (Re-check)
055,5.0,2.0,180,28.0,15,Crisis,Deep Crimson Trigger Test 3
056,7.8,3.4,208,32.9,4,Crisis,Highest Priority Alert Level (Final Check)
057,2.1,0.6,105,23.5,80,Normal,None
058,3.5,1.1,130,25.0,60,Mild Risk,Boundary Test 7
059,4.2,1.7,150,28.0,30,Crisis,Transition Warning (Mid-Level Crisis)
060,5.5,2.6,175,29.8,18,Crisis,Final Test Set - Comprehensive Failure

</create_file>

📊 평가: 완료 — CEO 지시사항에 따라 MiniFunnel E2E 테스트의 핵심 기반이 될 고난도 시나리오 데이터셋을 생성하고 파일 시스템에 저장했습니다.
📝 다음 단계: Developer(코다리)에게 위 `test_dataset.csv` 파일을 전달하여, 리팩토링된 Funnel 로직과 함께 이 데이터셋으로 단위/통합 테스트를 즉시 진행할 것을 지시합니다.

---
## 📁 파일 액션 결과

✅ 생성: c:\Data\Project\connect-ai\test_dataset.csv
