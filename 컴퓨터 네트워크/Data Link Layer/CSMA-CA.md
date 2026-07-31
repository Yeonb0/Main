---
aliases:
  - CSMA/CA
  - Collision Avoidance
  - CSMA/CA(Collision Avoidance)
---

- [[Collision|충돌]] 감지 대신 회피하는 [[CSMA]] 확장
- 무선 ([[Wi-Fi]]) 에서 주로 사용 -> detect 불가능 -> avoid

### 배경
- 무선 -> [[Half Duplex]]
	- 한 채널 사용 시 송신 / 수신 동시에 하나만 O
	- 동시 수행 -> 서로 간섭 (self interference)
	- [[CSMA-CD|CSMA/CD]] 처럼 collision detect 불가능
- [[ACK]] 이용
	- frame 전송 -> [[ACK]] 대기 -> 미수신 시 collision 판단
	- [[Binary Exponential Backoff]] 적용

### 절차
1. idle 확인 후 [[IFS]] 대기
2. [[Contention Window]] countdown
3. 전송 -> [[ACK]] 수신

### CSMA/CA with ACK
![[Medium-Access-Control-27.png]]
- 실제론 [[ACK]] 사용 -> [[IFS]] 를 SIFS / DIFS 로 구분
