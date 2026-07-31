---
aliases:
  - NRZ-I(Inverted)
  - Non-Return-to-Zero Inverted
---

- [[Polar Encoding]] 중 [[신호]] 전이(transition) 유무로 [[데이터]] 인코딩
	- bit 0 -> 전이 없음
	- bit 1 -> 전이 발생

![[Digital-Transmission-05.png]]

### 특징
- 1 반복 -> 계속 변화 -> [[DC Component]] 발생 X
- 0 지속 -> 전이 없음 -> [[Clock Drift]] 발생 가능
- r = 1 -> 좋은 transmission rate, but [[Self Synchronization]] 문제 -> [[4B5B|4B/5B]] 로 보완
