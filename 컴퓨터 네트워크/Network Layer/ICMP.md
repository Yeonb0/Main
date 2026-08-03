---
aliases:
  - Internet Control Message Protocol
  - ICMP(Internet Control Message Protocol)
---

- layer 3 의 보조 protocol
- [[데이터]] 전송 X -> [[Error|오류]] 보고 · 질의 전용

### 형태
![[Other-Network-Layer-Related-Protocols-06.png]]

### 종류
#### Error reporting
![[Other-Network-Layer-Related-Protocols-07.png]]

| 종류 | 내용 |
| --- | --- |
| Destination unreachable | 목적지로 가는 길 없음 |
| Source quench | [[Router\|router]] 가 full -> 요즘엔 TCP 가 대체 |
| Time exceeded | [[TTL]] 이 `0` -> [[Packet]] 폐기 |
| [[매개 변수\|Parameter]] problem | [[IP Header\|header]] 에 문제 有 |
| Redirection | 더 나은 gateway 안내 |

- Redirection : 한 망에 gateway 여러 개인 상황

![[Other-Network-Layer-Related-Protocols-08.png]]
- A -> B 전송 상황에서 R1 이 A 의 packet 수신
- R1 이 A 에게 "자신 아닌 R2 경유가 유리" 통보
- 통보와 별개로 B 에게 전송은 수행

#### Query
![[Other-Network-Layer-Related-Protocols-09.png]]

| 종류 | 내용 |
| --- | --- |
| Echo request & reply | [[ping]] 주고받기 |
| Timestamp request & reply | round-trip time 계산용, ping 과 역할 동일 -> 거의 미사용 |
| [[Router]] solicitation & advertisement | 주변 [[Router\|router]] 알아보기 / 알려주기 |

### 생성 규칙
- ICMP packet 의 error 에 대한 error report ICMP packet 생성 X
	- query 에 대해서는 생성 O
- error report 은 [[Fragmentation|fragment]] 된 packet 의 첫 fragment 에만 생성
- multicast packet 에 대해 생성 X
- 특별한 도착지(`127.0.0.1` or `0.0.0.0`) 에 대해 생성 X

### 활용
- [[IP]]-level debugging tool 의 기반
	- [[ping]] : Echo request & reply 사용
	- [[traceroute]] : time exceeded · destination unreachable 수신
