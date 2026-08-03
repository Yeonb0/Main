---
aliases:
  - 3-웨이 핸드셰이크
  - TCP Connection Setup
  - 3-Way Handshake(3-웨이 핸드셰이크)
---

- [[TCP]] 연결 설정 절차
- bi-directional -> client & server 모두 정보 send & receive

### 절차
1. Client : `SYN`
2. [[서버|Server]] : `ACK` + `SYN`
3. Client : `ACK` -> connection 완료

![[Transport-Layer-14.png]]

### 특징
- 연결 설정 시 data 전송 X -> [[TCP Sequence Number|sequence number]] 그대로 사용
- 악용 -> [[SYN Flooding Attack]]
- 종료 절차 -> [[TCP Connection Teardown]]
