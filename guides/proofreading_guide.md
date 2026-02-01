# Proofreading Guide

학술 문서를 체계적으로 검토하고 개선하기 위한 프루프리딩 가이드입니다.

**출력 파일:** `reports/step6_proofreading_report.md`

---

## 1. GitHub 파일 참조하기

### 파일 참조 방법

```
https://github.com/{owner}/{repo}/blob/{branch}/{path/to/file}
```

### 참조 시 확인 사항

- [ ] 파일 경로가 정확한지 확인
- [ ] 특정 라인 참조: `#L{시작}-L{끝}`
- [ ] 특정 커밋 참조: 커밋 해시 사용

---

## 2. Methods 평가 기준

### 2.1 평가 항목 상세

| 평가 항목 | 주요 검토 사항 | 일반적인 문제점 |
|-----------|----------------|-----------------|
| **Reproducibility** | 코드/데이터 공개, 파라미터, 환경 설정 | 버전 누락, 전처리 생략, 랜덤 시드 미기재 |
| **Controls** | 대조군, 혼란변수, 실험 조건 | 대조군 부재, 선택 편향, 배치 효과 |
| **Sample size/power** | 사전 검정력, 표본 크기, 효과 크기 | 검정력 분석 부재, 불충분한 표본 |
| **Statistical appropriateness** | 가정 검증, 검정 선택, 다중 비교 | 가정 위반, 부적절한 검정, 보정 미적용 |
| **Validation** | 내부/외부/교차 검증 | 과적합, 일반화 한계 |

### 2.2 Few-Shot 예시: Methods 평가

#### ✅ 좋은 평가 예시

**원문:**
> "We analyzed data from participants recruited through an online platform."

**평가:**

| 항목 | 문제점 | 리뷰어 질문 | 개선 방안 |
|------|--------|-------------|-----------|
| Reproducibility | 플랫폼 이름, 데이터 수집 기간, 소프트웨어 버전 누락 | "어떤 플랫폼인가? 언제 수집했는가? 어떤 버전의 소프트웨어를 사용했는가?" | 플랫폼 이름 및 인용 추가, 기간 명시, 소프트웨어 버전 기재 |
| Controls | 온라인 샘플의 대표성 및 품질 검증 미언급 | "이 표본이 일반 인구를 대표하는지 어떻게 확인했는가?" | 인구통계적 비교, QC 기준 추가 |
| Sample size | 검정력 분석 부재, 최소 N 기준 근거 없음 | "이 표본 크기로 검출하려는 효과 크기는 무엇인가?" | 사전 또는 사후 검정력 분석 추가 |

**수정안:**
> "We analyzed data from 23,647 participants recruited through the SAPA online platform (Condon & Revelle, 2014) between January and December 2023. All analyses were conducted using Python 3.9 with pandas 1.5.0 and scipy 1.9.0. Analysis code is available at [repository URL]."

---

#### ❌ 나쁜 평가 예시

**원문:**
> "We analyzed data from participants recruited through an online platform."

**평가:**
> "Methods가 약간 부족해 보입니다. 더 자세히 쓰면 좋겠습니다."

**왜 나쁜가:**
- 구체적인 문제점 지적 없음
- 어떤 항목이 부족한지 불명확
- 개선 방안 제시 없음

---

### 2.3 항목별 체크리스트

#### Reproducibility 체크리스트
- [ ] 소프트웨어 이름 및 버전 (Python 3.9, pandas 1.5.0 등)
- [ ] 랜덤 시드 (random_state=42 등)
- [ ] 코드/데이터 공개 여부 및 URL
- [ ] 전처리 단계 상세 설명
- [ ] 파라미터 값 명시

#### Controls 체크리스트
- [ ] 온라인 샘플의 제한점 인정
- [ ] 인구통계적 대표성 논의
- [ ] 혼란변수 통제 방법 또는 미통제 명시
- [ ] 자기선택 편향 가능성 언급

