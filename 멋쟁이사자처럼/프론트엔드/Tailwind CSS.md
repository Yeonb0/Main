- 빠르고 효율적인 [[UI]] 개발을 도와주는 [[프레임워크]].
- [[클래스]] 이름 조합을 통해 [[CSS]] 작성 

## 설치
```bash
npm install tailwindcss @tailwindcss/vite
```
- 설치 후 `tailwind.config.js` , `postcss.config.js` 파일 생성
### `config` 세팅
```ts
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: { extend: {} },
  plugins: [],
};
```
- `context` : 프로젝트 내 실 사용중인 [[클래스]]만 빌드 결과에 포함
### `theme` 커스터 마이징
- `tailwind.config.js` 에 브랜드 컬러, 여백, `z-index` 커스터마이징
```ts
theme: {
  extend: {
    colors: {
      primary: '#1A73E8',
      secondary: '#F9AB00',
    },
    spacing: {
      72: '18rem',
      84: '21rem',
    },
    zIndex: {
      60: '60',
    },
  },
},
```
## 사용법
- [[HTML]] 태그 내 [[클래스]]에 직접 적용
```html
<div className="w-12 h-10 text-white bg-gray-400"></div>
```

- [[사이즈 설정]]
- [[색상 설정]]
- [[디스플레이 설정]]
- [[레이아웃 설정]]
- [[여백 설정]]
- [[폰트 설정]]
- [[라운드 설정]]
- [[그림자 설정]]
- [[상태 변화 설정]]
- 

### 장점
- [[CSS]] 작성 시간 대폭 감소. [[컴포넌트]] 기반의 접근 방식으로 유지보수 용이.
- 커스터마이징 & [[반응형 웹]] 구현 간편
- 직관적 [[클래스]] 조합
- 불필요한 [[CSS]] 제거

### 단점 
- 스타일 마다 새로운 [[CSS]] [[클래스]] 작성으로 파일 크기가 커질 수 있음
- 구현 불가능한 특정 스타일은 별도 [[CSS]] 파일 작성해야 함
