---
name: capture-results
description: 노트북 실행 결과를 저장합니다. "결과 저장", "저장해줘" 요청 시 사용.
---

# 결과 저장 (capture-results)

## 목적

노트북 실행 결과를 JSON 파일로 저장하여, 다음 단계에서 참조할 수 있게 합니다.

## 동작

1. 현재 실행된 노트북이 무엇인지 파악
2. 노트북의 각 셀 출력에서 주요 수치와 결과를 최대한 많이 추출
3. `reports/step{N}_{name}.json`으로 저장
4. `reports/pipeline_context.json`의 current_step을 다음 단계로 업데이트

## 저장 원칙

- 노트북에서 출력된 모든 주요 수치를 빠짐없이 저장
- 각 분석 단계별 결과를 구분하여 기록 (QC, Big Five, Ideology 등)
- 척도별 N, Mean, SD 등 통계량은 모두 포함
- 이미지 파일이 생성된 경우 파일 경로만 기록
- 다음 단계에서 필요할 수 있는 정보는 모두 포함

## 파이프라인 흐름

```
scan → preprocess → viz → state_analysis → done
```

## 참고

- generate-next-step 스킬이 이 파일들을 참조하여 다음 노트북 생성
- 이전 step 파일들과 일관성 유지
