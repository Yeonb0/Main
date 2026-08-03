---
aliases:
  - TCP 연결 해제
  - half-close
  - TCP Connection Teardown(TCP 연결 해제)
---

- [[TCP]] 연결 종료 절차 -> 3-way handshake

### 절차
1. [[클라이언트|Client]] : `FIN`
2. [[서버|Server]] : `ACK` + `FIN`
3. Client : `ACK` -> connection 종료

![[Transport-Layer-15.png]]

### half-close
- Client `FIN` 전송, but Server 아직 data 전송 중
- Server : Client `FIN` 에 대한 `ACK` 먼저 전송
- data 전송 완료 후 `FIN` 전송
- 그동안 Server 의 단방향 data 전송

![[Transport-Layer-16.png]]
