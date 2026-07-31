---
aliases:
  - 결과에 의한 전달
  - Pass-by-Result(결과에 의한 전달)
---

- out-mode (actual <- formal)
- subprogram 으로 값 전달 X
- formal [[매개 변수|parameter]] 가 [[지역 변수]]처럼 동작 -> return 시 caller 의 actual parameter 로 전달
	- 이때 actual parameter 는 반드시 [[변수]]

### 문제점
- 추가 저장 공간 & move [[연산]] 비용
- actual parameter collision
```c
subroutine sub(x, y) {
    x = 3;
    y = 5;
}
main() {
    int p1;
    sub(p1, p1);
    p1???
}
```
- actual parameter 주소 평가 시점 모호
```c
int index, list[10];

subroutine sub(a) {
    index = 5;
    a = 3;
}
main() {
    index = 3;
    sub(list[index]);
}
```

### 구현
- actual parameter 값 [[stack]] 저장 -> subprogram 종료 시 호출 프로그램이 회수
