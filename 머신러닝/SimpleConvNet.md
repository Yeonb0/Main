---
aliases:
  - 단순 CNN 클래스
  - SimpleConvNet(단순 CNN 클래스)
---

- [[합성곱 계층]] + [[풀링 계층]] 조합한 단순 [[합성곱 신경망]] 구현 [[클래스]]
- 구성 : Convolution -> [[ReLU 함수 1|ReLU]] -> Pooling -> Affine -> ReLU -> Affine -> Softmax
![[합성곱-신경망-(CNN)-31.png]]

### 초기화
```python
class SimpleConvNet:
    def __init__(self, input_dim=(1, 28, 28),
                conv_param={'filter_num':30, 'filter_size':5, 'pad':0, 'stride':1},
                hidden_size=100, output_size=10, weight_init_std=0.01):
        filter_num = conv_param['filter_num']
        filter_size = conv_param['filter_size']
        filter_pad = conv_param['pad']
        filter_stride = conv_param['stride']
        input_size = input_dim[1]
        conv_output_size = (input_size - filter_size + 2*filter_pad) / filter_stride + 1
        pool_output_size = int(filter_num * (conv_output_size/2) * (conv_output_size/2))
```

| 인수                | 내용                              |
| ----------------- | ------------------------------- |
| `input_dim`       | 입력 데이터 차원 (채널 수, 높이, 너비)        |
| `conv_param`      | [[합성곱 계층]] [[하이퍼 파라미터]] -> 딕셔너리 |
| `hidden_size`     | [[은닉층]] [[뉴런]] 수 (완전연결)         |
| `output_size`     | [[출력층]] 뉴런 수 (완전연결)             |
| `weight_init_std` | 초기화 시 [[가중치]] 표준편차              |

- `conv_param` 구성
	- `filter_num` : [[필터]] 수
	- `filter_size` : 필터 크기
	- `pad` : [[패딩]] 크기
	- `stride` : [[스트라이드]] 간격

### 가중치 초기화
```python
# 가중치 초기화
self.params = {}
self.params['W1'] = weight_init_std * np.random.randn(filter_num, input_dim[0], filter_size, filter_size)
self.params['b1'] = np.zeros(filter_num)
self.params['W2'] = weight_init_std * np.random.randn(pool_output_size, hidden_size)
self.params['b2'] = np.zeros(hidden_size)
self.params['W3'] = weight_init_std * np.random.randn(hidden_size, output_size)
self.params['b3'] = np.zeros(output_size)
```
- `W1` -> [[합성곱 계층]] + ReLU + [[풀링 계층]] : `filter` input -> `pool` output
- `W2` -> Affine + ReLU (완전연결) : `pool` output -> `hidden` output
- `W3` -> Affine + Softmax (완전연결) : `hidden` output -> `output`
- [[편향]] (b) -> 0 으로 설정

### 계층 생성
```python
    # 계층 생성
    self.layers = OrderedDict()
    self.layers['Conv1'] = Convolution(self.params['W1'], self.params['b1'],
                                        conv_param['stride'], conv_param['pad'])
    self.layers['Relu1'] = Relu()
    self.layers['Pool1'] = Pooling(pool_h=2, pool_w=2, stride=2)
    self.layers['Affine1'] = Affine(self.params['W2'], self.params['b2'])
    self.layers['Relu2'] = Relu()
    self.layers['Affine2'] = Affine(self.params['W3'], self.params['b3'])

    self.last_layer = SoftmaxWithLoss()
```
- `OrderedDict()` : 순서 있는 딕셔너리에 계층 차례로 추가
- [[Softmax-with-Loss 계층]] -> `last_layer` 별도 [[변수]] 에 저장

### 추론 & 손실
```python
# 추론 수행
def predict(self, x):
    for layer in self.layers.values():
        x = layer.forward(x)
    return x

# 손실함수 값 구하기
def loss(self, x, t):
    y = self.predict(x)
    return self.last_layer.forward(y, t)
```
- `x` : 입력 [[데이터]] / `t` : [[정답 레이블]]
- `predict` : 각 계층 `forward` 호출 -> 다음 계층 전달
- `loss` : 첫 계층 ~ 마지막 계층까지 [[순전파]] 처리

### 기울기
```python
# 오차역전파법으로 기울기 구하기
def gradient(self, x, t):
        # 순전파
        self.loss(x, t)

        # 역전파
        dout = 1
        dout = self.last_layer.backward(dout) # 마지막 출력층부터

        layers = list(self.layers.values())
        layers.reverse() # 반대로 돌면서
        for layer in layers:
            dout = layer.backward(dout) # 역전파 실행

        # 결과 저장
        grads = {}
        grads['W1'] = self.layers['Conv1'].dW
        grads['b1'] = self.layers['Conv1'].db
        grads['W2'] = self.layers['Affine1'].dW
        grads['b2'] = self.layers['Affine1'].db
        grads['W3'] = self.layers['Affine2'].dW
        grads['b3'] = self.layers['Affine2'].db

        return grads
```
- [[오차역전파법]] -> [[순전파]] / [[역전파]] 반복 호출

### 학습
```python
# 데이터 읽기
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=False)

# 시간이 오래 걸릴 경우 데이터를 줄인다.
#x_train, t_train = x_train[:5000], t_train[:5000]
#x_test, t_test = x_test[:1000], t_test[:1000]

max_epochs = 20

network = SimpleConvNet(input_dim=(1,28,28), 
                        conv_param = {'filter_num': 30, 'filter_size': 5, 'pad': 0, 'stride': 1},
                        hidden_size=100, output_size=10, weight_init_std=0.01)
                        
trainer = Trainer(network, x_train, t_train, x_test, t_test,
                  epochs=max_epochs, mini_batch_size=100,
                  optimizer='Adam', optimizer_param={'lr': 0.001},
                  evaluate_sample_num_per_epoch=1000)
trainer.train()

# 매개변수 보존
network.save_params("params.pkl")
print("Saved Network Parameters!")

# 그래프 그리기
markers = {'train': 'o', 'test': 's'}
x = np.arange(max_epochs)
plt.plot(x, trainer.train_acc_list, marker='o', label='train', markevery=2)
plt.plot(x, trainer.test_acc_list, marker='s', label='test', markevery=2)
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()
```
- [[훈련 데이터]] 정확도 ==99.82%==
- [[시험 데이터]] 정확도 ==98.96%==
- 작은 [[신경망]] 대비 정확도 ↑
