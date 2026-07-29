---
aliases:
  - 스택
  - Stack
  - 스택(Stack)
---
- LIFO : Last In First Out

### Code
- `top` : 스택의 맨 위 (요소 in/out)
- `bottom` : 스택의 맨 아래
- `push` : `top` 에 자료 넣기
- `pop` : `top` 에서 자료 빼기

- stack 이 꽉차면 Overflow, 텅 비었으면 Underflow 발생

## [[ADT]]
### [[객체|Objects]]
- 0개 이상 원소를 가진 유한 순서 리스트

### [[함수|Functions]]
$\forall$ stack $\in$ `Stack`, item $\in$ `element`, maxStackSzie $\in$ `positive integer`

- `Stack` `CreateS(maxStackSize)`
	- `return` 최대 크기가 maxStackSize 인 빈 stack

- `Boolean` `IsFull(stack, maxStackSize)`
	- `if` (stack 원소 수 == maxStackSize)
		- `return` TRUE
		- `else return` FALSE

- `Stack` `Push(stack, item)`
	- `if` (`IsFull(stack)`)
		- `return` StackFull
	- `else`
		- `return` stack 의 top 에 item 삽입한 stack

- `Boolean` `IsEmpty(stack)`
	- `if` (stack == CreateS(maxStackSize))
		- `return` TRUE
		- `else return` FALSE

- `Element` `Pop(stack)`
	- `if` (`IsEmpty(stack)`)
		- `return`
	- `else` 
		- `return` stack 의 top 의 item 제거 
