---
aliases:
  - 지연
  - Delay(지연)
  - Latency
---

- 메시지의 첫 번째 bit 출발 ~ 마지막 bit 도착까지의 시간
- Delay = transmission delay + propagation delay + queuing delay + processing delay

### 종류
- Transmission delay (전송 속도) : bit 를 channel 로 내보내는 시간
	- $\frac{\text{message size}}{\text{bandwidth}}$
	- 회선의 [[Bandwidth]] 비례
- propagation delay (전파 속도) : 송신 -> 수신 도달까지 걸리는 시간
	- $\frac{\text{distance}}{\text{propagation speed}}$
	- 송-수신자 거리에 비례

![[Data-and-Signals-22.png]]

- Queuing delay : [[queue]] 에서 줄 서는 시간
- Processing delay : 시스템이 process 하는 데 걸리는 시간

### 특징
- bandwidth 와 곱 -> [[Bandwidth-Delay Product]]
