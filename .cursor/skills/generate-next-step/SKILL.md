---
name: generate-next-step
description: reports/ 폴더를 참조하여 다음 단계 노트북을 생성합니다.
---

# 다음 단계 노트북 생성 (generate-next-step)

## 동작 순서

1. `reports/pipeline_context.json` → `current_step` 확인
2. 해당 step의 참조 파일 읽기
3. 노트북 생성

---

## 파이프라인 (3 Steps)

| current_step | 생성할 노트북 | 참조 파일 |
|--------------|--------------|----------|
| `preprocess` | 02_preprocessing.ipynb | preprocessing_guide.md, step1_scan.json |
| `viz` | 03_visualization.ipynb | step2_preprocess.json |
| `state_analysis` | 04_state_analysis.ipynb | stats.md, step2_preprocess.json |

---

## Step 2: Preprocessing (02_preprocessing.ipynb)

### 목표
- QC (품질 관리)
- Big Five + Ideology + Honesty-Humility 점수 계산

### 필수 분석

**1. QC (Quality Control)**
- 응답 부족: `MIN_RESPONSES = 10` (고정값)
- Straight-lining: 모든 응답이 동일한 값인 경우 제외
- **결과 출력**: 제외된 인원 수, 유효 응답자 수

**2. Big Five 점수 계산**
- `superKey696.csv`에서 각 척도(NEO_O, NEO_C, NEO_E, NEO_A, NEO_N)의 문항 추출
- 역채점: key값이 -1인 문항은 `7 - 원점수`
- 척도 점수 = 해당 문항들의 평균
- **결과 출력**: 각 척도별 유효 N, Mean, SD

**3. Ideology 점수 계산**
- `Ideology = mean(z(MPQtr), z(NEOo6) * -1)`
- z-score 변환 후 평균
- **결과 출력**: 유효 N, Mean, SD

**4. Honesty-Humility 점수 계산**
- `Honesty_Humility = mean(z(NEOa2), z(NEOa4), z(HEXACO_H))`
- z-score 변환 후 평균
- **결과 출력**: 유효 N, Mean, SD

**5. 저장**
- `data/processed/sapa_scores.csv`에 RID + 7개 척도 저장

### 필수 출력 형식

```
=== QC 결과 ===
응답 부족 (10개 미만): N명
Straight-lining: N명
제외 합계: N명
유효 응답자: N명

=== 점수 계산 결과 ===
NEO_O: N=12345, M=4.31, SD=0.83
NEO_C: N=12345, M=4.23, SD=0.86
...
Ideology: N=12345, M=0.03, SD=0.97
Honesty_Humility: N=12345, M=-0.01, SD=0.73
```

---

## Step 3: Visualization (03_visualization.ipynb)

### 목표
- 7개 척도의 분포 및 상관관계 시각화

### 필수 분석

**1. 상관행렬**
- 7개 척도 간 상관 히트맵
- pairwise N 표시 (결측으로 인한 N 차이)

**2. 분포**
- Big Five: 히스토그램 (1-6점 범위)
- Ideology, Honesty-Humility: 히스토그램 (z-score, 0 기준선)

**3. 저장**
- PNG 파일로 저장

---

## Step 4: State Analysis (04_state_analysis.ipynb)

### 목표
- Lanning et al. (2022) 논문의 **State 수준 축소 재현**
- Critical Ratios로 각 State의 유의미한 성격 특징 도출

### 필수 분석 (논문 재현)

**1. 데이터 준비**
- `sapa_data.csv`에서 state 변수 로드
- `sapa_scores.csv`와 병합
- **"other" 제외** (9개 주만 분석: CA, FL, IL, MI, NY, PA, TX, VA, WA)

**2. State별 기술통계**
- 각 State × 척도별: N, Mean, SE
- SE = SD / sqrt(N)

**3. Critical Ratios 계산 (핵심)**
- `CR = (State Mean - Grand Mean) / SE`
- **|CR| > 3.0 → 유의미한 특징** (p < .003)

**4. 결과 출력 (필수 형식)**

```
=== State별 표본 수 ===
California: 1,713명
Michigan: 860명
...

=== 유의미한 특징 (|CR| > 3.0) ===
Michigan  | Honesty_Humility | CR=+4.31 | 높음
California | Ideology        | CR=-3.11 | 낮음
...

=== State 성격 프로필 요약 ===
Michigan: 정직-겸손↑, 우호성↑, 개방성↓
California: 정직-겸손↓, Ideology↓ (진보적)
New York: 개방성↑
Illinois: 외향성↑
Florida: 신경증↓ (정서적 안정)
```

### 불필요한 분석 (제외)
- ~~ANOVA~~ (논문에서 사용하지 않음)
- ~~효과 크기 (eta-squared)~~

---

## 노트북 공통 규칙

1. **첫 셀**: `%pip install pandas numpy matplotlib seaborn -q`
2. **작업 디렉토리**: notebooks에서 실행 시 상위로 이동
3. **상대 경로만 사용**: `data/raw/`, `reports/`
4. **결과는 반드시 위 형식대로 출력**
5. **마지막 셀**: step JSON 저장 + pipeline_context.json 업데이트

---

## 주의사항

### Ideology, Honesty-Humility 계산 시 index 정렬

QC 과정에서 일부 응답자를 제외하면 데이터의 index가 불연속적이 됩니다 (예: 0, 1, 3, 5, 7...). 새로 만든 scores DataFrame은 연속적인 index를 갖기 때문에, z-score 계산 결과를 할당할 때 반드시 .values를 사용해서 index 정보를 제거해야 합니다. 그렇지 않으면 값이 엉뚱한 위치에 할당되어 상관관계가 거의 0에 가깝게 나오는 오류가 발생합니다.

### 노트북 재실행 시 커널 재시작

이전 단계의 노트북을 수정하고 다시 실행한 후 다음 단계 노트북을 확인할 때는, 반드시 커널을 재시작(Restart Kernel)해야 합니다. 그렇지 않으면 메모리에 캐시된 이전 데이터가 사용되어 수정 사항이 반영되지 않습니다.
