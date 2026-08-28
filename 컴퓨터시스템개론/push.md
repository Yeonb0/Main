---
aliases:
  - 푸시
  - 푸시(push)
  - push 명령어
---

- [[stack]] 최상단에 값 저장하는 [[어셈블리 코드|어셈블리]] 명령어
- `push` src
- stack 에 data 추가 -> top 에서 변화 발생

![[Assembly-Function-02.png]]

### 절차
1. `%rsp` + 8 -> stack 공간 확보
2. 확보한 공간에 src 작성

### ==ex)== `push %rax`
![[Assembly-Function-03.png]]
