- [[인스턴스]] 증감 자동 처리 기능
- 서버 부하 정보 -> [[CloudWatch|Amazon CloudWatch]] 에서 수집

### 종류
- Amazon Auto Scaling : [[EC2]], [[Amazon DynamoDB|DynamoDB]], [[Aurora]] 같은 리소스 묶어 관리
- Amazon EC2 Auto Scaling : [[EC2 인스턴스]]만을 대상으로 함

### 인스턴스 관리 방법
1. [[EC2 인스턴스]]가 중지 -> 해당 인스턴스를 그룹에서 분리 & 새 인스턴스 만들어 대체
2. 정해둔 일정 (스케줄) 에 따라 [[스케일링]]
3. [[CPU]], 네트워크 부하 기준 임계값 넘으면 자동 관리

### 비용
- 무료
- 단, [[CloudWatch]] 사용 시 모니터링 관련 요금 발생