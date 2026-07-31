---
aliases:
  - 오류
  - 전송 오류
  - Error(오류)
---

- 전송된 data 에서 bit 가 flip (0 ↔ 1) 되어 도착
- 한 [[Block|block]] 에서 flip 된 bit 수 -> error 심각성 결정

### 원인
- [[Attenuation]], [[Distortion]], [[Noise]], interference
	-> amplitude, frequency, phase 변화

![[Error-Detection-and-Correction-01.png]]

### n-bit error
- error 단위는 한 bit X -> 한 block 안의 error 갯수
- ==ex)== 원본 `01101100` / 수신 `01011101` -> 3-bit error

### 대응
- [[Error Detection]]
- [[Error Correction]]
