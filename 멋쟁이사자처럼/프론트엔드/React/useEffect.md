- [[컴포넌트]]의 [[렌더링]] 과정과 [[사이드 이펙트]]를 분리해서 수행
![[Pasted image 20260704075943.png]]
- 어떤 값이 변경될 때마다 특정 코드 실행
- 외부 세계 상호 작용 + [[컴포넌트]]의 렌더링 or 성능에는 영향을 미치지 않도록
- [[컴포넌트]]의 [[렌더링]]이 끝난 후에 [[사이드 이펙트]]를 수행하게 함

## 형태
```jsx
useEffect(callback, deps)
```
- `callback` : 실행하고자 하는 [[콜백 함수]]
- `deps` (Dependency Array) : 의존성 [[배열]], 배열 요소의 값이 변경될 때마다 [[콜백 함수]] 실행
	- 언제 실행하지 결정

### `deps`
- 생략하는 경우 : [[useEffect]]가 선언된 [[컴포넌트]]가 [[렌더링]]될 때마다 `callback` 실행
- `[]` 빈 배열일 경우 : [[컴포넌트]]가 처음 [[렌더링]] 될 때 한 번만 실행하게 됨
	- [[API]] 호출 시 가장 많이 사용 -> 페이지 열릴 때 딱 한 번만 데이터 가져오므로
- 의존 요소가 존재할 경우 : 의존 요소가 변경될 때마다 `callback` 실행
```jsx
useEffect(() => {
  console.log(`업뎃 후 text 길이:${text.length}`); // 1

  return () => {
    console.log(`업뎃 전 text 길이:${text.length}`); // 2
  };

}, [text]);

// 사후르 -> 1 -> 클릭 -> 2 -> 퉁사후르 -> 1 -> 클릭 -> 2 -> 퉁퉁사후르 -> 1 ...
```
### 클린업 함수
- [[useEffect]]가 다시 실행되기 전 이전 작업을 정리해주는 함수

### 예제
```jsx
import { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

function ChatRoom({ roomId }) {
  const [serverUrl, setServerUrl] = useState('https://localhost:1234');

  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => {
      connection.disconnect();
    };
  }, [serverUrl, roomId]);
  // ...
}
```
- [[컴포넌트]]를 [[외부 시스템]]과 연결하기 위해선 [[컴포넌트]] 최상위 레벨에서 [[useEffect]] 호출해야 함


