---
aliases:
  - QAM
  - 직교 진폭 변조
  - Quadrature Amplitude Modulation(QAM)
---

- 진폭 + 위상 동시 [[Modulation 1|변조]]하는 [[Digital-to-Analog Conversion]] 방식
- [[Constellation Diagram]] 의 점 [[배치 처리|배치]]로 정의

### 형태
- n-QAM : constellation diagram 에 ==n 개== 점 사용
	- 한 [[Signal Element]] 당 $\log_2 n$ 개 bit 전송

![[Analog-Transmission-12.png]]

### 특징
- 점 수 ↑ -> 속도 ↑, [[Noise]] 취약
- [[Amplitude Shift Keying]] · [[Phase Shift Keying]] 결합 형태
- 현재 가장 많이 쓰이는 [[Modulation|변조]] 방식

### Wi-Fi
- [[IEEE 802.11]] 세대별 차수 ↑
	- Wi-Fi 5 -> 256 QAM
	- Wi-Fi 6 -> 1024 QAM
	- Wi-Fi 7 -> 4096 QAM
- 차수 선택 기준 -> [[MCS]] index
