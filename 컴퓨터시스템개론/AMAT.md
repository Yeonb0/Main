---
aliases:
  - 평균 메모리 접근 시간
  - Average Memory Access Time
  - AMAT(Average Memory Access Time)
---

- Average [[메모리 주소 지정 방식|Memory Access]] Time, [[메모리 계층]] 의 평균 접근 시간 지표
- [[캐시 히트율]] 과 miss 비용을 하나의 값으로 종합

$$
\text{AMAT} = \text{HT} + \text{MR} \times \text{MP}
$$

### 구성
- Hit Time (HT)
	- cache data → CPU 도달 걸리는 시간
	- block 이 cache 에 있는지 판단하는 시간 포함
- Miss Penalty (MP)
	- miss 때문에 발생하는 추가 시간
- 시간 소요
	- [[캐시 히트]] : Hit Time
	- [[캐시 미스]] : Hit Time + MP

### 다단계 캐시
- [[다단계 캐시]] -> 하위 레벨의 AMAT 가 상위 레벨의 MP 역할

$$
\begin{align*}
\text{AMAT}_i &= \text{HT}_i + \text{MR}_i \times \text{MP}_i \\ 
              &= \text{HT}_i + \text{MR}_i \times \text{AMAT}_{i+1}
\end{align*}
$$
