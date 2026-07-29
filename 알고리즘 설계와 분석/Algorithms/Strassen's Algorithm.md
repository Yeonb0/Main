- matrix 의 곱셈식을 8개에서 줄여보자
- Idea : 합차 공식 $x^{2} - y^{2} = (x+y)(x-y)$

### Divide
- n = 1 이면 base case 
- n > 1 이면 recursive case
	- matrix 를 $\frac{n}{2} \times \frac{n}{2}$ 로 나누기
- 기존 matrix 를 더하거나 빼서 $S_{1} \sim S_{10}$ 만들기
   ![[Pasted image 20260629112343.png]]

### Conquer
- 기존 matrix & $S$ 곱해서 $P_{1} \sim P_{7}$ 구하기
![[Pasted image 20260629112439.png]]

### Combine
- $P$ 를 더해서 원래 구하려던 matrix $C$ 구하기
  ![[Pasted image 20260629112606.png]]
- 각각의 C 는 원래 원하던 값과 동일하게 나옴

## [[알고리즘 분석]]
- base case (n = 1) : 두 수 곱하기 -> $\Theta(1)$
- recursive case (n > 1)
	- Divide : matrix 절반 쪼개기 -> $\Theta(1)$
	- Conquer
		- S 행렬 10개 생성 -> $\Theta(n^{2})$ 
		- P 행렬 7개 계산 -> $7T\left( \frac{n}{2} \right)$ 
	- Combine : P 로 C 계산 -> $\Theta(n^{2})$

> [!note] 전체 식
> 
> $$
>		T(n) = 7T\left( \frac{n}{2} \right) + \Theta(n^{2})
> $$
- [[Master Method]] 사용 : [[시간 복잡도]] $O(n^{2.81})$
