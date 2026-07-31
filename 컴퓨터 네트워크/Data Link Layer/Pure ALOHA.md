---
aliases:
  - 순수 알로하
  - Pure ALOHA(순수 알로하)
---

- 시간 분할 X [[ALOHA]] -> 보낼 frame 생기면 즉시 전송

### 절차
1. Sender 가 보낼 frame 있으면 즉시 전송
2. Receiver 가 frame 수신 -> [[ACK]] 전송
3. timeout period 동안 [[ACK]] 미수신 -> sender 재전송
	- random delay 만큼 대기 -> [[Binary Exponential Backoff]]

### Collision
![[Medium-Access-Control-18.png]]
- 2명 이상의 sender 가 동시 전송 -> receiver 아무것도 수신 X
- frame 전송 多 -> 성공률 ↑
- frame 전송 少 -> 성공률 ↓

### Vulnerable Time
- $2 \times T_{\text{fr}}$ -> 그 frame + 그 이전 frame -> [[Vulnerable Time]]

### Throughput
- $S = G \times e^{-2G}$
- ==ex)== G = 1 -> S = 0.135 -> 1 time slot 마다 평균 0.135 frame 전송
- ==ex)==
	![[Medium-Access-Control-17.png]]
	- $T_{\text{fr}}$ = $\frac{200\ \text{bits}}{200\times 10^3\ \text{bps}}$ = 1ms
	- 1초에 500 frame 생성 -> G = 0.5
	- S = G × $e^{-2G}$ = 0.184
	- 500 × 0.184 = ==92 frame== 만 성공적 전송
