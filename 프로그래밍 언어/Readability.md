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

- Orthogonality (직교성)
	- 기능이 겹치지 않음. 똑같은 기능을 여러 언어로 표현 X
	- [[데이터 타입]] + [[제어문]] 조합 했을 때 예외 발생 X

- [[제어문|Control Statement(제어문)]]
- [[데이터 타입|Data Type]] & [[Data Structure]]
	- 데이터 표현 명확할수록 가독성↑

- Syntax Consideration (문법 고려)
	- 이름 규칙, block 규칙, 생긴 모양 유사 







