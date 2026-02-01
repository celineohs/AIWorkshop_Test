# SAPA 데이터 분석 파이프라인

AI Agent를 활용한 성격 데이터 분석 및 학술 논문 초안 작성 파이프라인입니다.

---

## 프로젝트 구조

```
SAPA/
├── INSTRUCTIONS.md              ← AI Agent 지침
├── README.md                    ← 이 파일
├── data/
│   ├── raw/                     ← 원본 데이터
│   │   ├── sapa_data.csv
│   │   ├── item_info.csv
│   │   └── superKey696.csv
│   └── processed/               ← 처리된 데이터
│       └── sapa_scores.csv
├── notebooks/                   ← 분석 노트북
│   ├── 01_data_scan.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_visualization.ipynb
│   └── 04_state_analysis.ipynb
├── reports/                     ← 분석 결과
│   ├── step1_scan.json
│   ├── step2_preprocess.json
│   ├── step3_viz.json
│   ├── step4_state.json
│   ├── step5_draft_method.md
│   ├── step5_draft_results.md
│   ├── step6_proofreading_report.md
│   ├── step7_revised_method.md
│   ├── step7_revised_results.md
│   ├── pipeline_context.json
│   └── figures/
├── guides/                      ← 가이드 및 스타일 문서
│   ├── preprocessing_guide.md
│   ├── stats.md
│   ├── writing.md
│   ├── proofreading_guide.md
│   ├── revision.md
│   ├── APA7-Style.pdf
│   ├── The Elements of Style.pdf
│   └── Writing Science.pdf
└── .cursor/skills/              ← AI 스킬
```

---

## 파이프라인 개요

| 단계 | 이름 | 생성 파일 | 트리거 |
|------|------|----------|--------|
| 1 | Scan | `01_data_scan.ipynb` → `step1_scan.json` | 초기 실행 |
| 2 | Preprocess | `02_preprocessing.ipynb` → `step2_preprocess.json` | "다음 단계 만들어줘" |
| 3 | Visualization | `03_visualization.ipynb` → `step3_viz.json` | "다음 단계 만들어줘" |
| 4 | State Analysis | `04_state_analysis.ipynb` → `step4_state.json` | "다음 단계 만들어줘" |
| 5 | Writing | `step5_draft_method.md`, `step5_draft_results.md` | "다음 단계 만들어줘" |
| 6 | Proofreading | `step6_proofreading_report.md` | "다음 단계 만들어줘" |
| 7 | Revision | `step7_revised_method.md`, `step7_revised_results.md` | "다음 단계 만들어줘" |

---

## 사용 방법

### 파이프라인 실행

```
"다음 단계 만들어줘"  →  노트북/문서 생성
"결과 저장해줘"      →  JSON으로 저장, 다음 단계로 전환
```

### 개별 스킬 호출

| 스킬 | 트리거 키워드 | 설명 |
|------|--------------|------|
| **capture-results** | "결과 저장", "저장해줘" | 노트북 결과를 JSON으로 저장 |
| **generate-next-step** | "다음 단계 만들어줘" | 파이프라인 다음 단계 생성 |
| **github-update** | "GitHub 업데이트", "커밋" | 변경사항을 GitHub에 업로드 |
| **proofread** | "프루프리딩", "논문 검토" | 학술 문서 검토 (파이프라인 외부에서도 사용 가능) |

---

## 가이드 문서

`guides/` 폴더에 파이프라인에서 참조하는 가이드라인 문서들이 있습니다.

| 파일 | 용도 |
|------|------|
| `guides/preprocessing_guide.md` | 전처리 및 척도 계산 방법 |
| `guides/stats.md` | Critical Ratios 통계 방법론 |
| `guides/writing.md` | Method/Results 작성 가이드 (Few-shot 예시 포함) |
| `guides/proofreading_guide.md` | 프루프리딩 평가 기준 (Few-shot 예시 포함) |
| `guides/revision.md` | 수정 전략 가이드 (Few-shot 예시 포함) |

---

## 데이터 설명

- **SAPA**: Synthetic Aperture Personality Assessment
- **출처**: [Harvard Dataverse](https://dataverse.harvard.edu/)
- **특징**: 
  - 696개 성격 문항
  - Planned missingness (설계된 결측) 구조
  - Big Five, Ideology, Honesty-Humility 척도

---

## 분석 결과 요약

| 항목 | 값 |
|------|-----|
| 원본 응답자 수 | 23,679명 |
| QC 후 응답자 수 | 23,647명 |
| 분석 척도 | 7개 (Big Five 5개 + Ideology + H-H) |
| State-level 분석 대상 | 9개 주, 7,308명 |
| 유의미한 CR 특징 | 8개 (│CR│ > 3.0) |

---

## 필요 라이브러리

```bash
pip install pandas numpy matplotlib seaborn scipy
```

---

## 학습 목표

1. AI Agent에게 **자연어로 작업 지시**하는 방법
2. **재현 가능한 분석 파이프라인** 구축
3. **학술 논문 초안** 자동 생성 및 검토
4. **Overclaiming 방지** 및 보수적 글쓰기 원칙
