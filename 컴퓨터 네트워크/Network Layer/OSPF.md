---
aliases:
  - Open Shortest Path First
  - OSPF(Open Shortest Path First)
---

- [[Link-State Routing]] 구현 protocol
- Open Shortest Path First
- LSA message 로 정보 교환
- periodic + update 시 전송

### message format
![[Routing-23.png]]

| 항목 | 내용 |
| --- | --- |
| Link-[[state]] ID | 나 |
| Link ID | 내 친구 |
| Metric | 친구까지 거리 |
| Link data | 두 [[Router]] 사이 여러 link 구분 (≒ [[Sequence Number\|sequence number]]) |
