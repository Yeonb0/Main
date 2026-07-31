---
aliases:
  - 원시 데이터 타입
  - Primitive Data Type(원시 데이터 타입)
---

- 하드웨어가 직접 지원하는 [[데이터 타입]]
- 기계어 수준에서 처리 O

### Numeric Type
- Integer
	- 대부분의 CPU -> 여러 size 의 정수 지원
	- word size 와 다르게 compile 될 수 있음

	![[Data-Types-01.png]]

	- ==ex)== `int` : 64-bit 환경, 32-bit size
	- ==ex)== `pointer` : 64-bit -> 주소 길이 8 byte
	- 구현 : binary sequence
		- 가장 왼쪽 비트 ==(MSB, Most Significant Bit)== -> 부호 표시
		- 2's complement 방식 사용

	![[Data-Types-02.png]]

- Floating-Point
	- fraction + exponent 로 표현
	- 실수 모델링 -> 정확 X, approximation ==(근사)== 만 가능
	- 구현 : by binary
		- sign bit : 부호
		- exponent : 지수
		- fraction : 가수
	- bit 사용량↑ -> 근사 정밀도↑

	![[Data-Types-03.png]]

	- IEEE Floating-Point 표준
- Decimal
	- BCD ==(Binary Coded Decimal)== : 10진수 각 자리를 4 bit 이진수로 표현
	- 장점 : 정확한 표현
	- 단점 : 16개 표현 가능한데 10개만 사용 -> 메모리 낭비

### Boolean Type
- True / False ==두 값== 만 존재
- 구현 : single bit 로 표현 가능, but byte 단위 저장

### Character Type
- 문자 -> 숫자 코드 형태 저장
- ASCII : 1 byte ==(0 ~ 127)==
- Unicode
