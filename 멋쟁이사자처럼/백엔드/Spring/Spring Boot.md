- [[Spring]] [[프레임워크]]를 쉽게 사용할 수 있도록 만들어진 도구
	- 설정 간편 & 빠른 개발 가능
![[Pasted image 20260707103546.png]]

### 핵심 기능
- 기본 설정 자동 구성
- 구성에 대한 독선적 접근 방식
	- 초보자를 위해 좋은 기본값 제공
- 독립형 애플리케이션 만드는 능력

### 프로젝트 생성하기
1. Spring Initializr 접속 https://start.spring.io/ 
2. 프로젝트 설정
   ![[Pasted image 20260707103843.png]]
	- Project : 프로젝트 빌드 도구 -> ==Groovy== 선택
	- Language : 프로젝트 사용 언어 -> ==Java== 선택
	- Spring Boot : [[Spring Boot]] 버전 선택. (너무 최신은 불안정 할 수 있음) -> ==4.0.7== 선택
	- Group : 단체명
	- Artifact : 프로그램의 실제 이름. 빌드된 결과물의 이름
	- Package name : 자동 생성
	- Packaging : Jar
	- Configuration : YML
	- Java : 21
3. Dependency 설정
   ![[Pasted image 20260707104155.png]]
	- ==Spring Web== 설정
4. 최종
   ![[Pasted image 20260707104228.png]]
	- ==Generate== 버튼 누르고, 생성된 .zip 폴더 압축 해체