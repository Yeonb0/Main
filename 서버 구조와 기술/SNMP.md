---
aliases:
  - Simple Network Management Protocol
  - SNMP 서버
  - SNMP(Simple Network Management Protocol)
---

- [[컴퓨터 네트워크|네트워크]] 장비 or [[서버]] 정기적 관찰 & 현재 [[state|상태]] 파악용 [[프로토콜]]
- [[감시 서버]] 구현 수단

### 구조
- 매니저 ([[서버]]) : 감시하는 쪽, 에이전트에서 다양한 정보 가져오기 & 변경 O
- 에이전트 ([[클라이언트]]) : 감시 대상
- 1 매니저 - 多 에이전트
- 정보 표현 : [[MIB]](Management Information Base) & OID([[객체|Object]] ID)

### 버전
| 버전 | 내용 |
| --- | --- |
| 1 | 보편적 사용 |
| 2 | 구현해야 하는 기술 다 못 갖춤 -> 표준화 X |
| 3 | 보안 및 사용자 인증 기술까지 탑재 |
