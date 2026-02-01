# Lanning et al. (2022) 분석 파이프라인 (Analysis Pipeline)

이 문서는 "The Personality of American Nations" 논문의 분석 방법론을 재현하기 위한 단계별 가이드입니다. 데이터 전처리가 완료된 후, 실제 통계 분석이 어떻게 수행되었는지를 다룹니다.

---

## 1. 분석 단위 생성: County-Composites (지역 병합)
개별 카운티(County) 단위는 표본 수가 너무 적어(N < 10인 곳이 64%), 통계적 안정성을 위해 인접한 카운티들을 묶어 **County-Composites**를 생성합니다 [1].

### 알고리즘 로직
1.  **초기 상태:** 전체 2,486개 카운티.
2.  **병합 조건:** 표본 수(N)가 10명 미만인 카운티를 식별.
3.  **병합 규칙 (Iterative Merging):**
    *   가장 작은 카운티를 선택.
    *   동일한 'American Nation' 내에 속하며, 지리적으로 인접한(Queen-contiguity: 모서리나 점을 공유하는) 카운티 중 가장 작은 곳과 병합.
    *   병합된 그룹의 N이 10 이상이 될 때까지 반복.
4.  **결과:** 1,250개의 County-Composites 생성 (전체 표본의 99.9% 보존) [1].

---

## 2. 결측치 처리: MICE Imputation
지역 단위로 묶은 후에도 척도(Scale) 수준에서 발생하는 미세한 결측치를 처리합니다. 논문에서는 `mice` R 패키지를 사용했습니다 [2].

### 처리 단계
1.  **표준화 (Standardization):** 점수들을 먼저 표준화(z-score) 합니다.
2.  **예측 변수 설정:** 인구통계학적 변수와 나머지 성격 척도들을 예측 변수(predictors)로 사용합니다.
3.  **다중 대체 (Multiple Imputation):**
    *   **알고리즘:** MICE (Multivariate Imputation by Chained Equations).
    *   **방법:** PMM (Predictive Mean Matching).
    *   **반복:** 5번의 대체를 수행 (m=5).
4.  **최종 값 산출:** 5번 대체된 데이터셋의 결과값을 단순 평균(simple average)하여 최종 분석 데이터로 사용 [2].

---

## 3. 주요 통계 분석 (Statistical Analyses)

### A. 개인 vs. 지역사회 효과 비교 (Intraclass Correlations)
성격 차이가 "개인 수준"에서 큰지 "지역사회 수준"에서 큰지 비교합니다 [3].

*   **지표:** $r_{icc1}$ (Intraclass Correlation Coefficient 1).
*   **검증 방법 (Monte Carlo Simulation):**
    *   실제 데이터의 ICC를 계산.
    *   데이터를 무작위로 1,000번 섞어(reshuffling) 가상의 "랜덤 국가"를 만든 뒤 ICC 분포를 생성.
    *   실제 ICC가 랜덤 분포의 99% 신뢰구간을 벗어나는지 확인하여 유의성 검증.
*   **결과 해석:** 개인 수준의 차이는 작지만($r < .01$), 지역사회 수준으로 집계하면 효과가 10배 이상 커짐을 확인 [4].

### B. 각 'Nation'별 특징 도출 (Critical Ratios)
어떤 지역이 특정 성격 특성에서 유의미하게 높거나 낮은지 판별합니다 [5].

*   **계산:** 각 Nation별 평균 점수(Mean)와 표준오차(SE) 계산.
*   **공식:** `CR = (Group Mean - Grand Mean) / SE`
*   **기준 (Threshold):** 절대값 Critical Ratio ($|CR|$) > 3.0.
    *   즉, 평균이 표준오차의 3배 이상 떨어져 있을 때 유의미한 특징으로 간주 ($p < .003$).
*   **시각화:** Bubble plot 또는 히트맵을 사용하여 점수 분포 표현.

> **⚠️ 분석 시 컬럼명 주의**
> - Big Five 컬럼: `NEO_O`, `NEO_C`, `NEO_E`, `NEO_A`, `NEO_N` (약어 사용)
> - 복합 척도: `Ideology`, `Honesty_Humility`
> - `NEO_Openness`, `NEO_Conscientiousness` 등 전체 이름 사용 시 **KeyError** 발생!

**코드 예시 (Python):**
```python
# 7개 주요 척도 (실제 컬럼명 사용!)
scales = ['NEO_O', 'NEO_C', 'NEO_E', 'NEO_A', 'NEO_N', 'Ideology', 'Honesty_Humility']
scale_labels = ['O', 'C', 'E', 'A', 'N', 'Ideology', 'H-H']

# Grand Mean 계산
grand_means = df_analysis[scales].mean()

# State별 CR 계산
for state in valid_states:
    state_data = df_analysis[df_analysis['state'] == state]
    for scale, label in zip(scales, scale_labels):
        data = state_data[scale].dropna()
        n = len(data)
        mean = data.mean()
        se = data.std() / np.sqrt(n)
        cr = (mean - grand_means[scale]) / se
        # |CR| > 3.0 → 유의미
```

### C. 다변량 구조 분석 (Canonical Discriminant Analysis)
여러 성격 변수를 동시에 고려하여 지역들을 가장 잘 구분하는 차원을 찾습니다 [6].

*   **분석 도구:** 정준 판별 분석 (Canonical Discriminant Analysis).
    *   R 패키지 `candisc` 활용 가능 [7].
*   **입력 변수:** 7개의 광대역 척도 (Big Five + Honesty-Humility + Ideology).
*   **결과 도출:** 3개의 주요 차원 발견.
    1.  **Authoritarian Conventionalism (권위주의적 관습성):** 보수적 이념, 성실성 관련.
    2.  **Cognitive Resilience (인지적 회복탄력성):** 개방성, 정서적 안정성 관련.
    3.  **Competitiveness (경쟁성):** 우호성(역), 정직-겸손(역) 관련.
*   **해석:** 이 차원들 위에 각 Nation의 위치를 매핑하여 "Red vs Blue"를 넘어선 지역적 뉘앙스(예: Blue 지역 간의 차이)를 설명 [8].

---

## 4. (심화) 경계 최적화: Boundary Adjustment
Woodard의 모델이 실제 데이터와 얼마나 잘 맞는지를 검증하고, 경계를 조정해 봅니다 [9], [10].

*   **지표:** Well-formedness (Category Coherence).
    *   개념: 같은 Nation 내의 지역끼리는 비슷하고(유사성 최대화), 다른 Nation과는 달라야 함(차이 최대화).
*   **최적화 알고리즘:**
    1.  경계선에 있는 County-composite를 선택.
    2.  이 지역을 인접한 다른 Nation으로 "이동(flip)"시켰을 때 전체 Well-formedness 점수가 높아지는지 확인.
    3.  점수가 높아지면 이동시키되, 지리적 연속성(contiguity)이 깨지지 않는지 체크 (섬처럼 고립된 지역 생성 방지).
    4.  더 이상 점수가 오르지 않을 때까지(asymptote) 반복.
*   **결과:** New Netherland 지역이 대폭 축소되는 등 모델이 데이터에 맞게 재조정됨 [11].
요약: 분석을 위한 R 패키지 제안