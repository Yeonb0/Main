---
aliases:
  - 네거티브 샘플링 손실 계층
  - NegativeSamplingLoss(네거티브 샘플링 손실 계층)
---

- [[네거티브 샘플링]] 손실 계산 계층
- [[Embedding Dot 계층]] + [[Sigmoid with Loss 계층]] 을 `sample_size + 1` 개씩 보관

### 초기화
```python
class NegativeSamplingLoss:
    def __init__(self, W, corpus, power=0.75, sample_size=5):
        self.sample_size = sample_size
        self.sampler = UnigramSampler(corpus, power, sample_size)
        self.loss_layers = [SigmoidWithLoss() for _ in range(sample_size + 1)]
        self.embed_dot_layers = [EmbeddingDot(W) for _ in range(sample_size + 1)]
        self.params, self.grads = [], []
        for layer in self.embed_dot_layers:
            self.params += layer.params
            self.grads += layer.grads
```
- 인수
	- `W` : 출력 측 [[가중치]]
	- `corpus` : 단어 ID 리스트
	- `power` : 확률분포에 제곱할 값
	- `sample_size` : 부정적 예 샘플링 횟수
- `loss_layers` / `embed_dot_layers` : 계층 리스트 보관
	- 계층 수 = `sample_size` + 1 (부정적 예 `sample_size` 개 + 긍정적 예 1개 -> ==0번째== 계층)
- 샘플러 : [[UnigramSampler]]

### [[순전파]]
```python
    def forward(self, h, target):
        batch_size = target.shape[0]
        negative_sample = self.sampler.get_negative_sample(target)

        # 정답(positive sample) 계산
        score = self.embed_dot_layers[0].forward(h, target)
        correct_label = np.ones(batch_size, dtype=np.int32)
        loss = self.loss_layers[0].forward(score, correct_label)

        # 부정적 예(negative sample) 계산
        negative_label = np.zeros(batch_size, dtype=np.int32)
        for i in range(self.sample_size):
            negative_target = negative_sample[:, i]
            score = self.embed_dot_layers[i + 1].forward(h, negative_target)
            loss += self.loss_layers[i + 1].forward(score, negative_label)

        return loss
```
- `h` : 은닉층 [[뉴런]] / `target` : 긍정적 예 -> 정답 타깃
1. `sampler` 로 부정적 예 샘플링 -> `negative_sample` 저장
2. 긍정적 예 / 부정적 예 각각 [[Embedding Dot 계층]] `forward`
3. 점수 & [[정답 레이블]] -> [[Sigmoid with Loss 계층]] -> 손실 합산

### [[역전파]]
```python
    def backward(self, dout=1):
        dh = 0

        for l0, l1 in zip(self.loss_layers, self.embed_dot_layers):
            dscore = l0.backward(dout)
            dh += l1.backward(dscore)

        return dh
```
- 순전파의 역순으로 각 계층 `backward()` 호출
- 은닉층 뉴런 -> 순전파 시 여러 개로 복사 -> 역전파 시 [[기울기]] 합산
