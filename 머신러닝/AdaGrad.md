---
aliases:
  - 아다그라드
  - AdaGrad(아다그라드)
---

- 매개변수 ==각각== 에 맞춤 [[학습률]] 부여하는 최적화 기법
- 적응적 (adaptive) 학습률 조정 -> 크게 갱신된 원소일수록 학습률 ↓

### 수식
$$
\mathbf{h} \leftarrow \mathbf{h} + \frac{\partial L}{\partial \mathbf{W}} \odot \frac{\partial L}{\partial \mathbf{W}} \\ \mathbf{W} \leftarrow \mathbf{W} - \eta \frac{1}{\sqrt{\mathbf{h}}} \frac{\partial L}{\partial \mathbf{W}}
$$

- $\text{W}$ : 갱신할 [[가중치]] 매개변수
- $\frac{\partial L}{\partial \text{W}}$ : $\text{W}$ 에 대한 [[손실 함수]] 의 [[기울기]]
- $\eta$ : [[학습률]]
- $\text{h}$ : 기존 [[기울기]] 값 제곱해 누적 ($\odot$ 은 행렬 원소별 곱셈)
	- 갱신 시 $\frac{1}{\sqrt{\mathbf{h}}}$ 곱 -> 매개변수 원소마다 학습률 감소폭 상이

### 구현
```python
class AdaGrad:
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)

        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
```
- `1e-7` 가산 : `self.h[key]` 에 ==0== 존재 시 `divideByZero` 방지

### 특징
![[학습-관련-기술들-07.png]]
- [[확률적 경사 하강법|SGD]] 보다 최솟값 향해 효율적 이동
