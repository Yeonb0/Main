---
domain: graph
formulation: optimization
techniques: Greedy
aliases:
  - MST
  - 최소 신장 트리
---
### 문제 정의
- MST : 모든 node 를 연결한 [[트리]]를 구성할 때, edge 의 가중치 합이 최소이도록 연결

### 특징
- |E| = |V| - 1
- cycle 존재 X
- unique X
- [[Greedy Algorithm|Greedy]] 방법 사용
	- [[Exchange Argument]] 사용해 ==safe edge== 증명

### Safe edge
- MST를 만드는 edge 집합 A 에 추가해도 여전히 MST 의 subset 으로 유지되는 edge
- 두 집합 (S, V-S) 를 연결하는 edge 중 최소 weight 가지는 light edge 선택하기
> [!note] Theorem
> A 가 어떤 MST 의 subset 이고, (S, V-S) 가 A 를 respect 할 때,
> S 와 V-S 사이의 $E$ (cross edge) 중 ==light edge== 는 A 에 대해 ==safe edge== 이다.
	
> [!note]- Proof - [[Exchange Argument]]
> - 가정
> 	- (S, V-S) 가 A 를 respect
> 	- A : MST 의 subset
> 	- T : A 를 포함하는 edge set
> 	- (u, v) : (S, V-S) 의 cross edge 중 ==light edge==
> - Case 1) (u, v) 가 이미 T 안에 있음 -> 증명 끝
> - Case 2) (u, v) 가 T 안에 없음
> 	- 또 다른 cross edge (x, y) 가정
> 	- (x, y) 가 T에 포함되어서 MST 를 유지하려면 w(x, y) = w(u, v) 여야 함
> 	- 따라서 (u, v) 는 safe edge



### Pseudocode 

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

### [[Loop Invariant]]
- MST 를 만드는 edge set A 는 어떤 MST 의 subset 이다
1. Initialization : $\varnothing$ 은 모든 set 의 subset
2. Maintenance : 추가되는 edge 가 ==safe edge== 이므로 여전히 MST 의 subset
3. Termination : Maintenance 과정에서 MST 유지, Loop 끝날 때 모든 node 가 연결되었으므로 MST

### 알고리즘
- [[Kruskal's Algorithm]]
- [[Prim's Algorithm]]
