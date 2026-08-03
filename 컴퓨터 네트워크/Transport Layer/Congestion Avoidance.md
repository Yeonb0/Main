---
aliases:
  - 혼잡 회피
  - Congestion Avoidance Phase
  - Congestion Avoidance(혼잡 회피)
---

- [[Slow Start]] 후 SSThresh 지점 도달 -> 천천히 증가하는 구간
- CWND += MSS * $\frac{\text{MSS}}{\text{CWND}}$
- 선형적 증가 -> Additive Increase

![[Transport-Layer-23.png]]

- drop 발생 -> CWND = 1 초기화 & SSThresh 재설정 후 처음부터
- [[Fast Recovery]] 시 -> slow start skip 후 바로 진입
