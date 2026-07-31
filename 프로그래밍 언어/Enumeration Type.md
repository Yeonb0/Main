---
aliases:
  - 열거형 타입
  - Enumeration Type(열거형 타입)
---

- symbolic constant 를 순서대로 나열한 [[Ordinal Type]]
- 실제 구현 -> integer 로 변환되어 수행
	- 순서 비교 O
	- 산술 [[연산]] X
	- range error 발견 쉬움
- 지원 [[연산]] : Predecessor, Successor, [[Position]], Values

### 예시
``` csharp
type DAYS is (Mon, Tue, Wed, Thu, Fri, Sat, Sun) ; 
type WEKEND is (Sat, Sun) ;
int i;
DAYS a;
a = Mon; 
```
- `DAYS` -> Mon, Tue, Wed, Thu, Fri, Sat, Sun 중 한 값 보유
- in [[C]], C++
``` c
enum day {sun, mon, tue, wed, thr, fri, sat} d1, d2;
```
- sun ~ sat 값 가질 수 있는 [[변수]] d1, d2 선언
