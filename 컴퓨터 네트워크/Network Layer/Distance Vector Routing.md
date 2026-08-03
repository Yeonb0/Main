---
aliases:
  - 거리 벡터 라우팅
  - Distance Vector Routing(거리 벡터 라우팅)
---

- 자신의 table 전체를 직접 연결된 이웃에게만 전달 -> 목적지별 최단 거리 갱신
- distance vector = (destination, distance, next [[node]])
- [[Bellman-Ford]] 의 분산형 동작
![[Routing-11.png]]

### 절차
1. initial : 직접 연결된 정보만 작성
![[Routing-12.png]]
2. 이웃에게 (destination, distance) 전달
3. 기존 정보 X -> vector 신규 작성
4. 기존 정보 O -> 거리 감소 시에만 vector 갱신
5. 지속적 update -> 전체 최단 거리 수렴
![[Routing-13.png]]
- ==ex)== A -> C
	- A -> B -> C (8) : X
	- A -> E -> D -> C (5) : O
	- hop 수 ↑ 이지만 최단 거리 경로 선택

### link 장애
![[Routing-14.png]]
- 장애 인접 router 가 문제 파악 -> table 갱신 후 전파
![[Routing-15.png]]

### 단점
- 느린 수렴
- [[Count-to-Infinity Problem]]

### 구현
- [[RIP]]
