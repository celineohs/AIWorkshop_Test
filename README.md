# SAPA 데이터 전처리 실습

AI Agent를 활용한 데이터 전처리 파이프라인 실습 프로젝트입니다.

---

## 프로젝트 구조

```
sapa-demo/
├── INSTRUCTIONS.md      ← AI Agent 지침 (핵심!)
├── README.md            ← 이 파일
├── data/
│   ├── raw/             ← 원본 데이터
│   └── processed/       ← 처리된 데이터 (생성 예정)
├── scripts/             ← 분석 스크립트 (생성 예정)
└── reports/             ← 리포트/시각화 (생성 예정)
```

---

## 사용 방법

### 1. Cursor에서 이 폴더 열기

```
File → Open Folder → sapa-demo 선택
```

### 2. AI에게 작업 지시하기

`Ctrl+L` (Chat 열기) 후 아래처럼 요청:

```
@INSTRUCTIONS.md 이 지침대로 데이터 스캔해줘
```

### 3. 단계별 실습

| 단계 | 요청 예시 |
|------|----------|
| 1. 스캔 | "데이터 구조 파악해줘" |
| 2. QC | "QC 리포트 만들어줘" |
| 3. 점수 | "Big Five 점수 계산해줘" |
| 4. 시각화 | "상관관계 시각화 만들어줘" |
| 5. 정리 | "README 업데이트해줘" |

---

## 데이터 설명

- **SAPA**: Synthetic Aperture Personality Assessment
- **출처**: [Harvard Dataverse](https://dataverse.harvard.edu/)
- **특징**: 
  - 696개 성격 문항
  - Planned missingness (설계된 결측) 구조
  - Big Five 성격 요인 측정

---

## 실행 결과 요약

<!-- AI가 자동으로 이 부분을 업데이트합니다 -->

| 항목 | 값 |
|------|-----|
| 마지막 실행 | - |
| 응답자 수 (N) | - |
| 문항 수 | - |
| 생성된 리포트 | - |

---

## 필요 라이브러리

```bash
pip install pandas numpy matplotlib seaborn
# 선택: pip install plotly
```

---

## 학습 목표

1. AI Agent에게 **자연어로 작업 지시**하는 방법
2. **재현 가능한 전처리 파이프라인** 구축
3. **INSTRUCTIONS 파일**로 AI 행동 가이드하기
