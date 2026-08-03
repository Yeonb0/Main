---
aliases:
  - 패킷
  - Packet(패킷)
---

- [[컴퓨터 네트워크|네트워크]]에서 주고받는 [[데이터]] 조각의 일반적 명칭

### 종류
| 명칭 | 사용 계층 |
| --- | --- |
| packet | 데이터 조각 (general) |
| frame | layer 1, 2 |
| datagram | layer 3, 4 (UDP) |
| segment | layer 4 (TCP) |

### Frame 구조
| Header | Payload | Trailer |
| --- | --- | --- |
- Header : 목적지 주소 ([[MAC Address]]) 보유
	- layer 2 : 내 주소인지 판단 -> 일단 받고 목적지 주소 다르면 버림
	- layer 3 : AP -> 목적지 주소로 forwarding
- 프레임 경계 구분 -> [[Framing]] / [[Ethernet Framing]]

### Packet format
- layer 내려올수록 header · trailer 앞뒤로 덧붙음

| Header (L2) | Header (L3) | Payload | Trailer (L3) | Trailer (L2) |
| --- | --- | --- | --- | --- |
- layer 3 header -> [[IP Header]]
