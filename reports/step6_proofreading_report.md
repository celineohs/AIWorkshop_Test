# 프루프리딩 보고서

## 문서 정보
- **파일:** `reports/step5_draft_method.md`, `reports/step5_draft_results.md`
- **검토일:** 2024-12-19
- **검토 기준:** Nature 리뷰어 관점, APA 7th Edition

---

## 1. Methods 평가 결과

### 1. Reproducibility (재현성)

**구체적 문제점:**
- Python 버전 및 주요 라이브러리 버전 정보가 명시되지 않음
- 랜덤 시드 설정 여부가 불명확 (planned missingness에서 무작위 선택 시)
- 데이터 파일 경로 및 접근 방법이 구체적으로 기술되지 않음
- 코드 공개 여부 또는 재현 가능성에 대한 언급 없음

**리뷰어 예상 질문:**
- "저자들은 독자들이 이 분석을 재현할 수 있도록 어떤 정보를 제공했는가?"
- "랜덤 샘플링 과정에서 재현성을 보장하기 위해 시드를 설정했는가?"
- "분석 코드와 데이터가 공개되어 있는가?"

**개선 방안:**
- Python 버전 및 주요 패키지 버전 명시 (예: "Python 3.9, pandas 1.5.0, scipy 1.9.0")
- 데이터 파일 경로 명시 (예: "Data files are available at [repository URL]")
- 코드 공개 여부 명시 (예: "Analysis code is available at [GitHub repository]")
- Planned missingness에서 무작위 선택 시 시드 설정 여부 명시

---

### 2. Controls (통제)

**구체적 문제점:**
- 대조군 또는 비교 기준이 명확하지 않음 (state-level 분석에서)
- 선택 편향 가능성에 대한 언급 없음 (온라인 샘플의 특성)
- 혼란변수 통제 방법이 기술되지 않음
- 배치 효과나 시간적 변화에 대한 통제 없음

**리뷰어 예상 질문:**
- "온라인 샘플의 대표성 문제를 어떻게 다루었는가?"
- "State-level 분석에서 다른 주와 비교할 때 혼란변수(인구통계학적 특성 등)를 통제했는가?"
- "데이터 수집 기간 동안 시간적 변화나 배치 효과가 있었는가?"

**개선 방안:**
- 온라인 샘플의 특성 및 제한점 명시
- State-level 분석에서 인구통계학적 변수 통제 여부 명시
- Grand mean을 비교 기준으로 사용한 이유 명확화
- 데이터 수집 기간 및 시간적 변화 가능성 언급

---

### 3. Sample size/power (샘플/검정력)

**구체적 문제점:**
- 사전 검정력 분석이 보고되지 않음
- State-level 분석에서 최소 N=100 기준의 근거가 불명확
- 다중 비교 보정에 대한 명시적 언급 없음 (7개 척도 × 9개 주 = 63개 비교)
- 효과 크기(effect size) 보고 없음

**리뷰어 예상 질문:**
- "최소 N=100 기준을 선택한 통계적 근거는 무엇인가?"
- "7개 척도 × 9개 주 = 63개 비교에 대해 다중 비교 보정을 적용했는가?"
- "검정력 분석을 통해 적절한 표본 크기를 결정했는가?"

