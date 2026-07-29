- 컨테이너 내 요소들을 정렬 & 배치하는데 사용

### `display` 속성
```css
display: flex;
```
- 컨테이너가 [[Flexbox]]로 설정. 내부 요소들이 자동으로 Flexitem 이 됨.

### `flex-direction` 속성
- main 축의 방향 결정
```css
flex-direction: row; /* 기본값 */
flex-direction: row-reverse;
flex-direction: column;
flex-direction: column-reverse;
```
![[Pasted image 20260702104357.png]]

### `justify-content` 속성
- main 축 정렬 방법 결정
```css
justify-content: flex-start;  /* 기본값 */
justify-content: flex-end;
justify-content: center;
justify-content: space-between;
justify-content: space-around;
justify-content: space-evenly;
```
![[Pasted image 20260702104522.png]]

### `align-items` 속성
- main 축과 orthogonal 한 축 정렬 방법 결정
```css
align-items: stretch; /* 기본값 */
align-items: flex-start;
align-items: flex-end;
align-items: center;
align-items: baseline;
```
![[Pasted image 20260702104510.png]]

### `gap` 속성
- Flexitem 사이의 간격 조절
```css
gap: 10px;
```

### `flex-wrap` 속성
- Flex container 의 크기가 요소들을 감싸기 부족한 경우 줄 바꿈 여부 결정
```css
flex-wrap: nowrap; /* 기본값 : 줄바꿈 허용 X */
flex-wrap: wrap;   /* 줄바꿈 허용 */
```
![[Pasted image 20260702104550.png]]

### `flex-shrink` 속성
- 요소가 줄어드는 비율 정함
```css
flex-shrink: 1; /* 기본값 */
flex-shrink: 0; /* 줄어들지 않음 */
flex-shrink: 2; /* 제일 먼저 줄어듦 */
```
![[Pasted image 20260702104655.png]]