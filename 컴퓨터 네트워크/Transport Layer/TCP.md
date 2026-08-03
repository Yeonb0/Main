---
aliases:
  - Transmission Control Protocol
  - TCP(Transmission Control Protocol)
---

- connection-oriented : 연결 설정 O
- reliable : 순서대로, [[Error|error]] 없이 전달

### 용어
- Segment : [[Packet]] 의 다른 [[이름]] -> 잘라 보내는 단위
- bi-directional : 연결 후 쌍방 [[데이터]] 전송
- Buffer : sender / receiver 의 전송 대기 공간 -> [[운영체제|OS]] 관리

![[Transport-Layer-08.png]]

### 기능
| 기능 | 내용 |
| --- | --- |
| [[Flow Control\|Flow control]] | receiver 에 무리 X 속도 조절 |
| [[Congestion Control\|Congestion control]] | 중간 [[Router\|router]] drop 방지 속도 조절 |
| [[Error Control\|Error control]] | [[ACK]] 이용 재전송 |

### 구성 요소
- [[TCP Header]] / [[TCP Sequence Number]]
- 연결 : [[3-Way Handshake]] -> [[TCP Connection Teardown]]
- 전송 : [[TCP Sliding Window]]
