---
aliases:
  - Amazon API Gateway
---
- 웹 ([[HTTPS]]) 에 특화된 [[API]] 만드는 기능
	- [[REST API]] / [[HTTP API]] / [[WebSocket API]] 지원
- [[Lambda]]와 결합하는 경우 많음
- 한 시스템 내부에서 [[마이크로서비스]]화 된 서비스 연결용으로 사용

### API 종류
- 스테이트리스 : 호출 후 종료 ([[REST API]]/[[HTTP API]])
- 스테이트풀 : 계속 연결 유지 ([[WebSocket API]])

- 접속되는 쪽 : [[Lambda]] 함수, [[HTTP]] 시스템, Mock, [[AWS 서비스]]
- 접속하는 쪽 : 제한 X 

### 사용법
- [[API]] 접속시 [[엔드포인트]] 생성
	- 한 API 대해 여러 엔드포인트 생성 가능
	- 할당된 [[URL]] 사용 -> 스테이지 사용해 제품명 or 버전 번호 넣어 고정 가능