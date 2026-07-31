---
aliases:
  - 힙 관리
  - Heap Management(힙 관리)
---

- [[Heap]] 영역 동적 [[변수]]의 할당 & 회수 관리
- 가정 : heap 은 고정 크기로 할당된 공간, 사용 가능 cell 은 [[Linked List]] 로 연결 관리
- 해제가 암묵적 수행 -> 회수 시점 결정 필요

### Reference Counter
- 참조 카운터 -> 점진적 회수 ==(incremental reclamation)==
- 모든 cell 에 counter [[배치 처리|배치]] -> 현재 그 cell 을 가리키는 [[Pointer]] 수 저장
	- pointer 가 가리킴 -> counter↑
	- pointer 가 떠남 -> counter↓
	- counter == 0 -> memory 회수
- 단점
	- counter 저장 공간 overhead
	- counter 유지 실행 시간 overhead
	- circular reference -> 서로를 가리키는 두 [[객체]]의 counter 절대 0 X

![[Data-Types-09.png]]

### [[가비지 컬렉션]]
- 일괄 회수 ==(batch reclamation)==
- run-time 시스템이 memory 계속 할당 -> 모두 소진 시 한꺼번에 garbage 수거
