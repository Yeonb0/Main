---
aliases:
  - SYN 플러딩 공격
  - SYN Flooding Attack(SYN 플러딩 공격)
---

- [[3-Way Handshake]] 미완성 [[state]] 누적 악용 -> DoS (Denial-of-Service) attack

### 동작
1. Attacker : `SYN` 요청
2. [[서버|Server]] : state 생성 + `ACK` + `SYN` 전송 후 wait
3. Attacker : 다른 [[IP]] 로 `SYN` 반복 요청
4. state 만 증가 -> 정상 유저 수용 X

### 방어
- initial [[TCP Sequence Number|sequence number]] 로 반복 요청 추적
- memory 에 state 미보관 -> 최종 연결 때만 기록
