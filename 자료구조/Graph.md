---
aliases:
  - 그래프
  - 그래프(Graph)
---
### 정의
- 그래프 G 는 V, E 의 두 가지 set 을 포함
	- $G = (V,E)$ 
- V : vertex, node (정점) 의 set
	- $V(G)$
- E : edge (간선) 의 set
	- $E(G)$

### 종류
![[image (5).png]]
- 무방향 그래프 (undirected graph) 
	- 최대 간선 수 : $\frac{n(n-1)}{2}$
- 유방향 그래프 (directed graph)
	- 최대 간선 수 : $n(n-1)$

### 용어
- incident : edge & node 가 연결됨
- adjacent : node & node 가 한 edge 를 사이에 둠
- subgraph : 부분 그래프. 원래 그래프의 일부 node & edge 로 구성된 그래프
- path : 경로. 시작 node -> 종료 node 까지의 경로
	- length : 중간에 지나가는 edge 수
	- simple path : 시작 & 끝을 제외하고 나머지 node 들을 한 번만 지나가는 경로
- cycle : 시작 = 끝 node 인 simple path
- connected graph : 모든 node 가 연결된 그래프
- unconnected graph : 하나라도 연결되지 않은 node 가 있는 그래프
- tree : connected + acyclic graph

### 표현 방법
#### Adjacency List
- [[Linked List]] 로 표현
- Space : $\Theta(V + E)$

#### Adjacency Matrix
- 2D [[Array]] 로 표현
- Space : $\Theta(V^2)$
