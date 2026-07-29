---
aliases:
  - 분할정복
  - 분할 정복
---

- 전체 입력 n 개를 작게 쪼개서 해결 후 다시 합치기

### Divide
- base case 만날 때 까지 n 개의 입력을 쪼갬

### Conquer
- 쪼갠 case 들을 recursive 하게 풀기

### Combine 
- 계산한 case 들을 다시 합치기


## [[실행 시간 분석]]
1. [[점화식]] 정의
2. [[점화식]] 풀어서 점근해 구하기
3. [[Big O-notation]] / [[Θ-notation]] 으로 나타내기
$$
	T(n) = \begin{cases} \Theta(1) & \text{if } n < n_0 \\ D(n) + aT(n/b) + C(n) & \text{otherwise} \end{cases}
$$

- base case : 실행 비용 매우 작음 $\Theta(1)$
- recursive case
	- $D(n)$ : Divide
	- $aT(\frac{n}{b})$ : Conquer
		- $a$ : 나눈 case 를 Conquer 하는 횟수
		- $b$ : case 를 나누는 횟수
### [[Substitution Method]]

### [[Recursion Tree]]

### [[Master Method]]
