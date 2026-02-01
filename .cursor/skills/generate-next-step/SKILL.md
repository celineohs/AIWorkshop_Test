---
name: generate-next-step
description: 다음 단계 노트북을 생성합니다. "다음 단계 만들어줘" 요청 시 사용.
---

# 다음 단계 노트북 생성 (generate-next-step)

## 동작

1. `reports/pipeline_context.json` → `current_step` 확인
2. 해당 step의 참조 파일 읽기
3. 노트북 생성

## 파이프라인
| current_step | 생성할 파일 | 참조 |
|--------------|------------|------|
| `preprocess` | 02_preprocessing.ipynb | preprocessing_guide.md |
| `viz` | 03_visualization.ipynb | step2 결과 |
| `state_analysis` | 04_state_analysis.ipynb | stats.md |
| `writing` | step5_draft_method.md, step5_draft_results.md | writing.md |
| `proofreading` | step6_proofreading_report.md | proofreading_guide.md |
| `revision` | step7_revised_method.md, step7_revised_results.md | revision.md |
---

## Step 2: Preprocessing

### 참조
- `guides/preprocessing_guide.md` (점수 계산 공식)

### 분석 순서
1. **QC**: 응답 부족(10개 미만), Straight-lining 제외
2. **Big Five**: superKey696.csv로 NEO_O, NEO_C, NEO_E, NEO_A, NEO_N 계산
3. **Ideology**: z(MPQtr) + z(NEOo6)*-1 의 평균
4. **Honesty-Humility**: z(NEOa2) + z(NEOa4) + z(HEXACO_H) 의 평균
5. **저장**: data/processed/sapa_scores.csv

### 출력할 내용
- QC 결과 (제외 인원, 유효 N)
- 각 척도별 N, Mean, SD

---

## Step 3: Visualization

### 참조
- `reports/step2_preprocess.json` (계산된 척도 목록)

### 분석 순서
1. **상관행렬**: 7개 척도 간 상관 히트맵, pairwise N 확인
2. **분포**: Big Five 히스토그램, Ideology/H-H 히스토그램

### 출력할 내용
- 상관행렬 PNG
- 분포 히스토그램 PNG
- 주요 상관관계 수치

---

## Step 4: State Analysis

### 참조
- `guides/stats.md` (Critical Ratios 방법론)

### 분석 순서
1. **데이터 준비**: state 변수 병합, "other" 제외 (9개 주만)
2. **기술통계**: State × 척도별 N, Mean, SE
3. **Critical Ratios**: CR = (State Mean - Grand Mean) / SE
4. **유의미 판정**: |CR| > 3.0 → 유의미 (p < .003)

### 출력할 내용
- State별 표본 수
- 유의미한 특징 목록 (State, 척도, CR값, 방향)
- 히트맵 PNG

---

## Step 5: Writing

### 참조
- `guides/writing.md` (JSON 경로 매핑, 글쓰기 원칙)

### 작성 순서
1. step1~4 JSON 파일 읽기
2. writing.md의 경로 매핑 참조하여 값 추출
3. Method/Results 초안 생성

### 출력할 내용
- `reports/step5_draft_method.md`
- `reports/step5_draft_results.md`

---

## 노트북 공통 규칙

1. 첫 셀: `%pip install` (필요한 패키지)
2. 작업 디렉토리: notebooks에서 실행 시 상위로 이동
3. 상대 경로만 사용

---

## 주의사항

### z-score 계산 시 Index 유지
Ideology, H-H 계산 시 z-score를 DataFrame에 할당할 때 **반드시 index를 유지**해야 합니다.

```python
# ❌ 잘못된 방법 (NaN 전체 발생)
z_mpqtr = stats.zscore(scores['MPQ_Traditionalism'].values)
scores['Ideology'] = (z_mpqtr + z_neo_lib * -1) / 2

# ✅ 올바른 방법 (pd.Series로 index 유지)
valid_mask = scores['MPQ_Traditionalism'].notna() & scores['NEO_Liberalism'].notna()
mpqtr_valid = scores.loc[valid_mask, 'MPQ_Traditionalism']
z_mpqtr = pd.Series(stats.zscore(mpqtr_valid.values), index=mpqtr_valid.index)
```

### 컬럼명 규칙
Big Five 컬럼은 **약어** 사용: `NEO_O`, `NEO_C`, `NEO_E`, `NEO_A`, `NEO_N`
- ❌ `NEO_Openness` → KeyError 발생
- ✅ `NEO_O`

### 커널 재시작
이전 노트북 수정 후 다음 노트북을 확인할 때는 커널을 재시작해야 합니다.

### Writing Step 전제조건
step1~step4 JSON 파일이 모두 존재해야 writing step 실행 가능.

---
## Step 6: Proofreading

### 참조
- `guides/proofreading_guide.md` (평가 기준, Few-shot 예시, 템플릿)
- `reports/step5_draft_method.md` (평가 대상)
- `reports/step5_draft_results.md` (평가 대상)

### 평가 순서
1. **Methods 평가**: 5가지 기준 (Reproducibility, Controls, Sample size, Statistical appropriateness, Validation)
2. **Results 평가**: 각 문장별 Claim type, Evidence level, Overclaiming risk
3. **Top 3 Overclaim 식별**: 가장 위험한 문장 3개와 수정안
4. **종합 보고서 작성**: Must Fix / Should Fix / Nice to Have 분류

### 출력할 내용
- `reports/step6_proofreading_report.md`

### 전제조건
- step5_draft_method.md 존재
- step5_draft_results.md 존재

---
## Step 7: Revision

### 참조
- `reports/step5_draft_method.md` (원본 Method 초안)
- `reports/step5_draft_results.md` (원본 Results 초안)
- `reports/step6_proofreading_report.md` (프루프리딩 평가 및 수정 사항)

### 수정 순서
1. 프루프리딩 보고서의 "필수 수정 사항 (Must Fix)" 확인
2. Methods 섹션 수정 (재현성, 통제, 검정력, 통계 적절성, 타당성)
3. Results 섹션 수정 (overclaiming 완화, 표현 보수화)
4. "수정 전후 비교" 섹션의 수정안 반영

### 출력할 내용
- `reports/step7_revised_method.md`
- `reports/step7_revised_results.md`

### Revision 전제조건
- step5_draft_method.md 존재
- step5_draft_results.md 존재
- step6_proofreading_report.md 존재
