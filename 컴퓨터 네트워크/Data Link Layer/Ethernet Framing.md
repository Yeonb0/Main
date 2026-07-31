---
aliases:
  - 이더넷 프레이밍
  - Ethernet Framing(이더넷 프레이밍)
---

- [[Ethernet]] 의 frame 경계 구분 방식 -> 별도 flag delimiter X

### 구조
- Frame 시작 : Preamble + SFD
	- Preamble (7 byte) : 10101010
	- SFD (1 byte) : 10101011 -> 이제부터 frame 시작
- Frame 끝 : 별도 flag / delimeter X -> 물리 계층에서 판단
	- IFG (Inter-Frame Gap) : frame 과 frame 사이 ==12 byte== idle 시간

### Flag 방식과 비교
| 항목 | Flag 방식 ([[HDLC]] / [[PPP]]) | [[Ethernet]] |
| --- | --- | --- |
| 프레임 시작 | Flag (01111110) | Preamble (10101010) + SFD (10101011) |
| 프레임 끝 | Flag (01111110) | IFG (idle 감지) |
| Stuffing 필요 | Yes ([[Bit Stuffing\|bit]] / [[Byte Stuffing\|byte stuffing]]) | No |
| 길이 정보 | 불필요 (flag 로 구분) | 불필요 (IFG 로 감지) |
| Example | HDLC, PPP | Ethernet, Wi-Fi |
