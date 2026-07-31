---
aliases:
  - Code-Division Multiple Access
  - 코드 분할 다중 접속
  - CDMA(Code-Division Multiple Access)
---

- 같은 시간 · 같은 주파수 전송 -> code division 으로 구분하는 [[Channelization]] 방식

### 구조
- 각 station 에 Code 배정

![[Medium-Access-Control-07.png]]

- Code 성질 : 자기 자신과 곱 -> ==4== (인원 수), 다른 code 와 곱 -> ==0== (like orthogonal)

![[Medium-Access-Control-08.png]]

### 절차
1. [[데이터]] 부호화
	- 0 -> -1
	- 1 -> +1
	- 전송 X -> 0

![[Medium-Access-Control-09.png]]

2. Common Channel 에 전부 더한 값 전송 -> 각 채널로 전파
3. 수신 채널이 나 이외 다른 station 의 code 곱하고 ==4== 로 나누기

![[Medium-Access-Control-10.png]]

### 코드 생성
- [[Walsh Table]] 사용
