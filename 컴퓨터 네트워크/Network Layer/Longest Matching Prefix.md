---
aliases:
  - 최장 일치 프리픽스
  - 최장 일치 프리픽스(Longest Matching Prefix)
---

- [[Prefix Routing]] 에서 여러 Destination 이 목적지 포함 -> Prefix 가 긴쪽 (subnet 이 큰 쪽) 으로 이동
- 더 구체적인 주소로 이동
- Prefix 동일 -> 아무 곳으로 이동

![[Internet-Addressing-07.png]]
- ==ex)== 목적지가 `194.24.14.72`
	- London : `194.24.0.0` ~ `194.24.32.255`
	- San Francisco : `194.24.12.0` ~ `194.24.16.0`
	- 두 Destination 모두 목적지 포함 -> San Francisco 선택
