---
aliases:
  - Softmax-with-Loss Layer
  - 소프트맥스 손실 계층
  - Softmax-with-Loss 계층(Softmax-with-Loss Layer)
---

- [[소프트맥스 함수 1]] + [[교차 엔트로피 오차]] 를 묶은 계층
- 학습 시 필요, 추론 시 불필요

### 배경
![[오차역전파법-28.png]]
- 입력 이미지 -> [[Affine 계층]] & [[ReLU 계층]] 통과 변환
- 마지막 Softmax 계층 -> 10개 입력 [[정규화]]
- 점수 -> 확률로 변환

### 구조
![[오차역전파법-29.png]]
![[오차역전파법-30.png]]
- 아래쪽 = 간소화 버전
- `Softmax` 계층
	- [[순전파]] 입력 : $(a_1, a_2, a_3)$ -> 출력 : $(y_1, y_2, y_3)$
	- [[역전파]] 출력 : $(y_1 - t_1, y_2 - t_2, y_3 - t_3)$
		- 출력 - [[정답 레이블]] = 오차 그대로 전파
- `Cross Entropy Error` 계층
	- [[순전파]] 입력 : $(y_1, y_2, y_3)$ , [[정답 레이블]] $(t_1, t_2, t_3)$
	- 출력 : [[손실 함수|손실]] $L$

### 특징
- ==ex)== 정답 (0, 1, 0) / 출력 (0.3, 0.2, 0.5) -> 역전파 (0.3, -0.8, 0.5) : 오차 ↑
- ==ex)== 정답 (0, 1, 0) / 출력 (0.01, 0.99, 0) -> 역전파 (0.01, -0.01, 0) : 오차 ↓
- 오차 크기에 비례해 학습 정도 변화

### 구현
```python
class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None  # softmax의 출력
        self.t = None  # 정답 레이블(one-hot vector)

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)

        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx
```
- [[역전파]] 시 전파 값을 [[배치 처리|배치]] 수 `batch_size` 로 나눔 -> [[데이터]] 1개당 오차 전달
