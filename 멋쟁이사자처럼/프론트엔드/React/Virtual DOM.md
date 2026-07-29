- [[DOM]]을 [[JavaScript|JS]] [[객체]]로 흉내낸 것. 일종의 복제판
- 여러 개의 [[React Element]] 를 모아 [[트리]] 형태로 구조화


### 작동 원리
1. 실제 [[DOM]]의 사본인 [[Virtual DOM]]을 [[메모리]]에서 유지
2. [[업데이트]]를 계산해 new [[Virtual DOM]] vs 기존 [[Virtual DOM]] 차이 계산
3. 변경된 부분만 실제 [[DOM]] 에 반영
-> [[DOM]] 조작 최소화. 성능 최적화 + 빠른 렌더링 속도

![[Pasted image 20260703201521.png]]