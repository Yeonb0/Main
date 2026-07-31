---
aliases:
  - 포인터
  - Pointer(포인터)
---

- 값이 memory address 인 [[변수]]
- 아무것도 가리키지 않음 -> `nil`

### 용도
- 간접 주소 지정 ==(indirect addressing)== : 다른 [[변수]] 가리킴
- 동적 메모리 관리 ==(dynamic storage management)== : [[Heap]] 메모리 할당 / 해제

### 연산
- Assignment ==(대입)== : pointer 에 address 저장 -> [[C]] 의 `&`
``` c
int *aa, bb, cc; // aa 만 포인터 변수
aa = &bb; // aa에 bb의 주소 저장
```
- Dereferencing ==(역참조)== : pointer 가 가리키는 곳의 값 가져오기 -> C 의 `*`
``` c
cc = *aa; // cc에 aa가 가리키는 bb의 값 저장
```

![[Data-Types-06.png]]

- arithmetic ==(+ / -)== : 가리키는 type 크기 단위로 이동
``` c
char *c;
int  *i;

*(c + 1)   /* c가 가리키는 곳에서 1바이트 앞 */
*(i + 1)   /* i가 가리키는 곳에서 4바이트 앞 */
```

### 문제점
- [[Type Checking]]
- [[Dangling Pointer]] : `free` 된 동적 변수 주소를 가리키는 pointer
``` c
int *i;

sub1() {
    int j;
    j = 5;
    i = &j;
}

*i = ??
```
- Lost Object ==(Garbage)== : 접근 불가하지만 memory 공간 차지 중인 동적 [[객체]]
	- `free` X & 사용 X -> memory leak ==(메모리 누수)==
``` c
char *c;
c = malloc(...);   /* 첫 번째 할당 */
...
c = malloc(...);   /* 두 번째 할당 — 첫 번째 주소를 잃어버림 */
```

### 구현
- pointer 크기 -> word size
- 동적 변수 회수 -> [[Heap Management]]

#### [[Dangling Pointer]] 해결법
1. Tombstone Approch ==(묘비석 방식)==
	- 모든 동적 변수에 tombstone 이라는 중간 cell [[배치 처리|배치]]
	- pointer 는 변수를 직접 X, tombstone 을 가리킴
	- 동작
		- 동적 변수 할당 -> tombstone 생성 & 실제 변수 가리킴
		- 동적 변수 해제 -> tombstone `nil` 설정
		- 이후 pointer 접근 -> tombstone `nil` 이면 해제 판정

	![[Data-Types-07.png]]

	- 단점 : tombstone 유지 시간 & 공간 비용
2. Locks-and-key Approach
	- pointer 값을 (key, address) 쌍으로 표현, 동적 변수에 lock 값 함께 저장
	- 동작
		- 동적 변수 할당 -> lock 값 생성, pointer 의 key 에 같은 값 복사
		- pointer 복사 -> key 값도 함께 복사
		- 역참조 -> pointer 의 key 와 변수의 lock 비교, 일치 시 접근 허용
		- 동적 변수 해제 -> lock 값 삭제

	![[Data-Types-08.png]]
