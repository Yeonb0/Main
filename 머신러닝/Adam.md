---
aliases:
  - 아담
  - Adam(아담)
---

- [[모멘텀]] 과 [[AdaGrad]] 를 융합한 최적화 기법
- [[하이퍼 파라미터]] 의 [[편향]] 보정 수행

### 구현
```python
class Adam:
    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.m = None
        self.v = None
        self.iter = 0

    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = {}, {}
            for key, val in params.items():
                self.m[key] = np.zeros_like(val)
                self.v[key] = np.zeros_like(val)

        self.iter += 1
        lr_t = self.lr * np.sqrt(1.0 - self.beta2 ** self.iter) / (1.0 - self.beta1 ** self.iter)

        for key in params.keys():
            self.m[key] += (1 - self.beta1) * (grads[key] - self.m[key])
            self.v[key] += (1 - self.beta2) * (grads[key] ** 2 - self.v[key])
            params[key] -= lr_t * self.m[key] / (np.sqrt(self.v[key]) + 1e-7)
```
- `lr` · `beta1` · `beta2` 세 [[하이퍼 파라미터]] 설정

### 특징
![[학습-관련-기술들-08.png]]
- [[모멘텀]] 과 [[AdaGrad]] 를 합친 형태의 갱신 경로

### 사용
- [[깊은 CNN]] 최적화 기법으로 채택
