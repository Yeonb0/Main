---
aliases:
  - EmbeddingDot
  - Embedding Dot Layer
  - Embedding Dot 계층(EmbeddingDot)
---

- [[Embedding 계층]] + 내적(dot) 계산 묶은 계층
- 은닉층 [[뉴런]] · 타깃 단어의 출력측 [[가중치]] 행 -> 점수 스칼라
- [[네거티브 샘플링]] 의 점수 계산 담당

### 위치
![[word2vec-속도-개선-15.png]]
- 다중 분류 구성 대체
	- [[MatMul 노드]] (행렬 곱) -> dot (내적)
	- [[Softmax-with-Loss 계층]] -> [[Sigmoid with Loss 계층]]
- 은닉층 이후 처리 간단화

### 구현
```python
class EmbeddingDot:
    def __init__(self, W):
        self.embed = Embedding(W)
        self.params = self.embed.params
        self.grads = self.embed.grads
        self.cache = None

    def forward(self, h, idx):
        target_W = self.embed.forward(idx)
        out = np.sum(target_W * h, axis=1)

        self.cache = (h, target_W)
        return out

    def backward(self, dout):
        h, target_W = self.cache
        dout = dout.reshape(dout.shape[0], 1)

        dtarget_W = dout * h
        self.embed.backward(dtarget_W)
        dh = dout * target_W
        return dh
```
- [[인스턴스]] [[변수]]
	- `embed` : [[Embedding 계층]]
	- `params` : 매개변수 / `grads` : [[기울기]]
	- `cache` : [[순전파]] 시 계산 결과 유지
- `forward(h, idx)`
	- `h` : 은닉층 뉴런
	- `idx` : 단어 ID 의 [[넘파이]] [[배열]] -> [[미니배치 학습|미니배치]] 처리 가정
	- [[Embedding 계층]] `forward` 호출 -> 내적 `np.sum(target_W * h, axis=1)`

![[word2vec-속도-개선-16.png]]
- ==ex)== 0, 3, 1 번째 행 추출 -> `target_W` -> `h` 와 내적
- `backward(dout)` : [[순전파]] 의 반대 순서로 [[기울기]] 전달
