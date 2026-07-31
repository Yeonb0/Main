---
aliases:
  - 암묵적 형 변환
  - coercion(암묵적 형 변환)
  - Implicit Type Conversion
---

- 암묵적 형 변환
- [[타입 검사]] 시 operand 타입 호환 불가 -> 일부 compiler 가 자동 변환 수행 -> 호환 가능하게 만듦

### 특징
- compiler 수행 -> programmer 명시 X ↔ [[캐스팅]]
- 여러 [[데이터 타입]] 동시 표현 언어 -> [[형 변환]] 규칙으로 제공
- ==ex)== [[C]] : `short` -> `int`, `float` -> `double`
