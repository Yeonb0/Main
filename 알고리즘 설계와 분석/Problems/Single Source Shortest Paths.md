---
domain:
  - graph
formulation:
  - optimization
---
### 문제 정의
- 출발할 한 node `s` 로부터 다른 모든 node 까지의 최소 거리 구하기
- Input : Directed Graph $G = (V, E)$, Weight Function $w$
- Output
	- `v.d` = $\delta(s, v)$
	- `v.π` = predecessor

### Optimal Substructure
> [!note] Lemma
> 어떤 shortest path 의 부분 path 도 shortest path 이다.

### Pseudocode
- Initialize : 모든 node 초기화
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

- Relaxing -> 거리 설정
```cpp
RELAX(node u, node v, weight w) 
	if v.d > u.d + w(u, v) // 현재 추정치가 더 크면
		v.d = u.d + w(u, v)  // 더 작은 값으로 교체
		v.π = u
```

### Properties
- Triangle inequality : 모든 edge (u, v) 에 대해  
    $\delta(s, v) ≤ \delta(s, u) + w(u, v)$
    - s → u → v 는 s → v edge ≤ s → … → u edge + u → v edge
- Upper-bound property : $v.d ≥ \delta(s,v)$
    - 최소 거리 도달 시 안 바뀜
- No-path property : 최소가 ∞ 이면 가는 경로 없음
- Convergence property : s → … → u → v 일 때  
    s → … → u 까지 이미 relaxed 면 u → v 만 relax 해도 최단 경로
- Path-relaxation property : $s = v_0 → v_1 → … → v_k$ 가 최단 경로 p 를 형성 했다면,  
    중간 중간 모든 path 가 최소 거리. (어떤 순서든, 다른 relax 가 섞이든)

### 알고리즘
- [[Bellman-Ford]]
- [[Dijkstra]]
