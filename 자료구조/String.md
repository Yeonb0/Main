---
aliases:
  - 스트링
  - 문자열
  - string
---
## [[ADT]]
### [[객체|Objects]]
0개 이상 문자들의 유한 집합

### [[함수|Functions]]
$\forall s, t \in$ `String`, $i, j, m \in$ `non-negative integer`
- `String` `Null(m)`
	- `return` 최대 길이가 m 인 문자열. 초기는 NULL 로 설정

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