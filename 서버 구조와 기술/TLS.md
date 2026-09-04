---
aliases:
  - SSL
  - SSL/TLS
  - Transport Layer Security
  - TLS(Transport Layer Security)
  - Secure Sockets Layer
---

- 인터넷상에서 [[데이터]] 암호화해 송수신하는 [[프로토콜]] (SSL/TLS)

### 기능
| 기능 | 내용 |
| --- | --- |
| 도청 방지 | [[공통 키 암호 방식]] · [[공개 키 암호 방식]] 으로 암호화 -> 유출돼도 내용 공개 X |
| 스푸핑 방지 | 통신 상대 사칭 차단 |
| [[Modulation\|변조]] 방지 | 전송 중 데이터 변경 검출 |

### HTTPS
- HTTP + SSL/TLS
- 웹 사이트 열람 시 통신 암호화
- 사용률 ==98%==

### 한계
- SSL 인증서 보유 웹 사이트와의 통신만 안전
- 웹 이외 통신 대처 X -> [[VPN]]

### SSL
- Secure Sockets Layer
- [[TCP]] / [[IP]] 계층 - 애플리케이션 계층 사이 위치
- 인증 · 암호화 · 무결성 보장
- [[인터페이스 보안]] 의 [[컴퓨터 네트워크|네트워크]] 영역 적용 방식 -> [[IPSec]] · [[S-HTTP]] 와 병렬
