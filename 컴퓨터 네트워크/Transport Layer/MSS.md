---
aliases:
  - Maximum Segment Size
  - MSS(Maximum Segment Size)
  - 최대 세그먼트 크기
---

- 한 segment 에 담을 수 있는 최대 data 크기
- MSS = [[MTU]] - [[IP]] header (20) - TCP header (20 + α)

### 특징
- 보통 ==1460== 인 경우 多
- ==1500== 안 넘도록 절단
- [[Congestion Control]] 의 CWND 단위
