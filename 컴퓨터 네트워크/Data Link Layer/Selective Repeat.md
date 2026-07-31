---
aliases:
  - 선택적 재전송
  - Selective Repeat(선택적 재전송)
---

- [[Go-Back-N]] 문제 해결 -> receive window size 도 N
- Send window size = Receive window size
- 손실된 frame 만 선별 재전송
- Send window 는 [[Sliding Window]] 와 동일

### Receive Window
![[Framing-Error-Control-19.png]]
- window 안에 있는 frame -> 전송 받아야 하는 frame
- window 를 움직이는 상황 -> [[ACK]] 전송

### Sequence Number
- [[Sequence Number]] 가 m bit -> window 는 $2^{m-1}$ 보다 작거나 같음
- ==ex)== sequence number 가 [0, 15] (m = 4)
	- window size : send 8 개 ($2^3$) / receive 8 개 ($2^3$)

### Timer
- outstanding frame 각각 timer 필요
- timer 1 개만 사용 -> $S_f$ 에 위치
	- ![[Framing-Error-Control-21.png]]
	- frame 4 에 timer 없어서 loss 된 거 모름
