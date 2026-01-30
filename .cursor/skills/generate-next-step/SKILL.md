---
name: generate-next-step
description: reports/ 폴더의 모든 파일을 누적 참조하여 다음 단계 노트북을 생성합니다. "다음 단계", "노트북 만들어줘" 요청 시 사용합니다.
---

# 다음 단계 코드 생성 (generate-next-step)

## 목적

`reports/` 폴더의 **모든 파일을 누적 참조**하여 다음 단계 노트북을 생성합니다.

---

## 핵심: reports/ 폴더 누적 참조

### 파일 구조

```
reports/
├── preprocessing_guide.md      ← ① 항상 참조 (전처리 가이드)
├── stats.md                    ← ② 항상 참조 (통계 분석 가이드)
├── pipeline_context.json       ← ③ 현재 상태 (current_step)
├── step1_scan.json             ← ④ Step 1 결과
├── step2_preprocess.json       ← ⑤ Step 2 결과 (있으면)
├── step3_viz.json              ← ⑥ Step 3 결과 (있으면)
└── step4_state.json            ← ⑦ Step 4 결과 (있으면)
```

### AI Agent 동작 방식

```
1. reports/preprocessing_guide.md 읽음 (전처리 로직)
2. reports/stats.md 읽음 (통계 분석 방법론)
3. reports/pipeline_context.json 읽음 (current_step 확인)
4. reports/step*.json 파일들 모두 읽음 (이전 결과들)
5. 모든 정보 종합하여 다음 노트북 생성
```

---

## 파이프라인 구조 (4 Steps)

| current_step | 참조할 파일 | 생성할 노트북 |
|--------------|-------------|--------------|
| `"preprocess"` | preprocessing_guide.md + step1_scan.json | 02_preprocessing.ipynb |
| `"viz"` | 위 + step2_preprocess.json | 03_visualization.ipynb |
| `"state_analysis"` | 위 + stats.md + step3_viz.json | 04_state_analysis.ipynb |
| `"done"` | - | 완료 메시지 |

---

## Step별 생성 규칙

### Step 2 (Preprocessing) 생성 시

**참조 파일:**
- `preprocessing_guide.md` - 점수 계산 공식
- `step1_scan.json` - n_respondents, avg_responses

**step1_scan.json에서 가져올 정보:**
```python
with open('reports/step1_scan.json', 'r') as f:
    step1 = json.load(f)

avg_responses = step1['results']['avg_responses']  # 86
MIN_RESPONSES = max(10, int(avg_responses * 0.1))  # 10
```

**생성할 내용:**
- QC 기준: step1 결과 기반
- 점수 계산: preprocessing_guide.md 공식
- Big Five + Ideology + Honesty-Humility

### Step 3 (Visualization) 생성 시

**참조 파일:**
- `step1_scan.json` - 기본 정보
- `step2_preprocess.json` - 계산된 척도 목록, output_file

**step2_preprocess.json에서 가져올 정보:**
```python
with open('reports/step2_preprocess.json', 'r') as f:
    step2 = json.load(f)

scales = step2['results']['scores']['calculated_scales']
scores_file = step2['results']['scores']['output_file']
```

**생성할 내용:**
- 상관행렬 (7개 척도)
- 분포 히스토그램
- 박스플롯

### Step 4 (State Analysis) 생성 시

**참조 파일:**
- `stats.md` - 통계 분석 방법론 (Critical Ratios, ANOVA 등)
- `step2_preprocess.json` - 계산된 척도, 점수 파일 경로
- `step3_viz.json` - 시각화 결과

**stats.md에서 참조할 분석 방법:**
- Critical Ratios: |z|/se > 3.0 기준으로 유의미한 특징 판별
- ANOVA: State 간 성격 점수 차이 검정
- (논문 축소 버전: County-Composites 대신 State 수준 분석)

**필요한 데이터:**
```python
# 원본 데이터에서 state 변수 로드
data = pd.read_csv('data/raw/sapa_data.csv')
scores = pd.read_csv('data/processed/sapa_scores.csv')

# state 변수: CA, FL, IL, MI, NY, PA, TX, VA, WA, other
# demographic codes.txt 참조
```

**생성할 내용:**
1. State 변수 확인 및 분포
2. State별 성격 점수 기술통계 (Mean, SE)
3. ANOVA 분석 (State 간 차이 검정)
4. Critical Ratios 계산 (|Mean|/SE > 3.0)
5. State별 성격 프로필 시각화 (박스플롯, 히트맵)

