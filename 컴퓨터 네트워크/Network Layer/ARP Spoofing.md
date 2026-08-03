---
aliases:
  - ARP 스푸핑
  - ARP Spoofing(ARP 스푸핑)
---

- 위조된 [[ARP]] Reply 로 [[MAC Address|MAC 주소]] 속이는 공격
- ARP 인증 부재 + Host 는 수신한 답 무조건 신뢰 -> 공격 성립

### 형태
- Man-in-the-Middle(MITM) attack : 중간자가 [[Router|router]] 주소인 척 -> traffic 가로채기

### 대응
| 방안 | 내용 |
| --- | --- |
| DAI(Dynamic ARP Inspection) | 관리형 스위치에서 ARP packet 검사 -> 주소 변경 탐지 |
| static ARP | 중요 host 의 ARP table 정적 고정 |
