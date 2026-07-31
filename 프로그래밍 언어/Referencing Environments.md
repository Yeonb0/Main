---
aliases:
  - 참조 환경
  - Referencing Environments(참조 환경)
---

- 어떤 statement 에서 visible 한 [[변수]]들의 집합
- [[Scope]] 규칙 따라 결정

![[Names,-Bindings,-Type-Checking,-and-Scop-03.png]]

- ==ex)==
	1. `x`, `y` -> sub1 / `a`, `b` -> example
	2. `x` -> sub3 / `a`, `b` -> example
	3. `x` -> sub2 / `a`, `b` -> example
	4. `a`, `b` -> example

### [[Subprogram]] 이름 parameter
- subprogram [[이름]]이 다른 subprogram 의 [[매개 변수]]로 전달 O
- 전달된 subprogram 실행 시 참조 환경 결정 방식 상이

| 방식 | 환경 |
| --- | --- |
| shallow binding | callee 를 call 하는 subprogram (`SUB4`), [[Dynamic Scope]] 언어에서 사용 |
| deep binding | callee 가 선언된 subprogram (`SUB1`), [[Block\|블록]] 구조(block structured) 언어에서 사용 |
| others | callee 를 actual parameter 로 전달하는 호출문 포함 subprogram (`SUB3`) |

```pascal
procedure SUB1;
    var x : integer;
    procedure SUB2;
        begin
            write('x=', x);
        end; {of SUB2}
    procedure SUB3;
        var x : integer;
        begin
            x := 3; SUB4(SUB2);
        end; {of SUB3}
    procedure SUB4(SUBX);
        var x : integer;
        begin
            x := 4; SUBX;
        end; {of SUB4}
    begin {of SUB1}
        x := 1; SUB3;
    end; {of SUB1}
```

### 확장
- subprogram + 참조 환경 묶음 -> [[Closure]]
