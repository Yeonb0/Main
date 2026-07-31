---
aliases:
  - 오류 정정
  - Error Correction(오류 정정)
---

- [[Error]] 발생 인지 + 수정까지 가능 -> 오류 나면 수정 후 사용
- [[Error Detection]] 보다 많은 [[Redundancy]] 필요

![[Error-Detection-and-Correction-02.png]]

### 조건
- correction bit = n -> [[Minimum Hamming Distance|MHD]] > 2n (최소 2n + 1)
- 모든 오류 경우에 대해 수정 가능해야 함

### 종류
- [[Hamming Code]] : 1-bit correction
- [[2-Dimensional Parity]] : 1-bit correction
