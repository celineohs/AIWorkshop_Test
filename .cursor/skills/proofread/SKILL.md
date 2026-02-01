---
name: proofread
description: 학술 문서를 검토하고 평가합니다. "프루프리딩", "proofread", "논문 검토", "Methods 평가", "Results 평가", "overclaim 분석" 요청 시 사용.
---

# Proofreading Skill

학술 문서를 Nature 리뷰어 관점에서 검토하고 평가합니다.

> 모든 상세 내용은 `reports/proofreading_guide.md` 참조

---

## 동작 순서

1. **GitHub 파일 참조** (필요시)
   - 사용자가 제공한 GitHub 링크에서 원본 문서 확인
   - 관련 코드/데이터 파일 검토

2. **Methods 섹션 평가**
   - 5가지 측면에서 약점 지적: Reproducibility, Controls, Sample size/power, Statistical appropriateness, Validation
   - 각 약점에 대해: 구체적 문제점, 리뷰어 예상 질문, 개선 방안 제시

3. **Results 섹션 평가**
   - 각 문장별 Claim type, Evidence level, Overclaiming risk 분석
   - 가장 위험한 overclaim 3개 지적 및 수정 방법 제시

4. **종합 프루프리딩**
   - 평가 결과 통합
   - 수정 사항 도출
   - 최종 권고안 작성

---

## Methods 평가 프롬프트

```
다음 Methods 섹션을 Nature 리뷰어 관점에서 평가해줘:

[Methods text]

다음 5가지 측면에서 약점을 지적:
1. Reproducibility (재현성)
2. Controls (통제)
3. Sample size/power (샘플/검정력)
4. Statistical appropriateness (통계 적절성)
5. Validation (타당성)

각 약점에 대해:
- 구체적 문제점
- 리뷰어가 제기할 질문
- 개선 방안
```

---

## Results 평가 프롬프트

```
다음 Results 문장들을 분석해줘:

[Results text]

각 문장에 대해:
1. Claim type (causal/correlational/mechanistic/general)
2. Evidence level (direct/indirect/suggestive)
3. Overclaiming risk (1-10)
4. Conservative alternative phrasing

그리고:
- 가장 위험한 overclaim 3개 지적
- 각각을 데이터에 맞게 수정하는 방법
```

---

## 참고

> 평가 기준, 출력 템플릿, 참고 문서 목록은 모두 `reports/proofreading_guide.md` 참조
