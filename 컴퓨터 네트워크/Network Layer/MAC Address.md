---
aliases:
  - MAC 주소
  - 물리적 주소
  - MAC 주소(MAC Address)
---

- 기기에 할당된 물리적 주소
- 48 bit 주소

### 특징
- 한 기기에 여러 개 보유 O -> 5G · [[IEEE 802.11|Wi-Fi]] MAC 주소 상이
- 기기 이동해도 고정
- cf) [[IP 주소]] : 논리적 주소, 기기 이동할 때마다 변경
	- [[IPv4]] 32 bit

### 주소 해석
- [[IP 주소]] 만 아는 [[state|상태]] -> [[ARP]] 로 해당 MAC 주소 질의
- ARP 인증 부재 -> [[ARP Spoofing]] 위험
