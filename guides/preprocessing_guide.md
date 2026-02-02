# SAPA Project & American Nations 데이터 전처리 파이프라인

## 1. 데이터 구조 (변수 설명)
이 데이터는 **SAPA(Synthetic Aperture Personality Assessment)** 기법을 사용하여 수집되었습니다. 참가자들은 전체 문항 풀에서 무작위로 추출된 하위 집합(subset)에만 응답했습니다.

*   **기본 정보:** 약 75,716명의 참가자 데이터 (2013~2017년 수집) [1].
*   **성격 변수 (Items):** 총 696개의 IPIP(International Personality Item Pool) 문항.
    *   **척도:** 1(매우 부정확함) ~ 6(매우 정확함)의 6점 리커트 척도 [2], [3].
    *   **구성:** IPIP-NEO, IPIP-HEXACO, IPIP-MPQ 등 다양한 성격 검사 도구의 문항 혼합 [4].
*   **인구통계 변수 (Demographics):**
    *   `RID`: 무작위 생성된 참가자 고유 ID [5].
    *   `age`, `gender` (1=남성, 2=여성), `education` (교육 수준), `ethnic` (인종/민족) [5], [6].
    *   **지리 정보:** 미국 참가자의 우편번호(ZIP code)를 기반으로 카운티(County) 수준으로 매핑 [7], [1].

## 2. 점수 계산 방법
`psych` R 패키지를 사용하여 항목 수준의 데이터를 78개의 하위 척도 및 상위 요인 점수로 변환했습니다 [8].

### ⚠️ 중요: 파일 인코딩
**모든 CSV 파일 읽기/쓰기 시 `encoding='utf-8'`를 명시해야 합니다.**
- 다른 환경(Windows, Linux, Mac)에서도 인코딩 오류를 방지합니다.
- 예: `pd.read_csv('file.csv', encoding='utf-8')`
- 예: `df.to_csv('file.csv', encoding='utf-8')`

### Big Five 및 주요 성격 요인
*   **계산 방식:** `superKey696.csv`와 같은 채점 키(scoring matrix)를 사용하여 각 요인에 해당하는 문항들의 평균을 계산합니다.
*   **사용 척도:** IPIP-NEO와 IPIP-HEXACO의 도메인 점수를 사용했습니다.
    *   **Extraversion (외향성):** IPIP-NEO Extraversion + IPIP-HEXACO Extraversion (역채점 포함) [8].
    *   **Agreeableness (우호성) & Emotionality (정서성):** 유사한 방식으로 해당 도메인 점수 통합 [8].

### Ideology (이념) 계산식
보수적 이념(Conservative Ideology) 점수는 다음 두 척도의 표준화된 점수(z-score)를 평균하여 산출했습니다 [8].
> **Ideology Score** = mean( z(IPIP-MPQ Conservatism), z(IPIP-NEO Liberalism * -1) )
*   *참고: IPIP-NEO Liberalism(개방성 하위 요인 O6)은 역채점(Reversed)하여 보수성 지표로 변환함.*

### Honesty-Humility (정직-겸손) 계산식
다음 세 가지 척도의 표준화된 점수를 평균하여 산출했습니다 [8].
> **H-H Score** = mean( z(IPIP-NEO Morality[A2]), z(IPIP-NEO Modesty[A4]), z(IPIP-HEXACO Honesty-Humility) )

## 3. 역채점 문항 목록
채점 키 파일(`superKey696.csv`)에서 `-1`로 표시된 문항들은 점수 계산 시 역채점(Reverse Coding) 처리됩니다. (예: 6점 → 1점).

*   **데이터 예시 (`superKey696.csv` 기반):**
    *   `q_22` ("Act impulsively...") → **HEXACO_C (성실성)** 척도에서 `-1` (역채점) [9].
    *   `q_53` ("Am a physical coward") → **EPQ:P (정신병적 경향)** 척도에서 `-1` (역채점) [10].
    *   `q_146` ("Am indifferent to the feelings of others") → **IPIP100 Agreeableness** 척도에서 `-1` (역채점) [11].
    *   `q_225` ("Am out for my own personal gain") → **BFAS Agreeableness** 및 **HEXACO Honesty-Humility** 척도에서 `-1` (역채점) [12].

