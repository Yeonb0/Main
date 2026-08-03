---
aliases:
  - Border Gateway Protocol
  - BGP(Border Gateway Protocol)
---

- [[Border Router]] 간의 [[Router|routing]] [[프로토콜]]
- [[Autonomous System|AS]] 간 경로 결정 담당

![[Routing-02.png]]

### 필요성
| 항목 | 내용 |
| --- | --- |
| Scale | [[Autonomous System\|AS]] 안 / 밖이랑 다른 scale |
| Policy | AS 밖이면 cost 도 고려 |
| Trust | AS 밖으로는 내부 정보 유출 X |
| Autonomy | AS 마다 정책 상이 -> 여러 AS 사이의 관리 필요 |

### 종류
- [[eBGP]] : 다른 AS border router 끼리 정보 교환
- [[iBGP]] : 같은 AS 안에서 border router 끼리 정보 교환 (intra-domain)

### 특징
- TCP 위에서 동작 -> Application layer protocol
	- 단, network layer 와 관련
- shortest 한 게 best route X -> [[BGP Policy]] 따라 path 결정
