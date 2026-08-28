---
aliases:
  - ret 명령어
  - 복귀 명령어
  - 복귀 명령어(ret)
---

- [[함수]] 종료 후 호출 지점으로 복귀하는 명령어
- `pop %rip` 와 동일

### 절차
1. [[stack]] 에서 값 pop
2. pop 된 값 ( [[반환 주소]] ) 로 jump

### ==ex)==
```nasm
0000000000400550 <mult2>:
400550: mov %rdi,%rax # %rax := a
400553: imul %rsi,%rax # %rax := a * b
400557: ret # Return
```
