---
aliases:
  - 체크섬
  - Checksum(체크섬)
---

- [[Simple Parity Check Code|Parity check code]] 보다 복잡한 [[Error Detection]] 방식
- IP (layer 3) / TCP, UDP (layer 4) 에서 header 오류 확인용

### 절차
1. 보낼 값 전부 합산
2. [[Wrapped Sum]] & 1's complement -> checksum 생성
3. 수신 측에서 받은 값 다 더함 -> 0 -> no error

- ==ex)== 5개의 4-bit 숫자 전송

![[Error-Detection-and-Correction-11.png]]
