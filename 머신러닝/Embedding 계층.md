---
aliases:
  - Embedding Layer
  - Embedding 계층(Embedding Layer)
---

- 단어 ID 에 해당하는 [[가중치]] 행(벡터) 추출 계층
- [[단어의 분산 표현]] 저장소 역할
- 원핫 표현 × 가중치 행렬 곱 대체 -> [[머신러닝/word2vec]] 입력측 병목 해소

### 도입 배경
![[word2vec-속도-개선-03.png]]
- 어휘 ==100만 개== -> 원핫 벡터 100만 차원 -> [[MatMul 노드]] 계산 낭비
- 실제 [[연산]] = 행렬의 특정 행 추출뿐 -> 원핫 변환 & 행렬 곱 불필요

### 행 추출
```python
import numpy as np

W = np.arange(21).reshape(7,3)
print(W)
print(W[2])
print(W[5])
```

> [!note]- 실행 결과
> ![[word2vec-속도-개선-04.png]]

- 여러 행 -> [[배열]]에 행 번호 명시 ([[미니배치 학습|미니배치]] 처리 가정)

```python
idx = np.array([1, 0, 3, 0])
print(W[idx])
```

> [!note]- 실행 결과
> ![[word2vec-속도-개선-05.png]]

### [[순전파]]
```python
class Embedding:
    def __init__(self, W):
        self.params = [W]
        self.grads = [np.zeros_like(W)]
        self.idx = None

    def forward(self, idx):
        W, = self.params
        self.idx = idx
        out = W[idx]
        return out
```
- [[인스턴스]] [[변수]]
	- `params` : [[가중치]], [[편향]]
	- `grads` : [[기울기]]
	- `idx` : 추출 행의 단어 ID 배열

### [[역전파]]
![[word2vec-속도-개선-06.png]]
- 상류 [[기울기]] 그대로 통과 -> 단, 추출한 행 위치로 되돌림
- 나쁜 예 : 할당

```python
    def backward(self, dout):
        dW, = self.grads
        dW[...] = 0
        dW[self.idx] = dout # 실은 나쁜 예
        return None
```
- `idx` 원소 중복 -> 먼저 쓰인 값 덮어써짐
![[word2vec-속도-개선-07.png]]
- ==ex)== `dh[0]` 값이 0번째 idx 에 2번
- 올바른 예 : 더하기

```python
    def backward(self, dout):
        dW, = self.grads
        dW[...] = 0

        for i, word_id in enumerate(self.idx):
            dW[word_id] += dout[i]
        # 혹은
        # np.add.at(dW, self.idx, dout) -> 더 일반적

        return None
```
- 근거 : [[연쇄법칙]] -> 한 매개변수가 여러 경로에 기여 -> 각 경로 기울기의 ==합==

$$
\frac{\partial L}{\partial w_j} = \sum_{i:\ \text{input}[i]=j} \frac{\partial L}{\partial \text{output}[i]}
$$

- 할당 시 -> 중복 인덱스의 마지막 기울기만 잔존 -> 학습 부정확
- 확장 : [[Embedding Dot 계층]]
