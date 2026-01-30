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

| current_step | 생성할 노트북 | 참조 |
|--------------|--------------|------|
| `preprocess` | 02_preprocessing.ipynb | preprocessing_guide.md |
| `viz` | 03_visualization.ipynb | step2 결과 |
| `state_analysis` | 04_state_analysis.ipynb | stats.md |

---

## Step 2: Preprocessing

### 참조
- `reports/preprocessing_guide.md` (점수 계산 공식)

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
- `reports/stats.md` (Critical Ratios 방법론)

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

## 노트북 공통 규칙

1. 첫 셀: `%pip install` (필요한 패키지)
2. 작업 디렉토리: notebooks에서 실행 시 상위로 이동
3. 상대 경로만 사용

---

## 주의사항

### Index 정렬 문제
QC로 응답자를 제외하면 index가 불연속적이 됩니다. Ideology, H-H 계산 시 z-score 결과를 할당할 때 `.values`를 사용해서 index 정보를 제거해야 합니다. 안 그러면 상관관계가 거의 0으로 나오는 오류가 발생합니다.

### 커널 재시작
이전 노트북 수정 후 다음 노트북을 확인할 때는 커널을 재시작해야 합니다. 캐시된 데이터가 사용되어 수정 사항이 반영 안 될 수 있습니다.
