### `async`
- 함수 선언부에 `async`를 붙이면 [[Promise]]를 반환하는 [[비동기]] 함수로 만듬
- 항상 [[Promise|프로미스]] [[객체]] 를 `return`

```js
// 함수 선언식
async function func1() {
	const res = await fetch(url);  // 요청을 기다림
	const data = await res.json(); // JSON 형태의 응답을 JS 객체로 파싱
}
func1();

// 함수 표현식
const func2 = async () => {
	const res = await fetch(url);  // 요청을 기다림
	const data = await res.json(); // JSON 형태의 응답을 JS 객체로 파싱
}
func2();
```

### `await`
- `async` 함수 내부에서만 사용 가능한 키워드
- [[비동기]] 함수가 다 처리되길 기다림
- `promise.then()` 과 같은 역할

```js
// then 핸들러 방식
fetch(url)
    .then(res => res.json()) // JSON 형태의 응답을 JS 객체로 파싱
    .then(data => {
      // data 처리
      console.log(data);
    })

    
// await 방식
async function func() {
    const res = await fetch(url); // 요청을 기다림
    const data = await res.json(); // JSON 형태의 응답을 JS 객체로 파싱
    // data 처리
    console.log(data);
}
func();
```

### [[async & await]] [[예외 처리]]
- [[try & catch]] 문을 사용하자 
	- [[Promise]] 의 `catch()` 핸들러와 동일한 기능

```js
// async/await 방식
async function func() {
    try {
        const res = await fetch(url); // 요청을 기다림
        const data = await res.json(); // JSON 형태의 응답을 JS 객체로 파싱
        // data 처리
        console.log(data);
    } catch (err) {
        // 에러 처리
        console.error(err);
    } finally{
	    console.log("이 구문은 에러가 나든 안나든 항상 수행돼요"); // 성공/실패 관계없이 항상 실행
    }
}
func();
```
