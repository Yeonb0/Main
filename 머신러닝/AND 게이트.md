---
aliases:
  - AND Gate
  - AND 게이트(AND Gate)
source: 퍼셉트론.md
created: 2026-07-30
---

- 2 input & 1 output 논리 회로
- 두 입력이 모두 1 일 때만 1 출력, 그 이외에는 0 출력

### 진리표
| $x_1$ | $x_2$ | $y$ |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### 구현
- $w_1$, $w_2$, $\theta$ 조합 무수히 많음
	- ==ex)== (0.5, 0.5, 0.7), (0.5, 0.5, 0.8), (1.0, 1.0, 1.0)

```python
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7 # 매개변수 (가중치, 임곗값)
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    else:
        return 1
```

![[퍼셉트론-03.png]]

- [[가중치]] & [[편향]] 형태

```python
def AND(x1, x2):
    x = np.array([x1, x2])       # 입력
    w = np.array([0.5, 0.5])     # 가중치
    b = -0.7                     # 편향
    tmp = np.sum(w * x) + b      
    if tmp <= 0:
        return 0
    else:
        return 1
```
