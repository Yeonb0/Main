---
aliases:
  - TCP 슬라이딩 윈도우
  - TCP Sliding Window(TCP 슬라이딩 윈도우)
---

- [[TCP]] 의 [[Sliding Window]] -> byte 단위 관리
- layer 2 : 조건 따라 window size 고정 / TCP : 상황 따라 size 변경

### Send Window
![[Transport-Layer-17.png]]
- window 안 data 전송 -> `ACK` 받은 만큼 slide

| [[Pointer\|포인터]] | 의미 |
| --- | --- |
| LastByteAcked | 가장 최근 [[ACK]] 받은 byte (window 왼쪽) |
| LastByteSent | 가장 최근 보낸 byte (window 안쪽, ACK X) |
| LastByteWritten | 가장 최근 준비된 byte (window 오른쪽, Application) |

- LastByteAcked ≤ LastByteSent ≤ LastByteWritten

### Receive Window
![[Transport-Layer-18.png]]

| 포인터 | 의미 |
| --- | --- |
| LastByteRead | 가장 최근 ACK 보낸 byte |
| NextByteExpected | 다음 받아야 할 byte (그 전까진 모두 수신 가정) |
| LastByteRcvd | 가장 최근 받은 byte (중간 구멍 포함) |

- LastByteRead ≤ NextByteExpected ≤ LastByteRcvd

### Window Size
- Window size = min (rwnd, cwnd)
	- rwnd (receiver window) : receiver 가 advertise -> buffer 남은 공간, [[Flow Control]]
	- cwnd (congestion window) : 중간 [[Router|router]] 등 network [[state|상태]], [[Congestion Control]]
- size ↑ -> 속도 ↑, drop ↑ -> bandwidth 낭비
- size ↓ -> 속도 ↓, bandwidth 낭비
- -> 적당한 size [[Searching|탐색]] 필요
