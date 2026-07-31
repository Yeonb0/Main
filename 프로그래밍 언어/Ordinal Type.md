---
aliases:
  - 서수 타입
  - Ordinal Type(서수 타입)
---

- 가능한 값들의 범위를 양의 정수 집합과 연관 짓는 [[데이터 타입]]
- 서수 이용해 프로그래머가 직접 정의 -> user-defined ordinal type
- [[Readability|가독성]]↑

### 종류
- [[Enumeration Type]] : symbolic constant 를 순서대로 나열
- [[Subrange Type]] : 기존 type 의 일부 범위만 사용

### 구현
- Enumeration -> 음이 아닌 정수 ==(0 ~)== 와 연결
- Subrange -> parent 타입과 동일 구현 + range check
