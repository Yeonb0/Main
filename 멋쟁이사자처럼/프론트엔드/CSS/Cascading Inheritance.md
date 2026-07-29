- 부모 - 자식 관계의 계단식 상속
- 부모 요소에 적용된 스타일은 기본적으로 자식 요소 상속

- 모든 [[CSS]] 속성 상속 X
	- [[font]], [[color]] 등 [[텍스트]] 관련 -> 상속 O
	- [[background]], [[width]], [[height]] 등 [[레이아웃]] 관련 -> 상속 X

- 상속되지 않는 속성은 `inherit` 을 사용해 명시적으로 상속 가능 
```html
<div>
	<p> 자식 요소 </p>
</div>
```
```css
div {
	width: 50%;    /* 자동 상속 X */
	color: white;  /* 자동 상속 O */
}

p {
	width: inherit; /* 부모 요소 (div) 의 width 상속 */
}
```