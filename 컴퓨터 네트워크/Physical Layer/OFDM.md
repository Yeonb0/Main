---
aliases:
  - Orthogonal Frequency Division Multiplexing
  - OFDM(Orthogonal Frequency Division Multiplexing)
---

- 화면을 격자처럼 나눠 병렬 전송하는 다중 [[Carrier Signal|반송파]] [[Modulation|변조]]
- subcarrier : 세로(주파수) 분할
- symbol : 가로(시간) 분할 -> guard interval 필요

### 802.11n 구성
| [[Bandwidth]] | subcarrier | [[데이터]] | pilot |
| --- | --- | --- | --- |
| 20MHz | 56 개 (각 312.5KHz, 총 17.5MHz) | 52 개 | 4 개 |
| 40MHz | 114 개 | 108 개 | 8 개 |

- pilot : 송수신자 간 이미 알고 있는 데이터 -> 근처 주파수 영역 보정
- 40MHz : 주변 채널 몰아 사용 -> 속도 ↑ -> [[Wi-Fi Channel]]
- symbol : ==3.2 μs==
	- long GI : 0.8 μs -> 안좋은 환경
	- short GI : 0.4 μs -> 좋은 환경

![[Case-Study-Wi-Fi-10.png]]

- 40MHz -> 20MHz 의 2배보다 살짝 더 많이 전송
- short GI -> long GI 보다 많이 전송

### Data rate 계산
![[Case-Study-Wi-Fi-11.png]]

- ==ex)== 64QAM -> 각 칸마다 6 bit 전송
- Coding = $\frac{5}{6}$ -> 6 bit 중 5 bit 만 실제 데이터
- 40MHz -> channel 108 개
- Short Guard Interval -> 전송 3.2 μs + interval 0.4 μs -> 초당 277,777 번 전송
- Data rate = $6 \times \frac{5}{6} \times 108 \times 277,777$ = 150Mbps
- 4 spatial multiplexing -> 4배 -> 최고 속도 600Mbps

### 특징
- 사용자별 subcarrier 할당 확장 -> [[OFDMA]]
- 조합 index 선택 -> [[MCS]]
