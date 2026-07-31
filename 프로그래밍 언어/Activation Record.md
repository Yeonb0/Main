---
aliases:
  - 활성 레코드
  - 활성 레코드(Activation Record)
  - ARI
---

- subprogram 한 번의 실행에 필요한 [[데이터]] 묶음
- [[stack|Stack]] 위에 dynamic 하게 생성 -> [[저장소 바인딩]] 의 stack dynamic variable
- ALGOL 계열 : local [[변수]] dynamic 할당, 재귀 O, nonlocal -> [[Static Scope|static scoping]]

### 특징
- 형식 & 크기 -> [[컴파일|compile]] 시점 파악 O
- 형식 = [[인스턴스|instance]] 의 template
- 재귀 -> 각 실행마다 formal [[매개 변수|parameter]], dynamic local, return address 복사 필요

### 구조
| 항목 | 내용 |
| --- | --- |
| Local 변수 | record 내 storage 에 [[바인딩]] |
| Static link | static parent 가리킴, nonlocal 변수 접근 시 사용 |
| Dynamic link | dynamic parent(caller) 가리킴, procedure 완료 시 stack 제거에 사용 |
| Return address | 반환 주소 |
| Actual parameter | caller 가 제공한 값 or 주소 |

![[Implementing-Subprograms-01.png]]

### Dynamic Chain
- 특정 시점에 stack 에 존재하는 dynamic link 의 집합 (call chain)
- 실행이 현 위치에 어떻게 도달했는지 dynamic history 표현
- [[Deep Access]] 의 [[Searching|탐색]] 경로

### Local_Offset
- local 변수 참조 -> record 시작으로부터의 offset 으로 표현 O
- [[컴파일|compile]] 시점 변수의 순서 · 타입 · 크기로 결정

### 예시 - 재귀 · nonlocal 참조 X
```pascal
program MAIN_1
var P : real;
procedure A(X:integer);
  var Y:boolean;
  procedure C(Q:boolean);
  begin
    P=P+1; <------------------- 3
  end
  begin
    …  <----------------------- 2
    C(Y);
    …
  end {end of procedure A}
procedure B(R:real);
  var S,T;
  begin
    …  
    A(S);
    …
  end {end of procedure B}
begin {Main_1}
  …    <----------------------- 1
  B(P);
  …
end
```
- 호출 순서 : `MAIN_1` -> `B(P)` -> `A(S)` -> `C(Y)`
	- 1
		![[Implementing-Subprograms-02.png]]
	- 2
		![[Implementing-Subprograms-03.png]]
	- 3
		![[Implementing-Subprograms-04.png]]

### 예시 - 재귀
```pascal
Program TEST
var VALUE:integer;
function FACTORIAL(N:integer);
begin  <----------------------------------- 1
  if N<=1
  then FACTORIAL:=1
  else FACTORIAL:= N*FACTORIAL(N-1);
end    <----------------------------------- 2
begin
  VALUE:=FACTORIAL(3);
  writeln("factorial 3 is:", VALUE)  <----- 3
end.
```

![[Implementing-Subprograms-05.png]]
