---
aliases:
  - Address Resolution Protocol
  - ARP(Address Resolution Protocol)
  - 주소 결정 프로토콜
---

- [[IP 주소]] 로 [[MAC Address|MAC 주소]] 알아내는 protocol
- logical address([[IP 주소]], 연결마다 변경) -> physical address([[MAC Address|MAC 주소]], 기기 고정) 해석

### 계층
- layer 2 / layer 3 경계 -> 소속 논란 有

### 절차
- 모르면 broadcast
1. Request : `141.23.56.23` 있나요?
2. Reply
	- 해당 IP 아님 -> 응답 X
	- 해당 IP 맞음 -> 자신의 MAC 주소 회신
		- ==ex)== `142.23.56.23` : MAC 주소 `A4:6E:F4:59:83:AB`

![[Other-Network-Layer-Related-Protocols-01.png]]

### 형태
![[Other-Network-Layer-Related-Protocols-02.png]]

| [[필드]] | 내용 |
| --- | --- |
| Hardware type | layer 2 의 type ([[Ethernet\|ethernet]]) |
| Protocol type | layer 3 의 type ([[IP]]) |
| [[연산\|Operation]] | `1` request / `2` reply |
| hardware address | 6 byte |
| 나머지 필드 | 4 byte |

![[Other-Network-Layer-Related-Protocols-03.png]]
- Request 시 target MAC 주소 공란
- Request ↔ Reply 시 Sender 와 Target 교환

### 한계
- 인증 부재 -> [[ARP Spoofing]] 취약
