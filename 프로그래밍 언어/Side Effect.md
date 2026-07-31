---
aliases:
  - 부작용
  - Functional Side Effect
  - Side Effect(부작용)
---

- [[함수]]가 return 값 이외에 외부 [[변수]] or [[state|상태]] 변경
- [[Reliability|신뢰성]]↓ -> 허용 여부가 [[Subprogram]] 설계 이슈

### 언어별 대응
| 언어 | 처리 |
| --- | --- |
| Ada | 함수 [[매개 변수\|parameter]] 항상 in-mode -> side effect 방지 |
| Pascal, [[C]] | [[Pass-by-Value]] / [[Pass-by-Reference]] parameter -> side effect 함수 허용 |
