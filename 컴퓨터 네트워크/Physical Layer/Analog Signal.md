---
aliases:
  - 아날로그 신호
  - Analog Signal(아날로그 신호)
---

- 시간에 따라 연속적으로 변화하는 [[신호]]
- Sine wave : sin [[함수]] 형태의 주기 신호(periodic signal)

![[Data-and-Signals-02.png]]

### 특성
- 진폭(amplitude) : 얼마나 높이 움직이는가
	- Peak amplitute : 제일 높은 신호

![[Data-and-Signals-03.png]]

- 주파수(Frequency) : 1초에 같은 pattern 반복 횟수
	- 단위 : ==Hz==
- 주기(Period) : 한 pattern 에 걸리는 시간
	- 단위 : ==s==
	- 주파수와 역수 관계 -> 같은 feature

$$
f = \frac{1}{T} \quad \text{and} \quad T = \frac{1}{f}
$$

![[Data-and-Signals-04.png]]

- 위상(Phase) : 0 기준 신호 시작 위치
	- 각도 or radian
- 파장(wavelength, $\lambda$) : 한 주기 동안 이동 거리(Distance)
	- $\lambda = \frac{c}{f}$
		- c = 빛의 속도 = $3 \times 10^8$ -> 매질 따라 속도 변화
		- f = 주파수(frequency)
	- 주파수 ↑ -> 파장 ↓ (반비례), 주기와는 비례 -> 한 pattern 짧으면 가는 거리도 짧음
	- ==4 번째 feature X==
	- ==ex)== 밀리미터파 -> 파장이 밀리미터 수준

### 특징
- 주파수 -> 진동 속도 표현
	- 빨리 진동 -> 주파수 ↑
	- 느리게 진동 -> 주파수 ↓
- 특이 케이스
	- 아주 느리게 변하는 신호 -> zero frequency, ==DC(Direct Current)==
	- 순간적으로 급변하는 신호 -> frequency 무한대
- 서로 다른 신호 구분 기준 -> ==진폭(amplitude) / 주파수(frequency) / 위상(Phase)==
- 여러 신호의 합 -> [[Composite Signal]]

### 활용
- 진폭 / 주파수 / 위상 조절 -> [[Digital-to-Analog Conversion]] 인코딩 수단
	- [[Amplitude Shift Keying]] / [[Frequency Shift Keying]] / [[Phase Shift Keying]]
- analog data 를 [[Carrier Signal]] 에 적재 -> [[Analog-to-Analog Conversion]]
