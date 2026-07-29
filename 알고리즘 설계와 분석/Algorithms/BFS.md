---
domain: graph
formulation: search
techniques: BFS
aliases:
  - 너비 우선 탐색
  - Breadth First Search
---
### 문제 정의
- Input : $G = (V,E)$, 시작 node `s`
- Output
	- `v.d` : `s` 부터 node `v`까지의 최소 거리
	- `v.π` : predecessor (직전 node)

### Pseudocode
- FIFO [[queue|Queue]] 사용
- 무방향 그래프에서 사용

```cpp
BFS(graph[][] G, start s) {
	for each node u // s 제외
		u.color = WHITE // Initial color
		u.d = ∞
		u.π = NIL
	s.color = GRAY // 현재 search 중인 색
	s.d = 0
	s.π = NIL
	Q = [];
	ENQUEUE(Q, s)
	while Q != []
		u = DEQUEUE(Q)
		for each vertex v in G.Adj[u]
			if v.color == WHIHE // 탐색 X?
				v.color = GRAY
				v.d = u.d + 1 // 거리 설정
				v.π = u       // predecessor 설정
				ENQUEUE(Q, v)
			u.color = BLACK // u 까지는 탐색 완료
```

### 성능
- $O(V + E)$
	- 상한