---
aliases:
  - Maximum Transfer Unit
  - 최대 전송 단위
  - MTU(Maximum Transfer Unit)
---

- 한 번에 보낼 수 있는 최대 packet size
- protocol 마다 값 상이

![[Internet-Protocol-(IP)-15.png]]

![[Internet-Protocol-(IP)-16.png]]

### 특징
- payload 에 들어갈 수 있는 최대량
	- 상위 layer 가 맞춰서 전송
	- 초과 전송 시 -> [[Fragmentation]]
- 요즘 가장 많이 쓰는 [[Ethernet]] 기준 -> [[Path MTU Discovery]] 로 미리 파악
- layer 4 기준 -> [[MSS]] = MTU - [[IP]] header (20) - TCP header (20 + α)
