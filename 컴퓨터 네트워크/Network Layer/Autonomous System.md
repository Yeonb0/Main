---
aliases:
  - AS
  - 자율 시스템
  - Autonomous System(AS)
---

- 같은 router policy 를 가진 network group
- 같은 관리 주체의 [[Router]] 집합 -> ==domain==

### 특징
- ISP · 조직 단위 관리
- 전 세계 ==약 12만 개==, 국내 ==1187개==
- ==ex)== KT, LG U+, 서강대
### 계층
| 계층 | 범위 |
| --- | --- |
| Tier 1 | global |
| Tier 2 | regional |
| Tier 3 | local |

### routing 구분
- intradomain : AS 내부 -> [[RIP]], [[OSPF]]
- interdomain : AS 간, 정책 영향 O -> ==BGP==
- 구분별 방식 -> [[Routing Algorithm]]


### AS 관계
- Provider (망 제공) -> Customer (망 사용)
- Peer : 서로 망 공짜로 사용
	- ==ex)== KT / SKT / LG U+
- Multi-homing : 한 Customer 가 여러 Provider 사용
![[Routing-01.png]]

### 조건
- AS 마다 policy 상이 -> AS 간에는 다른 policy 필요 -> [[BGP]]
