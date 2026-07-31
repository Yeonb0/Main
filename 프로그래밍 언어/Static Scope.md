---
aliases:
  - 정적 스코프
  - Static Scope(정적 스코프)
---

- 대부분의 언어가 사용하는 [[Scope]] 결정 방식
- 계층적 구조 - [[Scope|scope]] 가 nest 된 구조

![[Names,-Bindings,-Type-Checking,-and-Scop-01.png]]

### 규칙
- Static Scoping rule : 내 지역 안에서 [[Searching|탐색]] -> 없으면 더 밖의 영역 탐색
	- ==ex)== 서강대 -> 대흥동 -> 마포구 -> 서울 -> 한국 -> global 순 탐색
- compile time 에 결정

### 특징
- procedure 아니어도 `{}` 통해 nest O
- nested subprogram O (Ada, [[JavaScript]], Fortran, F#, [[Python]])
	- [[함수]] 내부에 함수 선언
- static parent : 구조적으로 외부에 있는 함수
	- ==ex)== `sub1` 의 static parent 는 `big`

### 단점
- too much access
- 잘못된 함수 호출 compiler 가 잡지 못함
	- visible 하면 안 되는 것들이 보임

![[Names,-Bindings,-Type-Checking,-and-Scop-02.png]]

### 구현
- nonlocal [[변수]] 접근 규칙 -> [[Nested Subprograms]]
- static link 는 [[Activation Record]] 안에 저장
- [[Static Chain]] : ancestor 를 link 로 연결해 탐색
- [[Display]] : 접근 가능한 record 주소를 [[배열]]에 모아 저장
