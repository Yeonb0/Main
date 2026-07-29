- [[CSS]]에서 요소들의 위치를 결정하는 속성

### `static`
- 특별한 위치 지정 X. 문서의 흐름을 따름
- `default` 값
```css
.box {
	position: static;
}
```
![[Pasted image 20260702104803.png]]

### `relative` 
- 현재 위치를 기준으로 이동할 수 있음
- 원래 위치에서 이동해보이는 것일 뿐 -> 원래 자리 공간은 그대로 유지 (비어있음)
- `absolute` 와 함께 쓰일 때 부모 요소의 기준
```css
.box {
  position: relative;
  top: 20px; /* 원래 위치와 위에서 20px 떨어짐 */
  left: 10px; /* 원래 위치와 왼쪽에서 10px 떨어짐 */
}
```
![[Pasted image 20260702105035.png]]

### `absolute`
- 가까운 `relative` 부모 기준으로 이동
	- `relative` 부모가 없으면 `body`(문서 전체) 기준
```css
.parent {
  position: relative; /* 기준이 될 부모 */
}

.child {
  position: absolute;
  top: 20px; /* parent와 위에서 20px 떨어짐*/
  left: 100px; /* parent와 왼쪽에서 100px 떨어짐 */
}
```
![[Pasted image 20260702110756.png]]

### `fixed`
- 스크롤 해도 고정된 위치에 유지
	- 화면 자체가 기준
	- 네비게이션 바, 사이드 메뉴, 특정 버튼에 자주 사용
```css
.box {
  position: fixed;
  top: 10px; /* 화면과 위에서 50px 떨어짐*/
  right: 10px; /* 화면과 오른쪽에서 100px 떨어짐*/
}
```
![[Mar-16-2025 17-43-58.gif]]

### `sticky`
- 스크롤 위치에 따라 `relative` 처럼 동작하다가 특정 지점부터 `fixed` 처럼 고정되는 속성
	- 부모 요소의 범위를 벗어나면 다시 원래 흐름으로 복귀
	- offset 값을 반드시 지정해야 함
```css
.sticky-element {
  position: sticky;
  top: 0; /* 이 지점 도달하면 fixed 처럼 동작 */
}
```
![[ezgif.com-gif-maker.gif]]