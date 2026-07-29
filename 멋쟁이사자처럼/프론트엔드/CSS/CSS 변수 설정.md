- [[CSS]]에서 변수를 사용하는 방법
- `root` 의 가상 클래스 활용

- 변수 생성하기
```css
:root {
	--bg-color: #2C2C2C; 
	--text-color: #4285F4;
}
```

- 변수 사용하기
``` css
body { 
background-color: var(--bg-color); 
color: var(--text-color); 
}
```


