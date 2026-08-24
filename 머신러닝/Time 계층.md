---
aliases:
  - Time Layer
  - Time 계층(Time Layer)
---

- 같은 계층 $T$ 개 준비 -> 각 시각 [[데이터]] 를 개별 처리하는 계층
- [[시계열 데이터]] 한 번에 처리 -> [[RNNLM]] 의 구성 요소

### 구조
![[순환-신경망-(RNN)-22.png]]
![[순환-신경망-(RNN)-23.png]]

| 계층 | 역할 |
| --- | --- |
| `TimeEmbedding` | [[Embedding 계층]] $T$ 개 -> 단어 ID -> [[단어의 분산 표현]] |
| [[Time RNN 계층\|TimeRNN]] | [[RNN 계층]] $T$ 개 -> [[은닉 상태]] 출력 |
| `TimeAffine` | [[Affine 계층]] 을 행렬 계산으로 한 번에 처리 |
| `TimeSoftmaxWithLoss` | [[Softmax-with-Loss 계층]] $T$ 개 -> [[손실 함수\|손실]] 평균 |

### Time Embedding
```python
class TimeEmbedding:
    def __init__(self, W):
        self.params = [W]
        self.grads = [np.zeros_like(W)]
        self.layers = None
        self.W = W

    def forward(self, xs):
        N, T = xs.shape
        V, D = self.W.shape

        out = np.empty((N, T, D), dtype='f')
        self.layers = []

        for t in range(T):
            layer = Embedding(self.W)
            out[:, t, :] = layer.forward(xs[:, t])
            self.layers.append(layer)

        return out

    def backward(self, dout):
        N, T, D = dout.shape

        grad = 0
        for t in range(T):
            layer = self.layers[t]
            layer.backward(dout[:, t, :])
            grad += layer.grads[0]

        self.grads[0][...] = grad
        return None
```
- [[Embedding 계층]] $T$ 개 이용해 각각 처리

### Time Affine
```python
class TimeAffine:
    def __init__(self, W, b):
        self.params = [W, b]
        self.grads = [np.zeros_like(W), np.zeros_like(b)]
        self.x = None

    def forward(self, x):
        N, T, D = x.shape
        W, b = self.params

        rx = x.reshape(N*T, -1)
        out = np.dot(rx, W) + b
        self.x = x
        return out.reshape(N, T, -1)

    def backward(self, dout):
        x = self.x
        N, T, D = x.shape
        W, b = self.params

        dout = dout.reshape(N*T, -1)
        rx = x.reshape(N*T, -1)

        db = np.sum(dout, axis=0)
        dW = np.dot(rx.T, dout)
        dx = np.dot(dout, W.T)
        dx = dx.reshape(*x.shape)

        self.grads[0][...] = dW
        self.grads[1][...] = db

        return dx
```
- (N, T, D) -> (N×T, D) `reshape` -> [[행렬의 곱]] 한 번에 계산

### Time Softmax with Loss
![[순환-신경망-(RNN)-24.png]]
- $T$ 개 [[Softmax-with-Loss 계층]] 의 [[손실 함수|손실]] 평균 -> 최종 손실

$$
L = \frac{1}{T}(L_0, L_1, + \cdots + L_{T-1})
$$

- [[데이터]] $N$ 개 -> 다시 합산 후 평균 -> 최종 출력

```python
class TimeSoftmaxWithLoss:
    def __init__(self):
        self.params, self.grads = [], []
        self.cache = None
        self.ignore_label = -1

    def forward(self, xs, ts):
        N, T, V = xs.shape

        if ts.ndim == 3:  # 정답 레이블이 원핫 벡터인 경우
            ts = ts.argmax(axis=2)

        mask = (ts != self.ignore_label)

        # 배치용과 시계열용을 정리(reshape)
        xs = xs.reshape(N * T, V)
        ts = ts.reshape(N * T)
        mask = mask.reshape(N * T)

        ys = softmax(xs)
        ls = np.log(ys[np.arange(N * T), ts])
        ls *= mask  # ignore_label에 해당하는 데이터는 손실을 0으로 설정
        loss = -np.sum(ls)
        loss /= mask.sum()

        self.cache = (ts, ys, mask, (N, T, V))
        return loss

    def backward(self, dout=1):
        ts, ys, mask, (N, T, V) = self.cache

        dx = ys
        dx[np.arange(N * T), ts] -= 1
        dx *= dout
        dx /= mask.sum()
        dx *= mask[:, np.newaxis]  # ignore_labelㅇㅔ 해당하는 데이터는 기울기를 0으로 설정

        dx = dx.reshape((N, T, V))

        return dx
```
- `ignore_label` -> 해당 [[데이터]] 의 [[손실 함수|손실]] · [[기울기]] 0 처리
