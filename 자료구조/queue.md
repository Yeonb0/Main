---
aliases:
  - Queue
  - 큐
  - 큐(Queue)
---
- FIFO : First In First Out

### Code
- `front` : 가장 먼저 삽입된 위치. 삭제되는 곳
- `rear` : 가장 마지막 삽입 위치. 삽입되는 곳


- [[운영체제]]의 [[작업 스케줄링]]에 이용

## [[ADT]]
### [[객체|Objects]]
- 0개 이상의 원소를 가진 유한 순서 리스트

### [[함수|Functions]]
$\forall$ queue $\in$ `queue`, item $\in$ `element`, maxQueueSize $\in$ `positive integer`

- `Queue` `CreateQ(maxQueueSize)`
	- `return` 최대 크기가 maxQueueSize 인 공백 queue

- `Boolean` `IsFullQ(queue, maxQueueSize)`
	- `if` (queue 의 원소 수 == maxQueueSize)
		- `return` TRUE
		- `else return` FALSE

- `Queue` `AddQ(queue, item)`
	- `if` (`IsFullQ(queue)`) 
		- `return` queueFull
	- `else`
		- `return` rear 에 item 삽입한 queue 반환

- `Boolean` `IsEmptyQ(queue)`
	- `if` (queue == `CreateQ(maxQueueSize)`)
		- `return` TRUE
		- `else return` FALSE

- `Element` `DeleteQ(queue)`
	- `if` (`IsEmpty(queue)`)
		- `return`
	- `else`
		- `return` queue 의 front 에서 item 제거

### 파생
- [[원형 큐]]