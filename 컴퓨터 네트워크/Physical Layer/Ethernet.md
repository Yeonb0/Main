---
aliases:
  - 이더넷
  - 이더넷(Ethernet)
  - Ethernet(이더넷)
---

- 유선 인터넷 표준 -> [[IEEE 802.3]]
	- cf) IEEE 802.11 -> [[IEEE 802.11|Wi-Fi]] 표준
- 네트워크 커버 영역
	- [[LAN]] (local, 강의실 정도)
	- [[MAN]] (metropolitan, 마포구 정도)
	- [[WAN]] (wide, 우리나라 정도)

### Ethernet Cable
- 여러 다양한 종류의 전선 존재
- Cat 높을수록 max transmission speed ↑

### 종류
| 표준 | 내용 |
| --- | --- |
| 10BASE5 | 10Mbps, baseband transmission, max 500m, RG-8 thick cable |
| 10BASE2 | 10Mbps, baseband transmission, max 200m, RG-8 thin cable |
| 10BASE-T | 10Mbps, baseband transmission, twisted pair, max 약 100m |
| 100BASE-TX | 100Mbps, 2 twisted pair -> Fast Ethernet |
| 1000BASE-T | 1Gbps, 4 twisted pair, 5 level coding |
| 10GBASE-T | 10Gbps |

### Coding Scheme
| 표준 | 방식 |
| --- | --- |
| 10BASE-5 / 10BASE-2 / 10BASE-T | [[Manchester Encoding]] |
| 100BASE-TX | [[MLT-3]] + [[4B5B]] |
| 1000BASE-T | 8B1Q4 & 4D-PAN5 |
| 10GBASE-T | PAM-16 + DSQ128 + LDPC |

### Medium Access
- [[CSMA-CD|CSMA/CD]] 로 매체 접근 제어
- 최소 frame 크기 512 bit (64 byte) -> collision detect 보장
- time slot 512 bit times -> [[Binary Exponential Backoff]] 단위

### 프레임 전송
- [[LAN]] 에서 이용되는 [[데이터]] 링크 · 물리 계층 [[프로토콜]] -> [[TCP IP|TCP/IP]] 데이터 링크 계층 담당
- 수신한 [[Packet|패킷]] 에 MAC 헤더 부착 -> 데이터 보낼 상대방 지정
- 이더넷 프레임 내 데이터 -> 물리적 연결 통해 전기 [[신호]] 로 송출
