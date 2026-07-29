---
aliases:
  - 프롭스
  - props
---
- 부모 [[컴포넌트]] -> 자식 [[컴포넌트]]로 전달되는 [[데이터]] [[객체]]
	- 읽기 전용 데이터 -> 자식에서 수정 불가
	- 부모에서 값 수정 -> 자식에게 new 값 전달

### 데이터 전달 방법
```jsx
// Parent.jsx (부모 컴포넌트)
import React from 'react';
import Child from './Child';

const Parent = () => {
  const message = "React는 신기방기";
  const userName = "홍길동";

  return (
    <div>
      <h1>부모 컴포넌트</h1>
      {/* props로 데이터 전달 */}
      <Child message={message} userName={userName} />
    </div>
  );
};

export default Parent;
```

1. [[구조 분해 할당]] 사용
```jsx
// Child.jsx (자식 컴포넌트) 1안
import React from 'react';

const Child = ({ userName, message}) => {
  return (
    <div>
      <h2>자식 컴포넌트</h2>
      <p>{userName}: {message}</p>
    </div>
  );
};

export default Child;
```

2. [[Props|props]] 자체로 사용
```jsx
// Child.jsx (자식 컴포넌트) 2안
import React from 'react';

const Child = (props) => {
  return (
    <div>
      <h2>자식 컴포넌트</h2>
      <p>{props.username}: {props.message}</p>
    </div>
  );
};

export default Child;
```

- 자식 [[컴포넌트]] 에서 [[Props|props]]를 전달받지 않았을 때 기본값 설정 가능
	- [[Props|props]]가 전달되지 않을 때, [[undefined]] 일 때 사용
	- [[null]] 이나 빈 문자열 `""` 이면 사용 X
```jsx
// Child.jsx (자식 컴포넌트)
import React from 'react';

// username의 기본값 지정
const Child = ({ message, userName = "김첨지" }) => {
  return (
    <div>
      <h2>자식 컴포넌트</h2>
      <p>{userName}: {message}</p>
    </div>
  );
};

export default Child;
```

### [[HTML]] 전달 방법
- `children`
	- [[React]]에서 예약된 [[Props|props]]
	- <자식 컴포넌트>내용</자식 컴포넌트> -> 자체를 [[Props|props]]로 받을 수 있게 해줌

```jsx
// Parent.jsx (부모 컴포넌트)
import React from 'react';
import Child from './Child';

const Parent = () => {
  const message = "React는 신기방기";
  const userName = "홍길동";

  return (
    <div>
      <h1>부모 컴포넌트</h1>
      {/* props로 데이터 전달 */}
      <Child message={message} userName={userName} >
	      <p>저는 props로 전달된 HTML 자식입니다!</p>
	    </Child>
    </div>
  );
};

export default Parent;
```

```jsx
// Child.jsx (자식 컴포넌트) 1안
import React from 'react';

const Child = ({ message, userName, children }) => {
  return (
    <div>
      <h2>자식 컴포넌트</h2>
      <p>{userName}: {message}</p>
      {children}
    </div>
  );
};

export default Child;
```