**개선 방안:**
- 최소 N=100 기준 선택 근거 명시 (예: "to ensure stable estimates with SE < 0.1")
- 다중 비교 보정 방법 명시 (예: "Bonferroni correction" 또는 "CR > 3.0 provides conservative control")
- 효과 크기 보고 추가 (예: Cohen's d 또는 다른 적절한 지표)
- 검정력 분석 결과 또는 선행 연구 기반 근거 제시

---

### 4. Statistical appropriateness (통계 적절성)

**구체적 문제점:**
- CR > 3.0 기준의 통계적 근거가 약함 (p < .003 언급만 있음)
- 정규성 가정 검증 여부 불명확
- 상관분석에서 pairwise deletion 사용 시 편향 가능성 언급 없음
- z-score 계산 시 결측치 처리 방법이 불명확

**리뷰어 예상 질문:**
- "CR > 3.0 기준이 다중 비교를 적절히 통제하는가?"
- "상관분석에서 pairwise deletion이 결과에 미치는 영향을 평가했는가?"
- "z-score 계산 시 결측치가 포함된 경우를 어떻게 처리했는가?"

**개선 방안:**
- CR > 3.0 기준의 통계적 근거 강화 (예: "corresponds to p < .003 under normal approximation, providing conservative control for 63 comparisons")
- 상관분석에서 pairwise N 보고 및 편향 가능성 논의
- 결측치 처리 방법 명확화 (예: "only participants with complete data on all components")
- 정규성 가정 검증 또는 비모수적 대안 고려 여부 명시

---

### 5. Validation (타당성)

**구체적 문제점:**
- 척도의 내적 일관성(Cronbach's α) 보고 없음
- 구성 타당도 검증 없음
- 외부 검증 또는 교차 검증 없음
- State-level 분석의 일반화 가능성에 대한 논의 부족

**리뷰어 예상 질문:**
- "각 척도의 신뢰도는 얼마인가?"
- "State-level 패턴이 다른 시점이나 다른 샘플에서도 재현되는가?"
- "이 결과를 다른 국가나 지역에 일반화할 수 있는가?"

**개선 방안:**
- 각 척도의 내적 일관성 계수 보고 (Cronbach's α)
- 구성 타당도 검증 결과 제시 (예: 상관행렬, 요인 분석)
- State-level 결과의 일반화 가능성 및 제한점 명시
- 외부 검증 가능성 또는 향후 연구 방향 제시

---

## 2. Results 평가 결과

### 문장별 분석

| # | 원문 | Claim Type | Evidence Level | Risk (1-10) | Conservative Alternative |
|---|------|------------|----------------|-------------|--------------------------|
| 1 | "suggesting substantial conceptual overlap between these constructs" | General | Indirect | 4 | "suggesting substantial conceptual overlap between these constructs" (적절) |
| 2 | "indicating that individuals higher in openness tend to hold more progressive (less conservative) ideological views" | Correlational | Direct | 3 | "indicating that openness is associated with more progressive ideological views" (약간 완화) |
| 3 | "These patterns align with theoretical expectations" | General | Indirect | 2 | "These patterns are consistent with theoretical expectations" (약간 완화) |
| 4 | "suggesting greater emotional stability" | Correlational | Indirect | 5 | "suggesting lower neuroticism scores, which may reflect greater emotional stability" (더 명확) |
| 5 | "indicating lower scores on these conservative-leaning measures" | General | Direct | 2 | "indicating lower scores on these measures" (적절) |
| 6 | "These findings suggest meaningful regional variation in personality traits that may reflect cultural, economic, or historical factors" | Correlational | Suggestive | 7 | "These findings suggest regional variation in personality traits that could potentially reflect cultural, economic, or historical factors" (더 보수적) |

### 가장 위험한 Overclaim Top 3

#### 1. "These findings suggest meaningful regional variation in personality traits that may reflect cultural, economic, or historical factors unique to each state." (Line 36)

**문제점:**
- "meaningful"라는 표현이 과도하게 강함 (통계적 유의성과 실질적 의미를 혼동)
- "may reflect"는 적절하지만, "unique to each state"는 과도한 주장 (다른 요인 가능성 배제)
- 인과적 해석의 위험 (상관 데이터로부터 인과 추론 시도)

**수정 방법:**
- "meaningful" 제거 또는 "statistically significant"로 대체
- "unique to each state" 제거 또는 "potentially related to"로 완화
- 제한점 명시 강화

**수정안:**
"These findings indicate statistically significant regional variation in personality traits that could potentially be related to cultural, economic, or historical factors. However, alternative explanations, such as selective migration or sampling biases, cannot be ruled out."

---

#### 2. "suggesting greater emotional stability" (Line 34)

**문제점:**
- Neuroticism 점수가 낮다는 것과 "emotional stability"는 다른 개념 (역방향 해석이지만 과도한 추론)
- 간접적 추론을 직접적 결론처럼 서술

**수정 방법:**
- "greater emotional stability"를 "lower neuroticism scores"로 먼저 명시
- 추론적 해석을 더 보수적으로 표현

**수정안:**
"Florida showed significantly lower Neuroticism (CR = -3.22), which corresponds to lower neuroticism scores that may reflect greater emotional stability."

---

#### 3. "suggesting substantial conceptual overlap between these constructs" (Line 26)

**문제점:**
- "substantial"이 다소 강한 표현 (r = .79는 높지만 "substantial"은 주관적)
- 상관계수만으로 "conceptual overlap"을 주장하는 것은 약간 과도

**수정 방법:**
- "substantial"을 더 객관적인 표현으로 대체
- 상관계수 값에 기반한 해석으로 완화

**수정안:**
"suggesting a strong positive association (r = .79) that may reflect conceptual overlap between these constructs."

---

## 3. 종합 권고

### 우선순위 높음 (Must Fix)

1. **다중 비교 보정 명시**
   - 7개 척도 × 9개 주 = 63개 비교에 대한 명시적 보정 방법 기술
   - CR > 3.0 기준의 통계적 근거 강화

2. **재현성 정보 추가**
   - Python/패키지 버전 명시
   - 코드/데이터 공개 여부 명시
   - 랜덤 시드 설정 여부

3. **Results의 "meaningful" 표현 수정**
   - "statistically significant"로 대체
   - 제한점 강화

---

### 우선순위 중간 (Should Fix)

1. **척도 신뢰도 보고**
   - Cronbach's α 또는 다른 적절한 신뢰도 지표 추가

2. **효과 크기 보고**
   - State-level 차이의 실질적 의미 평가를 위한 효과 크기 추가

3. **혼란변수 통제 논의**
   - State-level 분석에서 인구통계학적 변수 통제 여부 명시

---

### 우선순위 낮음 (Nice to Have)

1. **검정력 분석 추가**
   - 사전 검정력 분석 결과 또는 선행 연구 기반 근거

2. **외부 검증 논의**
   - 결과의 일반화 가능성 및 제한점 강화

3. **정규성 가정 검증**
   - 가정 검증 결과 또는 비모수적 대안 고려 여부

---

## 4. 수정 전후 비교

| 위치 | 원문 | 수정안 | 수정 이유 |
|------|------|--------|-----------|
| Results, L.36 | "meaningful regional variation" | "statistically significant regional variation" | "meaningful"는 주관적, 통계적 유의성과 구분 |
| Results, L.36 | "unique to each state" | "potentially related to" | 과도한 주장 완화, 대안 설명 가능성 인정 |
| Results, L.34 | "suggesting greater emotional stability" | "which corresponds to lower neuroticism scores that may reflect greater emotional stability" | 간접적 추론을 더 명확하게 표현 |
| Results, L.26 | "substantial conceptual overlap" | "a strong positive association (r = .79) that may reflect conceptual overlap" | 객관적 수치 기반 표현으로 완화 |
| Methods, Data Analysis | CR 기준 설명 | 다중 비교 보정 명시 추가 | 63개 비교에 대한 통계적 통제 명확화 |
| Methods, Data Analysis | Python 사용 언급 | 버전 및 패키지 정보 추가 | 재현성 향상 |

---

## 5. 추가 권고사항

### Methods 섹션
- 데이터 수집 기간 명시 (가능하면)
- 온라인 샘플의 특성 및 제한점 명시
- 최소 N=100 기준 선택 근거 명확화

### Results 섹션
- Table 1에 신뢰도 계수 추가 고려
- 상관분석에서 pairwise N 보고 고려
- State-level 차이의 효과 크기 보고 고려

### 전체
- 일관된 용어 사용 확인 (예: "Honesty-Humility" vs "H-H")
- Figure 참조 일관성 확인 (Figure 1, Figure 2 등)
