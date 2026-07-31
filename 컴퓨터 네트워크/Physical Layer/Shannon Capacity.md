---
aliases:
  - 섀넌 용량
  - Shannon Theorem
  - Shannon Capacity(섀넌 용량)
---

- [[Noise]] 있는 channel 에서의 maximum bit rate -> upper bound
- $C = B \times \log_2(1 + \text{SNR})$
	- C : capacity (maximum bit rate)
	- B : bandwidth
	- SNR : signal-to-noise ration (not dB)

![[Data-and-Signals-21.png]]

### signal level
| 방식 | level | bit |
| --- | --- | --- |
| QPSK | 4 | 2 |
| 16QAM | 16 | 4 |
| 64QAM | 64 | 6 |
| 256QAM | 256 | 8 |
| 1024QAM | 1024 | 10 |

### 특징
- [[SNR]] ↑ (error 보다 signal 세기 큼) -> error ↓
- 같은 SNR 에서 사용 level ↑ -> error ↑
- High SNR 근사 : $C = B \times \frac{\text{SNR}_{dB}}{3}$
- noise 무시한 이론 -> [[Nyquist Equation]]
