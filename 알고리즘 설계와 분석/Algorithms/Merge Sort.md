- [[알고리즘 패러다임]] : [[Divide and Conquer]]
- [[알고리즘 문제]] : [[Sorting]]

## Divide and Conquer
### Divide
- `A[p ~ r]` 를 두 배열로 나누기
	- `A[p ~ q]`
	- `A[q+1 ~ r]`
- 기준 : `q`

### Conquer 
- 나눠진 두 배열 `A[p ~ q]`, `A[q+1 ~ r]` 을 각각  sorting

### Combine 
- 정렬된 두 배열 합치기


```cpp
MERGE_SORT(arr A, start p, end r) 
	if p >= r // base case : 요소가 1개 이하
		return
	q = (p+r)/2
	
	// Divide & Conquer
	MERGE_SORT(A, p, q)   // p ~ q 까지 재귀적으로 sort
	MERGE_SORT(A, q+1, r) // q+1 ~ r 를 재귀적으로 sort 

	// Combine : 두 배열 합치기
	MERGE(A, p, q, r)
```

> [!note]- `MERGE`
> ![[Pasted image 20260629095742.png]]
> ![[Pasted image 20260629095748.png]]
> - L / R 의 맨 앞 요소 비교해 더 작은 값을 원래 배열에 저장
> - 한쪽 끝 도달 시 반대쪽 끝 나머지 모두 옮기기


- 시간 <-> 공간 trade off

## [[알고리즘 분석]]
- base case : element 개수가 작을 때 $\Theta(1)$ 
- recursion case 
	- Divide : $\Theta(1)$
	- Conquer : $2T(\frac{n}{2})$
	- Combine : $\Theta(n)$

> [!note] 전체 식
> 
> $$
>	T(n) = 2T\left( \frac{n}{2} \right) + \Theta(n)
> $$

- [[Master Method]] 사용 : [[시간 복잡도]] $O(n \lg n)$
- [[Substitution Method]] 
	1. Guess : $T(n) = O(n\lg n)$ 
	2. Prove
		1. Inductive Case
		   ![[Pasted image 20260701110200.png]]
		2. Base case 
		   ![[Pasted image 20260701110225.png]]