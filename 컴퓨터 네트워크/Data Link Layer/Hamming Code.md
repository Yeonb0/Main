---
aliases:
  - 해밍 코드
  - Hamming Code(해밍 코드)
---

- 1-bit error correct 가능한 [[Minimum Hamming Distance|MHD]] = 3 인 codeword set
- $d_{min}$ = 3
	- 2-bit error detect 가능
	- 1-bit error correct 가능
- Hamming (n, k) code : k-bit dataword -> n-bit codeword (k < n)

### Voting (Hamming (3, 1) code)
| dataword (k) | codeword (n) |
| --- | --- |
| 0 | 000 |
| 1 | 111 |
- 1-bit error -> 다수결 따라 1 많으면 111, 0 많으면 000
- overhead : $\frac{1}{3}$
- efficiency : 33%

### Hamming (7, 4) code
- 4-bit -> 7-bit

| $C_1$ | $C_2$ | $D_3$ | $C_4$ | $D_5$ | $D_6$ | $D_7$ |
| --- | --- | --- | --- | --- | --- | --- |
| 001 | 010 | 011 | 100 | 101 | 110 | 111 |
- 1 (`001`), 2 (`010`), 4 (`100`) -> check bit
	- check bit 에 영향 주는 값 XOR (1 갯수 세기)
		- 1이 짝수개 -> 0
		- 1이 홀수개 -> 1
	- 1 (`001`) -> 3 (`011`), 5 (`101`), 7 (`111`)
	- 2 (`010`) -> 3 (`011`), 6 (`110`), 7 (`111`)
	- 4 (`100`) -> 5 (`101`), 6 (`110`), 7 (`111`)
- 3, 5, 6, 7 -> data bit

![[Error-Detection-and-Correction-10.png]]

- MHD = 3 -> 1-bit correction 가능
- efficiency : $\frac{4}{7}$ = 57.1 %

### Hamming (15, 11) code
- 11-bit -> 15-bit, 원리 same
- 1 (`0001`), 2 (`0010`), 4 (`0100`), 8 (`1000`) -> check bit
	- 영향 주는 값 1 갯수 세기
- 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15 -> data bit

### 일반화
- codeword 수 = $2^k -1$
- dataword 수 = $2^k - 1 - k$
- efficiency = $\frac{2^k-1-k}{2^k-1}$
- ==ex)== k = 3 -> (7, 4) / k = 4 -> (15, 11) / k = 5 -> (31, 26)
- k ↑ -> efficiency ↑, but 2-bit error 확률 ↑
- correction 은 항상 1-bit 만 가능
	-> 더 많은 오류 발생 시 다른 방법 사용 (ex. [[Cyclic Redundancy Check|CRC]])
- 7-bit 전송 case -> 8개
	- 최소 3개의 bit 필요
	- Hamming code 가 가장 효율적인 방법
