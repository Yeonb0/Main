---
aliases:
  - 랩 어라운드 합
  - Wrapped Sum(랩 어라운드 합)
---

- 정해진 bit 수 초과분을 하위로 되돌려 더하는 합 -> [[Checksum]] 계산에 사용
- ==ex)== 36 -> `100100` -> 4-bit 초과 -> 초과분 wrap

![[Error-Detection-and-Correction-12.png]]

### Error Detection
- 수신 측에서 받은 값 다 더해서 wrapped sum & 1's complement
	- `0000` -> no error
	- 그 이외 값 -> error
