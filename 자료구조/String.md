---
aliases:
  - 스트링
  - 문자열
  - string
  - Character String Type
  - 문자열 타입
---

## [[ADT]]
### [[객체|Objects]]
0개 이상 문자들의 유한 집합

### [[함수|Functions]]
$\forall s, t \in$ `String`, $i, j, m \in$ `non-negative integer`
- `String` `Null(m)`
	- `return` 최대 길이가 m 인 [[String|문자열]]. 초기는 NULL 로 설정

- `Integer` `Compare(s, t)`
	- `if` (s == t) 
		- `return` 0
	- `else if` (s > t)
		- `return` -1
		- `else return` +1

- `Boolean` `IsNull(s)`
	- `if` (`Compare(s, Null)`) 
		- `return` FALSE
		- `else return` TRUE

- `Integer` `Length(s)`
	- `if` (`Compare(s,Null)`)
		- `return` s 의 문자 수
		- `else return` 0

- `String` `Concat(s, t)`
	- `if` (`Compare(s, NULL)`)
		- `return` s 뒤에 t 를 붙인 문자열
		- `else return` s

- `String` `Substr(s, i, j)`
	- `if` ((j > 0) && (i + j - 1) < `Length(s)`)
		- `return` s 에서 i ~ j 구간 문자열
		- `else return` NULL

### 패턴 매칭 함수

### Character String Type
- non-primitive [[데이터 타입]] -> 하드웨어 지원 X, but [[Writability|작성 용이성]] 위해 언어 차원 지원
- Design Issue
	- 언어가 기본 제공 vs. char 의 [[배열]] ==([[C]])==
	- 문자열 길이가 static vs. dynamic
- 언어별 지원
	- [[C]] / C++ : 기본 타입 X, library 로 제공
	- Perl, [[JavaScript]], Ruby, PHP : language 레벨 제공

#### Primitive or Character Array
- special kind of character array
	- 단일 문자의 배열로 저장
	- [[C]] 의 string -> 끝에 `\0` ==(null)== 붙은 char 배열
- primitive data type
	- 언어 자체가 string type 제공 -> writability↑
	- assignment, relational operator, catenation, 부분 문자열 참조 등 [[연산]] 제공

#### 길이
- static length string : 선언 시 길이 static 저장 -> 저장 후 변경 X
- dynamic length string : 최대 제한 X, assign 마다 길이 설정 -> allocation overhead
- 각각 tradeoff 존재

#### 구현
- descriptor : [[변수]]의 attribute 모음
	- compile-time descriptor : static 문자열, compile 시 생성된 정보 보유
	- run-time descriptor : limited dynamic 문자열, 수행 도중 정보 보유
- dynamic allocation
	- [[Linked List]] 저장 -> 연속 X
	- 인접 memory cell 저장 -> 빠른 참조 & 적은 저장 공간, but 확장 시 복사 필요 & allocation 느림

#### 평가
- string type -> 언어의 [[Writability|작성 용이성]]에 중요
- 구현 비용 크지 않음 -> 제공 권장
