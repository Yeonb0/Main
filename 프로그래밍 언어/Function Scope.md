- [[변수]]가 선언된 함수 내부에서만 접근 가능
```js
function abc() {
	if(true) {
		var x = "hello";
		console.log(x); //정상 출력
	}
	console.log(x); //정상 출력
}

abc();
```

- [[var]]