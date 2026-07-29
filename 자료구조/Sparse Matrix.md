---
aliases:
  - 희소 행렬
---
## [[ADT]]
### [[객체|Objects]]
3원소 쌍 $\langle$행, 열, 값$\rangle$ 집합
- 행, 열 -> 정수
- 이 조합은 유일 
- 값 $\in$ `item`

### [[함수|Functions]]
$\forall a, b \in$ `SparseMatrix`, $x \in$ `item`, $i, j, \text{maxCol}, \text{maxRow} \in$ `index`
- `SparseMatrix` `Create(maxRow, maxCol)`
	- `return` maxRow $\times$ maxCol 까지 저장할 수 있는 SparseMatrix

- `SparseMatrix` `Tranpose(a)`
	- `return` $A^{T}$ 된 행렬

- `SparseMatrix` `Add(a, b)`
	- `if` (a 와 b 의 차원 일치)
		- `return` a + b
		- `else return` error

- `SparseMatrix` `Multiply`
	- `if` (a 의 col 수 = b 의 row 수)
		- `return` a · b
		- `else return` error