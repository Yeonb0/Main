---
aliases:
  - 누적 확인 응답
  - Cumulative ACK(누적 확인 응답)
---

- ACK(n) : n-1 까지 frame 다 받음 의미 -> [[Go-Back-N]] 의 [[ACK]] 방식

![[Framing-Error-Control-17.png]]

### 특징
- ACK 2 는 lost, but ACK 3 는 제대로 전달
	- ACK 2 전송 안됐더라도 1, 2 제대로 받았다는 것 확인 -> window 2 칸 이동
- 중간 ACK 손실 복구 O

### Timeout case
![[Framing-Error-Control-18.png]]
- Out-of-order frame 도착 -> ACK 전송 X ([[Stop-and-Wait]] 와 차이)
	- [[NAK]] 없음
