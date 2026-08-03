---
aliases:
  - 슬로 스타트
  - Slow Start Phase
  - Slow Start(슬로 스타트)
---

- [[Congestion Control]] 첫 단계 -> CWND 지수 증가
- Initial CWND = ==1 MSS==
- `ACK` 받을 때마다 CWND++ -> 각 RTT 마다 2배 (exponential increase)

![[Transport-Layer-21.png]]

![[Transport-Layer-22.png]]

- 결국 packet drop -> congestion 발생

### [[Timeout]] 시
- segment 전송 후 일정 시간 미수신 -> LOST 판단
- CWND = ==1== 로 초기화
- SSThresh = $\frac{\text{CWND}}{2}$ -> drop 당시 CWND 의 절반
- end-to-end 간 packet 이동 -> margin 크게 설정
- SSThresh 도달 이후 -> [[Congestion Avoidance]]
