- `JSON.parse()` : [[문자열]] -> [[배열]] 변환 [[함수]]
- `JSON.stringify()` : [[배열]] -> [[문자열]] 반환 [[함수]]
	- [[배열]] 데이터를 [[로컬 스토리지]]에 저장/불러올 때 사용
```js
// 배열 → 문자열(JSON 형식)로 변환하여 저장
localStorage.setItem("array", JSON.stringify(["123", "456"]));

// 문자열 → 배열(ex. ["123","456"])로 변환
const arrayData = JSON.parse(localStorage.getItem("array"));
```


