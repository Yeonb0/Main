---
aliases:
  - Multi-Level Transmit 3
  - MLT-3(Multi-Level Transmit 3)
---

- [[LAN]] 에서 사용하는 3-level 전송 방식
	- 다음 bit 가 0 -> 앞이랑 똑같이
	- 다음 bit 가 1 ->
		- 현재 level 이 0 이 아님 -> 0
		- 현재 level 이 0 임 -> 바로 직전 `+`, `-` 의 반대

![[Digital-Transmission-09.png]]

### 특징
- [[Baseline Wandering]] 발생 가능성 ↓, but 완전 없지는 않음
- 0 연속 -> level 고정 -> [[Clock Drift]]
