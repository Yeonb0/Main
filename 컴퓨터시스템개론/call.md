---
aliases:
  - call 명령어
  - 호출 명령어
  - 호출 명령어(call)
---

- [[함수]] 진입점으로 제어 흐름 이동시키는 명령어
- `call` Dest

### 절차
1. [[반환 주소]] ( `call` 명령어 다음 줄 ) [[stack]] 에 저장
2. Dest 로 jump

### ==ex)==
```nasm
0000000000400536 <multstore>:
...
400544: call 0x400550 <mult2> # mult2(5,3)
400549: mov %rax,(%rbx) # Update *dest ; *dest = t
; mul2 가 계산 한 값 (%rax) 를 %rbx 가 가리키는 메모리에 저장
```
- stack 에 `0x400544` 저장 -> `mult2` 로 이동
