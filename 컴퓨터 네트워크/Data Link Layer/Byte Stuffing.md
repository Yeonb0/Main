---
aliases:
  - 바이트 스터핑
  - Byte Stuffing(바이트 스터핑)
---

- byte 단위로 처리되는 시스템 대상 [[Variable-size Framing]] 보호 기법
	- ==ex)== [[PPP|PPP(Point-to-Point)]]
- marker (flag) → `7E`
- marker 제외 `7E` → `7D 5E`
- 원래 data 에서 `7D` → `7D 5D`
- 수신 측에서 원래대로 복원
