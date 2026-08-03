---
aliases:
  - 공정 큐잉
  - Fair Queueing(공정 큐잉)
---

- [[Round Robin]] 에 packet size $S_i$ 추가한 [[Scheduling]] 방식

### 절차
1. $S_i$ 초기값 0
2. packet 전송 시 그 크기 더하기
3. 여러 $S$ 중 작은 값 가진 [[queue]] 에서 전송 -> 더하기

- Tie break rule 지정 : A > B > C

![[Scheduling-and-Traffic-Shaping-06.png]]

### 단점
- $S$ 낮은 queue 가 한동안 혼자 전송 -> 독점
	- 해결 : ==use it or lose it== -> 가장 낮은 queue 전송 시 자신 이외 최소 $S$ 로 상향
- ==ex)== $S_1$ 150만 / $S_2$ 151만 / $S_3$ 2천

| 구분 | $S_3$ 값 | 결과 |
| --- | --- | --- |
| 적용 전 | 2천 ( 옛날 값 유지 ) | $S_3$ 가 150만까지 혼자 독점 |
| 적용 후 | 150만 ( $S_{min}$ 으로 끌어올림 ) | 처음부터 공평하게 경쟁 |

### 파생
- [[Weighted Fair Queueing]]
