---
aliases:
  - Signal-to-Noise Ratio
  - 신호 대 잡음비
  - SNR(Signal-to-Noise Ratio)
---

- [[Noise]] 에 비해 [[신호]]가 얼마나 큰지의 비율
- SNR = $\frac{\text{signal power}}{\text{noise power}}$

### 특징
- SNR ↑ -> quality good
- SNR ↓ -> signal & noise 비슷 -> error ↑

![[Data-and-Signals-20.png]]

- SNR 너무 낮음 -> 신호 복구 불가능
- $\text{SNR}_{dB} = 10 \log_{10}(\text{SNR})$ -> [[Decibel]] 표현
- [[Shannon Capacity]] 계산 입력값 (not dB)

### 무선 환경
- 수신 세기 이외의 noise 반영 -> 무선 링크 품질 지표
- SNR ↑ -> 높은 [[MCS]] level 사용 O
	- ==ex)== BPSK, 64-[[Quadrature Amplitude Modulation|QAM]]
- 요구 SNR + noise floor -> [[Receiver Sensitivity]]
