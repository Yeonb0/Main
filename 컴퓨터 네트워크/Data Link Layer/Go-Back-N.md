---
aliases:
  - 고 백 N
  - Go-Back-N(고 백 N)
---

- [[ACK]] 오기 전까지 frame 계속 전송
- 문제 발생 -> 그 이후로 보낸 frame 없던 것으로 치고 재전송
- send window N 칸 / receive window ==1 칸== -> [[Sliding Window]] 로 관리

### Design Issue
- ACK 받기 전까지 몇 개의 frame 을 보내야 하는가
- [[Sequence Number]] 몇 bit 써야 하는가
- [[Error]] 발생 시 어떡해야 하는가

### Sequence Number Range
- 범위 [0 ~ N-1] -> 사용 bit 수 $\log_2N$
	- ==ex)== [0 ~ 63] 이면 6 bit 사용
- 원칙 : Send window size 가 N 이면 sequence number 는 N 보다 ==커야== 함 (같음 X)
- 클 경우
	- ![[Framing-Error-Control-15.png]]
	- timeout 후 재전송 -> ACK 재전송 여부 문제
		- next expected frame 이 3 -> ACK(3) 전송
		- 이미 Sender 는 0, 1, 2 전송한 [[state|상태]]
		- 가장 정확한 경우 -> Receiver 가 frame 받을 때마다 매번 ACK 전송
- 같을 경우
	- ![[Framing-Error-Control-16.png]]
	- ACK 전달 X -> 잘못된 accept 발생

### Timer
- 가장 처음으로 보낸 frame ($S_f$) 에만 timer 1 개 사용
- ACK 수신 -> $S_f$ 다음 frame 에 timer set
- [[Timeout]] 발생 -> window 안 frame 모두 재전송 (& timer reset)

### 단점
- timeout 발생 시 window 안 모든 frame 재전송
- receive window size = 1 -> 1 만 lost 고 2~5 제대로 전송돼도 전부 재전송
	- -> [[Selective Repeat]] 로 해결
