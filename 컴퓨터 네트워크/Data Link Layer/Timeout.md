---
aliases:
  - 타임아웃
  - Timeout(타임아웃)
---

- Sender 가 frame 전송 후 [[ACK]] 를 기다리는 제한 시간
- timeout period = [[RTT]] + margin (delay 고려)
- Sender 는 frame 보낸 후 timer 설정
	- 너무 길어도 짧아도 X
- 만료 -> 같은 frame 재전송

### RTT
- Round Trip Time : message 보내고 다시 [[신호]] 받을 때까지 걸리는 시간
- 일정하지 않음
