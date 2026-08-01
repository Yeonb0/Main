---
aliases:
  - Load Effective Address
  - lea 명령어
---

- 주소 계산만 수행, [[메모리]] 접근 X 인 명령어
- [[mov]] 와 형태 비슷, 행동 상이

### 형태
- ==ex)== `lea 0x20(%rbx, %rcx, 4), %rax`
	- `%rax` = `0x20` + `%rbx` + `(%rcx * 4)`
	- `%rbx` = 0x3000, `%rcx` = 0x100 -> `%rax` = 0x3420

### 용도
- [[포인터]] 계산용 instruction
- [[산술 명령어]] 보다 빠름 -> 정수 산술 [[연산]]에도 사용

![[Assembly-Introduction-14.png]]

### [[mov]] 와 차이
| 명령어 | 동작 |
| --- | --- |
| `mov` | 주소 계산 & [[메모리]] 접근 |
| `lea` | 주소 계산만, [[메모리]] 접근 X -> 속도 빠름 |

-> arithmetic 명령어에 가까움
