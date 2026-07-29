- `fetch()` [[함수]]를 이용해 [[API]] [[요청]] 을 보내면, [[서버]]가 주로 [[JSON]] 데이터 응답

### `fetch()`
- [[브라우저]] 또는 [[JavaScript|JS]] 환경이 제공하는 [[Web API]]
- [[Promise]] [[객체]] 를 반환
	-> [[비동기]] 처리 완료 후 [[응답]] 객체 전달


```js
fetch('https://example.com/users/1')  // API 호출
  .then(response => response.json()) // JSON 형태의 응답을 JS 객체로 파싱
  .then(data => console.log(data)); // 변환된 데이터를 받아서 사용
```
- `response` 라는 이름으로 [[응답]] 객체 받음 (다른 이름 사용 가능)
	- `fetch()` 가 반환한 [[HTTP]] [[응답]]의 body 를 [[JSON]] 으로 파싱
- `data` 라는 이름으로 [[데이터]] 객체 받음 (다은 이름 사용 가능)
	- `reponse.json()` 으로 변환된 [[JavaScript|JS]] 객체에서 [[데이터]] 부분 사용