---
aliases:
  - 슬라이딩 윈도우
  - Sliding Window(슬라이딩 윈도우)
---

- frame 마다 [[Sequence Number]] 붙여 buffer 에 저장 -> 전송 가능 구간을 window 로 관리

![[Framing-Error-Control-13.png]]

### Send Window
- Window Size : ==15==
	- Window 왼쪽 : 전송 완료 & ACK 완료
	- 주황색 : 전송 완료 & ACK X -> outstanding frame
	- 흰색 : 전송 가능 & [[데이터]] 준비 X
	- Window 오른쪽 : 전송 불가능
- Sequence number : 4 bit -> 0 ~ 15 반복
	- $S_f$ : 첫 outstanding frame
	- $S_n$ : 다음 보낼 frame
	- $S_{size}$ : send window size
- Send Window 크기만큼 일단 frame 전송
	- [[ACK]] 돌려 받으면 그만큼 window 오른쪽으로 이동 (size 는 그대로)

### Receive Window
![[Framing-Error-Control-14.png]]
- [[Go-Back-N]] -> 1 칸
	- 다음 도착할 frame 대기
	- 기다리던 frame 아니면 discard
- [[Selective Repeat]] -> Send window size = Receive window size
- cf) [[Stop-and-Wait]] 는 Send 1 칸, Receive 1 칸

### cf) [[TCP Sliding Window]]
- layer 2 : 조건 따라 window size 고정
- [[TCP]] : rwnd & cwnd 따라 size 가변, frame 아닌 byte 단위 관리
