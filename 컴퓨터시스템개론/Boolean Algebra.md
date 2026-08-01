---
aliases:
  - 불 대수
  - Boolean Algebra(불 대수)
---

- [[boolean]] 값 True = 1 / False = 0 으로 두고 수행하는 [[연산]] 체계
- [[CPU]] 는 기본적으로 [[게이트]] 로 구성 -> 게이트 = Boolean operation 실행하는 회로

### 연산
#### And (&)
- 둘 다 1일 때만 1

| & | 0 | 1 |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |

#### Or (|)
- 하나라도 1이면 1

| \| | 0 | 1 |
| --- | --- | --- |
| 0 | 0 | 1 |
| 1 | 1 | 1 |

#### Not (~)
- 0 ↔ 1 바꾸기

| ~ |  |
| --- | --- |
| 0 | 1 |
| 1 | 0 |

#### Xor (^)
- A ≠ B 면 1

| ^ | 0 | 1 |
| --- | --- | --- |
| 0 | 0 | 1 |
| 1 | 1 | 0 |

### 성질
- Commutative property (교환 법칙) 성립
	- ==ex)== A & B = B & A
- Associative property (결합 법칙) 성립
	- ==ex)== A & (B & C) = (A & B) & C
- bit sequence (= bit vector) 로 확장 O -> [[비트 연산]]
