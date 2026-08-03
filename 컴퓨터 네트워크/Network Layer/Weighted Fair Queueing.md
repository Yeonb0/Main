---
aliases:
  - WFQ
  - 가중 공정 큐잉
  - Weighted Fair Queueing(WFQ)
---

- [[Fair Queueing]] + flow 별 weight
- 가장 많이 사용하는 [[Scheduling]] 방식

### 특징
- packet 전송 시 weight 로 나눈 값만큼만 가산
- weight ↑ -> 전송 기회 ↑
- $S_i = S_i + \frac{P}{w_i}$

### 예시
- ==ex)==

![[Scheduling-and-Traffic-Shaping-07.png]]
