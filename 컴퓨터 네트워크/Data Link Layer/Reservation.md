---
aliases:
  - 예약 접근
  - Reservation(예약 접근)
---

- data 슬롯 앞에 reservation 슬롯 두고 전송권 예약하는 [[Controlled Access]] 방식
- 시스템마다 운영 방식 조금씩 차이

![[Medium-Access-Control-01.png]]

### 절차
1. reservation 슬롯에서 전송할 station 이 ==1== 표시
2. 1 인 data station 에 reservation 시간 할당
3. 보낼 station 無 -> 다시 reservation time 복귀

### 장점
- station 간 [[Collision|충돌]] 위험 X
- 매번 5개 대기 X -> 효율적

### 단점
- station in/out 시 overhead
