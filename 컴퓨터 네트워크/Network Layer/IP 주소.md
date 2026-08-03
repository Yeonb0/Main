---
aliases:
  - IP 주소
  - IP 주소(IP Address)
  - IP Address
---

- [[컴퓨터 네트워크|네트워크]] 상 모든 기계에 존재하는 주소
- 기본적으로 unique 필요

### 종류
- [[IPv4]] : 4 byte 기본형
	- [[IPv4 Class]] 로 분류
	- [[Subnetting]] 으로 network / host 구분

### 특수 IP 주소
| 주소 | 용도 |
| --- | --- |
| `127.0.0.1` | 자기 자신 |
| `169.254.0.0/16` | 자동 [[IP]] 받기 실패 시 |
| `255.255.255.255` | [[브로드캐스트\|Broadcast]] (모두에게 전송) |

### Private IP address
![[Internet-Addressing-10.png]]
- class A, B, C 일정 구역
- public 아니라 local 에서 사용

### 할당과 변환
- [[DHCP]] : 접속한 기기에 IP 주소 자동 대여
- [[NAT]] : private IP ↔ public IP 변환 -> 주소 부족 완화
- [[ARP]] : IP 주소 -> [[MAC Address|MAC 주소]] 해석
