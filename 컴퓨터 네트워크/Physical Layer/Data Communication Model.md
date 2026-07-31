---
aliases:
  - 데이터 통신 모델
  - Data Communication Model(데이터 통신 모델)
---

- [[Physical Layer]] 에서 data 를 실제 [[신호]]로 주고받는 전체 흐름
- 전송 대상 data 는 반드시 bit 화 -> 전송 가능

![[Data-and-Signals-01.png]]

### 절차
1. Digital bit stream -> [[Analog Signal]] 변환
2. channel 통과
3. 수신측에서 Digital bit stream 복원

### 특징
- 전달 과정에서 오류 발생 가능 -> 검증 필요
- 신호 손상 원인 -> [[Transmission Impairment]]