#### Sample size/power 체크리스트
- [ ] 사전 또는 사후 검정력 분석
- [ ] 최소 N 기준 및 통계적 근거
- [ ] 효과 크기 보고 (Cohen's d, r 등)
- [ ] 다중 비교 시 보정 설명

#### Statistical appropriateness 체크리스트
- [ ] 정규성 가정 검토
- [ ] 검정 방법 선택 근거
- [ ] 다중 비교 보정 (Bonferroni, FDR 등)
- [ ] 유의성 기준 명시 (α = .05 또는 보정된 값)

#### Validation 체크리스트
- [ ] 신뢰도 보고 (Cronbach's α 등)
- [ ] 타당도 논의
- [ ] 교차검증 또는 독립 표본 검증 (해당시)

---

## 3. Results 평가 기준

### 3.1 Claim Type 분류

| Claim Type | 정의 | 허용 표현 | 금지 표현 |
|------------|------|-----------|-----------|
| **Causal** | 인과관계 | (실험 연구에서만) "A caused B" | (상관 연구에서) "A causes B" |
| **Correlational** | 상관관계 | "A is associated with B" | "A leads to B" |
| **Mechanistic** | 기전 설명 | "A may act through B" | "A acts through B" |
| **General** | 일반 서술 | "A was observed" | - |

### 3.2 Evidence Level

| Level | 정의 | 예시 |
|-------|------|------|
| **Direct** | 해당 변수를 직접 측정/조작 | 실험적 조작, 직접 측정 |
| **Indirect** | 관련 변수를 통한 추론 | 대리 변수, 파생 지표 |
| **Suggestive** | 탐색적/시사적 | 패턴 관찰, 예비 분석 |

### 3.3 Overclaiming Risk 점수

| 점수 | 위험도 | 기준 |
|------|--------|------|
| 1-3 | 낮음 | 데이터가 완전히 뒷받침, 보수적 표현 |
| 4-6 | 중간 | 해석에 약간의 비약, 수정 권장 |
| 7-10 | 높음 | 데이터 대비 과도한 주장, 수정 필수 |

---

### 3.4 Few-Shot 예시: Results 평가

#### 예시 1: 상관관계 보고

**원문:**
> "Agreeableness and Honesty-Humility showed a strong correlation (r = .79), demonstrating substantial conceptual overlap between these constructs."

**평가:**

| 항목 | 값 |
|------|-----|
| Claim Type | Correlational → Mechanistic (문제) |
| Evidence Level | Direct |
| Overclaiming Risk | 7/10 |

**문제점:**
- "demonstrating"은 증명을 의미, 상관 데이터로는 부적절
- "substantial conceptual overlap"은 이론적 주장, 상관만으로 입증 불가

**수정안:**
> "Agreeableness and Honesty-Humility showed a strong positive correlation (r = .79, p < .001), which is consistent with theoretical predictions of conceptual overlap between these constructs (Ashton et al., 2014)."

---

#### 예시 2: 지역 차이 보고

**원문:**
> "Michigan showed higher Honesty-Humility (CR = 4.31), suggesting that Midwestern residents are more honest."

**평가:**

| 항목 | 값 |
|------|-----|
| Claim Type | General → Causal (문제) |
| Evidence Level | Direct (CR) → Indirect (기질 해석) |
| Overclaiming Risk | 9/10 |

**문제점:**
- "more honest"는 실제 행동에 대한 주장, 자기보고 점수만으로 부적절
- 대안 설명 (선택적 이주, 표집 편향) 미고려

**수정안:**
> "Michigan showed significantly higher self-reported Honesty-Humility scores (CR = 4.31, p < .003). This statistically significant regional difference could reflect cultural factors, though alternative explanations such as selective migration or sampling biases cannot be ruled out."

---

#### 예시 3: 상관 → 인과 비약

**원문:**
> "Openness to Experience causes individuals to adopt more liberal political views."

**평가:**

| 항목 | 값 |
|------|-----|
| Claim Type | Causal (부적절) |
| Evidence Level | Indirect |
| Overclaiming Risk | 10/10 |

**문제점:**
- 횡단면 상관 데이터로 인과관계 주장 불가
- 역인과 가능성 미고려

**수정안:**
> "Openness to Experience was negatively correlated with Ideology (r = -.57, p < .001), indicating that individuals higher in openness reported more progressive political views. This cross-sectional association does not permit causal inference."

---

### 3.5 자주 발생하는 Overclaim 패턴

| 패턴 | 원문 예시 | 문제점 | 수정안 |
|------|----------|--------|--------|
| **상관→인과** | "A causes B" | 실험 없이 인과 주장 | "A is associated with B" |
| **meaningful** | "meaningful difference" | 통계적 유의성 ≠ 실질적 의미 | "statistically significant difference" |
| **증명** | "proves", "demonstrates" | 과학에서 절대적 증명 불가 | "suggests", "indicates" |
| **일반화** | "people are..." | 특정 표본에서 일반화 | "participants in this sample showed..." |
| **기전 추론** | "A acts through B" | 매개 분석 없이 기전 주장 | "A may be related to B through C" |

---

## 4. 표현 대체어 사전

### 4.1 인과 → 상관

| 원문 (Causal) | 수정안 (Correlational) |
|---------------|------------------------|
| A causes B | A is associated with B |
| A leads to B | A tends to coincide with B |
| A results in B | A is correlated with B |
| A determines B | A is linked to B |
| A produces B | A accompanies B |

### 4.2 강한 주장 → 완화

| 원문 (Strong) | 수정안 (Hedged) |
|---------------|-----------------|
| demonstrates | suggests |
| proves | indicates |
| clearly shows | appears to show |
| confirms | is consistent with |
| establishes | provides evidence for |
| meaningful | statistically significant |
| unique | potentially related |

### 4.3 일반화 → 제한

| 원문 (General) | 수정안 (Limited) |
|----------------|-----------------|
| People are... | Participants in this sample... |
| Americans tend to... | U.S. participants in this study... |
| Personality affects... | Self-reported personality scores were associated with... |

---

## 5. 출력 템플릿

### Methods 평가 출력

```markdown
## Methods 평가 결과

### 1. Reproducibility (재현성)
**구체적 문제점:**
- [구체적으로 누락된 정보 나열]

**리뷰어 예상 질문:**
- "저자들은 어떻게 [X]를 보장할 수 있는가?"

**개선 방안:**
- [구체적 추가 내용]

### 2. Controls (통제)
[동일 형식]

### 3. Sample size/power (샘플/검정력)
[동일 형식]

### 4. Statistical appropriateness (통계 적절성)
[동일 형식]

### 5. Validation (타당성)
[동일 형식]
```

### Results 평가 출력

```markdown
## Results 평가 결과

### 문장별 분석

| # | 원문 | Claim Type | Evidence | Risk | Conservative Alternative |
|---|------|------------|----------|------|--------------------------|
| 1 | "[원문]" | Correlational | Direct | 3 | "[수정안]" |
| 2 | "[원문]" | Causal (문제) | Indirect | 8 | "[수정안]" |

### 가장 위험한 Overclaim Top 3

#### 1. [문장]
- **위험도:** X/10
- **문제점:** [왜 위험한지]
- **수정안:** "[구체적 수정문]"
```

### 최종 보고서 템플릿

```markdown
# 프루프리딩 보고서

## 문서 정보
- **검토 대상:** [파일명]
- **검토일:** [날짜]

## 1. Methods 평가 요약

### 주요 약점 (심각도순)
1. [약점 1] - 심각도: 높음/중간/낮음
2. [약점 2]
3. [약점 3]

## 2. Results 평가 요약

### Overclaiming 현황
- 고위험 (Risk ≥ 7): N개
- 중위험 (Risk 4-6): N개
- 저위험 (Risk 1-3): N개

### Top 3 Overclaim
1. [문장 및 수정안]
2. [문장 및 수정안]
3. [문장 및 수정안]

## 3. 종합 권고

### Must Fix (반드시 수정)
- [ ] [수정 사항]

### Should Fix (권장 수정)
- [ ] [수정 사항]

### Nice to Have (선택적 개선)
- [ ] [수정 사항]

## 4. 수정 전후 비교

| 위치 | 원문 | 수정안 | 이유 |
|------|------|--------|------|
| Methods L.XX | "[원문]" | "[수정]" | [이유] |
| Results L.XX | "[원문]" | "[수정]" | [이유] |
```

---

## 참고 자료

### 프로젝트 내 참고 문서
- [The Elements of Style](guides/The%20Elements%20of%20Style.pdf) - 간결한 영문 작성
- [Writing Science](guides/Writing%20Science.pdf) - 과학 글쓰기 원칙
- [APA 7th Style](guides/APA7-Style.pdf) - 학술 형식 가이드

### 외부 참고 자료
- Nature Author Guidelines: https://www.nature.com/nature/for-authors
- ICMJE Recommendations: http://www.icmje.org/recommendations/
- CONSORT Statement: http://www.consort-statement.org/
