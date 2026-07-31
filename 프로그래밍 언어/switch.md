---
aliases:
  - switch statement
  - switch 문
  - case 문
---

- 여러 문장 · 문장 그룹 중 하나 선택하는 [[조건문]]
- Multiple Selection Constructs 대표 형태

### case
- ALGOL-W · Pascal
``` pascal
case expression of
    constant_list_1 : statement_1 ;
    ....
    constant_list_n : statement_n ;
end

case index of
    1,3 : begin
            odd := odd + 1 ;
          end
    2,4 : begin
            even := even + 1 ;
          end
    else writeln ("Error in case") ;
end
```

### switch
- [[C]]
- 조건식 -> integer type
- `break` 로 explicit branching -> 누락 시 이후 case 연속 실행
``` c
switch (index) {
    case 1 :
    case 3 : odd += 1 ;
             break ;   // 명시적 분기(explicit branching)
    case 2 :
    case 4 : even += 1 ;
             break ;
    default : printf("Error in switch");
}
```

### 조건 나열 형태
- [[Python]]
``` python
case
    when count < 10 then bag1 = true
    when count < 100 then bag2 = true
    when count < 1000 then bag3 = true
end
```
