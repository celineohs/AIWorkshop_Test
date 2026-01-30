# SAPA 데이터 전처리 프로젝트

## 개요

- **데이터**: SAPA (Synthetic Aperture Personality Assessment) 성격 검사
- **특징**: 696개 문항, planned missingness (설계된 결측)
- **목표**: 데이터 탐색 → 전처리 (QC + 점수 계산) → 시각화

---

## 파이프라인 구조 (3 Steps)

```
┌─────────────────────────────────────────────────────────────┐
│  Step 1: Data Scan                                          │
│  → 01_data_scan.ipynb                                       │
│  → 데이터 구조 파악, 결측 패턴 확인                          │
│                    ↓                                        │
│  Step 2: Preprocessing (통합)                               │
│  → 02_preprocessing.ipynb                                   │
│  → QC + 역채점 + Big Five/Ideology/H-H 점수 계산            │
│  → preprocessing_guide.md 참조!                             │
│                    ↓                                        │
│  Step 3: Visualization                                      │
│  → 03_visualization.ipynb                                   │
│  → 상관행렬, 분포, 박스플롯                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## Skills (2개)

| Skill | 역할 | 요청 예시 |
|-------|------|----------|
| `capture-results` | 노트북 결과 → Context JSON 저장 | "결과 저장해줘" |
| `generate-next-step` | Context 기반 → 다음 노트북 생성 | "다음 단계 만들어줘" |

---

## 핵심 파일

| 파일 | 용도 |
|------|------|
| `reports/pipeline_context.json` | 파이프라인 상태 (AI가 읽음) |
| `preprocessing_guide.md` | **전처리 로직, 점수 계산식** |
| `data/raw/superKey696.csv` | 채점 키 (역채점 정보 포함) |

---

## 사용 흐름

```
[Step 1]
사용자: (01_data_scan.ipynb 실행)
사용자: "결과 저장해줘"
AI: → pipeline_context.json 저장 (current_step: "preprocess")

[Step 2]
사용자: "다음 단계 만들어줘"
AI: → preprocessing_guide.md 참조 → 02_preprocessing.ipynb 생성
사용자: (실행 후) "결과 저장해줘"
AI: → context 업데이트 (current_step: "viz")

[Step 3]
사용자: "다음 단계 만들어줘"
AI: → 03_visualization.ipynb 생성
```

---

## 중요 참고사항

1. **Planned Missingness**: SAPA의 결측은 오류가 아니라 설계된 것
2. **preprocessing_guide.md**: 점수 계산 공식이 있으므로 반드시 참조
3. **출력 위치**: 점수 → `data/processed/`, 리포트 → `reports/`
