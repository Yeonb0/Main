---
aliases:
  - DP
  - 동적 계획법
---

- 어떤 문제를 여러 개의 subproblem 으로 나누고 풀어서 합치기
- subproblem 이 overlap (중복 계산) 될 때 사용
- Tabular Method : table 이라는 추가적 저장 공간 사용
> [!note] Optimal Substructure : 최적 부분 구조 / 최적 하위 구조
> 어떤 문제의 최적해가 그 문제에 속한 부분 문제 (subproblem) 들의 최적해로 구성 -> DP 적용 가능


### 과정
1. Characterize the structure of an optimal solution
   최적해를 어떤 구조로 정의할지 분석
2. Recursively define the value of an optimal solution
   재귀적으로 ([[점화식]] 형태로) 최적해 정의
3. Compute the value of an optimal solution, typically in a bottom-up fashion
   Botton-Up 방식으로 코드를 통해 값 만들기
4. Construct an optimal solution from computed information
   계산된 정보로 optimal 한 해 만들기


### Example
-> 주로 [[Optimization]] 문제에서 사용
- [[Rod Cutting]]
- [[Matrix-Chain Multiplication]]