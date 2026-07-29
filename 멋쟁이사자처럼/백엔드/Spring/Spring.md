---
aliases:
  - 스프링
---

- [[Spring 개요]]
- [[Spring 특징]]

## [[Spring Boot]]

## [[Gradle]]

### 용어
- [[스프링 컨테이너|컨테이너]]
- [[Bean]]
- [[의존성]]
- [[MVC 패턴]]
- [[웹 애플리케이션 계층 구조]]

### 디렉토리 구조
```groovy
my-spring-boot-app/
│
├── 📁 src/main/java/com/example/demo/
│   ├── 📂 controller/      # 클라이언트 요청을 받는 컨트롤러
│   ├── 📂 service/         # 비즈니스 로직을 처리하는 서비스
│   ├── 📂 repository/      # DB와 통신하는 리포지토리
│   ├── 📂 domain/           # 데이터 구조를 정의하는 도메인
│   └── ☕ DemoApplication.java   # 메인 클래스 (앱 시작점)
│
├── 📁 src/main/resources/
│   ├── ⚙️  application.yml      # 서버 포트, DB 연결 등 환경 설정
│   ├── 📂 static/               # 정적 파일 (CSS, JS, 이미지 등)
│   └── 📂 templates/            # Thymeleaf 뷰 템플릿 (HTML)
│
├── 🐘 build.gradle              # 의존성 및 빌드 설정 (Gradle)
└── 📄 README.md                 # 프로젝트 설명 문서
```
- `src/main/java/com/example/demo/` : [[Spring Boot]] 애플리케이션의 핵심 코드 위치
- `src/main/resources/` : 애플리케이션에서 사용되는 설정 파일 및 정적 리소스가 위치
- `application.properties / application.yml` : [[Spring Boot]]의 환경 설정 파일
	- [[서버]] [[포트]], [[데이터베이스]] 연결, 로그 레벨 등
- `build.gradle` : [[의존성]] 및 빌드 설정 관리
	- `dependencies` 블록 이용해 라이브러리 추가 가능