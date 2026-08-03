---
aliases:
  - 벨만 포드
techniques:
  - DP
formulation:
  - optimization
domain:
  - graph
---

- 음수 weight edge 허용

### Pseudocode
```cpp
BELLMAN_FORD(graph[][] G, weight w, start s)
	INITIALIZE_SINGLE_SOURCE(G, s)
		for i = 1 ~ G.V - 1     // V 개 node 잇는 최대 edge 수 횟수 (V-1)
			for each edge (u, v)  // 모든 edge 에 대해
				RELAX(u, v, w)      // RELAX 함수 실행 -> 완료 시 전체 node relaxed
				
		// Negative cycle check
		for each edge (u, v)
			if v.d > u.d + w(u, v) // 모두 relaxed 했는데 값이 작아지면
				return false         // negative cycle 있음!
		return true              // 모두 그대로면 없음
```

### 성능
- $O(V^2 + VE)$

### 활용
- [[Distance Vector Routing]] : 각 [[Router]] 가 이웃과 table 교환하며 분산 실행
	- 중앙 graph 없이 (destination, distance, next [[node]]) 만으로 relax
