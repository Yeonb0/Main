- [[변수]]가 선언된 [[Block]] 내부에서만 변수에 접근 가능
- 일반적인 [[프로그래밍 언어]]에서 기본값

```js
function abc() {
	if(true) {
		let x = "hello";
		console.log(x); //정상 출력
	}
	console.log(x); //Reference Error
}

abc();
```

- [[let]]