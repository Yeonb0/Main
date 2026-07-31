---
aliases:
  - CSMA/CD
  - Collision Detection
  - CSMA/CD(Collision Detection)
---

- 전송 중 [[Collision|충돌]] 감지 -> 전송 중단하는 [[CSMA]] 확장
- [[Ethernet]] 유선 환경에서 주로 사용

### 충돌 판단
![[Medium-Access-Control-23.png]]
- frame 크기를 키움
- 내 frame 전송 중 다른 frame 수신 -> collision 판단

### Frame 최소 크기
- 가장 먼 station 이 receive 하기 직전에 send 한 frame 이 도착할 때까지 전송 중이어야 detect O
- $T ≥ 2 \times T_p$
	- [[Ethernet]] 에 maximum 거리 존재
	- frame size variable 하나 최솟값 존재
- ==ex)==
	![[Medium-Access-Control-24.png]]
	- $T_{fr}$ ≥ 왕복 시간 = 51.2 $\mu$s
	- $T_{fr} = \frac{\text{Frame Size}}{\text{Link Bandwidth}}$
	- Frame Size ≥ ==512 bit, 64 byte==

### 충돌 감지 시
1. Jamming signal 전송 -> collision 발생 알림 & transmission 중단
	- jamming signal : 48 bit 짜리 garbage data
2. [[Binary Exponential Backoff]] -> random 시간 대기
3. 재전송 시작
