---
aliases:
  - Johnson
domain:
  - graph
formulation:
  - optimization
techniques:
  - DP
---
- edge 가 적을 때 [[Dijkstra]] 알고리즘을 사용
	- 단 음수 weight edge 불가능

### Reweighting
- 유지해야 하는 성질
	1. 조정된 가중치를 이용해도 shortest path 동일
	2. 각 가중치가 0 보다 커야 함

> [!note] Lemma
> $\hat{w}(u, v) = w(u, v) + h(u) - h(v)$

> [!note] Claim
> $\hat{w}(u, v) = w(u, v) + h(u) - h(v) \geq 0$

- $h(v) = \delta(s, v)$
- $s$ 는 원래 있는 모든 node 들과 weight 값 0 으로 연결되는 새로운 node 

### Pseudocode
```cpp
JOHNSON(graph[][] G, weight w)
	compute G`, where G`.v = G.V ∪ {s},
		G`E = G.E ∪ {(s, v) : v ∈ G.V}, and
		w(s, v) = 0 for all v 
	// G' 계산하기 O(V + E)
	if BELLMAN_FORD(G`, w, s) == FALSE  // 음수 사이클이 있으면
		print "the input grapg contains a negative-weight cycle"
	else
		for each node v 
			set h(v) by BELLMAN_FORD()
			// BELLMAN_FORD 구하기 O(VE)
		for each edge (u, v)
			w^(u, v) = w(u, v) + h(u) - h(v)
			// w^ 구하기 O(E)
		let D = d[u][v] new n * n matrix
		// matrix 만들기 O(V^2)
		for each node u
			DIJKSTRA(G, w^, u)
			// DIJKSTRA V 번 실행 O(V^2 lg V + VE)
			for each node v
				d[u][v] = δ^(u, v) + h(v) - h(u)
			// D matrix 계산하기 O(V^2)
		return D
```

### 성능 분석
- $O(V^2\lg V + VE)$
