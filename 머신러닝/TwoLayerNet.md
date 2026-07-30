---
aliases:
  - 2층 신경망 클래스
  - TwoLayerNet(2층 신경망 클래스)
---

- [[머신러닝/오차역전파법]] 적용 2층 [[머신러닝/신경망]] [[클래스]]
- 계층을 `OrderedDict` 에 보관 -> 추가 순서대로 [[순전파]] , 역순으로 [[역전파]]

### 인스턴스 변수
| [[인스턴스]] [[변수]] | 설명 |
| --- | --- |
| `params` | 딕셔너리 변수. 신경망 매개변수 보관 `params['W1']`, `params['W2']` / `params['b1']`, `params['b2']` |
| `layers` | 순서 있는 딕셔너리 변수. 신경망 계층 보관 `layers['Affine1']` -> `layers['Relu1']` -> `layers['Affine2']` |
| `lastLayer` | 신경망 마지막 계층. [[Softmax-with-Loss 계층]] |

### 메소드
| [[메소드]] | 설명 |
| --- | --- |
| `__init__(self, input_size, hidden_size, output_size, weight_init_std)` | 초기화 수행. [[입력층]] · [[은닉층]] · [[출력층]] [[뉴런]] 수 / 초기화 시 정규분포 스케일 |
| `predict(self, x)` | 예측 (추론) 수행. `x` -> 이미지 [[데이터]] |
| `loss(self, x, t)` | [[손실 함수]] 값 계산. `x` -> 이미지 데이터 / `t` -> [[정답 레이블]] |
| `accuracy(self, x, t)` | 정확도 계산 |
| `numerical_gradient(self, x, t)` | [[가중치 1]] 매개변수 [[기울기]] 를 [[수치 미분]] 으로 계산 |
| `gradient(self, x, t)` | [[가중치 1]] 매개변수 [[기울기]] 를 [[머신러닝/오차역전파법]] 으로 계산 |

### 구현
```python
import sys, os
from collections import OrderedDict

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 가중치 초기화
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

        # 계층 생성
        self.layers = OrderedDict() # 신경망 계층을 OrderedDict 에 보관!
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])

        self.last_layer = SoftmaxWithLoss()

    def predict(self, x):
        for layer in self.layers.values(): # 추가 순서대로 각 계층의 forward() 호출
            x = layer.forward(x)

        return x

    # x : 입력 데이터, t : 정답 레이블
    def loss(self, x, t):
        y = self.predict(x)

        return self.last_layer.forward(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1 : t = np.argmax(t, axis=1)
        accuracy = np.sum(y == t) / float(x.shape[0])

        return accuracy

    # x : 입력 데이터, t : 정답 레이블
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])

        return grads

    def gradient(self, x, t):
        # 순전파
        self.loss(x, t) 

        # 역전파
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()  # 게층 반대 순서로 호출!
        for layer in layers:
            dout = layer.backward(dout)

        # 결과 저장
        grads = {}
        grads['W1'] = self.layers['Affine1'].dW
        grads['b1'] = self.layers['Affine1'].db
        grads['W2'] = self.layers['Affine2'].dW
        grads['b2'] = self.layers['Affine2'].db

        return grads
```
