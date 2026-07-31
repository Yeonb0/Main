---
aliases:
  - HARQ
  - Hybrid ARQ(HARQ)
  - 하이브리드 ARQ
---

- HARQ = [[ARQ]] + [[FEC]]

### 특징
- 기존 ARQ : [[Error]] 발견 -> frame 버리고 재전송 요청
- HARQ : Error 발견 -> error 난 frame 도 일단 저장
	- 재전송된 frame 과 합쳐서 복원 성공률 ↑ (soft combining)

### 사용
- 4G LTE, 5G NR
