---
aliases:
  - Amazon Aurora
---
- [[AWS]] 오리지널 [[관계형 데이터베이스|RDB]]
- [[MySQL]] & [[PostgreSQL]] 과 호환
- [[매니지드 서비스]]
### 설정
- ==Serverless== : 성능 고정 X, 실제 부하 맞춰 자동 확장 or 축소
- ==Global Database== : 여러 [[리전]] 걸쳐 [[클러스터]] 구성 가능

### 구조
- [[클러스터]] 단위로 관리
- 기록된 데이터 -> 2개 이상의 [[AZ]]에 걸쳐 있는 6개의 스토리지에 저장
	- 완전성 & 가용성!

### Amazon Aurora DSQL
- [[NewSQL]] 유형
