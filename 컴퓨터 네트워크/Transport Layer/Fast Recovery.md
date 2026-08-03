---
aliases:
  - 빠른 회복
  - Fast Recovery(빠른 회복)
---

- [[Fast Retransmission]] 후 CWND 복구 방식
- Three duplicate [[ACK]] -> 중간 한 packet 빼고 대부분 정상 전송
	- cf) [[Timeout]] -> 대부분 packet 전송 실패

### 절차
1. CWND = SSThresh
2. SSThresh = $\frac{\text{CWND}}{2}$
3. [[Slow Start]] skip -> 바로 [[Congestion Avoidance]] 단계 이동

![[Transport-Layer-24.png]]

![[Transport-Layer-25.png]]
