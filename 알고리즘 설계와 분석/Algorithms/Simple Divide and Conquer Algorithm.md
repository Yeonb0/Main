- 문제를 간단하게 C = A · B 라고 설정
- matrix A, B, C 를 $\frac{n}{2} \times \frac{n}{2}$ 로 나누기 -> 총 4 부분 
  ![[Pasted image 20260629101455.png]]![[Pasted image 20260629101511.png]]
- 총 8개의 곱셈 식 필요

### Divide
- matrix 절반으로 쪼개기  $\frac{n}{2} \times \frac{n}{2}$

### Conquer 
- 행렬 곱하기

### Combime 
- 행렬끼리 곱한 것 합치기

```cpp
MATRIX-MULTIPLY-RECURSIVE(matrix A, B, C, size n)
1  if n == 1
2      // base case
3      c₁₁ = c₁₁ + a₁₁ · b₁₁
4      return
5  // Divide : 행렬 절반으로 나누기
6  partition A, B, and C into n/2 × n/2 submatrices
       A₁₁, A₁₂, A₂₁, A₂₂; B₁₁, B₁₂, B₂₁, B₂₂;
       and C₁₁, C₁₂, C₂₁, C₂₂; 
7  // Conquer : 8개 곱셈식
8  MATRIX-MULTIPLY-RECURSIVE(A₁₁, B₁₁, C₁₁, n/2)
9  MATRIX-MULTIPLY-RECURSIVE(A₁₁, B₁₂, C₁₂, n/2)
10 MATRIX-MULTIPLY-RECURSIVE(A₂₁, B₁₁, C₂₁, n/2)
11 MATRIX-MULTIPLY-RECURSIVE(A₂₁, B₁₂, C₂₂, n/2)
12 MATRIX-MULTIPLY-RECURSIVE(A₁₂, B₂₁, C₁₁, n/2)
13 MATRIX-MULTIPLY-RECURSIVE(A₁₂, B₂₂, C₁₂, n/2)
14 MATRIX-MULTIPLY-RECURSIVE(A₂₂, B₂₁, C₂₁, n/2)
15 MATRIX-MULTIPLY-RECURSIVE(A₂₂, B₂₂, C₂₂, n/2)
```

``` cpp
int main()
{
  int N = 4; // 4 x 4 Matrix
  int stride = N;
  int A[16] = {1, 2, 3, 4,
               5, 6, 7, 8,
               9, 1, 2, 3,
               4, 5, 6, 7};
  int B[16] = {/* 생략 */};
  int C[16] = {0};
  mat_mul_recursive(A, B, C, 0, 0, 0, 0, 0, 0, N, stride);
}

void mat_mul_recursive(int* A, int* B, int* C,
                       int rowA, int colA,
                       int rowB, int colB,
                       int rowC, int colC,
                       int size, int stride)
{
  // base case:
  if (size == 1) {
    C[rowC * stride + colC] += A[rowA * stride + colA] * B[rowB * stride + colB];
    return;
  }

  int new_size = size / 2;
  // C11 = A11*B11 + A12*B21
  mat_mul_recursive(A, B, C, rowA, colA, rowB, colB, rowC, colC, new_size, stride);
  mat_mul_recursive(A, B, C, rowA, colA + new_size, rowB + new_size, colB, rowC, colC, new_size, stride);
  /* 생략 */
}
```

## [[알고리즘 분석]]
- base case (n = 1) : 두 수 곱하기 -> $\Theta(1)$
- recursive case (n > 1) 
	- Divide : $\Theta(1)$
	- Conquer : $8T(\frac{n}{2})$
	- Combine : C를 바로 업데이트 하므로 존재 X

> [!note] 전체 식
> 
> $$
>	T(n) = 8T \left( \frac{n}{2} \right) + \Theta(1)
> $$

- [[Master Method]] 사용 :[[ 시간 복잡도]] $O(n^3)$

