---
aliases:
  - 경로 집약
  - 경로 집약(Route Aggregation)
  - Rout aggregation
---

- [[Router]] entry 중 Next hop 동일 -> 하나의 prefix 로 합치기
- 합칠 때는 prefix 가 (subnet) 모두 포함은 하되, 최소가 되도록

![[Internet-Addressing-08.png]]
- ==ex)== 3 곳의 Next hop 동일 -> `194.24.0.0/19` 로 합치기
	- 중간 12 ~ 15 비어 있지만 괜찮음
		- entry 없을 경우 : 이동 X
		- entry 있을 경우 : [[Longest Matching Prefix]] 니까 자동으로 이동

![[Internet-Addressing-09.png]]
- specific 한게 좋은 router
- `/28` 로 쓰면 0 ~ 15 로 추가 범위 포함 -> XX
