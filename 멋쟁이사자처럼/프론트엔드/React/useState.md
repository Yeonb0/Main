- [[React]]에서 가장 자주 사용하는 [[React Hook|Hook]] 중 하나
- [[함수형 컴포넌트]]에서 [[state]] 관리를 가능하게 함
- [[클래스형 컴포넌트]], [[반복문]], [[조건문]], 중첩된 [[함수]]에서 선언 불가
- `null` 같은 ==초기 상태 값== 필요

## 형태
- 2개의 값을 가진 배열 형태
```jsx
//useState의 기본 형태
const [state, setState] = useState(initialState)

//사용 예시
const [time, setTime] = useState(null)
const [age, setAge] = useState(30)
const [name, setName] = useState("Martin")
```

### `state`
- 첫 번째 인자 : 현재 [[state]]
- 첫 번째 [[렌더링]]에서는 전달한 `initialState` -> 숫자, 문자열, 배열 등

### `setState`
- [[state]]를 업데이트하고 [[리렌더링]] 을 발생 시키는 상태변화[[함수]]
	- [[컴포넌트]]가 [[리렌더링]] 됨
- [[비동기]]적으로 작동
	- [[비동기]] 함수 X / [[동기]] 함수지만 여러 상태 변화를 한 번에 처리하므로!
- 이전 상태의 값으로 `prev` 사용 

``` jsx
import React from "react";
import { useState } from "react";

const AppleExample = () => {
  // 상태 변수(apple)와 상태 업데이트 함수(setApple) 선언
  const [apple, setApple] = useState(100);

  const changeApple = () => {
    setApple((prev) => prev - 20);
  };

  return (
    <div>
      <span>apple: {apple}</span>
      <button onClick={changeApple}>20개 팔기</button>
    </div>
  );
};

export default AppleExample;
```


