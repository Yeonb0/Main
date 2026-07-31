---
aliases:
  - 디지털-아날로그 변환
  - Digital-to-Analog Conversion(디지털-아날로그 변환)
  - D/A 변환
---

- digital data 를 [[Analog Signal]] 로 변환해 전송하는 과정
- bandpass 매체(wireless, shared media) 전송 조건 -> analog signal 필수

![[Analog-Transmission-01.png]]

### 절차
1. Digital -> Analog 변환
2. channel 전송
3. Analog -> Digital 복원

### 조건
- [[Analog Signal]] 의 3 요소 이용 인코딩
	- 진폭(Amplitude)
	- 주파수(Frequency)
	- 위상(Phase)

### 구조
- [[Data Element]] : bit
- [[Signal Element]] : signal 의 가장 작은 단위
	- signal element 하나에 몇 bit 표현?
	- ==ex)== bit 1 개 -> 모양 2 개 / bit 8 개 -> 모양 64 개
- N : [[Data Transfer Rate 1|Data transmission rate(bit rate)]]
- S : [[신호|Signal]] transmission rate(baud rate)

$$
S = N \times \frac{1}{r}
$$

### 종류
![[Analog-Transmission-02.png]]

- [[Amplitude Shift Keying]]
- [[Frequency Shift Keying]]
- [[Phase Shift Keying]]
- [[Quadrature Amplitude Modulation]] -> ==현재 주력==
