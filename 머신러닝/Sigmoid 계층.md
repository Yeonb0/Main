---
aliases:
  - Sigmoid Layer
  - 시그모이드 계층
  - Sigmoid 계층(Sigmoid Layer)
---

- [[시그모이드 함수 1]] 의 [[순전파]] · [[역전파]] 구현 계층

$$
y = \frac{1}{1 +\exp(-x)}
$$

![[오차역전파법-17.png]]
- `exp` , `/` [[node]] 등장

### 역전파 절차
1. `/` node 미분 ($y = \frac{1}{x}$) -> $\frac{\partial y}{\partial x} = -\frac{1}{x^2} = -y^2$
![[오차역전파법-18.png]]
2. `+` node -> 상류 값 그대로 하류 전달
![[오차역전파법-19.png]]
3. `exp` node 미분 -> $\frac{\partial y}{\partial x} = \exp(x)$
![[오차역전파법-20.png]]
4. `×` node -> [[순전파]] 때 값 서로 바꿔 곱하기 (-1 곱하기)
![[오차역전파법-21.png]]

### 간소화
![[오차역전파법-22.png]]

$$
\begin{aligned}\frac{\partial L}{\partial y} y^2 \exp(-x) &= \frac{\partial L}{\partial y} \frac{1}{(1+\exp(-x))^2} \exp(-x) \\&= \frac{\partial L}{\partial y} \frac{1}{1+\exp(-x)} \cdot \frac{\exp(-x)}{1+\exp(-x)} \\&= \frac{\partial L}{\partial y} y(1-y)\end{aligned}
$$

- [[순전파]] 출력 $y$ 만으로 [[역전파]] 계산 O

### 구현
```python
class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out

        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out
        
        return dx
```
- [[순전파]] 출력 `out` 에 저장 -> [[역전파]] 계산에 [[재사용(Reuse)|재사용]]
