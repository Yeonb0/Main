---
aliases:
  - 경로 MTU 탐색
  - Path MTU Discovery(경로 MTU 탐색)
---

- 경로상 최소 [[MTU]] 미리 파악 -> [[Fragmentation]] 없이 전송하는 방식

### 절차
1. D (do not fragment) = 1 설정 후 전송
2. 문제 발생 시 [[ICMP]] 가 "Fragmentation Needed" 회신
3. fragment size 줄여서 재확인
4. 모두 통과하는 size 로 잘라서 전송

### 특징
- 요즘 가장 많이 사용하는 protocol -> [[Ethernet]]
	- source 에서 ==1480== byte 씩 보내는 경우 多

![[Internet-Protocol-(IP)-21.png]]
