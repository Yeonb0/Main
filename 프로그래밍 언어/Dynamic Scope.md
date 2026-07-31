---
aliases:
  - 동적 스코프
  - Dynamic Scope(동적 스코프)
---

- [[변수]]의 [[Scope]] 를 subprogram 의 호출 순서 기반으로 결정
- run time 에 결정 -> 자신을 호출한 [[함수]]의 scope [[Searching|탐색]]
- 거의 사용되지 않는 방식

![[Names,-Bindings,-Type-Checking,-and-Scop-01.png]]

### 특징
- dynamic parent : 함수를 실제로 호출한 함수
	- ==ex)== `sub1` 의 dynamic parent 는 `sub2`
- [[Static Scope]] 의 static parent 와 대비

### 장점
- [[매개 변수|parameter]] 넘길 필요 X

### 단점
- [[타입 검사]] 어려움
- [[Reliability|신뢰성]] ↓
