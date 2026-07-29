- [[JavaScript|JS]] 에서의 [[변수]] 선언 방법

### [[Scope]]
- [[Function Scope]] 가짐

### 중복 선언
- 같은 이름의 변수 중복 선언 허용 O

### [[호이스팅]]
- 호이스팅 발생 O, undefined 로 초기화
```js
var x // 선언부만 최상단으로 이동
console.log(x) // undefined
x = 5 // 할당은 원래 위치에서 실행
console.log(x)
```