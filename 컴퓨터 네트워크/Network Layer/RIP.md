---
aliases:
  - Routing Information Protocol
  - RIP(Routing Information Protocol)
---

- [[Distance Vector Routing]] 구현 protocol
- [[Router|Routing]] Information Protocol

### 전송
- ==30초== 주기 전송 + table update 시 전송

### message format
![[Routing-21.png]]
- 목적지 주소 (address + mask) + distance
