- 동시에 발생한 [[업데이트]]들을 모아서 [[DOM]] 수정 횟수를 최소화 하도록 처리

### Render Phase
- [[컴포넌트]]를 계산하고 [[업데이트]] 사항을 파악
- 변경된 [[state]]나 [[Props]]를 기반으로 어떤 UI 를 그려야 하는지 계산
- 실제 [[DOM]]에는 변경 X

React 가 `React Component` 를 호출하면 내부적으로 [[컴포넌트]] 실행 결과 계산
```jsx
function App() {
  return <h1>Hello React!</h1>;
}
```
-> React 내부에선 이 결과값으로 [[객체]] 형태의 [[React Element]] 반환
-> [[React Element]] 를 모아 [[Virtual DOM]]에 [[트리]] 형태로 구조화
![[Pasted image 20260703201541.png]]

### Commit Phase
- 실제 [[DOM]]에 변경 사항을 적용
- Render Phase 에서 계산한 결과를 실제로 반영
- 이후 Critical Rendering Path 거쳐 화면에 렌더링

-> 변경이 필요한 [[DOM]] 작업만 모아서 최소한으로 수정 
![[Pasted image 20260703202218.png]]