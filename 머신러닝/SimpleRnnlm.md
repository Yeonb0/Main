---
aliases:
  - 단순 RNNLM
  - SimpleRnnlm(단순 RNNLM)
---

- [[RNNLM]] 을 구현한 [[클래스]]
- [[계층 구현 규칙]] 준수 -> `params` · `grads` 보유

### 구조
![[순환-신경망-(RNN)-25.png]]
- 4개 [[Time 계층]] 을 쌓은 [[머신러닝/신경망|신경망]]
- `TimeEmbedding` -> [[Time RNN 계층|TimeRNN]] -> `TimeAffine` -> `TimeSoftmaxWithLoss`

### 초기화
```python
import sys
sys.path.append('..')
import numpy as np
from common.time_layers import *

class SimpleRnnlm:
    def __init__(self, vocab_size, wordvec_size, hidden_size):
        V, D, H = vocab_size, wordvec_size, hidden_size
        rn = np.random.randn

        # 가중치 초기화
        embed_W = (rn(V, D) / 100).astype('f')
        rnn_Wx = (rn(D, H) / np.sqrt(D)).astype('f')
        rnn_Wh = (rn(H, H) / np.sqrt(H)).astype('f')
        rnn_b = np.zeros(H).astype('f')
        affine_W = (rn(H, V) / np.sqrt(H)).astype('f')
        affine_b = np.zeros(V).astype('f')

        # 계층 생성
        self.layers = [
            TimeEmbedding(embed_W),
            TimeRNN(rnn_Wx, rnn_Wh, rnn_b, stateful=True),
            TimeAffine(affine_W, affine_b)
        ]
        self.loss_layer = TimeSoftmaxWithLoss()
        self.rnn_layer = self.layers[1]

        # 모든 가중치와 기울기를 리스트에 모은다.
        self.params, self.grads = [], []
        for layer in self.layers:
            self.params += layer.params
            self.grads += layer.grads
```
- `stateful=True` -> 이전 시각 [[은닉 상태]] 계승 O
- [[RNN 계층]] · [[Affine 계층]] [[가중치]] -> Xavier 초깃값 사용
	- 이전 계층 [[뉴런|노드]] $n$ 개 -> 표준편차 $\frac{1}{\sqrt{n}}$ 분포로 초기화
	- -> [[가중치 초깃값]]

![[순환-신경망-(RNN)-26.png]]

### 순전파 & 역전파
```python
    def forward(self, xs, ts):
        for layer in self.layers:
            xs = layer.forward(xs)
        loss = self.loss_layer.forward(xs, ts)
        return loss

    def backward(self, dout=1):
        dout = self.loss_layer.backward(dout)
        for layer in reversed(self.layers):
            dout = layer.backward(dout)
        return dout

    def reset_state(self):
        self.rnn_layer.reset_state()
```
- 각 계층 `forward()` / `backward()` 를 순서대로 호출
- `reset_state()` : [[머신러닝/신경망|신경망]] [[state|상태]] 초기화

### 학습 준비
```python
import sys
sys.path.append('..')
import numpy as np
import matplotlib.pyplot as plt
from common.optimizer import SGD
from dataset import ptb

# 하이퍼파라미터 설정
batch_size = 10
wordvec_size = 100
hidden_size = 100  # RNN 의 은닉 상태 벡터의 원소 수
time_size = 5      # Truncated BPTT 가 한 번에 펼치는 시간 크기
lr = 0.1
max_epoch = 100

# 학습 데이터 읽기 (전체 중 1000개만)
corpus, word_to_id, id_to_word = ptb.load_data('train')
corpus_size = 1000
corpus = corpus[:corpus_size]
vocab_size = int(max(corpus) + 1)

xs = corpus[:-1]  # 입력
ts = corpus[1:]   # 출력 (정답 레이블)
data_size = len(xs)
print('말뭉치 크기: %d, 어휘 수: %d' % (corpus_size, vocab_size))

# 학습 시 사용하는 변수
max_iters = data_size // (batch_size * time_size)
time_idx = 0
total_loss = 0
loss_count = 0
ppl_list = []

# 모델 생성
model = SimpleRnnlm(vocab_size, wordvec_size, hidden_size)
optimizer = SGD(lr)
```
- [[PTB 데이터셋]] 앞 ==1000개== 단어만 사용

### 학습
```python
# 1. 각 미니배치에서 샘플 읽기 시작 위치 계산
jump = (corpus_size - 1) // batch_size
offset = [i * jump for i in range(batch_size)]

for epoch in range(max_epoch):
    for iter in range(max_iters):
        # 2. 미니배치 획득
        batch_x = np.empty((batch_size, time_size), dtype='i')
        batch_t = np.empty((batch_size, time_size), dtype='i')

        for t in range(time_size):
            for i, offset_i in enumerate(offset):
                batch_x[i, t] = xs[(offset_i + time_idx) % data_size]
                batch_t[i, t] = ts[(offset_i + time_idx) % data_size]
            time_idx += 1

        # 기울기 구하면서 매개변수 갱신
        loss = model.forward(batch_x, batch_t)
        model.backward()
        optimizer.update(model.params, model.grads)
        total_loss += loss
        loss_count += 1

    # 에폭마다 perplexity 계산
    ppl = np.exp(total_loss / loss_count)
    print('| 에폭 %d | 퍼플렉서티 %.2f' % (epoch + 1, ppl))
    ppl_list.append(float(ppl))
    total_loss, loss_count = 0, 0
```
1. 각 [[미니배치 학습|미니배치]] 의 [[데이터]] 읽기 시작 위치 정렬 -> `offset`
2. `time_idx` 증가시키며 [[말뭉치]] 에서 순차적으로 데이터 획득
3. [[에포크]] 마다 [[퍼플렉서티]] 계산

> [!note]- 실행 결과
> ![[순환-신경망-(RNN)-27.png]]
> ![[순환-신경망-(RNN)-28.png]]

- 학습 반복 -> [[퍼플렉서티]] ↓

### 한계
- 큰 [[말뭉치]] 대응 X
- 학습 루프 [[캡슐화]] -> [[RnnlmTrainer]]
