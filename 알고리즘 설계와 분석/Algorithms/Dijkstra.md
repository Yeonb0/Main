---
aliases:
  - 다익스트라
techniques:
  - Greedy
  - Priority Queue
formulation:
  - optimization
domain:
  - graph
---

- 음수 weight edge 허용 X
- [[BFS]] 의 weighted version
	- [[queue]] 대신 [[Priority Queue]] 사용 -> 항상 가장 작은 값 뽑음
- [[Prim's Algorithm]]과 유사하게 동작
	- S = 선택된 [[node]] 집합
	- V-S = priority queue Q 안의 집합

### Pseudocode
```cpp
DIJKSTRA(graph[][] G, weight w, start s)
	INITIALIZE_SINGLE_SOURCE(G, s)
		S = ∅
		Q = ∅
	for each node u
		INSERT(Q, u)  // 모든 node 를 queue 에 넣기, key 는 u.d
	while Q != ∅
		u = EXTRACT_MIN(Q) // 가장 short 한 node 뽑아서
		S = S ∪ {u}        // V-S -> S 로 이동
		for each node v in G.Adj[u] // 뽑은 u 와 연결된 node 들
			RELAX(u, v, w)            // RELAX 하기
			if the call of RELAX() decreased v.d // relax 이후 d 가 감소했으면
				DECREASE_KET(Q, v, v.d) // queue 에서 key 업데이트
```

### 성능
- $O(V\lg V + E)$ -> Fibonacci heap
- $O(E\lg V)$ -> Binary heap

### [[Greedy Algorithm#^4cf760|Greedy Choice Property]]
- S = 최종 shortest-path weight 확정 node 집합

1. u 이전에 뽑힌 node 는 이미 relax 완료
2. 남은 가능성은 Q 에 남은 node 를 거치는 경로
3. 그런데 u 가 Q 에서 가장 작은 estimate 를 거침
4. 따라서 `u.d` 가 가장 작은 값이므로 확정

### 활용
- [[Link-State Routing]] : flooding 으로 모은 graph 에서 최단 경로 계산
	- 구현 protocol -> [[OSPF]]
