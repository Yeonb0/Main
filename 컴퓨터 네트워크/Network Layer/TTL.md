---
aliases:
  - Time to Live
  - TTL(Time to Live)
---

- [[IP Header]] 의 8 bit [[필드]] (0 ~ 255)
- [[Packet]] 이 거칠 수 있는 router 수 제한

### 동작
- router 간 이동마다 -1
- `0` 도달 -> forwarding 중단하고 drop
	- 빙빙 도는 경우 차단 목적

### 특징
- 전세계 어디로 보내도 보통 ==20 hop== 이내

### 활용
- `0` 도달 -> [[ICMP]] time exceeded 회신
- [[traceroute]] : TTL `1` 부터 키워가며 경로 상 [[Router|router]] 추적
