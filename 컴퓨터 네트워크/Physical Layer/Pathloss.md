---
aliases:
  - 경로 손실
  - Pathloss(경로 손실)
---

- 거리에 따라 감소하는 [[신호]] 양
- 송신 전력 · 수신 전력 관계 modeling -> 무선 [[Transmission Impairment]]
- TX (transmit) 안테나 -> RX (receive) 안테나 전송 시 신호 퍼짐 -> 전력 손실 ↑

![[Case-Study-Wi-Fi-01.png]]

### Friis propagation model
$$
\frac{P_r}{P_t} = G_tG_R \left( \frac{\lambda}{4\pi R} \right)^2
$$

- P : Power, 전력
- G : 안테나 gain (기본적으로 1)
- λ : 전파의 파장 (Wavelength)
- R : sender - receiver 거리

### General log-distance Pathloss model
$$
P_r \propto \frac{1}{R^n}
$$

- 측정 통해 ==n== 결정 -> 환경별 일반화

### 특징
- 안테나에서 신호 증폭 O
- 무선 수신 세기 결정 요인 -> pathloss + [[Fading]]
- 수신 가능 하한 기준 -> [[Receiver Sensitivity]]
