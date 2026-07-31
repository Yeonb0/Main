---
aliases:
  - 이더넷
  - 이더넷(Ethernet)
---

- 유선 인터넷 표준 -> [[IEEE 802.3]]
	- cf) IEEE 802.11 -> Wi-Fi 표준
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
