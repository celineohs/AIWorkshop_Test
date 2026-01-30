---
name: capture-results
description: 노트북 실행 결과를 단계별 JSON 파일로 저장합니다. "결과 저장", "context 저장" 요청 시 사용합니다.
---

# 결과 캡처 (capture-results)

## 목적

각 노트북 실행 결과를 **단계별 JSON 파일로 저장**합니다.
`generate-next-step` skill이 이 파일들을 **누적 참조**합니다.

## 저장 방식: 단계별 새 파일 생성

```
reports/
├── preprocessing_guide.md      ← 항상 존재 (전처리 가이드)
├── stats.md                    ← 항상 존재 (통계 분석 가이드)
├── step1_scan.json             ← Step 1 완료 시 생성
├── step2_preprocess.json       ← Step 2 완료 시 생성
├── step3_viz.json              ← Step 3 완료 시 생성
├── step4_state.json            ← Step 4 완료 시 생성
└── pipeline_context.json       ← 현재 상태 요약 (current_step)
```

## 파이프라인 구조 (4 Steps)

| Step | 노트북 | 생성 파일 | 다음 current_step |
|------|--------|----------|------------------|
| 1 | 01_data_scan.ipynb | `step1_scan.json` | preprocess |
| 2 | 02_preprocessing.ipynb | `step2_preprocess.json` | viz |
| 3 | 03_visualization.ipynb | `step3_viz.json` | state_analysis |
| 4 | 04_state_analysis.ipynb | `step4_state.json` | done |

---

## Step별 JSON 파일 내용

### Step 1: `step1_scan.json`

```json
{
  "step": 1,
  "name": "data_scan",
  "timestamp": "2026-01-30 14:00",
  "results": {
    "n_respondents": 23679,
    "n_items": 696,
    "missing_rate": 0.876,
    "avg_responses": 86,
    "response_range": [0, 311],
    "n_scales": 131
  },
  "notes": ["Planned missingness confirmed"]
}
```

### Step 2: `step2_preprocess.json`

```json
{
  "step": 2,
  "name": "preprocessing",
  "timestamp": "2026-01-30 15:00",
  "results": {
    "qc": {
      "min_responses": 10,
      "low_response_count": 1,
      "straight_lining_count": 31,
      "flagged_count": 32,
      "valid_n": 23647
    },
    "scores": {
      "calculated_scales": ["NEO_O", "NEO_C", "NEO_E", "NEO_A", "NEO_N", "Ideology", "Honesty_Humility"],
      "valid_n": 23357,
      "output_file": "data/processed/sapa_scores.csv"
    }
  },
  "notes": []
}
```

### Step 3: `step3_viz.json`

```json
{
  "step": 3,
  "name": "visualization",
  "timestamp": "2026-01-30 16:00",
  "results": {
    "generated_files": [
      "reports/correlation_matrix.png",
      "reports/big_five_distributions.png",
      "reports/ideology_hh_distributions.png",
      "reports/big_five_boxplot.png"
    ],
    "scales_visualized": ["NEO_O", "NEO_C", "NEO_E", "NEO_A", "NEO_N", "Ideology", "Honesty_Humility"]
  },
  "notes": []
}
```

### Step 4: `step4_state.json`

```json
{
  "step": 4,
  "name": "state_analysis",
  "timestamp": "2026-01-30 17:00",
  "results": {
    "n_states": 10,
    "states": ["CA", "FL", "IL", "MI", "NY", "PA", "TX", "VA", "WA", "other"],
    "anova": {
      "significant_scales": ["NEO_O", "Ideology"],
      "p_values": {"NEO_O": 0.001, "Ideology": 0.003}
    },
    "critical_ratios": {
      "CA": {"NEO_O": 3.5, "Ideology": -4.2},
      "TX": {"Ideology": 5.1}
    },
    "generated_files": [
      "reports/state_boxplot.png",
      "reports/state_heatmap.png"
    ]
  },
  "notes": ["State-level analysis (논문 축소 버전)"]
}
```

---

## pipeline_context.json 업데이트

`pipeline_context.json`은 **현재 상태 요약**만 담당:

```json
{
  "last_updated": "2026-01-30 15:00",
  "steps_completed": ["scan", "preprocess"],
  "current_step": "viz"
}
```

---

## 코드 예시

### Step 1 결과 저장

```python
import json
import os
from datetime import datetime

# Step 1 결과
step1_result = {
    "step": 1,
    "name": "data_scan",
    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M'),
    "results": {
        "n_respondents": len(df),
        "n_items": len(item_cols),
        "missing_rate": round(missing_rate, 3),
        "avg_responses": int(responses.mean())
    },
    "notes": ["Planned missingness confirmed"]
}

# 새 파일로 저장
with open('reports/step1_scan.json', 'w', encoding='utf-8') as f:
    json.dump(step1_result, f, indent=2, ensure_ascii=False)

# pipeline_context.json 업데이트
ctx = {
    "last_updated": step1_result["timestamp"],
    "steps_completed": ["scan"],
    "current_step": "preprocess"
}
with open('reports/pipeline_context.json', 'w', encoding='utf-8') as f:
    json.dump(ctx, f, indent=2, ensure_ascii=False)

print("✅ step1_scan.json 저장 완료!")
```

### Step 2 결과 저장

```python
# Step 2 결과
step2_result = {
    "step": 2,
    "name": "preprocessing",
    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M'),
    "results": {
        "qc": {
            "flagged_count": len(exclude_ids),
            "valid_n": len(data_clean)
        },
        "scores": {
            "calculated_scales": ["NEO_O", "NEO_C", "NEO_E", "NEO_A", "NEO_N", "Ideology", "Honesty_Humility"],
            "output_file": "data/processed/sapa_scores.csv"
        }
    },
    "notes": []
}

# 새 파일로 저장
with open('reports/step2_preprocess.json', 'w', encoding='utf-8') as f:
    json.dump(step2_result, f, indent=2, ensure_ascii=False)

# pipeline_context.json 업데이트
with open('reports/pipeline_context.json', 'r', encoding='utf-8') as f:
    ctx = json.load(f)
ctx["last_updated"] = step2_result["timestamp"]
ctx["steps_completed"].append("preprocess")
ctx["current_step"] = "viz"
with open('reports/pipeline_context.json', 'w', encoding='utf-8') as f:
    json.dump(ctx, f, indent=2, ensure_ascii=False)

print("✅ step2_preprocess.json 저장 완료!")
```

---

## AI Agent 동작

```
사용자: "결과 저장해줘"

AI:
1. 현재 어떤 노트북이 실행되었는지 파악
2. 해당 step의 JSON 파일 새로 생성 (step1_scan.json 등)
3. pipeline_context.json의 current_step 업데이트
```

---

## 장점

- **각 단계 결과가 독립적으로 보존**
- **이전 결과 덮어쓰기 없음**
- **generate-next-step이 모든 step*.json 파일 참조 가능**
