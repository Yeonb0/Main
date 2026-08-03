---
aliases:
  - 서브네팅
  - 서브네팅(Subnetting)
  - Subnet Mask
  - 서브넷 마스크
---

- [[IPv4 Class]] 사이 이용 가능한 host 갯수 차이 큼 -> subnet 으로 network / host 구분 표시
- `255.255.255.0` -> `11111111 11111111 11111111 00000000`
	- 1 부분 : network number (24 bit)
	- 0 부분 : host number (8 bit)
- 1 / 0 갯수 조정 -> host 갯수 2배씩 증감 O
	- 앞에서부터 1111, 0 & 1 섞어서 X

### Network address (망)
- 같은 망 : gateway 안 거치고 바로 전달 O
- 다른 망 : gateway 거쳐서 전달

### Address 할당
- [[컴퓨터 네트워크|Network]] address & subnet address 부여
	- host address 는 할당받은 범위 내에서 배정
	- address 배정 시 연속적으로 필요 (배달 위해서)
- ==ex)== `205.16.37.32` ~ `205.16.37.47` 할당 -> 16개의 host 할당
	![[Internet-Addressing-03.png]]
	- 첫 번째 (`205.16.37.32`) 할당 주소가 할당된 수 (16) 로 나눠 떨어져야 함
	- 나눠 떨어지지 않음 -> subnetting 하면서 사용하지 않는 주소 발생
	- subnet -> `11111111 11111111 11111111 11110000` (`255.255.255.224`)

### 표기
![[Internet-Addressing-04.png]]
- 전체 주소 : ==IP 주소 / 1 갯수==
- ==ex)== `205.16.37.39/28` 의 first address
	- 끝 4 bit 만 0 으로 변경
	- `11001101 00010000 00100101 00100000`

### 사용 이유
- subnet masking -> [[Router|routing]] 배달 위해
