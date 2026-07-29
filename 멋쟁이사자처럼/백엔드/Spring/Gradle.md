### 설명
- 한스 도커 외 6인 개발. [[Ant]], [[Maven]] 보완
- [[안드로이드 스튜디오]] 공식 [[빌드 도구]] 
- [[그루비]] 기반 빌드 스크립트 사용
- 실행 처리 명령 모은 것 -> 테스크 (Task) 
- 테스크 단위로 설정
- 테스크 재사용 가능, 다른 시스템 테스크 공유하는 빌드 캐시 가능


- [[Java]] 프로젝트에서 필요한 [[라이브러리]]를 쉽게 설치 & 관리하는 빌드 도구
- `build.gradle` 파일로 [[라이브러리]] 정의
- `dependencies` 블록에 추가해 쉽게 관리 가능
![[Pasted image 20260707105555.png]]

### [[의존성]] 추가하기
```groovy
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
}
```
- `spring-boot-starter-web`: 웹 애플리케이션 개발에 필요한 라이브러리 제공
- `spring-boot-starter-data-jpa`: 데이터베이스 연동 및 JPA 기능 사용을 위한 라이브러리 포함

### 특징
- [[DSL]] 기반
- [[의존성]] 관리 : 필요 라이브러리 자동으로 다운로드 해 프로젝트에 추가
- 빠른 빌드 속도
- [[Spring Boot]]와 강력한 호환성