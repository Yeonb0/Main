---
aliases:
  - BGP 정책
  - BGP Policy(BGP 정책)
---

- [[BGP]] 에서 shortest 한 게 best route X -> policy 에 따라 path 결정
- 우선순위 : customer > peer > provider

### transit traffic
- 내 customer 에게 가지 않는 traffic

![[Routing-05.png]]

- 100, 200 : Tier 1
- 10, 11, 12, 13 : Tier 2
- 1, 2, 3, 4 : Tier 3
- 한 번 내려가기 시작하면 다시 올라가기 X

### 경로 전송
| 대상 | 전송 범위 |
| --- | --- |
| to Customer | 모든 link 전송 |
| to Peer | Customer link 만 전송 |
| to Provider | Customer link 만 전송 |
