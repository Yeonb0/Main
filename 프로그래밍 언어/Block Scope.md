---
aliases:
  - Block
  - block
  - 블록
  - 블록(Block)
---

- 중괄호 `{}` 로 묶인 부분
- [[Compound Statement]] + [[변수]] 선언 -> [[Block 1|block]]
- ==ex)== [[C]] `{}` / [[Python]] indentation

### [[조건문]]
- [[if]]
- [[switch]]

### [[반복문]]
- [[for]]
- [[while]]

### 구현
- Block = [[데이터]] 선언 + 여러 문장
1. 항상 같은 위치에서 호출되는 parameterless procedure 취급
	- 최대 nest ↑ -> [[Display]] 크기 ↑
2. block 변수에 필요한 공간을 [[Activation Record]] 내 local 변수 옆에 할당
	- block 변수 offset static 하게 계산 O

![[Implementing-Subprograms-07.png]]

- 두 block 동시 동작 X -> 같은 offset 공간 공유
