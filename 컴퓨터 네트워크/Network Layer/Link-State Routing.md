---
aliases:
  - 링크 상태 라우팅
  - Link-State Routing(링크 상태 라우팅)
---

- 이웃 정보를 모든 [[node]] 에게 전송 -> 각 node 가 전체 graph 구성
- 나와 연결된 (ID, distance) 를 flooding
- cf) [[Distance Vector Routing]] : 자신의 모든 정보를 이웃에게만 전송
- 최근 널리 사용

### 최단 경로
- [[Dijkstra]] 로 계산
![[Routing-22.png]]
- D - distance / P - parent
- ==ex)== 선택 순서 A -> D (1) -> E (2) -> B (2) -> C (3) -> F (4)
	- 단계마다 최소 거리 node 한 개씩 선택
	- 동일 거리 시 임의 node 선택
- table 생성 후 최소 거리 경로로 전송

### 단점
- network-wide flooding -> overhead ↑
- 오용 시 attack

### 해결법
- [[TTL]] 로 전파 범위 조절
- 자신이 보낸 메시지 재수신 시 [[Sequence Number]] 동일 -> drop

### 구현
- [[OSPF]]
