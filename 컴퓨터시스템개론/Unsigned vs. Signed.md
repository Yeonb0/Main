---
aliases:
  - Unsigned와 Signed
  - 부호 없는 정수와 부호 있는 정수
---

- 같은 bit pattern 을 부호 없이 / 부호 있게 해석하는 두 가지 [[정수]] 표현
- |Unsigned| + |Signed| = $2^w$

### Unsigned
- 부호 X -> 표현 범위 좀 더 넓음
- Min = 0
- Max = $2^w - 1$

$$
\text{B2U}_w(x) = \sum^{w-1}_{i=0}x_i\cdot2^i
$$

### Signed
- 부호 O -> [[2의 보수]] 로 해석
- Min = $-2^{w-1}$
- Max = $2^{w-1} - 1$
	- 음수 범위가 1 개 많음 (asymmetric)

$$
\text{B2S}_w(x) = x_{w-1} \cdot(-2^{w-1})+\sum^{w-2}_{i=0}x_i\cdot2^i
$$

![[Data-Representation-07.png]]

### 대응표
| X | B2U(X) | B2S(X) |
| --- | --- | --- |
| 0000 | 0 | 0 |
| 0001 | 1 | 1 |
| 0010 | 2 | 2 |
| 0011 | 3 | 3 |
| 0100 | 4 | 4 |
| 0101 | 5 | 5 |
| 0110 | 6 | 6 |
| 0111 | 7 | 7 |
| 1000 | 8 | -8 |
| 1001 | 9 | -7 |
| 1010 | 10 | -6 |
| 1011 | 11 | -5 |
| 1100 | 12 | -4 |
| 1101 | 13 | -3 |
| 1110 | 14 | -2 |
| 1111 | 15 | -1 |

### Mapping
- 같은 bit pattern -> 두 개의 다른 수로 해석 O

![[Data-Representation-08.png]]
