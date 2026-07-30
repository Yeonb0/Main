---
aliases:
  - Affine Layer
  - 어파인 계층
  - Affine 계층(Affine Layer)
---

- [[머신러닝/신경망]] [[순전파]] 의 [[행렬의 곱 1]] 수행 계층
- 어파인 변환 (Affine Transformation) 처리 -> $\mathbf{X} \cdot \mathbf{W} + \mathbf{B}$

### 순전파
- [[가중치 1]] [[신호]] 총합 계산 -> `np.dot()` 사용
```python
X = np.random.rand(2)    # 입력   (2,)
W = np.random.rand(2, 3) # 가중치 (2, 3)
B = np.random.rand(3)    # 편향   (3,)

Y = np.dot(X, W) + B
```
![[오차역전파법-23.png]]

### 역전파
$$
\begin{align}\frac{\partial L}{\partial \mathbf{X}} &= \frac{\partial L}{\partial \mathbf{Y}} \cdot \mathbf{W}^{\mathrm{T}} \\\frac{\partial L}{\partial \mathbf{W}} &= \mathbf{X}^{\mathrm{T}} \cdot \frac{\partial L}{\partial \mathbf{Y}}\end{align}
$$

![[오차역전파법-24.png]]
- $\mathbf{X}$ & $\frac{\partial L}{\partial \mathbf{X}}$ , $\mathbf{W}$ & $\frac{\partial L}{\partial \mathbf{W}}$ -> 동일 형상
	- 대응 차원의 원소 수 일치 필요

### 배치용 Affine 계층
- 기존 Affine 계층 -> 입력 [[데이터]] 1개
- [[배치 처리]] -> 데이터 N개 묶어 [[순전파]]
![[오차역전파법-25.png]]
- 입력 $\mathbf{X}$ 형상 (N, 2)
- [[편향 1]] -> 각 데이터에 더해짐 (각 세로 열)
- ==ex)==
```python
X_dot_W = np.array([[0, 0, 0], [10, 10, 10]])
B = np.array([1, 2, 3])

print(X_dot_W + B)
```

> [!note]- 실행 결과
> ![[오차역전파법-26.png]]

```python
dY = np.array([[1, 2, 3], [4, 5, 6]])
dB = np.sum(dY, axis=0)
print(dB)  
```

> [!note]- 실행 결과
> ![[오차역전파법-27.png]]

- `np.sum()` `axis=0` -> 0번째 축 (데이터 단위 축) 총합

### 구현
```python
class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(self.x, self.W) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        return dx
```
- 접두 `d` -> [[미분]] 의미
