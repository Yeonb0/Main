---
aliases:
  - 단순 CBOW
  - SimpleCBOW(단순 CBOW)
---

- [[CBOW 모델]] 을 구현한 [[클래스]]
- [[계층 구현 규칙]] 준수 -> `params` · `grads` 보유 -> [[Trainer]] 로 학습 O

![[word2vec-23.png]]

### 초기화 메소드
```python
import sys
sys.path.append('../')
import numpy as np
from common.layers import MatMul, SoftmaxWithLoss

class SimpleCBOW:
    def __init__(self, vocab_size, hidden_size):
        V, H = vocab_size, hidden_size

        # 가중치 초기화
        W_in = 0.01 * np.random.randn(V, H).astype('f')
        W_out = 0.01 * np.random.randn(H, V).astype('f')

        # 계층 생성
        self.in_layer0 = MatMul(W_in)
        self.in_layer1 = MatMul(W_in)
        self.out_layer = MatMul(W_out)
        self.loss_layer = SoftmaxWithLoss()

        # 모든 가중치와 기울기를 리스트에 모은다.
        layers = [self.in_layer0, self.in_layer1, self.out_layer]
        self.params, self.grads = [], []
        for layer in layers:
            self.params += layer.params
            self.grads += layer.grads

        # 인스턴스 변수에 단어의 분산 표현 저장
        self.word_vecs = W_in
```

| 인수 | 내용 |
| --- | --- |
| `vocab_size` | 어휘 수 |
| `hidden_size` | 은닉층 [[뉴런]] 수 |

- [[가중치]] 초기화
	- `W_in` · `W_out` 2 종류 생성 & 무작위 값 초기화
	- `astype('f')` -> ==32 bit== fp 설정
- 계층 생성
	- 입력 측 [[MatMul 노드|MatMul]] : 맥락 단어 수 ([[윈도우 크기]]) 만큼
		- 입력 측 계층 모두 같은 [[가중치]] 공유
	- 출력 측 [[MatMul 노드|MatMul]] 1개
	- [[Softmax-with-Loss 계층]] 1개
- 모든 [[가중치]] · [[기울기]] 를 `params` , `grads` 에 수집

### 순전파 메소드
```python
    def forward(self, contexts, target):
        h0 = self.in_layer0.forward(contexts[:, 0, :])
        h1 = self.in_layer1.forward(contexts[:, 1, :])
        h = (h0 + h1) * 0.5
        score = self.out_layer.forward(h)
        loss = self.loss_layer.forward(score, target)
        return loss
```

| 인수 · 반환 | 내용 |
| --- | --- |
| `contexts` | 맥락 -> 3차원 (선택 단어 수 × window_size × 원핫 벡터) |
| `target` | 타깃 -> 2차원 (선택 단어 수 × 원핫 벡터) |
| `loss` | [[손실 함수\|손실]] |

### 역전파 메소드
![[word2vec-24.png]]
- `×` : [[순전파]] 입력 서로 바꿔 [[기울기]] 에 곱함
- `+` : [[기울기]] 그대로 통과

```python
    def backward(self, dout=1):
        ds = self.loss_layer.backward(dout)
        da = self.out_layer.backward(ds)
        da *= 0.5
        self.in_layer1.backward(da)
        self.in_layer0.backward(da)
        return None
```
- `forward()` -> `backward()` 실행만으로 리스트 [[기울기]] 갱신

### 학습
```python
import sys
sys.path.append('../')
from common.trainer import Trainer
from common.optimizer import Adam
from common.util import preprocess, create_contexts_target, convert_one_hot

window_size = 1
hidden_size = 5
batch_size = 3
max_epoch = 1000

text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocess(text)

vocab_size = len(word_to_id)
contexts, target = create_contexts_target(corpus, window_size)
target = convert_one_hot(target, vocab_size)
contexts = convert_one_hot(contexts, vocab_size)

model = SimpleCBOW(vocab_size, hidden_size)
optimizer = Adam()
trainer = Trainer(model, optimizer)

trainer.fit(contexts, target, max_epoch, batch_size)
trainer.plot()
```

> [!note]- 실행 결과
> ![[word2vec-25.png]]

- 학습 진행 -> [[손실 함수|손실]] ↓

```python
word_vecs = model.word_vecs
for word_id, word in id_to_word.items():
    print(f"{word}: {word_vecs[word_id]}")
```

> [!note]- 실행 결과
> ![[word2vec-26.png]]

- 학습 종료 후 [[가중치]] -> 단어를 [[밀집벡터]] 로 표현 O