**코드 템플릿:**
```python
# State별 기술통계
state_stats = scores.merge(data[['RID', 'state']], on='RID')
state_summary = state_stats.groupby('state')[scales].agg(['mean', 'std', 'count'])

# Standard Error 계산
for scale in scales:
    state_summary[(scale, 'se')] = state_summary[(scale, 'std')] / np.sqrt(state_summary[(scale, 'count')])

# Critical Ratio 계산
for scale in scales:
    state_summary[(scale, 'cr')] = abs(state_summary[(scale, 'mean')]) / state_summary[(scale, 'se')]
    
# 유의미한 특징 (|CR| > 3.0)
significant = state_summary.xs('cr', axis=1, level=1) > 3.0
```

---

## 노트북 시작 부분 템플릿

```python
import pandas as pd
import numpy as np
import json
import os
from glob import glob

# 작업 디렉토리 설정
if os.path.basename(os.getcwd()) == 'notebooks':
    os.chdir('..')

# reports/ 폴더의 모든 JSON 파일 로드
print("=== 참조할 Context 파일들 ===")
for f in sorted(glob('reports/*.json')):
    print(f"  - {f}")

# 이전 단계 결과 로드
if os.path.exists('reports/step1_scan.json'):
    with open('reports/step1_scan.json', 'r', encoding='utf-8') as f:
        step1 = json.load(f)
    print(f"\nStep 1 결과: {step1['results']}")

if os.path.exists('reports/step2_preprocess.json'):
    with open('reports/step2_preprocess.json', 'r', encoding='utf-8') as f:
        step2 = json.load(f)
    print(f"\nStep 2 결과: {step2['results']['scores']['calculated_scales']}")
```

---

## 코드 스타일 규칙

```python
# 1. 상대 경로만 사용
df = pd.read_csv('data/raw/sapa_data.csv')

# 2. 이전 step 결과 참조
with open('reports/step1_scan.json', 'r') as f:
    step1 = json.load(f)
n_respondents = step1['results']['n_respondents']

# 3. 한글 주석
# Step 1 결과에서 평균 응답 수 가져오기

# 4. 진행 상황 출력
print(f'✅ 이전 단계에서 {n_respondents:,}명 데이터 확인됨')
```

---

## 노트북 구조 규칙

```
[Cell 0] Markdown: 제목 + 학습 목표 + 참조 파일 목록
[Cell 1] Code: %pip install
[Cell 2] Code: import + reports/*.json 로드
[Cell 3~N] Code/Markdown: 본문
[마지막 Cell] Code: 새 step JSON 파일 저장
```

---

## AI Agent 체크리스트

노트북 생성 전 확인:

- [ ] `reports/preprocessing_guide.md` 읽었는가?
- [ ] `reports/stats.md` 읽었는가? (Step 4용)
- [ ] `reports/pipeline_context.json`에서 current_step 확인했는가?
- [ ] `reports/step*.json` 파일들 모두 확인했는가?
- [ ] 이전 step 결과를 코드에서 참조하는가?
- [ ] 마지막 셀에 새 step JSON 저장 코드 있는가?

---

## 사용 예시

### 예시 1: Step 2 생성
```
사용자: "다음 단계 만들어줘"

AI Agent:
1. reports/ 폴더 스캔
   - preprocessing_guide.md ✓
   - pipeline_context.json → current_step: "preprocess"
   - step1_scan.json ✓ (avg_responses: 86)
   
2. 02_preprocessing.ipynb 생성
   - step1_scan.json 참조하여 QC 기준 설정
   - preprocessing_guide.md 참조하여 점수 계산
   
3. 마지막 셀: step2_preprocess.json 저장 코드 포함
```

### 예시 2: Step 4 (State Analysis) 생성
```
사용자: "다음 단계 만들어줘"

AI Agent:
1. reports/ 폴더 스캔
   - preprocessing_guide.md ✓
   - stats.md ✓ (통계 분석 방법론)
   - pipeline_context.json → current_step: "state_analysis"
   - step1_scan.json ✓
   - step2_preprocess.json ✓ (7개 척도)
   - step3_viz.json ✓
   
2. 04_state_analysis.ipynb 생성
   - stats.md의 Critical Ratios 방법론 적용
   - State별 (9개 주 + other) 성격 점수 비교
   - ANOVA + Critical Ratio 분석
   
3. 마지막 셀: step4_state.json 저장 코드 포함
```
