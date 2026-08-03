---
aliases:
  - Class
  - IPv4 클래스
  - IPv4 클래스(IPv4 Class)
---

- [[IPv4]] 를 분류하는 기준
- [[컴퓨터 네트워크|Network]] address + Host address 구성
	- Network address : 망이 공통적으로 사용하는 주소
	- Host address : 망 안에서 unique 한 주소
- [[클래스|Class]] 따라 가능한 Host 개수 상이

### 종류
![[Internet-Addressing-01.png]]

| Class | 시작 [[비트]] | 범위 | 내용 |
| --- | --- | --- | --- |
| A | `0` | 0 ~ 127 | Network 당 Host $2^{24}$ 개 |
| B | `10` | 128 ~ 191 | Network 당 Host $2^{16}$ 개 |
| C | `110` | 192 ~ 223 | Network 당 Host $2^{8}$ 개 |
| D | `1110` | 224 ~ 239 | Multicast 용 |
| E | `1111` | 240 ~ 255 | 특수 목적으로 남겨놓음 (reserved) |

![[Internet-Addressing-02.png]]

### 전송 방식
- Unicast : 목적지가 하나
- Multicast : 여러 명에게 전송 (전체는 X)
	- ==ex)== Netflex, Tving
- [[브로드캐스트|Broadcast]] : 전체에게 전송

### 한계
- class 사이 이용 가능한 host 갯수 차이 큼 -> [[Subnetting]] 필요
