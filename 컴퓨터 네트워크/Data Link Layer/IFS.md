---
aliases:
  - inter-frame spacing
  - IFS(inter-frame spacing)
  - 프레임 간 간격
---

- [[CSMA-CA|CSMA/CA]] 에서 Carrier Sensing 중 idle 확인 시 곧바로 전송하지 않고 대기하는 시간
- 이유 : 멀리 있는 다른 frame 이 이미 전송했을 수 있음
- 시스템마다 고정
- idle [[state|상태]] 확인할 때마다 초기화

### 종류
| 종류 | 내용 |
| --- | --- |
| SIFS (Short IFS) | DIFS 보다 짧은 IFS, [[ACK]] 전송 전 사용 |
| DIFS (Data IFS) | Data 전송 전 대기하는 IFS |
