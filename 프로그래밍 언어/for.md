---
aliases:
  - for 문
  - Counter-Controlled Loop
  - counter-controlled loop(for)
---

- 조건 [[변수]](loop variable) 로 반복 횟수 제어하는 [[반복문]]

### 조건 parameter
- 초기값(initial) `;` 종료값(terminal) `;` 증가값(stepsize)

### 언어별 형태
- FORTRAN Ⅳ : posttest -> ==최소 1회== 실행
``` fortran
DO 30 I=1,100,2
….
30 CONTINUE
```
- FORTRAN 77, 90 : pretest, single-entry
``` fortran
Do label variable = initial, terminal [,stepsize]
```
- [[C]] : `for` statement
``` c
for (  i = 0   ;   i <= 10   ;   i++   ) 
		   ↑ 초기값    ↑ 종료조건       ↑ 증감값
```
	- pretest -> 종료조건 0 이면 종료, 아니면 loop 실행
	- 표현식 생략 O -> `for ( ; ; )` 무한 loop
