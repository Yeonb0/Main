---
aliases:
  - IP 서비스 모델
  - IP Service Model(IP 서비스 모델)
---

- layer 4 입장에서 [[IP|IP]] 가 제공하는 기능 정의
- Packet delivery + Global Addressing Scheme 두 축

### Packet delivery
- Connectionless : 연결 설정 없이 전송 (like 우편)
	- 수신 여부 알 수 X
	- cf) Connection-oriented : 연결 설정 후 전송 (like 전화) -> layer 4 TCP
- Best-effort (unreliable)
	- [[Packet]] 분실 · 순서 뒤바뀜 · 중복 · [[Delay|지연]] 가능하나 일단 최선 다해 전송
	- 그 이상 서비스는 layer 4 담당

### Global Addressing Scheme
- 세계 만국 공통 주소 체계 -> [[IP 주소]]
