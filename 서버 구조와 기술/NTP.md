---
aliases:
  - Network Time Protocol
  - NTP 서버
  - NTP(Network Time Protocol)
---

- 세계에서 시간을 동기화하는 [[프로토콜]]
- 상대 [[서버]]와 통신 [[Delay|지연]] 측정 -> 주고받는 시간 정보 보정 O
- 계층 구조 -> 시간 전달 방식 제어 O

### 계층 (stratum)
![[서버-운용을-알아보자-01.png]]
- 0 ~ 16 까지의 계층
- stratum0 : 원자 시계 or GPS 시간 같은 정확한 시간원
- 0 -> 1 -> 2 -> ... -> 16 으로 계층 구조 형성
