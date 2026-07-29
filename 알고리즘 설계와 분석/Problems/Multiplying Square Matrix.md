### 문제 정의
- 정사각행렬 곱하기

- Input : 세 개의 $n \times n$ 행렬, $A = (a_{ij})$, $B = (b_{ij})$, $C=(c_{ij})$
- Output : $C + A \cdot B$
  $$
		c_{ij} = c_{ij} + \sum^n_{k=1}a_{ik} \cdot b_{kj}
	$$

```cpp
MATRIX_MULTIPLY(matrix A, B, C, size n)
	for i = 1 ~ n
		for j = 1 ~ n
			for k = 1 ~ n
				c_ij = c_ij + a_ik * b_kj
```

### Algorithm
- [[Simple Divide and Conquer Algorithm]]
- [[Strassen's Algorithm]]