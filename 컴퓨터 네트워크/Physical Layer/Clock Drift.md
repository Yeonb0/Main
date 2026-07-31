---
aliases:
  - 클럭 드리프트
  - 클럭 드리프트(Clock Drift)
---

- device 마다 clock speed 미세하게 상이 -> 수신 시점 어긋남
- [[DC Component]] 로 인해 발생
- [[Self Synchronization]] 으로 clock 보정
	- bit 에 변화 없음 -> 보정 X
- [[NRZ-L]] < [[NRZ-I]]
	- [[NRZ-L]] : 0 or 1 지속 -> DC 발생
	- [[NRZ-I]] : 0 지속 -> DC 발생, 1 반복 -> 계속 전이 -> DC 발생 X
