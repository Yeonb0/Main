---
aliases:
  - 나이퀴스트 공식
  - Nyquist Theorem
  - Nyquist Equation(나이퀴스트 공식)
---

- [[Noise]] 고려 X 인 최대 [[Data Transfer Rate]] 계산식
- Data rate = $2 \times B \times \log_2L$
	- B : bandwidth
	- L : signal level 숫자 (사용 비트의 2의 제곱수)

### 조건
- 최소 필요 bandwidth = $\frac{n}{2}$ -> Nyquist Condition
	- [[Baseband Transmission]] 의 복원 하한선

### 특징
- signal level 많이 나눔 -> noise 에 취약
	- [[신호]]가 비슷해서 구분 어려움
- noise 반영 필요 -> [[Shannon Capacity]]
