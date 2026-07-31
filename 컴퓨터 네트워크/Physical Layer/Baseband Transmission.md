---
aliases:
  - 베이스밴드 전송
  - Baseband Transmission(베이스밴드 전송)
---

- 유선에서의 [[Digital Signal]] 전송 방법
- low-pass channel 사용 -> 0 부터의 낮은 주파수 대역 그대로 사용

![[Data-and-Signals-12.png]]

- [[Time Domain vs. Frequency Domain|Time domain]] -> Frequency domain 변환
- 결국 sine wave 들의 합으로 만들어 전송 -> 무한대의 [[Bandwidth]] 필요. 难

### 절차
1. Digital [[신호|Signal]] 은 이산적 -> Analog 로 변환
2. [[Channel]] 로 전달
	- channel : [[데이터]]가 전송되는 추상적 통로

### 조건
- 이상 : 0 ~ ∞ 의 bandwidth 사용 -> 정확하게 변환된 신호 전송

![[Data-and-Signals-13.png]]

- 현실 : 모든 bandwidth 사용 가능 X
	- 일부 bandwidth 만 사용해 signal 전달 -> signal 의 왜곡

![[Data-and-Signals-14.png]]

### Baseband Approximation
- ==ex)== 3 bit 전송

![[Data-and-Signals-15.png]]

- 8 pattern 존재, n = 1초에 보내야 하는 bit 수
	- 000 / 111 -> 주파수 0
	- 001 / 011 / 100 / 110 -> 4칸마다 주기 반복, 주파수 $\frac{n}{4}$
	- 010 / 101 -> 2칸마다 주기 반복, 주파수 $\frac{n}{2}$
- bandwidth = 최고 주파수 - 최저 주파수 = $\frac{n}{2}$ - 0 = $\frac{n}{2}$

![[Data-and-Signals-16.png]]

- bandwidth ↑ -> digital signal 과 유사 -> 원 신호 복원 용이
- bandwidth ↓ -> 복원 불가
	- Nyquist Condition : 최소 $\frac{n}{2}$ 만큼의 주파수 필요

![[Data-and-Signals-17.png]]

- bandwidth = f -> 최고 transfer rate = 2f -> [[Nyquist Equation]] 의 근거

### 비교
| 구분 | 사용처 |
| --- | --- |
| Baseband (low-pass channel) | ethernet 유선 |
| [[Bandpass Channel]] | Wi-Fi, LTE / 5G |
