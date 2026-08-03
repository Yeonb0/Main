---
aliases:
  - 이진 지수 백오프
  - Binary Exponential Backoff(이진 지수 백오프)
---

- [[Collision|충돌]] 후 재전송 대기 시간을 random + 지수적으로 늘리는 방식
- [[ALOHA]] / [[CSMA-CD|CSMA/CD]] / [[CSMA-CA|CSMA/CA]] 공통 사용

![[Medium-Access-Control-19.png]]

### 절차
1. $0 \sim 2^k-1$ 중 하나 뽑기 -> R
2. T × R 초 대기 (T : time slot)
3. 충돌 발생 시 K++ -> 대기 범위 $2^x$ 배

### 조건
- $K_{max} = 15$
	- 초과 시 포기 -> 상위 layer 에 위임
	- 이 정도면 [[ACK]] 전달 X 문제 -> K 증가로 해결 불가

### Time Slot
- 시스템 마다 상이
1. Transmission Time (packet size, 갯수)
2. Propagation Time (거리, 빛의 속도)
- 둘 중 큰 쪽으로 time slot 설정
- ==ex)== [[IEEE 802.11|Wi-Fi]] : $9\mu s$ / [[Ethernet]] : 512 bit times
