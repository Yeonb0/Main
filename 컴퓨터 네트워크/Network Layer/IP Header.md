---
aliases:
  - IP 헤더
  - IP 헤더(IP Header)
---

- [[IP]] [[Packet]] 앞에 붙는 layer 3 header
- 기본 20 byte (+ option 최대 40 byte, 거의 사용 X)

![[Internet-Protocol-(IP)-03.png]]

### 첫 번째 줄
- VER (4 bit) : IP version
	- [[IPv4]] `0100` / IPv6 `0110`
- HLEN (4 bit) : header 길이 (단위 4 byte)
	- ==ex)== `0101` -> 5 * 4 byte = 20 byte
- Service (8 bit) : 우선순위 + 서비스 정의
- Total length (16 bit) : header + data 전체 길이
	- 최대 ==65535 byte==

#### Service : 과거
![[Internet-Protocol-(IP)-04.png]]
- Precedence 3 bit -> priority 0 ~ 7
- TOS (Type of Service) 4 bit
	- D : delay 최소화
	- T : throughput 최대화
	- R : reliability 최대화
	- C : cost 최소화
- Precedence & TOS -> router 처리 정책 결정
	- ==ex)== 버리는 우선순위 정하기 / 보낼 순서 정하기

#### Service : 현재
![[Internet-Protocol-(IP)-05.png]]
- [[DSCP]] 6 bit -> Precedence 와 유사
	- source 바탕 4 가지 class 로 중요 순서 결정
	- EF -> AF -> CS -> Default

![[Internet-Protocol-(IP)-06.png]]
- [[ECN]] 2 bit -> Congestion Notification
	- 막힌다는 [[신호]]
	- 중간 [[Router]] 가 값 변경해 전달
	- 알림만 담당. 해결은 TCP 몫
	- ECT (ECN-Capable) : ECN 사용 가능 여부 -> sender 결정
	- CE (Congestion Experience) : 현재 congestion 여부 -> router 가 packet drop 대신 marking
	- CE 수신 -> receiver 가 [[TCP Header]] 의 ECE flag 로 통보

### 두 번째 줄
- [[Fragmentation]] 관련 [[필드]]
- Identification (16 bit)
	- 같은 frame 의 payload 에서 나뉜 조각 -> 동일 값 보유
	- source / destination 같을 때 -> fragmented / different frame 판별
- Flag (3 bit)
	- 첫 번째 bit : 사용 X
	- D (do not fragment) : 이 frame fragment X
		- [[MTU]] 때문에 fragment 필요 시 버림
	- M (more fragment) : 뒤에 fragment 더 존재
		- `0` -> 마지막 fragment or fragment X
- Fragmentation offset (13 bit) : 원래 payload 에서 시작 byte 위치
	- 단위 ==8 byte==

![[Internet-Protocol-(IP)-07.png]]
- ==ex)== 175 -> 첫 번째 byte 위치 1400 (175 * 8)
- header size 통해 끝 위치도 파악 O

### 세 번째 줄
- [[TTL]] (8 bit) : router 이동 가능 범위
- Protocol (8 bit) : 상위 layer 4 protocol 종류 표시

![[Internet-Protocol-(IP)-08.png]]

### 나머지
![[Internet-Protocol-(IP)-09.png]]
- 보내는 사람 / 받는 사람 [[IP 주소]]

![[Internet-Protocol-(IP)-10.png]]
- Option : 최대 40 byte 추가 가능 (거의 사용 X)

### 예시
![[Internet-Protocol-(IP)-11.png]]
- 패킷 길이 2 (8 byte) -> 5 이상이어야 하므로 [[Error|오류]]

![[Internet-Protocol-(IP)-12.png]]
- 총 8 * 4 = 32 byte
- 기본 20 byte + option 12 byte

![[Internet-Protocol-(IP)-13.png]]
- Header 20 byte, 총 길이 32 + 8 = 40
- Data 20 byte

![[Internet-Protocol-(IP)-14.png]]
- TTL = `01`
