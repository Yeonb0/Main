---
aliases:
  - 얕은 접근
  - 얕은 접근(Shallow Access)
---

- [[Dynamic Scope]] 언어의 nonlocal 참조 구현 방식
- subprogram 내 선언 [[변수]] -> 해당 subprogram 의 [[Activation Record|ARI]] 에 저장 X
- 프로그램 전체에서 각 변수 [[이름]]마다 별도의 [[stack|stack]] 유지

### 절차
1. 어떤 이름의 변수가 subprogram 시작 시 선언 -> 해당 이름의 stack 에 cell 추가
2. 해당 이름에 대한 참조 -> stack top 변수 참조

### 특징
- 참조 fast
- subprogram 진입 & 종료 시 stack 유지 비용 costly
- [[Deep Access]] 와 대비
