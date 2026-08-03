---
aliases:
  - 포트
  - Port(포트)
---

- 같은 host 안 process 구분 번호
- 16 bit -> ==0 ~ 65535==
- [[IP 주소]] : host 지정 (layer 3) / port : process 지정 (layer 4)

![[Transport-Layer-03.png]]

![[Transport-Layer-04.png]]

### 통신에 필요한 4 요소
1. local host
2. local process (port number)
3. remote host
4. remote process (port number)

### 종류
| 종류 | 범위 | 특징 |
| --- | --- | --- |
| well-known port | 0 ~ 1023 | 유명 · 공식 서비스 |
| registered ports | 1024 ~ 49151 | 등록 후 사용 |
| dynamic ports | 49152 ~ 65535 | 관리 주체 X, 자유 사용 |

- ==ex)== 22 ([[SSH]]), 25 (SMTP), 53 (DNS), 80 (HTTP), 443 (HTTPS)
- dynamic port -> [[운영체제|OS]] 자동 생성 시 사용 ([[NAT]])
- [[IP 주소]]와 결합 -> [[Socket]]
