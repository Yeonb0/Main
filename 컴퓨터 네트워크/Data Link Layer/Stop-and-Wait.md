---
aliases:
  - 정지-대기
  - Stop-and-Wait(정지-대기)
---

- frame 1 개 전송 -> [[ACK]] 수신까지 대기 -> 다음 frame 전송
- send window 1 칸 / receive window 1 칸 -> [[Go-Back-N]] 의 특별한 case

### Normal Case
![[Framing-Error-Control-02.png]]

### Error Case
- Case 1 : Send 과정 [[Error|오류]] -> Receiver 가 못 받음
	- ==ex)== 택배가 사라짐
	- ![[Framing-Error-Control-03.png]]
- Case 2 : ACK 전송 오류 -> Receiver 가 보낸 걸 Sender 가 못 받음
	- ==ex)== "확인했습니다!" 문자 전송 X
	- ![[Framing-Error-Control-04.png]]
- Case 3 : 전송 오류 X, [[Timeout]] 발생
	- ==ex)== "확인했습니다!" 받기 전에 택배 또 전송
	- ![[Framing-Error-Control-05.png]]

### Sender
- frame 전송 후 T 초 간 대기 (T : timeout period)
- T 초 내 ACK 도착 -> next frame 전송
- ACK 도착 X -> timeout -> 같은 frame 재전송
- 모든 Case 에서 동일 동작

### Receiver
- 전송 받은 frame 이 같은 frame / next frame 인지 판단 필요
- Normal Case -> new frame
- Case 1) Send 과정 오류 -> new frame (받은 적 없음)
- Case 2) ACK 전송 오류 -> 같은 frame
- Case 3) timeout 발생 -> 같은 frame
- 기존 frame 과 new frame 구분 수단 -> [[Sequence Number]]

### 단점
- 보내지 않고 대기하는 시간 김 -> 성능 ↓

![[Framing-Error-Control-12.png]]
