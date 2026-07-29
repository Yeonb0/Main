---
domain:
  - graph
formulation:
  - optimization
techniques:
  - DP
---
### 문제 정의
- 전체 node 에서 전체 node 까지의 최소 weight 구하기
- Input : directed graph $G = (V, E)$, weight function $w$
- Output : n -> n 개의 모든 shortest-path distance

### 알고리즘
- [[Floyd-Warshall]]
- [[Johnson's Algorithm]]
