---
aliases:
  - 가독성
  - Readability(가독성)
---

- Simplicity (단순성)
	- 기본 구성 요소 (기능) 적을 수록 이해 쉬움
		- 가장 simple 한 언어 -> [[Assembly]]
	- Feature Multiplicity : 같은 기능 수행 방법 여러 개 -> [[Readability|가독성]]↓
	``` cpp
	count++
	++count
	count += 1
	count = count + 1
	```
	- Operator [[오버로딩|Overloading]] : 같은 연산자에 여러 개의 기능
		- ==ex)== `+` : 정수 덧셈, 실수 덧셈, [[String|문자열]] 더하기
			- 기계어 동작 방식 상이, 개념은 동일 -> simple 한 설계 위해 같은 symbol 사용
		- ==ex)== [[C]]의 `&` -> 잘못된 사용
	``` c
	a = &b; // 주소 가져오기
	a = a & b; // and operation
	```

- Orthogonality (직교성)
	- 기능이 겹치지 않음. 똑같은 기능을 여러 언어로 표현 X
	- [[데이터 타입]] + [[제어문]] 조합 했을 때 예외 발생 X
	- `if` 와 `switch` -> orthogonal X ==(같은 조건 제어문)==

- [[제어문|Control Statement(제어문)]]
	- [[폰 노이만 구조]] -> 위에서 아래로 자연스러운 흐름
	- [[GOTO]]-less : jump 구조 최소 사용
	- [[Structured Programming]] : 들어오는 곳 1, 나가는 곳 1
- [[데이터 타입|Data Type]] & [[Data Structure]]
	- [[데이터]] 표현 명확할수록 가독성↑
	- ==ex)== boolean -> [[C]]에 존재 X -> 오류 多

- Syntax Consideration (문법 고려)
	- [[이름]] 규칙, [[Block|block]] 규칙, 생긴 모양 유사
	- 이름 규칙 : `_` 허용 여부
	- block 규칙 : `{}` / `end_loop` / 들여쓰기
