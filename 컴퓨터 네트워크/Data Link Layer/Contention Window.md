---
aliases:
  - 경쟁 윈도우
  - Contention Window(경쟁 윈도우)
---

- [[CSMA-CA|CSMA/CA]] 에서 [[IFS]] 이후 더 기다리는 random 대기 구간
- random 시간 × frame 만큼 대기

### 동작
- countdown 해서 0 -> 전송 시작
	- idle [[state|상태]]일 때만 감소
	- busy 상태 -> 초기화 X, pause O
	- 다시 idle -> 초기화된 [[IFS]] 대기 후 countdown 이어감
- collision 발생 -> contention window 2배 (==0 ~ 31== -> ==0 ~ 63==) -> [[Collision|충돌]] ↓
	- [[Binary Exponential Backoff]]
- ==ex)==
	![[Medium-Access-Control-25.png]]
	![[Medium-Access-Control-26.png]]
	- Window : A 5 / B 10 / C 15
