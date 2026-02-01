# Method/Results 초안 작성 가이드

이 문서는 SAPA 프로젝트의 분석 결과를 바탕으로 학술 논문의 Method 및 Results 섹션 초안을 작성하기 위한 가이드입니다.

**생성 파일:**
- `reports/step5_draft_method.md`
- `reports/step5_draft_results.md`

---

## 참고 자료

### 스타일 가이드
| 문서 | 경로 | 용도 |
|------|------|------|
| APA 7th Edition | `guides/APA7-Style.pdf` | 인용, 참고문헌, 형식 |
| The Elements of Style | `guides/The Elements of Style.pdf` | 간결하고 명확한 문장 |
| Writing Science | `guides/Writing Science.pdf` | 과학 글쓰기 원칙 |

### 데이터 소스 (JSON)
| 파일 | 생성 노트북 | 주요 내용 |
|------|------------|----------|
| `reports/step1_scan.json` | `01_data_scan.ipynb` | 원본 데이터 구조 |
| `reports/step2_preprocess.json` | `02_preprocessing.ipynb` | QC 및 척도 통계 |
| `reports/step3_viz.json` | `03_visualization.ipynb` | 상관행렬 |
| `reports/step4_state.json` | `04_state_analysis.ipynb` | 주별 CR 분석 |

---

## Few-Shot 예시: 좋은 Method 작성

### ✅ 좋은 Participants 예시

> We recruited participants through the SAPA (Synthetic Aperture Personality Assessment) online platform (Condon & Revelle, 2014). A total of 23,679 individuals participated in the study. After quality control procedures, data from 23,647 participants were included in the final analyses. We excluded 32 participants based on the following criteria: (a) insufficient responses (fewer than 10 items answered), and (b) straight-lining patterns (identical responses across consecutive items), which indicate low-quality or non-engaged responding.
>
> For state-level analyses, we included 9 states with sample sizes of at least 100 participants each (to ensure stable estimates with SE < 0.1), resulting in a final sample of 7,308 respondents.

**왜 좋은가:**
- 구체적인 숫자 (23,679 → 23,647, 32명 제외)
- 제외 기준의 근거 설명 (low-quality responding)
- 최소 N 기준의 통계적 근거 (SE < 0.1)

### ❌ 나쁜 Participants 예시

> Participants were recruited online. Some participants were excluded due to poor data quality. We analyzed data from several states.

**왜 나쁜가:**
- 구체적인 숫자 없음
- 제외 기준 불명확
- "several states"는 모호함

---

### ✅ 좋은 Data Analysis 예시

> All analyses were conducted using Python 3.9 with pandas 1.5.0, numpy 1.23.0, scipy 1.9.0. Analysis code is available at [repository URL].
>
> For state-level analyses, we calculated Critical Ratios (CR):
>
>     CR = (State Mean - Grand Mean) / SE
>
> Given the 63 comparisons (7 scales × 9 states), we used |CR| > 3.0 as a conservative threshold, corresponding to p < .003 under normal approximation.

**왜 좋은가:**
- 소프트웨어 버전 명시 (재현성)
- 코드 공개 여부 명시
- 공식 제시
- 다중 비교 보정 근거 설명

---

## Few-Shot 예시: 좋은 Results 작성

### ✅ 좋은 상관관계 보고 예시

> Figure 1 presents the correlation matrix among the seven personality scales. The strongest positive correlation was observed between Agreeableness and Honesty-Humility (r = .79, p < .001), suggesting a strong positive association that may reflect conceptual overlap between these constructs. The strongest negative correlation was between Openness and Ideology (r = -.57, p < .001), indicating that openness is associated with more progressive ideological views.

**왜 좋은가:**
- Figure 참조로 시작
- 구체적인 r 값과 p 값
- "suggesting", "may reflect" 등 보수적 표현

### ❌ 나쁜 상관관계 보고 예시

> Agreeableness and Honesty-Humility were highly correlated, which proves that these constructs are the same thing. Openness causes people to be more liberal.

**왜 나쁜가:**
- 구체적인 통계값 없음
- "proves"는 과도한 주장
- "causes"는 인과관계 주장 (상관 데이터에서 부적절)

---

### ✅ 좋은 State-Level 보고 예시

> We identified 8 statistically significant state-level features (|CR| > 3.0, p < .003) across 9 states and 7 personality scales (see Figure 2). Michigan showed significantly higher scores on Honesty-Humility (CR = 4.31) and Agreeableness (CR = 3.34).
>
> These findings indicate statistically significant regional variation that could potentially be related to cultural factors. However, alternative explanations, such as selective migration or sampling biases, cannot be ruled out.

**왜 좋은가:**
- "statistically significant" 사용 (not "meaningful")
- CR 값 구체적으로 제시
- 제한점 및 대안 설명 언급