## 4. 결측 처리 방법 (Missing Data Handling)
SAPA 기법 특성상 개인 수준에서 약 89%의 데이터가 결측치(planned missingness)입니다 [1]. 이를 해결하기 위해 다음 단계를 거쳤습니다.

1.  **집계 (Aggregation):** 데이터를 개인 수준이 아닌 **카운티 복합체(County-composite)** 수준으로 집계하여 항목 수준 결측치를 12.4%, 척도 수준 결측치를 0.02% 미만으로 감소시킴 [13].
2.  **다중 대체 (Multiple Imputation):**
    *   남은 척도 수준의 결측치는 **MICE (Multiple Imputation by Chained Equations)** 알고리즘을 사용해 처리.
    *   예측 평균 매칭(predictive mean matching) 방식을 사용하여 5번의 대체를 수행하고 그 평균값을 사용 [13].

## 5. County-composite 생성 방법
개인 식별 위험을 방지하고 통계적 안정성을 확보하기 위해 작은 카운티들을 병합했습니다.

*   **기준:** 표본 크기(N)가 10명 미만인 카운티를 병합 대상인 '작은 카운티'로 간주 [14].
*   **병합 알고리즘:**
    1.  가장 작은 카운티를 선택.
    2.  동일한 'American Nation'(문화적 구역) 내에 있으면서 인접한(Queen-contiguity 기준) 카운티 중 가장 작은 곳과 병합.
    3.  병합된 그룹의 N이 10 이상이 될 때까지 반복 [14], [15].
*   **결과:** 총 2,486개 카운티를 1,250개의 카운티 복합체(County-composites)로 재구성 [14].

---

## 6. 데이터 파일 경로

> **중요:** 모든 경로는 `sapa-demo/` 폴더를 기준으로 한 **상대 경로**입니다.  
> 프로젝트 폴더를 어디에 두든 동일하게 작동합니다.

| 파일 | 상대 경로 | 설명 |
|------|----------|------|
| 응답 데이터 | `data/raw/sapa_data.csv` | 23,680명 × 719열 (인구통계 + 696문항) |
| 문항 정보 | `data/raw/item_info.csv` | 문항-척도 텍스트 매핑 |
| 채점 키 | `data/raw/superKey696.csv` | 점수 계산 매트릭스 (1, -1, 0) |
| 처리 결과 | `data/processed/` | 생성된 점수 데이터 저장 위치 |
| 리포트 | `reports/` | QC 리포트, 시각화 저장 위치 |

### 프로젝트 폴더 구조

```
sapa-demo/                    ← 이 폴더를 Cursor로 열기
├── data/
│   ├── raw/
│   │   ├── sapa_data.csv         ← 원본 응답 데이터
│   │   ├── item_info.csv         ← 문항 정보
│   │   └── superKey696.csv       ← 채점 키 (핵심!)
│   └── processed/                ← 점수 계산 결과 저장
├── reports/                      ← 리포트/시각화 저장
├── scripts/                      ← 분석 스크립트 저장
├── preprocessing_guide.md        ← 이 파일
└── README.md
```

---

## 7. 실행 순서 (Step-by-Step)

### Step 1: 데이터 로드

```python
import pandas as pd
import numpy as np

# 프로젝트 루트 기준 상대경로
data = pd.read_csv('data/raw/sapa_data.csv', encoding='utf-8')
keys = pd.read_csv('data/raw/superKey696.csv', index_col=0, encoding='utf-8')
item_info = pd.read_csv('data/raw/item_info.csv', encoding='utf-8')

print(f"응답자 수: {len(data)}")
print(f"변수 수: {len(data.columns)}")
print(f"문항 수: {len(keys)}")
```

### Step 2: Big Five 점수 계산

