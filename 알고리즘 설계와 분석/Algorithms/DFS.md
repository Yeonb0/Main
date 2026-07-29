---
domain: graph
formulation: search
techniques: DFS
aliases:
  - 깊이 우선 탐색
  - Depth First Search
---
### 문제 정의
- Input : $G = (V,E)$
- Output
	- `v.d` : discovery 시작 시간
	- `v.f` : discovery 종료 시간
	- `v.π` : predecessor (직전 node)

### Pseudocode
```cpp
DFS(graph[][] G)
	for each vertex u
		u.color = WHITE
		u.π = NIL
	time = 0
	for each vertex u
		if u.color == WHITE  // 아직 탐색 안했다면
			DFS_VISIT(G, u)    // 탐색 시작
```

```cpp
DFS_VISIT(graph[][], node u)
	time = time + 1
	u.d = time      // 탐색 시작 시간
	u.color = GRAY  // 탐색 시작
	for each vertex v in G.Adj[u] // 연결 node 탐색
		if v.color == WHITE // 아직 탐색 안했으면
			v.π = u           // 이전 node 기록하고
			DFS_VISIT(G, v)   // 재귀 탐색
	time = time + 1
	u.f = time      // 탐색 종료 시간 
	u.color = BLACK // 탐색 끝
```

### 성능
- $\Theta(V + E)$
	- 모든 node & edge 탐색 보장

### Edge 종류
- u 가 `GRAY` 일때
	- v 가 `WHITE` -> Tree edge
	- v 가 `GRAY` -> Back edge (자기 자신 cycle)
	- v 가 `BLACK` & v 가 u 의 자손 -> Forward Edge
	- v 가 `BLACK` & 조상-후손 관계 X -> Cross Edge