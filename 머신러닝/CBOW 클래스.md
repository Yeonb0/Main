---
aliases:
  - CBOW Class
  - CBOW 클래스(CBOW Class)
---

- [[Embedding 계층]] & [[네거티브 샘플링]] 적용한 [[CBOW 모델]] 개선 구현
- [[SimpleCBOW]] 개선판 -> 큰 [[말뭉치]] 학습 O

### 초기화
```python
class CBOW:
    def __init__(self, vocab_size, hidden_size, window_size, corpus):
        V, H = vocab_size, hidden_size

        # 가중치 초기화
        W_in = 0.01 * np.random.randn(V, H).astype('f')
        W_out = 0.01 * np.random.randn(V, H).astype('f')

        # 계층 생성
        self.in_layers = []
        for i in range(2 * window_size):
            layer = Embedding(W_in) # Embedding 계층 사용
            self.in_layers.append(layer)
        self.ns_loss = NegativeSamplingLoss(W_out, corpus, power=0.75, sample_size=5)

        # 인스턴스 변수 저장
        layers = self.in_layers + [self.ns_loss]
        self.params, self.grads = [], []
        for layer in layers:
            self.params += layer.params
            self.grads += layer.grads

        # 인스턴스 변수에 단어의 분산 표현 저장.
        self.word_vecs = W_in
```

| 인수 | 내용 |
| --- | --- |
| `vocab_size` | 어휘 수 |
| `hidden_size` | 은닉층 [[뉴런]] 수 |
| `window_size` | 맥락의 크기 (주변 어디까지 맥락) |
| `corpus` | 단어 ID 목록 |

- [[Embedding 계층]] `window_size` × 2 개 -> `in_layers` [[배열]] 보관
- [[NegativeSamplingLoss]] 계층 생성
- `params` 에 [[가중치]] & [[편향]] / `grads` 에 [[기울기]]
- `word_vecs` 에 `W_in` 할당 -> [[단어의 분산 표현]] 접근

### 순전파 & 역전파
```python
    def forward(self, contexts, target):
        h = 0
        for i, layer in enumerate(self.in_layers):
            h += layer.forward(contexts[:, i])
        h *= 1 / len(self.in_layers)

        loss = self.ns_loss.forward(h, target)
        return loss

    def backward(self, dout=1):
        dout = self.ns_loss.backward(dout)
        dout *= 1 / len(self.in_layers)

        for layer in self.in_layers:
            layer.backward(dout)

        return None
```
- 각 계층 `forward` / `backward` 순서대로 호출
- `forward(contexts, target)` 인수 = 단어 ID (원핫 벡터 X)
![[word2vec-속도-개선-25.png]]

### 학습
```python
import numpy as np
import sys
from common import config

config.GPU = True

import pickle
from common.trainer import Trainer
from common.optimizer import Adam
from common.util import create_contexts_target, to_cpu, to_gpu
from dataset import ptb

# 하이퍼파라미터 설정
window_size = 5
hidden_size = 100
batch_size = 100
max_epoch = 10

# 데이터 읽기
corpus, word_to_id, id_to_word = ptb.load_data('train')
vocab_size = len(word_to_id)

contexts, target = create_contexts_target(corpus, window_size)
if config.GPU:
    contexts, target = to_gpu(contexts), to_gpu(target)

# 모델 등 생성
model = CBOW(vocab_size, hidden_size, window_size, corpus)
optimizer = Adam()
trainer = Trainer(model, optimizer)

# 학습 시작
trainer.fit(contexts, target, max_epoch, batch_size)
trainer.plot()  # 학습 경과 그래프 그리기

# 나중에 사용할 수 있도록 필요한 데이터 저장
word_vecs = model.word_vecs
if config.GPU:
    word_vecs = to_cpu(word_vecs)
params = {}
params['word_vecs'] = word_vecs.astype(np.float16)
params['word_to_id'] = word_to_id
params['id_to_word'] = id_to_word
pkl_file = 'cbow_params.pkl'
with open(pkl_file, 'wb') as f:
    pickle.dump(params, f, -1)
```
- [[PTB 데이터셋]] 사용, [[Adam]] 최적화
- 윈도우 크기 ==5==, 은닉층 뉴런 ==100개==
	- 보통 윈도우 크기 ==2 ~ 10== / 은닉층 뉴런 수 ==50 ~ 500==
- [[CPU]] 학습 시간 반나절 -> [[CuPy|GPU]] 모드 권장

> [!note]- 실행 결과
> ![[word2vec-속도-개선-26.png]]
> ![[word2vec-속도-개선-27.png]]

- 학습 완료 매개변수 -> `cbow_params.pkl` 저장

### 평가
```python
import common.util as util
from common.util import most_similar
import pickle

util.np = numpy

pkl_file = 'cbow_params.pkl'

with open(pkl_file, 'rb') as f:
    params = pickle.load(f)
    word_vecs = params['word_vecs']
    word_to_id = params['word_to_id']
    id_to_word = params['id_to_word']

querys = ['you', 'year', 'car', 'toyota']
for query in querys:
    most_similar(query, word_to_id, id_to_word, word_vecs, top=5)
```

> [!note]- 실행 결과
> ![[word2vec-속도-개선-28.png]]

- `most_similar()` -> [[코사인 유사도]] 상위 단어 확인
- 확장 평가 : [[유추 문제]]
