---
aliases:
  - 트레이스루트
  - traceroute(트레이스루트)
---

- source 와 destination 사이의 [[Router|router]] 들 추적하는 [[IP]]-level debugging tool

### 동작
- [[TTL]] 을 `1` -> `2` -> `3` 으로 키워가며 목적지로 전송
	- hop 마다 [[ICMP]] time exceeded 수신 -> 경로 파악
- 마지막 hop -> port 몰라서 drop
	- destination unreachable 수신

### 구현
| [[운영체제\|OS]] | 사용 protocol |
| --- | --- |
| Linux / MAC | UDP 전송 |
| Windows | [[ICMP]] Echo request |

![[Other-Network-Layer-Related-Protocols-11.png]]

![[Other-Network-Layer-Related-Protocols-12.png]]

### 특징
- 요청 시간 만료 -> ICMP reply 막은 사이트 (drop 은 X)
