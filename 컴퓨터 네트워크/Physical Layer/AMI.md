---
aliases:
  - Alternate Mark Inversion
  - AMI(Alternate Mark Inversion)
---

- [[Bipolar Encoding]] 중 signal level 3개 사용 : ==+V, 0V, -V==
	- bit 0 -> 0V
	- bit 1 -> +V, -V 교대 사용

### 특징
- 1 은 극성 교대 -> 평균 0 -> [[DC Component]] 발생 X
- 0 지속 -> 0V 유지 -> 전이 없음 -> [[Clock Drift]] 발생 가능
	- [[B8ZS]], [[HDB3]] 같은 [[Scrambling]] 으로 보완
