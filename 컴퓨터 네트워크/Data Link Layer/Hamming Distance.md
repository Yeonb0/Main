---
aliases:
  - 해밍 거리
  - Hamming Distance(해밍 거리)
---

- 어떤 두 codeword 사이 다른 bit 의 수
- 두 codeword XOR 결과의 1 갯수와 동일

### 예시
- d(000, 000) = 0
- d(000, 011) = 2
- d(0100, 0010) = 2
- d(10101, 11110) = 3

### 활용
- codeword set 전체 -> [[Minimum Hamming Distance]] -> 검출 · 수정 능력 결정
