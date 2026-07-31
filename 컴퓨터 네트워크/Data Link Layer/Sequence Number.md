---
aliases:
  - 일련 번호
  - Sequence Number(일련 번호)
---

- 보낼 frame & [[ACK]] 에 붙이는 번호 -> 기존 frame 과 new frame 구분

![[Framing-Error-Control-06.png]]

### ACK sequence number
- next expected frame 번호 -> 이거 사용
	- ![[Framing-Error-Control-07.png]]
- cf) 방금 받은 frame 번호 방식도 존재

### [[Stop-and-Wait]] 적용
- 1 bit (0, 1) 사용 : 0 → 1 → 0 → 1 → .. 번갈아 사용
- Case 1) Frame Loss 발생 -> receiver 는 문제 없음
	- ![[Framing-Error-Control-08.png]]
- Case 2) ACK lost -> frame 이 ACK sequence number 와 다르면 discard
	- ![[Framing-Error-Control-09.png]]
- Case 3) ACK 가 [[Timeout]] 이후 도착
	- ![[Framing-Error-Control-10.png]]

### 전체 예시
![[Framing-Error-Control-11.png]]
- $S_n$ : sequence number
- 마지막 Receiver : Out-of-Order frame 오더라도 ACK 전송
