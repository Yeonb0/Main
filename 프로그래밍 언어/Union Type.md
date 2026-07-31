---
aliases:
  - 공용체 타입
  - Union Type(공용체 타입)
---

- 같은 memory 공간에 서로 다른 type 값이 번갈아 저장 가능한 [[Data Structure|자료 구조]]

### Storage Allocation
- 크기 가장 큰 [[변수]] 기준으로 공간 확보 -> 나머지는 앞부분만 사용
- ==ex)==
``` pascal
type shape = (circle, triangle, rectangle) ;
object =
  record
    case form : shape of
      circle    : (diameter : real) ;
      triangle  : (leftside : integer; rightside : integer; angle : real) ;
      rectangle : (side1 : integer; side2 : integer)
  end ;

var thing : object
```

![[Data-Types-04.png]]

### 구현
- discriminated union -> 모든 variant 가 같은 주소 사용
	- 제일 큰 변수 기준 storage 크기 결정
- ==ex)== Ada
``` pascal
type NODE (TAG : BOOLEAN) is
  record
    case TAG is
      when TRUE  => COUNT : Integer
      when FALSE => SUM   : char
    end case;
  end record;
```
- `TAG` == `TRUE` -> `COUNT(Integer)` [[필드]] 사용 -> 이만큼 공간 할당
- `TAG` == `FALSE` -> `SUM(char)` 필드 사용 -> 같은 memory 주소 공유

![[Data-Types-05.png]]

- `tag` : 현재 저장된 값이 어떤 type 인지 표시
	- tag 자체도 저장 공간 차지
- safety issue 존재
