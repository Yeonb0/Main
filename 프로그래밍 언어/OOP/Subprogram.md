---
aliases:
  - 서브프로그램
  - Subprogram(서브프로그램)
---

- statement 모음의 [[추상화]] 단위 -> [[Process Abstraction]] 담당
- [[재사용(Reuse)|재사용]] -> 메모리 공간 & 코딩 시간 절약
- [[데이터]] 추상화 담당 -> [[ADT|ADT (Abstract Data Type)]]

### 특성
- 단일 진입점(single entry point) 보유
- caller 는 subprogram 실행 중 pause -> 주어진 시간에 subprogram 만 실행 중
- 실행 종료 -> caller 로 제어권 복귀

### 구성
| 항목 | 내용 |
| --- | --- |
| Subprogram definition | subprogram 추상화 동작 기술 |
| Subprogram call | 실행되도록 하는 명시적 요청 |
| Active | 실행 ~ 완료 전까지의 [[state\|상태]] |
| Subprogram header | definition 첫 줄, [[이름]] 제공 & [[매개 변수]] 목록 명시 |

- header ==ex)==
	- FORTRAN : `SUBROUTINE ADDER (parameters)`
	- Ada : `procedure ADDER (parameters) is`
	- [[C]] : `adder (parameters)` -> function 만 존재, 문맥으로 header 인식

### 종류
- Procedure : parameter 화 된 [[연산]] 정의 statement 모음 -> new statement 정의
	- caller 로 결과 전달 -> visible [[변수]] 변경 / formal parameter 변경
- [[함수|Function]] : 이름 + actual parameter 호출 -> user defined operator
	- 실행으로 생성된 값 -> 호출 코드로 반환
	- ==ex)== Pascal
```pascal
function power (base, exp : real) : real ;
  begin
    .....
  end
  .......
  result := 3.4 * power(10.0, x)
```
	- ==ex)== FORTRAN `Result = 3.4*10.0**x`

### 데이터 접근 방법
1. nonlocal 변수 직접 접근 (global, static 등) -> [[비지역 변수]]
	- 과도한 접근 -> [[Reliability|신뢰성]]↓
2. [[매개 변수|parameter]] 전달 -> parameterized computation
	- 어떤 computation 수행할지 parameter 가 결정
- 데이터 아닌 연산 전달 O -> subprogram 이름 자체를 parameter 로 사용

### 반환 타입
- 대부분 [[명령형 언어]] -> 반환 타입 제한

| 언어 | 반환 가능 타입 |
| --- | --- |
| FORTRAN 77 | 비구조적 타입(unstructured type) |
| Pascal, Modula-2 | 단순 타입 (integer, real, char, Boolean, pointer, enumeration) |
| [[C]] | [[배열]] & 함수 제외 모든 타입 |
| [[Java]], C# | 모든 타입 |

### 설계 이슈
- [[매개 변수]] 전달 방법 선택
- actual - formal parameter 타입 일치 검사 여부
- local 변수 static / dynamic 할당 -> [[지역 변수]]
- parameter 로 넘긴 subprogram 의 [[Referencing Environments|참조 환경]]
- 전달된 subprogram 호출 시 parameter [[타입 검사]] 여부
- overloading 가능 여부 -> [[오버로딩]]
- generic 가능 여부 -> [[Generic Subprogram]]
- separate / independent compilation 가능 여부
- side effect 허용 여부 -> [[Side Effect]]
