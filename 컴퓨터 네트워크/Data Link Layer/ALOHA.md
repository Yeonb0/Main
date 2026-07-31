---
aliases:
  - 알로하
  - ALOHA(알로하)
---

- Hawaii 대학에서 개발한 [[Random Access]] 프로토콜
- 보낼 것이 있으면 보냄
- [[Collision|충돌]] 시 random 한 시간 대기 후 재전송 -> [[Binary Exponential Backoff]]

### 종류
- [[Pure ALOHA]] : 시간 분할 X
- [[Slotted ALOHA]] : 시간 slot 분할

### Throughput
- Time Slot 시간 동안 성공적으로 수신되는 frame 확률 (충돌 제외)
- S : 성공적 수신 frame 수
- G : 한 $T_{\text{fr}}$ 마다 평균 frame 생성 수

### 최대 throughput 조건
| 프로토콜 | 식 | 최적 G |
| --- | --- | --- |
| [[Pure ALOHA]] | $S = G \times e^{-2G}$ | $\frac{1}{2}$ (2 $T_\text{fr}$ 마다 1개) |
| [[Slotted ALOHA]] | $S = G \times e^{-G}$ | 1 (1 $T_\text{fr}$ 마다 1개) |

### 식 유도
- poisson 분포

$$
P(k) = \frac{\lambda^k \times e^{-\lambda}}{k!}
$$

- k = 0 대입, λ = 2G 대입

$$
P(0) = \frac{e^{-2G}}{0!} = e^{-2G}
$$

- 따라서 $S = G \times e^{-2G}$
