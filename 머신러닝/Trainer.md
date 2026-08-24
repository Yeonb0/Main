---
aliases:
  - 트레이너
  - Trainer(트레이너)
---

- 학습 루프를 캡슐화한 [[클래스]]
- [[머신러닝/신경망|신경망]] & optimizer 전달 -> `fit()` 호출만으로 학습 진행
- [[미니배치 학습|미니배치]] 추출 · [[기울기]] 계산 · 매개변수 갱신 반복 코드 [[재사용(Reuse)|재사용]]

### 메소드
| [[메소드]] | 역할 |
| --- | --- |
| `__init__(model, optimizer)` | [[머신러닝/신경망\|신경망]] · 최적화 기법 보관 |
| `fit(...)` | 학습 시작 -> [[에포크]] 반복 |
| `plot(ylim)` | `fit()` 이 기록한 [[손실 함수\|손실]] [[Graph\|그래프]] 출력 |

### fit 인수
| 인수 | 내용 |
| --- | --- |
| `x` | 입력 [[데이터]] |
| `t` | [[정답 레이블]] |
| `max_epoch` | 학습 수행 [[에포크]] 수 |
| `batch_size` | [[미니배치 학습\|미니배치]] 크기 |
| `eval_interval` | 결과 (평균 [[손실 함수\|손실]] 등) 출력 간격 |
| `max_grad` | [[기울기]] 최대 norm |

### 절차
1. [[에포크]] 시작마다 [[데이터]] 무작위 섞기 -> `numpy.random.permutation`
2. [[미니배치 학습|미니배치]] 잘라 `model.forward()` -> [[손실 함수|손실]] 획득
3. `model.backward()` -> [[오차역전파법]] 으로 [[기울기]] 산출
4. `remove_duplicate()` : 공유 [[가중치]] 하나로 취합
5. `clip_grads()` : `max_grad` 지정 시 [[기울기]] norm 제한
6. `optimizer.update()` -> 매개변수 갱신

### 구현
```python
class Trainer:
    def __init__(self, model, optimizer):
        self.model = model
        self.optimizer = optimizer
        self.loss_list = []
        self.eval_interval = None
        self.current_epoch = 0

    def fit(self, x, t, max_epoch=10, batch_size=32, max_grad=None, eval_interval=20):
        data_size = len(x)
        max_iters = data_size // batch_size
        self.eval_interval = eval_interval
        model, optimizer = self.model, self.optimizer
        total_loss = 0
        loss_count = 0

        start_time = time.time()
        for epoch in range(max_epoch):
            # 뒤섞기
            idx = numpy.random.permutation(numpy.arange(data_size))
            x = x[idx]
            t = t[idx]

            for iters in range(max_iters):
                batch_x = x[iters*batch_size:(iters+1)*batch_size]
                batch_t = t[iters*batch_size:(iters+1)*batch_size]

                # 기울기 구해 매개변수 갱신
                loss = model.forward(batch_x, batch_t)
                model.backward()
                params, grads = remove_duplicate(model.params, model.grads)  # 공유된 가중치를 하나로 모음
                if max_grad is not None:
                    clip_grads(grads, max_grad)
                optimizer.update(params, grads)
                total_loss += loss
                loss_count += 1

                # 평가
                if (eval_interval is not None) and (iters % eval_interval) == 0:
                    avg_loss = total_loss / loss_count
                    elapsed_time = time.time() - start_time
                    print('| 에폭 %d |  반복 %d / %d | 시간 %d[s] | 손실 %.2f'
                          % (self.current_epoch + 1, iters + 1, max_iters, elapsed_time, avg_loss))
                    self.loss_list.append(float(avg_loss))
                    total_loss, loss_count = 0, 0

            self.current_epoch += 1

    def plot(self, ylim=None):
        x = numpy.arange(len(self.loss_list))
        if ylim is not None:
            plt.ylim(*ylim)
        plt.plot(x, self.loss_list, label='train')
        plt.xlabel('반복 (x' + str(self.eval_interval) + ')')
        plt.ylabel('손실')
        plt.show()
```
- 전제 : model 이 [[계층 구현 규칙]] 준수 -> `params` · `grads` 보유
