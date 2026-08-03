---
aliases:
  - 프리픽스 라우팅
  - 프리픽스 라우팅(Prefix Routing)
---

- [[Router]] 의 전체 테이블 작성 -> 복잡
- 같은 방향은 묶어서 표시 -> [[Subnetting|subnet]] 과 유사
	- 지역적으로 IP 주소 유사 필요

![[Internet-Addressing-06.png]]
- ==ex)== 목적지가 `194.24.17.4` -> Oxford 로 전송

### 확장
- 여러 Destination 이 목적지 포함 -> [[Longest Matching Prefix]]
- Next hop 동일 -> [[Route Aggregation]]
