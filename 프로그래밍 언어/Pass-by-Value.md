---
aliases:
  - call-by-value
  - 값에 의한 전달
  - Pass-by-Value(값에 의한 전달)
---

- actual parameter 값 -> 대응 formal parameter 초기화에 사용
- in-mode (actual -> formal)
- formal parameter 가 subprogram 내 [[지역 변수]]처럼 동작
- 실제 [[데이터]] 전송으로 구현 -> 원본 변경 X

### 단점
- parameter 가 큰 객체 -> 복사 비용↑

### 구현
- 값이 [[stack]] 위치에 복사

### 특징
- 대부분 언어의 기본 [[매개 변수]] 전달 방식
- ==ex)== [[C]], [[Java]]
