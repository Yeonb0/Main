---
aliases:
  - JavaScript Object Notation
  - Attribute-Value
---

- [[JavaScript]] [[객체|Object]] Notation
- [[데이터]]를 저장하고 전송하기 위한 가벼운 데이터 형식
- 개방형 표준 포맷
- 속성 - 값 (Attribute-Value) 쌍 데이터 객체 전달 -> 텍스트 사용

- [[key]]-[[value]] 쌍으로 이루어진 구조

```js
{
  "name": "Alice",
  "age": 25,
  "isStudent": false,
  "skills": ["JavaScript", "Python", "C++"],
  "address": {
    "city": "Seoul",
    "zipCode": "12345"
  }
}
// JSON은 보통 객체 {} 또는 배열 [] 형태로 표현
```

- [[JSON API]]

### 인터페이스 구현
- [[_inbox/_done/인터페이스 구현]] 의 데이터 통신 포멧
- [[AJAX]] 에서 [[XML]] 대체
