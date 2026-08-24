---
aliases:
  - skip-gram
  - 스킵그램
  - skip-gram 모델(스킵그램)
---

- [[머신러닝/word2vec]] 의 또 다른 모델
- [[CBOW 모델]] 에서 맥락과 타깃이 역전된 형태
- 타깃 -> 맥락 추측

![[word2vec-28.png]]

### 구조
![[word2vec-29.png]]
- 입력층 ==1== 개 (타깃)
- [[출력층]] : 맥락 수만큼 존재

### 확률 표기
$$
P(w_{t-1}w_{t+1}|w_t)
$$

- $w_t$ 주어졌을 때 $w_{t-1}, w_{t+1}$ 가 동시에 일어날 확률
- $w_{t-1}, w_{t+1}$ 조건부 독립 (관련성 X) 가정

$$
P(w_{t-1},w_{t+1}|w_t) = P(w_{t-1}|w_{t})P(w_{t+1}|w_{t})
$$

### 손실 함수
- [[교차 엔트로피 오차]] 적용 -> 유도

$$
\begin{aligned}
L &= -\log P(w_{t-1}, w_{t+1} \mid w_t) \\
&= -\log P(w_{t-1} \mid w_t)\, P(w_{t+1} \mid w_t) \\
&= -(\log P(w_{t-1} \mid w_t) + \log P(w_{t+1} \mid w_t))
\end{aligned}
$$

- [[말뭉치]] 전체로 확장

$$
\begin{aligned}
L = -\frac{1}{T} \sum_{t=1}^{T} \left( \log P(w_{t-1} \mid w_t) + \log P(w_{t+1} \mid w_t) \right)
\end{aligned}
$$

### CBOW 와 비교
| 항목 | 우세 모델 |
| --- | --- |
| [[단어의 분산 표현]] 정밀도 | skip-gram |
| 학습 속도 | [[CBOW 모델\|CBOW]] |

### 구현
```python
# coding: utf-8
import sys
sys.path.append('..')
import numpy as np
from common.layers import MatMul, SoftmaxWithLoss

class SimpleSkipGram:
    def __init__(self, vocab_size, hidden_size):
        V, H = vocab_size, hidden_size

        # 가중치 초기화
        W_in = 0.01 * np.random.randn(V, H).astype('f')
        W_out = 0.01 * np.random.randn(H, V).astype('f')

        # 계층 생성
        self.in_layer = MatMul(W_in)
        self.out_layer = MatMul(W_out)
        self.loss_layer1 = SoftmaxWithLoss()
        self.loss_layer2 = SoftmaxWithLoss()

        # 모든 가중치와 기울기를 리스트에 모은다.
        layers = [self.in_layer, self.out_layer]
        self.params, self.grads = [], []
        for layer in layers:
            self.params += layer.params
            self.grads += layer.grads

        # 인스턴스 변수에 단어의 분산 표현을 저장한다.
        self.word_vecs = W_in

    def forward(self, contexts, target):
        h = self.in_layer.forward(target)
        s = self.out_layer.forward(h)
        l1 = self.loss_layer1.forward(s, contexts[:, 0])
        l2 = self.loss_layer2.forward(s, contexts[:, 1])
        loss = l1 + l2
        return loss

    def backward(self, dout=1):
        dl1 = self.loss_layer1.backward(dout)
        dl2 = self.loss_layer2.backward(dout)
        ds = dl1 + dl2
        dh = self.out_layer.backward(ds)
        self.in_layer.backward(dh)
        return None
```
- 출력층 수만큼 [[Softmax-with-Loss 계층]] 생성 -> [[손실 함수|손실]] 합산
