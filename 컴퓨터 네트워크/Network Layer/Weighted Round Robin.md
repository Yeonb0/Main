---
aliases:
  - 가중 라운드 로빈
  - Weighted Round Robin(가중 라운드 로빈)
---

- [[Round Robin]] + priority 도입
- 각 [[Queue]] 마다 weight 설정
	- 차례마다 전송 [[Packet]] 개수 상이
	- ==ex)== weight 3 -> 3개 / weight 1 -> 1개 전송
