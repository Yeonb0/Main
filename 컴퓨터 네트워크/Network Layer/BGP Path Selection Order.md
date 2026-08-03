---
aliases:
  - BGP 경로 선택 순서
  - BGP Path Selection Order(BGP 경로 선택 순서)
---

- [[BGP]] 가 여러 후보 경로 중 하나 고르는 우선순위
- [[BGP Policy]] 우선 적용 후 아래 순서대로 비교

### 절차
1. LOCAL_PREF ↑ -> 같은 [[Autonomous System|AS]] 에서 나갈 때 높은 Preference
	- AS 의 관리자 의해 traffic 따라 결정

![[Routing-06.png]]

2. AS_PATH ↓ -> 지나는 AS 최소
3. MED ↓ -> 여러 입구로 들어올 수 있을 때 낮은 MED

![[Routing-07.png]]

4. [[eBGP]] > [[iBGP]]
5. Lowest IGP
6. Lowest router ID
