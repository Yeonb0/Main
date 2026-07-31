---
aliases:
  - dB
  - 데시벨
  - Decibel(데시벨)
  - dBm
---

- [[신호|Signal]] strength 표현 단위
- dB = 10 $\log_{10}(\frac{P_2}{P_1})$ -> 기준점($P_1$) 대비 신호의 크기(power) 비율

### 특징
- 10 dB -> 10배 큼
- 30 dB -> 1000배 큼
- dB 양수 -> signal 을 얻음 (증폭됨)
- dB 음수 -> signal 이 사라짐 (감쇠됨)
- 장점 : 큰 수끼리의 곱셈 -> 덧셈 / 뺄셈으로 변환
- [[Attenuation]] · [[SNR]] 표현에 사용

### dBm
- ==1 밀리와트== 기준 dB 의 절댓값
- dBm = 10 $\log_{10}P_m$

| power | dBm |
| --- | --- |
| 1mW | 0dBm |
| 10mW | 10dBm |
| 100mW | 20dBm |
| 0.1mW | -10dBm |

- ==ex)== 스마트폰 : 23 dBm
- ==ex)== -30 ~ 40 dBm : 전송률 good (와이파이 꽉참)
- ==ex)== -80 ~ 90 dBm : 전송이 끊킴 (와이파이 한 두 칸)
- ==ex)== -100 dBm : 통신 불가 (0.0000000001 mW)
