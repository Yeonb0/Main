---
aliases:
  - Negative Acknowledgement
  - NAK(Negative Acknowledgement)
  - 부정 응답
---

- 원하는 frame 외에 다른 frame 전송 받음 -> send 측에 원하는 frame 알려주기
- [[Selective Repeat]] 의 재전송 유도 수단

![[Framing-Error-Control-20.png]]

### 동작
- [[ACK]](1) : 0 번 frame 까지 전송 받음 알림
- NAK(1) : 1 번 frame 받아야 하는데 다른 frame 이 왔다고 알림
- NAK 전송 X -> sender 는 [[Timeout]] 까지 대기
- sender 는 NAK 받으면 해당 frame 재전송
- NAK 보냈는데도 해당 frame 미도착 -> 아무것도 안 함 (예시에선 한 번만 전송)

### Out-of-order frame 도착 시 정책
1. 매번 도착마다 NAK 전송
2. 같은 NAK 에 대해 1 번만 전송 -> [[Selective Repeat]] 사용
3. 아예 전송 X -> timeout 의존
