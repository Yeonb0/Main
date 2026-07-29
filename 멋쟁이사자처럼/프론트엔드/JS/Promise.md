---
aliases:
  - 프로미스
  - promise
---

- [[비동기]] 작업의 성공 or 실패 / 그 결과값 나타내는 [[객체]]
- [[비동기]] 함수 (`fetch`) 들은 [[Promise|프로미스]] 반환

### 상태
- 대기(Pending) : 작업이 완료되지 않은 상태
- 성공 (Fulfilled) : [[비동기]] 작업이 성공적으로 마무리 된 상태
- 실패 (Rejected) : [[비동기]] 작업이 실패한 상태

### 함수
- `resolve` : [[Promise|promise]] 객체의 상태를 ==**성공**==으로 설정
	- `.then()` 실행
- `reject` : [[Promise|promise]] 객체의 상태를 ==**실패**==로 설정
	- `.catch()` 실행
- `all([배열])` : 여러 개의 [[Promise]] 객체를 받아 하나의 [[Promise]] 로 묶어 반환
	- `.then()` : 모든 [[Promise]]가 성공했을 때 실행
	- `.catch()` : 한 [[Promise]]라도 실패하면 실행
	  ```js
	  Promise.all([promise1, promise2, promise3])
  .then((results) => {
    // 모든 Promise가 성공했을 때 실행됨
    console.log(results); // [result1, result2, result3]
  })
  .catch((error) => {
    // 하나라도 실패하면 실행됨
    console.error(error);
  });
	  ```

### 핸들러

| `.then()`    | 프로미스가 ==**성공(fulfilled)했을 때 실행**==할 콜백 함수를 등록하고, 새로운 프로미스를 반환 |
| ------------ | ------------------------------------------------------------- |
| `.catch()`   | 프로미스가 ==**실패(rejected)했을 때 실행**==할 콜백 함수를 등록하고, 새로운 프로미스를 반환  |
| `.finally()` | 프로미스의 ==**성공/실패 상관없이 실행**==할 콜백 함수를 등록하고, 새로운 프로미스를 반환        |


```js
const promise=new Promise((resolve,reject)=>{
	console.log("2초 후 promise의 상태가 성공으로 바뀝니다");
	setTimeout(()=>{
		resolve("결과값이요"); //promise 객체의 상태를 성공으로 설정
	},2000);
});

// -- promise 성공 시 실행할 콜백을 등록
promise.then((value)=>{
	console.log(value); // "결과값이요" 출력
	console.log("성공"); // promise 객체의 상태가 성공일 때만 수행
}); 

// -- promise 실패 시 실행할 콜백을 등록
promise.catch((error)=>{
	console.log(error);
	console.log("실패"); // promise 객체의 상태가 실패일 때만 수행
}); 

// ----------------------------------- //
// then과 catch 메서드는 동일한 promise 객체를 반환
// 따라서 각 메서드를 이어 붙일 수 있음 
// → ** promise 체이닝 **

promise
	.then((value)=>{
	console.log(value);
})
	.catch((error)=>{
	console.log(error);
});
```