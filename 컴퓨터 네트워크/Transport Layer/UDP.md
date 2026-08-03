---
aliases:
  - User Datagram Protocol
  - UDP(User Datagram Protocol)
---

- 매우 간단한 layer 4 protocol
- connection-less : 연결 설정 X
- unreliable : [[Error|error]], 순서 신경 X

### 기능
- [[Port|port]] 번호 받아 process 에 전달
- [[Checksum]] 으로 [[Error Detection]]

### 특징
- datagram : [[Packet]] 의 다른 [[이름]]
- [[Sequence Number]] X -> 순서 보장 X, 중복 detection X
- 장점 : 쉬움, 가벼움, 빠름

### Header
![[Transport-Layer-07.png]]
- Port number (Source / Destination) : 각 16 bit
- Total length : UDP header + data 길이
- Checksum : header 의 checksum

### 사용처
- 비중 : [[TCP]] ==65 ~ 70%== / UDP ==35 ~ 30%==
- 멀티미디어 스트리밍 서비스
	- ==ex)== 유튜브
- [[QUIC]] (layer 4) : HTTP/3 신규 protocol -> TCP 유사 + 더 가벼움, UDP 위에서 동작
- Multicast application : 여러 사람에게 동시 전송
- DNS, SNMP
