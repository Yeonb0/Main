---
aliases:
  - 흐름 제어
  - Flow Control(흐름 제어)
---

- receiver 에 무리 없도록 sender 전송 속도 조절
- [[TCP Header]] 의 Window size 로 receiver 남은 공간 추정

### 특징
- 16 bit -> ==0 ~ 65535 byte==
- TCP option (Window scale) 로 배수 지정 O
	- n -> $2^n$ 만큼 곱하기

![[Transport-Layer-19.png]]

- 전송 단위 상한 -> [[MSS]]
- 대응 개념 -> [[Congestion Control]]
