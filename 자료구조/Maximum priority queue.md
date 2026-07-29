---
aliases:
  - 최대 우선순위 큐
---
## [[ADT]]
### [[객체|Objects]]
- n > 0 인 element 들의 모임. 각 element 는 key 를 가지고 있음

### [[함수|Functions]]
$\forall$ q $\in$ `MaxPriorityQueue`, item $\in$ `Element`, n $\in$ `integer`

- `MaxPriorityQueue` `create(max_size)`
	- `return` 빈 priority queue 생성

- `Boolean` `isEmpty(q, n)`
	- `if` (n > 0)
		- `return` TRUE
		- `else return` FALSE

- `Element` `top(q, n)`
	- `if` (!`isEmpty(q, n)`)
		- `return` q 에서 가장 큰 element
	- `else return` error

- `Element` `pop(q, n)`
	- `if` (!`isEmpty(q, n)`)
		- `return` q 에서 가장 큰 element

- `MaxPriorityQueue` `push(q, item, n)`
	- `return` pq 에 item 을 삽입한 우선순위 큐