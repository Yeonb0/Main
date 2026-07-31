---
aliases:
  - CRC
  - 순환 중복 검사
  - Cyclic Redundancy Check(CRC)
---

- dataword 를 generator 로 나눈 remainder 를 붙여 보내는 [[Error Detection]] 방식
- [[Modulo-2 Arithmetic]] 기반 나눗셈

### 용어
| 항목 | 내용 |
| --- | --- |
| Divisior = Generator | 보낼 data 에 붙일 숫자 |
| [[Dataword]] | 보낼 data, Dataword + `000` 를 Divisior 로 나눔 |
| [[Codeword]] | dataword + remainder |

### 절차
1. dataword 뒤에 `000` 부착
2. divisior (generator) 로 나눔
3. remainder 붙여 codeword 전송
- ==ex)== Dataword `1001` / Divisor (Generator) `1011`

![[Error-Detection-and-Correction-14.png]]

### Error Detection
- 수신자가 generator (divisior) 로 나눔
	- remainder 000 -> no error
	- remainder 가 000 아님 -> error
- [[Polynomial|다항식]] 표현 -> [[Binary Polynomial]]

### 성능
- $x^0$ 있고, 최소 하나의 다른 항 존재 -> 모든 1-bit error 발견 가능

![[Error-Detection-and-Correction-16.png]]

- [[Burst Error]] : error 시작 ~ 끝 길이
	- ==ex)== 5-bit burst error : 1 _ _ _ 1
- $g(x)$ 의 최고차항 : n -> n-bit 이하 burst error 발견 가능
- [[if]] burst size = n + 1
	- 검출 안될 확률 : $1 - (\frac{1}{2})^{n-1}$
	- 대부분은 검출 가능
	- ==ex)== n = 6 (n+1 = 7) -> $\frac{31}{32}$ 확률로 검출 가능
- if burst size = n + 2 ↑
	- 나눠 떨어질 확률 $\frac{1}{2^n}$
	- 검출 안될 확률 : $1 - (\frac{1}{2})^{n}$
	- ==ex)== n = 6 (n+2 = 8) -> $\frac{63}{64}$ 확률로 검출 가능, 8, 9, 10 넘어가도 다 똑같이 $\frac{63}{64}$

![[Error-Detection-and-Correction-17.png]]

### CRC-32
- [[Ethernet]] 에서 [[CRC-32]] 사용
1. 상수항이 1 -> single-bit error 검출 가능
2. (x + 1) 을 인수로 가짐 -> 홀수 개-bit error 검출 가능
3. [[Primitive Polynomial]] -> $2^{32}-1$ 이하인 double-bit error 검출 가능
	- Primitive Polynomial -> 기약다항식, 더 이상 인수 분해 불가 다항식
