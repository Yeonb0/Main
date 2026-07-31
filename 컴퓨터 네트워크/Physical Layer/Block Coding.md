---
aliases:
  - 블록 코딩
  - mB/nB coding
  - 블록 코딩(Block Coding)
---

- [[Block Coding|mB/nB coding]] : m bits 의 data (원래 input) -> n bits 로 coding 해서 전송
	- 더 "큰" bit 로 mapping
- 목표 : [[Self Synchronization]], [[Error Detection|error detection]]

### 종류
- [[4B5B|4B/5B]]

### 용어
- dataword (k) : original message [[Block|block]]
- codeword (n) : block-coded 된 message
	- n > k
- r ([[Redundancy]]) = n - k

### 검증 기준
- 속도 : [[Redundancy]]
- 오류 검출 ([[Error Detection|detection]]) 능력
- 오류 수정 ([[Error Correction|correction]]) 능력 -> 모든 경우에 대해 가능

### 예시
- Example 1 : k = 2, n = 1, r = 1

![[Error-Detection-and-Correction-03.png]]

	-> 1-bit detection O, 2-bit detection X, correction X
- Example 2 : k = 2, n = 5, r = 3

![[Error-Detection-and-Correction-04.png]]

	- overhead : 150%
	- 1 bit error -> detection O, correction O
	- 2 bit error -> detection O, correction X
	- 3 bit error -> detection X, correction X
	- [[Minimum Hamming Distance|MHD]] = 3 -> 2 bit error detection & 1 bit error correction
