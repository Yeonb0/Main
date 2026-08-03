---
aliases:
  - 라우터
  - 라우터(Router)
  - Routing
  - 라우팅
  - Router(라우터)
---

- 받은 [[데이터]]를 routing table 바탕으로 다음 방향으로 전송
![[Internet-Addressing-05.png]]

### Routing table
- (Destination, Next Hop) 저장
	- Destination : [[Subnetting|subnet]] 단위 목적지 주소
	- Next Hop : 다음으로 갈 router

### 방식
- [[Prefix Routing]] : 같은 방향 묶어서 표시
- [[Longest Matching Prefix]] : 목적지 중복 시 선택 규칙
- [[Route Aggregation]] : Next hop 동일한 entry 병합

### AS 간 routing
- [[Autonomous System|AS]] 단위로 분할된 계층적 구조 -> [[Flat vs. Hierarchical Network]]
- [[Border Router]] : AS 끝단에서 목적지 AS 방향 결정
- [[BGP]] : AS 간 경로 교환 프로토콜

### 전송 순서
- routing = 다음 hop 결정 / [[Scheduling]] = 누구 먼저 보낼지 결정
- [[Queue]] 혼잡 시 [[Active Queue Management]] 로 미리 [[Packet]] drop
