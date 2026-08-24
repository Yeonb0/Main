---
aliases:
  - ReLU
  - Rectified Linear Unit
  - ReLU(Rectified Linear Unit)
source: 신경망.md
created: 2026-07-30
---

- 최근 이용되는 [[활성화 함수]]
	- 입력 0 이상 -> 그 입력 그대로 출력
	- 입력 0 이하 -> 0 출력

![[신경망-09.png]]

$$
h(x) = \begin{cases} x & (x > 0) \\ 0 & (x \leq 0) \end{cases}
$$

### 구현
```python
def relu(x):
    return np.maximum(0, x)
```
- `maximum` : 두 입력 중 큰 값 선택해 반환

### [[미분]]
$$
\frac{\partial y}{\partial x} =\begin{cases}1 & (x > 0) \\0 & (x \le 0)\end{cases}
$$

- 입력 0 초과 -> 상류 값 그대로 하류 전달 / 0 이하 -> 0 전달
- 구현 : [[ReLU 계층]]

### 사용
- [[LeNet]] -> [[시그모이드 함수]] 사용
- [[AlexNet]] -> [[ReLU 함수|ReLU]] 채택 -> 이후 [[합성곱 신경망]] 표준
- [[깊은 CNN]] -> [[활성화 함수]] 로 채택
