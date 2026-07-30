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
