---
aliases:
  - 토큰 버킷
  - Token Bucket(토큰 버킷)
---

- token 소비해 [[Packet]] 전송하는 [[Traffic Shaping]] 기법
- [[Leaky Bucket]] 의 완전 일정 전송 완화

### 특징
- token 일정한 속도로 축적
- token 한계 존재 -> 일정 이상 축적 X
- token 쌓여 있을 시 한 번에 많은 packet 전송 O

### 예시
- ==ex)==

![[Scheduling-and-Traffic-Shaping-11.png]]

- ==r== = token 쌓이는 속도
- 가정) 처음 bucket 에는 token 이 꽉 차있음
- 풀이
	- 0 ~ 10ms : 사용 X
	- 10 ~ 30ms : 40 kbps - 15kbps = 25 * 20 = 500 bit 필요
	- 30 ~ 40ms : 50 kbps - 15kbps = 35 * 10 = 350 bit 필요
	- 40 ~ 60ms : 10 kbps - 15kbps = -5 * 20 = -100 bit 필요 (얻음)
	- 60 ~ 100ms : 20 kbps - 15kbps = 5 * 40 = 200 bit 필요
	- 총 ==950 bits== 필요
