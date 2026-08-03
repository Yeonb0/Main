---
aliases:
  - 단편화
  - Fragmentation(단편화)
---

- [[MTU]] 초과 [[데이터]] -> 여러 조각으로 나눠 전송

### 절차
1. 나눠진 각 frame 마다 [[IP Header]] 부착
2. 최종 destination 에서 조립

### 특징
- 중간에 MTU 다시 커져도 재조립 X -> 최종 목적지에서만 조립
- 모든 fragment 도착해야 합침 -> 하나라도 누락 시 버림
- 관련 [[필드]] : Identification / Flag (D · M) / Fragmentation offset

### 예시
![[Internet-Protocol-(IP)-17.png]]
- fragment O & 마지막 fragment
- fragment X

![[Internet-Protocol-(IP)-18.png]]
- fragment O & 다음 fragment 존재

![[Internet-Protocol-(IP)-19.png]]
- fragment O & fragment offset 0

![[Internet-Protocol-(IP)-20.png]]
- Total length = header size 20 + payload 80 byte
- start 800 byte ~ end 879 byte
