---
aliases:
  - 비트 스터핑
  - Bit Stuffing(비트 스터핑)
---

- [[Variable-size Framing]] 에서 data 가 flag 로 오인되지 않도록 bit 삽입
- flag 제외, 1 이 연속 ==5 개== -> `0` stuffed bit 삽입
	- ==ex)== 1111110 → 11111`0`10
- 수신 측에서 원래대로 복원
