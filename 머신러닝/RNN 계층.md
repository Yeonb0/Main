---
aliases:
  - RNN Layer
  - RNN 계층(RNN Layer)
---

- 한 시각 분량만 처리하는 [[순환 신경망]] 의 최소 계층
- 입력 $\mathbf{x}_t$ + 이전 [[은닉 상태]] $\mathbf{h}_{t-1}$ -> 현재 [[은닉 상태]] $\mathbf{h}_t$
- $T$ 단계 묶음 -> [[Time RNN 계층]]

### 형상
![[순환-신경망-(RNN)-13.png]]

| 기호 | 의미 |
| --- | --- |
| $N$ | [[미니배치 학습\|미니배치]] 크기 |
| $D$ | 입력 벡터 차원 수 |
| $H$ | [[은닉 상태]] 벡터 차원 수 |

- [[행렬의 곱]] -> 항상 차원 일치 필요
- 각 샘플 [[데이터]] 를 ↓ (행) 방향으로 저장

### 초기화
```python
class RNN:
    def __init__(self, Wx, Wh, b):
        self.params = [Wx, Wh, b]
        self.grads = [np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)]
        self.cache = None
```
- `Wx` · `Wh` : 입력 · 은닉 [[가중치]] / `b` : [[편향]] -> `params` 에 리스트 저장
- 매개변수와 같은 형상의 0 [[배열]] -> `grads` 에 저장
- `cache` : [[역전파]] 계산에 쓸 중간 [[데이터]] 창고
- [[계층 구현 규칙]] 준수

### 순전파
$$
\mathbf{h}_t = \tanh (\mathbf{h}_{t-1}\mathbf{W}_\mathbf{h} + \mathbf{x}_t\mathbf{W}_\mathbf{x}+\mathbf{b})
$$

```python
    def forward(self, x, h_prev):
        Wx, Wh, b = self.params
        t = np.matmul(h_prev, Wh) + np.matmul(x, Wx) + b
        h_next = np.tanh(t)

        self.cache = (x, h_prev, h_next)
        return h_next   
```
- 인수 : `x` (입력) / `h_prev` (이전 RNN 계층 출력)

![[순환-신경망-(RNN)-14.png]]

### 역전파
![[순환-신경망-(RNN)-15.png]]
- [[순전파]] 반대 방향으로 각 연산자 역전파 수행

```python
    def backward(self, dh_next):
        Wx, Wh, b = self.params
        x, h_prev, h_next = self.cache

        dt = dh_next * (1 - h_next ** 2)
        db = np.sum(dt, axis=0)
        dWh = np.matmul(h_prev.T, dt)
        dh_prev = np.matmul(dt, Wh.T)
        dWx = np.matmul(x.T, dt)
        dx = np.matmul(dt, Wx.T)

        self.grads[0][...] = dWx
        self.grads[1][...] = dWh
        self.grads[2][...] = db

        return dx, dh_prev
```
- $\tanh$ [[미분]] -> `1 - h_next ** 2`
- 반환 : `dx` (입력 [[기울기]]) & `dh_prev` (이전 시각 [[은닉 상태]] 기울기)
