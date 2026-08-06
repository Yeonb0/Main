---
aliases:
  - VPC Endpoint
---
- [[VPC]] 안 -> [[VPC]] 밖 서비스로 연결할 수 있도록 접속점 만드는 서비스
- 비[[VPC]] 와 [[VPC]]를 연결해주는 것 -> 엔드포인트 서비스

### 종류
- 인터페이스 엔드포인트 (Interface Endpoint)
	- 네트워크 인터페이스 (ENI, Elastic Network Interface) 형태로 구성되는 엔드포인트
	- [[LAN]] 케이블을 꽂는 포트와 유사
	- 사설 [[IP 주소]] 할당 -> 출입구

- 게이트웨이 엔드포인트 (Gateway Endpoint)
	- [[Router#Routing table|라우팅 테이블]]에 경로 등록해 라우팅
	- 연결 대상: [[S3]], [[DynamoDB]]로 제한

- Gateway Load Balancer 엔드포인트 
	- [[GLB]] 사용해 다른 [[VPC]]에 연결할 때 만드는 엔트포인트
	- [[Packet|패킷]]을 [[캡슐화]]해 전달

### 요금
#### 인터페이스 엔드포인트
- VPC 엔드포인트 한 개당 사용료 + 데이터 처리량

#### 게이트웨이 엔드포인트
- 무료