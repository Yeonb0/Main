---
aliases:
  - 라우팅 알고리즘
  - Routing Algorithm(라우팅 알고리즘)
---

- routing table 을 구성하는 규칙
- 기본은 shortest path 기준 (거리 · cost)
- packet 마다 정책 상이 (fast · throughput) -> [[Router]] 다양성 필요

### 종류
- intradomain : 같은 관리 주체 내부 routing
	- Distance vector -> [[RIP]]
	- Link [[state]] -> [[OSPF]]
- interdomain : 다른 관리 구역 넘어가는 routing, 정책 영향 O
	- Path vector -> [[BGP]]
- 관리 주체 단위 -> [[Autonomous System]]

### Control Plane 구성
- Per-Router Control Plane : router 끼리 자체적으로 table 구성
![[Routing-08.png]]
- Logically Centralized Control Plane : Remote Controller 로 table 중앙 관리
![[Routing-09.png]]

### 메시지 전달 방식
1. periodic messaging : 주기적 전달
2. trigger based messaging : table update 시 전달
- 일반적으로 두 방식 병용
	- timer 만료까지 정보 미수신 -> 문제 감지

### 비교
| 항목 | [[Distance Vector Routing]] ([[RIP]]) | [[Link-State Routing]] ([[OSPF]]) |
| --- | --- | --- |
| 교환 정보 | 목적지, 목적지까지의 거리 | 이웃 ID, 이웃까지의 거리 |
| 전송 대상 | 직접 연결된 이웃만 | [[컴퓨터 네트워크\|네트워크]]의 모든 [[뉴런\|노드]] (flooding) |
| [[알고리즘]] | [[Bellman-Ford]] (분산형) | [[Dijkstra]] |
| 장점 | 단순, 낮은 오버헤드 | 빠른 수렴, 루프 없음 |
| 단점 | 느린 수렴, [[Count-to-Infinity Problem\|count-to-infinity]] | 높은 메시지 · CPU 오버헤드 |
