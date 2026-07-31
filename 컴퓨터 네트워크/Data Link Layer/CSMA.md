---
aliases:
  - Carrier Sense Multiple Access
  - CSMA(Carrier Sense Multiple Access)
---

- Listen before you talk -> 전송 전 channel 감지하는 [[Random Access]] 프로토콜
- [[ALOHA]] : 보내고 [[Collision|충돌]] 안나길 바람 -> 효율 ↓
- hardware 에 Carrier Sense Capability 필요

### 상태
| [[state\|상태]] | 대응 |
| --- | --- |
| idle | 유휴 [[state\|상태]] -> 전송 |
| busy | 이미 전송 받는 중 -> 대기 후 전송 |

### Vulnerable Time
![[Medium-Access-Control-21.png]]
- $T_p$ (propagation delay) -> [[Delay]]
- busy [[신호]] 도착 전 idle 상태로 오인 -> frame 전송

### 종류
- 기준 : Carrier Sensing 빈도

![[Medium-Access-Control-22.png]]

1. 1-persistent CSMA
	- 계속 carrier sensing
	- busy -> idle 변한 시점에 전송
	- 장점 : 바로 접근 O, 노는 시간 X
	- 단점 : Collision 가능성 ↑
2. non-persistent CSMA
	- 한 번 sensing 후 busy 면 일정 시간 대기 후 재 sensing
	- sense 했을 때 idle 로 변경 -> 전송
	- 장점 : Collision 가능성 ↓
	- 단점 : 다 같이 노는 구간 발생 -> 효율성 ↓
3. p-persistent CSMA
	- 계속 carrier sensing
	- idle 상태 sense
		- p 확률로 전송
		- 1-p 확률로 대기 후 전송
	- 1 & 2 의 장단점 보완

### 확장
- [[CSMA-CD|CSMA/CD]] : 유선, 충돌 감지
- [[CSMA-CA|CSMA/CA]] : 무선, 충돌 회피
