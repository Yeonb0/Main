---
aliases:
  - Byte Extension
  - movz
  - movs
  - 바이트 확장 명령어
---

- [[비트 확장]] 수행하는 [[데이터]] 이동 명령어
- 접미사로 extend 할 byte 표시

### 종류
- `movz` : zero extension
	- ==ex)== `movzbw` : zero extension (byte 1 -> word 2)
- `movs` : sign extension
	- ==ex)== `movslq` : sign extension (long 4 -> quad 8)
