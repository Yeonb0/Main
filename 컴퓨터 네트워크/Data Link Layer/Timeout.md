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

### cf) [[TCP]] 의 Timeout
- 만료 -> packet loss 판단 -> CWND = 1 초기화 & SSThresh 절반 설정 ([[Slow Start]] 재시작)
- end-to-end 이동 -> margin 크게 설정
- 판단 [[Delay|지연]] 회피 대안 -> [[Fast Retransmission]] 의 three duplicate ACK
