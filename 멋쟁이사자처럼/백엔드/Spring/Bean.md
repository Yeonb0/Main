---
aliases:
  - 빈
---
- [[Spring]]이 직접 제공 & 관리해주는 [[객체]]

### 필요성
1. [[객체]] 관리 자동화
2. [[DI|의존성 주입(DI)]] 지원
3. 재사용성 & 유지보수성 ↑

### 생성 방법
1. 컴포넌트 스캔 : 클래스에 [[어노테이션]] 붙이면 자동 [[Bean]] 등록
 > [!note]- 사용 가능 [[어노테이션]]
 > @Component
 > @Service
 > @Repository
 > @Controller

2. [[Bean]] 으로 직접 등록
	- `@Configuration`, `@Bean` [[어노테이션]] 통해 가능