- [[리렌더링]] 없이 값을 저장 or [[DOM]] 요소에 직접 접근 시 사용
	- 값을 바꾸어도 [[리렌더링]] X
- 처음에 제공한 `초기값` 으로 설정된 ==단일== `current` 속성이 있는 `ref` [[객체]] 반환

```jsx
{
  current: 0
}
```
-> `current` 속성 이용해 값 저장 / [[DOM]] 요소 참조 가능

### 값 저장
```jsx
import React, { useRef, useState } from "react";

const ClickCounter = () => {
  const [, forceUpdate] = useState(0);
  const count = useRef(0);

  const handleClick = () => {
    count.current += 1;
    console.log(`${count.current}`); // 값 확인
  };

  const onClickForceUpdate = () => {
    forceUpdate((prev) => prev + 1);
  };

  return (
    <div>
      <button onClick={handleClick}>Count 증가 버튼</button>
      <p>count: {count.current}</p>
      <button onClick={onClickForceUpdate}>리렌더링 유발 버튼</button>
    </div>
  );
};

export default ClickCounter;
```
- `forceUpdate` 통해 강제 [[리렌더링]] 발생 시켜도 값 초기화 되지 않고 유지

### [[DOM]] 조작
```jsx
import React, { useRef } from 'react';

function FocusInput() {
  const inputRef = useRef(null); // input 요소를 참조하기 위한 ref 생성

  const handleFocus = () => {
	  console.log(inputRef.current)
    inputRef.current.focus(); // input 요소에 포커스
  };

  return (
    <div>
      <input ref={inputRef} type="text" placeholder="Type something" />
      <button onClick={handleFocus}>Focus Input</button>
    </div>
  );
}

export default FocusInput;
```
- 특정 [[HTML]] 요소 관리 -> `attribute` 에 `ref={inputRef}` 와 같이 작성
	- `inputRef` 가 `<input>` 태그를 참조
- 버튼 클릭 시, `handleFocus` 함수 통해 `inputRef.current.focus()` 실행
  -> `inputRef` 가 참조하고 있는 `<input>` 태그로 focus

### 주의 사항
- [[렌더링]] 중에 `ref.current` 쓰거나 읽는 것 주의!
```jsx
//🚨 렌더링 중에는 ref 객체의 current에 값을 쓰면 안됩니다!
  myRef.current = 123;
//🚨 렌더링 중에는 ref 객체의 current의 값을 읽으면 안됩니다!
  <h1>{myOtherRef.current}</h1>;
```
- [[DOM]] 요소가 아직 존재 X / 이전 상태의 [[DOM]] 참조 가능성 O


