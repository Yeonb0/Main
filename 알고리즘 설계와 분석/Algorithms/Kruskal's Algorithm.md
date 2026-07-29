---
domain: graph
formulation: optimization
techniques:
  - Greedy
  - Union-Find
---
- [[Union-Find]] 사용

### Pseudocode
```cpp
MST_KRUSKAL(graph[][] g, weight w)
	A = ∅
	for each node v
		MAKE_SET(v) // 모든 node 를 set 으로 만들기
	create a single list of the edges in G.E // edge 들로 list 만들기
	sort the list of edges increasing order by weight w // 오름차순 정렬하기
	for each edge (u, v) in sorted list
		if FIND_SET(u) != FIND_SET(v) // S, V-S 에 따로 위치하면
			A = A ∪ {(u, v)} // A 에 추가하고
			UNION(u, v) // 한 set 으로 만들기
 return A
```

### 성능 분석
- $O(E \lg V)$
	- edge 가 sorted 되어있으면 $O(E \cdot \alpha(V))$ -> 거의 선형