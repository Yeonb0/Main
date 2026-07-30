---
aliases:
  - ReLU Layer
  - ReLU 계층(ReLU Layer)
---

- [[ReLU 함수]] 의 [[순전파]] · [[역전파]] 구현 계층
- 입력 0 초과 -> 상류 값 그대로 하류 / 0 이하 -> 0 전달

$$
y =\begin{cases}x & (x > 0) \\0 & (x \le 0)\end{cases}
$$

$$
\frac{\partial y}{\partial x} =\begin{cases}1 & (x > 0) \\0 & (x \le 0)\end{cases}
$$

![[오차역전파법-15.png]]

### 구현
- `forward()`, `backward()` 인수 -> [[넘파이]] [[배열]]

```python
class Relu:
    
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx
```
- `mask` [[인스턴스]] [[변수]] : `True` / `False` 구성 [[넘파이]] [[배열]]
	- 원소 값 0 이하 -> `True`
	- 원소 값 0 초과 -> `False`
	- `mask` 가 `True` 인 위치 -> 상류 `dout` 을 0 으로 설정
- ==ex)==
```python
x = np.array([[1.0, -0.5], [-2.0, 3.0]])
print(x)
mask = (x <= 0)
print(mask)
```

> [!note]- 실행 결과
> ![[오차역전파법-16.png]]
