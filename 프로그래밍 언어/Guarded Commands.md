---
aliases:
  - 가드 명령
  - 가드 명령(Guarded Commands)
---

- [[Dijkstra]] 제안 [[제어문]] 형태
- 같은 priority 조건 복수 -> non-deterministic 실행 ==(시스템이 random 선택)==
- [[병행 제어]] 시 사용

### Selection Structure
``` c
if <Boolean expression> -> <statement>
[] <Boolean expression> -> <statement>
[] ....
[] <Boolean expression> -> <statement>
fi
```
- 구조 도달 마다 모든 조건식 평가
	- 참 ==1개 이상== -> 그 중 random 실행
	- 참 ==0개== -> error 발생
- ==ex)==
``` c
if i = 0 -> sum := sum + i
[] i > j -> sum := sum + j
[] j > i -> sum := sum + i
fi
```
	- `i = 0` and `j = 1` -> 1번째 or 3번째 random 실행
	- `i = 0` and `i <> 0` -> runtime error

![[Statement-Level-Control-Structures-01.png]]

### Loop Structure
``` c
do q1 > q2 -> temp := q1; q1 := q2 ; q2 := temp ;
[] q2 > q3 -> temp := q2; q2 := q3 ; q3 := temp ;
[] q3 > q4 -> temp := q3; q3 := q4 ; q4 := temp ;
od
```
- `do ~ while` 유사
	- 모든 조건 false -> 탈출
	- 여러 조건 true -> random 하나 실행 후 재평가

![[Statement-Level-Control-Structures-02.png]]
