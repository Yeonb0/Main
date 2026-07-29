- [[JavaScript|JS]] 에서의 [[변수]] 선언 방법
- [[선언]] / [[할당]] 따로 가능

### [[Scope]]
- [[Block Scope]]
- [[Block]] 외부로부터의 접근 불허

### 중복 선언
- 같은 이름의 변수 중복 선언 허용 X

### [[호이스팅]]
- 호이스팅 발생 O, 초기화 X
- [[TDZ]] error 발생
```js
console.log(y) // ReferenceError
let y = 5
```
