---
aliases:
  - 양자화 오차
  - 양자화 오차(Quantization Error)
---

- 실제 값과 quantized value 의 차이 -> 원본과의 차이
- [[Quantizing]] 의 level 수 ↑ -> 오차 ↓
- 최대 있을 수 있는 error
	- $-\frac{D}{2} ≤ \text{error} ≤ \frac{D}{2}$

### $\text{SNR}_{dB}$
- 높음 : 원본과 비슷
- 낮음 : 노이즈가 많음
- $\text{SNR}_{dB} = 6.02n_b + 1.76_{dB}$
	- $n_b$ = sample 당 bit 수
	- quantization error 만 이용해 고려 (noise 고려 X)

![[Digital-Transmission-19.png]]