---

## 문장 수준 작성 규칙

### 1. 첫 문장 = Topic Sentence

| 섹션 | 첫 문장 예시 |
|------|-------------|
| Participants | "We recruited participants through the SAPA online platform." |
| Measures | "Personality traits were assessed using items from the IPIP." |
| Procedure | "The SAPA project employed a planned missingness design." |
| Data Analysis | "All analyses were conducted using Python." |
| Descriptive Statistics | "Table 1 presents descriptive statistics for the seven major scales." |
| Correlations | "Figure 1 presents the correlation matrix among the scales." |
| State-Level | "We identified 8 statistically significant state-level features." |

### 2. 통계값 보고 형식

| 유형 | 형식 | 예시 |
|------|------|------|
| 상관 | r = .XX, p < .XXX | r = .79, p < .001 |
| 평균/SD | M = X.XX, SD = X.XX | M = 4.31, SD = 0.83 |
| CR | CR = X.XX | CR = 4.31 |
| 표본 | N = X,XXX 또는 n = XXX | N = 23,647 또는 n = 860 |

**참고:** r 값은 소수점 앞 0 생략 (.79, not 0.79)

---

## Overclaiming 방지 표현

| ❌ 피해야 할 표현 | ✅ 대안 표현 |
|-----------------|-------------|
| proves | suggests, indicates |
| demonstrates | is consistent with |
| causes | is associated with |
| determines | is related to |
| meaningful | statistically significant |
| clearly shows | appears to show |
| confirms | provides evidence for |
| unique to | potentially related to |

---

## Method 섹션: 추출할 정보

### Participants
| 내용 | JSON 경로 |
|------|-----------|
| 원본 응답자 수 | `step1_scan.json → data_overview.n_respondents` |
| QC 후 최종 N | `step2_preprocess.json → qc_results.final_n` |
| 제외된 N | `step2_preprocess.json → qc_results.excluded_n` |
| 제외 사유 | `step2_preprocess.json → qc_results.exclusion_reasons` |
| 주별 분석 N | `step4_state.json → analysis_summary.n_respondents` |
| 분석 주 수 | `step4_state.json → analysis_summary.n_states` |

### Measures
| 내용 | JSON 경로 |
|------|-----------|
| 총 문항 수 | `step1_scan.json → data_overview.n_items` |
| 총 척도 수 | `step1_scan.json → data_overview.n_scales` |
| Big Five 척도 | `step1_scan.json → scoring_key.main_scales.NEO_Big_Five` |

### Procedure
| 내용 | JSON 경로 |
|------|-----------|
| 문항 결측률 | `step1_scan.json → planned_missingness.item_missing_rate_pct` |
| 평균 응답 수 | `step1_scan.json → planned_missingness.avg_responses_per_person` |

---

## Results 섹션: 추출할 정보

### Descriptive Statistics
| 내용 | JSON 경로 |
|------|-----------|
| 총 응답자 수 | `step2_preprocess.json → total_respondents` |
| 척도별 N | `step2_preprocess.json → scales.{척도명}.N` |
| 척도별 Mean | `step2_preprocess.json → scales.{척도명}.Mean` |
| 척도별 SD | `step2_preprocess.json → scales.{척도명}.SD` |

### Correlations
| 내용 | JSON 경로 |
|------|-----------|
| 상관행렬 | `step3_viz.json → correlation_matrix` |
| 주요 상관 | `step3_viz.json → major_correlations` |

### State-Level
| 내용 | JSON 경로 |
|------|-----------|
| 유의미한 특징 수 | `step4_state.json → n_significant_features` |
| 유의미한 특징 목록 | `step4_state.json → significant_features` |

---

## 체크리스트

### Method 섹션
- [ ] 원본 N과 최종 N 모두 명시
- [ ] 제외 기준 (a), (b) 형식으로 구체화
- [ ] 제외 기준의 근거 설명
- [ ] 최소 N=100 기준 근거 (SE < 0.1)
- [ ] 복합 척도 계산 공식 명시
- [ ] planned missingness 설계 및 인용
- [ ] 소프트웨어 버전 명시
- [ ] 다중 비교 보정 설명 (63개 비교)
- [ ] 온라인 샘플 제한점 언급

### Results 섹션
- [ ] Table/Figure 참조로 시작
- [ ] 주요 상관 (r, p값) 보고
- [ ] 유의미한 CR 특징 보고
- [ ] 모든 통계값 APA 형식
- [ ] 제한점 및 대안 설명 언급

### 글쓰기 품질
- [ ] 과거 시제 일관성
- [ ] 능동태 우선 사용
- [ ] overclaiming 표현 없음
- [ ] 각 단락 첫 문장 = topic sentence
- [ ] 인과 표현 회피 (상관 연구)
