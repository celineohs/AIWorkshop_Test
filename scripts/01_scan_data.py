"""
SAPA 데이터 스캔 스크립트
실행: python scripts/01_scan_data.py
"""

import pandas as pd
import os

def main():
    print("=" * 60)
    print("SAPA 데이터 스캔")
    print("=" * 60)
    
    # 데이터 로드
    df = pd.read_csv('data/raw/sapa_data.csv')
    keys = pd.read_csv('data/raw/superKey696.csv', index_col=0)
    
    # 기본 정보
    n_respondents = len(df)
    n_cols = len(df.columns)
    
    # 인구통계 vs 문항 구분
    demo_cols = ['RID', 'gender', 'relstatus', 'age', 'marstatus', 'height', 'BMI', 
                 'weight', 'exer', 'smoke', 'country', 'state', 'ethnic', 'education',
                 'jobstatus', 'occPrestige', 'occIncomeEst', 'p1edu', 'p1occPrestige',
                 'p1occIncomeEst', 'p2edu', 'p2occPrestige', 'p2occIncomeEst']
    item_cols = [col for col in df.columns if col.startswith('q_')]
    
    # 결측 패턴
    item_missing_rate = df[item_cols].isnull().mean().mean()
    avg_responses = df[item_cols].notna().sum(axis=1).mean()
    
    print(f"\n📊 기본 정보")
    print(f"  응답자 수 (N): {n_respondents:,}")
    print(f"  전체 변수 수: {n_cols}")
    print(f"  인구통계 변수: {len(demo_cols)}개")
    print(f"  성격 문항: {len(item_cols)}개")
    
    print(f"\n📉 결측 패턴 (Planned Missingness)")
    print(f"  문항 결측률: {item_missing_rate:.1%}")
    print(f"  응답자당 평균 응답 문항: {avg_responses:.0f}개")
    
    print(f"\n📁 채점 키 정보")
    print(f"  파일: data/raw/superKey696.csv")
    print(f"  척도 수: {len(keys.columns)}개")
    
    # 리포트 생성
    os.makedirs('reports', exist_ok=True)
    report = f"""# 데이터 개요 리포트

## 기본 정보
- **응답자 수 (N)**: {n_respondents:,}
- **전체 변수 수**: {n_cols}
- **인구통계 변수**: {len(demo_cols)}개
- **성격 문항**: {len(item_cols)}개

## 결측 패턴 (Planned Missingness)
- **문항 결측률**: {item_missing_rate:.1%}
- **응답자당 평균 응답 문항**: {avg_responses:.0f}개

> SAPA는 planned missingness 설계입니다. 
> 각 참가자가 전체 696문항 중 일부만 응답하도록 설계되어 결측이 많아도 정상입니다.

## 인구통계 변수
{', '.join(demo_cols)}

## 성격 문항
- 총 {len(item_cols)}개 문항 (q_6, q_20, q_22, ...)
- 척도: 1(매우 부정확) ~ 6(매우 정확)

## 채점 키 정보
- 파일: `data/raw/superKey696.csv`
- 척도 수: {len(keys.columns)}개
- 주요 척도: NEO_O, NEO_C, NEO_E, NEO_A, NEO_N, HEXACO_H, MPQtr 등
"""
    
    with open('reports/data_overview.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ 저장 완료: reports/data_overview.md")

if __name__ == "__main__":
    main()
