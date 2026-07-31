---
aliases:
  - 중첩 서브프로그램
  - 중첩 서브프로그램(Nested Subprograms)
---

- subprogram 안에 subprogram 선언 -> nonlocal [[변수]] 접근 메커니즘 필요
- nonlocal 변수 -> [[stack|stack]] 어딘가의 [[Activation Record]] 안에 존재

### 참조 절차
1. 해당 변수가 할당된 [[함수]]의 record 를 stack 에서 찾기
2. 변수의 local_offset 사용 -> 접근

### [[Static Scope|Static-scoped]] 언어의 semantic rule
- subprogram 에서 static ancestor [[Scope|scope]] 에 선언된 변수만 nonlocal 접근 O
- static ancestor 의 변수는 참조 시 stack 위에 반드시 존재
	- 자신의 모든 static ancestor 가 active 해야 호출 O
- 가장 close 한 nest 부터 바깥으로 [[Searching|탐색]] -> 처음 발견되는 것

### 구현 방법
- [[Static Chain]]
- [[Display]]
