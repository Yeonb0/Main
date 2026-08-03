---
aliases:
  - Multiple Input Multiple Output
  - MIMO(Multiple Input Multiple Output)
---

- 여러 TX 안테나 -> 여러 RX 안테나 동시 사용
- 안테나 사용 갯수에 따른 분류

![[Case-Study-Wi-Fi-06.png]]

### 장점
- Spatial multiplexing gain
	- TX 에서 서로 다른 [[데이터]] 전송
	- 서로 다른 데이터 보낸 TX 만큼 RX 있으면 복원 O
	- 안테나 갯수 적은 쪽 만큼 spatial stream 가능

	![[Case-Study-Wi-Fi-07.png]]

- Diversity gain
	- RX 많음 -> 더 잘 수신 O -> [[Fading]] 완화
	- 수신 [[state|상태]] 양호한 것 사용 / 합쳐서 사용

	![[Case-Study-Wi-Fi-08.png]]

- [[배열|Array]] gain (beamforming)
	- 안테나 전송 타이밍 & 세기 조절 -> 한쪽으로만 세게

	![[Case-Study-Wi-Fi-09.png]]

### 특징
- spatial stream 수 -> [[MCS]] 구성 요소
- 안테나 수 ↑ -> 속도 ↑
