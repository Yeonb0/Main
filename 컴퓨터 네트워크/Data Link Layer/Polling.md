---
aliases:
  - 폴링
  - Polling(폴링)
---

- Master 가 전송 순서 지정하는 [[Controlled Access]] 방식
- Master & Slave 구성
- ==ex)== [[Bluetooth]]

### 구조
- Master
	- 보내고 싶을 때 전송
	- SEL : 이제부터 전송한다고 알림
	- Poll : slave 가 보낼 것 있는지 check
- Slave : Poll 수신 이후
	- 보낼 것 有 -> data 전송
	- 보낼 것 無 -> NAK 전송

![[Medium-Access-Control-02.png]]
