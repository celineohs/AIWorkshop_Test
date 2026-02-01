# Revision 가이드

프루프리딩 보고서를 바탕으로 Method/Results 초안을 수정하는 가이드입니다.

**생성 파일:**
- `reports/step7_revised_method.md`
- `reports/step7_revised_results.md`

---

## 입력 파일

| 파일 | 역할 |
|------|------|
| `reports/step5_draft_method.md` | 원본 Method 초안 |
| `reports/step5_draft_results.md` | 원본 Results 초안 |
| `reports/step6_proofreading_report.md` | 프루프리딩 평가 및 수정 사항 |

---

## 수정 전략

### 1단계: 프루프리딩 보고서 분석

1. **Must Fix** 항목 추출
2. **Should Fix** 항목 추출
3. **Top 3 Overclaim** 확인
4. 수정 전후 비교 테이블 참조

### 2단계: 우선순위별 수정

1. Must Fix 항목 먼저 적용
2. Should Fix 항목 순차 적용
3. Nice to Have는 전체 흐름에 맞으면 적용

### 3단계: 일관성 검토

1. 용어 일관성 확인
2. 문체 일관성 확인
3. APA 형식 준수 확인

---

## 수정 우선순위

### Must Fix (필수)

| 항목 | 섹션 | 수정 내용 |
|------|------|----------|
| 다중 비교 보정 | Methods | 63개 비교 (7×9)에 대한 통계적 통제 설명 |
| 재현성 정보 | Methods | Python/패키지 버전, 코드/데이터 공개 |
| Overclaiming | Results | "meaningful" → "statistically significant" |
| 인과 표현 | Results | "causes", "leads to" 등 완화 |

### Should Fix (권장)

| 항목 | 섹션 | 수정 내용 |
|------|------|----------|
| 신뢰도 보고 | Methods | Cronbach's α (가능하면) |
| 효과 크기 | Results | Cohen's d, r² 등 |
| 혼란변수 | Methods | 통제하지 못한 변수 논의 |
| 제한점 | Results | 횡단면 데이터, 표집 편향 |

### Nice to Have (선택)

| 항목 | 섹션 | 수정 내용 |
|------|------|----------|
| 검정력 분석 | Methods | 사후 검정력 계산 |
| 정규성 검증 | Methods | 가정 검토 결과 |
| 외부 검증 | Results | 선행 연구와 비교 |

---

## Few-Shot 예시: Methods 수정

### 예시 1: 재현성 정보 추가

**원문:**
> All analyses were conducted using Python.

**수정안:**
> All analyses were conducted using Python 3.9 with pandas 1.5.0, numpy 1.23.0, scipy 1.9.0, and matplotlib 3.6.0. Analysis code and processed data are available at [repository URL].

**수정 이유:**
- 버전 명시로 재현성 확보
- 코드/데이터 공개 정책 명시

---

### 예시 2: 다중 비교 보정 추가

**원문:**
> Critical Ratios (CR) above 3.0 were considered statistically significant.

**수정안:**
> Critical Ratios (CR) were computed as (State Mean - Grand Mean) / SE. Given the 63 comparisons (7 scales × 9 states), we used |CR| > 3.0 as a conservative threshold, corresponding to p < .003 under normal approximation. This threshold provides conservative control for multiple comparisons, equivalent to a Bonferroni-corrected significance level of approximately p < .05/63 ≈ .0008.

**수정 이유:**
- 공식 명시
- 63개 비교 근거 설명
- Bonferroni 보정 언급

---

### 예시 3: 표본 크기 기준 명확화

**원문:**
> We included states with at least 100 participants.

**수정안:**
> For state-level analyses, we included only states with sample sizes of at least 100 participants. This threshold ensures stable estimates with standard errors below 0.1 for personality scale scores, assuming population SDs of approximately 1.0.

**수정 이유:**
- 100명 기준의 통계적 근거 (SE < 0.1)
- 가정 명시

---

### 예시 4: 온라인 샘플 제한점 추가

**원문:**
> Participants were recruited through the SAPA online platform.

**수정안:**
> Participants were recruited through the SAPA (Synthetic Aperture Personality Assessment) online platform (Condon & Revelle, 2014). As with all internet-based convenience samples, the data may not be fully representative of the general U.S. population, and self-selection biases cannot be ruled out.

**수정 이유:**
- 출처 인용 추가
- 온라인 표본의 일반화 한계 인정

---

## Few-Shot 예시: Results 수정

### 예시 1: "meaningful" 수정

**원문:**
> These findings indicate meaningful regional variation in personality traits.

**수정안:**
> These findings indicate statistically significant regional variation in personality traits (|CR| > 3.0, p < .003).

**수정 이유:**
- "meaningful"은 실질적 의미를 함축 (주관적)
- "statistically significant"는 객관적 기준

---

### 예시 2: 인과 표현 완화

**원문:**
> Florida showed significantly lower Neuroticism, suggesting greater emotional stability among Florida residents.

**수정안:**
> Florida showed significantly lower self-reported Neuroticism scores (CR = -3.22, p < .003), which may reflect greater emotional stability among respondents from this state.

