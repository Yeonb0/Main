---
aliases:
  - 팝
  - 팝(pop)
  - pop 명령어
---

- [[stack]] 최상단 값 꺼내 [[레지스터]] 에 담는 [[어셈블리 코드|어셈블리]] 명령어
- `pop` reg

### 절차
1. reg 에 기존 `%rsp` 가 가리키던 값 저장
2. `%rsp` + 8

### 특징
- memory 공간에는 값 그대로 잔존
	- but 더 이상 사용 X

### ==ex)== `pop %rbx`
![[Assembly-Function-04.png]]
