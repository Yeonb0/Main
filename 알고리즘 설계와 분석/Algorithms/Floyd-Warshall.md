---
aliases:
  - 플로이드 워셜
domain:
  - graph
formulation:
  - optimization
techniques:
  - DP
---
### Optimal substructure
- i -> j 까지 가는 경로 중간 node k 사용
- k = 0 -> 중간 node X
- k ≥ 1 -> 중간 node 1개 이상
	- 이미 도착한 경우 -> k-1 개
	- 중간 node 인 경우 -> (i -> k) + (k -> j)
	-> 둘 중 낮은 값 고르기

### Pseudocode
```cpp
FLOYD_WARSHALL(weight[] w, #node n) 
	D(0) = W      // 0 개 node 사용 -> w 로 초기화
	for k = 1 ~ n // 중간 node 수 고정
		let D(k) = d(k)[i][j] be a new n * n matrix // k 번째 만들기
		for i = 1 ~ n
			for j = 1 ~ n
				d(k)[i][j] = min(d(k-1)[i][j], d(k-1)[i][k] + d(k-1)[k][j]
				// 그 이전 완료 vs i->k + k->j 중 작은 거 고르기
	return D(n) // 0 부터 채워나가서 n 완성
```

### 성능 분석
 - $\Theta(n^3)$

### [[Transitive Closure]]
