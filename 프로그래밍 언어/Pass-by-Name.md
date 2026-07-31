---
aliases:
  - 이름에 의한 전달
  - Pass-by-Name(이름에 의한 전달)
---

- inout-mode (actual <-> formal)
- actual [[매개 변수|parameter]] -> formal parameter 에 텍스트적으로 치환
- late binding : 호출 시점엔 접근 방법만 [[바인딩]], 값 or 주소 실제 바인딩은 할당 · 참조 시까지 [[Delay|지연]]
	- 같은 formal parameter 참조마다 값 변화 O

### 형태별 구현
| actual parameter | 구현 |
| --- | --- |
| [[변수]] | [[Pass-by-Reference]] |
| [[상수]] | [[Pass-by-Value]] |
| [[배열]] 원소 / 변수 포함 표현식 | 참조마다 값 변화 O |

### 장점
- 유연성

### 단점
- 처리 속도 느림
- 구현 어려움
- read & write 어려움

### 구현
- thunk 사용 : parameter 없는 procedure / run-time 상주 code segment
	- 비용 높음
	- 호출된 subprogram 내의 pass-by-name parameter 모든 참조마다 호출
	- [[Referencing Environments|참조 환경]]에서 참조 평가 & actual parameter 주소 반환

### 활용
- [[Jensen's Device]]