```python
def calculate_scale_score(df, keys, scale_name):
    """
    채점 키를 사용해 척도 점수 계산
    - 1: 정채점, -1: 역채점 (7 - 원점수), 0: 해당 없음
    """
    # 해당 척도에 속하는 문항 찾기
    scale_items = keys.index[keys[scale_name] != 0].tolist()
    weights = keys.loc[scale_items, scale_name]
    
    # 데이터에 있는 문항만 필터링
    available_items = [q for q in scale_items if q in df.columns]
    
    if not available_items:
        return pd.Series([np.nan] * len(df), index=df.index)
    
    # 역채점 적용 (6점 척도: 7 - 원점수)
    subset = df[available_items].copy()
    for item in available_items:
        if weights[item] == -1:
            subset[item] = 7 - subset[item]
    
    # 평균 계산 (결측 무시)
    return subset.mean(axis=1, skipna=True)

# Big Five 점수 계산
# ⚠️ 컬럼명 규칙: 약어 사용 (NEO_O, NEO_C 등)
scores = pd.DataFrame()
scores['RID'] = data['RID']
scores['NEO_O'] = calculate_scale_score(data, keys, 'NEO_O')
scores['NEO_C'] = calculate_scale_score(data, keys, 'NEO_C')
scores['NEO_E'] = calculate_scale_score(data, keys, 'NEO_E')
scores['NEO_A'] = calculate_scale_score(data, keys, 'NEO_A')
scores['NEO_N'] = calculate_scale_score(data, keys, 'NEO_N')
```

> **⚠️ 컬럼명 주의사항**
> - 저장되는 컬럼명은 채점 키의 척도명과 동일하게 **약어**를 사용합니다.
> - `NEO_O` (Openness), `NEO_C` (Conscientiousness), `NEO_E` (Extraversion), `NEO_A` (Agreeableness), `NEO_N` (Neuroticism)
> - `NEO_Openness`, `NEO_Conscientiousness` 등 전체 이름을 사용하면 **KeyError** 발생!

### Step 3: Ideology & Honesty-Humility 점수 계산

> **⚠️ 중요: z-score 계산 시 주의사항**
> - `scipy.stats.zscore()`는 NaN이 포함되면 전체가 NaN이 됨
> - 구성 요소가 **모두 유효한 경우에만** 계산해야 함
> - numpy array를 DataFrame에 할당할 때 **index를 유지**해야 함

```python
from scipy import stats

# Ideology 구성 요소 계산
scores['MPQ_Traditionalism'] = calculate_scale_score(data, keys, 'MPQtr')
scores['NEO_Liberalism'] = calculate_scale_score(data, keys, 'NEOo6')

# ✅ 올바른 방법: 유효한 값만 추출하여 z-score 계산 후 index 유지
valid_mask = scores['MPQ_Traditionalism'].notna() & scores['NEO_Liberalism'].notna()

if valid_mask.sum() > 0:
    mpqtr_valid = scores.loc[valid_mask, 'MPQ_Traditionalism']
    neo_lib_valid = scores.loc[valid_mask, 'NEO_Liberalism']
    
    # pd.Series로 변환하여 index 유지
    z_mpqtr = pd.Series(stats.zscore(mpqtr_valid.values), index=mpqtr_valid.index)
    z_neo_lib = pd.Series(stats.zscore(neo_lib_valid.values), index=neo_lib_valid.index)
    
    scores['Ideology'] = (z_mpqtr + z_neo_lib * -1) / 2

# Honesty-Humility 구성 요소 계산
scores['NEO_Morality'] = calculate_scale_score(data, keys, 'NEOa2')
scores['NEO_Modesty'] = calculate_scale_score(data, keys, 'NEOa4')
scores['HEXACO_H'] = calculate_scale_score(data, keys, 'HEXACO_H')

# 세 구성 요소가 모두 유효한 경우에만 계산
valid_mask = (scores['NEO_Morality'].notna() & 
              scores['NEO_Modesty'].notna() & 
              scores['HEXACO_H'].notna())

if valid_mask.sum() > 0:
    neo_a2_valid = scores.loc[valid_mask, 'NEO_Morality']
    neo_a4_valid = scores.loc[valid_mask, 'NEO_Modesty']
    hexaco_h_valid = scores.loc[valid_mask, 'HEXACO_H']
    
    z_neo_a2 = pd.Series(stats.zscore(neo_a2_valid.values), index=neo_a2_valid.index)
    z_neo_a4 = pd.Series(stats.zscore(neo_a4_valid.values), index=neo_a4_valid.index)
    z_hexaco_h = pd.Series(stats.zscore(hexaco_h_valid.values), index=hexaco_h_valid.index)
    
    scores['Honesty_Humility'] = (z_neo_a2 + z_neo_a4 + z_hexaco_h) / 3
```

