---
aliases:
  - 취약 시간
  - Vulnerable Time(취약 시간)
---

- 어떤 frame 이 collision 에 노출되는 시간 구간
- 이 구간 동안 다른 전송 X -> 전송 성공

![[Medium-Access-Control-15.png]]

### 프로토콜별 길이
| 프로토콜 | vulnerable time | 근거 |
| --- | --- | --- |
| [[Pure ALOHA]] | $2 \times T_{\text{fr}}$ | 그 frame + 그 frame 이전 frame -> Time slot 2배 |
| [[Slotted ALOHA]] | $T_{\text{fr}}$ | 중간 시점 전송 시작 frame X -> 앞쪽 구간 소멸 |
| [[CSMA]] | $T_p$ ([[Delay\|propagation delay]]) | busy [[신호]] 도착 전 idle 로 오인 |

- ==ex)==
	![[Medium-Access-Control-16.png]]
	- $T_{\text{fr}}$ = $\frac{200\ \text{bits}}{200\times 10^3\ \text{bps}}$ = 1ms
	- 2 × 1ms = ==2ms== 동안 다른 전송 없어야 함
