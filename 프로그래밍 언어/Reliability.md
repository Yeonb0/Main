---
aliases:
  - 신뢰성
  - Reliability(신뢰성)
---

- 어떤 조건 하에서도 프로그램이 잘 돌아가도록
- [[Type Checking]] : 피연산자 타입이 다르면
	- ==ex)== [[C]] : type checking X, Pascal : [[배열]] 범위 검사 제공
- [[Exception Handling]] 
	- ==ex)== 0으로 나누기, 메모리 부족
	- run-time error 잡기 ==(dynamic)== ↔ [[컴파일]] 단계에서 잡기 ==(static)==
	- [[바인딩 시점]]에 따라 static / dynamic 선택
- [[Aliasing]] : 같은 저장 공간 대해 여러 [[이름]] 가짐
	- debugging 어려움 -> 위험