**수정 이유:**
- "self-reported" 추가로 측정 방법 명시
- "residents" → "respondents" 로 일반화 범위 제한
- "suggesting" → "may reflect" 로 확신도 낮춤

---

### 예시 3: 상관 해석 완화

**원문:**
> The strong correlation between Agreeableness and Honesty-Humility demonstrates substantial conceptual overlap.

**수정안:**
> Agreeableness showed a strong positive correlation with Honesty-Humility (r = .79, p < .001), consistent with theoretical predictions of conceptual overlap between these constructs (Ashton et al., 2014).

**수정 이유:**
- "demonstrates" → 제거 (상관 데이터로 "증명" 불가)
- "substantial" → "strong positive" (객관적 수치)
- 이론적 선행연구 인용으로 근거 보강

---

### 예시 4: 제한점 추가

**원문:**
> (Results 마지막 단락 없음)

**추가:**
> These findings should be interpreted with several limitations in mind. First, the cross-sectional nature of the data precludes causal inferences about the relationship between geography and personality. Second, the online convenience sample may not be fully representative of the general population. Third, regional differences could reflect selective migration (personality-driven relocation) rather than environmental influences.

**수정 이유:**
- 횡단면 연구의 인과 추론 한계
- 표집 방법의 일반화 한계
- 대안 설명 (선택적 이주) 제시

---

## 추가해야 할 단락

### Methods 섹션

#### Data and Code Availability

```markdown
### Data and Code Availability

Analysis code is available at [GitHub repository URL]. The SAPA data are 
collected through an ongoing project and are available for research purposes 
upon request from the SAPA Project (https://www.sapa-project.org/).
```

#### Statistical Considerations

```markdown
### Statistical Considerations

Given the exploratory nature of the state-level comparisons and the 63 
simultaneous tests (7 scales × 9 states), we employed a conservative 
significance threshold of |CR| > 3.0, corresponding to p < .003 under 
the normal approximation. This threshold provides conservative control 
for multiple comparisons. All p-values reported for individual comparisons 
are uncorrected; readers should interpret the pattern of results rather 
than any single comparison.
```

### Results 섹션

#### Limitations

```markdown
### Limitations

Several limitations warrant consideration. First, the cross-sectional 
design precludes causal inferences about the origins of regional 
personality differences. Second, as an online convenience sample, 
participants may differ systematically from the general population in 
ways that affect generalizability. Third, the observed regional 
differences could reflect selective migration (i.e., individuals with 
certain personality profiles choosing to live in particular states) 
rather than environmental influences. Fourth, we did not control for 
potential confounding variables such as age, education, or urbanicity, 
which may partially account for the observed patterns.
```

---

## 표현 대체 사전

### 반드시 수정

| 원문 | 수정안 | 이유 |
|------|--------|------|
| meaningful | statistically significant | 객관성 |
| demonstrates | suggests / indicates | overclaim 방지 |
| proves | provides evidence for | overclaim 방지 |
| causes | is associated with | 인과 회피 |
| residents | respondents | 일반화 제한 |

### 권장 수정

| 원문 | 수정안 | 이유 |
|------|--------|------|
| substantial | strong (r > .5) / moderate (r = .3-.5) | 객관적 기준 |
| clearly | (삭제) | 불필요한 강조 |
| undoubtedly | likely / possibly | 확신도 조절 |
| unique to | potentially related to | 일반화 제한 |

---

## 체크리스트

### Methods 수정 확인
- [ ] Python 버전 및 패키지 명시
- [ ] 코드/데이터 공개 여부 명시
- [ ] SAPA 인용 추가 (Condon & Revelle, 2014)
- [ ] CR 공식 명시
- [ ] 다중 비교 보정 설명 (63개 비교)
- [ ] 최소 N=100 기준 근거 (SE < 0.1)
- [ ] 온라인 샘플 제한점 언급
- [ ] Statistical Considerations 단락 추가

### Results 수정 확인
- [ ] "meaningful" → "statistically significant" 변경
- [ ] Top 3 Overclaim 모두 수정
- [ ] 모든 r 값에 p 값 추가
- [ ] 모든 CR 값에 p 값 추가
- [ ] "residents" → "respondents" 변경
- [ ] "demonstrates" → "suggests/indicates" 변경
- [ ] Limitations 단락 추가

### 전체 확인
- [ ] 용어 일관성 (Honesty-Humility, H-H)
- [ ] 숫자 형식 일관성 (쉼표, 소수점)
- [ ] Figure/Table 참조 정확성
- [ ] APA 7th Edition 형식 준수
- [ ] 문법/철자 오류 없음

---

## 수정 완료 후 검증

수정된 원고가 다음 조건을 충족하는지 확인:

1. **프루프리딩 보고서의 Must Fix 항목 100% 반영**
2. **Should Fix 항목 80% 이상 반영**
3. **Top 3 Overclaim 모두 수정**
4. **새로운 overclaiming 표현 없음**
5. **일관된 문체와 용어 사용**
