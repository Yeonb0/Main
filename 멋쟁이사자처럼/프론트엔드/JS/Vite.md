- 프론트엔드 빌드 도구
	- 개발 서버 속도 빠름
	- [[HMR]] : 매우 빠름
	- 빌드 속도 : 빠름 ([[ESBuild]] 사용)
	- 설정 유연성 : 설정 가능
	- [[번들링]] 방식 : [[ES Module]] 기반 동적 로딩

## 설치 방법
1. 터미널에 아래 명령어 입력
```bash
$ npm create vite@latest
```

2. [[패키지]] 설치 -> `y` 입력 (사용자 따라 생략 가능성 有)
```bash
Need to install the following packages: 
create-vite@6.2.0 
Ok to proceed? (y) y
```

3. 프로젝트 이름 입력
```bash
> npx 
> create-vite 

│ 
◆ Project name: 
│ css-advanced 
└
```

4. [[프레임워크]] 선택
```bash
◆ Select a framework: 
│ ● Vanilla 
│ ○ Vue 
│ ○ React 
│ ○ Preact 
│ ○ Lit 
│ ○ Svelte 
│ ... 
└
```

5. [[프로그래밍 언어]] 선택
```bash
◆ Select a variant: 
│ ○ TypeScript 
│ ● JavaScript 
└
```

6. 생성한 프로젝트 폴더로 이동
```bash
% cd css-advanced
```

7. 생성된 프로젝트에 [[Node.js]] 추가
``` bash
% npm i
```

8. 개발 서버 실행
```bash
npm run dev
```
