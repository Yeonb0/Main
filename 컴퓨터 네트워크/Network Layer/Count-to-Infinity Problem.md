---
aliases:
  - 무한 계수 문제
  - Count-to-Infinity Problem(무한 계수 문제)
---

- [[Distance Vector Routing]] 에서 끊긴 목적지의 cost 가 계속 ↑ 하는 현상
- 원인 : 목적지까지의 경로에 자신이 포함됐는지 모름 -> routing loop 발생
![[Routing-16.png]]

### 진행
- A - B 사이 직접 통로 차단
- B 가 C 경유로 A 도달 가능하다 착각 (실제 경로는 B 경유)
- ==25== 까지 B, C 의 A 행 cost 계속 ↑
![[Routing-17.png]]
![[Routing-18.png]]
![[Routing-19.png]]

### 해결법
- Split horizon : C -> B 로 table 전송 시 next 가 B 인 entry 제외
- Split horizon with poison reverse : next 가 B 인 entry 의 distance 를 ∞ 로 전송
	- ==3 개 loop== 해결 X
![[Routing-20.png]]
- Path vector routing : 중간 경로 전체 제공
	- 장점 : ==3 개 loop== 해결 O
	- 단점 : message overhead
