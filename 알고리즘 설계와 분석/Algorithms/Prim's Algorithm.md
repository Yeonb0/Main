---
domain: graph
techniques:
  - Greedy
  - Priority Queue
formulation: optimization
---
- Minimum [[Priority Queue]] 사용

### Pseudocode
```cpp
MST_PRIM(graph[][] G, weight w, r)
	for each node u // 모든 node 초기화
		u.key = ∞
		u.π = NIL
	r.key = 0 // root node 는 weight 0
	Q = ∅     
	for each node u // 모든 node 를 Q 에 넣기
		INSERT(Q, u)
	while Q != ∅    // Q 가 빌 때까지
		u = EXTRACT_MIN(Q)  // 제일 작은 값을 빼서 A 에 넣기
		for each vertex v in G.Adj[u]   // u 와 연결된 node 추가 
			if v in Q && w(u, v) < v.key  // A 에 없고, 초기화 안됐으면
			v.π = u
			v.key = w(u, v)
			DECREASE_KEY(Q, v, w(u,v)) // priority queue 에서 값 update
```

### 성능
- $O(V \lg V + E)$ -> Fibonacci Heap
- $O(E\lg V)$ -> Binary Heap