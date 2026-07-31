---
aliases:
  - 정적 체인
  - 정적 체인(Static Chain)
---

- [[stack|Stack]] 내의 특정 [[함수]]들을 연결하는 static link 의 chain
- subprogram 의 ancestor 를 부모부터 순서대로 연결
- nonlocal 참조 발생 -> [[변수]]가 있는 함수 찾을 때까지 chain [[Searching|탐색]]
- scope nest 는 [[컴파일|compile]] 시점 파악 O -> nonlocal 참조 여부 & 필요한 chain 길이 결정 O

### Static_depth
- 가장 바깥 [[Scope|scope]] 로부터의 중첩 깊이

### Nesting_depth (chain_offset)
- nonlocal 참조에 도달하기 위해 필요한 static chain 길이
- `nonlocal 사용 static_depth - nonlocal 선언 static_depth`
- ==ex)==
```pascal
program A ;
  procedure B ;
    procedure C ;
    end; { of procedure C }
  end; { of procedure B)
end ;
```
	- static_depth : `A(0)`, `B(1)`, `C(2)`
	- chain_offset : C 가 A 변수 참조 -> `2 - 0 = 2`

### 예시
```pascal
MAIN_2
  var X : integer
  BIGSUB
    var A, B, C : integer ;
    SUB1
      var A, D : integer ;
      A : = B + C ;
    var B, E : integer ;
    SUB2
      SUB3
        var C, E : integer ;
        SUB1 ;
        E := B + A ;
      ....
      SUB3 ;
      ....
    A := D + E ;
  SUB2 ;
BIGSUB ;
```
- 호출 순서 : `MAIN_2` -> `BIGSUB` -> `SUB2` -> `SUB3` -> `SUB1`
- static_depth : `MAIN_2` 0, `BIGSUB` 1, `SUB2` 2, `SUB3` 3, `SUB1` 2
- SUB1 의 `A := B + C`
	- `A` : SUB1 의 지역 변수 -> chain_offset `0`
	- `B`, `C` : BIGSUB 에 선언 -> chain_offset `1` (static link 1번 이동)
- SUB3 의 `E := B + A`
	- `E` : SUB3 의 지역 변수 -> chain_offset `0`
	- `B` : SUB2 에 선언 -> chain_offset `1`
	- `A` : BIGSUB 에 선언 -> chain_offset `2`

### 유지 방법
- subprogram 반환 시 : stack 에서 제거 -> 추가 작업 X
- subroutine 호출 시 : 호출 시점 parent 의 가장 최근 [[Activation Record]] 찾아야 함
	1. run time 에 dynamic chain 따라가며 탐색
	2. compile time 에 caller ↔ callee 의 nesting_depth 계산 -> call time 에 caller 의 static chain 을 nesting_depth 만큼 내려가 static link 결정

### 단점
- static parent 넘은 scope 의 변수 참조 costly
	- 선언에 도달하려면 link 한 칸씩 따라가야 함
- nonlocal 참조 비용 예측 어려움