> **❌ 흔한 실수 (NaN 발생 원인)**
> ```python
> # 잘못된 방법: .values 사용 후 바로 할당 → index 불일치로 NaN 발생
> z_mpqtr = stats.zscore(scores['MPQ_Traditionalism'].values)
> scores['Ideology'] = (z_mpqtr + z_neo_lib * -1) / 2  # 모두 NaN!
> ```

### Step 4: 결과 저장

```python
# processed 폴더가 없으면 생성
import os
os.makedirs('data/processed', exist_ok=True)

# 점수 저장
scores.to_csv('data/processed/sapa_scores.csv', index=False, encoding='utf-8')
print(f"저장 완료: data/processed/sapa_scores.csv")
print(f"점수 계산된 응답자 수: {len(scores)}")
```

---

## 8. 주요 척도 컬럼명 (superKey696.csv)

### 채점 키 척도명 → CSV 컬럼명 매핑

| 카테고리 | 채점 키 척도명 | 저장 컬럼명 | 설명 |
|----------|---------------|-------------|------|
| **NEO Big Five** | `NEO_O`, `NEO_C`, `NEO_E`, `NEO_A`, `NEO_N` | `NEO_O`, `NEO_C`, `NEO_E`, `NEO_A`, `NEO_N` | 약어 그대로 사용 |
| **NEO Facets** | `NEOo1`~`NEOo6`, `NEOc1`~`NEOc6`, ... | 동일 | NEO 하위 척도 |
| **HEXACO** | `HEXACO_H`, `HEXACO_E`, `HEXACO_X`, ... | 동일 | HEXACO 도메인 |
| **MPQ** | `MPQtr`, `MPQwb`, ... | `MPQ_Traditionalism` 등 | 읽기 쉬운 이름으로 변환 |
| **복합 척도** | (계산식 참조) | `Ideology`, `Honesty_Humility` | z-score 평균 |

### ⚠️ 흔한 컬럼명 오류

| 잘못된 이름 (❌) | 올바른 이름 (✅) |
|-----------------|-----------------|
| `NEO_Openness` | `NEO_O` |
| `NEO_Conscientiousness` | `NEO_C` |
| `NEO_Extraversion` | `NEO_E` |
| `NEO_Agreeableness` | `NEO_A` |
| `NEO_Neuroticism` | `NEO_N` |

> **규칙:** 시각화/분석 시 `data/processed/sapa_scores.csv`의 **실제 컬럼명**을 사용할 것!

---

## 9. 출력 파일 스키마

### `data/processed/sapa_scores.csv` 컬럼 구조

| 컬럼명 | 타입 | 설명 |
|--------|------|------|
| `RID` | int | 응답자 고유 ID |
| `NEO_O` | float | Openness (개방성) |
| `NEO_C` | float | Conscientiousness (성실성) |
| `NEO_E` | float | Extraversion (외향성) |
| `NEO_A` | float | Agreeableness (우호성) |
| `NEO_N` | float | Neuroticism (신경증) |
| `MPQ_Traditionalism` | float | Ideology 구성요소 |
| `NEO_Liberalism` | float | Ideology 구성요소 |
| `Ideology` | float | 보수 이념 (z-score 평균) |
| `NEO_Morality` | float | H-H 구성요소 |
| `NEO_Modesty` | float | H-H 구성요소 |
| `HEXACO_H` | float | H-H 구성요소 |
| `Honesty_Humility` | float | 정직-겸손 (z-score 평균) |

---

## 10. 체크리스트

실습 완료 시 아래 파일이 생성되면 성공:

- [ ] `data/processed/sapa_scores.csv` — Big Five + Ideology + H-H 점수
- [ ] `reports/figures/correlation_matrix.png` — 상관행렬 시각화
- [ ] `reports/figures/big_five_distributions.png` — Big Five 분포
- [ ] `reports/figures/ideology_hh_distributions.png` — Ideology/H-H 분포
- [ ] `reports/figures/state_critical_ratios_heatmap.png` — State별 CR 히트맵