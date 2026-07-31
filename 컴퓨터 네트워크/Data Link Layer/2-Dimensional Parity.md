---
aliases:
  - 2차원 패리티
  - 2-Dimensional Parity(2차원 패리티)
---

- data 를 행 · 열로 [[배치 처리|배치]] -> row · column 각각에 [[Parity Bit]] 추가
- [[Simple Parity Check Code]] 확장 -> 검출 능력 ↑

![[Error-Detection-and-Correction-07.png]]

### 구조
- 28-bit -> 7 × 4 bit + 7 + 4 + 1
	- 7 : Column parity
	- 4 : Row parity

![[Error-Detection-and-Correction-08.png]]

### 성능
- [[Error Detection]] -> 1, 2, 3-bit 까지 O
	- 4-bit error : 대부분 O, but 발견 불가능 경우 有

![[Error-Detection-and-Correction-09.png]]

	-> 오류가 2개씩 같은 row, column 일 때
- [[Error Correction]] -> 1-bit O
- overhead ↑ -> detection 능력 ↑
