---
aliases:
  - 선입선출 큐
  - FIFO Queue(선입선출 큐)
---

- First-In First-Out -> 한 줄로 쌓고 앞에서부터 전송
- 가장 단순한 [[Scheduling]] 방식

![[Scheduling-and-Traffic-Shaping-01.png]]

### 특징
- flow (src -> dst 흐름) 파악 X
- [[Congestion Control|congestion control(혼잡 제어)]] X
- [[Queue]] full -> 새로 도착한 [[Packet]] drop (==tail drop==)
- 공평 -> 우열 X
- [[Bandwidth]] 고려 X

### 단점
- 보내는 만큼 받음
	- ==selfish== 할수록 이득
	- attack 으로 악용 O
- 더 · 덜 중요한 것 판단 X
- tail drop -> 꽉 차는 순간 우르르 drop -> 대안 [[Active Queue Management]]
