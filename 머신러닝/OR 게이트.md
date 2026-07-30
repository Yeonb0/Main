---
aliases:
  - OR Gate
  - OR 게이트(OR Gate)
source: 퍼셉트론.md
created: 2026-07-30
---

- 입력 [[신호]] 중 하나 이상이 1 이면 1 출력

### 진리표
| $x_1$ | $x_2$ | $y$ |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### 구현
```python
def OR(x1, x2):
    x = np.array([x1, x2])       # 입력
    w = np.array([0.5, 0.5])     # 가중치
    b = -0.2                     # 편향
    tmp = np.sum(w * x) + b      
    if tmp <= 0:
        return 0
    else:
        return 1
```

- [[AND 게이트]] & [[NAND 게이트]] & [[OR 게이트]] -> [[가중치]]와 [[편향]] 값 설정 부분만 상이
