---
aliases:
  - Time RNN Layer
  - Time RNN 계층(Time RNN Layer)
  - TimeRNN
---

- [[RNN 계층]] $T$ 개를 연결한 계층
- 길이 $T$ 인 [[시계열 데이터]] 입력 -> $T$ 개 [[은닉 상태]] 출력
- 가로로 펼쳐진 [[머신러닝/신경망|신경망]] 을 하나의 계층으로 취급

### 구조
![[순환-신경망-(RNN)-11.png]]
- [[Truncated BPTT]] 전제 -> 가로 길이 $T$ 고정

![[순환-신경망-(RNN)-12.png]]
- $\mathbf{xs}$ 행렬 입력 -> $\mathbf{hs}$ 행렬 출력하는 단일 계층

![[순환-신경망-(RNN)-16.png]]

| 단계 | 계층 |
| --- | --- |
| 1 단계 | [[RNN 계층]] |
| $T$ 단계 | Time RNN 계층 |

### 은닉 상태 관리
![[순환-신경망-(RNN)-17.png]]
- [[은닉 상태]] 를 계층 내부에서 관리 -> RNN 계층 사이 인계 작업 고려 X
- `stateful` 인수로 조정

### 초기화
```python
class TimeRNN:
    def __init__(self, Wx, Wh, b, stateful=False):
        self.params = [Wx, Wh, b]
        self.grads = [np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)]
        self.layers = None

        self.h, self.dh = None, None
        self.stateful = stateful

    def set_state(self, h):
        self.h = h

    def reset_state(self):
        self.h = None
```

| [[인스턴스]] [[변수]] | 내용 |
| --- | --- |
| `layers` | 다수 [[RNN 계층]] 을 담는 리스트 |
| `h` | `forward()` 가 만든 [[은닉 상태]] (`h_prev` 역할) |
| `dh` | `backward()` 가 만든 [[은닉 상태]] [[기울기]] (`dh_prev` 역할) |
| `stateful` | `True` -> [[state\|상태]] 유지 / `False` -> 영행렬 초기화 |

### 순전파
```python
    def forward(self, xs):
        Wx, Wh, b = self.params
        N, T, D = xs.shape
        D, H = Wx.shape
        self.layers = []
        hs = np.empty((N, T, H), dtype='f')

        if not self.stateful or self.h is None:
            self.h = np.zeros((N, H), dtype='f')

        for t in range(T):
            layer = RNN(*self.params)
            self.h = layer.forward(xs[:, t, :], self.h)
            hs[:, t, :] = self.h
            self.layers.append(layer)
            
        return hs
```
- 인수 `xs` : $T$ 개 분량 [[시계열 데이터]] -> 형상 (N, T, D)
- 첫 호출 or `stateful` = `False` -> `h` 영행렬 초기화
- 각 시각 `t` 의 [[은닉 상태]] -> `t+1` 단계 [[RNN 계층]] 에 사용

### 역전파
![[순환-신경망-(RNN)-18.png]]
- $\mathbf{dhs}$ : 출력에서 오는 [[기울기]] / $\mathbf{dxs}$ : 입력쪽으로 나갈 [[기울기]]
- [[Truncated BPTT]] -> 이전 시각 방향 [[역전파]] X

![[순환-신경망-(RNN)-19.png]]
- $\mathbf{dh}_{next}$ (미래 계층 기울기) + $\mathbf{dh}_t$ (현재 계층 기울기) -> 합산 후 전파
- 결과 : $\mathbf{dh}_{prev}$ (이전 계층 기울기) & $\mathbf{dx}_t$ (현재 입력 기울기)

```python
    def backward(self, dhs):
        Wx, Wh, b = self.params
        N, T, H = dhs.shape
        D, H = Wx.shape

        dxs = np.empty((N, T, D), dtype='f')
        dh = 0
        grads = [0, 0, 0]
        for t in reversed(range(T)):
            layer = self.layers[t]
            dx, dh = layer.backward(dhs[:, t, :] + dh)  # 합산된 기울기
            dxs[:, t, :] = dx

            for i, grad in enumerate(layer.grads):
                grads[i] += grad

        for i, grad in enumerate(grads):
            self.grads[i][...] = grad
        self.dh = dh

        return dxs
```
- [[순전파]] 반대 순서로 각 [[RNN 계층]] `backward()` 호출
- [[가중치]] [[기울기]] -> 각 계층 합산해 `self.grads` 에 덮어쓰기
