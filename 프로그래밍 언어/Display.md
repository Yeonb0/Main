---
aliases:
  - 디스플레이
  - 디스플레이(Display)
---

- static link 를 [[Activation Record]] 가 아닌 display 에 모아 저장
- display : 단일 [[배열]], 특정 시점에 접근 가능한 activation record [[인스턴스|instance]] 의 주소 목록

### 참조
- nonlocal 참조 = `(display_offset, local_offset)`

| 항목 | 내용 |
| --- | --- |
| display_offset | display 안의 올바른 record 로의 link, static 하게 계산 |
| local_offset | [[Static Chain]] 과 동일 방식으로 계산 & 사용 |

- display 의 `k` 번째 pointer -> static_depth 가 `k` 인 activation record instance 가리킴

### 수정 절차
1. static_depth `k` 인 procedure `P` 호출 -> new record 에 display `k` 번째 pointer 의 복사본 저장
2. display `k` 번째 위치에 `P` 의 record 로의 link 저장
3. procedure 종료 -> record 에 저장해 둔 pointer 를 display 에 복원

![[Implementing-Subprograms-06.png]]

### 구현
- display 최대 크기 = subprogram 의 최대 static_depth -> compiler 결정
- memory 에 runtime static array 저장 -> nonlocal 은 local 보다 memory cycle 1회 추가
- register 저장 -> 추가 memory cycle X

### [[Static Chain|Static chaining]] 과 비교
- display memory 저장 -> nonlocal 참조 static chaining 보다 느림
- static level 이 ==1개 이상== 떨어진 nonlocal 참조 -> display 가 더 빠름
- display -> 모든 nonlocal 참조 시간 동일
- static chain -> callee 의 static level 이 멀지 않으면 유지 비용 유리
- static nest 깊음 + 먼 nonlocal 참조 多 -> Display
- nest 적음 + 먼 nonlocal 참조 少 -> Static chaining (일반적)
