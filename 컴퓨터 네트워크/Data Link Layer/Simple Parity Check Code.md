---
aliases:
  - 패리티 검사 부호
  - Simple Parity Check Code(패리티 검사 부호)
---

- parity -> error checking code
- k-bit dataword -> (k+1)-bit codeword, [[Parity Bit]] 1개 추가
- codeword 가 짝수개 (또는 홀수개) 의 1 가지도록 parity bit 결정

### 절차
1. `110101` + `[1 | 0]` -> `1101010`
2. 수신 error X -> parity bit 빼고 상위 전달
3. 수신 error O -> 그 [[Block|block]] 폐기

### 성능
- [[Minimum Hamming Distance|MHD]] = 2
- 1-bit error (+ 홀수-bit error) 검출 O / 짝수-bit error 검출 X

### 장점
- 2-bit error 가능성 낮음 -> 대부분 error 커버 가능
- dataword 길이 (k) 조정 가능 -> 길게 하면 효율성 good
- 가성비 좋음 -> 많이 사용됨

![[Error-Detection-and-Correction-06.png]]
