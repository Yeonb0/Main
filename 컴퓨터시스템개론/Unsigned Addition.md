---
aliases:
  - 부호 없는 덧셈
  - Unsigned Addition(부호 없는 덧셈)
---

- Unsigned 정수끼리 bit sequence 형태로 더하는 [[연산]]
- 두 binary number 더하기
	- [[CPU]] 회로에서 [[게이트]] 통해 똑같은 방식으로 구현
	- 단, carry output 버림
- modular sum

$$
\text{UAdd}_w(u, v) = (u + v) \mod 2^w
$$

![[Data-Representation-09.png]]

- w + 1 bit 버림 -> [[오버플로]] 로 실제 값과 다른 결과

### 시각화
- 현실 세계의 u, v 더하기
	- under, overflow 없음
	- linear 하게 증가

![[Data-Representation-11.png]]

- Unsigned Addition
	- $2^w \sim 2^{w-1}$ 까지는 $0 \sim 2^w$ 에 mapping
	- overflow 발생

![[Data-Representation-12.png]]
