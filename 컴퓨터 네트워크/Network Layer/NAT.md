---
aliases:
  - Network Address Translation
  - NAT(Network Address Translation)
  - 네트워크 주소 변환
---

- private [[IP]] ↔ public IP 상호 변환하는 기법
- [[IP 주소]] 부족 대응책

### 배경
- 공유기([[Router|router]]) 는 Public IP 보유
- 연결된 기기들에게 Private IP unique 하게 배정

![[Other-Network-Layer-Related-Protocols-13.png]]
- 공인 server 가 사설 IP 로 직접 전달 X -> NAT 필요

### 구조
![[Other-Network-Layer-Related-Protocols-14.png]]
- router 주소 보통 `X.X.X.1` 시작 -> 기기들에게 `2`, `3`, `4`, … 분배
- router 가 IP 2개 보유 : 외부용 & 내부용

| 구분 | 주소 |
| --- | --- |
| 외부 | `138.76.29.7` |
| 내부 | `10.0.0.4` |

- IP : Port 쌍으로 식별
	- IP 주소 : layer 3 개념
	- Port : layer 4 개념 (TCP, UDP)
		- 같은 IP host 내에서 어떤 process 인지 구분

### 절차
1. Host(`10.0.0.1:3345`) 가 공인 server(`128.119.40.186:80`) 로 [[Packet]] 전달
2. router 가 host 의 private 주소 ↔ 자신이 만든 public port 를 table 에 기록 후 public IP + 생성 Port 로 전송
	- LAN `10.0.0.1:3345` -> WAN `138.76.29.7:5001`
3. 공인 server 가 받은 주소(`138.76.29.7:5001`) 로 packet 재전송
4. router 가 받은 주소의 port(`5001`) 확인 -> 대상 host 판별 후 전달

### 한계
- 내부 -> 외부 나가는 packet 있을 때만 NAT table 생성
- 외부에서 먼저 접근 X -> [[Port Forwarding]] 필요
