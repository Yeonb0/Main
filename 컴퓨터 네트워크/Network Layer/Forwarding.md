---
aliases:
  - 포워딩
  - Forwarding(포워딩)
---

- [[Router]] 가 받은 [[Packet]] 을 알맞은 방향으로 내보내는 동작
- ==Data plane== 담당

### 절차
1. packet 도착
2. destination address 확인
3. routing table 조회 -> 출력 방향 결정

### routing 과 비교
| 항목 | Forwarding | Routing |
| --- | --- | --- |
| plane | Data plane | Control plane |
| 역할 | table 조회 -> 전송 | [[Routing Algorithm]] 으로 table 구성 |
| 시점 | packet 도착 시 | 주기적 · 변화 발생 시 |

### 전송 순서
- 방향 결정 이후 출력 [[Queue]] 내 순서는 [[Scheduling]] 이 결정
- 몰려 들어온 burst 는 [[Traffic Shaping]] 으로 규칙적 흐름 변환
