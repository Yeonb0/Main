---
aliases:
  - 빠른 재전송
  - Fast Retranssmission
  - Fast Retransmission(빠른 재전송)
---

- [[Timeout]] 대기 없이 재전송 -> end-to-end 대기로 인한 loss 판단 [[Delay|지연]] 해소
- Three duplicate ACK : 같은 번호 [[ACK]] ==3번== 반복 -> drop 판단
- 판단 즉시 해당 segment 재전송
- 이후 CWND 처리 -> [[Fast Recovery]]
