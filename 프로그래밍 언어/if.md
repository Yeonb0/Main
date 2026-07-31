---
aliases:
  - if statement
  - if 문
---

- 조건식 평가 -> 실행 경로 분기하는 [[조건문]]

### 형태
- Single-Way Selector : `if ( ) then ...`
	- FORTRAN : 중첩 X, single statement 만
	- ALGOL : `begin ~ end` -> 여러 statement 선택 O
- Two-Way Selector : `if ( ) then ... else ...`
	- 두 경로 중 하나 선택

### 조건식
- 대부분 언어 : boolean 표현식
- [[C]] : arithmetic 표현식 ==(boolean 타입 부재)==

### Nesting Selectors
- 중첩 선택자 모호성 -> 마지막 `else` 의 짝 판별 문제
``` c
if (sum = 0) then
	if (count = 0)
		then result := 0
else result := 1
```
- 대부분 언어 : 가장 가까운, 짝 없는 `then` 절 ==(count = 0)==
- [[Python]] : indentation 기준 ==(sum = 0)==
- 일부 언어 : `END` · `END IF` 로 끝 명시
