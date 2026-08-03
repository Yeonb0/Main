---
aliases:
  - external BGP
  - eBGP(external BGP)
---

- 다른 [[Autonomous System|AS]] 의 [[Border Router]] 끼리 정보 교환
- Distance vector + path -> path 까지 전체 전송하는 path vector routing

![[Routing-03.png]]

### 특징
- ==ex)== 30번이 123번 가고 싶을 때 -> `30 → 14 → 56 → 123` 이동
- Multi path 가능
	- 가장 shortest 여도 정책 따라 다른 route 선택 O
	- ==ex)== 123 가는 길 2개

### route advertisement
- 연결된 AS 의 route router 에게 전달
- path 를 전송 -> loop 발견 O
- path 에 전달할 router 번호 있으면 전송 X
