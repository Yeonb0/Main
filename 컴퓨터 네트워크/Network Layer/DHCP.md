---
aliases:
  - Dynamic Host Configuration Protocol
  - DHCP(Dynamic Host Configuration Protocol)
---

- 연결한 기기에게 [[IP 주소]] 자동 대여하는 protocol
- Application layer(layer 4) protocol
- IP 주소 보유한 DHCP [[서버]] -> 접속 host 에 임대

### 특징
- ==ex)== 카페 [[IEEE 802.11|Wi-Fi]]
	- 계속 사용 -> 임대 연장
	- 미사용 -> 다른 기기에게 재대여
- 한 DHCP server 가 여러 [[Autonomous System|AS]] 관리 O
	- 다른 [[컴퓨터 네트워크|네트워크]] -> broadcast 범위 밖
	- DHCP relay 가 대신 넘겨서 전송

![[Other-Network-Layer-Related-Protocols-04.png]]

### 절차
- DORA
1. DISCOVER
2. OFFER
3. REQUEST
4. [[ACK]]

![[Other-Network-Layer-Related-Protocols-05.png]]

### 할당 정보
- [[IP 주소]]
- [[Subnetting|서브넷 마스크]]
- 기본 [[게이트웨이]]
- [[DNS]] 서버 주소

### 임대
- 임대 (lease) : DHCP 서버 할당 정보 이용 가능 시간
- 서버 내 임대 상황 기록 [[데이터베이스]] 파일 존재
	- 임대 시작 · 종료 날짜, 임대 [[state|상태]], [[클라이언트]] 사용 식별자 등 보관
