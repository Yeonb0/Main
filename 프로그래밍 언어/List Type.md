---
aliases:
  - 리스트 타입
  - List Type(리스트 타입)
---

- 원소를 순서대로 나열한 타입, 원소 type 제약 X
- [[Python]] 의 list -> [[배열]] 역할 겸함 ==(사실상 heterogeneous array)==
	- 타 언어와 달리 가변 -> 수정 O
	- 원소는 어떤 type 이라도 가능
``` python
# 리스트 생성
myList = [3, 5.8, "grape"] 

# 원소 접근 (index 는 0부터)
x = myList[1] # x = 5.8

# 원소 삭제 
del myList[1]
```

### List Comprehension
- 수학의 집합 표기법에서 유래
- 간결, but [[Readability 1|가독성]]↓
``` python
[x * x for x in range(7) if x % 3 == 0]
# [0, 9, 36]

[x * x for x in range(6) if x % 3 == 0]
# [0, 9]
```
