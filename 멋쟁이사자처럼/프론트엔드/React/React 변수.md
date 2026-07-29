### 일반 [[변수]]
- 값이 바뀌어도 [[리렌더링]] X
- [[컴포넌트]]가 다시 [[렌더링]] 되면 값 초기화

### [[useState]]
- 값이 바뀌면 [[리렌더링]] O
- 화면에 바로 반영되어야 하는 값 관리

### [[useRef]]
- 값이 바뀌어도 [[리렌더링]] X
- [[컴포넌트]]가 다시 [[렌더링]] 되어도 값 유지
- 화면에 바로 반영 X, 값 기억은 필요할 때

```jsx
import React, { useState, useRef } from "react";

function CounterExample() {
  // useState: 값이 변경되면 리렌더링 발생
  const [stateCount, setStateCount] = useState(0);

  // useRef: 값이 변경되어도 리렌더링되지 않음
  const refCount = useRef(0);

  // 일반 변수: 리렌더링되면 값이 초기화됨
  let varCount = 0;

  return (
    <div>
      <p>stateCount : {stateCount}</p>
      <p>refCount : {refCount.current}</p>
      <p>varCount : {varCount}</p>

      <button onClick={() => setStateCount(stateCount + 1)}>state up</button>
      <button
        onClick={() => {
          refCount.current += 1;
          console.log("refCount:", refCount.current);
        }}
      >
        ref up
      </button>
      <button
        onClick={() => {
          varCount += 1;
          console.log("varCount:", varCount);
        }}
      >
        var up
      </button>
    </div>
  );
}

export default CounterExample;

```