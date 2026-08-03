---
aliases:
  - 리키 버킷
  - Leaky Bucket(리키 버킷)
---

- 구멍 뚫린 양동이 형태의 [[Traffic Shaping]] 기법

![[Scheduling-and-Traffic-Shaping-10.png]]

### 특징
- 들어오는 [[Packet]] 일정 X
- 나가는 packet 일정 O
- 어떠한 burst 도 허락 X -> 완화 형태 [[Token Bucket]]
