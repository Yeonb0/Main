---
aliases:
  - Data Move Instruction
  - mov 명령어
  - 데이터 이동 명령어
---

- 형태 : `mov Source, Destination`
- source -> destination 으로 [[데이터]] 복사

### 접미사 (Suffix)
- 이동 data 양 결정

| suffix | 크기 |
| --- | --- |
| `b` | 1 byte |
| `w` | 2 byte |
| `l` | 4 byte |
| `q` | 8 byte |

- 명확할 때 생략 O ==ex)== `mov rax rdi`

### operand type
- register
- immediate : 접두사 `$` 사용
- memory : 특정 주소의 내용 (접두사 X)
	- ==ex)== `mov 0x1000, %rbx` : `0x1000` 에 위치한 [[메모리]] 주소 load
	- ==ex)== `mov (%rax), %rbx` : `%rax` 가 point 하고 있는 주소 load

![[Assembly-Introduction-08.png]]

### 조건
- destination 이 Imm X
- Mem -> Mem X
- [[x86-64 레지스터]] 부분 접근 O

![[Assembly-Introduction-09.png]]

> [!note]- `%eax` 사용 시
> 위쪽 4 byte 를 0으로 변경
