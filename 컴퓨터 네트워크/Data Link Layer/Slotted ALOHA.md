---
aliases:
  - 슬롯 알로하
  - Slotted ALOHA(슬롯 알로하)
---

- 시간을 slot 으로 나눠 관리하는 [[ALOHA]]
- slot 시작 시점에만 전송 O

![[Medium-Access-Control-20.png]]

### 조건
- slot 은 frame 들어가기 충분한 크기
- Slot 간의 시작 시간 맞추기 -> time synchronization

### Vulnerable Time
- $T_{\text{fr}}$ -> [[Vulnerable Time]]
- 중간 시점에서 전송 시작하는 frame X -> 앞쪽 vulnerable time 소멸
- [[Pure ALOHA]] 의 $2T_{\text{fr}}$ 대비 $\frac{1}{2}$ 배

### Throughput
- $S = G \times e^{-G}$
- [[Pure ALOHA]] 의 $S = G \times e^{-2G}$ -> 지수 -2G 에서 -G 로
