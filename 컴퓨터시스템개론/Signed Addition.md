---
aliases:
  - 부호 있는 덧셈
  - Signed Addition(부호 있는 덧셈)
---

- Signed 정수끼리 더하는 [[연산]], [[Unsigned Addition]] 과 계산 방식 동일

### 절차
1. 두 binary number 더하기
2. [[2의 보수]] 방법으로 해석
3. 옳은 결과 도출 -> 마찬가지로 carry output 버림

![[Data-Representation-10.png]]

### 시각화
- [[오버플로]], underflow 발생 가능
	- overflow : 음수 + 음수 = 양수
	- underflow : 양수 + 양수 = 음수

![[Data-Representation-13.png]]

![[Data-Representation-14.png]]

- Signed 의 최소 : 1000 0000 …. 0000
- Signed 의 최대 : 0111 1111 …. 1111
