---
aliases:
  - IP
  - Internet Protocol (IP)
  - 인터넷 프로토콜
  - Internet Protocol
---

- 여러 [[Router]] 거쳐 목적지까지 [[데이터]] 전달하는 layer 3 프로토콜
- Multi hop 전달 가능하게 함 -> 다음 번 목적지로 보내는 역할
- Protocol : 규약 · 절차 · [[메세지]] 규정

### 계층 구분
- layer 1 & 2 : 직접 연결된 상대와 통신 (유선 / 무선)
	- ==ex)== 802.11 (Wi-Fi) / [[Ethernet]] (유선) / PPP
	- 통신 위해선 양쪽 모두에 동일 protocol 필요
- layer 3 : 여러 개 거쳐야 하는 목적지까지 데이터 전송
	- IP 담당

![[Internet-Protocol-(IP)-01.png]]

### 구성 요소
| 요소 | 역할 |
| --- | --- |
| H (Host) | 데이터 송신 / 수신 주체 |
| R ([[Router]]) | 직접적 기능 X, [[Packet]] 전달 역할만 |

### 특징
- 전세계 만국 공통 layer 3 프로토콜 -> [[Hourglass Model]] 의 허리
- 상위 layer 4 에 [[IP Service Model]] 제공
- 주소 체계 -> [[IP 주소]] (논리적 주소, IPv4 32 bit)
