---
aliases:
  - 유니그램 샘플러
  - UnigramSampler(유니그램 샘플러)
---

- [[네거티브 샘플링]] 의 부정적 예 추출 [[클래스]]
- [[말뭉치]] 단어 출현 횟수 -> 확률분포 -> 확률분포대로 샘플링

### 구현
```python
class UnigramSampler:
    def __init__(self, corpus, power, sample_size):
        self.sample_size = sample_size
        self.vocab_size = None
        self.word_p = None

        counts = collections.Counter()
        for word_id in corpus:
            counts[word_id] += 1

        vocab_size = len(counts)
        self.vocab_size = vocab_size

        self.word_p = np.zeros(vocab_size)
        for i in range(vocab_size):
            self.word_p[i] = counts[i]

        self.word_p = np.power(self.word_p, power)
        self.word_p /= np.sum(self.word_p)

    def get_negative_sample(self, target):
        batch_size = target.shape[0]

        if not GPU:
            negative_sample = np.zeros((batch_size, self.sample_size), dtype=np.int32)

            for i in range(batch_size):
                p = self.word_p.copy()
                target_idx = target[i]
                p[target_idx] = 0
                p /= p.sum()
                negative_sample[i, :] = np.random.choice(self.vocab_size, size=self.sample_size, replace=False, p=p)
        else:
            # GPU(cupy）로 계산할 때는 속도를 우선한다.
            # 부정적 예에 타깃이 포함될 수 있다.
            negative_sample = np.random.choice(self.vocab_size, size=(batch_size, self.sample_size),
                                               replace=True, p=self.word_p)

        return negative_sample
```

### 인수
| 인수 | 내용 |
| --- | --- |
| `corpus` | 단어 ID 목록 |
| `power` | 확률분포에 제곱할 값 (기본 ==0.75==) |
| `sample_size` | 부정적 예 샘플링 횟수 |

- `get_negative_sample(target)` : `target` 을 긍정적 예, 나머지를 부정적 예로 보고 샘플링
- [[CuPy|GPU]] 모드 -> 속도 우선 -> 부정적 예에 타깃 포함 가능

### 사용
==ex)==
```python
corpus = np.array([0, 1, 2, 3, 4, 1, 2, 3])
power = 0.75
sample_size = 2

sampler = UnigramSampler(corpus, power, sample_size)
target = np.array([1, 3, 0])
negative_sample = sampler.get_negative_sample(target)
print(negative_sample)
```

> [!note]- 실행 결과
> ![[word2vec-속도-개선-23.png]]
> ![[word2vec-속도-개선-24.png]]
