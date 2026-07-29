- [[알고리즘 패러다임]] - [[Brute Force]]
- [[알고리즘 문제]] - [[Sorting]]

```cpp
INSERTION_SORT(arr[] A, int n)
	for i = 2 ~ n
		key = A[i] // 현재 element 값
		// A[i] 를 정렬된 subarray A[1 ~ i-1] 의 적절한 위치에 넣기
		// A[1 ~ i-1] 은 이미 정렬되어 있음
		j = i - 1
		while (j > 0) && (A[j] > key)
			A[j+1] = A[j]
			j--
		A[j+1] = key
```

- Sorting 과정
	- i 는 -> 쪽으로 이동
	- j 는 <- 쪽으로 이동하면서 비교
		- 자신보다 낮은 값 -> break
		- 자신보다 큰 값 -> swap

- [[Loop Invariant]] 증명 : `A[i]`에 대해서 `A[1 ~ i-1]` 이 정렬되어 있다는 것 보이기
	- Initialization : `i = 2` 일 때 `A[1]` 은 한개의 원소 이므로 정렬되어 있음
	- Maintanence : `for`은 `A[i]`의 올바른 위치를 찾을 때 까지 오른쪽으로 한자리씩 이동 
	- Termination : `for`루프는 $i = n+1$ 이면 종료. `A[1 ~ n]` 은 정렬된 배열

## [[알고리즘 분석]]
- [[실행 case 분석]] -> worst case 기준

- Upper bound : 입력이 어떻든 상한이 $O(n^2)$
	- 최악의 경우에도 $O(n^2)$을 넘지 않음
		- 바깥 for : n-1 회 실행
		- 안쪽 while : i-1 회 실행
	- 전체 실행 $(n-1)(n-1)$ => $O(n^2)$

- Lower bound : 입력이 최소여도 하한이 $\Omega(n^2)$
	- worst case 에서 $n^2$ 만큼 걸리는 입력이 적어도 하나 존재함을 보임
		- ![[Pasted image 20260629093638.png]]
		- 적절한 위치로 가기 위해서는 적어도 중간 구간을 통과해야함 → 최소 $\frac{n}{3}$ 씩 이동
		- 구간이 3개로 나눠질 때 → worst case 이므로 큰 값들이 맨 처음 구간 `A[1:n/3]` 에 있음

	$$  
	\underbrace{\frac{n}{3}}_{\text{이동하는 값의 개수}} \times \underbrace{\frac{n}{3}}_{\text{각자 이동하는 최소 거리}} = \frac{n^2}{9}  
$$
	- 따라서 최소로 이동한다고 하더라도 $n^2$ 만큼의 시간 필요  ⇒ $\Omega(n^2)$

- Tight bound 
	- worst case 에 대해 $O(n^2) = \Omega(n^2) = \Theta(n^2)$