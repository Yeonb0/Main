---
aliases:
  - 프로세스 간 통신
  - End-to-End Communication
  - Process-to-Process Communication(프로세스 간 통신)
---

- layer 4 가 담당하는 통신 단위 -> end-to-end (process-to-process)
- [[Port|port 번호]]로 host 내부 process 식별

![[Transport-Layer-01.png]]

### 통신 범위
| layer | 범위 |
| --- | --- |
| layer 1, 2 | hop-to-hop, single hop |
| layer 3 | host-to-host |
| layer 4 | process-to-process |

![[Transport-Layer-02.png]]

### Layer 별 기능
| layer | 기능 |
| --- | --- |
| Layer 1 (Physical) | [[신호]] 생성 |
| Layer 2 (Data link) | [[Framing]], [[ARQ]], [[Error Detection]] / [[Error Correction]] |
| Layer 3 ([[컴퓨터 네트워크\|Network]]) | addressing, [[Routing Algorithm\|routing]], host 전달 |
| Layer 4 (Transport) | [[Packet\|packet]] 세밀 조절 & 전달 |

- layer 4 protocol -> [[TCP]] / [[UDP]]
- 조절 대상 -> [[Flow Control]], [[Congestion Control]]
