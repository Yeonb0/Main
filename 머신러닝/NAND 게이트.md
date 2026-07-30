---
aliases:
  - NAND Gate
  - Not AND
  - NAND 게이트(NAND Gate)
source: 퍼셉트론.md
created: 2026-07-30
---

- Not AND -> [[AND 게이트]]와 반대되는 값 출력
- 두 입력이 모두 1 일 때만 0 출력, 그 이외에는 1 출력

### 진리표
| $x_1$ | $x_2$ | $y$ |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### 구현
- ==ex)== $(w_1, w_2, \theta)$ = (-0.5, -0.5, -0.7) -> [[AND 게이트]] 매개변수의 부호 반전

```python
def NAND(x1, x2):
    x = np.array([x1, x2])       # 입력
    w = np.array([-0.5, -0.5])   # 가중치 (AND와 반대로)
    b = 0.7                      # 편향   (AND와 반대로)
    tmp = np.sum(w * x) + b      
    if tmp <= 0:
        return 0
    else:
        return 1
```

### 특징
- 이론상 [[NAND 게이트]] 만으로 [[다층 퍼셉트론]] 구성 -> 컴퓨터 제작 가능
	- 현실적으로는 불가능
