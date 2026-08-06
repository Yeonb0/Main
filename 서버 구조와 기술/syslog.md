---
aliases:
  - 시스템 로그
  - syslog(시스템 로그)
---

- 리눅스 표준 로그 관리 기능
- 로그 분류 기준 : 퍼실리티 + 레벨

### 퍼실리티 (facility)
- 로그 종류 구분

| 퍼실리티 | 설명 |
| --- | --- |
| auth, authpriv | 인증 서비스 (login, su 등) |
| cron | cron |
| daemon | 각종 데몬 |
| kern | [[커널]] |
| lpr | 프린트 시스템 |
| mail | 메일 시스템 |
| news | 뉴스 서비스 |
| syslog | syslog 기능 |
| user | 사용자 시스템 |
| local0~7 | 독자적인 설정 |

### 레벨 (level)
- 값 ↓ -> 중요도 ↑

| 레벨 키워드 | 레벨 | 설명 |
| --- | --- | --- |
| emergencies | 0 | 시스템 불안정 |
| alerts | 1 | 즉시 처리 필요 |
| critical | 2 | 크리티컬한 [[state\|상태]] |
| errors | 3 | 에러가 발생한 [[state\|상태]] |
| warnings | 4 | 경고 상태 |
| notications | 5 | 정상이지만 주의가 필요한 상태 |
| informational | 6 | 정보 메시지 |
| debugging | 7 | 디버깅 메시지 |
