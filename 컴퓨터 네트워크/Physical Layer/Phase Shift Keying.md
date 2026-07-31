---
aliases:
  - PSK
  - 위상 편이 변조
  - Phase Shift Keying(PSK)
---

- [[Digital-to-Analog Conversion]] 방식 중 위상(Phase) 변화로 bit 표현
- 진폭 · 주파수 고정

![[Analog-Transmission-07.png]]

### 종류
| 방식 | 위상 수 | 표현 |
| --- | --- | --- |
| BPSK(Binary PSK) | 2 | 0 or 1 |
| QPSK(Quadrature PSK) | 4 | 00, 01, 10, 11 |

- BPSK 위상 : ==0˚, 180˚==
- QPSK 위상 : ==45˚, 135˚, -45˚, -135˚==
	- BPSK 대비 ==2 배== 속도

![[Analog-Transmission-08.png]]

![[Analog-Transmission-09.png]]

### 특징
- 진폭 일정 -> [[Amplitude Shift Keying]] 대비 [[Noise]] 내성 ↑
- 위상 + 진폭 동시 사용 -> [[Quadrature Amplitude Modulation]]
