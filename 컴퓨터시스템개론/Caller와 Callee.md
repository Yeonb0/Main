---
aliases:
  - 호출자와 피호출자
  - Caller
  - Callee
  - 호출자와 피호출자(Caller and Callee)
---

- [[함수]] 호출 관계에서의 두 역할
	- caller : 다른 [[함수]] 를 call 하는 쪽
	- callee : call 당하는 쪽
- 절대 구분 X, 상대적 -> 한 [[함수]] 가 caller · callee 동시에 O

![[Assembly-Function-05.png]]

### ==ex)== [[C]] code
```c
void multstore(long *dest) {
	long t = mult2(5L, 3L);
	*dest = t;
}
```
-> caller function : `mult2` call

```c
long mult2(long a, long b) {
	long s = a * b;
	return s;
}
```
-> callee function : `multstore` 에 의해 call 당함

### ==ex)== [[어셈블리 코드]]
```nasm
0000000000400536 <multstore>:
400536: push %rbx
400537: mov %rdi,%rbx
40053a: mov $0x3,%esi # Setup 2nd arg
40053f: mov $0x5,%edi # Setup 1st arg
400544: call 0x400550 <mult2> # mult2(5,3)
400549: mov %rax,(%rbx) # Update *dest
40054c: pop %rbx
40054d: ret
```

```nasm
0000000000400550 <mult2>:
400550: mov %rdi,%rax # %rax := a
400553: imul %rsi,%rax # %rax := a * b
400557: ret # Return
```

### 인수 전달
- `%esi` -> `3` : 2nd argument
- `%edi` -> `5` : 1st argument

### 레지스터 백업
- `%rbx` : 약속된 argument 값 X -> [[함수]] 가 [[백업]] & 복구 책임
	- `multstore` 가 callee 입장 -> 시작 전 · 후 값 동일
- `%rax` : [[caller-saved]], `call` 이전 값 보장 X
	- [[반환 주소]] 채워져 있다는 것만 보장
