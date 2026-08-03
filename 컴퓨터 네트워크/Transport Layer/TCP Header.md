---
aliases:
  - TCP 헤더
  - TCP Header(TCP 헤더)
---

- [[TCP]] segment 앞에 붙는 layer 4 header
- 각 줄 32 bit

![[Transport-Layer-11.png]]

### 필드
- Port number (Source / Destination) : 각 16 bit
- Sequence number : 보낼 data 의 [[TCP Sequence Number|sequence number]]
- [[ACK|Acknowledgement]] number : 상대 data 의 acknowledgement number
	- bi-directional -> 둘 다 필요, 서로 다른 byte number 에서 시작
- HLEN (4 bit) : header length (단위 4 byte)
	- option 없으면 기본 ==5==
	- TCP option 자주 사용 -> 유동적 변경
- reserved (6 bit → 4 bit) : 사용 X 예약 bit
- Flag (6 bit → 8 bit) : 0 or 1
- Window size (16 bit) : advertised window 크기
	- receiver 가 자신의 남은 window 통보 -> sender 는 이 size 초과 전송 X
	- [[Flow Control]] 용도

### Flag
![[Transport-Layer-12.png]]

| flag              | 의미                                             |
| ----------------- | ---------------------------------------------- |
| URG (Urgent)      | 중요 data 존재 (Ctrl + C / Esc 등)                  |
| ACK               | [[ACK\|Acknowledgement]] 존재 -> 맨 처음 빼고 보통 1    |
| PSH (Push)        | buffer 내용 즉시 상위로 전달                            |
| RST (Reset)       | 문제 발생 연결 종료 (Client & [[서버\|Server]] 둘 다 전송 O) |
| SYN (Synchronize) | 최초 연결 설정 (Client)                              |
| FIN (Finish)      | 정상 연결 해제 (Client)                              |

- URG -> urgent pointer (16 bit) 사용
	- data = urgent + normal 구성
	- normal data 시작 위치 표시 -> 이전까지 urgent data

### ECN 관련 flag
- [[ECN]] 2 bit -> [[IP]] header 에 위치
	- ECT (ECN-Capable) : ECN 사용 가능 여부 -> sender 결정
	- CE (Congestion Experience) : 현재 congestion 여부 -> [[Router|router]] 결정, packet drop 대신 marking
- ECE (ECN-Echo) : CE marking 된 packet 수신 -> receiver 가 1 로 설정해 전송
- CWR : ECE 1 받은 sender 가 전송
	- sender -> congestion 파악 후 [[Congestion Control|CWND]] ↓
	- receiver 가 CWR = 1 수신 -> 다시 ECE = 0 전송

![[Transport-Layer-13.png]]
