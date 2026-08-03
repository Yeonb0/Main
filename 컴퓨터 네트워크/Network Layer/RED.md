---
aliases:
  - Random Early Detection
  - RED(Random Early Detection)
---

- 특정 전송률 초과 시 random 으로 [[Packet]] drop 하는 [[Active Queue Management|AQM]] 기법

![[Scheduling-and-Traffic-Shaping-02.png]]

### 특징
- Minimum thrashold 까지 점점 drop 률 ↑
- Maximum thrashold 시 모든 packet drop
- Avglen = (1 - w) Avglen + w × SampleLen -> smoothing

![[Scheduling-and-Traffic-Shaping-03.png]]

### 계산
- ==ex)== 오는 Packet (SampleLen) : 100 -> 200 -> 50 -> 250 -> 100, ==w = 0.1==
	1. 100
	2. (1 - 0.1) × 100 + 0.1 × 200 = 90 + 20 = 110
	3. (1 - 0.1) × 110 + 0.1 × 50 = 99 + 5 = 104
