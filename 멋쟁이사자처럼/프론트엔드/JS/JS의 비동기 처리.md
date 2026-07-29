- [[자바스크립트 엔진]]의 [[Call Stack]] 이 비어있으면 [[Event Loop]] 가 [[Callback Queue]] 에서 대기 중인 작업을 불러와 실행 

## 발전 과정
### 콜백
- [[콜백 함수]] 내에서 [[콜백 함수]]를 반복해서 호출하는 방식

```js
function getDB(callback) {
    // 데이터베이스로부터 3초 후에 데이터 값을 받아온 후, 콜백 함수 호출
    setTimeout(() => {
        const value = 100;
        callback(value);
    }, 3000);
}

function main() {
    // 호출할 작업에 콜백 함수를 넘긴다
    getDB(function(value) {
        let data = value * 2;
        console.log('data의 값 : ', data);
    });
}
main();
```

- 문제점 : [[콜백 지옥]]

### `Promise`
- [[Promise]] 객체 활용 
- 문제점 : [[Promise hell]]

### `async` & `await`
- [[async & await]]
-> [[비동기]]적 [[API fetch]]
